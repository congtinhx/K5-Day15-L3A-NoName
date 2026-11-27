# AI SPEC — Yêu cầu hủy đơn ShopeeFood đã thanh toán · Nhóm NoName · Phòng [XXX] · Zone [X]

> Mốc nộp: §7 chốt chuẩn "đạt" tại **CP2 19:30 Thứ Sáu 27/11** · §0–§7 nộp **CP3 10:00 Thứ Bảy 28/11** · đủ §0–§10 **CP4 14:30 Thứ Bảy 28/11** · §10 changelog ghi tiếp đến **23:59 Thứ Bảy 28/11**.
> Đầu mỗi mục ghi bước guide (`02-guide.md` trong repo đề) chỉ cách điền. Mỗi mục ngắn, có số và nguồn; chi tiết để ở file được trỏ tới. Xoá dòng hướng dẫn trong ngoặc vuông khi điền xong.

Track: [ ] A · [ ] B · [ ] C · [x] D · [ ] E — bài toán: D1 · Xử lý khiếu nại đơn giao đồ ăn → lát cắt: yêu cầu hủy đơn ShopeeFood đã thanh toán trước
Data BTC cấp đã dùng (nếu có — không commit nguyên file): không có (Track D không có data BTC). Dùng review công khai Google Play + trang trợ giúp ShopeeFood; data đơn hàng sẽ là data giả lập có seed.

## §0. Hiện tại việc này diễn ra thế nào *(guide 1.1)*
- Luồng hiện tại trên app ShopeeFood (theo Trung tâm Trợ giúp ShopeeFood, xem 27/11/2026; ảnh chụp từ tài khoản nhóm sẽ bổ sung):
  1. Khách đặt món, thanh toán trước (ShopeePay/thẻ) hoặc tiền mặt.
  2. Khách chỉ tự hủy được bằng nút **Hủy đơn hàng** ở cuối trang Chi tiết đơn hàng khi quán chưa xác nhận làm món hoặc chưa có tài xế nhận đơn (help.cs.shopeefood.vn/portal/102/article/71090).
  3. Khi nút hủy mờ (quán đã xác nhận / tài xế đang giao), ShopeeFood đề nghị khách tiếp tục đơn (article/71096); nếu quán làm món lâu, ShopeeFood đề nghị khách chờ thêm (article/71321).
  4. Muốn hủy sau đó → khách phải **Chat với ShopeeFood** và trao đổi với hỗ trợ.
  5. Đơn hủy vì khách đổi ý → không hoàn tiền, Shopee Xu, mã khuyến mãi (category/595/596). Đơn cần hoàn tiền / đã trừ tiền mà chưa hoàn thành → ShopeeFood kiểm tra giao dịch 1–3 ngày làm việc (portal/102). Hủy quá 2 đơn không lý do chính đáng → khóa tài khoản vĩnh viễn (Quy chế hoạt động, portal/103/article/73880).
- Công cụ / AI đang được dùng: trợ lý chat trong app Shopee/ShopeeFood; một review 1★ (24/10/2026) phàn nàn trợ lý tự động trả lời không đúng — cơ chế bên trong **chưa kiểm**.

## §1. Người dùng & bằng chứng *(guide 1.1, 1.2)*
- Người dùng chính (một vai cụ thể): sinh viên 18–24 tuổi đặt đồ ăn qua ShopeeFood, thanh toán trước bằng ShopeePay/thẻ, muốn hủy đơn vì chờ lâu, đặt nhầm hoặc đổi kế hoạch.
- Việc họ cố làm xong: hủy một đơn đồ ăn vừa đặt và biết chắc có được hoàn tiền không, bao nhiêu, khi nào.
- Hôm nay họ giải bằng gì, hỏng ở đâu, vì sao chưa bỏ: bấm nút hủy (chỉ được khi quán chưa xác nhận) hoặc chat hỗ trợ; hỏng ở chỗ nút hủy mờ mà không giải thích, hỗ trợ trả lời mẫu/chậm, không báo trước hủy thì mất gì; chưa bỏ vì ShopeeFood rẻ, nhiều voucher và là kênh duy nhất để xử lý đơn đã đặt.
- Pain: sinh viên muốn hủy đơn đồ ăn vừa đặt — không hiểu vì sao không hủy được và hủy thì mất bao nhiêu tiền/Xu/mã — phải chat nhiều lần, chờ 1–3 ngày làm việc nếu tiền đã bị trừ, hoặc mất tiền khi hủy vì đổi ý.
- Bằng chứng — số chính + kết luận (chi tiết: `evidence/data-mining.md`): 220 review 1–2★ mới nhất trên Google Play (27/11/2026) → **35/220 = 16%** nhắc hủy đơn; 17/220 = 7,7% than không cho hủy; 4/220 bị trừ tiền mà không hoàn. Đếm bằng từ khóa — đọc tay lại trước CP2. Giả thuyết ban đầu "thiếu món" chỉ 3/220 = 1,4% → đã đổi hướng. Khảo sát ≥20 và phỏng vấn ≥3 đang làm để kiểm lại.

## §2. Impact & quyết định chọn *(guide 1.3)*

Cơ sở: lớp L3 ~700 học viên (02-guide.md mục 4.2). Giả định *(tự ước tính)*: 60% đặt ShopeeFood ≥1 lần/tuần → ~420 người. Tỉ lệ review: `evidence/data-mining.md`.

| Hướng | Bao nhiêu người gặp | Bao nhiêu lần / tháng | Mỗi lần tốn gì | Impact / tháng | Làm kịp không | Chọn? |
|---|---|---|---|---|---|---|
| **Hủy đơn** (review: 35/220 = 16%) | 420 × 20% ≈ 84 *(tự ước tính)* | 1 lần/người → ~84 lần | ~15 phút chat/chờ hỗ trợ + ~10% ca mất ~60.000đ do hủy vì đổi ý không biết luật *(tự ước tính)* | 84 × 15 = 1.260 phút ≈ **21 giờ** + 84 × 10% × 60.000đ ≈ **0,5 triệu đ** | Có — luật trạng thái đơn rõ, có nguồn chính thức, kiểm được bằng code | **Chọn** |
| Giao trễ, chờ lâu (review: 67/220 = 30%) | 420 × 50% ≈ 210 *(tự ước tính)* | 2 lần/người → ~420 lần | ~10 phút chat/chờ hỗ trợ *(tự ước tính)* | 420 × 10 = 4.200 phút ≈ 70 giờ | Có, nhưng mức bù trễ phải tự đặt toàn bộ — ShopeeFood VN không công bố | Loại |
| Thiếu món (review: 3/220 = 1,4%) | 420 × 5% ≈ 21 *(tự ước tính)* | 1 lần → ~21 lần | ~20 phút + ~35.000đ món *(tự ước tính)* | ≈ 7 giờ + 0,3 triệu đ | Có | Loại |

- **Impact / tháng** của hướng chọn = 84 người × 1 lần × 15 phút = 1.260 phút ≈ 21 giờ (+ ≈ 0,5 triệu đ tiền mất do hủy vì đổi ý) — nguồn từng thừa số: 700 học viên (02-guide.md 4.2); 60% đặt hàng tuần, 20% gặp vấn đề hủy, 15 phút/lần, 10% ca mất 60.000đ *(tự ước tính — thay bằng số khảo sát trước CP3)*.
- Hướng ĐÃ LOẠI + vì sao:
  - Giao trễ: bằng chứng mạnh nhất (30%) nhưng chính sách bù trễ không công khai → chuẩn đạt phải dựa trên luật tự đặt; hệ thống cũng không rút ngắn được thời gian giao. Giữ ca "muốn hủy vì chờ lâu" làm câu thử `kho`.
  - Thiếu món: giả thuyết ban đầu, review chỉ 1,4% — dưới ngưỡng 15%.
- Số lần / tháng của từng kiểu người dùng *(tự ước tính, dùng cho persona ở §8)*: ít đặt (1–3 đơn/tháng, ~0,1 lần muốn hủy/tháng) 50% · vừa (4–8 đơn/tháng, ~0,3 lần/tháng) 35% · nhiều/đặt hộ nhóm (>8 đơn/tháng, ~1 lần/tháng) 15%.

## §3. Giải pháp tương tự *(guide 2.1)*
- [sản phẩm / tính năng gần giống]: một điều đáng học · một điều đáng né · mình khác gì

## §4. Thiết kế *(guide 2.2, 3.2)*
- **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả):
- Không làm (≥3 điều):
- **Sơ đồ** (ảnh / Mermaid / draw.io): [chèn ở đây]
- **Hình dạng:** [ ] workflow cố định · [ ] một agent · [ ] nhiều agent — 2 dòng lý do, và vì sao **không** chọn hình dạng phức tạp hơn:
- **AI dựa vào đâu** — mỗi công cụ (khớp `codebase/tools.py`):

  | Công cụ | Input | Output | Tác động ra ngoài? |
  |---|---|---|---|
  |  |  |  |  |

- **Mức tự động:** [ ] AI gợi ý, người quyết · [ ] AI tự làm khi chắc, chuyển người khi không · [ ] AI tự làm — lý do (sai thì ai chịu gì, sửa đắt hay rẻ):
- **Chỗ chặn rủi ro** (rủi ro lớn nhất của lát cắt bị chặn ở đâu, bằng gì):
- **Chỗ người duyệt** (việc AI không được tự làm):
- **Nguyên tắc thiết kế** (≥3, bắt buộc G10):

  | Nguyên tắc | Chỗ cụ thể trên sơ đồ / trong bản chạy thử |
  |---|---|
  | G10 — thu hẹp phạm vi khi không chắc |  |
  |  |  |
  |  |  |

- Phần nào còn giả (công cụ trả dữ liệu giả, model chế độ giả…) — ghi rõ, không giả làm thật:

## §5. Chỗ khó — 4 lớp + ≥6 kịch bản + 2 tấn công *(guide 2.3)*

| Kịch bản | Lớp (1–4) | Hành vi mong muốn (nói gì, hiện gì, cho làm gì tiếp) | Câu thử |
|---|---|---|---|
|  |  |  |  |
| *(tấn công)* |  |  |  |
| *(tấn công)* |  |  |  |

(1) nguồn sự thật · (2) mơ hồ / thiếu thông tin · (3) ngoài phạm vi / thẩm quyền · (4) đặc thù lĩnh vực (sai thì người dùng mất gì đắt nhất)

## §6. Bốn đường đi của trải nghiệm
- Mọi thứ suôn sẻ: · Không chắc (lớp 2): · Không có căn cứ (lớp 1): · Người dùng sửa:
- Bị đòi ngoài phạm vi (lớp 3): · Trường hợp đặc thù lĩnh vực (lớp 4):

## §7. Đánh giá & chuẩn "đạt" *(guide 2.4, 4.1)*
- Data card: `data/DATA_CARD.md` · bộ câu thử: `eval/benchmark.csv` — __ câu (thuong __ · kho __ · tu_choi __) · metric: `eval/metric_spec.yaml` (__ metric)
- **Chuẩn "đạt"** (chốt **trước 19:30 Thứ Sáu 27/11**, giữ nguyên đến 23:59 Thứ Bảy 28/11): "Đạt khi ≥ __% câu qua, và __"
- Kết quả: lượt 1 __/__ (__%) · lượt 2 __/__ (__%) — run ID: __ / __ → chi tiết `eval/report.md`, hồ sơ `eval/README.md`

## §8. Chi phí khi dùng thật *(guide 4.2)*
- Persona + giá: `cost/personas.yaml` · lượt mô phỏng: `cost/simulate-__.csv` (__ phiên)
- Chi phí / task thành công: __ (model __) · __ (model __)
- Chi phí / tháng ở quy mô thật: thấp __ · cơ sở __ · cao __ → chi tiết `cost/cost-estimate.md`
- So với impact / người / tháng (§2): đáng làm không, vì sao:

## §9. Rủi ro & an toàn
- Dữ liệu: đã ẩn danh gì, không thu gì, không đưa gì vào model gói miễn phí:
- AI **không được** làm gì kể cả khi người dùng yêu cầu:
- Ai có thể bị hại nếu AI sai, và nhóm chặn thế nào:

## §10. Phân công & changelog
- Phân công có tên (theo chặng, chia cặp — guide "Cách chia việc"): __
- Dùng AI vào việc gì (2–3 dòng; chi tiết `docs/ai-usage.md`):
- Nhật ký thay đổi — **mọi thay đổi sau CP2 19:30 Thứ Sáu 27/11 phải có dòng ở đây**:

**CP2 → CP4** (vd thu hẹp lát cắt, hỏi thêm người dùng, lần cải tiến trước lượt 2)

| Thời điểm | Đổi gì | Vì sao (trỏ về câu thử / lỗi / bằng chứng nào) |
|---|---|---|
|  |  |  |

**Sau CP4 (đến 23:59 Thứ Bảy 28/11)** (sửa theo góp ý — không sửa chuẩn "đạt", câu thử, số bằng chứng, kết quả các lượt đã chạy)

| Thời điểm | Đổi gì | Vì sao |
|---|---|---|
|  |  |  |
