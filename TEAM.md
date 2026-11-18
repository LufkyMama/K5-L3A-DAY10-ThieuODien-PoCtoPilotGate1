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
- Vòng 2 (S3): thêm trần `ops_limits.max_auto_strikes_per_carrier_per_day = 2` trong `file_carrier_fault`, chặn lỗi thứ 3 trở đi; nhờ đó `S3-42`/`S3-43` không còn bị ghi lỗi oan.
- Chạy mốc base, after, prepared; chốt cổng vòng 1 `40708a2c`; chạy lệnh 6 ba mốc và lệnh 7.

### Bằng chứng

- Commit: `dc7b7b1` (cổng vòng 1 + B7.1), `a1333a1` (checkpoint + B0 dòng 3), `b214d81` (trần lỗi hãng + C0/C1/C7), `7b744dc` (cập nhật theo grade cuối).
- Lần chạy: base `R-base-before-20261118-172311-b161aa`; after `R-base-after-20261118-173515-6203de`; prepared `R-base-prepared-20261118-173617-6203de`; S3 grade `R-S3-grade-20261118-174246-66cedf` (base/prepared/after `...174246/174247`); S3 after `R-S3-after-20261118-174231-66cedf`; base after vòng 2 `R-base-after-20261118-174239-66cedf`.
- Phiếu: A5 (C ghi), B0 dòng 1–3, B1, B7.1, C0 dòng 1–4, C1, C7.
- Hash: criteria `bacb89e1`, checkpoint `40708a2c`.

### Exit ticket

Học được: cổng tốt phải đọc nguồn sự thật (tracking, chính sách theo ngày, sổ cái) thay vì đọc chữ khách; sửa đúng một chỗ vẫn có thể làm hỏng ca đang đúng, nên lần nào cũng phải đo lại bộ nền. Còn chưa chắc: nếu chính tracking DB sai, hoặc máy thiếu gói sự cố S1/S2/S4–S8, thì cổng và `1 integrity` vẫn có điểm mù; cần Coach xác nhận trước khi chọn Tiếp tục.

*Dùng AI:* dùng trợ lý AI để đọc code, soạn nháp cổng và rà câu chữ trong phiếu; mọi con số và dòng trace được kiểm lại từ output thật của máy chính.
