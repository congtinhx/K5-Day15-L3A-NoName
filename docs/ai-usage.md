# Khai báo sử dụng AI của nhóm NoName

Tài liệu ghi nhận AI được dùng vào việc gì, phạm vi hỗ trợ và trách nhiệm kiểm tra của thành viên. Cập nhật ngày 27/11/2026. Phần tóm tắt sử dụng AI trong README của nhóm cần thống nhất với hồ sơ này.

## 1. Nguyên tắc ghi nhận

Chỉ ghi hoạt động và kết quả kiểm tra đã thực hiện. Trạng thái “chưa tổng hợp” nghĩa là hồ sơ chưa có đủ thông tin khai báo, không có nghĩa hạng mục không sử dụng AI. Thành viên phụ trách bổ sung công cụ, phạm vi hỗ trợ và kết quả kiểm tra thực tế khi có.

Người phụ trách cần giải thích được nội dung thuộc phần việc của mình. AI không thay thế người tham gia phỏng vấn, người trả lời khảo sát hoặc người chấm độc lập.

## 2. Các hạng mục sử dụng AI

| Hạng mục | Công cụ đã khai báo | Phạm vi AI hỗ trợ | Trạng thái kiểm tra | Phụ trách cập nhật |
|---|---|---|---|---|
| Code bản chạy thử | Claude (Opus 5.5) · Codex (Khoa dùng để audit) | Claude viết `codebase/tools.py` (luật P1–P7, T1 trong `check_cancel`), `agent.py` (workflow cố định, `check_llm`), `data/make_orders.py` (seed 15), phần gọi API trong `ai.py`; sửa theo audit Codex 27/11 (P1/P2, P5, T1, sức khỏe, thiếu mã đơn, kiểm chữ model) và trước lượt 1 (B25: đơn quán đã xác nhận không hỏi lý do; O5: câu tấn công đã có mã không hỏi lại mã) | Tĩnh chạy `python run.py`, `run.py check`, `eval --try` với model thật; đối chiếu 25/25 câu benchmark ra đúng quyết định expected khi chạy chế độ giả; Khoa audit bằng Codex, Khoa + Đức chấm chéo 5 output (khớp 4/5) | Tĩnh |
| Prompt và lời gọi mô hình | Claude (Opus 5.5) | Viết 2 prompt trong `agent.py`: `EXTRACT_SYSTEM` (phân loại lý do, trả JSON) và `WRITE_SYSTEM` (diễn đạt lại trong khung quyết định code đã chốt, cấm thêm số tiền/voucher/chính sách, không markdown); model chỉ diễn đạt, không tính tiền | Tĩnh gọi thử gpt-5.4-nano (2 lời gọi/câu, token > 0); `check_llm` thử 7 câu mẫu: chặn đúng 5 câu sai, cho qua 2 câu đúng | Tĩnh |
| Phân tích review | Chưa tổng hợp | Chưa tổng hợp phần hỗ trợ viết script hoặc gợi ý nhãn | Kết quả đọc tay tham chiếu evidence/data-mining.md; chưa ghi riêng mức đóng góp của AI | Hưng |
| Rà câu hỏi phỏng vấn và khảo sát | Chưa tổng hợp | Chưa ghi nhận công cụ và hoạt động cụ thể | Khi bổ sung cần nêu cách kiểm câu dẫn dắt; giữ nguyên dữ liệu trả lời thực tế | Đức và Hưng |
| Xây dựng benchmark | Chưa tổng hợp đầy đủ | Các tình huống chuyển thể cho CP3 được ghi riêng ở dòng dưới | Mỗi câu cần nguồn, phần chuyển thể và dữ kiện giả lập; trạng thái tích hợp xem eval/README.md | Khoa |
| Sinh dữ liệu giả lập | Chưa tổng hợp | Chưa ghi nhận mức hỗ trợ của AI | Seed 15 và quy mô dữ liệu được mô tả trong data/DATA_CARD.md; chưa ghi riêng kết quả kiểm tay | Tĩnh và Khoa |
| Hỗ trợ chấm benchmark bằng AI | Codex | Đối chiếu output/trace với tiêu chí B14–B25, chuẩn bị đề xuất cho người chấm; phân tích O1/O3 được lưu riêng | Đức đã duyệt 12 đề xuất lượt 1 ngày 28/11/2026, kết quả 8 đạt/4 trượt; đã tích hợp điểm B01–B13 của Khoa; soát chéo chưa hoàn tất | Đức và Khoa |
| Slide và tài liệu khác | Antigravity (Gemini) | Hỗ trợ tổng hợp và soạn `spec.md` §9 (Rủi ro & an toàn), bổ sung dòng changelog §10 và bản thảo nội dung slide trang 1–3 (`slides/slides-1-3.md`) từ dữ liệu hiện có trong repo (không bịa dữ kiện) | Đã đối chiếu `codebase/agent.py`, `tools.py`, `data/DATA_CARD.md`, `evidence/summary.md`; chạy `python run.py check` đạt; Hưng duyệt và xác nhận commit ngày 28/11/2026 | Hưng (phần §9 và slide trang 1–3); thành viên phụ trách tài liệu khác bổ sung thêm |
| Biên bản, nguồn tình huống và hồ sơ đánh giá CP3 | Codex | Chuẩn hóa trình bày P1–P3; cập nhật thông tin được xác nhận; chuyển thể 5 tình huống có nguồn; phân tích O1/O3 và mô tả quy trình chấm | Đức đã xác nhận cả 3 người ngoài nhóm, không ghi nhận giờ và P2 bị từ chối hoàn. 4 tình huống đã được Khoa tích hợp tại d2df60b; phân tích điểm chưa được người chấm xác nhận | Đức; Khoa kiểm tra khi tích hợp câu thử |
| Chuẩn bị chấm bộ 25 câu CP3 | Codex | Đối chiếu nguồn với B17/B18/B24/B25; cập nhật Data Card và hồ sơ; trích nguyên văn tiêu chí B14–B25 thành bảng kiểm; đề xuất riêng phạm vi metric CP3 | Khoa đã tích hợp 4 tình huống vào benchmark tại d2df60b. Bảng kiểm gốc giữ nguyên; đề xuất chấm lượt 1 được ghi ở dòng dưới. Phạm vi metric CP3 chờ Đức và Khoa thống nhất | Đức và Khoa |
| Đối chiếu lượt chạy AI thật phần B14–B25 | Codex | Đọc run-1.csv và trace; đề xuất pass cùng căn cứ cho 12 câu; ghi nhận các lỗi giải thích có thể có | Đức duyệt đủ 12 câu ngày 28/11/2026: 8 đạt, 4 trượt; đã nhập pass/ghi_chu của B14–B25. Đã tích hợp điểm Khoa và chạy score: 17/25 đạt (68%); chưa soát chéo hoặc tổng hợp đủ các metric riêng | Đức và Khoa |

## 3. Tài liệu liên quan

- Biên bản gốc và phần làm rõ: evidence/interviews/P1.md, P2.md, P3.md.
- Bằng chứng và các tình huống chuyển thể: evidence/summary.md.
- Điểm hiệu chuẩn, phân tích hỗ trợ và quy trình đánh giá: eval/README.md.

Giữ nguyên lời trả lời thực tế và lịch sử chấm. Không sử dụng AI để tạo người tham gia, bịa trích dẫn hoặc phản hồi khảo sát, thay output đã chạy hay điều chỉnh expected cho khớp kết quả. Mọi đề xuất chấm bằng AI cần được người phụ trách duyệt trước khi điền điểm chính thức.
