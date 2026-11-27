"""Công cụ của bài toán — nhóm NoName · lát cắt: yêu cầu hủy đơn ShopeeFood đã thanh toán.

Mỗi công cụ một hàm có @tool. Docstring: tên · input · output · có tác động ra ngoài không.
Dữ liệu đọc từ data/orders.json, data/users.json (GIẢ LẬP, seed 15 — xem data/DATA_CARD.md).
Công cụ có tác động ra ngoài (cancel_order, escalate_to_human) KHÔNG làm thật: chỉ tạo bản nháp / ticket giả.

Luật (spec.md §4, nguồn: Trung tâm Trợ giúp ShopeeFood, xem 27/11/2026):
  P1 tự hủy được khi quán chưa xác nhận làm món hoặc chưa có tài xế nhận đơn.
     Đọc cùng P2 (nút hủy mờ khi quán ĐÃ xác nhận HOẶC tài xế đang giao): nếu một trong hai việc đã xảy ra
     thì P2 chặn. Vì vậy chỉ hủy được khi CẢ HAI chưa xảy ra = trạng thái cho_xac_nhan. Đây là cách nhóm
     ghép P1+P2 để không mâu thuẫn — xem spec.md §4.
  P2 quán đã xác nhận / tài xế đã nhận / đang giao → không hủy được, đề nghị tiếp tục đơn
  P3 quán làm món lâu → đề nghị chờ thêm
  P4 hủy vì đổi ý → không hoàn tiền, Shopee Xu, mã khuyến mãi
  P5 tiền đã trừ mà đơn chưa hoàn thành → kiểm tra 1–3 ngày làm việc, hoàn về phương thức gốc
  P6 hủy quá 2 đơn không lý do chính đáng → khóa tài khoản vĩnh viễn
  P7 khiếu nại đơn chỉ nhận trong 12 tiếng
  T1 (TỰ ĐẶT) quán trễ > 30 phút so với giờ dự kiến → chuyển nhân viên xem xét cho hủy.
     Chỉ áp khi món còn ở quán (quan_da_xac_nhan, tai_xe_da_nhan); đang giao thì không áp.
"""
import datetime as dt
import itertools
import json
import os

from tracing import tool, TOOLS  # noqa: F401

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")

LATE_MIN = 30          # T1 (tự đặt)
REFUND_DAYS = 3        # P5: 1–3 ngày làm việc
COMPLAINT_HOURS = 12   # P7
CANCEL_LIMIT = 2       # P6

POLICY = {
    "P1": "Khách tự hủy được khi quán chưa xác nhận làm món và chưa có tài xế nhận đơn.",
    "P2": "Quán đã xác nhận/chuẩn bị món hoặc tài xế đang giao thì không hủy được; ShopeeFood đề nghị khách tiếp tục đơn.",
    "P3": "Quán làm món lâu thì ShopeeFood đề nghị khách chờ thêm.",
    "P4": "Hủy vì đổi ý (đổi món, thời gian, thông tin) thì không được hoàn tiền, Shopee Xu và mã khuyến mãi.",
    "P5": "Đơn đã trừ tiền mà chưa hoàn thành: ShopeeFood kiểm tra giao dịch trong 1–3 ngày làm việc và hoàn về phương thức thanh toán ban đầu (không cam kết tiền về trong 1–3 ngày).",
    "P6": "Hủy quá 2 đơn không có lý do chính đáng có thể bị khóa tài khoản vĩnh viễn.",
    "P7": "Khiếu nại về đơn hàng chỉ được tiếp nhận trong 12 tiếng.",
    "T1": "(Quy định tự đặt của nhóm) Quán trễ hơn 30 phút so với giờ dự kiến, món còn ở quán, thì chuyển nhân viên xem xét cho hủy.",
}

ACTIVE = {"cho_xac_nhan", "quan_da_xac_nhan", "tai_xe_da_nhan", "dang_giao"}
BLOCKED = {"quan_da_xac_nhan", "tai_xe_da_nhan", "dang_giao"}
AT_SHOP = {"quan_da_xac_nhan", "tai_xe_da_nhan"}   # T1 chỉ áp khi món còn ở quán
PREPAID = {"shopeepay", "the"}
_ticket = itertools.count(1)


def _load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return json.load(f)


def _t(s):
    return dt.datetime.fromisoformat(s)


def now():
    """Giờ 'hiện tại' của sandbox (cố định trong data để kết quả lặp lại được)."""
    return _t(_load("orders.json")["meta"]["now"])


def business_days_between(start, end):
    """Số ngày làm việc (T2–T6) trọn vẹn đã qua sau ngày `start` đến hết ngày `end`."""
    d, n = start.date(), 0
    while d < end.date():
        d += dt.timedelta(days=1)
        if d.weekday() < 5:
            n += 1
    return n


@tool
def get_order(order_id: str) -> dict:
    """get_order · Input: mã đơn (str, vd "SF1001").
    Output: dict đơn hàng (trạng thái, giờ đặt, giờ dự kiến, tổng tiền, thanh toán, Xu, mã KM…) hoặc {} nếu không có.
    Chỉ đọc — không tác động ra ngoài."""
    return dict(_load("orders.json")["orders"].get((order_id or "").upper(), {}))


@tool
def list_active_orders(user_id: str) -> list:
    """list_active_orders · Input: user_id. Output: danh sách mã đơn đang chạy của khách.
    Chỉ đọc — không tác động ra ngoài. Dùng khi khách không nêu mã đơn."""
    orders = _load("orders.json")["orders"].values()
    return [o["order_id"] for o in orders if o["user_id"] == user_id and o["trang_thai"] in ACTIVE]


@tool
def get_cancel_history(user_id: str) -> dict:
    """get_cancel_history · Input: user_id. Output: {"so_don_huy_khong_ly_do_30_ngay": int}.
    Chỉ đọc — không tác động ra ngoài."""
    u = _load("users.json")["users"].get(user_id, {})
    return {"so_don_huy_khong_ly_do_30_ngay": int(u.get("so_don_huy_khong_ly_do_30_ngay", 0))}


@tool
def get_policy(codes: list) -> dict:
    """get_policy · Input: danh sách mã luật (vd ["P1","P5"]). Output: {mã: nội dung luật}.
    Chỉ đọc — không tác động ra ngoài."""
    return {c: POLICY[c] for c in codes if c in POLICY}


@tool
def check_cancel(order: dict, user_id: str, reason: str, flags: dict, history: dict, now_s: str) -> dict:
    """check_cancel (CODE, không phải model) · Input: đơn, user_id, lý do đã phân loại, cờ an toàn, lịch sử hủy, giờ hiện tại.
    Output: {"quyet_dinh": cho_huy|tu_choi|hoi_them|chuyen_nguoi|thong_tin, "hoan_tien": int đ, "hoan_xu": bool,
             "hoan_ma": bool, "luat": [mã luật], "ly_do": str, "canh_bao": [str], "du_kien": str|None}
    Không tác động ra ngoài. Mọi phép tính tiền và kiểm trạng thái nằm ở đây."""
    t_now = _t(now_s)
    d = {"quyet_dinh": None, "hoan_tien": 0, "hoan_xu": False, "hoan_ma": False,
         "luat": [], "ly_do": "", "canh_bao": [], "du_kien": None}

    def out(q, ly_do, luat, **kw):
        d.update(quyet_dinh=q, ly_do=ly_do, luat=luat, **kw)
        return d

    # 0. An toàn sức khỏe — chuyển ngay, trước mọi luật khác
    if flags.get("suc_khoe"):
        return out("chuyen_nguoi", "Có dấu hiệu ngộ độc / dị ứng — chuyển nhân viên ngay.", [])

    # 1. Tấn công / tự xưng nhân viên: không đổi luật, từ chối phần đòi vượt quy định
    if flags.get("tan_cong") or flags.get("tu_xung_nhan_vien"):
        return out("tu_choi", "Yêu cầu bỏ qua quy định hoặc tự xưng nhân viên không được chấp nhận; "
                   "hệ thống chỉ xử lý theo quy định hủy đơn.", ["P1", "P2"])

    # 2. Bị trừ tiền mà không có đơn
    if reason == "tru_tien_khong_don":
        return out("chuyen_nguoi", "Tiền bị trừ nhưng không tìm thấy đơn — cần nhân viên kiểm tra giao dịch.", ["P5"])

    # 3. Không có đơn / không phải đơn của khách
    if not order:
        return out("hoi_them", "Chưa có mã đơn hợp lệ.", [])
    if order["user_id"] != user_id:
        return out("tu_choi", "Đơn này không thuộc tài khoản đang đăng nhập — không thể thao tác.", [])

    status = order["trang_thai"]
    total = int(order["tong_tien"])
    prepaid = order["thanh_toan"] in PREPAID

    # 4. Đòi tiền vượt giá trị đơn / bồi thường thêm → người duyệt
    req = flags.get("so_tien_yeu_cau") or 0
    if flags.get("doi_boi_thuong") or req > total:
        return out("chuyen_nguoi", "Yêu cầu số tiền/bồi thường vượt giá trị đơn (%s) — ngoài thẩm quyền tự động."
                   % vnd(total), ["P5"])

    # 5. Đơn đã hủy — hỏi tiền hoàn
    if status == "da_huy":
        if not prepaid or order.get("hoan_tien") == "da_hoan":
            return out("thong_tin", "Đơn đã hủy và không còn khoản chờ hoàn.", ["P5"])
        n = business_days_between(_t(order["gio_huy"]), t_now)
        if n > REFUND_DAYS:
            return out("chuyen_nguoi", "Đơn đã hủy %d ngày làm việc mà chưa hoàn (quá %d ngày)." % (n, REFUND_DAYS), ["P5"])
        return out("thong_tin", "Đơn đã hủy %d ngày làm việc, vẫn trong hạn hoàn 1–3 ngày làm việc." % n, ["P5"])

    # 6. Đơn đã giao
    if status == "da_giao":
        hours = (t_now - _t(order["gio_giao"])).total_seconds() / 3600
        if hours > COMPLAINT_HOURS:
            return out("tu_choi", "Đơn đã giao %.0f tiếng trước, quá hạn khiếu nại 12 tiếng." % hours, ["P7"])
        return out("tu_choi", "Đơn đã giao, không hủy được. Nếu món có vấn đề, gửi khiếu nại trong 12 tiếng.", ["P7"])

    # 7. Thiếu lý do — lý do quyết định số tiền hoàn
    if not reason:
        return out("hoi_them", "Cần biết lý do hủy để báo đúng số tiền hoàn (đổi ý thì không hoàn).", ["P4"])

    # 8. Đơn chưa xác nhận → cho hủy (P1)
    if status == "cho_xac_nhan":
        warn = []
        if history.get("so_don_huy_khong_ly_do_30_ngay", 0) >= CANCEL_LIMIT and reason == "doi_y":
            warn.append("Bạn đã hủy %d đơn không lý do chính đáng; hủy thêm có thể bị khóa tài khoản vĩnh viễn (P6)."
                        % history["so_don_huy_khong_ly_do_30_ngay"])
        if reason == "doi_y":
            return out("cho_huy", "Đơn chưa được quán xác nhận nên hủy được; lý do đổi ý nên không hoàn tiền, Xu, mã.",
                       ["P1", "P4"] + (["P6"] if warn else []), canh_bao=warn)
        refund = total if prepaid else 0
        return out("cho_huy", "Đơn chưa được quán xác nhận nên hủy được.", ["P1", "P5"] if prepaid else ["P1"],
                   hoan_tien=refund, canh_bao=warn)

    # 9. Quán đã xác nhận / tài xế đã nhận / đang giao
    if status in BLOCKED:
        eta = _t(order["gio_du_kien"])
        late = (t_now - eta).total_seconds() / 60
        if late > LATE_MIN and status in AT_SHOP:
            return out("chuyen_nguoi", "Đơn trễ %d phút so với giờ dự kiến (> %d phút)." % (late, LATE_MIN), ["T1", "P2"])
        luat = ["P2"] + (["P3"] if reason == "cho_lau" else []) + (["P4"] if reason == "doi_y" else [])
        return out("tu_choi", "Quán đã xác nhận hoặc tài xế đã nhận đơn nên không hủy được.", luat,
                   du_kien=order["gio_du_kien"][11:16])

    return out("chuyen_nguoi", "Trạng thái đơn không rõ (%s)." % status, [])


@tool
def cancel_order(order_id: str) -> dict:
    """cancel_order (GIẢ LẬP) · Input: mã đơn. Output: {"trang_thai": "ban_nhap_cho_khach_xac_nhan"}.
    CÓ tác động ra ngoài và khó đảo ngược → KHÔNG hủy thật; chỉ tạo bản nháp chờ khách bấm xác nhận."""
    return {"order_id": order_id, "trang_thai": "ban_nhap_cho_khach_xac_nhan"}


@tool
def escalate_to_human(order_id: str, reason: str) -> dict:
    """escalate_to_human (GIẢ LẬP) · Input: mã đơn, lý do. Output: {"ticket": "TK-…"}.
    Có tác động ra ngoài (tạo ticket cho nhân viên) — đảo ngược được; trong sandbox chỉ sinh mã ticket giả."""
    return {"ticket": "TK-%04d" % next(_ticket), "order_id": order_id, "ly_do": reason}


def vnd(x):
    return "{:,}đ".format(int(x)).replace(",", ".")
