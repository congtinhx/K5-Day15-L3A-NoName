# Tóm tắt mô phỏng simulate-2@20261128-114428

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 26 | 1 | 584 | 92 | 2.0 | 4.2 |
| dung_vua | 17 | 1 | 577 | 95 | 2.0 | 4.2 |
| dung_nhieu | 7 | 1 | 597 | 102 | 2.0 | 4.3 |

Tỉ lệ đạt dùng để tính: 18/25 (72%) — lượt run-2@20261128-024240

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (41.000 người) | Chi phí / tháng — cơ sở (205.000 người) | Chi phí / tháng — cao (410.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-5.4-nano (vào 0.2 · ra 1.25 $/1M) | $0.00023 | $0.00033 | $0.00033 | $3.00 | $15.00 | $30.01 | $0.000073 |
| gpt-5.4-mini (vào 0.75 · ra 4.5 $/1M) | $0.00086 | $0.0012 | $0.0012 | $11.02 | $55.11 | $110.23 | $0.00027 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.0) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gpt-5.4-nano. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
