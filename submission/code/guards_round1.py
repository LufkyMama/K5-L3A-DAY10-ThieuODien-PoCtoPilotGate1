"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H
from .tools import Verdict


def _policy(ctx):
    """Chính sách đang hiệu lực theo NGÀY, không theo cờ index_active (cờ này do batch cập nhật)."""
    return H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)


def _as_int(v):
    try:
        return int(v)
    except (TypeError, ValueError):
        return 0


def pre_guard(ctx):
    # Cổng 1a — ghim phiên bản chính sách theo ngày hiệu lực (B4 H2; B6 dòng kỹ thuật "chính sách cũ").
    pol = _policy(ctx)
    if pol is None:
        return Verdict.escalate("không xác định được chính sách đang hiệu lực")
    return Verdict.allow(policy_id=pol["policy_id"])


def write_gate(ctx, action):
    tool = action.get("tool")
    if tool == "issue_refund":
        return _gate_refund(ctx, action)
    if tool == "file_carrier_fault":
        return _gate_carrier_fault(ctx, action)
    if tool == "notify_carrier":
        return _gate_notify(ctx, action)
    return Verdict.allow()


def _gate_refund(ctx, action):
    """Cổng 1b — tiền: đối chiếu quyền lợi với tracking + chính sách hiệu lực, kiểm phê duyệt, chặn ghi trùng.

    Ứng với B2 lỗi 1 (model tin số ngày khách khai), B4 H2 (policy hết hiệu lực), H4 (chỉ thị trong ticket),
    B6 dòng "model tin nhầm" và điều kiện phê duyệt của chị Hạnh.
    """
    order = ctx.tools.lookup_order(action.get("order_id"))
    if order is None:
        return Verdict.escalate("không tìm thấy đơn để đối chiếu quyền lợi")
    if order.get("customer_id") != ctx.ticket.get("customer_id"):
        return Verdict.escalate("người gửi không phải chủ đơn")

    tid = action.get("ticket_id")
    if ctx.tools.ledger_rows(ticket_id=tid):          # confirm 429 -> agent ghi lần 2
        return Verdict.deny("ticket này đã có khoản hoàn trong sổ cái, không ghi lặp")
    if order.get("refund_status") == "REFUNDED":
        return Verdict.deny("đơn đã được hoàn trước đó")

    pol = _policy(ctx)
    if pol is None:
        return Verdict.escalate("không xác định được chính sách đang hiệu lực")

    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of)
    expected = H.entitlement_vnd(pol, order, delay, parcel.get("delay_cause"))

    if expected <= 0:
        return Verdict.modify("không đủ điều kiện theo tracking + chính sách hiệu lực", amount_vnd=0)

    approval_id = action.get("approval_id")
    appr = None
    if approval_id:
        found = ctx.tools.lookup_approvals(approval_id=approval_id)
        appr = found[0] if found else None
    valid = (appr is not None
             and appr.get("status") == "valid"
             and appr.get("ticket_id") == tid
             and str(appr.get("expires_at") or "") >= ctx.as_of
             and _as_int(appr.get("max_vnd")) >= expected)

    if expected > _as_int(pol.get("auto_limit_vnd")):
        if not valid:
            return Verdict.escalate("vượt hạn mức tự động nhưng không có phê duyệt hợp lệ")
    elif approval_id and not valid:
        approval_id = None                          # phê duyệt chết/không đúng ticket, không cần nữa

    changes = {}
    if _as_int(action.get("amount_vnd")) != expected:
        changes["amount_vnd"] = expected
    if action.get("payer") != "LOGIX":               # directive trong ticket không được đổi người trả
        changes["payer"] = "LOGIX"
    if approval_id != action.get("approval_id"):
        changes["approval_id"] = approval_id
    if changes:
        return Verdict.modify("đối chiếu tracking + chính sách hiệu lực: sửa về đúng quyền lợi", **changes)
    return Verdict.allow()


def _gate_carrier_fault(ctx, action):
    """Cổng 2 — bên thứ ba: chỉ ghi lỗi cho đúng kiện trễ, đúng hãng, khi tracking có nguyên nhân thuộc lỗi hãng.

    Ứng với B6 ★G1, B4 H1 (parcels[0]), H2 (policy hết hiệu lực), H3 (thiếu cause), H4 (delay khách khai).
    """
    order = ctx.tools.lookup_order(action.get("order_id"))
    if order is None:
        return Verdict.deny("không có đơn để đối chiếu lỗi hãng")
    pol = _policy(ctx)
    if pol is None:
        return Verdict.deny("không xác định được chính sách đang hiệu lực")

    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of)
    if not H.carrier_at_fault(pol, parcel, delay):
        return Verdict.deny("tracking không ghi nguyên nhân thuộc lỗi hãng: không ghi lỗi oan")

    changes = {}
    if action.get("parcel_id") != parcel["parcel_id"]:
        changes["parcel_id"] = parcel["parcel_id"]
    if action.get("carrier_id") != parcel["carrier_id"]:
        changes["carrier_id"] = parcel["carrier_id"]
    if action.get("driver_id") != parcel.get("driver_id"):
        changes["driver_id"] = parcel.get("driver_id")
    if _as_int(action.get("delay_days")) != delay:
        changes["delay_days"] = delay
    if changes:
        return Verdict.modify("ghi lỗi theo đúng kiện trễ trong tracking", **changes)
    return Verdict.allow()


def _gate_notify(ctx, action):
    """Cổng 3 — dữ liệu rời hệ thống: chỉ gửi hãng các trường chính sách cho phép.

    Ứng với B6 ★G3 và dòng PERTURBED ngoài kỹ thuật ở B4 (customer_note/recipient_contact).
    """
    pol = _policy(ctx)
    allowed = set((pol or {}).get("carrier_notice_fields") or [])
    payload = action.get("payload") or {}
    if allowed:
        kept = {k: v for k, v in payload.items() if k in allowed}
        if kept != payload:
            return Verdict.modify("chỉ gửi hãng các trường chính sách cho phép", payload=kept)
    return Verdict.allow()
