# Reflection — Trần Đăng Khoa

Nhóm NoName · K5-L3A · Track D1 · 28/11/2026
Đề tài: Hỗ trợ hủy đơn ShopeeFood đã thanh toán trước. 

## 1. Vai trò và phần việc đã làm

- Phụ trách benchmark và đánh giá. Ở CP2, viết câu thử, tiêu chí chấm từng câu, bốn metric và Data Card, tham gia hiệu chuẩn cách chấm và chuẩn bị phần chuẩn đạt ở §7 (`204bcc8`). Nhóm chốt chuẩn ở `4c54b26`.
- Ở CP3, tôi mở rộng [benchmark](../eval/benchmark.csv) từ 15 lên 25 câu, giữ nguyên các câu đã khóa. Bộ cuối có 5 câu thường, 18 câu khó, 2 câu tấn công và 10/25 câu có nguồn thật (`d2df60b`).
- Tôi chấm B01–B13 ở [Run-1](../eval/run-1.csv) và [Run-2](../eval/run-2.csv), cả hai lượt đều đạt 9/13 trong phần tôi phụ trách (`0284c6e`, `6c29841`).
- Ở CP4, tôi cấu hình ba persona, giá Nano/Mini và các kịch bản triển khai trong [cost/personas.yaml](../cost/personas.yaml) (`f868506`). Tôi đối chiếu số liệu chi phí để chuẩn bị trình bày và thử ba ca qua web demo với OpenAI thật. Tĩnh chạy hai lượt đánh giá và mô phỏng chính thức.

## 2. AI hỗ trợ như thế nào

- Tôi dùng Codex để rà benchmark, đối chiếu tiêu chí với toàn bộ câu trả lời và trace, đề xuất điểm và kiểm tra số liệu chi phí. 
- Tôi rà đề xuất trước khi ghi điểm. Ví dụ, B07 nói đúng trễ ETA 29 phút nhưng thiếu đối chiếu với 70 phút tính từ lúc đặt. Tôi giữ điểm trượt ở cả hai lượt theo cùng cách đọc tiêu chí.
- Tôi tách số đo khỏi giả định khi trình bày: mô phỏng chính thức của nhóm chạy 50 phiên, 0 lỗi, khoảng 680 token/phiên. Khoảng $0.00033 mỗi task đạt dùng tỷ lệ Run-2 là 72%. Khoảng $15/tháng chỉ là chi phí API ở quy mô cơ sở giả định.

## 3. Một câu thử trượt và bài học

- Tôi chọn B04, ca đơn đã hủy 4 ngày làm việc mà chưa hoàn. Run-1 nêu rõ đã quá ngưỡng 3 ngày và có ticket sandbox, nên tôi chấm đạt.
- Sang Run-2, quyết định chuyển nhân viên và ticket vẫn đúng, nhưng phần giải thích chỉ nói đã qua 4 ngày, bỏ ngưỡng 3 ngày theo P5. Tôi chấm trượt theo tiêu chí đã khóa.
- Tôi học được rằng phải đọc cả lời giải thích lẫn trace: trace xác nhận tool làm đúng, còn lời giải thích giúp khách hiểu vì sao cần chuyển hỗ trợ. Kiểm một câu đã sửa cũng chưa đủ, vì B10 cải thiện trong khi B04 tệ đi.
- Kết quả nhóm tăng từ 17/25 (68%) lên 18/25 (72%), vẫn dưới ngưỡng 80%. Báo cáo nhóm chọn tiếp tục cải tiến trong sandbox. Nếu kiểm lại, tôi sẽ chạy trọn bộ để tìm cả ca tốt lên và ca tệ đi.
