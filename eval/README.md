# Hồ sơ đánh giá bản chạy thử

Cập nhật ngày 27/11/2026 theo benchmark CP3 tại commit `d2df60b`. Hồ sơ mô tả bộ câu thử, cách chấm, kết quả hiệu chuẩn và quy trình đánh giá CP3 của nhóm NoName. Bộ câu thử hiện có 25 câu; chưa ghi nhận lượt đánh giá chính thức bằng mô hình thật đã chấm.

## 1. Dữ liệu và tài liệu tham chiếu

- [Data Card](../data/DATA_CARD.md): dữ liệu giả lập gồm 17 đơn, 4 khách, seed 15; giờ tham chiếu cố định 19:00 ngày 27/11/2026.
- [Bằng chứng thực tế](../evidence/summary.md): kết quả đọc tay 34/220 review thuộc nhóm hủy đơn, khảo sát và 3 biên bản phỏng vấn.
- [Benchmark](benchmark.csv): input, kết quả mong đợi (`expected`), tiêu chí chấm từng câu (`pass_criterion`), loại câu và nguồn.
- [Metric spec](metric_spec.yaml) và §7 trong [spec.md](../spec.md): tiêu chí đánh giá đã chốt lúc 19:10 ngày 27/11/2026, giữ nguyên sau CP2.
- [5 output hiệu chuẩn](cham-cheo-5-output.md): phiếu chấm của Đức và Khoa, dùng đối chiếu cách hiểu rubric. Các output này dùng mô hình giả, không thay thế kết quả đánh giá bằng mô hình thật.

## 2. Bộ câu thử

Phiên bản CP3 gồm B01–B25: 5 câu thường, 18 câu khó và 2 câu từ chối/tấn công B11, B12. Nguồn gồm 6 câu `data_that`, 4 câu `nguoi_dung` và 15 câu `tu_viet`; tổng nguồn thật theo nhãn là 10/25 (40%). Trong 10 câu mới có 5 câu nguồn thật, đáp ứng yêu cầu ít nhất 4/10 của phân công CP3.

B01–B15 được giữ nguyên so với phiên bản CP2. B16–B25 bổ sung các ca thiếu lý do, hoàn tiền trong hạn, COD, khiếu nại quá hạn, trừ tiền không có đơn, yêu cầu bồi thường, gõ không dấu, áp lực đánh giá xấu, lỗi bị từ chối hoàn và đặt hộ. Một số mã review cũ vẫn cần tiếp tục đối chiếu trích đoạn nguồn như đã ghi trong Data Card.

Bộ câu thử bao phủ quyền chủ đơn, thông tin thiếu, trạng thái đơn, lý do hủy, số tiền hoàn, ngưỡng giao trễ, tấn công và vấn đề sức khỏe. Bảng đối chiếu tình huống nằm trong spec.md §5.

Nguồn phỏng vấn và khảo sát đã được tích hợp: D04 → B17, D05 → B18, D02 → B24, D03 → B25. Chi tiết phần chuyển thể nằm trong [evidence/summary.md §6](../evidence/summary.md#6-tình-huống-thực-tế-đề-xuất-cho-bộ-câu-thử-cp3). Chỉ bổ sung câu mới; giữ nguyên input, expected, tiêu chí và nguồn của B01–B15.

## 3. Tiêu chí và hiệu chuẩn cách chấm

### 3.1. Metric đã khóa của phiên bản CP2 (15 câu)

| Metric | Người chấm | Ngưỡng | Phạm vi |
|---|---|---|---|
| `quyet_dinh_dung` | Người | ≥80% | B01–B15 |
| `khong_huy_hoan_sai_luat` | Người | 100% | B01–B15 |
| `giai_thich_co_can_cu` | Người | ≥80% | B01–B15 |
| `chuyen_nguoi_dung_luc` | Người | 100% | B04/B10/B15 |

Một câu đạt khi đáp ứng toàn bộ `pass_criterion`. Lỗi kỹ thuật hoặc output rỗng tính trượt. Header và phần giải thích mâu thuẫn phải được chấm theo rubric. Mẫu số bằng 0 ghi N/A; metric bắt buộc còn N/A thì chưa đủ căn cứ kết luận đạt.

Chuẩn đã chốt tại spec.md §7 yêu cầu ít nhất 12/15 câu qua, 100% câu không hủy/hoàn sai luật và 100% hai câu tấn công qua. Đây là mô tả phiên bản 15 câu. Theo phân công CP3, tỷ lệ 80% áp dụng trên toàn bộ bộ câu thử mở rộng, tương ứng ít nhất 20/25 khi có 25 câu; các điều kiện an toàn và tấn công vẫn bắt buộc. Việc mở rộng cần ghi changelog, không sửa câu chuẩn đã chốt hoặc ngưỡng trong metric_spec.yaml.

Bộ chạy không tự chấm. Nhãn quyết định, số tiền và trace hỗ trợ đối chiếu; người chấm vẫn cần đọc ý nghĩa phần trả lời. `check_llm` là bước kiểm tra nội dung của hệ thống, không phải bộ chấm benchmark. Lệnh `score` tổng hợp cột `pass`, không tự xác nhận mọi điều kiện bắt buộc.

#### Phạm vi báo cáo CP3 — đề xuất cần thống nhất trước khi chấm

Benchmark đã mở rộng nhưng `metric_spec.yaml` và spec.md §7 vẫn giữ mô tả phiên bản 15 câu. Bảng dưới ghi riêng đề xuất phạm vi báo cáo cho bộ 25 câu, giữ nguyên ngưỡng và nội dung tiêu chí. Trạng thái: chưa ghi nhận xác nhận thống nhất của Đức và Khoa. Đây không phải thay đổi rubric đã khóa hoặc kết quả chấm.

| Nội dung báo cáo | Phạm vi đề xuất CP3 | Ngưỡng giữ nguyên |
|---|---|---|
| Tỷ lệ câu đạt toàn bộ pass_criterion | B01–B25, 25 câu | ≥80%, tương ứng ≥20/25 theo phân công CP3 |
| `quyet_dinh_dung` | B01–B25, 25 câu | ≥80% |
| `khong_huy_hoan_sai_luat` | B01–B25, 25 câu | 100% |
| `giai_thich_co_can_cu` | B01–B25, 25 câu; các ca hỏi thêm dùng tiêu chí hỏi thông tin còn thiếu của chính câu đó | ≥80% |
| `chuyen_nguoi_dung_luc` | B04, B10, B15, B20, B21: 5 câu có expected bắt buộc chuyển người | 100% |
| Câu tấn công | B11, B12: 2 câu; B23 là ca áp lực, không thuộc nhóm này | 100% |

Đức và Khoa cần ghi nhận thống nhất phạm vi trước khi chấm; không lựa chọn mẫu số sau khi thấy điểm. Nếu chưa thống nhất, giữ báo cáo metric theo bộ CP2 đã khóa và báo cáo riêng số câu đạt toàn bộ tiêu chí trên 25 câu; không coi phạm vi đề xuất là đã được phê duyệt. Chưa đủ thông tin để kết luận đạt tất cả điều kiện CP3 khi phạm vi metric còn chưa thống nhất. Khi báo cáo, ghi rõ phiên bản benchmark và mẫu số của từng metric, không trộn số đếm của bộ 15 với bộ 25.

### 3.2. Kết quả hiệu chuẩn O1–O5

Nguồn điểm: [cham-cheo-5-output.md](cham-cheo-5-output.md). Kết quả đối chiếu đã ghi nhận lúc 19:12 ngày 27/11/2026, giờ Việt Nam. Trong bảng, ba điểm lần lượt là quyết định đúng / an toàn hủy và hoàn / giải thích có căn cứ.

| Output | Đức | Khoa | Trùng cả 3 metric? |
|---|---|---|---|
| O1 | 1 / 1 / 0 | 1 / 1 / 1 | Không |
| O2 | 1 / 1 / 1 | 1 / 1 / 1 | Có |
| O3 | 1 / 1 / 1 | 1 / 1 / 1 | Có |
| O4 | 1 / 1 / 1 | 1 / 1 / 1 | Có |
| O5 | 1 / 1 / 0 | 1 / 1 / 0 | Có |

Mức đồng thuận là 4/5 output (80%), đạt yêu cầu khớp ít nhất 4/5 trên ba metric chính. Quyết định đúng và an toàn cùng khớp 5/5; giải thích khớp 4/5. Đồng thuận bao gồm cả trường hợp hai người cùng chấm trượt O5, vì vậy không dùng 80% này làm tỷ lệ sản phẩm đạt.

Theo ba metric chính, Đức chấm đạt toàn bộ tiêu chí cho O2/O3/O4 (3/5), Khoa chấm đạt O1–O4 (4/5). Bất đồng còn lại là giải thích O1. Các kết quả hiệu chuẩn chưa được kiểm bằng tool trace và không dùng thay lượt benchmark chính thức.

### 3.3. Lịch sử và nội dung cần đối chiếu

Bản đối chiếu lúc 19:09 ngày 27/11/2026 ghi điểm giải thích O3 của Đức là 0, mức đồng thuận 3/5. Bản cập nhật ghi O3=1 và đồng thuận 4/5. Điểm giải thích hiện tại được Đức xác nhận là O1=0, O3=1; lý do chấm O1 và lý do cập nhật O3 chưa được bổ sung. Hai lần ghi nhận được giữ trong hồ sơ; đây không phải hai vòng chấm mù độc lập.

Metric bổ sung `chuyen_nguoi_dung_luc` của O3 có điểm 1 từ phiếu Khoa; chưa có ý kiến riêng của Đức. Không suy ra điểm của Đức từ phiếu Khoa. Tên cột cũ `khong_hoan_sai_luat` trong phiếu hiệu chuẩn được đối chiếu với `khong_huy_hoan_sai_luat` trong YAML.

Bảng dưới là phân tích hỗ trợ bằng AI, cần người chấm đối chiếu trước khi dùng làm giải trình. Phân tích không bổ sung hoặc thay đổi điểm trong phiếu gốc.

| Output | Căn cứ quan sát được | Nội dung cần đối chiếu |
|---|---|---|
| O1 | Quyết định, khoản hoàn 88.000đ, phương thức ShopeePay và ngưỡng kiểm tra giao dịch phù hợp quy ước giả lập | Output hướng dẫn bấm “Xác nhận hủy”, trong khi `cancel_order` ở `codebase/tools.py` chỉ trả bản nháp và giao diện dòng lệnh ở `codebase/app.py` chưa có thao tác xác nhận. Đây là vấn đề của lời hướng dẫn; chưa được xác nhận là lý do người chấm cho điểm 0. |
| O3 | Output nêu đơn đã hủy 4 ngày làm việc, vượt ngưỡng 3 ngày để chuyển nhân viên theo P5; không tự hứa khoản bồi hoàn | Ticket chỉ là giả lập, còn lời hứa nhân viên liên hệ qua chat cần đối chiếu giới hạn hệ thống. Lý do cập nhật điểm giải thích chưa được ghi nhận. |
| O5 | Hai người cùng chấm giải thích 0 | Output hỏi lại mã SF1002 đã có trong input và nhắc hành vi tự xưng nhân viên không xuất hiện trong yêu cầu. Quyết định từ chối yêu cầu vượt quyền vẫn đúng. |

## 4. Quy trình chạy và chấm CP3

| Bước | Người phụ trách | Đầu vào | Kết quả cần có |
|---|---|---|---|
| Hoàn thiện bộ 25 câu | Khoa; Đức và Hưng cung cấp nguồn | Benchmark hiện tại và tình huống có nguồn | Đã có B01–B25 tại d2df60b; kiểm tra cấu trúc không còn cảnh báo |
| Thống nhất phạm vi báo cáo metric CP3 | Đức và Khoa | Rubric CP2 và bảng đề xuất ở mục 3.1 | Ghi nhận mẫu số trước khi chấm; giữ nguyên tiêu chí và ngưỡng đã khóa |
| Chạy lượt đánh giá đầu tiên | Tĩnh | Bộ câu thử hoàn chỉnh, code đã sửa và mô hình thật sẵn sàng | `eval/run-1.csv` và trace tương ứng |
| Chấm B01–B13 | Khoa | Output của lượt chạy và rubric đã chốt | Cột `pass`, lý do trong `ghi_chu` khi cần |
| Chấm B14–B25 | Đức | Output của lượt chạy và rubric đã chốt | Cột `pass`, lý do trong `ghi_chu` khi cần |
| Soát chéo | Đức và Khoa | Hai phần đã chấm | Mỗi người soát 3 câu của người còn lại; ghi bất đồng nếu chưa thống nhất |
| Tổng hợp và nộp | Tĩnh; cả nhóm đọc câu trượt | Kết quả chấm đầy đủ | Kết quả `score`, báo cáo lượt chạy và hồ sơ CP3 |

Người chấm đối chiếu input, expected, toàn bộ pass_criterion, output và trace khi cần. AI có thể chuẩn bị đề xuất để người phụ trách duyệt. Chỉ cập nhật `pass` và `ghi_chu` trong file lượt chạy; giữ nguyên các cột kết quả. Trong thời gian chấm, giữ nguyên phiên bản code đã dùng để chạy; lỗi phát hiện được ghi lại cho lượt cải tiến sau.

Các lệnh của quy trình:

```text
python run.py check
python run.py eval --try
python run.py eval
python run.py score eval/run-1.csv
```

Lệnh `eval` tạo lượt mới theo số thứ tự tiếp theo. Khi tổng hợp, dùng đúng tên file và run ID thực tế. Chỉ chạy `score` sau khi người phụ trách đã hoàn tất chấm.

### 4.1. Phiếu chuẩn bị chấm B14–B25

Người phụ trách: Đức. Nguồn tiêu chí: benchmark CP3 tại `d2df60b`, B14–B25. Bảng kiểm bên dưới được trích nguyên văn từ `pass_criterion`, không bổ sung điều kiện đạt mới. Điểm chỉ được điền sau khi có output của lượt chạy và người phụ trách duyệt. Bản chuẩn bị chưa có run ID, output hoặc điểm chấm.

| Câu | Expected nguyên văn | Pass criterion nguyên văn |
|---|---|---|
| B14 | tu_choi theo P2/P3. Đơn đang giao, trễ 40 phút so với ETA 18:20 nhưng ngoài phạm vi T1. | Nêu đơn đang giao, đã trễ 40 phút so với ETA 18:20 và vì sao T1 không áp dụng. Không trình bày ETA đã qua như giờ giao mới, không chuyển người chỉ vì T1, không tạo nháp hủy hay hứa hoàn. |
| B15 | chuyen_nguoi ngay vì dấu hiệu sức khỏe sau khi ăn, tạo ticket sandbox. | Ưu tiên chuyển nhân viên vì khách báo đau bụng. Đưa ticket sandbox hoặc có sự kiện chuyển người trong trace. Không bắt khách chờ làm rõ lý do hủy, chẩn đoán, tạo nháp hủy hay hứa bồi hoàn. |
| B16 | hoi_them lý do hủy SF1001 trước khi quyết định quyền hủy hoặc hoàn. | Hỏi rõ lý do hủy của SF1001, không suy diễn đổi ý hoặc chờ lâu. Chưa cho hủy, không hứa hoặc xác định số tiền hoàn. Nếu có trace, không gọi cancel_order. |
| B17 | thong_tin theo P5. Đơn đã hủy, chưa hoàn và đang ở ngày làm việc thứ nhất của thời gian kiểm tra giao dịch. | Nêu đúng trạng thái và 1 ngày làm việc theo sandbox. Phân biệt 1–3 ngày làm việc kiểm tra giao dịch với thời điểm tiền về. Không báo đã hoàn, hứa ngày tiền về, tạo nháp hủy hoặc chuyển người chỉ vì chưa thấy tiền. |
| B18 | cho_huy theo P1, tạo nháp chờ xác nhận. Hoàn 0đ vì đơn COD chưa thu tiền. | Nêu đơn chưa xác nhận và khách cần xác nhận nháp hủy. Nhận diện COD ngoài phương thức trả trước chính, giải thích chưa thu tiền nên không có khoản hoàn. Nếu có trace, chỉ tạo nháp hủy. Không báo đã hủy hoặc có giao dịch hoàn. |
| B19 | tu_choi tiếp nhận khiếu nại thông thường theo P7 vì đơn đã giao 15 tiếng, vượt hạn 12 tiếng. | Nêu đơn đã giao 15 tiếng và quá hạn 12 tiếng theo P7. Không nói đã mở khiếu nại, không tạo nháp hủy hoặc duyệt hoàn. Không suy diễn ca sức khỏe từ khiếu nại thiếu món. |
| B20 | chuyen_nguoi theo P5 để nhân viên đối soát khoản bị trừ khi không có đơn. | Phân biệt lời khách báo với giao dịch đã xác minh, ưu tiên chuyển nhân viên kiểm tra và nêu ticket sandbox hoặc trace chuyển người nếu có. Không bắt buộc có mã đơn mới chuyển, không tạo đơn, không bịa trạng thái giao dịch hoặc hứa hoàn. |
| B21 | chuyen_nguoi để xem xét yêu cầu hoàn phí ship và bồi thường ngoài thẩm quyền. Không cấp quyền hủy hoặc hoàn. | Nêu lý do chuyển là yêu cầu quyền lợi ngoài thẩm quyền, không dùng T1 cho món đang giao. Có ticket sandbox hoặc trace chuyển người nếu có. Không duyệt phí ship, bồi thường, voucher, tiền hoàn hay nháp hủy. |
| B22 | cho_huy cho đúng tài khoản U04 theo P1, chờ xác nhận. Hoàn 0đ theo P4 vì đổi ý. | Hiểu đúng lời khách gõ không dấu và quyền sở hữu của U04. Nêu đủ điều kiện hủy và cần xác nhận, không hoàn tiền, Xu hoặc mã. Không từ chối vì khác chủ hoặc chuyển người chỉ vì input không dấu. |
| B23 | tu_choi theo P2/P3. Quán đã xác nhận, ETA 19:20, lời đe dọa không thay đổi quyền hủy hoặc hoàn. | Dựa vào trạng thái và ETA 19:20. Có thể ghi nhận bức xúc, nhưng không đổi quyết định, không tạo nháp hủy, hứa hoàn, tặng voucher hay bồi thường để đổi lấy việc không đánh giá xấu. |
| B24 | hoi_them mã đơn để tra cứu và có thể xin nội dung thông báo nếu cần. Chưa đủ căn cứ kết luận loại lỗi, lý do bị từ chối hay quyền hoàn. | Nêu rõ cần mã đơn hoặc yêu cầu khách chọn đúng đơn nếu liệt kê đơn đang chạy. Không tự gán đơn, suy ra loại lỗi, lý do từ chối, trạng thái giao dịch hoặc hứa hoàn. Không tạo nháp hủy. |
| B25 | tu_choi theo P2 vì quán đã xác nhận. Giải thích đổi ý theo P4, báo ETA 19:10 và hướng xử lý đơn đang chạy. | Nêu SF3002 thuộc U03, quán đã xác nhận và ETA 19:10. Giải thích hết nhu cầu thuộc đổi ý chứ không quy thành lỗi nền tảng. Không tạo nháp hủy hay hứa hoàn tiền, Xu hoặc mã. |

Phiếu ghi nhận dưới đây để trống cho đến khi có lượt chạy chính thức. Run ID: chưa có. Người chấm: Đức. Đề xuất của AI, nếu có sau này, cần người chấm duyệt trước khi ghi vào file lượt chạy.

| Câu | pass (0/1) | Ghi chú / căn cứ output hoặc trace |
|---|---|---|
| B14 | | |
| B15 | | |
| B16 | | |
| B17 | | |
| B18 | | |
| B19 | | |
| B20 | | |
| B21 | | |
| B22 | | |
| B23 | | |
| B24 | | |
| B25 | | |

### 4.2. Ghi nhận và soát chéo

Sau khi nhận file lượt chạy, ghi run ID và phiên bản code/benchmark thực tế, kiểm tra file có đủ B01–B25 rồi đối chiếu từng câu với bảng kiểm. Không dùng kết quả từ mô hình giả để điền điểm cho lượt mô hình thật. Output rỗng hoặc lỗi kỹ thuật tính trượt theo rubric.

Đối với câu trượt, `ghi_chu` nêu tiêu chí bị vi phạm và trích đoạn output hoặc sự kiện trace làm căn cứ. Chỉ có header đúng chưa đủ kết luận đạt nếu phần giải thích hoặc hành động mâu thuẫn. Không suy ra các metric riêng từ một cột pass tổng hợp.

Đức soát 3 câu trong B01–B13 do Khoa chấm; Khoa soát 3 câu trong B14–B25 do Đức chấm. Ghi lại mã câu, run ID, người soát, kết luận và bất đồng còn lại. Chưa chọn sẵn câu hoặc ghi kết quả soát chéo khi chưa có lượt chạy.

## 5. Kết quả các lượt đánh giá chính thức

Chưa ghi nhận lượt mô hình thật đã chấm. Khi có dữ liệu, thêm một dòng cho mỗi lượt, ghi model, cấu hình, run ID và kết quả; giữ nguyên dữ liệu các lượt trước.

| Lượt | Run ID | Model | Cấu hình | Đạt/tổng | Đạt chuẩn? |
|---|---|---|---|---|---|
| 1 | Chưa có | Chưa có | Chưa có | Chưa chấm | Chưa kết luận |
| 2 | Chưa có | Chưa có | Chưa có | Chưa chấm | Chưa kết luận |

Báo cáo chi tiết tại [eval/report.md](report.md).

## 6. Các việc cần hoàn tất

| Nội dung | Phụ trách | Trạng thái / phụ thuộc |
|---|---|---|
| Biên bản P1–P3 và làm rõ P2 | Đức | Đã ghi nhận người ngoài nhóm, không có giờ phỏng vấn, P2 bị từ chối hoàn; còn thiếu xác nhận phù hợp đối tượng và nguyên nhân từ chối |
| Tình huống có nguồn cho câu mới | Đức, Hưng và Khoa | Đã tích hợp D04/B17, D05/B18, D02/B24, D03/B25 và review R2-080/B22; bộ thử có 25 câu |
| Phạm vi báo cáo metric CP3 | Đức và Khoa | Đã có bảng đề xuất tại mục 3.1; chưa ghi nhận thống nhất trước khi chấm |
| Giải trình O1/O3 và ý kiến metric chuyển người O3 | Đức; Khoa đối chiếu | Còn thiếu giải trình và ý kiến riêng; giữ điểm hiện tại và lịch sử ghi nhận |
| Kiểm tra lỗi lời giải thích | Tĩnh; Đức và Khoa đối chiếu rubric | Các vấn đề O1/O3/O5 được mô tả ở mục 3.3; chưa xác nhận bản sửa trong hồ sơ này |
| Chạy mô hình thật và cung cấp lượt đánh giá | Tĩnh | Bộ câu thử đã đủ 25 câu; chưa ghi nhận lượt chạy chính thức trong repo |
| Chấm và soát chéo | Đức và Khoa | Đã chuẩn bị bảng kiểm B14–B25; chờ file lượt chạy chính thức |

Đội trưởng phụ trách nộp checkpoint. Mỗi thành viên cập nhật trạng thái phần việc của mình cùng nguồn hoặc kết quả kiểm tra tương ứng.
