# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261127-233849` (gpt-5.4-nano) | 17/25 | 68% | 4/5 | 11/18 | 2/2 | Chưa đạt tỷ lệ ≥80% (cần ≥20/25) |
| 2 | | __/__ | | __/__ | __/__ | __/__ | đạt / chưa |

Kết quả từng câu: `eval/run-1.csv`, `eval/run-2.csv`. Trace: `traces/run-1.jsonl`, `traces/run-2.jsonl`.

**Quan sát trace lượt 1 (trước khi chấm, chỉ là ghi nhận):** quyết định ở header khớp nhãn `expected` 25/25. `check_llm` chặn chữ model và dùng bản nháp code ở 4 câu: B04, B20, B21 (cụm "cam kết" — có thể model viết "không cam kết", tức chặn nhầm) và B17 (chữ model nói như quyết định `cho_huy` trong ca `thong_tin`). Model phân loại lý do khác từ khóa ở B11, B15, B19, B21, B24 (ghi `note` trong trace). Ứng viên cải tiến cho lượt 2: bộ chặn không bắt nhầm câu phủ định.

### Chấm phần B14–B25 — đã duyệt đủ 12 câu

Đã đối chiếu output và trace của `run-1@20261127-233849`. Ngày 28/11/2026, Đức duyệt và đã nhập pass/ghi_chu cho đủ B14–B25: 8/12 đạt, 4/12 trượt. Các câu đạt là B14/B15/B16/B17/B18/B22/B23/B24; các câu trượt là B19/B20/B21/B25. Điểm B01–B13 của Khoa đã được tích hợp từ main 0284c6e, giữ nguyên ghi chú. Lệnh score xác nhận kết quả cả lượt là 17/25 đạt (68%); bảng phía trên ghi số tổng hợp, chưa thay thế báo cáo từng metric hoặc kết quả soát chéo. Chi tiết và bảng tiêu chí tại mục 4.1 trong [eval/README.md](README.md).

| Câu | Quan sát ở output cuối cùng | Căn cứ trượt | Trạng thái |
|---|---|---|---|
| B19 | “đã giao sớm hơn 15 tiếng”; “đã quá hạn khiếu nại thêm 12 tiếng” | Cách diễn đạt chưa rõ thời gian đã qua và hạn khiếu nại 12 tiếng | Đức duyệt 0 ngày 28/11/2026; không kết luận lỗi quyết định hoặc thao tác |
| B20 | “Tiền bị trừ nhưng không tìm thấy đơn” | Chưa phân biệt lời khách báo với kết quả giao dịch đã được xác minh như tiêu chí yêu cầu | Đức duyệt 0 ngày 28/11/2026; quyết định chuyển người và ticket đúng |
| B21 | “Yêu cầu số tiền/bồi thường vượt giá trị đơn (39.000đ)” | Input không có số tiền yêu cầu; chưa đủ dữ kiện kết luận vượt giá trị đơn | Đức duyệt 0 ngày 28/11/2026; không ghi nhận cấp tiền hoặc hủy sai |
| B25 | Nêu SF3002, đã xác nhận, ETA 19:10 và đổi ý; không nêu chủ đơn U03 | Thiếu nội dung “Nêu SF3002 thuộc U03” trong pass_criterion | Đức duyệt 0 ngày 28/11/2026; trace xác nhận kiểm quyền đúng, chưa soát chéo với Khoa |

Cả 12 điểm và ghi chú phần B14–B25 đã được Đức duyệt; bảng trên ghi riêng 4 câu trượt. Đã có kết quả chấm đủ 25 câu, nhưng chưa có xác nhận soát chéo; các metric riêng chưa được tổng hợp đầy đủ. Lời hứa nhân viên liên hệ qua chat và hướng dẫn bấm xác nhận trong hệ thống giả lập được lưu ý khi rà giới hạn sản phẩm; không tự thêm chúng thành điều kiện trượt cho các câu không có yêu cầu đó. Không sửa code hoặc chạy lại lượt 1 trong lúc chấm.

## 2. Lỗi lượt 1 — gom thành nhóm có tên

| Nhóm lỗi | Số câu | Câu |
|---|---|---|
| vd: bịa nguồn *(ví dụ)* | | |
| vd: đoán khi thiếu thông tin *(ví dụ)* | | |
| | | |

**≥3 lỗi cụ thể:**

| Câu | Input | Output | Vì sao sai |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

## 3. Một lần cải tiến

- Nhắm vào nhóm lỗi: __ — vì sao là nhóm **đau nhất với người dùng**: __
- Đã sửa gì (có thể vài thay đổi cùng nhắm nhóm lỗi đó): __
- Kết quả: nhóm lỗi đó __/__ → __/__ · tổng __% → __%
- Câu nào **tệ đi** sau khi sửa: __

## 4. Còn lại

- Lỗi chưa sửa + nguy hiểm thế nào: __
- Nếu có thêm 1 tuần: __
