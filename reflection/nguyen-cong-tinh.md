# Reflection — Nguyễn Công Tĩnh

> Đội trưởng nhóm NoName · L3A · H209 · Zone 3 · Track D1 (yêu cầu hủy đơn ShopeeFood đã thanh toán).

1. **Vai trò + phần mình làm (trỏ tới file / commit):**
   - Đội trưởng: giữ repo, chia việc theo cặp ở CP2–CP4, nộp 4 checkpoint bằng mã `2A202603373`.
   - Bản chạy thử: `codebase/tools.py` (7 công cụ, `check_cancel` áp luật P1–P7 và T1, tính tiền hoàn bằng code), `codebase/agent.py` (workflow cố định, `check_llm` kiểm chữ model), nối OpenAI `gpt-5.4-nano` trong `codebase/ai.py`, data giả lập `data/make_orders.py` (seed 15, 17 đơn). Commit chính: `acee21e`, `199dc8b`, `053c1ae`. Viết `spec.md` §4.
   - Đo đạc: chạy lượt 1 (`run-1@20261127-233849`, 17/25) và lượt 2 (`run-2@20261128-024240`, 18/25), áp cải tiến nhóm lỗi A (`3b99ff8`), chạy mô phỏng chi phí `simulate-1`, `simulate-2` (50 phiên). Video CP3 và video demo dự phòng.
   - Demo: `demo-slides.pdf` (`65d13ef`), giao diện web `codebase/web.py` + `codebase/web_ui.html` (`304e52a`, `14661aa`, có nút tạo đơn thử cho giám khảo).

2. **AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):**
   - Mình dùng **Claude** để viết phần lớn code ở trên, phần lớn `spec.md` §4 và §8, `cost/cost-estimate.md`, slide trang 4–8 và giao diện web. Mình chạy lại từng lần, kiểm kết quả và quyết định có dùng hay không. Khoa dùng Codex audit code của mình.
   - Chỗ phải sửa: bản đầu đọc luật P1 theo "và" nhưng tài liệu nhóm ghi "hoặc"; câu trả lời hứa "hoàn trong 1–3 ngày" trong khi P5 chỉ nói 1–3 ngày là thời gian *kiểm tra giao dịch*; luật T1 áp cả khi tài xế đang giao; tự chọn đơn khi khách không nêu mã. Các lỗi này do Khoa audit bằng Codex phát hiện, mình chốt cách đọc luật (giữ "và" vì P2 chặn hủy khi quán đã xác nhận) rồi cho sửa (`199dc8b`).
   - Bài học khi dùng AI: AI viết code chạy được rất nhanh, nhưng **cách hiểu luật là việc của nhóm**. Mình phải đọc từng quyết định AI chọn trong code chứ không chỉ xem nó chạy hay không.

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
   - **B01** — khách: "Hủy giúp mình đơn SF1001, chờ lâu quá". Ở lượt 1, code tính đúng (cho hủy, hoàn 88.000đ) và bản nháp code viết đúng "ShopeeFood kiểm tra giao dịch trong 1–3 ngày làm việc", nhưng **model viết lại thành hoàn tiền "trong 1–3 ngày"** — một lời hứa ShopeeFood không đưa ra. `check_llm` lúc đó không bắt vì câu không chứa từ cấm.
   - Bài học: header đúng chưa đủ, **phần chữ model viết lại cũng có thể hứa sai về tiền**. Ở lượt 2 nhóm cho `check_llm` chặn mọi câu hứa thời điểm tiền về và câu làm rơi dữ kiện của bản nháp: B01 hết hứa sai, nhưng vẫn trượt vì thiếu phân biệt P4, và B04 lại tệ đi. Sửa một nhóm lỗi có thể làm hỏng câu khác, nên luôn phải **chạy lại trọn bộ 25 câu** và chấm như cũ, không chỉ chạy lại câu đang sửa.
