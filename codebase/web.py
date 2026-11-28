"""Giao diện web cho bản chạy thử — nhóm NoName.

Chạy:   python codebase/web.py            → mở http://127.0.0.1:8000
        python codebase/web.py --port 8080

- Gọi ĐÚNG hàm answer() trong agent.py (cùng luồng với `python run.py` và `run.py eval`),
  nên kết quả trên giao diện giống kết quả đã đánh giá.
- Dùng .env như khung (MODEL_PROVIDER, MODEL_NAME, API_KEY). Chưa có .env thì chạy chế độ giả.
- Chỉ dùng thư viện chuẩn Python. Chỉ mở trên máy mình (127.0.0.1), không mở ra mạng ngoài.
- Không phải file khung: `python run.py` vẫn là bản dòng lệnh như cũ.
"""
import json
import os
import sys
import threading
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import tracing          # noqa: E402
import tools            # noqa: E402
from agent import answer, LABEL  # noqa: E402
from ai import MODEL_PROVIDER, MODEL_NAME  # noqa: E402

LOCK = threading.Lock()   # tracing dùng biến toàn cục → xử lý từng câu một
EXTRA = {}                # đơn thử tạo từ giao diện: chỉ trong bộ nhớ, tắt server là mất, không ghi file

_orig_load = tools._load


def _load_with_extra(name):
    data = _orig_load(name)
    if name == "orders.json" and EXTRA:
        data = dict(data, orders=dict(data["orders"], **EXTRA))
    return data


tools._load = _load_with_extra   # get_order / list_active_orders thấy cả đơn thử
CODE_OF = {v: k for k, v in LABEL.items()}


def load_json(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf-8") as f:
        return json.load(f)


def parse_output(out):
    """Tách dòng QUYẾT ĐỊNH (code in) thành các trường để giao diện hiển thị."""
    lines = out.splitlines()
    head, body = (lines[0] if lines else ""), "\n".join(lines[1:]).strip()
    info = {"quyet_dinh": "", "nhan": "", "fields": {}}
    parts = [p.strip() for p in head.split(" · ")]
    if parts and parts[0].startswith("QUYẾT ĐỊNH:"):
        label = parts[0].split(":", 1)[1].strip()
        info["nhan"] = label
        info["quyet_dinh"] = CODE_OF.get(label, "")
        for p in parts[1:]:
            if p.startswith("Đơn "):
                info["fields"]["don"] = p[4:]
            elif ":" in p:
                k, v = p.split(":", 1)
                info["fields"][k.strip()] = v.strip()
    return head, body, info


def ask(text, user):
    text = (text or "").strip()
    if user and user != "U01" and not text.startswith("["):
        text = "[%s] %s" % (user, text)
    with LOCK:
        t0 = time.perf_counter()
        tracing.begin("web")
        try:
            res = answer(text)
            err = None
        except Exception as e:  # lỗi gọi model: trả về cho giao diện, không sập server
            res, err = {"output": ""}, "%s: %s" % (type(e).__name__, e)
        summary, events = tracing.end()
        latency = round(time.perf_counter() - t0, 2)
    out = res.get("output", "") if isinstance(res, dict) else str(res)
    head, body, info = parse_output(out)
    return {"input": text, "output": out, "head": head, "body": body, "info": info,
            "summary": summary, "events": events, "latency_s": latency, "error": err}


def create_order(req):
    """Tạo đơn thử theo mô tả của giám khảo. Giờ tính tương đối so với giờ sandbox."""
    import datetime as dt
    now = dt.datetime.fromisoformat(load_json("orders.json")["meta"]["now"])
    st = req.get("trang_thai") or "cho_xac_nhan"
    if st not in ("cho_xac_nhan", "quan_da_xac_nhan", "tai_xe_da_nhan", "dang_giao", "da_giao", "da_huy"):
        raise ValueError("trạng thái không hợp lệ")
    user = req.get("user_id") or "U01"
    if user not in load_json("users.json")["users"]:
        raise ValueError("khách không hợp lệ")
    total = int(req.get("tong_tien") or 0)
    if not 1000 <= total <= 10_000_000:
        raise ValueError("tổng tiền 1.000–10.000.000đ")
    pay = req.get("thanh_toan") or "shopeepay"
    if pay not in ("shopeepay", "the", "tien_mat"):
        raise ValueError("thanh toán không hợp lệ")
    oid = "SF%d" % (9001 + len(EXTRA))
    fmt = lambda t: t.strftime("%Y-%m-%dT%H:%M")
    o = {"order_id": oid, "user_id": user, "quan": "Quán Thử", "trang_thai": st, "tong_tien": total,
         "thanh_toan": pay, "xu_da_dung": 0, "ma_khuyen_mai": None, "label": "synthetic", "tam": True}
    if st == "da_huy":
        days = int(req.get("so_ngay") or 1)
        cancel = now - dt.timedelta(days=days)
        o.update(gio_dat=fmt(cancel - dt.timedelta(minutes=30)), gio_du_kien=fmt(cancel + dt.timedelta(minutes=10)),
                 gio_huy=fmt(cancel), hoan_tien="chua_hoan", kich_ban="Đơn thử: đã hủy cách đây %d ngày, chưa hoàn" % days)
    elif st == "da_giao":
        hours = float(req.get("so_gio") or 1)
        done = now - dt.timedelta(hours=hours)
        o.update(gio_dat=fmt(done - dt.timedelta(minutes=40)), gio_du_kien=fmt(done), gio_giao=fmt(done),
                 kich_ban="Đơn thử: đã giao cách đây %g tiếng" % hours)
    else:
        late = int(req.get("tre_phut") or 0)
        eta = now - dt.timedelta(minutes=late)
        o.update(gio_dat=fmt(eta - dt.timedelta(minutes=40)), gio_du_kien=fmt(eta),
                 kich_ban="Đơn thử: " + ("trễ %d phút so với giờ dự kiến" % late if late > 0 else
                                          "còn %d phút nữa mới tới giờ dự kiến" % -late if late < 0 else "đúng giờ dự kiến"))
    EXTRA[oid] = o
    return o


def bootstrap():
    o, u = tools._load("orders.json"), load_json("users.json")
    return {"now": o["meta"]["now"], "orders": list(o["orders"].values()), "users": u["users"],
            "policy": tools.POLICY, "provider": MODEL_PROVIDER,
            "model": MODEL_NAME if MODEL_PROVIDER != "fake" else "chế độ giả (chưa nối model)"}


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        data = body if isinstance(body, bytes) else body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            with open(os.path.join(HERE, "web_ui.html"), encoding="utf-8") as f:
                return self._send(200, f.read(), "text/html; charset=utf-8")
        if self.path == "/api/bootstrap":
            return self._send(200, json.dumps(bootstrap(), ensure_ascii=False))
        return self._send(404, '{"error":"not found"}')

    def do_POST(self):
        if self.path == "/api/order":
            n = int(self.headers.get("Content-Length") or 0)
            try:
                o = create_order(json.loads(self.rfile.read(n).decode("utf-8") or "{}"))
            except (ValueError, TypeError) as e:
                return self._send(400, json.dumps({"error": str(e)}, ensure_ascii=False))
            return self._send(200, json.dumps(o, ensure_ascii=False))
        if self.path != "/api/ask":
            return self._send(404, '{"error":"not found"}')
        n = int(self.headers.get("Content-Length") or 0)
        try:
            req = json.loads(self.rfile.read(n).decode("utf-8") or "{}")
        except ValueError:
            return self._send(400, '{"error":"bad json"}')
        if not (req.get("text") or "").strip():
            return self._send(400, '{"error":"empty"}')
        return self._send(200, json.dumps(ask(req.get("text"), req.get("user") or "U01"), ensure_ascii=False))

    def log_message(self, fmt, *args):  # gọn terminal khi demo
        if self.command == "POST":
            sys.stdout.write("  [%s] %s\n" % (time.strftime("%H:%M:%S"), fmt % args))


def main(argv):
    port = 8000
    if "--port" in argv:
        port = int(argv[argv.index("--port") + 1])
    srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    url = "http://127.0.0.1:%d" % port
    print("Giao diện demo: %s   (model: %s)" % (url, bootstrap()["model"]))
    print("Dừng: Ctrl+C")
    if "--no-browser" not in argv:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nĐã dừng.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
