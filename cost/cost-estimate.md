# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate` → chép bảng trong `cost/simulate-N-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`, Khoa điền): 3 kiểu, mỗi phiên 1 lượt hỏi (1 yêu cầu hủy). Ít đặt 50% · 0,1 lần muốn hủy / người / tháng; vừa 35% · 0,3 lần; nhiều / đặt hộ nhóm 15% · 1 lần. Nguồn: `spec.md` §2 *(tự ước tính)*, đối chiếu khảo sát Q2 (`evidence/survey/results.csv`: 16/20 · 2/20 · 2/20 theo dải số đơn). Trung bình có trọng số: 0,5×0,1 + 0,35×0,3 + 0,15×1 = **0,305 phiên / người / tháng**.
- **Số người dùng thật** 3 kịch bản: thấp 41.000 · cơ sở 205.000 · cao 410.000. Nguồn: 1% · 5% · 10% của mốc 4,1 triệu người dùng ShopeeFood (Znews 12/07/2024, https://znews.vn/shopeefood-but-pha-nho-van-dung-ai-vao-dich-vu-goi-mon-truc-tuyen-post1485989.html). Tỉ lệ 1/5/10% là **(tự ước tính)** quy mô triển khai, không phải số người dùng đã xác minh.
- **Giá** ≥2 mức model (USD / 1 triệu token): `gpt-5.4-nano` vào 0,20 · ra 1,25 (OpenAI, https://developers.openai.com/api/docs/models/gpt-5.4-nano, xem 28/11/2026 — bảng giá BTC chưa có model này) · `gpt-5.4-mini` vào 0,75 · ra 4,50 (`further-reading/model-prices.md` của repo đề, xem 28/11/2026).
- **Tỉ lệ đạt** dùng để tính: **18/25 (72%) — lượt `run-2@20261128-024240` (lượt 2)**, chấm xong 11:44 28/11. Bản đầu (`simulate-1`, 11:26) tạm dùng lượt 1 (17/25 = 68%) vì lượt 2 chưa chấm xong; giữ nguyên file `simulate-1` để đối chiếu, bảng dưới dùng `simulate-2`.
- Đo token trên model **gpt-5.4-nano** (model đang chạy bản thử), tính giá **gpt-5.4-nano** và **gpt-5.4-mini**. Cùng hãng nên bộ tách token gần nhau, nhưng mini có thể viết dài hơn → chi phí mini ở đây là ước tính thấp.

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-2.csv` (`cost/simulate-2-summary.md`) · 50 phiên · seed 42 · 0/50 phiên lỗi · tỉ lệ đạt lượt 2. Mỗi phiên: 2,0 lời gọi model (phân loại lý do + diễn đạt), ~4,2 lời gọi công cụ, ~583 token vào / ~94 token ra.

| Persona | Số phiên | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 26 | 1 | 584 | 92 | 2.0 | 4.2 |
| dung_vua | 17 | 1 | 577 | 95 | 2.0 | 4.2 |
| dung_nhieu | 7 | 1 | 597 | 102 | 2.0 | 4.3 |

| Model | Chi phí / phiên | Chi phí / task thành công | / tháng — thấp (41.000) | / tháng — cơ sở (205.000) | / tháng — cao (410.000) | / người / tháng (cơ sở) |
|---|---|---|---|---|---|---|
| gpt-5.4-nano | $0.00023 | **$0.00033** | $3.00 | **$15.00** | $30.01 | $0.000073 |
| gpt-5.4-mini | $0.00086 | $0.0012 | $11.02 | $55.11 | $110.23 | $0.00027 |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt (72%, lượt 2): $0.00023 ÷ 0,72 ≈ $0.00033 — **không coi như đạt 100%**. Kiểm lại tay: kịch bản cơ sở 205.000 × 0,305 ≈ 62.500 phiên / tháng × $0.00024 ≈ $15, khớp bảng. Bản `simulate-1` (tỉ lệ lượt 1, 68%) cho $0.00035 / task thành công — chi phí / phiên gần như không đổi giữa hai lần chạy.

## 3. So với impact

- Impact / người / tháng (`spec.md` §2, *(tự ước tính)*): người gặp vấn đề hủy đơn mất ~15 phút chat/chờ hỗ trợ mỗi lần, ~10% ca mất ~60.000đ vì hủy do đổi ý mà không biết luật. Theo tần suất persona (0,305 lần / người / tháng): **~4,6 phút + ~1.800đ rủi ro mất tiền / người / tháng** (0,305 × 15 phút; 0,305 × 10% × 60.000đ).
- Chi phí model / người / tháng (cơ sở, gpt-5.4-nano): **$0.000073** — nhỏ hơn 1 xu USD; kể cả gpt-5.4-mini cũng chỉ $0.00027.
- **Kết luận một dòng — đáng làm không:** **Đáng làm xét về chi phí model** — $15 / tháng cho ~62.500 yêu cầu hủy ở kịch bản cơ sở là không đáng kể so với ~4,6 phút + ~1.800đ tiết kiệm / người / tháng; rào cản thật không phải tiền model mà là **chất lượng** (lượt 2 mới 72%, dưới chuẩn 80%) và **giờ công nhân viên** cho các ca chuyển người (mục 4).

## 4. Chi phí ngoài model và độ nhạy *(tự ước tính, không bắt buộc)*

- **Giờ công nhân viên là chi phí lớn nhất:** 5/25 câu thử (20%) là ca bắt buộc chuyển nhân viên (B04, B10, B15, B20, B21). Nếu 20% của ~62.500 phiên / tháng (cơ sở) chuyển người và mỗi ca tốn ~5 phút nhân viên *(tự ước tính)* → ~1.040 giờ công / tháng, lớn hơn chi phí model nhiều bậc. Tỉ lệ thật phụ thuộc phân bố yêu cầu thật, chưa đo.
- **Đổi model:** nano → mini tăng ~3,7 lần chi phí (vẫn < $0.001 / người / tháng ở kịch bản cơ sở). Chỉ đáng đổi nếu mini giảm rõ nhóm lỗi "model viết lại làm sai" — chưa đo.
- **Cắt 1 lời gọi model:** bỏ bước phân loại lý do bằng model (chỉ dùng từ khóa) giảm ~1/3 token vào, nhưng mất khả năng hiểu lý do diễn đạt lạ (trace lượt 1: model và từ khóa lệch ở 5 câu).
- Hosting, lưu trữ log: chưa tính.
