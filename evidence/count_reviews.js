// evidence/count_reviews.js
// Đếm nhãn trên review Google Play của ShopeeFood (com.deliverynow).
// Cách chạy (Chrome):
//   1. Mở https://play.google.com/store/apps/details?id=com.deliverynow&hl=vi&gl=VN
//   2. Bấm "Xem tất cả bài đánh giá" → chọn "Mới nhất" → lọc "1 sao" (lần 2: "2 sao").
//   3. Mở DevTools (F12) → Console → dán toàn bộ file này → Enter.
//   4. Chạy cho 1★ (LIMIT = 120) và 2★ (LIMIT = 100), cộng kết quả.
// Script không lưu tên người viết. Selector của Google Play có thể đổi theo thời gian.

const LIMIT = 120; // 120 cho 1★, 100 cho 2★

const CATS = {
  huy_don: /hủy|huỷ|huy don/i,
  khong_huy_duoc: /(không|ko|k) (cho )?hủy|không hủy được|ko hủy được/i,
  tru_tien_khong_hoan: /(trừ tiền|thanh toán).{0,80}(không|ko|k) hoàn|(không|ko|k) hoàn (lại )?tiền/i,
  giao_tre: /lâu|trễ|muộn|chậm|tiếng|ghép đơn|\b1h|\b2h|phút/i,
  ghep_don: /ghép đơn|ghep don|gom đơn/i,
  gia_phi_voucher: /phí|giá|đắt|voucher|deal|mã giảm|freeship|xu/i,
  tai_xe: /tài xế|shipper|bom hàng|thái độ/i,
  chat_luong_mon: /nguội|ôi|thiu|dở|tóc|gián|đổ |chảy|nhựa|bẩn|hỏng/i,
  app_dia_chi: /địa chỉ|vị trí|định vị|bug|lỗi app|đăng nhập|cập nhật|giao diện|không vào được/i,
  thanh_toan: /thanh toán|trừ tiền|shopeepay|ví |tiền mặt|chuyển khoản/i,
  cskh_hoan: /hoàn tiền|hoàn lại|khiếu nại|cskh|hỗ trợ|chăm sóc|tổng đài|bồi hoàn|đền bù|đền|report|chat với|phản hồi/i,
  thieu_mon: /thiếu|thieu|mất món|sót món|không có món|ko có món|k có món|thiếu đồ|thiếu nước/i,
};

(async () => {
  const dlg = document.querySelector('div[role=dialog]');
  const scroller = [...dlg.querySelectorAll('div')]
    .find(d => d.scrollHeight > d.clientHeight + 50 && getComputedStyle(d).overflowY !== 'visible');
  for (let i = 0; i < 40 && dlg.querySelectorAll('.RHo1pe').length < LIMIT; i++) {
    scroller.scrollTop = scroller.scrollHeight;
    await new Promise(r => setTimeout(r, 700));
  }
  const reviews = [...dlg.querySelectorAll('.RHo1pe')].slice(0, LIMIT).map(e => ({
    date: (e.querySelector('.bp9Aid') || {}).textContent || '',
    text: ((e.querySelector('.h3YV2d') || {}).textContent || '').replace(/\s+/g, ' '),
  }));
  const counts = {};
  for (const k in CATS) counts[k] = reviews.filter(r => CATS[k].test(r.text)).length;
  const none = reviews.filter(r => !Object.values(CATS).some(re => re.test(r.text))).length;
  console.log({ N: reviews.length, from: reviews.at(-1)?.date, to: reviews[0]?.date, counts, none });
})();
