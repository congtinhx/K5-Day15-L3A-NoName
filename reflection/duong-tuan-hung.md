# Reflection — Dương Tuấn Hưng

Nhóm NoName · Ngày 28/11/2026. Reflection cá nhân, được AI hỗ trợ tổng hợp từ hồ sơ và lịch sử commit của dự án và đã được Dương Tuấn Hưng rà duyệt.

## 1. Vai trò và phần việc đã làm

Thành viên nhóm NoName (Cặp 1 cùng Nguyễn Công Tĩnh), phụ trách thu thập bằng chứng pain, rà soát rủi ro/an toàn và nội dung mở đầu slide.
Đào 220 review 1–2★ bằng [count_reviews.js](../evidence/count_reviews.js), đọc tay 35 review ứng viên (chốt 34/220 = 15,5%, loại `R2-060`) tại [data-mining.md](../evidence/data-mining.md) và [canvas.md](../canvas.md) (`4e63ad0`).
Triển khai khảo sát ẩn danh `n=20` tại [questions.md](../evidence/survey/questions.md) và [results.csv](../evidence/survey/results.csv) (`e329397`).
Viết giải pháp tương tự [spec.md §3](../spec.md) (`7beb65e`), hoàn thiện bốn đường đi trải nghiệm [spec.md §6](../spec.md) và đối chiếu bằng chứng [summary.md](../evidence/summary.md) (`97a5a6c`).
Hoàn thiện rủi ro & an toàn [spec.md §9](../spec.md), soạn nội dung slide trang 1–3 tại [slides-1-3.md](../slides/slides-1-3.md) và cập nhật [ai-usage.md](../docs/ai-usage.md) (`7448aa0`).

## 2. AI hỗ trợ như thế nào

Sử dụng Antigravity (Gemini) hỗ trợ tổng hợp dữ liệu sẵn có trong repo để soạn [spec.md §9](../spec.md), bản thảo [slides-1-3.md](../slides/slides-1-3.md) và rà soát tính nhất quán qua `python run.py check`.
Mọi số liệu bằng chứng đều được tự kiểm chứng lại: sau khi lọc bằng script từ khóa, phải đọc tay toàn bộ 35 review ứng viên để loại câu bắt nhầm `R2-060` ("hủy app") và bổ sung 6 câu phản ánh không hủy được bị regex bỏ sót (17 → 23).
Khi dùng AI soạn tài liệu CP4, rà lại để giữ nguyên các mục chưa xác nhận trong [ai-usage.md](../docs/ai-usage.md) và phân biệt rõ số đếm thật với số `*(tự ước tính)*` trên slide trang 2.
Giữ nguyên tắc không để AI tạo dữ liệu giả cho phần kiểm chứng người dùng (`validation/log.md`) hay tự điền thông tin chưa có nguồn.

## 3. Một câu thử trượt và bài học

Chọn câu **B08** (chuyển thể từ review `R1-110` trong tập review nhóm đã đào): khách `U02` đổi ý hủy `SF2001` và hỏi hủy thêm có ảnh hưởng tài khoản không.
Ở lượt 1 (`run-1@20261127-233849`), code cho hủy đúng và cảnh báo đúng hướng theo P6 nhưng model viết lại làm rơi dữ kiện "2 lần hủy trong 30 ngày" dù công cụ đã trả về.
Sang lượt 2 (`run-2@20261128-024240`), sau khi thêm hậu kiểm `facts()` trong `check_llm`, output nêu được "2 lần hủy" nhưng vẫn trượt vì thiếu mốc "30 ngày" và diễn đạt khoản không hoàn khó hiểu ([report.md](../eval/report.md)).
Bài học: code quyết định đúng và tra đủ dữ liệu vẫn chưa đủ nếu lớp diễn đạt làm rơi điều kiện bắt buộc; cần khóa rõ các mốc số liệu (2 lần / 30 ngày) ngay trong bản nháp và hậu kiểm thay vì chỉ nhắc trong prompt.
