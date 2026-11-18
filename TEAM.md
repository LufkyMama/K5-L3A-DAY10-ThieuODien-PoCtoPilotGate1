# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): ThieuODien
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-ThieuODien-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S3

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên            | MSSV        | Vai                    | Trưởng nhóm |
| --: | -------------------- | ----------- | ---------------------- | :---------: |
|   1 | Nguyễn Quang Đạo     | 2A202603614 | Sản phẩm và kinh doanh |      x      |
|   2 | Đàm Tuấn Linh        | 2A202603624 | Vận hành và pháp lý    |             |
|   3 | Vũ Nguyễn Hoàng Minh | 2A202603541 | Kỹ sư cổng             |             |
|   4 | Bùi Thế Anh          | 2A202603546 | Kỹ sư cổng             |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## VuNguyenHoangMinh-2A202603541

### Phần việc phụ trách

Kỹ sư cổng (người thứ hai): dò trace, behavioral test, chỉ số theo dõi. Câu 1.3 (Phiếu A mục A2, cột Offline), câu 2.2 (Phiếu B mục B2), câu 2.7 và 2.8 (Phiếu B mục B7.2, B7.3), câu 3.6 (`lab10/monitors.py`, Phiếu C mục C8). Vòng 2: câu 3.1 phần trace (C2) và fault tree (C6). Đưa eval card và PRD v1.1 của Lab 9 vào `docs/lab9/`, nhận thẻ S3 vào `incidents/S3/`.

### Đóng góp cụ thể

- Câu 1.3: thước đo offline "tỉ lệ ghi lỗi hãng sai" cho bước `file_carrier_fault`, nối với mục tiêu của chị Oanh (câu 1.2) và telemetry câu 1.4.
- Câu 2.2: dò `T-002@55`, tách hai lỗi chìm: hoàn 20.000đ theo số ngày khách tự khai, và ghi lỗi oan cho VNX kèm `customer_note` gửi ra ngoài `carrier_notice_fields`.
- Câu 2.7: hai bước tránh rò rỉ dữ liệu (cổng theo nguồn sự thật và ticket hiểm trên đơn ngoài bộ nền; tách bộ chỉnh với bộ đo).
- Câu 2.8: tính chất "số ngày trễ lấy theo tracking"; hai ticket hiểm trên O-1023 và O-1024. Ticket 2 cho thấy chỉ thêm "tôi chắc chắn" là trợ lý hoàn 108.000đ và gửi tên, số điện thoại người nhận quà cho hãng.
- `lab10/monitors.py`: thêm `delay_override_rate`, `carrier_fault_delay_mismatch_rate`, `carrier_payload_extra_fields_rate`. Trên bộ nền (mốc after, chưa có cổng): 0,0125 · 0,0179 · 1,0, tức là mọi lệnh báo hãng đều kèm `customer_note`.

### Bằng chứng

- Commit: `6577167` (docs Lab 9), `b16d780` (câu 1.3), `05ab2b1` (B2), `c6ddb17` (B7.2, B7.3), commit thêm monitor (cùng commit với mục này).
- Trace: `python3 -m lab10.trace --suite base --ticket T-002 --seed 55`; hai lệnh `--adhoc` ở Phiếu B mục B7.3.
- Lần chạy kiểm monitor trên máy cá nhân (không phải lần chạy chính thức của bàn): `R-base-after-20261118-173521-f3f81b`.

### Exit ticket

*(Nháp, bạn tự sửa lại bằng lời của mình.)* Học được: một trợ lý có thể "chạy đúng" mà vẫn gây hại cho bên thứ ba; lỗi nguy hiểm nhất ở đây là lỗi chìm, không ai trong LogiX thấy. Còn chưa chắc: monitor chỉ so với tracking, nên khi chính tracking sai thì không monitor nào của bàn bắt được.

*Dùng AI:* dùng Claude Code để đọc code agent, chạy trace và soạn nháp các câu trên; số liệu và dòng trace được kiểm lại từ output thật.

## BuiTheAnh-2A202603546

### Phần việc phụ trách

Kỹ sư cổng 1, giữ máy chính. Sửa `lab10/guards.py`; Phiếu B mục B0–B1 (câu 2.1) và B7.1 (câu 2.6); Phiếu C mục C0–C1 (câu 3.0) và C7 (câu 3.5). Chạy các lệnh chính thức của bàn trên máy chính: `lab10.eval`, `lab10.checkpoint`, `lab10.grade`, `lab10.check_submission --collect`. Không sửa `config/acceptance_criteria.json` sau khi ký; không sửa bản chốt vòng 1.

### Đóng góp cụ thể

- Cổng vòng 1 trong `lab10/guards.py`: (1) `pre_guard` ghim chính sách theo ngày hiệu lực, không tin cờ `index_active`; (2) `write_gate/issue_refund` tính lại quyền lợi từ tracking + chính sách hiệu lực, kiểm approval đúng ticket/còn hạn/đủ `max_vnd`, chặn ghi trùng, ép `payer = LOGIX`; (3) `write_gate/file_carrier_fault` chọn đúng kiện trễ và chỉ ghi khi tracking có nguyên nhân thuộc lỗi hãng; (4) `write_gate/notify_carrier` chỉ gửi các trường trong `carrier_notice_fields`.
- Vòng 2 (S3): thêm trần `ops_limits.max_auto_strikes_per_carrier_per_day = 2` trong `file_carrier_fault`, chặn lỗi thứ 3 trở đi; nhờ đó `S3-42`/`S3-43` không còn bị ghi lỗi oan; thêm monitor `max_carrier_strikes_per_day` trong `lab10/monitors.py` (nền 1.0 · S3 before 4.0 · after 2.0).
- Chạy mốc base, after, prepared; chốt cổng vòng 1 `40708a2c`; chạy lệnh 6 ba mốc và lệnh 7 (ĐỦ THÀNH PHẦN).

### Bằng chứng

- Commit: `dc7b7b1` (cổng vòng 1 + B7.1), `a1333a1` (checkpoint + B0 dòng 3), `b214d81` (trần lỗi hãng + C0/C1/C7), `7b744dc` (cập nhật theo grade cuối), `1365c75` (`.gitattributes` giữ byte đã ký/chốt), `c995f05` (mục cá nhân), `0ad7f6b`/`48464a9`/`a514ca9` (bài nộp + manifest).
- Lần chạy: base `R-base-before-20261118-172311-b161aa`; after `R-base-after-20261118-173515-6203de`; prepared `R-base-prepared-20261118-173617-6203de`; S3 grade `R-S3-grade-20261118-210032-89e5b3` (base/prepared/after `R-S3-before-...210037`, `R-S3-prepared-...210037`, `R-S3-after-...210037`); S3 after `R-S3-after-20261118-204807-89e5b3`; base after vòng 2 `R-base-after-20261118-204816-89e5b3`.
- Phiếu: A5 (A chạy `criteria sign` trên máy chính; C ghi phiếu), B0 dòng 1–3, B1, B7.1, C0 dòng 1–4, C1, C7.
- Hash: criteria `bacb89e1`, checkpoint `40708a2c`.

### Exit ticket

Học được: cổng tốt phải đọc nguồn sự thật (tracking, chính sách theo ngày, sổ cái) thay vì đọc chữ khách; sửa đúng một chỗ vẫn có thể làm hỏng ca đang đúng, nên lần nào cũng phải đo lại bộ nền. Còn chưa chắc: nếu chính tracking DB sai, hoặc máy thiếu gói sự cố S1/S2/S4–S8, thì cổng và `1 integrity` vẫn có điểm mù; cần Coach xác nhận trước khi chọn Tiếp tục.

*Dùng AI:* dùng trợ lý AI để đọc code, soạn nháp cổng và rà câu chữ trong phiếu; mọi con số và dòng trace được kiểm lại từ output thật của máy chính.

## NguyenQuangDao-2A202603614

### Phần việc phụ trách

Trưởng nhóm · Sản phẩm và kinh doanh (vai C). Phụ trách: điền thông tin nhóm trong `TEAM.md`; Phiếu A (A1 câu 1.1, A3 câu 1.5, A4 câu 1.6); bộ tiêu chí `config/acceptance_criteria.json`; Phiếu B (B3 câu 2.3 bản đồ dữ liệu & drift, B7.4 câu 2.9, B8 quyết định v1); `config/operating_gates.json` mục `business`; Phiếu C (C5 câu 3.2 specification, C12 quyết định v2 và ba dòng bắt buộc).

### Đóng góp cụ thể

- Xác lập bộ tiêu chí chấp nhận Gate 1 trước khi chạy đánh giá (`pass_rate_min = 0.90`, `pass_k_min = 0.85`, an toàn = `0`, `escalation_rate_max = 0.35`, `cost_per_ticket_vnd_max = 8000`, `roi_min = 0.25`, `queue_stuck_max = 0`) cùng `decision_rule` cho 4 quyết định và `stop_condition`.
- Xây dựng bản đồ dữ liệu (B3), phân tích trước kịch bản concept drift ngày `2026-12-01` khi chuyển `REFUND-v3` sang `REFUND-v4`, và thiết lập cổng `business` (`daily_refund_cap_vnd = 1500000`, `cost_budget_per_ticket_vnd = 1500`, `pilot_scope = all 100%`, `roi_min = 0.25`).
- Đối chiếu chi phí, ROI, hàng chờ và phân khúc kho/hãng ở cả 3 mốc (`base`, `prepared`, `after`) để viết specification câu 3.2, chốt quyết định v1 (`Tiếp tục`), v2 (`Tiếp tục`) và ba dòng bắt buộc cho thẻ S3.

### Bằng chứng

- Commit: `8f60657` (tiêu chí, TEAM.md, cổng `business`, Phiếu A & B), cùng commit hoàn thiện B8, C5 (3.2), C12 và mục cá nhân.
- Commit ký tiêu chí: `a6416fd`; checkpoint vòng 1: `40708a2c`.
- Các lần chạy chính thức trên máy chính: `R-base-before-20261118-172311-b161aa`, `R-base-prepared-20261118-173617-6203de`, `R-S3-grade-20261118-174246-66cedf`, `R-S3-after-20261118-174247-66cedf`, `R-base-after-20261118-174239-66cedf`.

### Exit ticket

- Một điều học được: Đặt và ký tiêu chí đo lường cả an toàn lẫn kinh tế–vận hành trước khi đo giúp tránh nới chuẩn theo kết quả, và chính sách thay đổi theo ngày (`concept drift`) có thể làm một trợ lý đang xanh hoàn toàn trên bộ nền thành lỗ ròng nếu không ghim nguồn sự thật.
- Một điều còn chưa chắc: Trên dữ liệu pilot thật ngoài MockLLM, sự biến thiên về độ dài văn bản, tỷ lệ sai sót của tracking DB và thời gian kiểm mẫu thực tế của nhân viên sẽ làm chi phí thực và ROI dịch chuyển bao nhiêu so với mức `4.405đ` / `1.27` trong mô phỏng.

*Dùng AI:* có sử dụng trợ lý AI để rà soát PRD/world data, tính toán đối chiếu chỉ số kinh doanh và soạn thảo câu chữ cho các phần của vai C trong `templates/` và `TEAM.md`; toàn bộ số liệu được kiểm chứng trực tiếp qua `lab10.eval` và `config/`.

## DamTuanLinh-2A202603624

### Phần việc phụ trách

Vận hành và pháp lý (vai D). Phụ trách:
- Phiếu A (`templates/form-a-criteria.md`): Câu 1.2 (mục A1) và Câu 1.4 (mục A2, cột Telemetry production).
- Phiếu B (`templates/form-b-evaluation-gates.md`): Câu 2.4 (mục B4 HAZOP vòng 1 và mục B5 Checklist go-live 9 nhóm việc), Câu 2.5 (mục B6 Pre-mortem 4 lăng kính), Câu 2.10 (mục B7.5 Runbook phần 1–3 và mục B7.6 Giờ cao điểm).
- Cấu hình cổng vận hành và pháp lý (`config/operating_gates.json` → mục `operations` và `legal`).
- Phiếu C (`templates/form-c-incident.md`): Câu 3.1 (mục C3.5 Mở lại bản đồ dữ liệu cho thẻ S3 và mục C4 HAZOP của thẻ S3), Câu 3.3 (mục C5 Giả định môi trường), Câu 3.7 (mục C9 Fault tree sau khi sửa, mục C10 Risk register, mục C11 Cập nhật checklist 9 nhóm việc và Runbook phần 4–5).
- Hoàn thiện `submission/submission.json` và rà soát checklist nộp bài.

### Đóng góp cụ thể

- **Khối 1 (Phiếu A):** Xác định mục tiêu đối soát của chị Oanh (`NV-OANH`) và mục tiêu SLA 60 phút / công suất 6 ca/giờ của chị Hạnh (`NV-HANH`); thiết kế telemetry không nhãn cho bước `file_carrier_fault` với cửa sổ trượt 60 phút và ngưỡng báo động `S >= 1`.
- **Khối 2 (Phiếu B & `operating_gates.json`):** Phân tích HAZOP trên `file_carrier_fault` và 3 thành phần ngoài code (người duyệt, dữ liệu gửi bên thứ ba, ngân sách); lập checklist 9 nhóm việc có PIC; soạn pre-mortem 4 lăng kính nối tới 3 cổng G1–G3; thiết lập `operations` (`pic: NV-TUNG`, `approver_id: NV-HANH`, `reviewers_on_shift: 1`, `max_queue_wait_minutes: 60`, `decision_note: true`, `review_sampling_pct: 10`, 5 điều kiện dừng) và `legal` (chặn 10 trường PII/ghi chú tự do, bắt buộc có `delay_cause`); viết Runbook 1–3 và kịch bản Giờ cao điểm.
- **Khối 3 (Phiếu C — Thẻ S3):** Mở lại bản đồ dữ liệu chỉ ra sự lệch giữa `index_active` và khoảng hiệu lực `[effective_from, effective_to]` khi sang ngày `2026-12-02` (`REFUND-v4`) cũng như trường hợp `delay_cause = null` (`O-2320-P1`); viết HAZOP 4 dòng cho S3 (bổ sung nhánh `INCAPABLE` vượt trần 2 lỗi/hãng/ngày ở `S3-42`/`S3-43`); cập nhật Fault tree sau khi sửa, thêm 2 dòng Risk register, cập nhật checklist và viết Runbook phần 4–5.

### Bằng chứng

- Commit: `71f8411` (Phiếu A câu 1.2, 1.4), `a9117e4` (Phiếu B mục B4, B5, B6), `8a00d79` (`config/operating_gates.json` mục `operations`/`legal` và Phiếu B mục B7.5, B7.6), `60ee678` (Phiếu C mục C3.5, C4, C5 câu 3.3, C9, C10, C11).
- Mã lần chạy đối chiếu từ máy chính (A): `R-base-before-20261118-172311-b161aa`, `R-base-prepared-20261118-173617-6203de`, `R-S3-grade-20261118-174246-66cedf` (`R-S3-before-20261118-174246-66cedf`, `R-S3-prepared-20261118-174247-66cedf`, `R-S3-after-20261118-174247-66cedf`), `R-base-after-20261118-174239-66cedf`.

### Exit ticket

- **Một điều học được:** Cổng bằng code chỉ bảo vệ được ở ranh giới lệnh gọi tool; để vận hành an toàn ngoài thực tế cần kết hợp cổng con số (`operating_gates.json`), quy trình đối soát độc lập của con người (`NV-OANH`, `NV-HANH`) và runbook có thời hạn dừng cụ thể (5 phút, do `NV-TUNG` giữ công tắc).
- **Một điều còn chưa chắc:** Khi dữ liệu gốc trong tracking DB hoặc bảng `policies` bị nhập sai nhưng vẫn hợp lệ về mặt hình thức, cả cổng code lẫn monitor tự động đều không tự phát hiện được ngay mà phải chờ đối soát thực tế với hãng vận chuyển.
- *Dùng AI:* Sử dụng trợ lý AI để hỗ trợ rà soát cấu trúc phiếu, đối chiếu số liệu trong `data/world.json` và soạn thảo văn bản; mọi con số, mã nhân viên và bằng chứng đều được kiểm tra lại theo dữ liệu và report từ máy chính.
