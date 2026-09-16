# _f0_a.py — Zentra Law F0: overview, matters, matter detail, checklist
# Gaya selamat: semua HTML ialah string biasa; nilai disuntik melalui token @@KEY@@ (fungsi T()).
from datetime import date
import re
from _f0_common import *

HERE = date(2026, 9, 17)

MATTERS = [
    dict(id="CV-2026-0142", type="Subsale purchase", client="Nurul Ain binti Hassan",
         other="Tan Wei Ming", lawyer="A. Rahman", bank="CIMB Bank", price=650000, loan=520000,
         prop="Geran 45678, Lot 1234, Mukim Kajang, Daerah Hulu Langat, Selangor",
         stage="Loan documents / stamping", pct=82, risk="warn"),
    dict(id="CV-2026-0138", type="Subsale sale (with redemption)", client="Tan Wei Ming",
         other="Nurul Ain binti Hassan", lawyer="S. Leong", bank="Maybank Islamic", price=650000, loan=0,
         prop="Same property, seller side &mdash; discharge of charge pending",
         stage="Redemption &amp; completion", pct=64, risk="warn"),
    dict(id="CV-2026-0151", type="End-financing (bank panel)", client="Muhammad Haziq bin Omar",
         other="Public Bank Berhad", lawyer="A. Rahman", bank="Public Bank", price=430000, loan=360000,
         prop="Parcel 12-08, Block C, Residensi Aman, Cheras, Kuala Lumpur",
         stage="Facility agreement / stamping", pct=71, risk="ok"),
    dict(id="CV-2026-0155", type="Developer sale (Schedule H)", client="Chong Li Fen",
         other="Aman Setia Development Sdn Bhd", lawyer="S. Leong", bank="Hong Leong Bank",
         price=498000, loan=420000, prop="Unit B-19-03, Aman Setia Residences, Sepang, Selangor",
         stage="Progressive billing &mdash; 10% on SPA", pct=35, risk="ok"),
    dict(id="CV-2026-0160", type="Tenancy agreement", client="Bright Path Academy Sdn Bhd",
         other="Landlord: Koperasi Seri Mutiara Berhad", lawyer="N. Farah", price=0, loan=0,
         prop="Level 3, Wisma Mutiara, Bandar Baru Bangi (2 years, RM6,800 per month)",
         stage="E-signature", pct=90, risk="ok"),
    dict(id="CV-2026-0162", type="Transfer by love and affection", client="Ismail bin Yusof",
         other="Ahmad bin Ismail (son)", lawyer="N. Farah", price=0, loan=0,
         prop="GM 1122, Lot 4477, Mukim Jeram, Kuala Selangor &mdash; leasehold, 99 years",
         stage="State Authority consent", pct=48, risk="warn"),
]

FEE_PUR = sro_scale(650000)
FEE_LOAN = sro_scale(520000)
DUTY_MOT = stamp_duty_mot(650000)
DUTY_LOAN = stamp_duty_loan(520000)
SST = (FEE_PUR + FEE_LOAN) * 0.08
SUB_INST = subsidiary_instrument(FEE_PUR)
DISC = money(1937.50)

V = {
    "FEE_PUR": money(FEE_PUR), "FEE_LOAN": money(FEE_LOAN), "SST": money(SST),
    "DUTY_MOT": money(DUTY_MOT), "DUTY_LOAN": money(DUTY_LOAN), "SUB_INST": money(SUB_INST),
    "TOTAL_PROF": money(FEE_PUR + FEE_LOAN + SST),
    "TOTAL_EST": money(FEE_PUR + FEE_LOAN + SST + DUTY_MOT + DUTY_LOAN + 1180),
    "PRICE": money(650000, 0), "LOAN": money(520000, 0), "DISC": DISC,
    "DAYS_COMPLETE": str(days_left(date(2026, 12, 11))),
    "DAYS_STAMP": str(days_left(date(2026, 9, 22))),
    "BAL_CLIENT": money(128450, 0), "UNBILLED": money(41530, 0),
}

def T(s):
    return re.sub(r"@@(\w+)@@", lambda m: V.get(m.group(1), m.group(0)), s)

def rows_matters():
    out = []
    for m in MATTERS:
        cls = "amber" if m["risk"] == "warn" else "ok"
        out.append('<tr data-k="' + m["type"].split()[0].lower() + '">'
                   '<td><a href="matter.html?m=' + m["id"] + '"><b>' + m["id"] + '</b></a></td>'
                   '<td>' + m["type"] + '</td><td>' + m["client"] + '</td><td>' + m["other"] + '</td>'
                   '<td>' + m["lawyer"] + '</td><td><span class="pill ' + cls + '">' + m["stage"] + '</span></td>'
                   '<td class="num">' + str(m["pct"]) + '%</td></tr>')
    return "\n".join(out)

PAGES_A = []

# ---------------------------------------------------------------- 1. overview
PAGES_A.append(dict(f="index.html", t="Overview", body=T("".join([
"""@@TOP@@""",
"""    <div class="note warn"><b>What this prototype is.</b> A clickable mock-up with sample data, so the flows can be tested before any production code is written. Start with <a href="guide.html">the review guide</a>, then walk the menu from top to bottom. Everything here is English (US), the same visual theme as Zentra Hub.</div>
""",
"""    <h2 class="sec"><span class="num">1</span> Firm at a glance</h2>
    <div class="grid g4">
      <a class="kpi link" href="matters.html"><div class="lab">Active matters</div><div class="val">16</div><div class="sub"><span class="up">+4</span> opened this month</div></a>
      <a class="kpi link warn" href="deadlines.html"><div class="lab">Statutory deadlines &le; 14 days</div><div class="val">3</div><div class="sub">stamping, completion, consent</div></a>
      <a class="kpi link blue" href="client-account.html"><div class="lab">Client account balance</div><div class="val">@@BAL_CLIENT@@</div><div class="sub">held for 6 matters &middot; reconciled 31 Aug 2026</div></a>
      <a class="kpi link" href="billing.html"><div class="lab">Invoices &amp; drafts</div><div class="val">@@UNBILLED@@</div><div class="sub">3 payable &middot; 2 drafts</div></a>
    </div>
""",
"""    <h2 class="sec"><span class="num">2</span> The board &mdash; conveyancing matters in flight</h2>
    <div class="card">
      <div class="chips">
        <span class="chip on">All practice areas</span><span class="chip">Subsale</span><span class="chip">Financing</span>
        <span class="chip">Developer</span><span class="chip">Tenancy</span><span class="chip">Consent / estate</span>
      </div>
      <div class="wrap-tbl">
        <table class="tbl">
          <tr><th>Matter</th><th>Type</th><th>Client</th><th>Counterparty / bank</th><th>Lawyer</th><th>Stage</th><th class="num">Progress</th></tr>
@@MATTER_ROWS@@
        </table>
      </div>
      <p class="small muted" style="margin-bottom:0"><a href="matters.html">Open the full matter list</a> &mdash; filter by stage, lawyer or deadline.</p>
    </div>
""",
"""    <h2 class="sec"><span class="num">3</span> What this system manages</h2>
    <div class="grid g3">
      <a class="card link" href="matters.html"><h3 style="margin-top:0">Matters &amp; parties</h3><p class="small muted" style="margin-bottom:0">Intake, conflict check, engagement letter, parties, property, instruments, the bank or developer chain.</p></a>
      <a class="card link" href="checklist.html"><h3 style="margin-top:0">Document checklist</h3><p class="small muted" style="margin-bottom:0">Every document a matter needs, who owes it, what blocks signing &mdash; and what may never be signed electronically.</p></a>
      <a class="card link" href="documents.html"><h3 style="margin-top:0">Documents &amp; signing</h3><p class="small muted" style="margin-bottom:0">Generate from templates, then sign the compliant way: e-signature where allowed, wet-ink where the law insists.</p></a>
      <a class="card link" href="deadlines.html"><h3 style="margin-top:0">Statutory clock</h3><p class="small muted" style="margin-bottom:0">3+1 months to completion, late-payment interest, 30-day stamping, 60-day CKHT, state consent windows.</p></a>
      <a class="card link" href="fees.html"><h3 style="margin-top:0">Fees you cannot under-charge</h3><p class="small muted" style="margin-bottom:0">Scale fees under the Solicitors' Remuneration Order 2023, the 25% discount ceiling, and the waiver rules that are not discounts.</p></a>
      <a class="card link" href="client-account.html"><h3 style="margin-top:0">Client account</h3><p class="small muted" style="margin-bottom:0">Receipts, payments, a ledger per client, and the reconciliation pack the firm's accountant signs.</p></a>
      <a class="card link" href="billing.html"><h3 style="margin-top:0">Billing</h3><p class="small muted" style="margin-bottom:0">Scale fee, disbursements, SST and LHDN e-invoice status on one bill.</p></a>
      <a class="card link" href="portal.html"><h3 style="margin-top:0">Client portal</h3><p class="small muted" style="margin-bottom:0">What the client sees: where the file is, what to sign, what to pay.</p></a>
      <a class="card link" href="admin.html"><h3 style="margin-top:0">Firm admin</h3><p class="small muted" style="margin-bottom:0">Users and roles, MFA, subscription, data residency, and the AI switch.</p></a>
      <a class="card link" href="compliance.html"><h3 style="margin-top:0">Compliance guard</h3><p class="small muted" style="margin-bottom:0">No referral payments, discount and waiver log, publicity approvals, AMLA checks, rate versions.</p></a>
      <a class="card link" href="audit.html"><h3 style="margin-top:0">Audit trail</h3><p class="small muted" style="margin-bottom:0">An append-only record of who did what, sealed in a hash chain.</p></a>
      <a class="card link" href="roadmap.html"><h3 style="margin-top:0">Roadmap</h3><p class="small muted" style="margin-bottom:0">How conveyancing-first becomes five practice areas without five systems.</p></a>
    </div>
""",
"""    <h2 class="sec"><span class="num">4</span> Two rules this product obeys</h2>
    <div class="grid g2">
      <div class="card"><h3 style="margin-top:0">1. The money is never ours</h3>
        <p class="small muted">Zentra Law is software. Client money stays in the firm's own client account at the firm's own bank; the system records it, reconciles it and prints the accountant's pack. Subscription fees sit in a separate ledger and a separate bank account &mdash; never mixed.</p>
        <p class="small muted" style="margin-bottom:0"><a href="client-account.html">See the client account screen &rarr;</a></p></div>
      <div class="card"><h3 style="margin-top:0">2. No referral money, anywhere</h3>
        <p class="small muted">Bar Council Ruling 14.23 bars a lawyer from paying anyone to introduce clients. So there is no referral-fee field, no agent commission and no finder's payout in this system &mdash; only a referral <i>source</i> note that carries <b>RM0.00</b>.</p>
        <p class="small muted" style="margin-bottom:0"><a href="compliance.html">See the compliance guard &rarr;</a></p></div>
    </div>
""",
"""    <p class="foot-note">Zentra Law prototype &middot; Zentra Property Group &middot; English (US) UI &middot; sample data only<br>No real client, file or money is represented here. Compliance notes are design intent and remain subject to legal review.</p>
"""]))))

# ---------------------------------------------------------------- 2. matters
PAGES_A.append(dict(f="matters.html", t="Matters", body=T("".join([
"""@@TOP@@""",
"""    <h2 class="sec"><span class="num">1</span> All matters</h2>
    <div class="card">
      <div class="chips" id="mFilter">
        <span class="chip on" data-k="all">All (16)</span>
        <span class="chip" data-k="subsale">Subsale</span>
        <span class="chip" data-k="end-financing">Financing</span>
        <span class="chip" data-k="developer">Developer</span>
        <span class="chip" data-k="tenancy">Tenancy</span>
        <span class="chip" data-k="transfer">Consent / estate</span>
      </div>
      <div class="field" style="max-width:420px;margin:12px 0">
        <input class="btn ghost" style="width:100%;text-align:left" placeholder="Search file number, client, property or bank" id="mSearch">
      </div>
      <div class="wrap-tbl">
        <table class="tbl" id="mTable">
          <tr><th>Matter</th><th>Type</th><th>Client</th><th>Counterparty / bank</th><th>Lawyer</th><th>Stage</th><th class="num">Progress</th></tr>
@@MATTER_ROWS@@
          <tr><td colspan="7" class="muted small">+ 10 more matters &mdash; sample data only; the six above are wired into this prototype</td></tr>
        </table>
      </div>
      <p class="small muted" style="margin-bottom:0">Prototype note: filters and search work on the rows shown. In production this list is server-side, paginated and permission-scoped &mdash; a lawyer sees their own matters unless granted wider access.</p>
    </div>
""",
"""    <h2 class="sec"><span class="num">2</span> How a matter is opened</h2>
    <div class="card">
      <div class="steps">
        <div class="step done"><span>1</span><div><b>Intake</b><div class="small muted">Client, parties, property, source of instruction, conflict check.</div></div></div>
        <div class="step done"><span>2</span><div><b>Engagement &amp; costs</b><div class="small muted">Engagement letter, scale-fee estimate, disbursement estimate, SST &mdash; client acknowledges.</div></div></div>
        <div class="step active"><span>3</span><div><b>Documents &amp; signing</b><div class="small muted">The checklist engine drives what must be collected, drafted and signed, and by which method.</div></div></div>
        <div class="step"><span>4</span><div><b>Completion</b><div class="small muted">Redemption, release of the balance, vacant possession, discharge of undertakings.</div></div></div>
        <div class="step"><span>5</span><div><b>Post-completion</b><div class="small muted">Stamping, registration, CKHT retention, final bill and file closure.</div></div></div>
      </div>
      <div class="note warn">Steps cannot be skipped silently. Each gate records who passed it, when, and on what evidence &mdash; the same discipline the audit trail shows later.</div>
    </div>
""",
"""    <p class="foot-note">Zentra Law prototype &middot; Zentra Property Group &middot; English (US) UI &middot; sample data only<br>Matter list. No real client, file or money is represented here.</p>
"""]))))

# ---------------------------------------------------------------- 3. matter detail
PAGES_A.append(dict(f="matter.html", t="Matter detail", body=T("".join([
"""@@TOP@@""",
"""    <h2 class="sec"><span class="num">1</span> The file in one screen</h2>
    <div class="grid g4">
      <div class="kpi"><div class="lab">Purchase price</div><div class="val">@@PRICE@@</div><div class="sub">MOT duty @@DUTY_MOT@@ &middot; loan @@LOAN@@</div></div>
      <div class="kpi warn"><div class="lab">Completion in</div><div class="val">@@DAYS_COMPLETE@@ days</div><div class="sub">11 Dec 2026 &middot; SPA 3+1 months</div></div>
      <div class="kpi blue"><div class="lab">Stamping in</div><div class="val">@@DAYS_STAMP@@ days</div><div class="sub">22 Sep 2026 &middot; 30-day rule</div></div>
      <div class="kpi"><div class="lab">Progress</div><div class="val">82%</div><div class="sub">gate 3 of 5 active</div></div>
    </div>
""",
"""    <h2 class="sec"><span class="num">2</span> Parties and property</h2>
    <div class="grid g2">
      <div class="card">
        <h3 style="margin-top:0">Parties</h3>
        <table class="tbl">
          <tr><th>Role</th><th>Name</th><th>Identification</th><th>Contact</th></tr>
          <tr><td>Client (buyer) <span class="pill blue">client</span></td><td>Nurul Ain binti Hassan</td><td>IC masked</td><td>sample@email.com</td></tr>
          <tr><td>Seller</td><td>Tan Wei Ming</td><td>IC masked</td><td>via solicitors</td></tr>
          <tr><td>Financier</td><td>CIMB Bank Berhad</td><td>Panel firm ref 7712</td><td>panel portal</td></tr>
          <tr><td>Referral source <span class="pill gray">no payment</span></td><td>Walk-in enquiry (counter)</td><td>&mdash;</td><td>RM0.00 &mdash; see the guard</td></tr>
        </table>
        <p class="small muted">Conflict check ran 12 Aug 2026, 09:14 &mdash; no adverse party match in the firm's records or among the parties of any open matter.</p>
        <p class="small muted" style="margin-bottom:0">AMLA customer due diligence: identification collected, source of funds declared, record filed with the matter.</p>
      </div>
      <div class="card">
        <h3 style="margin-top:0">Property and instruments</h3>
        <table class="tbl">
          <tr><th>Item</th><th>Detail</th></tr>
          <tr><td>Title</td><td>Geran 45678, Lot 1234, Mukim Kajang, Daerah Hulu Langat, Selangor</td></tr>
          <tr><td>Tenure</td><td>Freehold &middot; individual title &middot; Bumi lot: no</td></tr>
          <tr><td>Encumbrances</td><td>Charge in favour of Maybank Islamic &mdash; to be discharged</td></tr>
          <tr><td>Principal instrument</td><td>Sale and purchase agreement (subsale) &mdash; <span class="pill amber">wet-ink</span></td></tr>
          <tr><td>Transfer</td><td>Memorandum of Transfer (Form 14A) &mdash; <span class="pill bad">wet-ink only</span></td></tr>
          <tr><td>Financing</td><td>Charge (Form 16A) &mdash; <span class="pill bad">wet-ink only</span></td></tr>
          <tr><td>Subsidiary instrument</td><td>Discharge of charge &mdash; fee @@SUB_INST@@ (10% of scale, min RM500, max RM2,000)</td></tr>
        </table>
      </div>
    </div>
""",
"""    <h2 class="sec"><span class="num">3</span> Money on this file</h2>
    <div class="card">
      <table class="tbl">
        <tr><th>Line</th><th>Basis</th><th class="num">Amount</th></tr>
        <tr><td>Professional fee &mdash; sale and purchase</td><td>SRO 2023, First Schedule Table A, scale fee</td><td class="num">@@FEE_PUR@@</td></tr>
        <tr><td>Professional fee &mdash; financing documents</td><td>SRO 2023, Third Schedule, scale fee</td><td class="num">@@FEE_LOAN@@</td></tr>
        <tr><td>SST</td><td>8% on professional fees</td><td class="num">@@SST@@</td></tr>
        <tr class="total"><td>Professional fees plus SST</td><td>&mdash;</td><td class="num">@@TOTAL_PROF@@</td></tr>
        <tr><td>Stamp duty &mdash; MOT</td><td>1% / 2% / 3% bands on @@PRICE@@</td><td class="num">@@DUTY_MOT@@</td></tr>
        <tr><td>Stamp duty &mdash; loan agreement</td><td>0.5% of @@LOAN@@</td><td class="num">@@DUTY_LOAN@@</td></tr>
        <tr><td>Disbursements</td><td>Land search, registration, bankruptcy search, travel</td><td class="num">RM1,180.00</td></tr>
        <tr class="total"><td>Total estimate issued to the client</td><td>Engagement letter dated 12 Aug 2026</td><td class="num">@@TOTAL_EST@@</td></tr>
      </table>
      <p class="small muted" style="margin-bottom:0">Every number carries the rate version that produced it, so a bill reprinted in 2027 still shows the 2026 basis. <a href="fees.html">Open the fee engine &rarr;</a></p>
    </div>
""",
"""    <h2 class="sec"><span class="num">4</span> This week on the file</h2>
    <div class="grid g2">
      <div class="card"><h3 style="margin-top:0">Tasks</h3>
        <ul class="check">
          <li><span class="ok">&#10003;</span><div><b>Signed SPA collected</b> &mdash; all parties, 2 witnesses <span class="small muted">14 Aug 2026</span></div></li>
          <li><span class="ok">&#10003;</span><div><b>Land search</b> &mdash; private search, 3 lots <span class="small muted">19 Aug 2026</span></div></li>
          <li><span class="ok">&#10003;</span><div><b>Loan documents from CIMB</b> received and checked <span class="small muted">08 Sep 2026</span></div></li>
          <li><span class="ok">&#10003;</span><div><b>Redemption statement requested</b> from Maybank Islamic <span class="small muted">10 Sep 2026</span></div></li>
          <li><span>2</span><div><b>Stamp the MOT and loan agreement</b> &mdash; due 22 Sep 2026</div></li>
          <li><span>3</span><div><b>Release the 90% balance</b> against completion documents <span class="pill amber">gate</span></div></li>
          <li><span>4</span><div><b>CKHT retention</b> &mdash; seller side retained, CKHT1 within 60 days</div></li>
        </ul>
      </div>
      <div class="card"><h3 style="margin-top:0">Documents on the file</h3>
        <div class="chips">
          <span class="chip-doc ok">SPA &mdash; signed, wet-ink</span>
          <span class="chip-doc ok">Engagement letter &mdash; e-signed</span>
          <span class="chip-doc ok">Loan offer &mdash; bank, wet-ink</span>
          <span class="chip-doc">Facility agreement &mdash; awaiting bank</span>
          <span class="chip-doc">Memorandum of Transfer &mdash; draft</span>
          <span class="chip-doc">Charge &mdash; draft</span>
          <span class="chip-doc">Discharge of charge &mdash; awaiting bank</span>
          <span class="chip-doc">CKHT1 &mdash; seller</span>
        </div>
        <div class="hr"></div>
        <p class="small muted" style="margin:0">Anything that must be signed in wet ink carries a warning label on purpose &mdash; see <a href="documents.html">documents &amp; signing</a>.</p>
      </div>
    </div>
""",
"""    <p class="foot-note">Zentra Law prototype &middot; Zentra Property Group &middot; English (US) UI &middot; sample data only<br>Matter detail. No real client, file or money is represented here.</p>
"""]))))

# ---------------------------------------------------------------- 4. checklist
CHECK = [
    ("Client and identity", [
        ("Client identification &mdash; IC copy, front and back", "Client", "done", "AMLA customer due diligence record"),
        ("Signed letter of engagement and costs estimate", "Client", "done", "E-signature allowed"),
        ("PDPA consent notice acknowledged", "Client", "done", "E-signature allowed"),
        ("Source of funds declaration", "Client", "due", "AMLA &mdash; kept with the CDD record"),
    ]),
    ("Property and title", [
        ("Land search (private search) result", "Firm", "done", "Checks encumbrances and restrictions"),
        ("Copy of title or strata roll", "Firm", "done", "Title particulars go on the SPA"),
        ("Quit rent and assessment receipts, current year", "Seller", "done", "Completion condition"),
        ("State authority consent application, if leasehold", "Firm", "progress", "Creates its own clock &mdash; see deadlines"),
        ("Discharge of charge or redemption statement", "Seller's bank", "progress", "Needed before completion"),
    ]),
    ("Agreement and instruments", [
        ("Sale and purchase agreement &mdash; 4 copies", "Firm", "done", "Wet-ink, with attesting witnesses"),
        ("Memorandum of Transfer (Form 14A)", "Firm", "progress", "Wet-ink only &mdash; land office presentation"),
        ("Charge or Deed of Assignment (Form 16A)", "Bank / firm", "progress", "Wet-ink only"),
        ("Bank letter of offer or facility agreement", "Bank", "progress", "The bank's own signing requirement applies"),
        ("Statutory declaration, if required", "Parties", "due", "Wet-ink and attestation"),
    ]),
    ("Completion and post-completion", [
        ("Completion account &mdash; balance, apportionments, interest", "Firm", "due", "The 3+1 month clock"),
        ("Stamping of the MOT and loan agreement", "Firm", "due", "30 days from execution &mdash; automatic reminder"),
        ("Presentation and registration at the land office", "Firm", "wait", "After stamping"),
        ("CKHT1 and CKHT2 filings, seller side", "Firm", "due", "60 days from disposal"),
        ("Final bill, client account statement, file closure", "Firm", "wait", "Retention, then the disposal schedule"),
    ]),
]
PILL = {"done": '<span class="pill ok">received</span>', "progress": '<span class="pill blue">in progress</span>',
        "due": '<span class="pill amber">outstanding</span>', "wait": '<span class="pill gray">blocked</span>'}

def rows_checklist():
    out = []
    for grp, items in CHECK:
        out.append('<h3 style="margin-top:18px">' + grp + '</h3>')
        out.append('<div class="wrap-tbl"><table class="tbl">')
        out.append('<tr><th style="width:44%">Document</th><th>Owner</th><th>Status</th><th>Why it matters</th><th></th></tr>')
        for name, owner, st, why in items:
            out.append('<tr><td>' + name + '</td><td class="small">' + owner + '</td><td>' + PILL[st] +
                       '</td><td class="small muted">' + why + '</td><td class="small"><a href="#">upload</a></td></tr>')
        out.append('</table></div>')
    return "\n".join(out)

PAGES_A.append(dict(f="checklist.html", t="Document checklist", body=T("".join([
"""@@TOP@@""",
"""    <div class="grid g4">
      <div class="kpi"><div class="lab">Items</div><div class="val">18</div><div class="sub">4 groups</div></div>
      <div class="kpi"><div class="lab">Received</div><div class="val">8</div><div class="sub">evidence attached</div></div>
      <div class="kpi warn"><div class="lab">Outstanding</div><div class="val">6</div><div class="sub">2 need wet-ink signing</div></div>
      <div class="kpi"><div class="lab">Blocked</div><div class="val">4</div><div class="sub">waiting on bank or land office</div></div>
    </div>
""",
"""    <h2 class="sec"><span class="num">1</span> Checklist for CV-2026-0142</h2>
    <div class="card">
      <div class="chips">
        <span class="chip on">Subsale purchase (this file)</span>
        <span class="chip">Subsale sale</span><span class="chip">Financing only</span>
        <span class="chip">Developer, Schedule H</span><span class="chip">Tenancy</span><span class="chip">Transfer by love and affection</span>
      </div>
      <p class="small muted" style="margin:10px 0 0">Switch template and the checklist re-forms with the right items for that matter type. Templates are versioned, so a file opened in 2026 keeps the 2026 list even after the firm updates the template.</p>
@@CHECKLIST_ROWS@@
      <div class="hr"></div>
      <div class="note warn"><b>Method lock.</b> Two items on this list can never be completed by e-signature &mdash; the Memorandum of Transfer and the Charge. If a clerk tries, the system refuses and records the attempt instead of warning quietly. <a href="documents.html">See the signing matrix &rarr;</a></div>
    </div>
""",
"""    <p class="foot-note">Zentra Law prototype &middot; Zentra Property Group &middot; English (US) UI &middot; sample data only<br>Document checklist. No real client, file or money is represented here.</p>
"""]))))
