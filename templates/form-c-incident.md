# Phiếu C · Sự cố và quyết định v2 · Khối 3 (phút 125–200)

**Bàn:** K5-L3A-DAY10-ThieuODien-PoCtoPilotGate1 · **Thẻ đã bốc:** S3 *(ghi đúng số đã bốc; lệnh tự kiểm tra in dòng này trong report.)*

Mở `incidents/Sx/card.md` của đúng số đã bốc. Các bước trên thẻ trỏ về đúng mục trong phiếu này. Mục C3 chỉ điền phần ứng với
số thẻ của bàn; các phần khác để trống.

**Mục lục**
- [C0 · Nhật ký lần chạy vòng 2 (suốt khối)](#c0)
- [C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem · phút 125–135 · bước 0 trên thẻ](#c1)
- [C2 · Câu 3.1 · Bảng soát lỗi của thẻ · phút 135–145 · bước 1–2](#c2)
- [C3 · Câu 3.1 · Phần riêng theo thẻ · phút 135–145 · bước 3](#c3)
- [C4 · Câu 3.1 · HAZOP của thẻ (≥ 3 dòng) · phút 145–150 · bước 4](#c4)
- [C5 · Câu 3.2, 3.3 · Specification và giả định môi trường · phút 145–150 · bước 4](#c5)
- [C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa · phút 150–155 · bước 4](#c6)
- [C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn · phút 155–180 · bước 5–7](#c7)
- [C8 · Câu 3.6 · Chỉ số theo dõi mới · phút 155–180 · bước 5](#c8)
- [C9 · Câu 3.7 · Fault tree SAU khi sửa · phút 180–185 · bước 8](#c9)
- [C10 · Câu 3.7 · Risk register (≥ 1 dòng) · phút 180–185 · bước 8](#c10)
- [C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5 · phút 180–185 (runbook có thể xong trong 185–200) · bước 8](#c11)
- [C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc · phút 185–200 · bước 9](#c12)

---

<a id="c0"></a>

## C0 · Nhật ký lần chạy vòng 2

Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Điền cột "Đổi MỘT thứ gì" (tham số `--note`) và "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | `R-S3-prepared-20261118-174247-66cedf` | S3 · prepared | nhận thẻ S3, chưa sửa thêm (đúng cổng vòng 1 đã chốt) | 0.8333 [0.5833; 1.0] | 0.8333 | 0đ · 10 · 0 | 0.0833 | Cổng vòng 1 đỡ hoàn sai 900.000đ → 0, lỗi hãng oan 35 → 10, ROI −2.59 → 1.51; còn 10 lỗi do chưa có trần 2 lỗi/hãng/ngày. |
| 2 | `R-S3-after-20261118-174231-66cedf` | S3 · after | thêm trần 2 lỗi/hãng/ngày (code) + cấu hình vòng 2 của D (`decision_note`, kiểm mẫu 10%, `legal`) | 1.0 [1.0; 1.0] | 1.0 | 0đ · 0 · 0 | 0.0833 | `S3-42`/`S3-43` không còn ghi lỗi thứ 3/4; 60/60 đạt, không vượt trần; chi phí 4.405đ, ROI 1.27, 0 ca ùn. |
| 3 | `R-S3-after-20261118-174247-66cedf` | S3 · after | lệnh 6 chạy lại trên code + config cuối | 1.0 [1.0; 1.0] | 1.0 | 0đ · 0 · 0 | 0.0833 | Xác nhận `visible ✅`, `monitor ✅`, `regression ✅`; after sạch, `continue_allowed: true` trên visible. `1 integrity ❌` chỉ vì máy thiếu gói S1/S2/S4–S8 (upstream chưa phát), không phải file bàn sửa — cần Coach xác nhận trước khi chọn Tiếp tục. |
| 4 | `R-base-after-20261118-174239-66cedf` | base · after | (kiểm không regression với cấu hình vòng 2 của D) | 1.0 [1.0; 1.0] | 1.0 | 0đ · 0 · 0 | 0.2273 | 110/110 đạt, không ca mới hỏng; chi phí 4.456đ, ROI 1.24, 0 ca ùn. |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident Sx
```

- Mã lần chạy grade: `R-S3-grade-20261118-174246-66cedf` · base: `R-S3-before-20261118-174246-66cedf` · prepared: `R-S3-prepared-20261118-174247-66cedf`
- Cổng vòng 1 đỡ được ô / con số nào (so cột base với cột prepared): hoàn sai **900.000đ → 0**; under-refund **667.000đ → 0**; lỗi hãng oan **35 → 10**; pass_rate **0.25 → 0.8333**; pass_k **0.25 → 0.8333**; ROI **−2.59 → 1.51**; chi phí mỗi ticket **3.147đ → 3.980đ** (vẫn < 10.000đ làm tay); tổng hoàn tự động **180.000đ → 109.400đ**; hàng chờ **0 ca ùn** ở cả ba mốc; PII **0**. Với cấu hình vòng 2 của D ở mốc after: chi phí **4.405đ**, ROI **1.27**, vẫn **0 ca ùn** và **0 lỗi hãng oan**. Trace `S3-01@11`: base dùng `REFUND-v3` (`pinned: false`) nên `FORCE_MAJEURE` vẫn `do_fault: true`; prepared ghim `REFUND-v4` (`pinned: true`) nên `do_fault: false`.
- Khối kinh doanh và vận hành còn dòng nào vượt trần: ở prepared **không còn dòng "vượt trần"**; còn **10 lỗi ghi oan cho hãng** (ngưỡng bắt buộc `wrongful_carrier_faults ≤ 0`), tập trung ở `S3-42`/`S3-43` (lỗi MKD thứ 3, 4 trong ngày).

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- Sự cố trên thẻ thuộc lăng kính nào (kỹ thuật, kinh doanh, con người và vận hành, pháp lý)? **Kỹ thuật** (chính sách hết hiệu lực vẫn được dùng; tracking thiếu nguyên nhân; ghi lỗi theo kiện đầu), **pháp lý** (hãng/bên thứ ba bị phạt oan 120.000đ/lỗi) và **con người – vận hành** (hãng nhận quá nhiều lỗi trong ngày, không ai xác nhận trước khi ghi).
- Có nằm trong các lý do bàn đã viết không? Nếu có: cổng vòng 1 đã đỡ được bao nhiêu (đọc cột prepared trong report)? Nếu không: vì sao cả bàn không nghĩ tới? **Có một phần**: B4 H2 đã nêu "dùng REFUND-v3 sau 2026-11-30" và B6 ★G1 đã nêu quy lỗi sai kiện/thiếu nguyên nhân. Cổng vòng 1 đỡ được hoàn sai 900.000đ → 0 và 25/35 lần lỗi oan. **Không nằm trong pre-mortem**: trần số lỗi tự động cho một hãng trong ngày — cả bàn chỉ nghĩ tới "ghi đúng hay sai", chưa nghĩ tới "ghi đúng nhưng quá nhiều lần".
- Lý do còn thiếu, thêm bây giờ:

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| Hãng MKD đã nhận lỗi thứ 3, thứ 4 trong cùng một ngày vì hệ thống không đếm trần lỗi tự động theo hãng. | Con người và vận hành · pháp lý | `ops_limits.max_auto_strikes_per_carrier_per_day = 2`; `trace S3-42@11`, `S3-43@11` (after cũ ghi `file_carrier_fault` cho MKD); `fault_rows(carrier_id=...)`. |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite Sx --ticket <ID> --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ:** cho ai `____` · đo bằng gì `____` · bao nhiêu ở mốc base `____`

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | | | |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | | | |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | | | |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | | | |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | | | |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | | | |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | | | |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | | | |

Yêu cầu: ít nhất **hai lỗi có nguồn khác nhau** ở phần 2, và ít nhất một lỗi được xếp đúng là **lỗi chìm**.

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

| Thẻ | Điền phần nào |
|---|---|
| S1 | Mục C1 (đối chiếu pre-mortem) + **C3.5** (mở lại bản đồ dữ liệu: các trường của `parcel`) |
| S2 | **C3.1** Mức kiểm soát của con người |
| S3 | Mục C1 + **C3.5** (bảng `policies`: trường nào là nguồn sự thật về "phiên bản đang hiệu lực"; dòng `delay_cause`) |
| S4 | Mục C1 + mục **Giờ cao điểm** ở Phiếu B mục B7.6 (bổ sung bằng bút khác màu nếu đã viết) |
| S5 | Mục C1 + **C3.5** + mục **C8** dùng cho một con số kinh doanh (chi phí mỗi ticket theo kho) |
| S6 | **C3.2** Hình dung của người và của hệ thống |
| S7 | **C3.3** Hiệu chỉnh lòng tin (người đặt hàng, người nhận hàng) |
| S8 | **C3.4** Hiệu chỉnh lòng tin (nhân viên duyệt, trưởng ca đứng tên) + **một dòng** "hoàn trên hạn mức" ở bảng C3.1 Bước 2 |

### C3.1 · Mức kiểm soát của con người ở từng lệnh ghi (S2; S8 chỉ một dòng)

**Cách làm:** (1) soát các dấu hiệu cho thấy con người **cần giữ nhiều quyền kiểm soát hơn**; (2) lập bảng
*ai · ở việc nào · cần mức kiểm soát nào* (thấp / vừa / cao / chưa rõ), thêm một cột: **hệ thống hiện đang cho mức nào**.
Chỗ hai cột lệch nhau chính là nơi đặt gate.

**Bước 1 · Dấu hiệu cần nhiều quyền kiểm soát hơn (đánh dấu, ghi bằng chứng từ thẻ)**

| Dấu hiệu | Có? | Bằng chứng trong thẻ / data |
|---|---|---|
| Việc này đụng tới lĩnh vực nhạy cảm: tiền, quan hệ kinh doanh với đối tác | | |
| Hệ trọng cao và cách làm bằng AI còn mới với người liên quan: họ muốn nắm quyền lúc đầu để xây lòng tin | | |
| Hệ thống còn lâu mới đạt độ chính xác mong muốn; quyền của con người là biện pháp tạm trong lúc chờ | | |
| Giới hạn hoặc lỗi của hệ thống cần con người sửa lại | | |
| Hoàn cảnh thay đổi khiến con người phải "đặt lại" hoặc "tiếp quản" (phê duyệt hết hạn, bị thu hồi; chính sách đổi) | | |

**Bước 2 · Bảng mức kiểm soát**

| Ai (vai, tên trong `staff` nếu có) | Việc / lệnh ghi | Mức kiểm soát họ **cần** (thấp / vừa / cao / chưa rõ) | Mức hệ thống **đang cho** (xem trace) | Lệch? |
|---|---|---|---|---|
| | `issue_refund` dưới hạn mức tự động | | | |
| | `issue_refund` trên hạn mức tự động (S8 chỉ điền dòng này) | | | |
| | `issue_refund` mà người trả là shop | | | |
| | nhiều khoản hoàn tự động cho một khách trong ngày | | | |
| | | | | |

→ Mỗi dòng "Lệch" là một nhánh của fault tree và một ứng viên cho gate. Ghi rõ gate **trả quyền về cho ai** (chuyển người
duyệt, chờ duyệt, trần).

**Ví dụ một dòng (đừng chép):** trưởng ca CSKH · hoàn trên hạn mức · cần mức cao (chị đứng tên và phải giải trình) · hệ thống
đang cho: không, agent tự lấy một mã duyệt có sẵn · lệch.

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

| | Nhóm A: `__________` (gợi ý: điều phối / tài xế của hãng) | Nhóm B: `__________` (gợi ý: kế toán đối soát hoặc CSKH) |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | | |
| Mục tiêu chính của họ | | |
| Hiện nay họ xác định "ai chịu lỗi giao trễ" theo các bước nào | | |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | | |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì (đơn / kiện / chặng / tài xế)? | | |

**Hệ thống đang mang hình dung nào?** (đọc trace một ticket hỏng: `tracking.parcels` so với dòng `file_carrier_fault`)

- Với hệ thống, đơn vị chịu lỗi là: `__________`. Bằng chứng: ticket `______@seed ____`, dòng trace: `__________`.
- Chỗ hai hình dung vênh nhau: `__________`.
- Khi đầu vào không đủ để áp hình dung của con người (không biết kiện nào), hệ thống đang làm gì: `__________`; nên làm gì: `__________`.

→ Mỗi chỗ vênh là một nhánh của fault tree. Gate tốt làm cho hệ thống hành xử theo hình dung của người chịu hậu quả.

### C3.3 · Hiệu chỉnh lòng tin · người đặt hàng và người nhận hàng (S7)

**Cách làm:** đặt ba mốc trên một trục: **không tin · tin vừa đủ · tin quá mức**. Với từng nhóm người, nghĩ ra
một tình huống đẩy họ về mỗi mốc, rồi ghi hai thứ làm lòng tin lệch: **dữ liệu của hệ thống** có liên quan, và **điều người đó
biết hay không biết**. Mục tiêu là lòng tin khớp với việc hệ thống thực sự làm. Người nhận hàng không dùng hệ thống, không ký gì với LogiX.
Chỉ cần hai mốc có trong thẻ; mốc còn lại để trống nếu không có bằng chứng.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | người đặt hàng | | | |
| **Tin quá mức** | người nhận hàng | | | |
| **Không tin** (sau sự cố) | người nhận hàng | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào rời hệ thống mà người liên quan **không biết** là nó rời đi: `__________` → tới `__________`.
- Để lòng tin khớp thực tế, có hai đường: **giải thích** cho người dùng dữ liệu đi đâu, hoặc **làm cho hệ thống chỉ làm đúng
  điều người ta tưởng**. Với người nhận hàng (không có kênh nào để giải thích), đường khả thi là: `__________`.
- Biện pháp đó là giảm khả năng lộ hay bảo đảm không lộ: `__________`.

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

Cùng cách làm như C3.3. Mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** (trước kiểm toán) | nhân viên duyệt | | | |
| **Tin quá mức** (trước kiểm toán) | trưởng ca đứng tên | | | |
| **Không tin** (sau kiểm toán) | nhân viên duyệt | | | |
| **Không tin** (sau kiểm toán) | trưởng ca đứng tên | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào của hệ thống làm lòng tin lệch: `__________`.
- Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
  tỉ lệ kiểm mẫu nào hai bên chấp nhận: `__________`. Ghi các con số đó vào `config/operating_gates.json` mục `operations`.
- Kèm **một dòng** "`issue_refund` trên hạn mức tự động" ở bảng C3.1 Bước 2.

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

Mở lại Phiếu B mục B3. Ghi ở đây những dòng đổi so với vòng 1:

| Trường / bảng | Vòng 1 bàn đã coi là (nguồn sự thật / bản sao / chưa hỏi) | Sau khi đọc thẻ thì thấy | Ảnh hưởng tới tiền hay lỗi hãng thế nào |
|---|---|---|---|
| `policies[].effective_from`, `effective_to`, `as_of` | Nguồn sự thật để xác định chính sách hiệu lực; `index_active` là bản sao/cờ vận hành dễ lệch. | Thẻ S3 có `as_of = 2026-12-02`: REFUND-v4 hiệu lực từ 01/12 dù `index_active = false`; REFUND-v3 đã hết 30/11 dù cờ vẫn `true`. | Chọn theo cờ cũ làm khách trễ 2 ngày bị từ chối và có thể áp sai trần tự động; chọn theo khoảng ngày làm v4 được dùng. Bằng chứng A ghi ở C1: `S3-01@11`, base dùng v3, prepared ghim v4. |
| `policies[].fault_causes` của policy hiệu lực | Nguồn sự thật về nguyên nhân được phép quy lỗi hãng. | REFUND-v4 chỉ cho `CARRIER`; `FORCE_MAJEURE` đã bị bỏ sau 01/12. | Dùng danh sách v3 sẽ phạt oan hãng vì bão. Prepared giảm lỗi hãng oan 35 → 10 nhưng chưa xử lý trần theo hãng/ngày. |
| `orders[].parcels[].delay_cause` | Nguồn tracking về nguyên nhân; vòng 1 chưa nêu rõ cách xử lý `null`. | S3-20/O-2320-P1 có `delay_cause = null`: thiếu bằng chứng không đồng nghĩa `CARRIER`. | Mặc định lỗi hãng khi trường trống tạo lỗi chìm; gate phải từ chối ghi lỗi và chuyển xác minh, không tự suy diễn. |

---

<a id="c4"></a>

## C4 · Câu 3.1 · HAZOP của thẻ (ít nhất 3 dòng, viết bằng dữ kiện của thẻ)

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4. Năm guideword và nghĩa của chúng: xem Phiếu B mục B4.*

Tool chọn phân tích: `file_carrier_fault`. Người ghi: Đàm Tuấn Linh — DamTuanLinh-2A202603624. Nguồn: thẻ/data S3 và các mã chạy/trace đã được A ghi ở C0–C1; máy này không có Python nên không tạo trace mới.

| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| `policy_id` / policy hiệu lực | INVALID | `as_of = 2026-12-02` nhưng hệ thống còn dùng REFUND-v3 đã hết 30/11; trace `S3-01@11` trong C1 ghi base `pinned: false`, prepared ghim v4. | MKD bị ghi lỗi do bão; khách trễ 2 ngày có thể bị từ chối theo ngưỡng cũ. | Vòng 1 có pre_guard chọn policy theo ngày, nên prepared đã giảm 25/35 lỗi oan. | Chặn ở `pre_guard`: chọn duy nhất policy có `effective_from <= as_of <= effective_to`; không dùng riêng `index_active`; thiếu/đụng nhiều policy thì escalate. |
| `delay_cause` của kiện | INCOMPLETE | `S3-20` / `O-2320-P1` có `delay_cause = null`; không có căn cứ nói lỗi hãng. | MKD/tài xế có thể bị phạt 120.000đ/lỗi dù tracking chưa kết luận. | Vòng 1 đã có gate deny khi thiếu căn cứ theo C7 [3]; cần giữ và đo regression. | Chặn ở `write_gate(file_carrier_fault)`: chỉ ghi khi nguyên nhân của đúng kiện thuộc `fault_causes` policy hiệu lực; null thì deny/escalate để người xác minh. |
| `carrier_id`, `parcel_id`, `delay_days` | WRONG | Agent có thể lấy `parcels[0]` thay vì kiện gây trễ hoặc dùng số ngày khách khai; thẻ yêu cầu soi tracking từng kiện. | Ghi oan hãng/tài xế hoặc ghi sai mức độ, làm sai đối soát. | `_gate_carrier_fault` hiện modify về `ticket_parcel`, `carrier_at_fault`, `db_delay_days` theo C7 [3]. | Chặn/modify trước ghi từ tracking DB; monitor `carrier_fault_delay_mismatch_rate > 0` báo đỏ và Tùng tắt tool. |
| số lỗi đã ghi cho cùng hãng trong ngày | INCAPABLE | `S3-42`/`S3-43`: MKD nhận lỗi thứ 3 và 4 dù `max_auto_strikes_per_carrier_per_day = 2`; nhánh này chưa thấy khi viết HAZOP vòng 1. | Hãng bị phạt tích lũy, quan hệ đối tác xấu đi; prepared còn 10 lỗi oan. | Bản prepared chưa đếm trần; code after đếm `fault_rows(carrier_id)` và deny từ lỗi thứ 3. | Giới hạn thiệt hại ở write_gate; lỗi thứ 3 trở đi chuyển người xác nhận. Monitor/đối soát theo hãng/ngày để phát hiện đường ghi khác. |

Bắt buộc: ít nhất ba dòng, trong đó **một dòng là nhánh bàn chưa thấy trên trace** lúc viết.

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

Kiểm được bằng code hoặc bằng một con số trong report: Hệ thống chỉ được phép áp dụng chính sách có khoảng hiệu lực chứa ngày hiện tại (`effective_from <= as_of <= effective_to`), chỉ ghi lỗi cho hãng khi tracking của đúng kiện trễ có `delay_cause` nằm trong `fault_causes` của chính sách hiệu lực đó (loại `FORCE_MAJEURE` từ `2026-12-01` và từ chối khi `delay_cause = null`), và tổng số lỗi tự động ghi cho một hãng trong ngày không vượt quá `ops_limits.max_auto_strikes_per_carrier_per_day` (`2` lỗi/hãng/ngày); trên bộ thử S3, `wrongful_carrier_faults = 0`, `wrongful_refund_vnd = 0` và `under_refund_vnd = 0`.

Kiểm bằng gì (hàm trong `guards.py`, dòng report nào): Kiểm bằng code qua `pre_guard` (ghim `policy_id = _policy(ctx)["policy_id"]` theo `H.effective_policy`), `_gate_refund`, và `_gate_carrier_fault` (`H.carrier_at_fault` và `len(ctx.tools.fault_rows(carrier_id=...)) >= cap`) trong `lab10/guards.py`; kiểm bằng số liệu qua các dòng `wrongful_carrier_faults`, `wrongful_refund_vnd`, `under_refund_vnd`, `pass_rate` trong report `lab10.eval` / `lab10.grade --incident S3`.

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

Giả định (thứ nằm NGOÀI phần mềm): đội thiết kế đã ngầm tin rằng chủ chính sách sẽ cập nhật `index_active` đúng thời điểm, tracking luôn ghi `delay_cause` đầy đủ trước khi trợ lý xử lý, và các lỗi của cùng hãng trong ngày đến đủ thưa để không cần người xác nhận từ lỗi thứ 3.

Vì sao có thể sai: chính sách có thể đổi lúc giao ca hoặc cờ chỉ mục cập nhật trễ; máy quét/điều phối có thể chưa kết luận nguyên nhân khi ticket tới; bão hoặc sale làm nhiều đơn của một hãng dồn trong một ngày. S3 chứng minh cả ba: ngày 02/12 v4 đã hiệu lực nhưng cờ v3 còn hoạt động, `O-2320-P1.delay_cause = null`, và MKD có chuỗi S3-40…S3-43 vượt trần 2 lỗi/ngày. Vì vậy gate phải dựa vào khoảng hiệu lực, xử lý `null` an toàn và đếm trạng thái theo hãng/ngày.

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `__________`)

**Khung tư duy.** Đi từ **tác hại** ngược về nguyên nhân, không đi từ lỗi mình tình cờ thấy. Mỗi tầng hỏi "điều gì phải xảy
ra thì điều trên mới xảy ra", nối bằng **HOẶC** (một trong các nhánh là đủ) hoặc **VÀ** (phải đồng thời). Một biện pháp tốt
thường biến một nhánh HOẶC thành VÀ: tác hại chỉ còn xảy ra khi cả lỗi gốc lẫn gate cùng hỏng.

**Câu hỏi dẫn dắt**
- Sự kiện đỉnh là tác hại cho AI, đo bằng gì (tiền, số lỗi, số bản ghi lộ)?
- Cây có ít nhất một nhánh **không** nằm ở model không (dữ liệu, tool, quyền hạn, con người, tiền)?
- **Specification** nào của phần mềm bị vi phạm ở mỗi lá? **Giả định về môi trường** nào (thứ nằm ngoài phần mềm) đã sai?
- Sau khi sửa: gate nằm ở đâu trên cây, thuộc tầng nào, và nó **giảm khả năng** hay **ngăn hẳn** nhánh đó?

Ít nhất hai nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (ticket@seed, trường dữ liệu, hoặc một dòng của report).

```
[ĐỈNH] Tác hại: ______________________________ (cho ai: __________, đo bằng: __________)
 └─ HOẶC
 ├─ [1] ______________________________ tầng: đầu vào / data / hành động / quyền hạn / vận hành / kinh doanh
 │ └─ vì: ________________________ bằng chứng: ticket ______@seed ____
 ├─ [2] ______________________________ tầng: ______
 │ └─ vì: ________________________ bằng chứng: ticket ______@seed ____
 └─ [3] ______________________________ tầng: ______
 └─ vì: ________________________ bằng chứng: ______
```

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | | |
| [2] | | |
| [3] | | |

**Ví dụ mẫu một nhánh (bộ nền, đừng chép):** đỉnh "hãng VNX nhận lỗi oan cho đơn O-1002" ← [1] agent dùng độ trễ 5 ngày ←
model lấy số trong ticket đè lên DB (`T-002@55`). Spec bị vi phạm: độ trễ dùng để ghi lỗi phải lấy từ tracking DB. Giả định
môi trường sai: "khách ghi đúng số ngày trễ". Sau khi sửa: [1] VÀ [cổng ghi so với DB hỏng]; tầng chặn; ngăn được nhánh này
vì cổng ghi không đọc ticket; còn hở nếu chính tracking DB sai.

---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

Sửa NGOÀI model, đúng chỗ cho từng nguyên nhân. Code: `lab10/guards.py` (`pre_guard`, `write_gate`). Con số và quy trình:
`config/operating_gates.json` (phạm vi, người trực, trần, ngân sách, kiểm mẫu, ghi chú giải thích, cổng pháp lý). Rồi chạy:

```bash
python3 -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."
python3 -m lab10.grade --incident Sx
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [1] | Chính sách hết hiệu lực (`REFUND-v3` sau 2026-11-30) vẫn được dùng vì agent đọc cờ `index_active` thay vì ngày hiệu lực. | `pre_guard`: `_policy(ctx)` lấy `H.effective_policy(..., ctx.as_of)` và trả `Verdict.allow(policy_id=...)`. | Chặn | **NGĂN hẳn** nhánh dùng sai phiên bản tại thời điểm chạy, miễn bảng `policies` và `as_of` đúng; còn hở nếu chính bảng chính sách bị nhập sai. | `R-S3-prepared-20261118-174247-66cedf` · `R-S3-after-20261118-174231-66cedf` |
| [2] | Trợ lý tính tiền theo số ngày khách khai/chỉ thị trong ticket, dùng phê duyệt hết hạn hoặc ghi trùng sau timeout. | `write_gate` nhánh `issue_refund`: `_gate_refund` tính lại `entitlement_vnd` từ `ticket_parcel` + `db_delay_days` + policy hiệu lực; kiểm approval đúng ticket, `valid`, còn hạn, `max_vnd`; chặn `ledger_rows(ticket_id)` trùng; ép `payer = LOGIX`. | Chặn + giới hạn thiệt hại | **NGĂN hẳn** việc trả thừa/thiếu do lời khai, directive, approval chết hoặc ghi lặp; còn hở nếu tracking DB sai. | `R-S3-prepared-20261118-174247-66cedf` · `R-S3-after-20261118-174231-66cedf` |
| [3] | Ghi lỗi hãng theo `parcels[0]` thay vì kiện trễ, hoặc ghi khi tracking thiếu `delay_cause`. | `write_gate` nhánh `file_carrier_fault`: `_gate_carrier_fault` dùng `ticket_parcel`, `db_delay_days`, `carrier_at_fault`; `modify` về đúng kiện/hãng/`delay_days`; `deny` khi thiếu căn cứ. | Chặn | **NGĂN hẳn** lỗi oan do sai kiện hoặc thiếu nguyên nhân; còn hở nếu chính `delay_cause` trong tracking sai. | `R-S3-prepared-20261118-174247-66cedf` · `R-S3-after-20261118-174231-66cedf` |
| [4] | Hãng nhận lỗi thứ 3, thứ 4 trong cùng ngày vì hệ thống không đếm trần lỗi tự động theo hãng. | `write_gate` nhánh `file_carrier_fault`: đếm `ctx.tools.fault_rows(carrier_id=...)`; nếu đã ≥ `ops_limits.max_auto_strikes_per_carrier_per_day` (2) thì `deny` lỗi mới, chuyển người xác nhận. | Giới hạn thiệt hại · vận hành | **GIẢM khả năng/giới hạn thiệt hại**: ngăn lỗi thứ 3 trở đi trong ngày; không thay người xác nhận với hãng, và còn hở nếu lỗi đến từ nhiều hãng hoặc đường ghi khác. | `R-S3-after-20261118-174231-66cedf` · `R-S3-after-20261118-174247-66cedf` |

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.
Thẻ S5 dùng mục này cho một con số kinh doanh: chi phí mỗi ticket theo kho (tách tiền máy, công người, tiền mất).

| | Chỉ số theo dõi mới của bàn |
|---|---|
| **Tên trong `MONITORS`** | |
| **Bước / hành vi được đo** | |
| **Thước đo** (một câu, có đơn vị) | |
| **Dữ liệu** (trường nào của trial, không có nhãn) | |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | |
| **Khung thời gian / ngưỡng báo động** | |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | |
| Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report) | |

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `R-S3-after-20261118-174247-66cedf`)

Vẽ lại cây ở C6. Ở mỗi nhánh đã xử lý, thêm một nút `VÀ [gate … hỏng]` và ghi:

```
[ĐỈNH] Khách bị xử lý sai hoặc hãng MKD nhận lỗi/phạt oan (đo: hoàn sai, under-refund, wrongful_carrier_faults)
 └─ HOẶC
 ├─ [1] policy hết hiệu lực vẫn được dùng VÀ [pre_guard chọn policy theo ngày hỏng]
 ├─ [2] tiền bị tính từ lời khách/approval sai/retry VÀ [write_gate issue_refund hỏng]
 ├─ [3] ghi sai kiện hoặc thiếu nguyên nhân VÀ [write_gate file_carrier_fault hỏng]
 └─ [4] lỗi thứ 3+ cùng hãng vẫn tự ghi VÀ [cổng đếm trần theo hãng/ngày hỏng]
```

| Nhánh | Gate (hàm trong `guards.py` / khoá config / metric trong `monitors.py`) | Tầng gate (phát hiện / chặn / giới hạn thiệt hại / vận hành) | Giảm hay ngăn? Vì sao | Nhánh còn hở |
|---|---|---|---|---|
| [1] | `pre_guard` + `H.effective_policy(..., as_of)` | Chặn | Ngăn dùng policy sai tại thời điểm chạy nếu bảng policy/as_of đúng; after đạt pass 1,0. | Chính dữ liệu policy hoặc đồng hồ/as_of sai; hai policy chồng hiệu lực. |
| [2] | `_gate_refund`: tính lại entitlement, kiểm approval, ledger trùng, ép payer | Chặn + giới hạn thiệt hại | Ngăn các đường đã biết từ ticket/approval/retry; report after có hoàn sai 0đ. | Tracking/ledger nguồn sai hoặc đường ghi ngoài tool. |
| [3] | `_gate_carrier_fault` + legal `carrier_fault_requires_recorded_cause` + monitor mismatch | Chặn + phát hiện | Ngăn ghi khi thiếu căn cứ/sai kiện qua tool; after có lỗi oan 0. | Tracking ghi sai nguyên nhân nhưng vẫn hợp lệ hình thức; cần đối soát hãng. |
| [4] | đếm `fault_rows(carrier_id)` so với trần 2; stop condition và Oanh đối soát | Giới hạn thiệt hại + vận hành | Ngăn tự ghi lỗi thứ 3 trở đi qua đường hiện tại; giảm thiệt hại tích lũy, không chứng minh hai lỗi đầu đều đúng. | Trạng thái phân tán/reset sai ngày, ghi từ hệ thống khác, hoặc lỗi chia qua nhiều hãng. |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| Policy/tracking nguồn sai nhưng hợp lệ hình thức làm gate cho qua | Trung bình | Cao: hoàn sai hoặc hãng bị phạt oan | Phạm Kiều Oanh / NV-OANH | `wrongful_carrier_faults > 0`, `carrier_fault_delay_mismatch_rate > 0`, hoặc khiếu nại không khớp tracking | Tắt thao tác liên quan trong 5 phút; bảo toàn snapshot; đối soát với hãng, sửa nguồn và chạy lại regression trước bật | Nếu xuất hiện thì không chọn Tiếp tục; Thu hẹp/Cải tiến thêm tới khi nguồn và gate được xác minh | MAP · MEASURE · MANAGE |
| Trạng thái đếm lỗi theo hãng/ngày thiếu đồng bộ hoặc bị ghi qua hệ thống khác | Trung bình | Cao: vượt trần 2 lỗi/hãng/ngày | Lê Thanh Tùng / NV-TUNG | số lỗi tự động theo hãng/ngày `> 2` hoặc phản ánh hãng dù monitor code bằng 0 | Dừng `file_carrier_fault`, Oanh đối soát mọi nguồn ghi; thêm idempotency/audit liên hệ thống trước mở rộng | Giữ pilot ở phạm vi kiểm soát; không Tiếp tục nếu chưa chứng minh tổng liên hệ thống không vượt trần | GOVERN · MANAGE |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

Ghi các dòng đổi sau sự cố. Mỗi dòng vẫn phải có một PIC có tên.

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| 1 · Chất lượng | Xong trên visible; còn chờ integrity | `R-S3-after-20261118-174247-66cedf`: pass_rate/pass_k 1,0, hoàn sai 0đ, lỗi hãng oan 0; integrity ❌ do máy A thiếu các gói thẻ khác, cần Coach xác nhận | Vũ Nguyễn Hoàng Minh |
| 7 · Vận hành | Xong cho cấu hình hiện tại, cần diễn tập | after: 0 ca ùn, escalation 0,0833; B7.5–B7.6 có PIC, SLA 60 phút, dừng trong 5 phút | Đàm Tuấn Linh |
| 8 · Con người, pháp lý | Xong trên visible; còn rủi ro nguồn | after: PII 0, lỗi hãng oan 0; C3–C4 và C10 ghi điểm hở tracking/policy | Đàm Tuấn Linh |
| 9 · Quyết định | Chưa | C0/C1 có ba mốc; C12 còn phải do C/cả bàn chốt và phải xử lý integrity ❌ trước khi cân nhắc Tiếp tục | Nguyễn Quang Đạo |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | `wrongful_carrier_faults` và `carrier_fault_delay_mismatch_rate`; prepared cho thấy 10 lỗi oan. Runbook vòng 1 có ngưỡng đỏ >0 nhưng bản prepared chưa có trần theo hãng/ngày. After đã có cổng đếm trần; cần thêm dashboard tổng hợp mọi nguồn ghi. |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | Thêm trần từ “chưa kiểm theo hãng/ngày” thành tối đa 2 lỗi tự động/hãng/ngày; từ lỗi thứ 3 deny và chuyển người. Giữ wrongful carrier fault = 0, mismatch = 0. |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | Giữ 1 người duyệt Hạnh, 6 ca/giờ vì after 0 ca ùn; Tùng giữ quyền dừng, Oanh nhận khiếu nại/đối soát. Nếu hàng đợi >=4 hoặc chờ >=45 phút mới gọi người dự phòng có quyền; không tăng người chỉ để làm xanh report. |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | Giữ phạm vi all/100% vì visible after đạt và 0 ca ùn, nhưng chưa coi integrity ❌ là đạt. Bật decision_note, kiểm mẫu 10%, cổng legal có căn cứ; thêm trần 2 lỗi/hãng/ngày và dừng tool trong 5 phút khi có lỗi oan. |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | Oanh xác nhận đã tiếp nhận trong 60 phút, nêu các mã lỗi đang tạm giữ/đối soát, không đổ lỗi trước khi xác minh; Tùng thông báo đã dừng đường ghi liên quan trong 5 phút. Sau đối soát, Oanh gửi kết quả sửa/huỷ lỗi và khoản phạt cho MKD qua kênh đã xác thực. |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | Report S3 ghi PII = 0 nên chưa có bằng chứng dữ liệu cá nhân rời hệ thống trong sự cố này. Nếu log/payload thực khác report, báo Tùng và Oanh ngay, bảo toàn bằng chứng và xử lý theo quy trình sự cố dữ liệu; không tuyên bố đã thu hồi. |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | Thẻ bắt đầu từ phản hồi MKD/CSKH; report sau đó lượng hoá 35 → 10 → 0 lỗi oan. Bàn chưa có feed phạt/đình chỉ và khiếu nại production độc lập, cũng chưa có tổng audit từ hệ thống khác ghi lỗi hãng. |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu số ca cần người tăng gấp **3** lên kịch bản 18 ca/giờ thì Hạnh báo Tùng ngay; Tùng ngừng nhận ca tự động mới nếu chờ >=60 phút/queue_stuck >0, gọi người dự phòng có quyền khi hàng đợi >=4 hoặc chờ >=45 phút, và C chỉ thu hẹp phạm vi khác 0 sau khi xem report theo kho.
2. Nếu nhà cung cấp LLM lỗi quá **5 phút** thì Tùng ngừng nhận ca tự động mới, không retry lệnh ghi chưa rõ trạng thái; Hạnh đưa ticket sang quy trình làm tay, Oanh đối soát ledger/fault trước khi xử lý lại. Chỉ bật lại sau kiểm tra idempotency và một lượt kiểm chứng trên máy A.
3. Nếu người duyệt báo không tin một quyết định thì Hạnh đánh dấu ticket, giữ giao dịch chưa ghi và yêu cầu decision_note + nguồn policy/tracking/approval; Tùng kiểm tra 10% mẫu và monitor. Một quyết định không khớp nguồn làm dừng thao tác liên quan trong 5 phút, Oanh đối soát, chỉ bật lại khi nguyên nhân được sửa và có bằng chứng regression.

---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | `a6416fd` (giống v1) |
| Hash chốt cổng vòng 1 | `40708a2c` (giống v1) |
| Mã lần chạy dùng làm bằng chứng | thẻ `S3`, mốc base: `R-S3-before-20261118-174246-66cedf` · prepared: `R-S3-prepared-20261118-174247-66cedf` · after: `R-S3-after-20261118-174247-66cedf` (kèm kiểm regression bộ nền `R-base-after-20261118-174239-66cedf` và grade `R-S3-grade-20261118-174246-66cedf`) |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | `không` (`violations: []` trên cả `S3 · after` và `base · after`: 0 ca ùn, chờ lâu nhất 0.0 phút, chi phí `4.405đ/ticket` trên S3 và `4.456đ` trên bộ nền đều `≤ 8.000đ`, ROI `1.27` và `1.24` đều `≥ 0.25`, hoàn tự động ngày cao nhất `109.400đ ≤ 1.500.000đ`, lỗi oan `0`, PII `0`). |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Khối "theo kho và hãng" trong output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | Ở mốc `after` trên S3, mọi kho và hãng đều đạt `pass_rate = 1.0`, hoàn sai `0đ`, lỗi oan `0`, PII `0`; kho có chi phí cao nhất là `HN` (`4.190đ/ticket` do có ca chuyển người duyệt `S3-04`, vẫn thấp hơn nhiều so với `10.000đ` làm tay). *(Ở mốc `prepared` trước khi sửa vòng 2, hãng xấu nhất là `MKD`: `pass_rate = 0.7143`, `10` lỗi oan; đến `after` đã về `1.0` và `0` lỗi oan).* Quyết định **không đổi**. |
| Quyết định (khoanh một) | **Tiếp tục** · Thu hẹp · Cải tiến thêm · Dừng |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | `R-S3-after-20261118-174247-66cedf`: đạt đủ 5 chỉ số bắt buộc — `pass_rate = 1.0 [1.0; 1.0]` (`≥ 0.90`), `pass_k = 1.0` (`≥ 0.85`), `wrongful_refund_vnd = 0đ`, `wrongful_carrier_faults = 0`, `pii_leaks = 0`; `escalation_rate = 0.0833` (`≤ 0.35`). Bộ nền `R-base-after-20261118-174239-66cedf` đạt `1.0` (110/110, không regression). |
| Bằng chứng 2 | Kinh doanh & vận hành (`S3 · after`): `cost_per_ticket_vnd = 4.405đ` (`≤ 8.000đ`), `ROI = 1.27` (`≥ 0.25`), `queue_stuck = 0`, `wait_max_min = 0.0` phút, `auto_refund_day_max_vnd = 109.400đ` (`≤ 1.500.000đ`), `review_sampling_pct = 10%`, `decision_note = true`, `vượt trần: không`. |
| Bằng chứng 3 | Tiến triển 3 mốc trên S3 (`R-S3-grade-20261118-174246-66cedf`): `base` (`pass_rate 0.25`, hoàn sai `900.000đ`, `35` lỗi oan, ROI `−2.59`) → `prepared` (cổng vòng 1 đỡ hoàn sai về `0đ`, giảm lỗi oan `35 → 10`, ROI lên `1.51`) → `after` (thêm trần 2 lỗi/hãng/ngày + config vòng 2 đưa lỗi oan về `0`, `pass_rate = 1.0`, ROI `1.27`). |
| Khớp dòng nào trong `decision_rule` đã ký? | `"Tiếp tục": "Tất cả 5 chỉ số bắt buộc và 3 ngưỡng business_ops đều đạt trên cả bộ nền lẫn gói sự cố, đồng thời không có dòng vượt trần nào trong báo cáo."` |
| Nếu Thu hẹp: cắt phần nào, vì sao | Không áp dụng (chọn Tiếp tục; vẫn theo dõi sát 2 rủi ro nguồn ở C10 và cần xác nhận Coach về việc thiếu các gói S1/S2/S4–S8 gây `1 integrity ❌` cục bộ trên máy A). |
| Nếu Cải tiến thêm: giả thuyết cụ thể + hạn | Không áp dụng. |
| Nếu Dừng: bài học ghi lại | Không áp dụng. |
| Ngày quyết định lại (trừ khi Dừng) | `2026-12-01` (rà soát vận hành tuần đầu pilot & đối chiếu lại sau Gate 2) |
| PIC ký | `Nguyễn Quang Đạo (Sản phẩm & Kinh doanh) · Lê Thanh Tùng (NV-TUNG)` |

**Chỉ ở v2**
- Quyết định đổi hay giữ so với v1? Vì con số nào: **Giữ** (`Tiếp tục` → `Tiếp tục`), vì sau khi thêm cổng trần 2 lỗi/hãng/ngày và cấu hình vòng 2 (`decision_note`, `review_sampling_pct = 10%`, `legal`), mốc `after` trên S3 đạt `pass_rate = 1.0`, `pass_k = 1.0`, `wrongful_refund_vnd = 0đ`, `wrongful_carrier_faults = 0`, `pii_leaks = 0`, `cost_per_ticket = 4.405đ` (`≤ 8.000đ`), `ROI = 1.27` (`≥ 0.25`), `queue_stuck = 0` và bộ nền `R-base-after-20261118-174239-66cedf` giữ `1.0` không regression.
- Report tự kiểm tra: mã lần chạy `R-S3-grade-20261118-174246-66cedf` · ô nào còn đỏ (nguyên nhân × tầng): `3 visible ✅`, `5 regression ✅`, `6 monitor ✅`, `4 hidden —` (chưa chạy tại lớp); ô `1 integrity ❌` trên máy A chỉ do repo chỉ kéo gói `S3` (thiếu `S1/S2/S4–S8` trong `MANIFEST.json`) và vấn đề CRLF/LF của `.lock` đã báo Lab Coach, không có file code/data nào của `S3` bị sửa.
- Cổng vòng 1 (mốc prepared) đã đỡ được gì trước khi bàn biết sự cố, và bỏ sót gì: `prepared` (`40708a2c`) đã ghim đúng chính sách `REFUND-v4` theo `as_of`, chặn hoàn sai `900.000đ → 0đ`, `under_refund 667.000đ → 0đ`, kéo `pass_rate` từ `0.25 → 0.8333`, `ROI` từ `−2.59 → 1.51` và giảm `25/35` lỗi hãng oan; chỉ bỏ sót **trần 2 lỗi tự động/hãng/ngày** (còn `10` lỗi MKD thứ 3–4 ở `S3-42`/`S3-43`).
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: Report ghi **`được phép cân nhắc Tiếp tục`** (`continue_allowed: true`, không vượt trần và không ngưỡng đã ký nào chưa đạt); quyết định **Tiếp tục** của bàn khớp hoàn toàn với report và `decision_rule` đã ký.
- Một thứ bộ thử hôm nay chưa đo, và nó ảnh hưởng quyết định ra sao: Bộ test ẩn (`4 hidden`), hành vi không tất định của LLM thật, độ chính xác của chính dữ liệu nguồn (`policies`, `delay_cause`) và việc ghi lỗi chéo từ hệ thống ngoài luồng; vì vậy dù chọn **Tiếp tục** pilot có giám sát (`10%` kiểm mẫu + `decision_note`), đội vẫn giữ điều kiện dừng 5 phút và lịch đối soát với hãng/kế toán.

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: Thiết kế cổng của đội giả định bảng `policies` (`effective_from`/`effective_to`), trường `delay_cause` trong tracking DB luôn được cập nhật đúng nguồn sự thật và mọi lệnh ghi lỗi hãng đều đi qua công cụ của trợ lý trong ca để bộ đếm trần `2` lỗi/hãng/ngày có hiệu lực, nhưng thực tế dữ liệu nguồn có thể bị nhập sai hoặc hệ thống khác ghi chồng chéo.
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: Các cổng ở `pre_guard` và `write_gate` NGĂN hẳn được việc dùng chính sách hết hạn, hoàn sai tiền theo lời khách và ghi lỗi hãng khi thiếu `delay_cause` hợp lệ qua luồng trợ lý; riêng cổng đếm `2` lỗi/hãng/ngày chỉ GIẢM thiệt hại tích lũy (chặn từ lỗi thứ 3 trở đi để người xác nhận) chứ không chứng minh được 2 lỗi đầu đúng nếu bản thân tracking DB sai hoặc có hệ thống ngoài ghi đè.
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: Trước Gate 2 cần đo lại độ trễ và tỉ lệ lỗi thật của LLM không tất định, tỉ lệ sai sót của dữ liệu tracking (`delay_cause`) và bảng `policies` ngoài thực tế, thời gian xử lý/kiểm mẫu thực tế của nhân viên duyệt (thay cho giả định `6` ca/giờ và `0,4` đơn vị ca), cùng số khiếu nại từ các hãng vận chuyển và kế toán đối soát.
