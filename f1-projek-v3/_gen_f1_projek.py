#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""F1 — Halaman projek ZAFA/Zentra Sales Suite v3 (PRATONTON) + borang EOI RM0.
Sumber fakta: ~/mrtanah-site/data/projek-baharu.json (Notion 'Projek Baharu MT').
Hantar ke: ~/mockup-hartanah/f1-projek-v3/ (noindex, pratonton untuk kelulusan Zahir).
Borang EOI → webhook portal MT (aksi form=eoi) → Sheet 'EOI Projek Baharu MT'.
"""
import json, html, os, datetime

SRC = "/home/ubuntu/mrtanah-site/data/projek-baharu.json"
OUT = "/home/ubuntu/mockup-hartanah/f1-projek-v3"
WH = "https://script.google.com/macros/s/AKfycbwafaViIuCpc-Q0XnUpSHgkKVTFcyfPProf0GvSi9C-L22hUsZ_NA-03wXjd2F-GRIS/exec"
WA = "60163119076"
TODAY = datetime.date.today().strftime("%d/%m/%Y")
os.makedirs(OUT, exist_ok=True)

CSS = """
:root{--hijau:#0E4B3C;--hijau2:#12604A;--emas:#C9A227;--bg:#F6F8F6;--line:#DCE4DE;--txt:#1B2521;--mut:#5C6A63}
*{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',system-ui,-apple-system,sans-serif;color:var(--txt);background:var(--bg);line-height:1.6}
.pv{background:#1B2521;color:#fff;font-size:12.5px;text-align:center;padding:7px 14px}
.pv b{color:var(--emas)}
header{background:linear-gradient(135deg,var(--hijau),var(--hijau2));color:#fff;padding:16px 22px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px}
header .b{font-weight:700;letter-spacing:.3px}header .b span{color:var(--emas)}
header a{color:#fff;text-decoration:none;font-size:14px;opacity:.9}
.wrap{max-width:980px;margin:0 auto;padding:22px 18px 60px}
h1{font-size:clamp(22px,3.4vw,32px);margin:14px 0 4px;line-height:1.25}
.sub{color:var(--mut);margin:0 0 18px;font-size:15px}
.card{background:#fff;border:1px solid var(--line);border-radius:14px;padding:18px;margin:16px 0}
.card h2{font-size:17px;margin:0 0 12px;color:var(--hijau)}
table{width:100%;border-collapse:collapse;font-size:14.5px}
td{padding:7px 8px;border-bottom:1px solid var(--line);vertical-align:top}
td:first-child{color:var(--mut);width:42%}
.pill{display:inline-block;background:#EAF3EE;color:var(--hijau);border-radius:999px;padding:2px 10px;font-size:12px;font-weight:600}
.pill.w{background:#FDF3E0;color:#8a5b00}.pill.r{background:#FDECEC;color:#a12a2a}
.kpi{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px}
.kpi div{background:#F1F6F2;border-radius:10px;padding:12px}
.kpi b{display:block;font-size:19px;color:var(--hijau)}
.kpi span{font-size:12.5px;color:var(--mut)}
form label{display:block;font-size:13.5px;font-weight:600;margin:10px 0 4px}
input,select,textarea{width:100%;padding:10px 11px;border:1px solid var(--line);border-radius:9px;font-size:15px;font-family:inherit}
.row{display:grid;grid-template-columns:1fr 1fr;gap:12px}
@media(max-width:640px){.row{grid-template-columns:1fr}}
.consent{display:flex;gap:9px;align-items:flex-start;margin:14px 0;font-size:13.5px;color:var(--mut)}
.consent input{width:17px;height:17px;flex:0 0 auto;margin-top:3px}
button{background:var(--emas);color:#1B2521;border:0;border-radius:10px;padding:13px 20px;font-size:15.5px;font-weight:700;cursor:pointer;width:100%}
button:disabled{opacity:.6;cursor:not-allowed}
.msg{margin-top:12px;padding:12px;border-radius:10px;font-size:14.5px;display:none}
.msg.ok{background:#EAF3EE;color:#0E4B3C;display:block}
.msg.err{background:#FDECEC;color:#7d2020;display:block}
.note{background:#FDF9EC;border-left:4px solid var(--emas);padding:12px 14px;border-radius:8px;font-size:14px;margin:14px 0}
.warn{background:#FDECEC;border-left:4px solid #a12a2a;padding:12px 14px;border-radius:8px;font-size:14px;margin:14px 0}
a.wa{display:inline-block;background:#25D366;color:#fff;text-decoration:none;padding:11px 16px;border-radius:10px;font-weight:600;margin-top:8px}
footer{border-top:1px solid var(--line);margin-top:26px;padding-top:16px;font-size:12.5px;color:var(--mut)}
"""

HR = ""

def esc(s):
    return html.escape(str(s if s is not None else ""))

def galeri_link(slug):
    return ""

def eoi_form(p):
    jenis = "".join('<option>%s</option>' % esc(u.get("kod", "")) for u in (p.get("unit_list") or []))
    return """
    <div class="card" id="eoi">
      <h2>Register your interest — RM0 (no payment)</h2>
      <div class="note"><b>No money is collected at this stage.</b> Under Regulation 11(2) of the Housing
      Development (Control &amp; Licensing) Regulations 1989, no payment may be taken before the Sale &amp;
      Purchase Agreement (SPA) is signed. Your interest is logged with a queue reference only; the 10%
      deposit is paid <b>after</b> the SPA is signed, into the developer's Housing Development Account.</div>
      <form id="eoiForm">
        <input type="text" name="website" style="display:none" tabindex="-1" autocomplete="off">
        <div class="row">
          <div><label>Full name *</label><input name="nama" required minlength="2" placeholder="As per MyKad"></div>
          <div><label>WhatsApp number *</label><input name="wa" required placeholder="0123456789" inputmode="tel"></div>
        </div>
        <div class="row">
          <div><label>Email (optional)</label><input name="emel" type="email" placeholder="name@email.com"></div>
          <div><label>Unit type you prefer</label><select name="jenis_unit"><option value="">Not sure yet</option>__JENIS__</select></div>
        </div>
        <div class="row">
          <div><label>Budget (RM)</label><input name="bajet" inputmode="numeric" placeholder="e.g. 800000"></div>
          <div><label>Preferred contact</label><select name="kaedah"><option>WhatsApp</option><option>Phone call</option><option>Email</option></select></div>
        </div>
        <div class="consent">
          <input type="checkbox" name="consent" required>
          <span>I agree that my details are stored and used to follow up on this enquiry (Personal Data Protection Act 2010).
          Data is handled by the system operator and is not sold to third parties.</span>
        </div>
        <button type="submit" id="eoiBtn">Submit interest (RM0)</button>
        <div class="msg" id="eoiMsg"></div>
      </form>
      <p style="font-size:13px;color:#5C6A63;margin:12px 0 0">Prefer to talk first?
      <a href="https://wa.me/__WA__?text=__WATEXT__" target="_blank" rel="noopener">WhatsApp us</a>.</p>
    </div>"""

def page(p, indeks):
    unit_rows = "".join(
        "<tr><td>%s</td><td>%s · %s · %s · %s</td></tr>" % (
            esc(u.get("kod", "")), esc(u.get("kps", "")), esc(u.get("bilik", "")),
            esc(u.get("kereta", "")) + (" park" if u.get("kereta") else ""), esc(u.get("harga", "")))
        for u in (p.get("unit_list") or []))
    sempadan = "".join(
        "<tr><td>%s</td><td>%s</td></tr>" % (esc(x[0]), esc(x[1])) for x in [
            ("Project name", p.get("nama")),
            ("Licensed developer", p.get("pemaju")),
            ("Developer licence no.", p.get("pemaju_lesen_no")),
            ("Advertising &amp; selling permit", p.get("permit_iklan_no")),
            ("Local authority", p.get("pbt")),
            ("Plan reference", p.get("pbt_rujukan_pelan")),
            ("Expected completion", p.get("dijangka_siap")),
            ("Tenure", p.get("pegangan")),
            ("Restrictions", p.get("sekatan")),
            ("Total units", p.get("bilangan_unit")),
            ("Phase status", p.get("status_fasa")),
            ("Construction update", p.get("status_pembinaan")),
        ])
    # gate permit: 4 medan wajib
    wajib = [p.get("pemaju_lesen_no"), p.get("permit_iklan_no"), p.get("pbt_rujukan_pelan"), p.get("bilangan_unit")]
    lengkap = all(bool(str(x or "").strip()) for x in wajib)
    gate = ('<div class="note"><b>Permit data complete.</b> Developer licence and advertising &amp; selling permit '
            'details are shown above (Regulation 6).</div>' if lengkap else
            '<div class="warn"><b>Permit data incomplete.</b> This page stays out of Google until the developer '
            'licence and advertising &amp; selling permit details are confirmed (Regulation 6).</div>')
    body = """<!doctype html><html lang="en-US"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>__NAMA__ — ZAFA Sales Suite (preview)</title><style>__CSS__</style></head><body>
<div class="pv">PRATONTON FASA 1 — noindex · data permit sebenar · borang EOI berfungsi (ujian) · belum diterbitkan ke mrtanah.com</div>
<header><div class="b">ZENTRA <span>SALES SUITE</span></div>
<div><a href="index.html">All projects</a> · <a href="https://wa.me/__WA__" target="_blank" rel="noopener">WhatsApp</a></div></header>
<div class="wrap">
<h1>__NAMA__</h1>
<p class="sub">__LOKASI__, __NEGERI__ · __JENIS__ · __KPS__ · __HARGA__</p>
<div class="kpi">
  <div><b>__UNIT__</b><span>units (permit phase)</span></div>
  <div><b>__SELESAI__</b><span>expected completion</span></div>
  <div><b>__PEGANGAN__</b><span>tenure</span></div>
  <div><b>__STATUS__</b><span>phase status</span></div>
</div>
__GATE__
<div class="card"><h2>Availability snapshot</h2>
<div class="note"><b>Phase-level availability only.</b> Unit-by-unit inventory is not yet published: it is not
released by the developer and there is no sales-gallery figure confirmed for today. Availability shown here is
a phase indicator, refreshed __TARIKH__; unit-level availability must be confirmed with the sales gallery
before any booking. The zero-deposit interest list below secures your place in the queue — it does not hold a
specific unit.</div>
<table><tr><td>Permitted phase</td><td>__FASA__</td></tr>
<tr><td>Overall take-up (as reported)</td><td>__PEMBINAAN__</td></tr>
<tr><td>Unit types &amp; price list (permit)</td><td>__UNITLIST__</td></tr></table></div>
<div class="card"><h2>Facts &amp; compliance</h2><table>__SEMpadan__</table></div>
<div class="card"><h2>Unit types and permit price range</h2><table>__UNITROWS__</table>
<p style="font-size:13.5px;color:#5C6A63;margin:10px 0 0">Prices are the developer's permitted list prices. Any
rebate or package must be declared in the SPA — ask us for the current written offer.</p></div>
__BORANG__
<div class="card"><h2>What happens next</h2><ol>
<li><b>Submit this form (RM0)</b> — you get a queue reference by WhatsApp/email.</li>
<li><b>Talk to an agent</b> — project briefing, showroom appointment, unit availability check.</li>
<li><b>Confirm the unit</b> — when you are ready, a temporary lock is placed on that unit. Still no money.</li>
<li><b>Sign the SPA</b> — digital SPA through KPKT HIMS with eKYC and e-stamping; the 10% deposit is then paid to the developer's Housing Development Account.</li>
<li><b>Financing</b> — apply to your chosen bank; the system tracks submission, consent and approval.</li>
<li><b>Construction &amp; billing</b> — milestone billing per the Third Schedule, visible in your portal.</li>
<li><b>Vacant possession</b> — handover, defect list, defects-liability period.</li>
</ol></div>
<footer>Preview prepared for Zahir MJ (Mr Tanah) — internal admin. Client-facing brand: Zentra Property Group.
This page is a design proposal and is not linked from the live site. Project facts are real; unit inventory is a
phase-level indicator until the developer releases it.<br>System generated __TARIKH__.</footer>
</div>
<script>
(function(){
  var WH="__WH__", form=document.getElementById('eoiForm'), btn=document.getElementById('eoiBtn'), box=document.getElementById('eoiMsg');
  function show(ok,t){box.className='msg '+(ok?'ok':'err');box.textContent=t;if(ok)box.innerHTML=t;}
  form.addEventListener('submit', async function(ev){
    ev.preventDefault(); btn.disabled=true; btn.textContent='Submitting...';
    var f=new FormData(form);
    var payload={form:'eoi',nama:f.get('nama'),wa:f.get('wa'),emel:f.get('emel')||'',projek:"__NAMA__",slug:"__SLUG__",
      jenis_unit:f.get('jenis_unit')||'',bajet:f.get('bajet')||'',kaedah:f.get('kaedah'),sumber:location.pathname,
      consent:f.get('consent')?'YA':'',website:f.get('website')||''};
    try{
      var r=await fetch(WH,{method:'POST',headers:{'Content-Type':'text/plain;charset=utf-8'},body:JSON.stringify(payload)});
      var d=await r.json();
      if(d.ok){ show(true,'<b>Received — reference '+d.ref+'</b><br>No payment was taken. An agent will contact you within 24 hours (office hours).'); form.reset(); }
      else { show(false,'⚠️ '+(d.error||'Submission failed. Please try again or WhatsApp us.')); }
    }catch(e){ show(false,'⚠️ Network error — please WhatsApp us instead.'); }
    btn.disabled=false; btn.textContent='Submit interest (RM0)';
  });
})();
</script>
</body></html>"""
    b = body
    for k, v in [("__CSS__", CSS), ("__NAMA__", esc(p.get("nama"))), ("__LOKASI__", esc(p.get("lokasi"))),
                 ("__NEGERI__", esc(p.get("negeri"))), ("__JENIS__", esc(p.get("jenis"))),
                 ("__KPS__", esc(p.get("kps"))), ("__HARGA__", esc(p.get("harga_label"))),
                 ("__UNIT__", esc(p.get("bilangan_unit"))), ("__SELESAI__", esc(p.get("dijangka_siap"))),
                 ("__PEGANGAN__", esc((p.get("pegangan") or "—").split("—")[0].strip())),
                 ("__STATUS__", esc(p.get("status_fasa"))), ("__FASA__", esc(p.get("bilangan_unit"))),
                 ("__PEMBINAAN__", esc(p.get("status_pembinaan"))),
                 ("__UNITLIST__", esc(", ".join(u.get("kod", "") for u in (p.get("unit_list") or [])))),
                 ("__GATE__", gate), ("__SEMpadan__", sempadan), ("__UNITROWS__", unit_rows),
                 ("__TARIKH__", TODAY), ("__WA__", WA), ("__WH__", WH), ("__SLUG__", esc(p.get("slug")))]:
        b = b.replace(k, v)
    b = b.replace("__BORANG__", eoi_form(p).replace("__JENIS__", jenis_options(p))
                  .replace("__WA__", WA)
                  .replace("__WATEXT__", esc("Saya berminat dengan " + str(p.get("nama"))).replace(" ", "%20")))
    return b

def jenis_options(p):
    return "".join("<option>%s</option>" % esc(u.get("kod", "")) for u in (p.get("unit_list") or []))

def index_page(proj):
    kad = ""
    for p in proj:
        kad += """<div class="card"><h2>%s</h2>
        <p class="sub" style="margin:0 0 8px">%s, %s · %s · %s</p>
        <p style="font-size:14px;margin:0 0 10px">Permit iklan: %s</p>
        <a href="%s.html">Buka halaman projek (v3 + EOI RM0) →</a></div>""" % (
            esc(p.get("nama")), esc(p.get("lokasi")), esc(p.get("negeri")), esc(p.get("jenis")),
            esc(p.get("harga_label")), esc(p.get("permit_iklan_no")), esc(p.get("slug")))
    return """<!doctype html><html lang="en-US"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">
<title>Fasa 1 — projek baharu (pratonton)</title><style>%s</style></head><body>
<div class="pv">PRATONTON FASA 1 — noindex · borang EOI RM0 berfungsi · belum terbit ke mrtanah.com</div>
<header><div class="b">ZENTRA <span>SALES SUITE</span></div><div>Phase 1 preview</div></header>
<div class="wrap">
<h1>Fasa 1 — daftar projek &amp; EOI RM0</h1>
<p class="sub">Setiap halaman: panel permit iklan (Peraturan 6) · ringkasan ketersediaan · borang daftar minat RM0
(tiada medan bayaran) · langkah susulan yang telus. Data permit adalah sebenar; inventori unit masih peringkat fasa.</p>
%s
<footer>Disediakan untuk Zahir MJ (Mr Tanah) — pratonton reka bentuk, tiada pautan dari laman sebenar.</footer>
</div></body></html>""" % (CSS, kad)

d = json.load(open(SRC, encoding="utf-8"))
proj = d.get("projek", []) if isinstance(d, dict) else d
for p in proj:
    open(os.path.join(OUT, p["slug"] + ".html"), "w", encoding="utf-8").write(page(p, proj.index(p)))
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(index_page(proj))
print("Siap:", len(proj), "halaman projek + index di", OUT)
