# Khai báo sử dụng AI của nhóm NoName

Tài liệu ghi nhận AI được dùng vào việc gì, phạm vi hỗ trợ và trách nhiệm kiểm tra của thành viên. Cập nhật ngày 27/11/2026. Phần tóm tắt sử dụng AI trong README của nhóm cần thống nhất với hồ sơ này.

## 1. Nguyên tắc ghi nhận

Chỉ ghi hoạt động và kết quả kiểm tra đã thực hiện. Trạng thái “chưa tổng hợp” nghĩa là hồ sơ chưa có đủ thông tin khai báo, không có nghĩa hạng mục không sử dụng AI. Thành viên phụ trách bổ sung công cụ, phạm vi hỗ trợ và kết quả kiểm tra thực tế khi có.

Người phụ trách cần giải thích được nội dung thuộc phần việc của mình. AI không thay thế người tham gia phỏng vấn, người trả lời khảo sát hoặc người chấm độc lập.

## 2. Các hạng mục sử dụng AI

| Hạng mục | Công cụ đã khai báo | Phạm vi AI hỗ trợ | Trạng thái kiểm tra | Phụ trách cập nhật |
|---|---|---|---|---|
| Code bản chạy thử | Chưa tổng hợp | Chưa tổng hợp trong hồ sơ | Chưa ghi nhận kết quả kiểm tra | Tĩnh |
| Prompt và lời gọi mô hình | Chưa tổng hợp | Chưa tổng hợp trong hồ sơ | Chưa ghi nhận kết quả kiểm tra | Tĩnh |
| Phân tích review | Chưa tổng hợp | Chưa tổng hợp phần hỗ trợ viết script hoặc gợi ý nhãn | Kết quả đọc tay tham chiếu evidence/data-mining.md; chưa ghi riêng mức đóng góp của AI | Hưng |
| Rà câu hỏi phỏng vấn và khảo sát | Chưa tổng hợp | Chưa ghi nhận công cụ và hoạt động cụ thể | Khi bổ sung cần nêu cách kiểm câu dẫn dắt; giữ nguyên dữ liệu trả lời thực tế | Đức và Hưng |
| Xây dựng benchmark | Chưa tổng hợp đầy đủ | Các tình huống chuyển thể cho CP3 được ghi riêng ở dòng dưới | Mỗi câu cần nguồn, phần chuyển thể và dữ kiện giả lập; trạng thái tích hợp xem eval/README.md | Khoa |
| Sinh dữ liệu giả lập | Chưa tổng hợp | Chưa ghi nhận mức hỗ trợ của AI | Seed 15 và quy mô dữ liệu được mô tả trong data/DATA_CARD.md; chưa ghi riêng kết quả kiểm tay | Tĩnh và Khoa |
| Hỗ trợ chấm benchmark bằng AI | Chưa ghi nhận lượt chấm chính thức | Đã có phân tích hỗ trợ O1/O3 trong eval/README.md; chưa ghi điểm benchmark bằng AI | Điểm của người chấm và nhận xét AI được lưu riêng | Đức và Khoa |
| Slide và tài liệu khác | Chưa tổng hợp | Chưa tổng hợp trong hồ sơ | Chưa ghi nhận kết quả kiểm tra | Thành viên phụ trách từng tài liệu |
| Biên bản, nguồn tình huống và hồ sơ đánh giá CP3 | Codex | Chuẩn hóa trình bày P1–P3; cập nhật thông tin được xác nhận; chuyển thể 5 tình huống có nguồn; phân tích O1/O3 và mô tả quy trình chấm | Đức đã xác nhận cả 3 người ngoài nhóm, không ghi nhận giờ và P2 bị từ chối hoàn. 4 tình huống đã được Khoa tích hợp tại d2df60b; phân tích điểm chưa được người chấm xác nhận | Đức; Khoa kiểm tra khi tích hợp câu thử |
| Chuẩn bị chấm bộ 25 câu CP3 | Codex | Đối chiếu nguồn với B17/B18/B24/B25; cập nhật Data Card và hồ sơ; trích nguyên văn tiêu chí B14–B25 thành bảng kiểm; đề xuất riêng phạm vi metric CP3 | Khoa đã tích hợp 4 tình huống vào benchmark tại d2df60b. Bảng kiểm chưa có output hoặc điểm. Phạm vi metric CP3 chờ Đức và Khoa thống nhất trước khi chấm | Đức và Khoa |

## 3. Tài liệu liên quan

- Biên bản gốc và phần làm rõ: evidence/interviews/P1.md, P2.md, P3.md.
- Bằng chứng và các tình huống chuyển thể: evidence/summary.md.
- Điểm hiệu chuẩn, phân tích hỗ trợ và quy trình đánh giá: eval/README.md.

Giữ nguyên lời trả lời thực tế và lịch sử chấm. Không sử dụng AI để tạo người tham gia, bịa trích dẫn hoặc phản hồi khảo sát, thay output đã chạy hay điều chỉnh expected cho khớp kết quả. Mọi đề xuất chấm bằng AI cần được người phụ trách duyệt trước khi điền điểm chính thức.
