# _f0_b.py — Zentra Law F0: documents, signing, deadlines, fee engine
from _f0_common import *
from _f0_a import T, V

PAGES_B = []

DOCS = [
    ("Letter of engagement and costs estimate", "Client", "E-signature", "ok", "Electronic Commerce Act 2006 allows it. SigningCloud envelope with hash and log."),
    ("PDPA consent notice", "Client", "E-signature", "ok", "Consent must be recorded with time and the exact wording shown."),
    ("Tenancy agreement", "Landlord and tenant", "E-signature", "ok", "Not a document excluded by the ECA. Stamp the counterpart within 30 days."),
    ("Sale and purchase agreement (subsale)", "All parties plus witnesses", "Wet-ink", "warn", "Attestation is required; the completed agreement is produced for stamping and for the land office chain."),
    ("Memorandum of Transfer (Form 14A)", "Transferor and transferee", "Wet-ink only", "bad", "Excluded in practice: the land office will not register an electronically signed instrument."),
    ("Charge or Deed of Assignment (Form 16A)", "Charger and chargee", "Wet-ink only", "bad", "Same as the transfer. The bank also insists on its own execution page."),
    ("Bank letter of offer or facility agreement", "Bank and borrower", "Bank's rule", "warn", "Some banks accept e-signature, most do not. The system follows the panel's instruction per bank."),
    ("Statutory declaration", "Declarant plus commissioner", "Wet-ink", "warn", "Must be sworn before a commissioner for oaths."),
    ("Invoice, receipt and statement of account", "Firm to client", "No signature", "ok", "Generated and sent; the e-invoice status from LHDN is tracked alongside."),
]

def rows_docs():
    out = []
    for name, who, method, cls, why in DOCS:
        out.append('<tr><td><b>' + name + '</b><div class="small muted">' + why + '</div></td><td class="small">' + who +
                   '</td><td><span class="pill ' + cls + '">' + method + '</span></td>'
                   '<td class="small"><a href="#">generate</a> &middot; <a href="#">send for signature</a></td></tr>')
    return "\n".join(out)

PAGES_B.append(dict(f="documents.html", t="Documents and signing", body=T("".join([
"""@@TOP@@""",
"""    <div class="note warn"><b>The rule that shapes this screen.</b> E-signature is lawful in Malaysia, but the Electronic Commerce Act 2006 excludes certain documents and, in practice, the land offices and stamping counter want wet ink on instruments of transfer and charge. So the product does not offer one signing method &mdash; it offers the <b>correct</b> one per document, and refuses the wrong one.</div>
""",
"""    <h2 class="sec"><span class="num">1</span> Signing matrix</h2>
    <div class="card">
      <div class="wrap-tbl">
        <table class="tbl">
          <tr><th>Document</th><th>Signatories</th><th>Method</th><th style="width:170px">Action</th></tr>
@@DOC_ROWS@@
        </table>
      </div>
    </div>
""",
"""    <h2 class="sec"><span class="num">2</span> Try the guard</h2>
    <div class="card">
      <div class="grid g2">
        <div>
          <div class="field"><label class="small muted">Document to send</label>
            <select id="docSel">
              <option value="esign">Letter of engagement and costs estimate</option>
              <option value="esign">PDPA consent notice</option>
              <option value="esign">Tenancy agreement</option>
              <option value="wet">Sale and purchase agreement (subsale)</option>
              <option value="block">Memorandum of Transfer (Form 14A)</option>
              <option value="block">Charge or Deed of Assignment (Form 16A)</option>
            </select></div>
          <div class="field" style="margin-top:10px"><label class="small muted">Recipient</label>
            <input placeholder="client@email.com" value="nurul.sample@email.com"></div>
          <p style="margin-top:14px"><button class="btn" id="sendBtn">Send for e-signature</button></p>
        </div>
        <div>
          <div class="note" id="guardBox"><b>Ready.</b> Choose a document on the left and press send &mdash; the prototype answers exactly as the real system would.</div>
        </div>
      </div>
    </div>
""",
"""    <h2 class="sec"><span class="num">3</span> Template library</h2>
    <div class="grid g3">
      <div class="card"><h3 style="margin-top:0">Conveyancing</h3><p class="small muted" style="margin-bottom:0">Subsale SPA, developer SPA (Schedule G and H), deed of assignment, discharge of charge, completion accounts, undertakings, CKHT forms, tenancy, letter of demand.</p></div>
      <div class="card"><h3 style="margin-top:0">Corporate and commercial</h3><p class="small muted" style="margin-bottom:0">Share sale, shareholders' agreement, board and members' resolutions, employment contracts, distributor and service agreements.</p></div>
      <div class="card"><h3 style="margin-top:0">Family and estate</h3><p class="small muted" style="margin-bottom:0">Wills, grant of probate and letters of administration packs, trust deeds, guardianship, transfer by love and affection.</p></div>
    </div>
    <p class="foot-note">Zentra Law prototype &middot; Zentra Property Group &middot; English (US) UI &middot; sample data only<br>Documents and signing. Templates shown are placeholders; the firm supplies its own precedent.</p>
"""]))))

PAGES_B.append(dict(f="signing.html", t="Signing room", body=T("".join([
"""@@TOP@@""",
"""    <h2 class="sec"><span class="num">1</span> Signing sessions this week</h2>
    <div class="wrap-tbl card">
      <table class="tbl">
        <tr><th>Session</th><th>Matter</th><th>When</th><th>Where</th><th>Documents</th><th>Status</th></tr>
        <tr><td><b>SS-2026-0088</b></td><td>CV-2026-0142</td><td>Thu 18 Sep 2026, 10:00</td><td>Firm's office, meeting room 2</td><td>MOT, Charge, 4 SPA copies</td><td><span class="pill amber">witness arranged</span></td></tr>
        <tr><td><b>SS-2026-0089</b></td><td>CV-2026-0162</td><td>Fri 19 Sep 2026, 15:30</td><td>Client's home, Kuala Selangor</td><td>Form 14A, statutory declaration</td><td><span class="pill blue">out for signature</span></td></tr>
        <tr><td><b>SS-2026-0091</b></td><td>CV-2026-0138</td><td>Mon 22 Sep 2026, 09:30</td><td>Bank's branch, Kajang</td><td>Discharge of charge, undertakings</td><td><span class="pill gray">awaiting bank</span></td></tr>
        <tr><td><b>SS-2026-0094</b></td><td>CV-2026-0160</td><td>E-signature, no visit</td><td>Remote</td><td>Tenancy agreement</td><td><span class="pill ok">1 of 2 signed</span></td></tr>
      </table>
    </div>
""",
"""    <h2 class="sec"><span class="num">2</span> What a wet-ink session has to record</h2>
    <div class="grid g3">
      <div class="card"><h3 style="margin-top:0">Attendance</h3><p class="small muted" style="margin-bottom:0">Who was present, in what capacity, identification seen, and whether a witness was independent of the firm.</p></div>
      <div class="card"><h3 style="margin-top:0">Documents in and out</h3><p class="small muted" style="margin-bottom:0">Each document, number of copies, which copies left with which party, and what came back signed.</p></div>
      <div class="card"><h3 style="margin-top:0">Afterwards</h3><p class="small muted" style="margin-bottom:0">Scanned copy filed against the checklist item, originals logged into the deed box, and the next statutory clock started.</p></div>
    </div>
    <div class="note">Conveyancing is still a paper practice. Most conveyancing signing in Malaysia is wet ink, so this room matters more than the e-signature button &mdash; that is why the prototype gives it its own screen.</div>
""",
"""    <h2 class="sec"><span class="num">3</span> E-signature envelopes in flight</h2>
    <div class="wrap-tbl card">
      <table class="tbl">
        <tr><th>Envelope</th><th>Document</th><th>Recipients</th><th>Sent</th><th>Status</th><th>Evidence</th></tr>
        <tr><td>EN-4471</td><td>Letter of engagement &mdash; CV-2026-0142</td><td>1 of 1</td><td>12 Aug 2026</td><td><span class="pill ok">completed</span></td><td class="small"><a href="#">certificate &middot; hash &middot; log</a></td></tr>
        <tr><td>EN-4503</td><td>Tenancy agreement &mdash; CV-2026-0160</td><td>2 of 2</td><td>15 Sep 2026</td><td><span class="pill blue">1 signed, 1 viewed</span></td><td class="small"><a href="#">audit trail</a></td></tr>
        <tr><td>EN-4508</td><td>PDPA consent notice &mdash; CV-2026-0155</td><td>1 of 1</td><td>16 Sep 2026</td><td><span class="pill amber">reminder sent</span></td><td class="small"><a href="#">audit trail</a></td></tr>
      </table>
      <p class="small muted" style="margin-bottom:0">Completed envelopes keep the signed PDF, the signing certificate, the document hash and the access log together &mdash; that bundle is what the firm produces if a signature is ever disputed.</p>
    </div>
    <p class="foot-note">Zentra Law prototype &middot; Zentra Property Group &middot; English (US) UI &middot; sample data only<br>Signing room. Signature provider to be confirmed: SigningCloud Malaysia is the working assumption.</p>
"""]))))

PAGES_B.append(dict(f="deadlines.html", t="Statutory clock", body=T("".join([
"""@@TOP@@""",
"""    <div class="grid g4">
      <div class="kpi warn"><div class="lab">Due within 7 days</div><div class="val">1</div><div class="sub">stamping, CV-2026-0142</div></div>
      <div class="kpi"><div class="lab">Due within 30 days</div><div class="val">4</div><div class="sub">stamping and consent</div></div>
      <div class="kpi"><div class="lab">Completion clocks running</div><div class="val">7</div><div class="sub">3+1 months, late interest tracked</div></div>
      <div class="kpi blue"><div class="lab">CKHT filings open</div><div class="val">2</div><div class="sub">60 days from disposal</div></div>
    </div>
""",
"""    <h2 class="sec"><span class="num">1</span> The clock, matter by matter</h2>
    <div class="wrap-tbl card">
      <table class="tbl">
        <tr><th>Matter</th><th>Obligation</th><th>Starts</th><th>Due</th><th class="num">Days left</th><th>Rule</th></tr>
        <tr><td>CV-2026-0142</td><td>Stamp the MOT and loan agreement</td><td>Execution 23 Aug 2026</td><td>22 Sep 2026</td><td class="num"><span class="pill amber">@@DAYS_STAMP@@</span></td><td class="small muted">Within 30 days; late stamping attracts a penalty</td></tr>
        <tr><td>CV-2026-0142</td><td>Complete the purchase and release the balance</td><td>SPA 12 Aug 2026</td><td>11 Dec 2026</td><td class="num">@@DAYS_COMPLETE@@</td><td class="small muted">3 months plus 1 month extension; 8% per annum late interest</td></tr>
        <tr><td>CV-2026-0138</td><td>CKHT1 filing and retention, seller side</td><td>Disposal date</td><td>+60 days</td><td class="num">19</td><td class="small muted">Seller's retention held by the firm, then remitted</td></tr>
        <tr><td>CV-2026-0151</td><td>Stamp the facility agreement</td><td>Execution 02 Sep 2026</td><td>01 Oct 2026</td><td class="num">14</td><td class="small muted">Within 30 days</td></tr>
        <tr><td>CV-2026-0155</td><td>Progressive instalment 10% on SPA</td><td>SPA date</td><td>On execution</td><td class="num">0</td><td class="small muted">HDA Schedule H, Third Schedule stages</td></tr>
        <tr><td>CV-2026-0162</td><td>State Authority consent, leasehold transfer</td><td>Application 30 Jul 2026</td><td>Track reply</td><td class="num">open</td><td class="small muted">Consent window varies by state land office</td></tr>
      </table>
    </div>
""",
"""    <h2 class="sec"><span class="num">2</span> Why the clock is the product</h2>
    <div class="grid g2">
      <div class="card"><h3 style="margin-top:0">What a missed date costs</h3>
        <ul class="check">
          <li><span>1</span><div>Penalty on late stamping of the transfer or loan instrument.</div></li>
          <li><span>2</span><div>Late-payment interest at the contractual rate, usually paid by whoever caused the delay.</div></li>
          <li><span>3</span><div>An extension of time negotiated at a disadvantage, or a notice to complete.</div></li>
          <li><span>4</span><div>A professional negligence claim, and a claim the firm's insurance may or may not answer.</div></li>
        </ul>
      </div>
      <div class="card"><h3 style="margin-top:0">What the system does about it</h3>
        <ul class="check">
          <li><span>1</span><div>Every date is derived, not typed: the SPA date creates the completion clock and the interest rate.</div></li>
          <li><span>2</span><div>Reminders go out at 30, 14, 7, 3 and 1 day, to the lawyer and to the clerk.</div></li>
          <li><span>3</span><div>A red date cannot be dismissed without a written reason recorded against the file.</div></li>
          <li><span>4</span><div>The client portal shows the same countdown, which removes the "I did not know" conversation.</div></li>
        </ul>
      </div>
    </div>
    <p class="foot-note">Zentra Law prototype &middot; Zentra Property Group &middot; English (US) UI &middot; sample data only<br>Statutory clock. Dates shown are illustrative.</p>
"""]))))

PAGES_B.append(dict(f="fees.html", t="Fee engine", body=T("".join([
"""@@TOP@@""",
"""    <div class="note warn"><b>Why this screen exists.</b> In conveyancing the fee is not a matter of taste: the Solicitors' Remuneration Order 2023 sets a scale, caps the discount at 25% of the scale fee for sale and transfer work, and separates a genuine waiver of fees on the client's behalf from a discount to a referrer. A firm that guesses loses money, or breaches the order. So the numbers are computed, not typed.</div>
""",
"""    <h2 class="sec"><span class="num">1</span> Live calculator</h2>
    <div class="card">
      <div class="grid g3">
        <div class="field"><label class="small muted">Purchase price or adjudicated value (RM)</label><input id="fPrice" value="650000"></div>
        <div class="field"><label class="small muted">Loan amount (RM)</label><input id="fLoan" value="520000"></div>
        <div class="field"><label class="small muted">Discount on scale fee (%)</label><input id="fDisc" value="25"></div>
      </div>
      <div class="hr"></div>
      <div class="wrap-tbl">
        <table class="tbl" id="fOut">
          <tr><th>Line</th><th>Basis</th><th class="num">Amount (RM)</th></tr>
        </table>
      </div>
      <p class="small muted"><b>Bands applied:</b> scale fee 1.25% on the first RM500,000 (minimum RM500), then 1% on the next RM7,000,000, then negotiable above RM7,500,000 but not exceeding 1%. MOT stamp duty: 1% on the first RM100,000, 2% on the next RM400,000, 3% on the next RM500,000, 4% above RM1,000,000. Loan agreement duty: 0.5% of the amount secured. SST 8% on professional fees.</p>
      <div class="note" id="discNote"></div>
    </div>
""",
"""    <h2 class="sec"><span class="num">2</span> Discount, waiver and what is neither</h2>
    <div class="grid g3">
      <div class="card"><h3 style="margin-top:0">Discount</h3><p class="small muted" style="margin-bottom:0">A reduction of the scale fee, capped at 25% for sale and transfer work. The cap is enforced by the engine, not by a policy memo.</p></div>
      <div class="card"><h3 style="margin-top:0">Waiver</h3><p class="small muted" style="margin-bottom:0">A deliberate act of the firm, recorded as a waiver with a reason and an approver. Reporting a waiver as a discount is what gets a firm into trouble.</p></div>
      <div class="card"><h3 style="margin-top:0">Referral payment</h3><p class="small muted" style="margin-bottom:0">Not permitted at all. There is no field for it anywhere in this system, and the guard screen explains why.</p></div>
    </div>
""",
"""    <h2 class="sec"><span class="num">3</span> Rate versions</h2>
    <div class="wrap-tbl card">
      <table class="tbl">
        <tr><th>Rate table</th><th>Version</th><th>Effective from</th><th>Source</th><th>Applied to</th></tr>
        <tr><td>Scale fees, sale and transfer</td><td>v3</td><td>15 Jul 2023</td><td>Solicitors' Remuneration Order 2023, First Schedule</td><td><span class="pill ok">current</span></td></tr>
        <tr><td>Scale fees, financing documents</td><td>v2</td><td>15 Jul 2023</td><td>Solicitors' Remuneration Order 2023, Third Schedule</td><td><span class="pill ok">current</span></td></tr>
        <tr><td>Stamp duty, transfer</td><td>v6</td><td>01 Jan 2026</td><td>Stamp Act 1949, current bands</td><td><span class="pill ok">current</span></td></tr>
        <tr><td>Stamp duty, loan security</td><td>v4</td><td>01 Jan 2026</td><td>Stamp Act 1949, 0.5%</td><td><span class="pill ok">current</span></td></tr>
        <tr><td>RPGT and CKHT rates</td><td>v5</td><td>01 Jan 2026</td><td>Real Property Gains Tax Act 1976</td><td><span class="pill ok">current</span></td></tr>
      </table>
      <p class="small muted" style="margin-bottom:0">A central rate table is the quiet advantage of a subscription product: when the next budget changes a band, every subscribing firm is on the new number the same morning, and every old bill still shows the version it used.</p>
    </div>
    <p class="foot-note">Zentra Law prototype &middot; Zentra Property Group &middot; English (US) UI &middot; sample data only<br>Fee engine. Figures are illustrative; verify against the current order before use.</p>
"""]))))
