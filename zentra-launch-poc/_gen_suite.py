#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Zentra Launch — POC generator (English US).
Brand: ZAFA Property Group (client-facing) / Mr Tanah (admin, internal)
Output: ~/mockup-hartanah/zentra-launch-poc/  (noindex preview)
"""
import os

OUT = "/home/ubuntu/mockup-hartanah/zentra-launch-poc"
os.makedirs(OUT, exist_ok=True)

# ── Jenama = TETAPAN (dikonfirmasi Zahir 15/9/2026: Zentra Property Group)
BRAND = "Zentra Property Group"
SUITE = "Zentra Launch"
BANNER = ("PROOF OF CONCEPT / PREVIEW — not the live system. "
          "Sample structure where noted; project facts are real (Avalon @ Cybersouth). Noindex.")

NAV = [
    ("index.html", "Overview"),
    ("project-microsite.html", "A · Project Microsite"),
    ("unit-lock.html", "B · Unit Lock Board"),
    ("sales-board.html", "C · Sales Board"),
    ("billing-commission.html", "D · Billing &amp; Commission"),
    ("compliance.html", "E · Compliance &amp; Audit"),
    ("agent.html", "F · Agent Dashboard"),
    ("branding.html", "G · Branding (pending)"),
    ("design.html", "Design &amp; Roadmap"),
]

CSS = """
:root{--ink:#12241F;--muted:#5D6F69;--line:#DCE5E0;--bg:#F5F8F6;--card:#fff;
--green:#0C4437;--green2:#12604E;--gold:#C9A227;--ok:#1E7A4B;--warn:#B7791F;--bad:#B23A34;--info:#1F5F8B}
*{box-sizing:border-box}
body{margin:0;font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Roboto,Helvetica,Arial,sans-serif;color:var(--ink);background:var(--bg)}
a{color:var(--green2)}
.mockbar{background:#0C4437;color:#fff;font-size:12.5px;padding:8px 16px;letter-spacing:.01em}
.switch{display:flex;flex-wrap:wrap;gap:6px;padding:10px 16px;background:#fff;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:9}
.switch a{font-size:12.5px;padding:5px 10px;border:1px solid var(--line);border-radius:999px;text-decoration:none;color:#33463F}
.switch a.on{background:var(--green);color:#fff;border-color:var(--green)}
.wrap{max-width:1120px;margin:0 auto;padding:26px 18px 70px}
h1{font-size:clamp(23px,3.2vw,32px);line-height:1.25;margin:0 0 6px}
h2{font-size:19px;margin:30px 0 10px;padding-bottom:6px;border-bottom:2px solid var(--line)}
h3{font-size:15.5px;margin:0 0 6px}
.sub{color:var(--muted);font-size:14px;margin:6px 0 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px;margin:12px 0}
.grid{display:grid;gap:14px}
.g2{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}
.g3{grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}
.g4{grid-template-columns:repeat(auto-fit,minmax(190px,1fr))}
table{width:100%;border-collapse:collapse;font-size:13.5px;background:#fff;border:1px solid var(--line);border-radius:10px;overflow:hidden}
th,td{text-align:left;padding:8px 11px;border-bottom:1px solid var(--line);vertical-align:top}
th{background:#EFF4F1;font-size:12.5px;text-transform:uppercase;letter-spacing:.03em;color:#3B4F49}
tr:last-child td{border-bottom:none}
.muted{color:var(--muted)}
.pill{display:inline-block;font-size:11.5px;font-weight:700;padding:2px 9px;border-radius:999px;border:1px solid transparent;white-space:nowrap}
.p-ok{background:#E4F4EA;color:#166B41;border-color:#BFE3CC}
.p-warn{background:#FBF0DC;color:#8A5A0B;border-color:#EFD9AE}
.p-bad{background:#FBE7E5;color:#8E2C27;border-color:#EFC5C0}
.p-info{background:#E6F0F7;color:#1B4F73;border-color:#C3DAEA}
.p-grey{background:#EDF0EE;color:#4C5A55;border-color:#D8DFDB}
.note{background:#EAF4EF;border-left:4px solid var(--green2);padding:12px 14px;border-radius:8px;font-size:14px}
.warn{background:#FCF3E2;border-left:4px solid var(--warn);padding:12px 14px;border-radius:8px;font-size:14px}
.danger{background:#FBEDEB;border-left:4px solid var(--bad);padding:12px 14px;border-radius:8px;font-size:14px}
.kpi{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px}
.kpi b{display:block;font-size:26px;line-height:1.1;color:var(--green)}
.kpi span{font-size:12.5px;color:var(--muted)}
.grid-units{display:grid;grid-template-columns:120px repeat(10,minmax(0,1fr));gap:5px;font-size:12px}
.grid-units .blk{font-weight:700;color:#33463F;align-self:center}
.u{border:1px solid var(--line);border-radius:7px;padding:6px 3px;text-align:center;background:#fff}
.u small{display:block;font-size:9.5px;color:var(--muted)}
.u.av{background:#E9F6EE;border-color:#BFE3CC}
.u.lk{background:#FCF3E2;border-color:#EFD9AE}
.u.bk{background:#E6EFF8;border-color:#C3DAEA}
.u.sold{background:#F2F4F3;color:#8A9691}
.u.buf{background:#FBE7E5;border-color:#EFC5C0}
.legend{display:flex;flex-wrap:wrap;gap:12px;font-size:12.5px;margin-top:10px}
.legend i{display:inline-block;width:12px;height:12px;border-radius:3px;margin-right:5px;vertical-align:-1px;border:1px solid var(--line)}
input,select,textarea{font:inherit;padding:8px 10px;border:1px solid var(--line);border-radius:8px;width:100%;background:#fff}
label{font-size:12.5px;font-weight:600;color:#3B4F49;display:block;margin:10px 0 4px}
.btn{display:inline-block;background:var(--green);color:#fff;text-decoration:none;padding:10px 16px;border-radius:9px;font-weight:700;font-size:14px;border:none;cursor:pointer}
.btn.sec{background:#fff;color:var(--green);border:1px solid var(--green)}
.bar{height:9px;border-radius:6px;background:#E7EDEA;overflow:hidden}
.bar>i{display:block;height:100%;background:var(--green2)}
code{background:#EDF1EF;padding:1px 5px;border-radius:5px;font-size:12.5px}
.foot{color:var(--muted);font-size:12.5px;margin-top:34px;border-top:1px solid var(--line);padding-top:14px}
"""


def table(head, rows):
    out = ['<table><thead><tr>'] + ['<th>%s</th>' % h for h in head] + ['</tr></thead><tbody>']
    for r in rows:
        out.append('<tr>' + ''.join('<td>%s</td>' % c for c in r) + '</tr>')
    out.append('</tbody></table>')
    return ''.join(out)


def pill(txt, cls='p-grey'):
    return '<span class="pill %s">%s</span>' % (cls, txt)


def page(fname, title, subtitle, body, active=None):
    nav = ''.join('<a href="%s" class="%s">%s</a>' % (h, 'on' if h == (active or fname) else '', t) for h, t in NAV)
    html = ('<!doctype html><html lang="en-US"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<meta name="robots" content="noindex,nofollow">'
            '<title>%s — %s</title><style>%s</style></head><body>'
            '<div class="mockbar">%s</div><div class="switch">%s</div>'
            '<div class="wrap"><h1>%s</h1><p class="sub">%s</p>%s'
            '<div class="foot"><b>%s</b> — Prepared for Zahir MJ by Mr Tanah (internal admin). '
            'Client-facing brand: <b>%s</b>. This preview is a design proposal, not a live system.</div>'
            '</div></body></html>') % (title, SUITE, CSS, BANNER, nav, title, subtitle, body, SUITE, BRAND)
    # Normalisasi jenama: semua token ZAFA ditukar ke nilai TETAPAN (tukar nama = tukar BRAND/SUITE di atas)
    html = (html.replace("ZAFA Property Group", BRAND)
                .replace("ZAFA Sales Suite", SUITE)
                .replace("Zentra Sales Suite", SUITE)   # nama kerja lama (15/9) — jangan terbit semula
                .replace("ZAFA", BRAND))
    open(os.path.join(OUT, fname), 'w', encoding='utf-8').write(html)
    return fname


# ------------------------------------------------------------------ shared facts
AVALON = dict(
    name="Avalon @ Cybersouth",
    dev="Ecolake Residence Sdn Bhd (Avaland Berhad)",
    dl="30240/10-2027/0239(A) — valid 12/10/2022 – 11/10/2027",
    permit="30240-3/07-2028/0539(N)-(S) — valid 07/07/2025 – 06/07/2028",
    pbt="Majlis Perbandaran Sepang (MP Sepang)",
    loc="Cybersouth, Dengkil, Selangor",
    tenure="Leasehold 82 years — expires 14 Nov 2104",
    units="343 units (permitted phase: 166)",
    type="2-storey terrace (strata)",
    size="2,004 – 2,454 sq ft",
    price="From RM803,800 (list: RM1,004,750 – RM1,856,000)",
    completion="July 2028",
)

gate_rows = [
    ["Compliance gate", "Rule enforced by the system", "Effect if it fails"],
    ["Developer licence (DL) &amp; advertising permit (APDL)",
     "Permit number, validity and authorised-agent name must be present before any project page can be published or promoted.",
     pill("Page blocked / noindex", 'p-bad')],
    ["No pre-SPA payment",
     "Unit reservation is <b>zero-deposit (RM0)</b>. The system refuses any client-money collection before a signed SPA (Reg. 11(2), HDR 1989). 10% goes to the developer's HDA only after eSPA.",
     pill("Payment fields disabled", 'p-bad')],
    ["eSPA via HIMS (mandatory since 1 Jan 2026)",
     "Unit and buyer data must exist in HIMS before SPA generation; eKYC (MyKad + biometrics) at booking.",
     pill("SPA blocked upstream", 'p-warn')],
    ["e-Invoice (LHDN MyInvois)",
     "Every invoice carries the <b>registered legal name + TIN</b>; trade name is display-only. TIN validated before issue.",
     pill("Invoice cannot be issued", 'p-warn')],
    ["PDPA 2010 (Act 709)",
     "Consent captured per purpose, 72-hour breach-notification workflow, DPO recorded.",
     pill("Data export blocked", 'p-warn')],
    ["Bumiputera lot release",
     "Bumi status per unit, discount, release approval reference and date tracked; release requires state-authority consent.",
     pill("Unit stays locked", 'p-info')],
]

# ------------------------------------------------------------------ 1. OVERVIEW
overview_body = (
    '<div class="note"><b>What this is:</b> a proposed sales system for new property launches, operated by '
    '<b>Mr Tanah</b> (internal admin) and presented to clients as <b>ZAFA Property Group</b> — '
    '“System provided by ZAFA Property Group”. The suite name is <b>ZAFA Sales Suite</b>. '
    'Language: <b>English (US)</b> client-facing, with a Malay (ms-MY) layer for internal MT operations.</div>'
    '<div class="warn" style="margin-top:12px"><b>Why not just buy a developer system?</b> Mr Tanah is the '
    '<b>appointed sales &amp; marketing agency</b>, not the developer. Developer platforms (MHub, PropertyX/IFCA) '
    'own unit inventory and HIMS/eSPA generation. The agency layer — leads, agents, temporary unit locks, '
    'booking packs, loan follow-up, document compliance and commission — is where Mr Tanah needs its own system, '
    'and where it must <b>plug into</b> the developer platform rather than replace it.</div>'

    '<h2>Module map — six layers</h2>' +
    table(["Layer", "What it does", "Where it lives"], [
        ["1 · Public", "Project microsites, live unit availability, zero-deposit EOI, appointment booking, AI assistant, WhatsApp", "zafaproperties.com + mrtanah.com/projek-baharu"],
        ["2 · Sales operations", "Agent onboarding, lead routing, temporary unit locks, pricing/discount engine, booking pack, eKYC", "ZAFA Sales Suite (agent + admin)"],
        ["3 · Transaction", "Loan submission &amp; consent, eSPA/HIMS tracking, document room per party, milestone billing, VP &amp; defect tracking", "Suite + role portals"],
        ["4 · Compliance &amp; governance", "DL/APDL register &amp; expiry monitor, no-client-money enforcement, PDPA consent registry, immutable audit trail", "Suite (admin only)"],
        ["5 · Finance", "Commission accrual → release at milestones, agent payouts, service fee invoicing, e-invoice", "Suite + ZMJ Solutions accounting"],
        ["6 · Data &amp; AI", "Take-up, funnel conversion, agent performance, market intelligence, AI assistant on project pages", "Suite dashboards + Ali"],
    ]) +

    '<h2>Core design principles (10)</h2><ol>'
    '<li><b>No client money at Mr Tanah.</b> Reservations are RM0 (EOI/OTP). The 10% deposit reaches the developer\'s HDA only after a signed SPA.</li>'
    '<li><b>One unit, one lock.</b> Every lock has an owner, a timer and an audit record — no double selling.</li>'
    '<li><b>Enter data once.</b> The same record feeds HIMS/eSPA, invoicing and commissions.</li>'
    '<li><b>Compliance gates, not reminders.</b> Missing DL/APDL, expired permits or unconsented data block publication.</li>'
    '<li><b>Buyer-side transparency.</b> Buyers choose their own lawyer (RFQ tender) and financier; Mr Tanah takes no kickbacks and adds no fees.</li>'
    '<li><b>Role-based portals.</b> Token links per buyer, seller, agent, lawyer, banker — the same pattern already used by the Mr Tanah portal.</li>'
    '<li><b>Immutable audit trail.</b> Who locked, booked, changed price or released a unit — recorded forever.</li>'
    '<li><b>Build on existing assets.</b> Notion databases, Google Workspace, Apps Script, WhatsApp, Billplz/DuitNow QR, AI assistant.</li>'
    '<li><b>Modular 5 phases.</b> Each phase delivers standalone value.</li>'
    '<li><b>KPI driven.</b> Lock→booking time, loan approval rate, time-to-SPA, take-up per phase.</li>'
    '</ol>'

    '<h2>End-to-end flows (12)</h2>' + table(["#", "Flow", "Key control"], [
        ["1", "Developer appointment → project data intake (DL, APDL, price list, unit schedule)", "Permit register + authorised-agent check"],
        ["2", "Project microsite publish (phase, unit availability, price from, documents)", "Compliance gate blocks publish"],
        ["3", "Lead capture (ads, WhatsApp, referrals, walk-in) → routing to agents", "Source tracking + PDPA consent"],
        ["4", "Zero-deposit EOI / pre-launch queue with priority classes", "Queue position + unit preference"],
        ["5", "Unit locking (temporary hold, buffer, agency-level lock policy)", "Timer + audit"],
        ["6", "Booking pack (forms, documents, NRIC/passport, buyer + joint buyer)", "eKYC before submission"],
        ["7", "Developer HIMS/eSPA submission and status tracking", "Zero-mismatch data validation"],
        ["8", "Loan submission, banker consent, approval tracking, valuation", "Consent capture + rejection alerts"],
        ["9", "Milestone billing per Third Schedule (Jadual Ketiga) with e-invoice", "Architect certificate gate"],
        ["10", "Vacant possession, defect list, defects-liability expiry", "VP date drives retention &amp; commission"],
        ["11", "Commission accrual → release at milestones → agent payout", "Event-based release, overpayment prevention"],
        ["12", "Post-sale: referrals, repeat buyers, project reporting to developer", "Repeat-buyer history"],
    ]) +

    '<h2>Roadmap — 5 phases, 8–12 weeks</h2>' + table(["Phase", "Scope", "Duration", "Deliverable"], [
        ["<b>F1</b>", "Project register + microsite v3 (live unit availability) + zero-deposit EOI + DL/APDL gate", "1–2 weeks", "Public project pages that can legally take enquiries"],
        ["<b>F2</b>", "Unit inventory + temporary lock board + agent dashboard + booking pack", "2–3 weeks", "Agent-ready sales desk"],
        ["<b>F3</b>", "Buyer portal, eKYC, loan submission &amp; consent, eSPA/HIMS tracking, document room", "2–3 weeks", "Transaction tracking per party"],
        ["<b>F4</b>", "Milestone billing, e-invoice, commission engine, agent payouts", "3–4 weeks", "Finance &amp; commission control"],
        ["<b>F5</b>", "BI dashboards, AI assistant, developer/HIMS integration, market intelligence", "Ongoing", "Scale &amp; optimisation"],
    ]) +

    '<h2>Screens in this proof of concept</h2>' + table(["Screen", "For", "What it shows"], [
        ["A · Project Microsite", "Buyers / public", "Real project facts, unit availability, zero-deposit EOI, APDL panel, EN/BM switch"],
        ["B · Unit Lock Board", "Sales admin", "Block-by-block unit grid with status, locks, buffers and audit"],
        ["C · Sales Board", "Management", "Take-up, funnel, alerts and phase performance"],
        ["D · Billing &amp; Commission", "Finance", "Third Schedule milestones + event-based commission release"],
        ["E · Compliance &amp; Audit", "Admin / auditor", "DL-APDL, eSPA/HIMS, e-invoice, PDPA, bumi release, audit trail"],
        ["F · Agent Dashboard", "Agents", "My EOIs, my locks, my bookings, my commissions"],
        ["G · Branding", "Zahir", "ZAFA Property Group (client) vs Mr Tanah (admin), e-invoice legal-name rule, name/domain checks"],
    ])
)

page("index.html", "Proof of Concept",
     "New-launch sales system for Mr Tanah · client-facing brand: %s · English (US)" % BRAND, overview_body)

# ------------------------------------------------------------------ 2. PROJECT MICROSITE
micro = (
    '<div class="card">'
    '<div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:12px">'
    '<div><div style="font-size:22px;font-weight:800;letter-spacing:-.01em">%s</div>'
    '<div class="muted">%s · %s</div></div>'
    '<div style="text-align:right"><div class="pill p-ok">Advertising permit valid</div>'
    '<div class="muted" style="font-size:12.5px;margin-top:6px">Permit expires 06 Jul 2028</div></div></div>'
    '<div class="grid g2" style="margin-top:14px">'
    '<div><table><tbody>'
    '<tr><th>Developer</th><td>%s</td></tr>'
    '<tr><th>Developer licence</th><td>%s</td></tr>'
    '<tr><th>Advertising permit (Reg. 6)</th><td>%s</td></tr>'
    '<tr><th>Local authority</th><td>%s</td></tr>'
    '</tbody></table></div>'
    '<div><table><tbody>'
    '<tr><th>Tenure</th><td>%s</td></tr>'
    '<tr><th>Units</th><td>%s</td></tr>'
    '<tr><th>Type / built-up</th><td>%s · %s</td></tr>'
    '<tr><th>Price</th><td>%s</td></tr>'
    '<tr><th>Expected completion</th><td>%s</td></tr>'
    '</tbody></table></div></div></div>'

    '<h2>Live availability (phase 2)</h2>'
    '<div class="grid g4">'
    '<div class="kpi"><b>62</b><span>Units released</span></div>'
    '<div class="kpi"><b>31</b><span>Available</span></div>'
    '<div class="kpi"><b>21</b><span>Locked / under booking</span></div>'
    '<div class="kpi"><b>10</b><span>Booked / SPA signed</span></div></div>'
    '<p class="muted" style="font-size:12.5px">Availability figures = sample structure for this preview; project facts above are real.</p>'

    '<h2>Register your interest — zero deposit (RM0)</h2>'
    '<div class="warn"><b>Reg. 11(2), Housing Development (Control &amp; Licensing) Regulations 1989:</b> '
    'no payment of any kind may be collected before a signed SPA — not by the developer\'s agent, the lawyer or any stakeholder. '
    'This form therefore collects <b>no money and takes no payment details</b>. It registers your interest and reserves '
    'a queue position only.</div>'
    '<div class="card"><div class="grid g2">'
    '<div><label>Full name (as per MyKad)</label><input placeholder="e.g. Ahmad bin Ali">'
    '<label>Mobile (WhatsApp)</label><input placeholder="+60 12-345 6789">'
    '<label>Email</label><input placeholder="name@email.com"></div>'
    '<div><label>Unit type of interest</label><select><option>Type A — 2,004 sq ft</option><option>Type B — 2,238 sq ft</option><option>Type C — 2,454 sq ft</option></select>'
    '<label>Preferred block / floor</label><input placeholder="e.g. Block B, level 2">'
    '<label>How did you hear about this project?</label><select><option>Agent referral</option><option>Facebook / Instagram</option><option>Google search</option><option>Walk-in / sales gallery</option></select></div></div>'
    '<div class="grid g2" style="margin-top:12px">'
    '<div><label>I consent to my details being processed for this enquiry (PDPA 2010)</label>'
    '<select><option>Yes — consent given</option><option>No</option></select></div>'
    '<div style="align-self:end"><button class="btn">Submit interest (RM0)</button> '
    '<span class="muted" style="font-size:12.5px;display:inline-block;margin-left:8px">No payment step exists.</span></div></div></div>'

    '<h2>What happens next (buyer view)</h2>' + table(["Step", "What you do", "What the system does"], [
        ["1", "Submit this form (RM0)", "Creates an EOI with a queue position; issues a reference number by WhatsApp/email"],
        ["2", "Attend a viewing or sales-gallery appointment", "Assigns an agent, records attendance, prepares the booking pack"],
        ["3", "Confirm the unit", "Places a temporary lock on that unit; no money changes hands"],
        ["4", "Sign the Sale &amp; Purchase Agreement", "Digital SPA is generated through KPKT HIMS with eKYC and e-stamping; the 10 per cent deposit falls due to the developer\'s Housing Development Account"],
        ["5", "Apply for financing", "System tracks bank submissions, consents and approvals; buyers may compare 2–3 financiers"],
        ["6", "Follow construction &amp; billing", "Milestone billing per the Third Schedule; progress visible in your portal"],
        ["7", "Vacant possession", "Handover, defect list and defects-liability period tracked"],
    ]) +
    '<div class="note">Two-language layer: the microsite ships in <b>English (US)</b> with a '
    '<span class="pill p-info">EN</span> <span class="pill p-grey">BM</span> switch; content is stored per language so buyer '
    'communications can follow each buyer\'s preference.</div>'
) % (AVALON['name'], AVALON['loc'], AVALON['type'], AVALON['dev'], AVALON['dl'], AVALON['permit'],
     AVALON['pbt'], AVALON['tenure'], AVALON['units'], AVALON['type'], AVALON['size'], AVALON['price'], AVALON['completion'])

page("project-microsite.html", "A · Project Microsite (public)", "Buyer-facing page for one launch — real facts, zero-deposit EOI", micro)

# ------------------------------------------------------------------ 3. UNIT LOCK BOARD
def unit_cell(no, status, code):
    return '<div class="u %s">%s<small>%s</small></div>' % (code, no, status)

blocks = [
    ("Block A", ["A-01-01", "A-01-02", "A-01-03", "A-01-04", "A-01-05", "A-01-06", "A-01-07", "A-01-08", "A-01-09", "A-01-10"],
     ["av", "av", "lk", "av", "bk", "av", "sold", "av", "av", "av"]),
    ("Block B", ["B-02-01", "B-02-02", "B-02-03", "B-02-04", "B-02-05", "B-02-06", "B-02-07", "B-02-08", "B-02-09", "B-02-10"],
     ["av", "lk", "lk", "av", "av", "bk", "av", "av", "sold", "av"]),
    ("Block C", ["C-03-01", "C-03-02", "C-03-03", "C-03-04", "C-03-05", "C-03-06", "C-03-07", "C-03-08", "C-03-09", "C-03-10"],
     ["buf", "av", "av", "lk", "av", "av", "av", "bk", "av", "sold"]),
]
st_map = {"av": "Available", "lk": "Locked", "bk": "Booked", "sold": "SPA signed", "buf": "Buffer"}

grid_html = '<div class="grid-units">'
for name, nos, sts in blocks:
    grid_html += '<div class="blk">%s</div>' % name
    for n, s in zip(nos, sts):
        grid_html += unit_cell(n, st_map[s], s)
grid_html += '</div>'

lockboard = (
    '<div class="warn">Unit-level data below is <b>sample structure</b> — Mr Tanah does not yet hold a unit schedule '
    'from any developer. Real inventory must come from the developer (or their platform such as MHub/PropertyX) and be '
    'kept in sync with HIMS before any unit is offered.</div>'
    '<h2>Unit grid — Phase 2 (sample)</h2><div class="card">' + grid_html +
    '<div class="legend">'
    '<span><i style="background:#E9F6EE"></i>Available</span>'
    '<span><i style="background:#FCF3E2"></i>Locked (temporary hold)</span>'
    '<span><i style="background:#E6EFF8"></i>Booked</span>'
    '<span><i style="background:#F2F4F3"></i>SPA signed</span>'
    '<span><i style="background:#FBE7E5"></i>Buffer / bumi hold</span></div></div>'

    '<h2>Active locks</h2>' + table(["Unit", "Status", "Held by", "Agent", "Expires", "Note"], [
        ["B-02-02", pill("Locked", 'p-warn'), "Agency lock", "Siti (MT)", "in 3 h 20 m", "Buyer viewing at 4 pm"],
        ["B-02-03", pill("Locked", 'p-warn'), "Zahir (MT)", "Zahir", "in 22 h", "Awaiting spouse decision + joint-buyer docs"],
        ["C-03-04", pill("Locked", 'p-warn'), "FA Realty (co-agency)", "Danial", "expires today 18:00", "Co-agency: 50% split pre-agreed"],
        ["C-03-01", pill("Buffer", 'p-bad'), "Developer", "—", "—", "Bumiputera release pending state consent"],
    ]) +

    '<h2>Lock policy (applies to every unit)</h2>' + table(["Rule", "Default", "Who can override"], [
        ["Standard hold", "24 hours from lock creation", "Sales lead"],
        ["Sales-gallery hold", "4 hours", "Agent"],
        ["Buffer / bumi hold", "Until release approval is recorded", "Admin only"],
        ["Maximum concurrent locks per agent", "3 units", "Sales lead"],
        ["Auto-release", "On expiry, or 30 min after a missed appointment", "System (automatic)"],
        ["Same-unit double booking", "Blocked — the lock must expire or be released first", "Nobody"],
    ]) +
    '<div class="note"><b>Why locking matters:</b> buyers lose trust the moment two agents promise the same unit. '
    'The lock record is also the evidence trail for developer disputes and co-agency commission splits.</div>'

    '<h2>Audit trail (immutable)</h2>' + table(["Time", "Actor", "Action", "Unit", "Detail"], [
        ["15/09 09:12", "Siti (MT)", "Lock created", "B-02-02", "Hold 24 h · reason: viewing"],
        ["15/09 09:41", "System", "Availability refreshed", "—", "Sync with developer platform"],
        ["15/09 10:05", "Zahir (MT)", "Lock extended", "B-02-03", "24 h → 48 h · reason: joint buyer"],
        ["15/09 11:20", "Danial (FA Realty)", "Lock created", "C-03-04", "Co-agency hold 8 h"],
        ["15/09 12:02", "System", "Auto-release", "A-02-07", "Hold expired, unit returned to Available"],
    ])
)

page("unit-lock.html", "B · Unit Lock Board", "Temporary unit holds, buffers and a full audit trail", lockboard)

# ------------------------------------------------------------------ 4. SALES BOARD
sales = (
    '<div class="grid g4">'
    '<div class="kpi"><b>48.4%</b><span>Take-up (phase 2, sample)</span></div>'
    '<div class="kpi"><b>31</b><span>EOI received this month</span></div>'
    '<div class="kpi"><b>41.2%</b><span>Loan approval rate (industry, 2025)</span></div>'
    '<div class="kpi"><b>4.2 → 1.0</b><span>EOI → booking conversion target</span></div></div>'

    '<h2>Funnel — last 30 days (sample)</h2>' + table(["Stage", "Count", "Conversion", "Median age"], [
        ["Microsite visits", "4,182", "—", "—"],
        ["Enquiries / EOIs", "31", "0.74% of visits", "—"],
        ["Agent appointments", "19", "61% of EOIs", "2.1 days"],
        ["Unit locks", "12", "63% of appointments", "1.4 days"],
        ["Bookings", "8", "67% of locks", "3.0 days"],
        ["Loan approvals", "5", "63% of bookings", "18 days"],
        ["SPA signed", "4", "80% of approvals", "26 days"],
    ]) +
    '<div class="note"><b>Benchmark context (Malaysia, 1Q2026):</b> loan applications hit RM470.5 billion in 2025 — the highest in five years — '
    'yet only <b>41.2%</b> were approved. Speed and early eligibility screening, not persuasion, decide who converts. '
    'That is why Phase 3 prioritises eligibility screening and lender follow-up.</div>'

    '<h2>Phase performance</h2>' + table(["Phase", "Released", "Available", "Locked", "Booked", "SPA signed", "Take-up"], [
        ["Phase 1 (166 units)", "166", "0", "0", "0", "166", '<div class="bar"><i style="width:100%"></i></div> 100%'],
        ["Phase 2 (62 units, sample)", "62", "31", "21", "6", "4", '<div class="bar"><i style="width:48%"></i></div> 48.4%'],
        ["Phase 3 (not released)", "—", "—", "—", "—", "—", pill("Pending permit", 'p-warn')],
    ]) +

    '<h2>Alerts the board raises</h2>' + table(["Alert", "Trigger", "Owner"], [
        [pill("Permit expiry", 'p-bad'), "APDL or developer licence expires within 90 days", "Admin"],
        [pill("Stale lock", 'p-warn'), "Unit locked more than 48 h without progress", "Sales lead"],
        [pill("Loan stalled", 'p-warn'), "No lender update for 7 days after submission", "Financing desk"],
        [pill("Billing overdue", 'p-bad'), "Milestone invoice unpaid 21 working days after notice", "Finance"],
        [pill("Defect liability", 'p-info'), "Defects-liability period ends within 30 days", "Handover team"],
        [pill("HIMS mismatch", 'p-bad'), "Unit or buyer data differs from HIMS record", "Admin"],
    ]) +
    '<div class="note">Every alert carries a named owner and an escalation path — silent dashboards are useless. '
    'Alerts route to the internal operations bot (Mr Tanah) and, where appropriate, to the client\'s portal.</div>'
)

page("sales-board.html", "C · Sales Board", "Take-up, funnel, phase performance and exception alerts", sales)

# ------------------------------------------------------------------ 5. BILLING & COMMISSION
billing = (
    '<div class="note">Schedule G (landed) and Schedule H (strata) agreements under the Housing Development '
    '(Control &amp; Licensing) Act 1966 dictate when money may be collected. Below is the statutory payment schedule '
    'for a Schedule G agreement — the billing engine follows it exactly and refuses early billing.</div>'

    '<h2>Statutory payment schedule (Schedule G, Third Schedule)</h2>' +
    table(["Milestone", "%", "Gate before invoicing", "Typical evidence"], [
        ["On signing the SPA", "10%", "Signed agreement (eSPA)", "eSPA reference + e-stamp certificate"],
        ["Foundation works", "10%", "Architect certificate", "Form/certificate (architect or engineer)"],
        ["Reinforced concrete framework", "15%", "Architect certificate", "Certificate + site photos"],
        ["Walls with door &amp; window frames fixed", "10%", "Architect certificate", "Certificate"],
        ["Roof, wiring, plumbing, gas and telephone cables", "10%", "Architect certificate", "Certificate"],
        ["Internal &amp; external plastering", "10%", "Architect certificate", "Certificate"],
        ["Sewerage works", "5%", "Architect certificate", "Certificate"],
        ["Drains", "5%", "Architect certificate", "Certificate"],
        ["Roads", "5%", "Architect certificate", "Certificate"],
        ["Vacant possession (water &amp; electricity ready)", "12.5%", "Handover notice", "VP notice + key handover record"],
        ["After title documents &amp; Memorandum of Transfer served (or VP, whichever later)", "2.5%", "21 working days after service", "Document service record"],
        ["Retained by developer\'s solicitor as stakeholder", "5%", "6 months (2.5%) and 18 months (2.5%) after VP", "Stakeholder release instruction"],
    ]) +
    '<div class="warn"><b>Late-payment interest:</b> typical agreements allow 10% p.a. on overdue instalments after '
    '21 working days\' notice. The billing engine therefore calculates the notice date, the grace period and any interest '
    'automatically — and never sends a demand without the architect certificate attached.</div>'

    '<h2>Billing status (sample)</h2>' + table(["Unit", "Milestone", "Amount", "Invoiced", "e-Invoice", "Payment"], [
        ["B-02-06", "On signing SPA (10%)", "RM 102,300", "12/09/2026", pill("Validated", 'p-ok'), pill("Paid", 'p-ok')],
        ["A-01-05", "Foundation (10%)", "RM 118,900", "08/09/2026", pill("Validated", 'p-ok'), pill("Paid", 'p-ok')],
        ["C-03-08", "Framework (15%)", "RM 214,600", "10/09/2026", pill("Pending TIN", 'p-warn'), pill("Due 40 days", 'p-info')],
        ["B-02-09", "Plastering (10%)", "RM 131,750", "01/09/2026", pill("Validated", 'p-ok'), pill("Overdue", 'p-bad')],
    ]) +
    '<div class="note"><b>e-Invoice rule:</b> the issuing entity\'s <b>registered legal name and TIN</b> must appear on every '
    'invoice — a trade name such as “ZAFA Property Group” may be displayed as a brand but cannot replace the registered name. '
    'Current instruction: issue under <b>ZMJ Solutions</b>, with the ability to switch to a new group company once registered.</div>'

    '<h2>Commission engine — event-based release</h2>'
    '<div class="warn" style="margin-bottom:10px"><b>Proposed release schedule (awaiting Zahir\'s decision):</b> '
    '10% on booking · 25% on SPA signed · 25% on loan approval · 40% on vacant possession. '
    'Alternative: gate the final tranche on commission actually received from the developer.</div>' +
    table(["Event", "Trigger", "Release", "Evidence required"], [
        ["Booking", "Booking accepted by developer", "10%", "Signed booking form + developer acknowledgement"],
        ["SPA signed", "eSPA executed in HIMS", "25%", "eSPA reference + e-stamp"],
        ["Loan approved", "Letter of Offer accepted", "25%", "LOO + acceptance"],
        ["Vacant possession", "VP delivered", "40%", "VP notice + key handover"],
    ]) +
    table(["Agent", "Project", "Units", "Accrued", "Released", "Held", "Next release"], [
        ["Siti", "Avalon @ Cybersouth", "3", "RM 12,240", "RM 3,060", "RM 9,180", "SPA signed (25%)"],
        ["Danial (co-agency)", "Avalon @ Cybersouth", "1", "RM 4,080", "RM 408", "RM 3,672", "Loan approved (25%)"],
        ["Fadilah", "Avalon @ Cybersouth", "2", "RM 8,160", "RM 2,040", "RM 6,120", "VP (40%)"],
    ]) +
    '<div class="note">Commission figures are sample numbers to show the structure. Developer commission rates, co-agency '
    'splits and any rebate treatment must be recorded in the agency appointment letter before they are relied on.</div>'
)

page("billing-commission.html", "D · Billing &amp; Commission", "Statutory milestone billing plus event-based commission release", billing)

# ------------------------------------------------------------------ 6. COMPLIANCE
compliance = (
    '<div class="note">Compliance is enforced as a <b>gate</b>, not a reminder: if a rule fails, the affected action '
    'is blocked and the failure is logged with an owner. Nothing here is advisory-only.</div>'
    '<h2>Gate register</h2>' + table(["Gate", "Rule enforced", "Current state"], gate_rows[1:]) +

    '<h2>Project permit register</h2>' + table(["Project", "Developer licence", "Advertising permit", "Expiry", "Status"], [
        ["Avalon @ Cybersouth (Phase 2)", "30240/10-2027/0239(A)", "30240-3/07-2028/0539(N)-(S)", "06/07/2028", pill("Compliant", 'p-ok')],
        ["Setia Seraya P15 (sample)", "—", "—", "—", pill("Permit not provided", 'p-bad')],
        ["Terra Residences (sample)", "—", "—", "—", pill("Expiring in 62 days", 'p-warn')],
    ]) +
    '<div class="danger" style="margin-top:10px">A project page may only be published when, at minimum: the developer '
    'licence and advertising permit numbers are recorded, the permit is valid today, the authorised agent (ejen diberi kuasa) '
    'matches our appointment, and the price list version is dated. Otherwise the page stays <code>noindex</code> with a visible '
    'compliance notice — never a soft “coming soon” teaser that still markets the project.</div>'

    '<h2>eSPA / HIMS readiness</h2>' + table(["Requirement (effective 1 Jan 2026)", "Owner", "State"], [
        ["All units registered in HIMS before sale", "Developer", pill("Developer action", 'p-info')],
        ["Two-way sync of bookings → HIMS reference", "Platform partner", pill("To be confirmed", 'p-warn')],
        ["Buyer identity validation (MyKad + biometric eKYC)", "Developer / iDsaya", pill("At booking", 'p-info')],
        ["Zero-mismatch data between sales system and HIMS", "Mr Tanah (data quality)", pill("Validated", 'p-ok')],
        ["e-Stamping via LHDN before SPA execution", "Solicitor / developer", pill("Tracked", 'p-info')],
        ["Banks accept eSPA only with supporting documents", "Financing desk", pill("Checklist built", 'p-ok')],
    ]) +
    '<div class="note"><b>Design consequence:</b> because eSPA is generated by the developer through HIMS, the agency system '
    'must treat HIMS as the source of truth for SPA status. Our job is to keep unit, buyer and pricing data '
    '<b>clean enough to pass validation the first time</b> — mismatches stop sales outright.</div>'

    '<h2>Privacy, e-invoice and bumi</h2>' + table(["Area", "Requirement", "How the suite handles it"], [
        ["PDPA 2010 (Act 709)", "Consent per purpose; breach notification to the Commissioner as soon as practicable and within 72 hours; significant-scale breaches notified to affected individuals; DPO appointed",
         "Consent registry per purpose, breach playbook, DPO recorded, data-subject request workflow"],
        ["e-Invoice (LHDN MyInvois)", "Registered legal name + TIN; buyer TIN validation; 72-hour cancellation window",
         "TIN validated before issue; invoice PDF stores validation reference and UUID"],
        ["Bumiputera lots", "State-level quota and discount; release only with state-authority consent after the required advertising period",
         "Per-unit bumi status, discount field, release reference and date; units stay buffered until approval is recorded"],
        ["Anti-money-laundering (agency duties)", "Customer due diligence on buyers and sources of funds",
         "CDD checklist attached to the booking pack; documents stored with access control"],
    ]) +

    '<h2>Audit trail</h2>' + table(["Who can see what", "Buyer", "Agent", "Co-agency", "Admin (MT)", "Developer", "Lawyer / banker"], [
        ["Buyer contact details", "Own record", "Own leads only", "Own leads only", "Yes", "Booked units only", "Own case only"],
        ["Unit status &amp; locks", "Aggregate only", "Yes", "Yes", "Yes", "Yes", "Own case only"],
        ["Commission detail", "No", "Own only", "Own only", "Yes", "Per agreement", "No"],
        ["Permit register", "Public summary", "Yes", "Yes", "Yes", "Yes", "Yes"],
        ["Audit log", "No", "No", "No", "Yes", "No", "No"],
    ])
)

page("compliance.html", "E · Compliance &amp; Audit", "DL/APDL, eSPA-HIMS, e-invoice, PDPA, bumi and access control", compliance)

# ------------------------------------------------------------------ 7. AGENT DASHBOARD
agent = (
    '<div class="grid g4">'
    '<div class="kpi"><b>7</b><span>My active leads</span></div>'
    '<div class="kpi"><b>3</b><span>My unit locks</span></div>'
    '<div class="kpi"><b>2</b><span>Bookings in progress</span></div>'
    '<div class="kpi"><b>RM 20,400</b><span>Commission accrued</span></div></div>'

    '<h2>My pipeline</h2>' + table(["Buyer", "Source", "Stage", "Unit", "Next action", "Age"], [
        ["Ahmad bin Ali", "Facebook ad", pill("EOI", 'p-info'), "B-02-05", "Gallery appointment 16/09 11:00", "2 days"],
        ["Lee Mei Ling", "Agent referral", pill("Locked", 'p-warn'), "A-01-03", "Joint-buyer documents outstanding", "5 days"],
        ["Rajesh Kumar", "Google search", pill("Booked", 'p-ok'), "B-02-06", "Loan submission — 2 banks shortlisted", "9 days"],
        ["Nurul Huda", "Walk-in", pill("Eligibility check", 'p-grey'), "—", "DSR screening before appointment", "1 day"],
    ]) +

    '<h2>Tools an agent actually needs</h2>' + table(["Tool", "Why it matters"], [
        ["Real-time availability", "Agents stop promising units that are gone — the single biggest trust killer at launches"],
        ["Instant lock request", "Confirm a hold during the viewing, not after"],
        ["Affordability &amp; DSR checker", "Screen eligibility before spending a weekend on a dead lead"],
        ["Bank submission tracker", "See which lenders are holdups and chase the right party"],
        ["Document checklist", "Submit a complete booking pack the first time"],
        ["Commission ledger", "Know what is accrued, released and still held — with the trigger for each tranche"],
        ["Project brief &amp; price list version", "Always quote the current approved price, never an outdated PDF"],
    ]) +
    '<div class="note"><b>Market evidence:</b> in 1Q2026 Malaysian agencies reported agents gravitating to launches that are '
    '"easy to sell" — and to developers whose tools let them sell fastest. Tools are not back-office cost; they are the '
    'distribution channel.</div>'

    '<h2>Co-agency handling</h2>' + table(["Item", "Rule"], [
        ["Co-agency split", "Recorded before the lock is created; both parties see the same locked unit record"],
        ["Lead ownership", "First-touch agent keeps the lead for 90 days unless reassigned by the sales lead"],
        ["Disputes", "Resolved on the audit trail, not on memory — every lock, message and document carries a timestamp"],
        ["Payout", "Released on the same event schedule as direct agents, per co-agency agreement"],
    ])
)

page("agent.html", "F · Agent Dashboard", "What an agent sees: leads, locks, bookings and commission", agent)

# ------------------------------------------------------------------ 8. BRANDING (ZAFA)
branding = (
    '<div class="note"><b>Zahir\'s instruction (15 Sep 2026):</b> the system carries a different name — not “Mr Tanah”. '
    '<b>Admin = Mr Tanah</b> (internal operations, never shown to clients). '
    '<b>Clients see: “System provided by Zentra Property Group”.</b></div>'
    '<div class="tip"><b>NAME CONFIRMED 15/9/2026 → Zentra Property Group</b> (suite: <b>Zentra Sales Suite</b>). '
    'History: “ZAFA” was dropped the same day (an existing company used that name). The brand is held as a '
    '<b>configuration value</b> — every client surface, document, email and the domain plan re-brand from one setting; no code, schema or workflow changes. '
    'Screening results and mitigations: §4.</div>'

    '<h2>1. Two-layer branding architecture</h2>' +
    table(["Item", "CLIENT layer — ZAFA Property Group", "ADMIN layer — Mr Tanah (internal)"], [
        ["Name displayed", "<b>ZAFA Property Group</b> + “System provided by ZAFA Property Group”", "<b>Mr Tanah</b> (Zahir, Fadilah, MT agents)"],
        ["Portal", "Sign-in, buyer/agent dashboards, booking status, document downloads", "Unit lock board, commissions, compliance, audit, inventory control"],
        ["Email / WhatsApp", "Sender: ZAFA Property Group", "Internal operations notifications"],
        ["Client documents", "Booking letter, payment schedule, EOI confirmation — ZAFA header", "Internal files, worklists, MT commission reports"],
        ["Invoices / e-invoice", "<b>Registered legal name + TIN required</b> (currently ZMJ Solutions); trade name shown as “ZAFA Property Group”", "Accounting records"],
        ["Data controller", "Privacy notice must state the actual controlling entity (Mr Tanah / ZMJ Solutions)", "Internal audit log identifies the real operator"],
    ]) +
    '<div class="note"><b>Implementation:</b> one database, one codebase, branding as a configuration layer (logo, palette, name, '
    'domain, email identity, document templates). Two separate systems would double cost and split the audit trail. '
    'The internal audit log always names the real operator — required for PDPA and for any dispute.</div>'

    '<h2>2. Client-facing samples</h2>'
    '<div class="card" style="background:#0C4437;color:#fff">'
    '<div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px">'
    '<div><div style="font-size:19px;font-weight:800">ZAFA Property Group</div>'
    '<div style="font-size:12.5px;opacity:.85">Launch Sales &amp; Booking Platform — for buyers, agents and developers</div></div>'
    '<div style="text-align:right;font-size:12.5px;opacity:.9">Avalon @ Cybersouth<br>Phase 2 · 31 units available</div></div></div>'
    '<div class="grid g2">'
    '<div class="card"><h3>Footer sample</h3>'
    '<div style="border-top:1px solid #DCE5E0;padding-top:10px;font-size:12.5px;color:#5D6F69">'
    '<b style="color:#0C4437">ZAFA Property Group</b><br>System provided by ZAFA Property Group · v1.0<br>'
    'Personal data is processed under the PDPA 2010 (Act 709) · hello@zafapropertygroup.com</div></div>'
    '<div class="card"><h3>Client document sample</h3>'
    '<div style="border:1px solid #DCE5E0;border-radius:10px;padding:12px;font-size:13px">'
    '<b>ZAFA Property Group</b><br><span class="muted">Launch Booking Administration</span>'
    '<hr style="border:none;border-top:1px solid #DCE5E0">'
    'Interest confirmation (RM0)<br>Project: Avalon @ Cybersouth · Unit: A-02-05 (sample)<br>'
    'Buyer: ———— · Agent: ———— · Date: ————<br>'
    '<span class="muted" style="font-size:12px">This document is not a sale &amp; purchase agreement. '
    'The SPA is generated by the developer through KPKT HIMS.</span></div></div></div>'

    '<h2>3. Where the brand appears — and where the legal name must</h2>'
    '<div class="warn"><b>e-Invoice rule (LHDN):</b> the invoice must carry the <b>registered legal name and TIN</b> of the issuing '
    'entity. A trade name cannot substitute for it. Current instruction: issue under <b>ZMJ Solutions</b> and display '
    '“ZAFA Property Group” as the trade brand; the suite must support switching the issuing entity — including its TIN — '
    'when a new group company is registered.</div>'

    '<h2>4. Name &amp; domain screening — Zentra Property Group (15/9/2026)</h2>' +
    table(["Check", "Finding", "Verdict / action"], [
        ["zentrapropertygroup.com", "<b>Available</b> — USD 11.08/yr (exact-match .com)", pill("Register", 'p-ok')],
        ["zentrapropertygroup.my / .net / .asia", "<b>Available</b> — USD 2.37 (promo) / 12.52 / 11.84", pill("Register .my + .net defensive", 'p-ok')],
        ["zentra.com · zentra.my · zentragroup.com · zentraproperties.com · zentraproperty.com", "<b>All taken</b>", pill("Exact-match name is the only route", 'p-warn')],
        ["ZENTARA GROUP SDN. BHD. (SSM 1552884H)", "Exists in Malaysia — <b>one letter</b> from “Zentra” (pubs/bars sector)", pill("Highest risk — SSM name search first", 'p-bad')],
        ["Zentra Group plc (UK-listed)", "Residential developer &amp; property manager, “Zentra Group” + same sector", pill("Never use “Zentra Group” alone", 'p-warn')],
        ["Zentra Real Estate (California) · zentra.inc (proptech, Spain/Dubai)", "Agents/proptech use the name abroad", pill("Fine locally; avoid global-only “Zentra”", 'p-info')],
        ["Zentra Industries Sdn. Bhd. (MY, construction materials)", "Exists — construction sector", pill("Different sector; keep full name", 'p-info')],
        ["“ZENTRA” — Forest Heights, Seremban (Sunrise MCL Land)", "<b>An active Malaysian new-launch project brand</b> (shop offices)", pill("Buyer-search confusion in MY property", 'p-warn')],
        ["MyIPO trademark (Class 36 real estate)", "Not retrievable via public search here", pill("Verify before printing", 'p-warn')],
        ["SSM name availability (ezBiz/MyCoID)", "Not yet applied", pill("Check before incorporation", 'p-warn')],
    ]) +
    '<div class="warn"><b>Screening verdict:</b> the name is <b>usable</b> — the exact-match .com is free, which is the strongest asset — '
    'but three collisions must be managed: (1) <b>ZENTARA GROUP Sdn Bhd</b> (one-letter difference) can block or draw an objection at SSM; '
    '(2) <b>Zentra Group plc</b> is a listed UK residential property company, so never shorten the brand to “Zentra Group”; '
    '(3) “<b>Zentra</b>” is already a live Malaysian property project (Seremban), so always market as the full three words — '
    '<b>Zentra Property Group</b> — with the full name in titles, listings, OG tags and domain.</div>'
    '<div class="tip"><b>Mitigations to apply:</b> (a) run the SSM name search and a MyIPO Class 35/36 check before any printing or incorporation; '
    '(b) register zentrapropertygroup.com <b>and</b> .my, plus .net defensively; (c) lock the wordmark/typography so it cannot be confused with Zentara/Zentra Group plc; '
    '(d) keep the brand as a trade name under the registered entity until the new group company is incorporated — invoices always carry the registered name + TIN.</div>'

    '<h2>5. Branding compliance checklist</h2>' + table(["Item", "Requirement", "State"], [
        ["Trade name vs registered name", "Invoices, receipts and e-invoices must use the registered name and TIN", pill("Rule enforced", 'p-ok')],
        ["Estate agency licensing", "If the brand markets property to the public, it must sit under a registered estate agency firm (PEA) or act as a registered agent under the appointed agency (e.g. IQI Realty)", pill("To confirm", 'p-warn')],
        ["Advertising permit (Reg. 6)", "The authorised-agent name on the permit must match the party actually marketing the project", pill("To verify per project", 'p-warn')],
        ["PDPA privacy notice", "Must name the real data controller even where the brand differs", pill("Drafted", 'p-ok')],
        ["Client-facing separation", "No Mr Tanah name or links on client surfaces (except legally required documents)", pill("Design rule", 'p-ok')],
        ["Email deliverability", "Branded sending domain with SPF/DKIM before any client campaign", pill("Pending domain", 'p-info')],
    ]) +
    '<h2>6. New-name screening — ready to run</h2>'
    '<div class="note">Send any candidate name and this is screened end-to-end (target: under 5 minutes per name):</div>' +
    table(["Check", "How", "What makes it fail"], [
        ["Name collision (companies)", "Web search + SSM records for identical/near names", "Identical or confusingly similar registered name"],
        ["Domain availability", "Registrar lookup for .com / .my / .com.my / .net", "“.com” taken by an active same-sector site"],
        ["Existing web presence", "Search the exact name and its variants", "Same sector already holds the name"],
        ["Sector confusion", "Look for other property firms using the initials/cadence", "Buyers may mistake it for another agency"],
        ["Licensing fit", "Check whether the name implies an agency (needs PEA) or reads as a platform", "Implied licensing without registration"],
        ["Brand mechanics", "Pronounceability, spelling over the phone, length, logo/monogram options", "Hard to spell after hearing it once"],
    ]) +
    '<div class="tip"><b>Then, in one step:</b> the confirmed name is set once — every screen, document, email, footer and the domain plan re-brand automatically. Nothing else in the build changes.</div>'

    '<h2>7. Open decisions</h2><ol>'
    '<li><b>Register zentrapropertygroup.com</b> (+ .my, and .net defensively) — by card at the registrar checkout, or add account credit so the API can register it.</li>'
    '<li><b>Verify the name before printing:</b> SSM name search (against ZENTARA GROUP Sdn Bhd) and MyIPO Class 35/36 trademark check.</li>'
    '<li>Confirm the <b>issuing entity + TIN</b> for e-invoices now (ZMJ Solutions) and the migration path to the new group company.</li>'
    '<li>Confirm whether the brand will itself market property to the public (licensing implications) or remain a platform identity.</li>'
    '<li>Provide brand assets: wordmark, palette, typography, email addresses.</li>'
    '<li><b>Phase 1 go-ahead</b> — project register + microsite v3 + RM0 EOI + permit gate on the six existing projects.</li></ol>'
)

page("branding.html", "G · Branding — Zentra Property Group (client) vs Mr Tanah (admin)",
     "One system, two brand layers — clients see ZAFA; Mr Tanah operates the platform", branding)

# ------------------------------------------------------------------ 9. DESIGN & ROADMAP
design = (
    '<h2>1. Architecture — six layers</h2>'
    '<div class="card" style="font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12.5px;white-space:pre;overflow:auto">'
    'CLIENT SURFACES            AGENT SURFACES              ADMIN SURFACES\n'
    '─────────────────          ──────────────              ──────────────\n'
    'Project microsites    →    Agent dashboard        →    Sales board\n'
    'Zero-deposit EOI           Lock requests               Unit lock board\n'
    'Buyer portal               Commission ledger           Compliance gates\n'
    '        │                        │                            │\n'
    '        └────────────────────────┴──────────────┬─────────────┘\n'
    '                                                ▼\n'
    '                     APPLICATION  (ZAFA Sales Suite core)\n'
    '   Projects · Phases · Blocks · Units · Price lists · Parties\n'
    '   EOIs · Locks · Bookings · Loans · SPA tracking · Billing · Commission\n'
    '        │                │                 │                │\n'
    '        ▼                ▼                 ▼                ▼\n'
    '   DATA STORE      INTEGRATIONS       COMPLIANCE         AI & BI\n'
    '   (single source)  HIMS/eSPA,       DL/APDL gate,       Market data,\n'
    '                    e-invoice,        no-client-money,    forecasting,\n'
    '                    WhatsApp, email,  PDPA registry,      assistant on\n'
    '                    payments, banks   audit trail         project pages</div>'

    '<h2>2. Data model — 14 entities</h2>' +
    table(["Entity", "Key fields", "Notes"], [
        ["Project", "Name, developer, DL no., APDL no., PBT, tenure, bumi quota %, completion date, permit validity", "Permit gate lives here"],
        ["Phase", "Phase code, units released, launch date, permit reference", "Some phases are released later"],
        ["Block", "Block code, levels, units per level", "Drives booking forms and progressive billing references"],
        ["Unit", "Unit no., type, built-up, list price, bumi status, status, current lock, price-list version", "One row per saleable unit"],
        ["Price list", "Version, effective date, unit price, package/rebate treatment", "Versioned so old quotations can be audited"],
        ["Lead", "Name, contact, source, consent, owner agent, stage", "PDPA consent captured at entry"],
        ["EOI", "Queue position, priority class, unit preference, expiry", "Zero-deposit registration"],
        ["Lock", "Unit, holder, type (agent/agency/buffer), start, expiry, reason", "Prevents double selling"],
        ["Booking", "Booking ref, buyer, joint buyer, unit, price, developer acknowledgement", "Feeds HIMS/eSPA"],
        ["Buyer &amp; joint buyer", "Identity, contact, employment, income, TIN", "Shared with developer and lender only"],
        ["Loan application", "Lender, amount, margin, status, LOO, expiry, consent", "Consent record is mandatory"],
        ["SPA record", "eSPA/HIMS reference, signing status per party, stamping, dates", "HIMS is the source of truth"],
        ["Milestone bill", "Milestone, %, amount, certificate, invoice, e-invoice UUID, payment", "Third Schedule driven"],
        ["Commission", "Agent, split, accrual, release events, payout, self-billed e-invoice", "Event-based release"],
        ["Audit event", "Actor, action, subject, before/after, timestamp, source", "Immutable"],
    ]) +

    '<h2>3. Roles and access</h2>' +
    table(["Role", "Sees", "Can do"], [
        ["Admin (Mr Tanah)", "Everything", "Everything, including price lists and compliance overrides (logged)"],
        ["Sales lead", "All leads, units, agents", "Assign leads, approve locks, resolve disputes"],
        ["Agent", "Own leads, locks, bookings, commission", "Create EOIs, request locks, submit booking packs"],
        ["Co-agency agent", "Shared case records only", "Same as agent within the shared case"],
        ["Buyer (token link)", "Own case, documents, billing", "Upload documents, e-sign, view schedule"],
        ["Developer", "Unit status and bookings for their project", "Acknowledge bookings, upload certificates"],
        ["Lawyer", "Own conveyancing case", "Upload SPA/MOT documents, update milestones"],
        ["Banker / financier", "Own loan case", "Update submission status, upload LOU/LOO"],
    ]) +

    '<h2>4. Buy vs build</h2>' +
    table(["Option", "Fit for Mr Tanah", "Verdict"], [
        ["MHub (developer platform)", "Best-in-class for developers; assumes we own unit inventory and HIMS submission; pricing not published", "Use the developer\'s instance; integrate rather than duplicate"],
        ["PropertyX / IFCA (agency + developer)", "Closest functional match to an agency sales platform (202 mapped API operations); enterprise licensing, pricing not published", "Benchmark; consider only if a developer appoints us on it"],
        ["Agent CRM (listing platforms)", "Strong on listings and leads, weak on unit inventory, booking packs, milestone billing and commission events", "Not sufficient alone"],
        ["Build the agency layer on existing Mr Tanah assets", "Fits our role, our compliance stance and our existing portals; keeps data ownership; incremental cost per phase", "<b>Recommended</b>"],
    ]) +
    '<div class="note">Decision principle: the developer owns the unit and the SPA. Mr Tanah owns the <b>agency process</b> — '
    'leads, agents, holds, booking packs, financing follow-up, documentation quality and commission. Build exactly that, '
    'then integrate outward.</div>'

    '<h2>5. Risks and controls</h2>' +
    table(["Risk", "Control"], [
        ["Unit data inaccuracy (blocked SPA, angry buyer)", "Single source of truth + daily reconciliation with the developer/HIMS"],
        ["Double-selling a unit", "Mandatory locking with expiry and audit"],
        ["Collecting money before SPA (illegal)", "Payment fields disabled until an eSPA reference exists"],
        ["Permit lapse while marketing", "90-day expiry alerts, automatic unpublish on expiry"],
        ["Loan rejections (industry approval rate 41.2%)", "Eligibility screening before appointment; multi-lender tracking"],
        ["Commission disputes", "Event-based release tied to evidence, not opinion"],
        ["PDPA breach", "Consent registry, access control, 72-hour breach playbook, DPO"],
        ["Agent adoption", "Agent-first tools: instant availability, one-tap locks, commission visibility"],
    ]) +

    '<h2>6. Next decisions for Zahir</h2><ol>'
    '<li><b>Scope</b> — agree the suite is the agency layer, not a replacement for the developer system.</li>'
    '<li><b>Booking model</b> — zero-deposit EOI/option only (recommended) or something else.</li>'
    '<li><b>Phase 1 start</b> — approve F1 (project register + microsite v3 + RM0 EOI + permit gate) for the six existing projects.</li>'
    '<li><b>Commission release schedule</b> — 10 / 25 / 25 / 40 (recommended) or gated on developer payment.</li>'
    '<li><b>Data request to developers</b> — unit schedules, DL and APDL copies, price lists per phase.</li>'
    '<li><b>Branding</b> — register the domain and provide brand assets; run the SSM + MyIPO checks (see screen G).</li>'
    '<li><b>PDPA</b> — appoint a DPO and confirm the privacy notice wording for both brand layers.</li></ol>'
)

page("design.html", "Design &amp; Roadmap", "Architecture, data model, roles, buy-vs-build, risks and open decisions", design)

# ------------------------------------------------------------------ redirect stubs (old paths)
def stub(dirpath, target, label):
    os.makedirs(dirpath, exist_ok=True)
    open(os.path.join(dirpath, "index.html"), 'w', encoding='utf-8').write(
        '<!doctype html><html lang="en-US"><head><meta charset="utf-8">'
        '<meta name="robots" content="noindex,nofollow">'
        '<meta http-equiv="refresh" content="0;url=%s">' % target +
        '<title>Moved — %s</title></head><body style="font-family:system-ui;padding:40px">' % label +
        '<p>This preview has moved.</p>'
        '<p><a href="%s">Continue →</a></p></body></html>' % target)

stub("/home/ubuntu/mockup-hartanah/sjpb-poc", "../zentra-launch-poc/index.html", "Zentra Launch preview")
stub("/home/ubuntu/mockup-hartanah/zafa-sales-suite", "../zentra-launch-poc/index.html", "Zentra Launch preview")

open(os.path.join(OUT, "suite.css"), 'w', encoding='utf-8').write(CSS)
print("Done:", sorted(os.listdir(OUT)))
