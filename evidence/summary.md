# Tổng hợp bằng chứng về nhu cầu hủy và hoàn tiền ShopeeFood

Cập nhật ngày 27/11/2026. Tài liệu tổng hợp nguồn bằng chứng cho CP3 và cung cấp tình huống thực tế để mở rộng bộ câu thử. Hạn CP3: 10:00 ngày 28/11/2026.

## 1. Nguồn bằng chứng và phạm vi sử dụng

| Nguồn | Kết quả hiện có | Giới hạn | Tài liệu gốc |
|---|---|---|---|
| Review Google Play | Đọc tay 35 review ứng viên, giữ 34/220 review thuộc nhóm hủy đơn | Mẫu chỉ gồm review 1–2 sao, không đại diện cho toàn bộ người dùng hoặc riêng sinh viên | [Cách đếm và kết quả](data-mining.md) |
| Phỏng vấn | 3 biên bản của người ngoài nhóm NoName; người phỏng vấn đã xác nhận ngày 27/11/2026 | Không ghi nhận giờ; chưa xác nhận độ tuổi và mức phù hợp với nhóm sinh viên 18–24 tuổi | [P1](interviews/P1.md), [P2](interviews/P2.md), [P3](interviews/P3.md) |
| Khảo sát | 20 phản hồi đã ẩn danh, gồm 9 học viên AI20K, 7 sinh viên 18–24 tuổi và 4 người đi làm | Mẫu gồm nhiều nhóm đối tượng; không gộp toàn bộ thành sinh viên 18–24 tuổi | [Bộ câu hỏi và tổng hợp](survey/questions.md), [dữ liệu khảo sát](survey/results.csv) |

CP3 yêu cầu ít nhất một nguồn đạt ngưỡng của đề và ít nhất 5 trích dẫn nguyên văn. Việc đánh giá ngưỡng cần xét cả số lượng, đối tượng và giới hạn lấy mẫu. Riêng 3 cuộc phỏng vấn chưa đủ để xác nhận điều kiện đúng đối tượng sinh viên 18–24 tuổi.

## 2. Kết quả chính

### Review

Theo kết quả đọc tay trong [data-mining.md](data-mining.md), 34/220 review nhắc đến hủy đơn (15,5%); 23/220 phản ánh không hủy được (10,5%). Một review bắt nhầm do nội dung nói về hủy app đã được loại khỏi 35 ứng viên. Các tỷ lệ này mô tả tập review đã chọn, không phải tỷ lệ người dùng gặp vấn đề.

### Phỏng vấn

Người phụ trách thu thập: Nguyễn Ngọc Minh Đức. Cả 3 người được phỏng vấn là học viên L3 và không thuộc nhóm NoName.

| Mã | Tình huống và cách xử lý | Kết quả được ghi nhận | Thời gian xử lý | Số lần trong tháng vừa qua |
|---|---|---|---|---|
| P1 | Muốn hủy vì giao chậm; hủy qua app khi đơn đang chờ | Hủy được; theo lời kể, nhận lại tiền khoảng 2 phút sau đó | Khoảng 5 phút | 1 lần |
| P2 | Đơn báo trạng thái lỗi; bấm hủy | Bị từ chối hoàn tiền, theo thông tin làm rõ của người phỏng vấn; chưa rõ lỗi cụ thể và lý do từ chối | 10 phút, chưa rõ mốc bắt đầu và kết thúc | Nhiều lần, chưa có số cụ thể |
| P3 | Đặt hộ người đã có đồ ăn; app chặn hủy sau khi đơn được xác nhận; liên hệ riêng tài xế | Không được hoàn tiền; chưa ghi nhận rõ kết quả hủy cuối cùng và trạng thái xử lý hoàn | Hơn 20 phút | 1 lần |

Không tính thời gian trung bình vì cách xác định khoảng thời gian chưa đồng nhất và P3 chỉ có cận dưới. Không quy đổi “nhiều lần” thành một con số. P2 bị từ chối hoàn chưa chứng minh việc từ chối là sai chính sách.

### Khảo sát

Dữ liệu có 20 phản hồi; 14 người cho biết có dùng thanh toán trước. Kết quả chi tiết và cách đếm nằm trong [báo cáo khảo sát](survey/questions.md). Khi sử dụng kết quả, cần phân biệt học viên AI20K, sinh viên 18–24 tuổi và người đi làm, đồng thời đối chiếu các câu trả lời mâu thuẫn trong dữ liệu gốc.

## 3. Trích dẫn nguyên văn từ khảo sát

Các trích dẫn dưới đây lấy từ câu 11 trong [results.csv](survey/results.csv), đã bỏ thông tin định danh. Số phiếu là thứ tự dòng dữ liệu, không tính dòng tiêu đề. Giữ nguyên nội dung chữ; bỏ khoảng trắng thừa ở đầu và cuối câu.

| Phiếu | Nội dung nguyên văn |
|---|---|
| #1 | “Ko có thông tin hỗ trợ đầy đủ” |
| #5 | “lâu mất thời gian, thời gian hoàn tiền lâu” |
| #12 | “ship không muốn hủy” |
| #15 | “không muốn nhận hàng nữa” |
| #18 | “không thể hủy đơn ngay lập tức” |
| #19 | “muốn hủy nhưng không thể hủy” |

Các tình huống phỏng vấn trong mục 2 là bản tóm tắt biên bản. Phần làm rõ P2 do người phỏng vấn cung cấp được ghi riêng trong biên bản P2.

## 4. Đối chiếu giữa các nguồn

Review và khảo sát cùng ghi nhận phản ánh về việc không hủy được hoặc tiền chưa được hoàn. P3 bổ sung tình huống app chặn hủy sau xác nhận; P2 bổ sung trường hợp lỗi và bị từ chối hoàn nhưng chưa rõ nguyên nhân. P1 ghi nhận trường hợp hủy và nhận tiền nhanh, cho thấy trải nghiệm không đồng nhất.

Các nguồn hỗ trợ việc chọn tình huống cho bản chạy thử, nhưng chưa đủ để kết luận mọi khách hàng đều khó hủy, mọi trường hợp chưa hoàn đều sai luật, hoặc các vấn đề này phổ biến ở mức nào trong toàn bộ nhóm sinh viên. Kết quả phỏng vấn chưa trực tiếp xác nhận các ngưỡng H1–H5 trong [hồ sơ giả thuyết](hypothesis.md).

## 5. Thông tin cần bổ sung

| Nội dung | Trạng thái | Phụ trách |
|---|---|---|
| Xác nhận người phỏng vấn ngoài nhóm | Đã xác nhận cả 3 trường hợp ngày 27/11/2026 | Đức |
| Giờ phỏng vấn | Không ghi nhận; giữ nguyên trạng thái thiếu dữ liệu | Đức |
| Độ tuổi và mức phù hợp với đối tượng sinh viên 18–24 tuổi | Chưa xác nhận | Đức |
| Lỗi cụ thể và lý do P2 bị từ chối hoàn | Chưa ghi nhận | Đức |
| Đối chiếu kết quả khảo sát, giới hạn mẫu và review | Tham chiếu tài liệu khảo sát và data-mining; cần hoàn thiện tổng hợp cho CP3 | Hưng |

## 6. Tình huống thực tế đề xuất cho bộ câu thử CP3

### Mục đích và trạng thái

Bảng dưới cung cấp 5 tình huống có nguồn để xây dựng B16–B25. Các câu chuyển thể cần được kiểm tra trước khi sử dụng; không tính chúng là người tham gia mới hoặc kết quả đánh giá đã chạy.

Người phụ trách nguồn phỏng vấn: Đức. Người phụ trách tích hợp vào bộ câu thử: Khoa. Người bổ sung nguồn review: Hưng.

### Danh sách tình huống

| Mã | Nguồn | Câu thử đề xuất | Điều kiện khi đưa vào benchmark |
|---|---|---|---|
| D01 | [P1](interviews/P1.md), câu 1, 2 và 4 | Mình chờ đồ ăn lâu quá, kiểm tra giúp mình có hủy đơn được không? | Gắn mã đơn và trạng thái giả lập. Gần B01, chỉ chọn khi kiểm tra thêm được hành vi chưa phủ. Mốc nhận tiền 2 phút trong lời kể không phải cam kết của hệ thống. |
| D02 | [P2](interviews/P2.md), câu 2, 4 và thông tin làm rõ | Đơn của mình báo lỗi nên mình bấm hủy, nhưng bị từ chối hoàn tiền. Nhờ kiểm tra giúp vì sao. | Chưa biết lỗi và lý do từ chối. Cần chọn dữ liệu giả lập và kết quả mong đợi theo luật đã chốt; không mặc định khách đủ điều kiện hoàn. |
| D03 | [P3](interviews/P3.md), câu 1 và 2 | Mình đặt hộ người yêu nhưng người yêu đã có đồ ăn rồi. Đơn đã xác nhận và app không cho hủy, giờ mình phải làm sao? | Gắn mã đơn giả lập đã xác nhận. Gần B02/B03, cần tránh lặp cùng hành vi. Không bổ sung kết quả hủy thành công khi nguồn chưa ghi nhận. |
| D04 | [Khảo sát](survey/results.csv), phiếu #5, câu 5–8 và 11 | Mình hủy đơn vì chờ lâu, tiền đã trừ nhưng chưa thấy hoàn. Kiểm tra giúp mình với. | Ưu tiên kiểm tra trong hạn xử lý hoàn; đối chiếu đơn giả lập SF1006 trước khi chọn. Số ngày chờ do dữ liệu giả lập quy định, không có trong lời kể. |
| D05 | [Khảo sát](survey/results.csv), phiếu #10, câu 3 và 5–8 | Đơn mình thanh toán tiền mặt, chưa trả tiền mà chờ lâu quá. Mình muốn hủy thì xử lý thế nào? | Ưu tiên trường hợp thanh toán tiền mặt còn thiếu; đối chiếu đơn giả lập SF1009 trước khi chọn. Không diễn giải thành khoản tiền đã bị trừ. |

### Yêu cầu tích hợp

Khoa bổ sung mã câu B16–B25, mã đơn giả lập, `expected`, `pass_criterion` và `type`. Trường `source` sử dụng tiền tố `nguoi_dung:`, ghi rõ biên bản hoặc số phiếu, nội dung được chuyển thể và các dữ kiện giả lập thêm vào. “Giả lập” tương ứng với nhãn `synthetic` trong dữ liệu dự án.

Giữ nguyên B01–B15. Ưu tiên D02, D04 và D05 để bổ sung hành vi còn thiếu. D01 và D03 cần được kiểm tra trùng lặp trước khi chọn. Phân công CP3 yêu cầu ít nhất 4 trong 10 câu mới có nguồn thật; 5 tình huống đề xuất chưa tự bảo đảm điều kiện này nếu có ca bị loại do trùng lặp. Khi thiếu, bổ sung nguồn review hoặc tình huống phù hợp khác trước khi chạy kiểm tra bộ câu thử.
