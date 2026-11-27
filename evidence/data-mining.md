# Đào data — cách đếm và kết quả

> Điền ở guide bước 1.2. Ôn lại: ngày 2, ngày 6 · lab ngày 2, lab ngày 6.
> Repo chỉ chứa số đã tổng hợp và vài dòng ví dụ — không chép lại nguyên file data.

## 1. Cách đếm — viết TRƯỚC khi chạy

- Data dùng: review công khai của app **ShopeeFood** (`com.deliverynow`) trên Google Play, bản tiếng Việt (`hl=vi&gl=VN`), thiết bị Điện thoại, sắp xếp "Mới nhất", xem ngày 27/11/2026.
  - 1★: 120 review mới nhất (22/10/2026 → 25/11/2026). Toàn app có 32.296 review 1★.
  - 2★: 100 review mới nhất (25/12/2025 → 26/11/2026). Toàn app có 6.239 review 2★.
- Đếm gì: số review nhắc tới một nhóm vấn đề (nhãn) · trên tập nào: 220 review 1–2★ ở trên · lọc gì: chỉ lọc theo số sao, không lọc nội dung.
- **Mẫu số là gì:** N = 220 review 1–2★ (một review có thể mang nhiều nhãn, nên tổng % > 100%).
- Script / công thức: `evidence/count_reviews.js` — chạy trong DevTools Console của trang review Google Play sau khi đã mở "Xem tất cả bài đánh giá", chọn "Mới nhất" và lọc số sao. Gắn nhãn bằng biểu thức từ khóa (regex) ghi trong script. Không lưu tên người viết.

## 2. Đọc trước, đếm sau

Đã đọc ~40 review đầu trước khi đặt nhãn. Các *kiểu* hành vi thấy được:
- Chờ lâu / giao trễ, nhiều review nói bị ghép đơn.
- Muốn hủy đơn nhưng app không cho hủy; bị trừ tiền nhưng đơn tự hủy hoặc không hoàn tiền.
- Than phí, giá, bẫy deal/voucher.
- Lỗi app, địa chỉ, định vị; thái độ tài xế; món nguội/đổ.
- Hỗ trợ khách hàng chậm, trả lời mẫu.
- Một phần review chỉ chửi chung ("tệ", "rác"), không nêu lý do.

## 3. Kết quả (đã đọc tay xác nhận nhóm "hủy đơn")

| Đếm gì | x / N | % | Ghi chú |
|---|---|---|---|
| Nhắc **hủy đơn** (đã đọc tay xác nhận) | 34/220 | 15,5% | 1★: 26/120 · 2★: 8/100 (từ khóa bắt 35, đọc tay loại 1 câu bắt nhầm `R2-060` viết "hủy app") — **hướng chọn** |
| …trong đó than **không cho hủy / không hủy được** | 23/220 | 10,5% | 1★: 16 · 2★: 7 (đọc tay tăng từ 17 → 23 do regex sót cách viết "k hủy món đc", "không được hủy đơn", "không hỗ trợ hủy đơn"…) |
| …trong đó **đã thanh toán/trừ tiền, đơn hủy không hoàn hoặc mất tiền** | 5/220 | 2,3% | đều 1★ (`R1-002, R1-003, R1-079, R1-101, R1-107`; 4 câu nêu rõ mất tiền/không hoàn, `R1-003` bị trừ tiền rồi tự hủy) |
| Giao trễ, chờ lâu | 67/220 | 30% | 1★: 34 · 2★: 33; 21/220 nhắc "ghép đơn" |
| Phí, giá, voucher, deal | 37/220 | 17% | ít liên quan khiếu nại một đơn |
| Tài xế | 29/220 | 13% | |
| Chất lượng món (nguội, đổ, chảy nhựa…) | 28/220 | 13% | |
| Lỗi app, địa chỉ, định vị | 20/220 | 9% | |
| Thanh toán lỗi | 19/220 | 9% | |
| Hỗ trợ khách hàng / hoàn tiền kém | 15/220 | 7% | |
| Thiếu món (đã đọc tay xác nhận) | 3/220 | 1,4% | giả thuyết ban đầu — bị bác bỏ |
| Không gắn được nhãn nào | 68/220 | 31% | chủ yếu chửi chung |

## 4. ≥5 ví dụ cụ thể (mã review do nhóm đánh: R1-xxx = 1★, R2-xxx = 2★; đã bỏ tên, trích ≤2 câu hoặc viết lại ngắn)

1. R1-002 (24/11/2026): đơn bị hủy do phía giao hàng nhưng 2 tháng chưa được hoàn tiền, lại bị yêu cầu gửi sao kê giấy.
2. R1-003 (24/11/2026): tiền tài khoản đã bị trừ nhưng đơn báo đang chờ thanh toán, sau đó tự hủy.
3. R1-012 (21/11/2026): quán hết món vẫn giao loại khác, "ko cho hủy đơn, ép người mua nhận hàng".
4. R1-083 (29/10/2026): app định vị sai vị trí và không hỗ trợ hủy đơn.
5. R1-097 (27/10/2026): quán cách 2km mà lần nào cũng chờ ít nhất 45 phút, quán xa thì chờ mòn mỏi mà không cho hủy đơn.
6. R1-107 (25/10/2026): đặt đồ ăn đã thanh toán trước, bị hủy rồi không hoàn tiền lại.
7. R2-015 (17/10/2026): muốn hủy đơn, nhắn tin trợ giúp nhưng không ai hỗ trợ.
8. R1-074 (01/11/2026): sinh viên ấn nhầm mua deal giá đắt hơn do giỏ hàng giống nhau nhưng app không cho hủy.
9. R1-110 (25/10/2026): chờ 50 phút không có tài xế vẫn không cho hủy đơn; yêu cầu hủy thì bị cảnh báo ảnh hưởng tài khoản.
10. R2-080 (12/03/2026): chưa có tài xế nhưng không cho hủy, bắt đợi nửa tiếng tìm tài xế mới cho hủy dù muốn đổi địa chỉ hoặc không còn nhu cầu.

## 5. Giới hạn của data

- Review cho biết người ta **than gì**, không cho biết **vì sao** và **bao lâu một lần**.
- Lệch về phía người bức xúc (chỉ lấy 1–2★); không đại diện cho mọi người dùng, cũng không riêng sinh viên.
- Gắn nhãn bằng từ khóa có thể bắt nhầm hoặc bỏ sót (viết tắt, sai chính tả) → đã đọc tay lại toàn bộ 35 review khớp từ khóa "hủy đơn": loại 1 câu bắt nhầm (`R2-060`: "hủy app"), giữ 34/220 (15,5%); các nhóm nhãn khác chưa đọc tay toàn bộ.
- 2★ trải dài gần 1 năm, 1★ chỉ ~1 tháng → không so được tần suất theo thời gian.
→ Kiểm lại bằng: khảo sát ≥20 sinh viên ngoài nhóm (câu về lần gần nhất muốn hủy đơn, có biết luật hủy không) và phỏng vấn ≥3 người về "lần gần nhất muốn hủy đơn".
