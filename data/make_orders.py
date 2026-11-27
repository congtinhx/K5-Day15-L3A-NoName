"""Sinh data đơn hàng GIẢ LẬP (synthetic) cho bản chạy thử — nhóm NoName.

Chạy: python data/make_orders.py  → ghi data/orders.json và data/users.json
Seed cố định (SEED = 15) nên chạy lại ra đúng cùng file.
Mọi tên quán / khách / mã đơn là GIẢ ("Quán Mẫu …", "Khách Mẫu …"). Không có đơn thật.

Mỗi đơn được dựng để phủ một trạng thái/luật (P1–P7, T1) — xem cột "kich_ban".
Giờ "hiện tại" của sandbox cố định: NOW (Thứ Sáu 27/11/2026 19:00) để kết quả lặp lại được.
"""
import json
import os
import random

SEED = 15
NOW = "2026-11-27T19:00"
HERE = os.path.dirname(os.path.abspath(__file__))

rng = random.Random(SEED)


def money():
    """Tổng tiền đơn: 35.000–180.000đ, bội số 1.000 (seed)."""
    return rng.randrange(35, 181) * 1000


# (mã đơn, user, trạng thái, giờ đặt, giờ dự kiến giao, thanh toán, thêm, kịch bản)
SPEC = [
    ("SF1001", "U01", "cho_xac_nhan", "2026-11-27T18:50", "2026-11-27T19:25", "shopeepay", {}, "P1: còn hủy được"),
    ("SF1002", "U01", "quan_da_xac_nhan", "2026-11-27T18:40", "2026-11-27T19:20", "the", {}, "P2: quán đã xác nhận, chưa trễ"),
    ("SF1003", "U01", "tai_xe_da_nhan", "2026-11-27T17:40", "2026-11-27T18:25", "shopeepay", {}, "T1: trễ 35 phút > 30"),
    ("SF1004", "U01", "dang_giao", "2026-11-27T17:50", "2026-11-27T18:31", "shopeepay", {}, "T1 biên: trễ 29 phút"),
    ("SF1005", "U01", "da_huy", "2026-11-23T11:30", "2026-11-23T12:10", "shopeepay",
     {"gio_huy": "2026-11-23T12:00", "hoan_tien": "chua_hoan"}, "P5: hủy 4 ngày làm việc chưa hoàn"),
    ("SF1006", "U01", "da_huy", "2026-11-26T19:30", "2026-11-26T20:10", "the",
     {"gio_huy": "2026-11-26T20:00", "hoan_tien": "chua_hoan"}, "P5: hủy hôm qua, đang trong 1–3 ngày"),
    ("SF1007", "U01", "da_giao", "2026-11-27T03:20", "2026-11-27T04:00", "shopeepay",
     {"gio_giao": "2026-11-27T04:00"}, "P7: giao 15 tiếng trước, quá 12h"),
    ("SF1008", "U01", "da_giao", "2026-11-27T17:20", "2026-11-27T18:00", "shopeepay",
     {"gio_giao": "2026-11-27T18:00"}, "giao 1 tiếng trước (ca ngộ độc / khiếu nại món)"),
    ("SF1009", "U01", "cho_xac_nhan", "2026-11-27T18:55", "2026-11-27T19:30", "tien_mat", {}, "P1: tiền mặt, không cần hoàn"),
    ("SF2001", "U02", "cho_xac_nhan", "2026-11-27T18:52", "2026-11-27T19:30", "shopeepay", {}, "P6: khách đã hủy 2 đơn"),
    ("SF3001", "U03", "cho_xac_nhan", "2026-11-27T18:45", "2026-11-27T19:20", "shopeepay", {}, "2 đơn đang chạy (1)"),
    ("SF3002", "U03", "quan_da_xac_nhan", "2026-11-27T18:30", "2026-11-27T19:10", "shopeepay", {}, "2 đơn đang chạy (2)"),
    ("SF4001", "U04", "cho_xac_nhan", "2026-11-27T18:50", "2026-11-27T19:30", "shopeepay", {}, "đơn của người khác"),
]

orders = {}
for i, (oid, uid, status, placed, eta, pay, extra, scenario) in enumerate(SPEC, 1):
    total = money()
    o = {
        "order_id": oid,
        "user_id": uid,
        "quan": "Quán Mẫu %d" % (rng.randrange(1, 30)),
        "trang_thai": status,
        "gio_dat": placed,
        "gio_du_kien": eta,
        "tong_tien": total,
        "thanh_toan": pay,
        "xu_da_dung": rng.choice([0, 0, 500, 1000]),
        "ma_khuyen_mai": rng.choice([None, "GIAMMAU10K", "FREESHIPMAU"]),
        "kich_ban": scenario,
        "label": "synthetic",
    }
    o.update(extra)
    orders[oid] = o

users = {
    "U01": {"ten": "Khách Mẫu 1", "so_don_huy_khong_ly_do_30_ngay": 0, "label": "synthetic"},
    "U02": {"ten": "Khách Mẫu 2", "so_don_huy_khong_ly_do_30_ngay": 2, "label": "synthetic"},
    "U03": {"ten": "Khách Mẫu 3", "so_don_huy_khong_ly_do_30_ngay": 0, "label": "synthetic"},
    "U04": {"ten": "Khách Mẫu 4", "so_don_huy_khong_ly_do_30_ngay": 1, "label": "synthetic"},
}

meta = {"seed": SEED, "now": NOW, "label": "synthetic", "version": "v1 · 27/11/2026"}
with open(os.path.join(HERE, "orders.json"), "w", encoding="utf-8") as f:
    json.dump({"meta": meta, "orders": orders}, f, ensure_ascii=False, indent=2)
with open(os.path.join(HERE, "users.json"), "w", encoding="utf-8") as f:
    json.dump({"meta": meta, "users": users}, f, ensure_ascii=False, indent=2)
print("Đã ghi %d đơn, %d khách (seed %d)" % (len(orders), len(users), SEED))
