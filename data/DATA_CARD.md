# Data card — dữ liệu bản chạy thử dùng

Bản nháp CP2 · 27/11/2026. Các trích đoạn review dùng mã đã bỏ tên. Dữ liệu đơn và khách trong bản chạy thử là dữ liệu giả lập.

## Dataset 1 · Google Play Reviews — ShopeeFood

| Hạng mục | Chi tiết |
|---|---|
| Dùng để làm gì | Đào bằng chứng về khó khăn khi hủy đơn và chọn tình huống cho benchmark. Review ghi trải nghiệm người dùng, quyền hủy và hoàn của từng câu thử lấy từ policy và fixture đã duyệt. |
| Từ đâu | Review công khai của ShopeeFood trên Google Play, package `com.deliverynow`, bản tiếng Việt (`hl=vi&gl=VN`), thiết bị điện thoại. |
| Xử lý | Chọn “Mới nhất”, lọc theo số sao, không lọc nội dung khi lấy mẫu. Gắn nhãn sơ bộ theo từ khóa bằng [evidence/count_reviews.js](../evidence/count_reviews.js). Hưng đọc tay 35 review ứng viên hủy đơn và loại `R2-060` vì nhắc hủy app. Chỉ 35 ứng viên được đọc tay trong bước này. Script không lưu tên, review cung cấp cho benchmark đã bỏ tên và được dẫn bằng mã/ngày. |
| Số dòng / số đoạn | 220 review, gồm 120 review 1★ từ 22/10/2026 đến 25/11/2026 và 100 review 2★ từ 25/12/2025 đến 26/11/2026. |
| Phiên bản / ngày lấy | Thu thập 27/11/2026. Bản đọc tay do Dương Tuấn Hưng báo ngày 27/11/2026 lúc 17:24, đã ghi tại [evidence/data-mining.md §3](../evidence/data-mining.md) và [canvas dòng 4](../canvas.md). |
| Nhãn và lưu trữ | Dữ liệu thật. Checkout có số tổng hợp và ví dụ đã bỏ tên, chưa có tập review thô. |
| Kết quả cập nhật | Hủy đơn **34/220 (15,5%)**, không cho hủy **23/220 (10,5%)**, đã thanh toán hoặc bị trừ tiền rồi đơn hủy không hoàn hoặc mất tiền **5/220 (2,3%)**. Evidence ghi 4 ca nêu rõ mất tiền/không hoàn, còn R1-003 ghi bị trừ tiền rồi đơn tự hủy. |
| Giới hạn | Mẫu chỉ có 1–2★, thiên về người không hài lòng, hai nhóm sao có khoảng thời gian khác nhau. Lọc ứng viên bằng từ khóa có thể bỏ sót review liên quan ngoài 35 mục đã đọc. Các tỷ lệ mô tả mẫu đã lấy. |

**Review dùng trong benchmark:** `R1-086` → B03 (việc gấp, chuyển thể thành đổi kế hoạch rõ ràng), `R1-002` → B04 (chậm hoàn, chuyển từ hai tháng trong review sang 4 ngày làm việc theo fixture), `R1-074` → B05 (mua nhầm deal), `R1-108` → B07 (chờ lâu, dùng giờ đặt và ETA giả lập), `R1-110` → B08 (lo ngại ảnh hưởng tài khoản khi yêu cầu hủy; lý do đổi ý, trạng thái chờ xác nhận và lịch sử hai lần hủy là dữ kiện của SF2001/U02). R1-002, R1-074 và R1-110 được đối chiếu tại [evidence/data-mining.md](../evidence/data-mining.md) §4. Canvas cũng trích R1-074. R1-086 và R1-108 dẫn theo tin nhắn Hưng cung cấp lúc 17:24, do hai mã này chưa có trong evidence/canvas. [Benchmark](../eval/benchmark.csv) ghi nguồn và phần chuyển thể từng câu. Nội dung input là tình huống chuyển thể. Mã đơn, giờ, trạng thái và tiền là dữ kiện synthetic. Giữ `R1-083` và `R2-080` làm ứng viên CP3.

## Dataset 2 · Synthetic Orders and Users

| Hạng mục | Chi tiết |
|---|---|
| Dùng để làm gì | Luồng tra đơn, kiểm chủ đơn, lịch sử hủy, tính trễ ETA, kiểm hoàn tiền và dựng câu thử. Mặc định dùng khách `U01`; tiền tố `[U02]`, `[U03]`, `[U04]` chọn khách giả lập. |
| Từ đâu | Nguyễn Công Tĩnh tạo [orders.json](orders.json) và [users.json](users.json) bằng [make_orders.py](make_orders.py). |
| Xử lý | Bảng `SPEC` dựng tay cố định mã đơn, khách, trạng thái, thời gian, thanh toán và tình huống. `random.Random(15)` sinh tổng tiền 35.000–180.000đ theo bội số 1.000, số quán mẫu, Xu và mã giảm giá. Tên khách mẫu và lịch sử hủy khai báo cố định. |
| Số dòng / số đoạn | 17 đơn, 4 khách. |
| Phiên bản / ngày lấy | `v1 · 27/11/2026`, seed `15`, giờ sandbox cố định `2026-11-27T19:00` không kèm offset múi giờ. |
| Nhãn | `synthetic` ở metadata và từng bản ghi. Dữ liệu giả lập dùng để thử workflow. |
| Kiểm tay | Người kiểm và số bản ghi đã kiểm tay chưa được xác nhận. |
| Giới hạn | Thiếu đối soát giao dịch độc lập, thiếu trạng thái quán/tài xế tách riêng và dữ kiện xác minh định vị. Có fixture món còn ở quán trễ ETA 29/30/31 phút và đang giao trễ 40 phút. Còn thiếu ca đúng 3 ngày làm việc. Code đếm thứ Hai–thứ Sáu giữa các ngày lịch, không xét ngày lễ. |

**Schema JSON**

- Cả hai file có `meta` dạng object, với `seed` kiểu số nguyên và `now`, `label`, `version` kiểu chuỗi.
- `orders.json` có `orders` dạng object ánh xạ mã đơn sang bản ghi. Các trường chuỗi gồm `order_id`, `user_id`, `quan`, `trang_thai`, `gio_dat`, `gio_du_kien`, `thanh_toan`, `kich_ban`, `label`. `tong_tien` là số nguyên đồng, `xu_da_dung` là số nguyên, `ma_khuyen_mai` là chuỗi hoặc `null`. Đơn đã hủy thêm `gio_huy` và `hoan_tien` kiểu chuỗi, hai fixture hiện có đều là `chua_hoan`. Đơn đã giao thêm `gio_giao` kiểu chuỗi. Các trường giờ dùng ISO.
- Sáu trạng thái gồm `cho_xac_nhan`, `quan_da_xac_nhan`, `tai_xe_da_nhan`, `dang_giao`, `da_huy`, `da_giao`. Phương thức thanh toán gồm `shopeepay`, `the`, `tien_mat`.
- `users.json` có `users` dạng object ánh xạ mã khách sang bản ghi. `ten` và `label` là chuỗi, `so_don_huy_khong_ly_do_30_ngay` là số nguyên.

**Tái tạo:** từ gốc repo, `python data/make_orders.py` ghi đè cả hai JSON bằng seed và giờ sandbox cố định. Lệnh này chưa được chạy trong lần cập nhật Data Card.

**Danh sách fixture thực tế**

| Khách | Mã đơn và trạng thái |
|---|---|
| `U01` | `SF1001`, `SF1009` chờ xác nhận (SF1009 trả tiền mặt); `SF1002`, `SF1012`, `SF1013` quán đã xác nhận; `SF1003`, `SF1011` tài xế đã nhận; `SF1004`, `SF1010` đang giao; `SF1005`, `SF1006` đã hủy, chưa hoàn; `SF1007`, `SF1008` đã giao. |
| `U02` | `SF2001` chờ xác nhận, lịch sử 2 lần hủy không lý do chính đáng trong 30 ngày. |
| `U03` | `SF3001` chờ xác nhận và `SF3002` quán đã xác nhận. Cả hai đang chạy. |
| `U04` | `SF4001` chờ xác nhận, khác chủ mặc định U01. |

**Fixture T1 trong benchmark**

| ID | Đơn | Trạng thái | ETA | Trễ ETA tại 19:00 | Tổng tiền |
|---|---|---|---|---:|---:|
| B07 | SF1011 | Tài xế đã nhận, món còn ở quán | 18:31 | 29 phút | 60.000đ |
| B13 | SF1012 | Quán đã xác nhận | 18:30 | 30 phút | 47.000đ |
| B10 | SF1013 | Quán đã xác nhận | 18:29 | 31 phút | 177.000đ |
| B14 | SF1010 | Đang giao | 18:20 | 40 phút | 39.000đ |

Giờ đã chờ tính từ lúc đặt, còn độ trễ tính từ ETA. B15 dùng SF1008 đã giao lúc 18:00. Triệu chứng do tin nhắn thử cung cấp. Với B01, Tĩnh xác nhận dùng toàn bộ 88.000đ của fixture và hoàn về ví ShopeePay ban đầu. Nhóm suy ra công thức để dùng trong sandbox theo [spec.md](../spec.md) §4. Mốc 1–3 ngày làm việc là thời gian kiểm tra giao dịch.
