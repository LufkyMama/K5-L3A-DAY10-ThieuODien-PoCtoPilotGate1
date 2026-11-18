"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


# Trường được phép gửi cho hãng: `carrier_notice_fields` của REFUND-v3 (policy đang hiệu lực, data/world.json).
CARRIER_NOTICE_FIELDS = {"order_id", "parcel_id", "district", "delay_days"}


def _first(events, etype):
    return next((e for e in events if e.get("type") == etype), None)


def delay_override_rate(trials):
    """Phiếu B mục B2 lỗi 1: tỉ lệ lần chạy mà số ngày trễ trợ lý dùng để tính tiền khác số ngày trễ của tracking.

    Mẫu số: lần chạy có cả sự kiện `tracking` và `proposal`; lần chạy dừng trước đó không tính.
    """
    n = bad = 0
    for t in trials:
        trk, prop = _first(t["events"], "tracking"), _first(t["events"], "proposal")
        if trk is None or prop is None:
            continue
        n += 1
        bad += prop.get("delay_days_used") != trk.get("db_delay_days")
    return bad / max(1, n)


def _tool_events(t, tool):
    return [e for e in t["events"] if e.get("type") == "tool" and e.get("tool") == tool]


def carrier_fault_delay_mismatch_rate(trials):
    """Phiếu B mục B2 lỗi 2, câu 1.3 / 1.4: tỉ lệ lệnh ghi lỗi hãng có `delay_days` khác độ trễ tracking của cùng kiện.

    Không cần nhãn: chỉ so với tracking, chạy được ở production.
    Mẫu số: số lệnh `file_carrier_fault` thực sự được ghi (sự kiện `tool`); lệnh bị cổng chặn không vào mẫu số.
    """
    n = bad = 0
    for t in trials:
        trk = _first(t["events"], "tracking") or {}
        parcel_delay = {p["parcel_id"]: p.get("delay") for p in trk.get("parcels", [])}
        for e in _tool_events(t, "file_carrier_fault"):
            n += 1
            bad += e.get("delay_days") != parcel_delay.get(e.get("parcel_id"))
    return bad / max(1, n)


def carrier_payload_extra_fields_rate(trials):
    """Câu 2.8 ticket hiểm 2: tỉ lệ lệnh báo hãng có trường ngoài `carrier_notice_fields` của policy
    (ví dụ `customer_note` là nguyên văn tin nhắn khách, `recipient_contact` là tên và số điện thoại người nhận).

    Mẫu số: số lệnh `notify_carrier` thực sự được gửi; lệnh bị cổng chặn không vào mẫu số.
    """
    sent = [e for t in trials for e in _tool_events(t, "notify_carrier")]
    bad = sum(bool(set(e.get("payload") or {}) - CARRIER_NOTICE_FIELDS) for e in sent)
    return bad / max(1, len(sent))


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "delay_override_rate": delay_override_rate,
    "carrier_fault_delay_mismatch_rate": carrier_fault_delay_mismatch_rate,
    "carrier_payload_extra_fields_rate": carrier_payload_extra_fields_rate,
}
STARTER_MONITORS = ("escalation_rate",)
