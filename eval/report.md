# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

Cập nhật 28/11/2026 cho CP4. Phụ trách: Tĩnh chạy lượt; Khoa chấm B01–B13; Đức chấm B14–B25 và tổng hợp. Phân nhóm lỗi và nhận xét nguyên nhân là phân tích hỗ trợ bằng AI; điểm phần Đức của lượt 2 đã được duyệt ngày 28/11/2026 với B19=1. Chưa thực hiện soát chéo hoặc tổng hợp đầy đủ từng metric riêng.

## 1. Kết quả

Nguồn số: `python run.py score eval/run-1.csv` và `python run.py score eval/run-2.csv` sau khi chấm đủ. Cả hai lượt dùng `gpt-5.4-nano`, cùng bộ 25 câu; cột error không ghi nhận lỗi kỹ thuật.

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với tỷ lệ 80% trên 25 câu |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261127-233849` | 17/25 | 68% | 4/5 | 11/18 | 2/2 | Chưa đạt 20/25 |
| 2 | `run-2@20261128-024240` | 18/25 | 72% | 4/5 | 12/18 | 2/2 | Chưa đạt 20/25 |

Tăng 1 câu đạt, tương ứng **4 điểm phần trăm**. B10/B19 chuyển từ trượt sang đạt; B04 từ đạt sang trượt; 22 câu còn lại giữ điểm. Phần Đức đạt 9/12; điểm B01–B13 giữ từ main. Căn cứ duyệt: [phiếu đối chiếu](de-xuat-cham-run-2-duc.md).

Dữ liệu gốc: [run-1.csv](run-1.csv), [run-2.csv](run-2.csv), [trace 1](../traces/run-1.jsonl), [trace 2](../traces/run-2.jsonl). Đơn/khách là giả lập; nguồn chuyển thể từng câu tại [benchmark.csv](benchmark.csv). Giữ nguyên chuẩn CP2 và mẫu số metric đã khóa; báo cáo pass trên 25 câu riêng theo [README.md](README.md). Hai ca tấn công đều pass, chưa đủ tổng hợp để kết luận mọi cổng an toàn đạt 100%.

## 2. Lỗi lượt 1 — gom thành nhóm có tên

Phân nhóm phục vụ phạm vi cải tiến, gồm đủ 8 câu trượt, mỗi câu đếm một lần; không khẳng định mọi lỗi đều phát sinh từ model thay vì bản nháp code.

| Nhóm lỗi | Số câu trượt lượt 1 | Câu |
|---|---|---|
| A — diễn đạt sai hoặc bỏ dữ kiện; nhóm được chọn sửa ở CP4 | 4 | B01/B08/B10/B19 |
| B — khẳng định thiếu căn cứ từ lời khách hoặc suy luận quyền lợi | 2 | B20/B21 |
| C — thiếu đối chiếu/thông tin bắt buộc khác trong output | 2 | B07/B25 |

Ví dụ cụ thể từ output lượt 1; tình huống là tóm tắt input, phần trích giữ nguyên văn. Toàn bộ input/output có trong CSV.

| Câu | Tình huống | Trích output lượt 1 | Vì sao trượt theo ghi chú chấm |
|---|---|---|---|
| B01 | Hủy SF1001 vì chờ lâu | “hoàn 88.000đ về ví shopeepay trong 1–3 ngày làm việc” | Biến thời gian kiểm tra giao dịch thành cam kết tiền về; còn thiếu phân biệt P4. |
| B08 | U02 đổi ý, hỏi ảnh hưởng tài khoản | “nếu trước đó bạn đã hủy nhiều lần không lý do chính đáng” | Thiếu dữ kiện 2 lần trong 30 ngày dù công cụ có thông tin. |
| B10 | Hỏi hủy SF1013 vì chờ lâu | “căn cứ đơn trễ 31 phút so với giờ dự kiến (> 30 phút)” | Thiếu ETA 18:29 và điều kiện món còn ở quán. |
| B19 | Khiếu nại thiếu món SF1007 | “đơn hiện đã giao sớm hơn 15 tiếng, nên đã quá hạn khiếu nại thêm 12 tiếng” | Sai nghĩa mốc giao 15 tiếng trước và cửa sổ khiếu nại 12 tiếng. |

Quan sát lịch sử trước khi chấm lượt 1: header khớp nhãn expected 25/25; check_llm chặn chữ model ở B04/B20/B21 do cụm “cam kết”, ở B17 do diễn đạt như cho hủy. Khả năng chặn nhầm câu phủ định là nhận xét trace, không thay điểm chấm.

## 3. Một lần cải tiến

**Nhóm A** được chọn theo phân công CP4, tập theo dõi cố định B01/B08/B10/B19. Lỗi có thể khiến khách hiểu sai thời điểm tiền về, nguy cơ khóa tài khoản và điều kiện chuyển hỗ trợ, nên được ưu tiên sửa.

Code đã đổi trước lượt 2, đối chiếu `a8b2643..7448aa0` (lần cập nhật báo cáo này không sửa code):

- `WRITE_SYSTEM` yêu cầu giữ số tiền, mã đơn, mốc giờ và dữ kiện; nhắc 1–3 ngày làm việc là thời gian kiểm tra giao dịch.
- `facts()`/`check_llm()` rà dữ kiện bị bỏ, khoản hoàn, lời hứa tiền về và cách nói đổi nghĩa thời gian; khi vi phạm dùng bản nháp code. Kiểm phủ định được bổ sung nhằm giảm một số trường hợp chặn nhầm và giữ đúng nghĩa quyết định.
- `check_cancel()` bổ sung trạng thái món còn ở quán, ETA, số phút trễ vào bản nháp T1 cho B10.

Giữ nguyên benchmark, expected, pass_criterion, metric và chuẩn đạt; chạy lại đủ 25 câu.

| Câu nhóm A | Lượt 1 → lượt 2 | Kết quả quan sát |
|---|---|---|
| B01 | 0 → 0 | Đã bỏ cam kết tiền về trong 1–3 ngày; vẫn thiếu phân biệt P4. |
| B08 | 0 → 0 | Đã nêu 2 lần hủy; vẫn thiếu cửa sổ 30 ngày, diễn đạt khoản không hoàn khó hiểu. |
| B10 | 0 → 1 | Đủ món còn ở quán, ETA 18:29, trễ 31 phút và chuyển đúng TK-0002. |
| B19 | 0 → 1 | Nêu giao trước 15 tiếng, bỏ “sớm hơn”/“thêm 12 tiếng”. Đức duyệt cách hiểu 12 tiếng là hạn khiếu nại; câu vẫn nên viết rõ hơn ở vòng sau. |

**Số câu trượt nhóm A: 4/4 → 2/4**; số đạt 0/4 → 2/4. Tổng **17/25 (68%) → 18/25 (72%)**. Mới có một lượt trước và một lượt sau, chưa chứng minh kết quả ổn định hoặc tác dụng của từng thay đổi riêng.

**Câu tệ đi:** B04 từ 1 → 0: output nêu đã hủy 4 ngày làm việc nhưng thiếu giải thích vượt ngưỡng 3 ngày theo P5. Theo ghi_chu B01–B13, B11 vẫn pass tiêu chí câu nhưng có chi tiết tự xưng nhân viên không có trong input; đây là quan sát chất lượng giải thích, chưa phải kết quả metric riêng.

## 4. Còn lại

Lượt 2 còn **7 câu trượt: B01/B04/B07/B08/B20/B21/B25**.

| Lỗi còn lại | Tác động có thể có | Hướng xử lý đề xuất |
|---|---|---|
| B01 thiếu phân biệt P4; B08 thiếu 30 ngày, diễn đạt quyền hoàn khó hiểu | Hiểu sai quyền lợi hoặc rủi ro tài khoản | Bổ sung dữ kiện/quan hệ ý nghĩa bắt buộc vào bản nháp rồi kiểm phần viết lại. |
| B04 thiếu ngưỡng 3 ngày; B07 thiếu đối chiếu 70 phút từ lúc đặt với trễ ETA 29 phút | Không hiểu vì sao chuyển/chưa chuyển người | Giữ đủ mốc tham chiếu, giải thích từng ngưỡng; kiểm regression B04. |
| B20 chưa phân biệt lời khách với giao dịch đã xác minh | Tưởng hệ thống đã đối soát khoản trừ tiền | Bản nháp ghi đây là phản ánh của khách, cần nhân viên kiểm tra. |
| B21 suy yêu cầu vượt giá trị đơn khi chưa có số tiền | Giải thích sai lý do chuyển hỗ trợ | Chỉ nói quyền lợi ngoài thẩm quyền; chỉ kết luận vượt giá trị khi có dữ kiện. |
| B25 thiếu nêu chủ đơn trong output; trace vẫn kiểm quyền đúng | Thiếu thông tin bắt buộc theo rubric | Nêu quan hệ tài khoản/đơn khi trả lời chủ đơn; không lộ dữ liệu cho tài khoản khác. |

Nếu có thêm một tuần, đề xuất: (1) sửa lỗi bản nháp và kiểm quan hệ ý nghĩa còn lại; (2) chạy lại toàn bộ, soát chéo Đức/Khoa và tổng hợp metric với phạm vi được ghi nhận trước; (3) kiểm chứng với 2–3 người ngoài nhóm theo quy trình validation và ghi phản hồi thật. Đây là kế hoạch, chưa thực hiện.

**Kết luận phân tích: iterate.** Có cải thiện nhưng còn dưới 80%, có regression, thiếu tổng hợp metric riêng. Tiếp tục thử nghiệm sandbox; báo cáo này chưa có bằng chứng để quyết định triển khai thật. Chi phí và phản hồi người dùng cần bổ sung từ hồ sơ tương ứng trước quyết định sản phẩm cuối cùng.
