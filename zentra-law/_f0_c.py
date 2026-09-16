# _f0_c.py — Zentra Law F0: billing, client account, portal, admin, compliance, audit, roadmap, guide
from _f0_common import *
from _f0_a import T, V

PAGES_C = []

PAGES_C.append(dict(f="billing.html", t="Billing", body=T("".join([
"""@@TOP@@""",
"""    <div class="grid g4">
      <div class="kpi"><div class="lab">Invoiced this month</div><div class="val">RM186,400</div><div class="sub">31 bills</div></div>
      <div class="kpi warn"><div class="lab">Overdue</div><div class="val">RM12,760</div><div class="sub">4 clients &middot; oldest 41 days</div></div>
      <div class="kpi blue"><div class="lab">E-invoice accepted</div><div class="val">27 / 31</div><div class="sub">4 awaiting validation</div></div>
      <div class="kpi"><div class="lab">Disbursements to recover</div><div class="val">RM9,340</div><div class="sub">paid from client account</div></div>
    </div>
""",
"""    <h2 class="sec"><span class="num">1</span> Bill for CV-2026-0142</h2>
    <div class="card">
      <table class="tbl">
        <tr><th>Item</th><th>Basis</th><th class="num">Amount</th></tr>
        <tr><td>Professional fee &mdash; sale and purchase</td><td>Scale, less 25% discount</td><td class="num">@@FEE_PUR@@</td></tr>
        <tr><td>Discount granted</td><td>Within the order's ceiling</td><td class="num">-@@DISC@@</td></tr>
        <tr><td>Professional fee &mdash; financing documents</td><td>Third Schedule scale</td><td class="num">@@FEE_LOAN@@</td></tr>
        <tr><td>SST at 8%</td><td>On professional fees after discount</td><td class="num">@@SST@@</td></tr>
        <tr><td>Disbursements</td><td>Stamp duty, searches, registration, travel</td><td class="num">RM17,280.00</td></tr>
        <tr class="total"><td>Total due</td><td>&mdash;</td><td class="num">RM32,436.10</td></tr>
      </table>
      <div class="hr"></div>
      <div class="grid g3">
        <div><div class="small muted">E-invoice status</div><div><span class="pill ok">validated by LHDN</span></div><div class="small muted">UUID and validation date stored with the bill</div></div>
        <div><div class="small muted">Payment</div><div><span class="pill amber">part paid</span></div><div class="small muted">Received 12 Sep 2026 &mdash; RM20,000.00 into client account</div></div>
        <div><div class="small muted">Statement</div><div><a href="#">Statement of account</a></div><div class="small muted">Sent to the client portal automatically</div></div>
      </div>
    </div>
""",
"""    <h2 class="sec"><span class="num">2</span> Two kinds of money, never one ledger</h2>
    <div class="grid g2">
      <div class="card"><h3 style="margin-top:0">Client money</h3>
        <p class="small muted">Deposits, balance of purchase price, stamping and registration money, and any money held for a third party. It sits in the firm's client account at the firm's bank and may only be paid out for the purpose for which it was received.</p>
        <p class="small muted" style="margin-bottom:0"><a href="client-account.html">Client account screen &rarr;</a></p></div>
      <div class="card"><h3 style="margin-top:0">The firm's own money</h3>
        <p class="small muted">Fees earned, and the firm's operating expenses. The system keeps the two apart at the database level, not just on the screen, and month-end reconciliation proves they never touched.</p>
        <p class="small muted" style="margin-bottom:0"><a href="audit.html">Audit trail &rarr;</a></p></div>
    </div>
    <p class="foot-note">Zentra Law prototype &middot; Zentra Property Group &middot; English (US) UI &middot; sample data only<br>Billing. Amounts illustrative.</p>
"""]))))

PAGES_C.append(dict(f="client-account.html", t="Client account", body=T("".join([
"""@@TOP@@""",
"""    <div class="note warn"><b>This screen records money; it never holds it.</b> Client funds stay in the firm's own client account at the firm's own bank. Zentra Law keeps the ledger, prints the reconciliation, and produces the pack the firm's accountant signs &mdash; and nothing else. Subscription fees are collected through a separate account and never appear in this ledger.</div>
""",
"""    <h2 class="sec"><span class="num">1</span> Ledger for one client</h2>
    <div class="card">
      <div class="grid g3" style="margin-bottom:14px">
        <div><div class="small muted">Client</div><div><b>Nurul Ain binti Hassan</b></div></div>
        <div><div class="small muted">Matter</div><div>CV-2026-0142</div></div>
        <div><div class="small muted">Balance held</div><div><b>RM45,800.00</b> <span class="pill ok">reconciled</span></div></div>
      </div>
      <div class="wrap-tbl">
        <table class="tbl">
          <tr><th>Date</th><th>Reference</th><th>Description</th><th class="num">In (RM)</th><th class="num">Out (RM)</th><th class="num">Balance (RM)</th></tr>
          <tr><td>12 Aug 2026</td><td>R-0091</td><td>Deposit 10% of purchase price received from client</td><td class="num">65,000.00</td><td class="num">&mdash;</td><td class="num">65,000.00</td></tr>
          <tr><td>14 Aug 2026</td><td>P-0233</td><td>Stakeholder deposit released to seller's solicitors as stakeholder on exchange</td><td class="num">&mdash;</td><td class="num">65,000.00</td><td class="num">0.00</td></tr>
          <tr><td>02 Sep 2026</td><td>R-0144</td><td>Stamping money and registration fees advanced by client</td><td class="num">18,300.00</td><td class="num">&mdash;</td><td class="num">18,300.00</td></tr>
          <tr><td>05 Sep 2026</td><td>P-0261</td><td>Land search and bankruptcy search fees</td><td class="num">&mdash;</td><td class="num">420.00</td><td class="num">17,880.00</td></tr>
          <tr><td>12 Sep 2026</td><td>R-0160</td><td>Payment on account of fees</td><td class="num">20,000.00</td><td class="num">&mdash;</td><td class="num">37,880.00</td></tr>
          <tr><td>16 Sep 2026</td><td>P-0274</td><td>Transfer to office account for fees earned, per approved bill</td><td class="num">&mdash;</td><td class="num">7,920.00</td><td class="num">45,800.00</td></tr>
        </table>
      </div>
      <p class="small muted" style="margin-bottom:0">Every payout carries the reason, the approving lawyer and the bill it settles. A payout without an approver cannot be posted &mdash; the screen refuses it.</p>
    </div>
""",
"""    <h2 class="sec"><span class="num">2</span> Month-end and the accountant's pack</h2>
    <div class="grid g3">
      <div class="card"><h3 style="margin-top:0">Reconciliation</h3><p class="small muted" style="margin-bottom:0">Ledger balance against bank statement, per client and in total, with the difference explained line by line.</p><div class="small muted" style="margin-top:8px"><span class="pill ok">31 Aug 2026 &mdash; no difference</span></div></div>
      <div class="card"><h3 style="margin-top:0">Statutory checks</h3><p class="small muted" style="margin-bottom:0">Payout only with a solicitor's authority, no client money in the office account, no cross-subsidy between clients, records kept for the required retention period.</p><div class="small muted" style="margin-top:8px"><span class="pill ok">4 of 4 passed</span></div></div>
      <div class="card"><h3 style="margin-top:0">Export pack</h3><p class="small muted" style="margin-bottom:0">Client ledgers, cash book, bank reconciliation, list of client balances and the firm's own statements &mdash; as a signed bundle for the reporting accountant.</p><div class="small muted" style="margin-top:8px"><a href="#">Prepare pack</a></div></div>
    </div>
    <div class="note">A subscription product earns its keep here: the firm stops assembling this pack by hand at year end, and the firm's accountant stops asking for the missing sheet.</div>
    <p class="foot-note">Zentra Law prototype &middot; Zentra Property Group &middot; English (US) UI &middot; sample data only<br>Client account. No real money is represented here.</p>
"""]))))

PAGES_C.append(dict(f="portal.html", t="Client portal", body=T("".join([
"""@@TOP@@""",
"""    <h2 class="sec"><span class="num">1</span> What the client sees</h2>
    <div class="grid g2">
      <div class="card">
        <div class="lg"><div class="dhead"><b>Your purchase &mdash; Kajang, Selangor</b><span class="pill blue">in progress</span></div>
        <div class="lh"><div class="ln"><span>Stage</span><b>Loan documents and stamping</b></div>
          <div class="ln"><span>Completion</span><b>11 Dec 2026</b></div>
          <div class="ln"><span>Days left</span><b>@@DAYS_COMPLETE@@</b></div>
          <div class="ln"><span>Balance held for you</span><b>RM45,800.00</b></div></div>
        <div class="prog"><div style="width:82%"></div></div>
        <p class="small muted">Next: we stamp the transfer and the loan agreement on or before 22 Sep 2026. Nothing is required from you this week.</p>
        </div>
      </div>
      <div class="card"><h3 style="margin-top:0">Waiting for you</h3>
        <ul class="check">
          <li><span>1</span><div><b>Sign the facility agreement</b> &mdash; in person, bank branch, Thursday 18 Sep 2026, 10:00. You will need your identification document.</div></li>
          <li><span>2</span><div><b>Confirm the completion date</b> &mdash; choose a date in the portal, we will align with the seller's solicitors.</div></li>
          <li><span>3</span><div><b>Read the costs statement</b> &mdash; final figures will replace the estimate once stamping is done.</div></li>
        </ul>
        <div class="hr"></div>
        <p class="small muted" style="margin:0">Documents to download: SPA (countersigned), engagement letter, costs estimate, statement of account.</p>
      </div>
    </div>
""",
"""    <h2 class="sec"><span class="num">2</span> Design decisions in the portal</h2>
    <div class="grid g3">
      <div class="card"><h3 style="margin-top:0">No file names as passwords</h3><p class="small muted" style="margin-bottom:0">Access is by invitation to an email address or mobile number with a one-time code, never by an identification number or a file reference. An identification number is not a secret, and the firm would carry the loss if it were treated as one.</p></div>
      <div class="card"><h3 style="margin-top:0">Nothing confidential leaks</h3><p class="small muted" style="margin-bottom:0">The client sees their own file only: no internal notes, no fee-earner commentary, no other party's private data.</p></div>
      <div class="card"><h3 style="margin-top:0">Every view is logged</h3><p class="small muted" style="margin-bottom:0">Who opened which document, when, from where. That log is part of the client's data protection record and the firm's defence.</p></div>
    </div>
    <p class="foot-note">Zentra Law prototype &middot; Zentra Property Group &middot; English (US) UI &middot; sample data only<br>Client portal. Sample client data only.</p>
"""]))))

PAGES_C.append(dict(f="admin.html", t="Firm admin", body=T("".join([
"""@@TOP@@""",
"""    <h2 class="sec"><span class="num">1</span> The subscription this firm is on</h2>
    <div class="grid g3">
      <div class="card"><h3 style="margin-top:0">Plan</h3><div class="val" style="font-size:22px;font-weight:700">Practice</div>
        <p class="small muted">Up to 5 fee earners, unlimited matters, 3 practice areas enabled, 200 gigabytes of documents in Malaysia.</p>
        <div class="small muted">Placeholder pricing &mdash; to be set before launch.</div></div>
      <div class="card"><h3 style="margin-top:0">Modules enabled</h3>
        <div class="chips"><span class="chip on">Conveyancing</span><span class="chip on">Client account</span>
        <span class="chip on">Billing and e-invoice</span><span class="chip on">Client portal</span>
        <span class="chip">Corporate and commercial</span><span class="chip">Family and estate</span><span class="chip">Litigation</span></div></div>
      <div class="card"><h3 style="margin-top:0">Data residency</h3>
        <div class="pill ok">Malaysia</div>
        <p class="small muted" style="margin-bottom:0">Primary region in Malaysia; encrypted backups in a second Malaysian zone. No client data is sent outside Malaysia without the firm's written instruction and a lawful basis.</p></div>
    </div>
""",
"""    <h2 class="sec"><span class="num">2</span> Users, roles and access</h2>
    <div class="wrap-tbl card">
      <table class="tbl">
        <tr><th>User</th><th>Role</th><th>Sees</th><th>MFA</th><th>AI drafting</th><th>Last active</th></tr>
        <tr><td>A. Rahman</td><td>Partner <span class="pill blue">owner</span></td><td>Every matter, every ledger, all settings</td><td><span class="pill ok">on</span></td><td><span class="pill ok">on</span></td><td>today 08:12</td></tr>
        <tr><td>S. Leong</td><td>Lawyer</td><td>Own matters and the matters they are assigned</td><td><span class="pill ok">on</span></td><td><span class="pill ok">on</span></td><td>today 07:40</td></tr>
        <tr><td>N. Farah</td><td>Lawyer</td><td>Own matters</td><td><span class="pill ok">on</span></td><td><span class="pill amber">off by choice</span></td><td>yesterday</td></tr>
        <tr><td>R. Iswaran</td><td>Conveyancing clerk</td><td>Only the checklists and dates on files assigned</td><td><span class="pill ok">on</span></td><td><span class="pill gray">none</span></td><td>today 08:55</td></tr>
        <tr><td>M. Zulaikha</td><td>Accounts</td><td>Client ledgers, bills, reconciliations &mdash; no matter content</td><td><span class="pill ok">on</span></td><td><span class="pill gray">none</span></td><td>today 07:15</td></tr>
        <tr><td>Nurul Ain (client)</td><td>Client</td><td>Their own file only, as shown in the portal</td><td><span class="pill ok">one-time code</span></td><td><span class="pill gray">none</span></td><td>yesterday</td></tr>
      </table>
      <p class="small muted" style="margin-bottom:0">Role separation is not cosmetic: the clerk cannot post a ledger entry, and the accounts user cannot open a matter file. That is how the two-money separation survives a busy Friday.</p>
    </div>
""",
"""    <h2 class="sec"><span class="num">3</span> Settings a firm actually asks about</h2>
    <div class="grid g2">
      <div class="card"><h3 style="margin-top:0">Security</h3>
        <ul class="check">
          <li><span class="ok">&#10003;</span><div>Multi-factor authentication for every staff user, enforced, no exceptions.</div></li>
          <li><span class="ok">&#10003;</span><div>Encryption in transit and at rest, with keys managed by the platform.</div></li>
          <li><span class="ok">&#10003;</span><div>Session timeout, device list, and a one-click "sign out everywhere".</div></li>
          <li><span class="ok">&#10003;</span><div>Vendor access to a firm's data requires the firm's approval and is logged.</div></li>
        </ul></div>
      <div class="card"><h3 style="margin-top:0">Artificial intelligence</h3>
        <ul class="check">
          <li><span>1</span><div>Off by default for any firm that wants it off; off by choice for one lawyer in this firm.</div></li>
          <li><span>2</span><div>Client data is never sent to a public model, and never used to train a model.</div></li>
          <li><span>3</span><div>Where AI drafts, the draft is watermarked in the file history and a human must approve before it leaves the firm.</div></li>
          <li><span>4</span><div>The Bar Council's guidance on generative AI is quoted in the firm's own policy page, not hidden in a terms document.</div></li>
        </ul></div>
    </div>
    <p class="foot-note">Zentra Law prototype &middot; Zentra Property Group &middot; English (US) UI &middot; sample data only<br>Firm admin. Plans and pricing are placeholders pending a decision.</p>
"""]))))

PAGES_C.append(dict(f="compliance.html", t="Compliance guard", body=T("".join([
"""@@TOP@@""",
"""    <div class="note warn"><b>Read this screen first.</b> Most of what makes this product credible is here. A practice management system that quietly allows a referral commission, or a discount above the ceiling, or an electronically signed transfer, is a liability sold as a subscription.</div>
""",
"""    <h2 class="sec"><span class="num">1</span> Referral sources instead of referral payments</h2>
    <div class="wrap-tbl card">
      <table class="tbl">
        <tr><th>Matter</th><th>Source of instruction</th><th>Relation to the firm</th><th class="num">Paid to the source</th><th>Evidence</th></tr>
        <tr><td>CV-2026-0142</td><td>Walk-in enquiry at the counter</td><td>None</td><td class="num">RM0.00</td><td class="small">Attestation signed by the partner</td></tr>
        <tr><td>CV-2026-0138</td><td>Existing client, previous file 2024</td><td>Former client</td><td class="num">RM0.00</td><td class="small">Client record linked</td></tr>
        <tr><td>CV-2026-0151</td><td>Bank panel appointment</td><td>Panel firm code 7712</td><td class="num">RM0.00</td><td class="small">Panel appointment letter on file</td></tr>
        <tr><td>CV-2026-0160</td><td>Landlord's company secretary</td><td>Professional correspondent</td><td class="num">RM0.00</td><td class="small">No fee paid; noted in the file</td></tr>
      </table>
      <p class="small muted" style="margin-bottom:0">Bar Council Ruling 14.23 treats paying a person to introduce clients as touting. So the field exists to <i>record the source and show the zero</i>, not to pay anyone. There is no commission rule engine, no payout module and no agent ledger anywhere in this product.</p>
    </div>
""",
"""    <h2 class="sec"><span class="num">2</span> Discounts, waivers and publicity</h2>
    <div class="grid g2">
      <div class="card"><h3 style="margin-top:0">Fee decisions log</h3>
        <table class="tbl">
          <tr><th>Date</th><th>Matter</th><th>Decision</th><th>Approver</th></tr>
          <tr><td>12 Aug 2026</td><td>CV-2026-0142</td><td>25% discount, at the ceiling</td><td>A. Rahman</td></tr>
          <tr><td>15 Aug 2026</td><td>CV-2026-0138</td><td>Waiver of scale fee &mdash; family matter, recorded as a waiver</td><td>A. Rahman</td></tr>
          <tr><td>02 Sep 2026</td><td>CV-2026-0151</td><td>30% discount requested by referrals &mdash; <span class="pill bad">refused by the engine</span></td><td>&mdash;</td></tr>
        </table>
        <p class="small muted" style="margin-bottom:0">A request above the ceiling is not silently rounded down; it is refused and logged, which is the evidence a firm would want if the order were ever audited.</p></div>
      <div class="card"><h3 style="margin-top:0">Publicity approvals</h3>
        <table class="tbl">
          <tr><th>Material</th><th>Channel</th><th>Status</th></tr>
          <tr><td>Firm profile and practice areas</td><td>Website</td><td><span class="pill ok">approved</span></td></tr>
          <tr><td>Note on conveyancing timelines</td><td>Client newsletter</td><td><span class="pill ok">approved</span></td></tr>
          <tr><td>"Fastest transfer in town" advertisement</td><td>Social media</td><td><span class="pill bad">refused &mdash; comparative claim</span></td></tr>
        </table>
        <p class="small muted" style="margin-bottom:0">The rules on publicity are the firm's responsibility even when a third party writes the copy, so approvals are recorded against the material, not against the messenger.</p></div>
    </div>
""",
"""    <h2 class="sec"><span class="num">3</span> The rest of the guard rails</h2>
    <div class="grid g4">
      <div class="card"><h3 style="margin-top:0">Client money</h3><p class="small muted" style="margin-bottom:0">Ledger per client, reconciliation every month, retention of records, and no payout without a solicitor's authority.</p><div class="small muted" style="margin-top:8px"><span class="pill ok">4 of 4 checks passed</span></div></div>
      <div class="card"><h3 style="margin-top:0">Anti-money laundering</h3><p class="small muted" style="margin-bottom:0">Customer due diligence on every party, source of funds, and a record that survives the file.</p><div class="small muted" style="margin-top:8px"><span class="pill amber">2 files pending a document</span></div></div>
      <div class="card"><h3 style="margin-top:0">Data protection</h3><p class="small muted" style="margin-bottom:0">Consent notices, retention and disposal schedule, breach playbook with a 72-hour clock, and a named officer.</p><div class="small muted" style="margin-top:8px"><span class="pill ok">policy published</span></div></div>
      <div class="card"><h3 style="margin-top:0">Signing method</h3><p class="small muted" style="margin-bottom:0">Documents that may not be signed electronically are blocked in code, with the attempt logged.</p><div class="small muted" style="margin-top:8px"><span class="pill ok">enforced</span></div></div>
    </div>
    <p class="foot-note">Zentra Law prototype &middot; Zentra Property Group &middot; English (US) UI &middot; sample data only<br>Compliance guard. Design intent only; the firm remains responsible for its own compliance, and the rules cited must be verified with counsel.</p>
"""]))))

PAGES_C.append(dict(f="audit.html", t="Audit trail", body=T("".join([
"""@@TOP@@""",
"""    <h2 class="sec"><span class="num">1</span> Who did what, sealed</h2>
    <div class="card">
      <div class="wrap-tbl">
        <table class="tbl">
          <tr><th>When</th><th>User</th><th>Action</th><th>Record</th><th class="mono small">Seal</th></tr>
          <tr><td>17 Sep 2026 08:55</td><td>R. Iswaran</td><td>Attempted to send Form 14A for e-signature</td><td>CV-2026-0142</td><td class="mono small">4f8c&hellip;1a7</td></tr>
          <tr><td>17 Sep 2026 08:55</td><td>system</td><td>Refused: instrument of transfer is not eligible for electronic signature</td><td>CV-2026-0142</td><td class="mono small">b21e&hellip;903</td></tr>
          <tr><td>17 Sep 2026 08:41</td><td>S. Leong</td><td>Approved payout RM7,920.00 from client account against bill 1042</td><td>CV-2026-0142</td><td class="mono small">77aa&hellip;c15</td></tr>
          <tr><td>17 Sep 2026 08:12</td><td>A. Rahman</td><td>Refused a 30% discount request: above the order's ceiling</td><td>CV-2026-0151</td><td class="mono small">e0d4&hellip;88b</td></tr>
          <tr><td>16 Sep 2026 17:20</td><td>M. Zulaikha</td><td>Signed off monthly bank reconciliation, no difference</td><td>Client account &mdash; August 2026</td><td class="mono small">1c93&hellip;5fe</td></tr>
          <tr><td>16 Sep 2026 15:02</td><td>Nurul Ain (client)</td><td>Downloaded countersigned sale and purchase agreement</td><td>Client portal</td><td class="mono small">9ad1&hellip;7c4</td></tr>
          <tr><td>15 Sep 2026 11:31</td><td>system</td><td>Reminder sent: stamping due in 7 days</td><td>CV-2026-0142</td><td class="mono small">55ef&hellip;210</td></tr>
        </table>
      </div>
    </div>
""",
"""    <h2 class="sec"><span class="num">2</span> How the trail is protected</h2>
    <div class="grid g4">
      <div class="card"><h3 style="margin-top:0">Append only</h3><p class="small muted" style="margin-bottom:0">Entries are written once. There is no edit and no delete, only a correcting entry that points at the original.</p></div>
      <div class="card"><h3 style="margin-top:0">Chained</h3><p class="small muted" style="margin-bottom:0">Each entry carries a seal derived from the previous one, so a gap or a rewrite is visible.</p></div>
      <div class="card"><h3 style="margin-top:0">Readable by the firm</h3><p class="small muted" style="margin-bottom:0">The firm can export its own trail at any time, which matters if it ever changes system.</p></div>
      <div class="card"><h3 style="margin-top:0">Not visible to others</h3><p class="small muted" style="margin-bottom:0">One firm never sees another firm's trail. Isolation is tested, not assumed.</p></div>
    </div>
    <p class="foot-note">Zentra Law prototype &middot; Zentra Property Group &middot; English (US) UI &middot; sample data only<br>Audit trail. Seals illustrative.</p>
"""]))))

PAGES_C.append(dict(f="roadmap.html", t="Roadmap", body=T("".join([
"""@@TOP@@""",
"""    <div class="note">One system, five practice areas, one release at a time. Conveyancing comes first because the work is rule-driven, document-heavy and repeated &mdash; exactly where software earns its keep.</div>
""",
"""    <h2 class="sec"><span class="num">1</span> Practice areas and when they arrive</h2>
    <div class="wrap-tbl card">
      <table class="tbl">
        <tr><th>Practice area</th><th>What the module must know</th><th>Phase</th><th>Depends on</th></tr>
        <tr><td><b>Conveyancing</b><div class="small muted">Subsale, financing, developer sales, tenancy, consent and estate transfers</div></td>
            <td>Scale fees, stamp duty, 3+1 months, HDA stages, land office presentation, CKHT</td>
            <td><span class="pill ok">Phase 1</span></td><td class="small">Nothing &mdash; this is the first build</td></tr>
        <tr><td><b>Corporate and commercial</b><div class="small muted">Company secretarial work, share and asset sales, contracts</div></td>
            <td>Statutory registers and deadlines, board and member resolutions, e-invoice for corporate clients</td>
            <td><span class="pill blue">Phase 2</span></td><td class="small">Document assembly, billing</td></tr>
        <tr><td><b>Employment and industrial relations</b><div class="small muted">Contracts, misconduct and dismissal, Industrial Court matters</div></td>
            <td>Statutory timelines for domestic inquiry and representation, award tracking</td>
            <td><span class="pill blue">Phase 2</span></td><td class="small">Matter model, deadlines engine</td></tr>
        <tr><td><b>Family and estate planning</b><div class="small muted">Wills, probate, letters of administration, guardianship</div></td>
            <td>Asset schedules, court forms, renunciation and consent documents, distribution accounts</td>
            <td><span class="pill violet">Phase 3</span></td><td class="small">Document assembly, client portal</td></tr>
        <tr><td><b>Litigation</b><div class="small muted">Civil and commercial disputes up to trial and appeal</div></td>
            <td>Court filing references, cause papers, hearing dates, cause-book chronology, e-filing</td>
            <td><span class="pill violet">Phase 4</span></td><td class="small">Hearing and event calendar, evidence bundle</td></tr>
      </table>
    </div>
""",
"""    <h2 class="sec"><span class="num">2</span> Build phases</h2>
    <div class="steps">
      <div class="step done"><span>0</span><div><b>Clickable prototype</b><div class="small muted">This set of screens, with sample data. Purpose: approve the shape before any database exists.</div></div></div>
      <div class="step active"><span>1</span><div><b>Conveyancing minimum</b><div class="small muted">Matters, checklist, documents, deadlines, fee engine, client account, billing, portal, audit trail &mdash; one firm, then tenants.</div></div></div>
      <div class="step"><span>2</span><div><b>Second and third practice areas</b><div class="small muted">Corporate, commercial and employment, reusing the same matter and billing core.</div></div></div>
      <div class="step"><span>3</span><div><b>Family and estate</b><div class="small muted">Probate packs, wills and trust work, with stricter confidentiality defaults.</div></div></div>
      <div class="step"><span>4</span><div><b>Litigation</b><div class="small muted">Court-driven calendars and evidence management, the heaviest build of the five.</div></div></div>
    </div>
""",
"""    <h2 class="sec"><span class="num">3</span> What is deliberately out of scope</h2>
    <div class="grid g3">
      <div class="card"><h3 style="margin-top:0">Legal advice by machine</h3><p class="small muted" style="margin-bottom:0">The product drafts from the firm's own precedents and computes from the law, but it does not give advice, and it never signs anything by itself.</p></div>
      <div class="card"><h3 style="margin-top:0">Holding client money</h3><p class="small muted" style="margin-bottom:0">No payment gateway touches client funds. If a firm wants to collect from a client, the money lands in the firm's account, recorded by the ledger.</p></div>
      <div class="card"><h3 style="margin-top:0">Buying clients for firms</h3><p class="small muted" style="margin-bottom:0">No lead marketplace, no commission, no referral payout. That boundary protects the subscribing firm first.</p></div>
    </div>
    <p class="foot-note">Zentra Law prototype &middot; Zentra Property Group &middot; English (US) UI &middot; sample data only<br>Roadmap. Phasing indicative.</p>
"""]))))

PAGES_C.append(dict(f="guide.html", t="Review guide", body=T("".join([
"""@@TOP@@""",
"""    <div class="note warn"><b>How to review this prototype.</b> Nothing here is final, and nothing is connected to a database. Walk the screens in this order, keep one question in your mind for each, and mark down anything that feels wrong &mdash; the next phase is easier to change than the one after it.</div>
""",
"""    <h2 class="sec"><span class="num">1</span> Ten screens, ten questions</h2>
    <div class="wrap-tbl card">
      <table class="tbl">
        <tr><th style="width:26%">Screen</th><th>What to check</th><th style="width:34%">Decision it unlocks</th></tr>
        <tr><td><a href="index.html">Overview</a></td><td>Is this the right first screen for a firm, and are these the four numbers a firm looks at?</td><td>Default dashboard content</td></tr>
        <tr><td><a href="matters.html">Matters</a></td><td>Are the stages the ones your conveyancing actually moves through?</td><td>Stage model and matter fields</td></tr>
        <tr><td><a href="matter.html">Matter detail</a></td><td>Is anything a lawyer needs missing from this one screen?</td><td>Matter workspace layout</td></tr>
        <tr><td><a href="checklist.html">Checklist</a></td><td>Would your clerk work from this list, and are the owners right?</td><td>Checklist templates per matter type</td></tr>
        <tr><td><a href="documents.html">Documents</a></td><td>Do you agree that the transfer and the charge must never be e-signed, and is the guard firm enough?</td><td>Signing rules per document</td></tr>
        <tr><td><a href="signing.html">Signing room</a></td><td>Is the wet-ink session record the thing your firm would actually use?</td><td>Signing workflow priority</td></tr>
        <tr><td><a href="deadlines.html">Statutory clock</a></td><td>Are the clocks and reminder days the ones that save you?</td><td>Deadline rules and reminders</td></tr>
        <tr><td><a href="fees.html">Fee engine</a></td><td>Do the numbers match how you bill today, including the discount ceiling?</td><td>Fee rules, discount and waiver policy</td></tr>
        <tr><td><a href="client-account.html">Client account</a></td><td>Does the reconciliation pack match what your accountant asks for?</td><td>Ledger and reporting requirements</td></tr>
        <tr><td><a href="compliance.html">Compliance guard</a></td><td>Is the no-referral-payment boundary the right one, and does the publicity log solve a real problem?</td><td>Compliance posture of the product</td></tr>
      </table>
    </div>
""",
"""    <h2 class="sec"><span class="num">2</span> Then four product decisions</h2>
    <div class="grid g2">
      <div class="card"><h3 style="margin-top:0">1. Pricing shape</h3><p class="small muted" style="margin-bottom:0">Per fee earner per month, or per matter, or a base fee plus modules? The prototype shows a plan card but no numbers, on purpose.</p></div>
      <div class="card"><h3 style="margin-top:0">2. Tenant scope at launch</h3><p class="small muted" style="margin-bottom:0">One friendly firm first, or straight to multiple subscribing firms? Isolation work differs.</p></div>
      <div class="card"><h3 style="margin-top:0">3. Signature provider</h3><p class="small muted" style="margin-bottom:0">Malaysian provider by default, with a foreign alternative for firms that insist? Evidence bundle stays the same either way.</p></div>
      <div class="card"><h3 style="margin-top:0">4. What is outsourced</h3><p class="small muted" style="margin-bottom:0">Documents, e-invoice, e-signature and hosting can each be built or bought. The prototype assumes bought.</p></div>
    </div>
    <p class="foot-note">Zentra Law prototype &middot; Zentra Property Group &middot; English (US) UI &middot; sample data only<br>Review guide. Return answers in any form; they become the next version of the plan.</p>
"""]))))
