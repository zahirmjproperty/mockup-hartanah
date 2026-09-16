# _f0_d.py — Zentra Law F0: drafting, vetting and execution pipeline
from _f0_common import *
from _f0_a import T

PAGES_D = []

STAGES = [
    ("1", "Instruction in", "done", "1 day", "Client, parties, source of instruction, conflict check started"),
    ("2", "Facts and term sheet", "done", "2 days", "Price, deposit, target dates, special conditions, fixtures, arrears"),
    ("3", "Search and title report", "done", "3-5 days", "Land search, bankruptcy search, issue list for the draft"),
    ("4", "Precedent and clause selection", "done", "1 day", "Firm's precedent bank plus clause library, version cited"),
    ("5", "First draft", "done", "3-5 days", "v0.1 assembled with schedules filled"),
    ("6", "Internal review and partner approval", "done", "2-4 days", "v0.2 after peer comments, v1.0 approved for issue"),
    ("7", "Issue to the other side", "active", "1 day after approval", "Covering letter, version logged, other side's clock starts"),
    ("8", "Counterparty mark-up received", "active", "day 9 of 14", "Clause-by-clause comparison generated"),
    ("9", "Vetting against the playbook", "active", "3 days from receipt", "Every deviation categorised: accept, refuse, negotiate"),
    ("10", "Negotiation rounds", "todo", "n rounds", "Redraft with a change summary for each round"),
    ("11", "Client instruction and approval", "todo", "3-10 days", "Advice log; client authority for the final terms"),
    ("12", "Engrossment and version freeze", "todo", "-", "Execution version, hashed, copies scheduled"),
    ("13", "Execution", "todo", "session or HIMS", "Wet ink, HIMS e-SPA, or permitted e-signature"),
    ("14", "Post-execution", "todo", "30 days to stamp", "e-Duti Setem, distribution, registration, file closure"),
]

VERSIONS = [
    ("v0.1", "12 Aug 2026", "Drafted from precedent PP-SPA-SUB-BUY v4", "Internal first draft", "A. Rahman", "a41c&hellip;"),
    ("v0.2", "14 Aug 2026", "Peer review: loan rejection clause added, fixtures schedule expanded", "Internal", "S. Leong", "7e02&hellip;"),
    ("v1.0", "15 Aug 2026", "Approved for issue to the seller's solicitors", "Issued", "A. Rahman", "b8d5&hellip;"),
    ("v1.1", "09 Sep 2026", "Counterparty mark-up: completion 3+1 to 3+2 months, interest 8% to 10%, vacant possession penalty deleted", "Received", "&mdash;", "3f19&hellip;"),
    ("v1.2", "11 Sep 2026", "Our response: interest capped at 8%, per-day penalty restored at RM100, extension refused unless financing delayed", "Issued", "A. Rahman", "c6b7&hellip;"),
    ("EV-1", "16 Sep 2026", "Execution version frozen for signing, 4 copies, fixtures schedule final", "Frozen", "A. Rahman", "9ad4&hellip;"),
]

NEGO = [
    ("Completion period", "3 months plus 1 month extension", "3+1 only; no second extension", "3+2 months", "Refused the second month; extension stays 1 month with interest", "A. Rahman", "11 Sep"),
    ("Late payment interest", "8% per annum on the balance, daily", "8% maximum", "10% per annum", "Settled at 8%; interest not payable where delay is the seller's", "A. Rahman", "11 Sep"),
    ("Vacant possession penalty", "RM100 per day after the completion date", "RM50 per day", "Deleted entirely", "Restored at RM100 per day; seller accepted after explanation", "A. Rahman", "11 Sep"),
    ("Loan rejection clause", "Agreement voidable, deposit refunded less administration cost, 60 days to obtain approval", "Refund less RM1,500", "No such clause", "**Kept.** Client refused the seller's position", "Client, on advice", "09 Sep"),
    ("Fixtures and fittings", "Itemised schedule annexed", "Itemised schedule", "&ldquo;As is&rdquo; with no schedule", "Schedule annexed; air conditioners and water heaters listed", "S. Leong", "10 Sep"),
    ("Quit rent and assessment arrears", "Seller settles to the completion date", "Apportioned", "Buyer takes over all arrears", "Seller settles; receipts to be produced before completion", "S. Leong", "11 Sep"),
]

SLA = [
    ("Draft of v1.2 in the other side's hands", "Seller's solicitors (M/s Tan & Co)", "9 days", "Reminder at 7 days sent 15 Sep", "warn"),
    ("Client instruction on the sellers' second extension request", "Client (Nurul Ain)", "2 days", "Portal note sent, phone call logged 16 Sep", "ok"),
    ("Bank facility agreement to be returned signed", "CIMB panel solicitors", "5 days", "Chase on 18 Sep", "warn"),
    ("Stamping money to be placed with us", "Client", "12 days", "Due before 22 Sep stamping", "bad"),
]

INSTR = [
    ("09 Sep 2026", "Seller wants a 2-month extension instead of 1", "Explained the interest exposure for the client, and that the extension protects the seller, not us", "Client instructed us to refuse the extension", "Portal note plus phone call"),
    ("09 Sep 2026", "Seller deleted the vacant possession penalty", "Explained why the penalty matters where the seller still occupies the house", "Client asked us to restore it &mdash; done", "Portal note"),
    ("10 Sep 2026", "Seller proposes to keep the air conditioners", "Advised that fixtures should be itemised on a schedule to avoid a dispute at handover", "Client instructed: schedule required", "Email on file"),
]

PLAYBOOK = [
    ("Deposit", "10%: 2-3% on booking, balance to 10% on SPA", "Staged payment across two dates", "Paid to the seller directly before the SPA is signed"),
    ("Completion", "3 months plus 1 month", "3 months where financing is already approved", "Repeated extensions with no interest"),
    ("Late payment interest", "8% per annum, daily on the balance", "8% per annum", "No cap, or interest on the full price"),
    ("Loan rejection", "Voidable with deposit refunded less administration cost", "Refund less RM1,500 within 21 days", "No loan rejection clause at all"),
    ("Vacant possession", "On completion, free of occupiers and tenants", "7 days later with a daily penalty", "Undisclosed tenancy"),
    ("Vacant possession penalty", "RM100-200 per day", "RM50 per day", "No penalty"),
    ("Arrears of quit rent and assessment", "Seller clears to the completion date", "Apportioned", "Buyer takes over the arrears"),
    ("Fixtures and fittings", "Itemised schedule annexed", "Short schedule", "\u201cAs is\u201d with nothing listed"),
    ("Seller default", "Deposit returned with interest and costs", "Deposit returned", "10% forfeited even where the seller defaults"),
]

def rows_versions():
    out = []
    for v, when, change, state, who, seal in VERSIONS:
        cls = {"Internal": "gray", "Issued": "blue", "Received": "amber", "Frozen": "ok"}.get(state, "gray")
        out.append('<tr><td class="mono"><b>' + v + '</b></td><td class="small">' + when + '</td>'
                   '<td class="small">' + change + '</td><td><span class="pill ' + cls + '">' + state + '</span></td>'
                   '<td class="small">' + who + '</td><td class="mono small">' + seal + '</td></tr>')
    return "\n".join(out)

def rows_nego():
    out = []
    for clause, ours, fallback, theirs, outcome, who, when in NEGO:
        out.append('<tr><td><b>' + clause + '</b></td><td class="small">' + ours + '</td>'
                   '<td class="small muted">' + fallback + '</td><td class="small">' + theirs + '</td>'
                   '<td class="small">' + outcome + '</td><td class="small">' + who + '<div class="muted">' + when + '</div></td></tr>')
    return "\n".join(out)

def rows_stages():
    out = []
    for num, name, st, sla, what in STAGES:
        out.append('<tr><td class="mono small">' + num + '</td><td><b>' + name + '</b></td>'
                   '<td><span class="pill ' + ('ok' if st == 'done' else 'blue' if st == 'active' else 'gray') + '">' +
                   ('done' if st == 'done' else 'in progress' if st == 'active' else 'not reached') + '</span></td>'
                   '<td class="small">' + sla + '</td><td class="small muted">' + what + '</td></tr>')
    return "\n".join(out)

def rows_playbook():
    out = []
    for clause, ours, fallback, danger in PLAYBOOK:
        out.append('<tr><td><b>' + clause + '</b></td><td class="small">' + ours + '</td>'
                   '<td class="small muted">' + fallback + '</td><td class="small">' + danger + '</td></tr>')
    return "\n".join(out)

def rows_sla():
    out = []
    for item, holder, days, action, cls in SLA:
        out.append('<tr><td>' + item + '</td><td class="small">' + holder + '</td>'
                   '<td class="num"><span class="pill ' + cls + '">' + days + '</span></td>'
                   '<td class="small muted">' + action + '</td></tr>')
    return "\n".join(out)

def rows_instr():
    out = []
    for when, question, explanation, decision, channel in INSTR:
        out.append('<tr><td class="small">' + when + '</td><td>' + question + '</td>'
                   '<td class="small muted">' + explanation + '</td><td>' + decision + '</td>'
                   '<td class="small">' + channel + '</td></tr>')
    return "\n".join(out)

BOARD = [
    ("Drafting with us", [("CV-2026-0142 &mdash; SPA (buyer)", "v0.1 in progress, due in 2 days", "blue")]),
    ("Internal review / approval", [("CV-2026-0171 &mdash; tenancy, office lot", "v0.3 with partner, 1 day", "blue"),
                                    ("CV-2026-0168 &mdash; Deed of Assignment", "peer comments returned", "amber")]),
    ("With the other side", [("CV-2026-0142 &mdash; SPA (buyer)", "day 9 of 14 with seller's solicitors", "amber"),
                             ("CV-2026-0159 &mdash; SPA (seller side)", "day 21 &mdash; formal reminder served", "bad")]),
    ("Vetting and negotiation", [("CV-2026-0142 &mdash; SPA (buyer)", "6 clauses in dispute, 2 need the partner", "amber"),
                                 ("CV-2026-0151 &mdash; facility agreement", "bank clauses accepted, 1 exception logged", "blue")]),
    ("Client approval", [("CV-2026-0142 &mdash; SPA (buyer)", "awaiting instruction on extension request", "warn")]),
    ("Ready for execution", [("CV-2026-0160 &mdash; tenancy", "EV-1 frozen, e-signature envelopes out", "ok"),
                             ("CV-2026-0155 &mdash; developer SPA", "HIMS draft generated, eKYC pending for 1 buyer", "amber")]),
    ("Post-execution", [("CV-2026-0138 &mdash; SPA (seller side)", "stamped 09 Sep, copies distributed", "ok"),
                        ("CV-2026-0147 &mdash; tenancy", "e-Duti Setem certificate filed, closing in 4 days", "ok")]),
]

def board_html():
    out = ['<div class="grid g3">']
    for title, cards in BOARD:
        out.append('<div class="card"><h3 style="margin-top:0">' + title + '<span class="small muted"> &middot; ' + str(len(cards)) + '</span></h3>')
        for name, note, cls in cards:
            out.append('<div class="lg" style="margin-bottom:10px"><div class="ln" style="border:0;padding:0 0 6px"><b class="small">' + name + '</b>'
                       '<span class="pill ' + cls + '">' + ('on track' if cls in ('ok', 'blue') else 'attention') + '</span></div>'
                       '<div class="small muted">' + note + '</div></div>')
        out.append('</div>')
    out.append('</div>')
    return "\n".join(out)

PAGES_D.append(dict(f="drafting.html", t="Drafting and vetting", body=T("".join([
"""@@TOP@@""",
"""    <div class="note warn"><b>This is the part most systems skip.</b> A matter is not a folder with a signed agreement in it. It is a document that passes through fourteen stages, several loops of negotiation, and a client who has to authorise the final terms. The pipeline below is what Zentra Law should enforce, chase and record &mdash; because the two things that cost a firm most are a draft that sits still and a date that passes.</div>
""",
"""    <h2 class="sec"><span class="num">1</span> Where every agreement stands today</h2>
@@BOARD@@
""",
"""    <h2 class="sec"><span class="num">2</span> The fourteen stages, with gates</h2>
    <div class="card">
      <div class="wrap-tbl">
        <table class="tbl">
          <tr><th>#</th><th>Stage</th><th>State on CV-2026-0142</th><th>Target</th><th>What it produces</th></tr>
@@STAGE_ROWS@@
        </table>
      </div>
      <p class="small muted" style="margin-bottom:0">A stage cannot be skipped silently. Where a stage does not apply &mdash; a developer sale has no counterparty negotiation, because the form is fixed by statute &mdash; the system records <i>why</i> it was skipped.</p>
    </div>
""",
"""    <h2 class="sec"><span class="num">3</span> Version trail on one file</h2>
    <div class="card">
      <div class="wrap-tbl">
        <table class="tbl">
          <tr><th>Version</th><th>Date</th><th>What changed</th><th>State</th><th>By</th><th>Seal</th></tr>
@@VERSION_ROWS@@
        </table>
      </div>
      <p class="small muted" style="margin-bottom:0">The execution version is sealed before anyone signs. If a signature is ever questioned, the firm can produce the exact text that was signed, who approved it, and what it looked like before and after &mdash; which is the whole of a negligence defence in one screen.</p>
    </div>
""",
"""    <h2 class="sec"><span class="num">4</span> Negotiation log, clause by clause</h2>
    <div class="card">
      <div class="wrap-tbl">
        <table class="tbl">
          <tr><th>Clause</th><th>Our position</th><th>Fallback we allow</th><th>Other side</th><th>Outcome</th><th>Approved by</th></tr>
@@NEGO_ROWS@@
        </table>
      </div>
      <div class="note warn">Anything beyond the fallback column cannot be accepted by a junior. The system routes it to the partner &mdash; and if the client overrides the advice, the advice and the override are both recorded.</div>
    </div>
""",
"""    <h2 class="sec"><span class="num">5</span> Whose move is it</h2>
    <div class="wrap-tbl card">
      <table class="tbl">
        <tr><th>Outstanding item</th><th>Holding the file</th><th class="num">Days</th><th>Next action</th></tr>
@@SLA_ROWS@@
      </table>
      <p class="small muted" style="margin-bottom:0">Chasers are generated by the system, not remembered by a clerk: reminder at 7 days, second reminder at 14, escalation to the partner at 21.</p>
    </div>
""",
"""    <h2 class="sec"><span class="num">6</span> What the client was told, and what the client decided</h2>
    <div class="wrap-tbl card">
      <table class="tbl">
        <tr><th>Date</th><th>Question</th><th>Advice given</th><th>Client decision</th><th>Channel</th></tr>
@@INSTR_ROWS@@
      </table>
      <p class="small muted" style="margin-bottom:0">This log is the difference between &ldquo;the client never agreed to that&rdquo; and a dated record of the explanation and the instruction. Where a client declines the firm's advice, that too is written down.</p>
    </div>
""",
"""    <h2 class="sec"><span class="num">7</span> Clause playbook &mdash; subsale sale and purchase, acting for the buyer</h2>
    <div class="wrap-tbl card">
      <table class="tbl">
        <tr><th>Clause</th><th>Our position</th><th>Fallback</th><th>Tripwire that must be escalated</th></tr>
@@PLAYBOOK_ROWS@@
      </table>
      <p class="small muted" style="margin-bottom:0">Each firm edits its own playbook. That is what turns a junior's draft into something that reflects the firm's standards &mdash; and what makes the product worth a subscription to a firm that has three lawyers and one partner.</p>
    </div>
""",
"""    <h2 class="sec"><span class="num">8</span> Execution pack and post-execution</h2>
    <div class="grid g2">
      <div class="card"><h3 style="margin-top:0">Execution pack &mdash; CV-2026-0142</h3>
        <ul class="check">
          <li><span class="ok">&#10003;</span><div>Execution version EV-1 sealed, seal 9ad4&hellip;</div></li>
          <li><span class="ok">&#10003;</span><div>4 copies scheduled; 2 for the parties, 1 for the bank, 1 for the file</div></li>
          <li><span class="ok">&#10003;</span><div>Signatories confirmed: buyer, seller, 2 witnesses (independent of the firm)</div></li>
          <li><span class="ok">&#10003;</span><div>Fixtures schedule final and initialled by both sides</div></li>
          <li><span>5</span><div>Attendance sheet and original custody log to be completed at the session</div></li>
        </ul></div>
      <div class="card"><h3 style="margin-top:0">After signing</h3>
        <ul class="check">
          <li><span>1</span><div>Stamp within 30 days through e-Duti Setem in MyTax; certificate filed against the matter</div></li>
          <li><span>2</span><div>Stamped copies distributed to the parties, the bank and the file</div></li>
          <li><span>3</span><div>Present for registration where the matter runs to the land office</div></li>
          <li><span>4</span><div>Close the file only when the certificate and the client's copies are recorded</div></li>
          <li><span>5</span><div>Retention scheduled, then disposal under the firm's policy</div></li>
        </ul></div>
    </div>
""",
"""    <h2 class="sec"><span class="num">9</span> Two 2026 rules the pipeline must obey</h2>
    <div class="grid g2">
      <div class="card"><h3 style="margin-top:0">Developer sales: e-SPA is now mandatory</h3>
        <p class="small muted">For new residential property under the Housing Development Act, execution runs through KPKT's Housing Integrated Management System. The buyer completes identity verification in the iDsaya application, signs digitally under the Digital Signature Act 1997, and the lawyer acts as a digital witness. Stamping follows through LHDN.</p>
        <p class="small muted" style="margin-bottom:0">So the pipeline diverts: no counterparty negotiation (the form is fixed), but a new checklist &mdash; HIMS draft generated, each buyer verified, digital witnessing, certificate captured.</p></div>
      <div class="card"><h3 style="margin-top:0">Tenancy: stamp duty on the full annual rent</h3>
        <table class="tbl">
          <tr><th>Tenancy</th><th>Working</th><th class="num">Duty</th></tr>
          <tr><td>RM1,500 per month, 1 year</td><td>18,000 &divide; 250 = 72 units &times; RM1</td><td class="num">RM72</td></tr>
          <tr><td>RM2,000 per month, 2 years</td><td>24,000 &divide; 250 = 96 units &times; RM3</td><td class="num">RM288</td></tr>
          <tr><td>RM3,000 per month, 2 years, commercial</td><td>36,000 &divide; 250 = 144 units &times; RM3</td><td class="num">RM432</td></tr>
        </table>
        <p class="small muted" style="margin-bottom:0">Rates are RM1, RM3, RM5 and RM7 for each RM250 of annual rent by term. The old RM2,400 deduction was removed by the Finance Act 2024 and must not appear in the engine &mdash; plenty of guides online still show it.</p></div>
    </div>
""",
"""    <p class="foot-note">Zentra Law prototype &middot; Zentra Property Group &middot; English (US) UI &middot; sample data only<br>Drafting and vetting pipeline. Compliance notes are design intent and remain subject to legal review with the subscribing firm's counsel.</p>
"""]))))
