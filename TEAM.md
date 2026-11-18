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

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
