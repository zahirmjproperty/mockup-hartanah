# _f0_e.py — Zentra Law F0: agreement generator (template studio + wizard + validation)
from _f0_common import *
from _f0_a import T

PAGES_E = []

TLIB = [
    ("Engagement letter and costs estimate", "Firm-wide", "v4.2", "S. Ariffin (partner)", "12 Aug 2026", "8 / 8", "live", "ok"),
    ("Tenancy agreement - residential", "Conveyancing", "v6.0", "S. Ariffin (partner)", "02 Sep 2026", "10 / 10", "live", "ok"),
    ("Tenancy agreement - commercial", "Conveyancing", "v3.4", "L. Tan (partner)", "02 Sep 2026", "7 / 7", "live", "ok"),
    ("Sale and purchase agreement - subsale (acts for purchaser)", "Conveyancing", "v9.1", "S. Ariffin (partner)", "28 Aug 2026", "12 / 12", "live", "ok"),
    ("Sale and purchase agreement - subsale (acts for vendor)", "Conveyancing", "v7.3", "S. Ariffin (partner)", "28 Aug 2026", "11 / 11", "live", "ok"),
    ("Sale and purchase agreement - developer (HDA, Schedule G/H)", "Conveyancing", "v2.0", "L. Tan (partner)", "05 Sep 2026", "6 / 6", "live (HIMS e-SPA route)", "ok"),
    ("Deed of assignment (master title)", "Conveyancing", "v5.2", "L. Tan (partner)", "19 Aug 2026", "5 / 5", "live", "ok"),
    ("Discharge of charge", "Conveyancing", "v2.6", "L. Tan (partner)", "19 Aug 2026", "4 / 4", "live", "ok"),
    ("Will (testator with minor children)", "Family and estate", "v1.4", "N. Devi (partner)", "-", "0 / 4", "draft - not approved", "warn"),
    ("Letter of demand", "Litigation", "v0.9", "-", "-", "0 / 3", "parked for phase 4", "gray"),
]

def rows_tlib():
    out = []
    for name, area, ver, owner, approved, tests, status, cls in TLIB:
        out.append('<tr><td><b>' + name + '</b><div class="small muted">' + area + '</div></td>'
                   '<td class="mono small">' + ver + '</td><td class="small">' + owner + '</td>'
                   '<td class="small">' + approved + '</td><td class="small mono">' + tests + '</td>'
                   '<td><span class="pill ' + cls + '">' + status + '</span></td>'
                   '<td class="small"><a href="#">history</a> &middot; <a href="#">tests</a> &middot; <a href="#">use</a></td></tr>')
    return "\n".join(out)

FIELDS = [
    ("Purchaser name", "auto from matter", "Nurul Ain binti Hassan", "text", "ok"),
    ("Purchaser identification", "auto from matter", "900101-14-6078", "ic", "ok"),
    ("Vendor name", "auto from matter", "Tan Wei Ming", "text", "ok"),
    ("Property title", "auto from matter", "Geran 45678, Lot 1234, Mukim Kajang", "text", "ok"),
    ("Purchase price", "typed", "RM650,000.00", "money", "ok"),
    ("Deposit paid on signing", "rule (10%)", "RM65,000.00", "money", "ok"),
    ("Completion date", "rule (SPA + 3 months)", "11 Dec 2026", "date", "ok"),
    ("Financier", "auto from matter", "CIMB Bank Berhad", "text", "ok"),
    ("Late payment interest", "clause library default", "8% per annum", "pct", "ok"),
    ("Chattels and inventory list", "typed (optional)", "Air-conditioners (3 units), kitchen cabinet", "text", "warn"),
]

def rows_fields():
    out = []
    for name, source, value, kind, cls in FIELDS:
        out.append('<tr><td class="small">' + name + '</td><td><span class="pill ' + ('blue' if source.startswith('auto') else ('green' if source.startswith('rule') else 'gray')) + '">' + source + '</span></td>'
                   '<td class="mono small">' + value + '</td><td class="small muted">' + kind + '</td></tr>')
    return "\n".join(out)

CLAUSE_GROUPS = [
    ("Strata management (Act 757) notices and by-laws", "Included", "Property is a stratified parcel", "ok"),
    ("Restriction in interest - state authority consent", "Not included", "Freehold, no restriction", "gray"),
    ("Bumiputera lot release", "Not included", "Not a Bumiputera lot", "gray"),
    ("Existing tenancy - purchaser takes subject to tenancy", "Not included", "Vacant possession", "gray"),
    ("Redemption of existing charge by vendor's financier", "Included", "Charge in favour of Maybank Islamic", "ok"),
    ("Loan rejection - refund of deposit", "Included", "Purchaser financing 80%", "ok"),
    ("Furniture, fittings and chattels", "Included", "Inventory list attached", "warn"),
    ("Late delivery charges (developer only)", "Not applicable", "Not an HDA transaction", "gray"),
]

def rows_clauses():
    out = []
    for name, state, why, cls in CLAUSE_GROUPS:
        out.append('<tr><td class="small">' + name + '</td><td><span class="pill ' + cls + '">' + state + '</span></td><td class="small muted">' + why + '</td></tr>')
    return "\n".join(out)

REDLINE = [
    ("Text diff in the browser", "difflib or diff-match-patch", "Free", "No", "No", "Screen review only"),
    ("LibreOffice unoserver / unocompare", "LibreOffice UNO", "Free (self-hosted)", "Partial", "Yes", "Fallback if native track changes misbehave"),
    ("Native track changes - python-redlines (Docxodus engine)", "Python", "Free (open source)", "High", "Yes - real w:ins / w:del", "Chosen for phase 1"),
    ("Draftable", "Hosted or self-hosted API", "USD129-261 per user per year", "Very high", "Yes", "Later phase if needed"),
    ("Aspose.Words", ".NET / Python / Java SDK", "USD1,000-3,000+ per developer per year; OEM/SaaS from USD10,000+", "Very high", "Yes", "Avoid unless justified"),
]

def rows_redline():
    out = []
    for name, tech, cost, fmt, tc, note in REDLINE:
        out.append('<tr><td class="small"><b>' + name + '</b><div class="small muted">' + tech + '</div></td>'
                   '<td class="small">' + cost + '</td><td class="small">' + fmt + '</td><td class="small">' + tc + '</td>'
                   '<td class="small muted">' + note + '</td></tr>')
    return "\n".join(out)

BODY = "".join([
"""@@TOP@@""",
"""    <div class="note"><b>What this screen proves.</b> A lawyer picks an approved template, the form arrives mostly filled from the matter record, conditional blocks come from the firm's clause library, the validation engine blocks anything that would be wrong on its face, and the document is generated, scanned and watermarked <b>DRAFT</b> until a partner approves it. Nothing leaves the firm without that approval.</div>

    <div class="note warn"><b>Two hard rules of the engine.</b> (1) Placeholders that Word has split across runs must be repaired before generation, or the replacement fails silently and the document goes out with <span class="mono">{{name}}</span> inside it. (2) Every generated document records the template version and the clause set used, so a file signed today can always be reproduced exactly.</div>
""",
"""    <h2 class="sec"><span class="num">1</span> Template studio - the library a firm may draw from</h2>
    <div class="wrap-tbl card">
      <table class="tbl">
        <tr><th style="width:34%">Template</th><th>Version</th><th>Owner</th><th>Approved</th><th>Golden tests</th><th>Status</th><th></th></tr>
@@TLIB_ROWS@@
      </table>
    </div>
    <p class="small muted">Only templates with status <b>live</b> can be generated. A template without an owner, without a passing test set, or without partner approval cannot be promoted - the system simply does not offer it.</p>
""",
"""    <h2 class="sec"><span class="num">2</span> Generate an agreement - the form a clerk sees</h2>
    <div class="grid g2">
      <div class="card">
        <h3 style="margin-top:0">Sale and purchase agreement (subsale, acting for purchaser) <span class="pill blue mono">v9.1</span></h3>
        <p class="small muted">Matter CV-2026-0142. Fields marked <span class="pill blue">auto from matter</span> were filled by the system; only the rest is typed.</p>
        <div class="wrap-tbl">
          <table class="tbl">
            <tr><th>Field</th><th>Source</th><th>Value</th><th>Type</th></tr>
@@FIELD_ROWS@@
          </table>
        </div>
        <div class="hr"></div>
        <h4 style="margin:0 0 8px">Live check - change a value and press generate</h4>
        <div class="grid g2">
          <div class="field"><label>Purchase price (figures)</label><input id="genPrice" value="650000"></div>
          <div class="field"><label>Purchase price (in words)</label><input id="genWords" value="Ringgit Malaysia Six Hundred Fifty Thousand Only"></div>
          <div class="field"><label>Purchaser identification</label><input id="genIc" value="900101-14-6078"></div>
          <div class="field"><label>SPA date</label><input id="genSpa" value="2026-08-12"></div>
          <div class="field"><label>Completion date</label><input id="genComp" value="2026-11-12"></div>
          <div class="field"><label>Late payment interest (% per annum)</label><input id="genInt" value="8"></div>
        </div>
        <div class="chips">
          <label class="chip on" id="chipStrata"><input type="checkbox" checked> Strata title</label>
          <label class="chip" id="chipBumi"><input type="checkbox"> Bumiputera lot</label>
          <label class="chip" id="chipRestrict"><input type="checkbox"> Restriction in interest</label>
        </div>
        <button class="btn gold" id="genBtn" type="button">Generate agreement</button>
        <div class="note" id="genResult" style="margin-top:12px"><b>Ready.</b> Press generate to run the validation engine and assemble the document.</div>
      </div>
      <div class="card">
        <h3 style="margin-top:0">Conditional blocks drawn from the clause library</h3>
        <div class="wrap-tbl">
          <table class="tbl">
            <tr><th>Block</th><th>State</th><th>Why</th></tr>
@@CLAUSE_ROWS@@
          </table>
        </div>
        <div class="hr"></div>
        <h4 style="margin:0 0 8px">Post-generation scan (runs on every output)</h4>
        <ul class="check">
          <li><span class="ok">&#10003;</span><div>No leftover placeholders - scanned for <span class="mono">{{ }}</span>, <span class="mono">{% %}</span>, <span class="mono">XXX</span>, <span class="mono">TBC</span></div></li>
          <li><span class="ok">&#10003;</span><div>Parties named consistently in all 23 references</div></li>
          <li><span class="ok">&#10003;</span><div>Price RM650,000.00 matches the payment schedule and the words</div></li>
          <li><span class="ok">&#10003;</span><div>Inventory list referenced and attached</div></li>
          <li><span>!</span><div>Page range 38 pages - inside the expected band for a subsale SPA</div></li>
        </ul>
        <div class="hr"></div>
        <h4 style="margin:0 0 8px">Output package</h4>
        <div class="grid g2">
          <div class="kpi"><div class="lab">For review</div><div class="val small">DOCX</div><div class="sub">track changes on, watermark DRAFT</div></div>
          <div class="kpi"><div class="lab">For signature</div><div class="val small">PDF</div><div class="sub">wet ink only for this document</div></div>
          <div class="kpi"><div class="lab">For archive</div><div class="val small">PDF/A</div><div class="sub">with template version and hash</div></div>
          <div class="kpi blue"><div class="lab">Evidence</div><div class="val small">sealed</div><div class="sub">who generated, when, from which version</div></div>
        </div>
      </div>
    </div>
""",
"""    <h2 class="sec"><span class="num">3</span> Validation engine - the 40 rules that make this a legal tool</h2>
    <div class="grid g2">
      <div class="card">
        <h3 style="margin-top:0">Hard blocks (the document cannot be generated)</h3>
        <ul class="check">
          <li><span class="bad">&#10007;</span><div>Price in figures does not match the price in words</div></li>
          <li><span class="bad">&#10007;</span><div>Completion date is not the SPA date plus three months</div></li>
          <li><span class="bad">&#10007;</span><div>Identification number fails format or check digit</div></li>
          <li><span class="bad">&#10007;</span><div>Strata property on a landed template, or the reverse</div></li>
          <li><span class="bad">&#10007;</span><div>Restriction in interest present but no state consent clause</div></li>
          <li><span class="bad">&#10007;</span><div>Existing charge with no redemption clause</div></li>
          <li><span class="bad">&#10007;</span><div>Instrument of transfer or charge routed to e-signature</div></li>
          <li><span class="bad">&#10007;</span><div>Developer SPA outside the HIMS e-SPA route</div></li>
        </ul>
      </div>
      <div class="card">
        <h3 style="margin-top:0">Warnings (a partner must acknowledge, with a reason)</h3>
        <ul class="check">
          <li><span>!</span><div>Late payment interest outside the firm's 8-10% band</div></li>
          <li><span>!</span><div>No chattels and inventory list although the offer letter promised fittings</div></li>
          <li><span>!</span><div>No loan rejection clause although the purchaser is financing</div></li>
          <li><span>!</span><div>Taxes and assessment apportionment missing or ambiguous</div></li>
          <li><span>!</span><div>Extension period exists but the extension interest rate is blank</div></li>
          <li><span>!</span><div>Discount on scale fees exceeds the firm's policy</div></li>
        </ul>
        <p class="small muted" style="margin-bottom:0">Every acknowledgement is recorded: who accepted it, when, and why. Silence is never consent.</p>
      </div>
    </div>
""",
"""    <h2 class="sec"><span class="num">4</span> Comparing the other side's mark-up</h2>
    <div class="wrap-tbl card">
      <table class="tbl">
        <tr><th style="width:32%">Option</th><th>Cost</th><th>Keeps formatting</th><th>Exports tracked changes</th><th>Note</th></tr>
@@REDLINE_ROWS@@
      </table>
    </div>
    <div class="note"><b>Why this matters.</b> The point of automatic comparison is not convenience - it is detection. If the other side edits text without turning tracked changes on, the firm still sees every change, in writing, on the record.</div>
""",
"""    <h2 class="sec"><span class="num">5</span> Artificial intelligence - what it may and may not do</h2>
    <div class="grid g3">
      <div class="card"><h3 style="margin-top:0;font-size:15px">May</h3><ul class="check small">
        <li><span class="ok">&#10003;</span><div>Suggest a clause from the firm's own approved library</div></li>
        <li><span class="ok">&#10003;</span><div>Summarise the other side's mark-up into a one-page list</div></li>
        <li><span class="ok">&#10003;</span><div>Explain a clause to the client in plain language</div></li>
      </ul></div>
      <div class="card"><h3 style="margin-top:0;font-size:15px">May not</h3><ul class="check small">
        <li><span class="bad">&#10007;</span><div>Write a clause that is not in the approved library, unattended</div></li>
        <li><span class="bad">&#10007;</span><div>Send anything to a client, the other side or the land office</div></li>
        <li><span class="bad">&#10007;</span><div>Be used to train a model on client documents</div></li>
      </ul></div>
      <div class="card"><h3 style="margin-top:0;font-size:15px">Controls</h3><ul class="check small">
        <li><span class="ok">&#10003;</span><div>Per-firm off switch - some bank panels forbid external AI</div></li>
        <li><span class="ok">&#10003;</span><div>Every use logged: who, when, model, output, decision</div></li>
        <li><span class="ok">&#10003;</span><div>Bar Council Circular 242/2025 and the 2025 update built into the policy text</div></li>
      </ul></div>
    </div>
    <div class="note warn"><b>The rule behind the rule.</b> A lawyer's professional judgement cannot be delegated to software. The system is a drafting assistant that never becomes the lawyer of record.</div>
""",
"""    <h2 class="sec"><span class="num">6</span> What the firm gets on day one</h2>
    <div class="grid g4">
      <div class="kpi"><div class="lab">Fields auto-filled</div><div class="val">70%</div><div class="sub">straight from the matter record</div></div>
      <div class="kpi"><div class="lab">First draft in</div><div class="val">&lt; 2 min</div><div class="sub">against 2-4 hours by hand</div></div>
      <div class="kpi"><div class="lab">Templates at launch</div><div class="val">10</div><div class="sub">conveyancing set first</div></div>
      <div class="kpi warn"><div class="lab">Approval gate</div><div class="val">Always</div><div class="sub">no partner, no release</div></div>
    </div>
    <div class="card" style="margin-top:16px">
      <h3 style="margin-top:0">How the ten minutes are spent now</h3>
      <p class="small muted">Open the matter, press generate agreement, glance at the validation panel, fix the two typed fields, read the assembled outline block by block, send for partner review. The clerk no longer copies last month's file and hunts for names to change - which is exactly where the errors used to live.</p>
    </div>
""",
])

PAGES_E.append(dict(f="generator.html", t="Agreement generator", body=T(BODY)))
