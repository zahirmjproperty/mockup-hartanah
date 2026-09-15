#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Jana POC (mock-up) Sistem Jualan Projek Baharu (SJPB) untuk Mr Tanah.
Lokasi: ~/mockup-hartanah/sjpb-poc/  (noindex, pratonton sahaja)
Fakta projek = data sebenar (Avalon @ Cybersouth); data unit/EOI/komisen = CONTOH struktur.
"""
import os

OUT = os.path.expanduser("~/mockup-hartanah/sjpb-poc")
os.makedirs(OUT, exist_ok=True)

CSS = """
:root{--emerald:#125C4A;--emerald-d:#0C4437;--gold:#C9A227;--bg:#F5F8F6;--card:#fff;
--ink:#132A24;--muted:#5D6F69;--line:#DCE5E0;--blue:#1B5E9B;--amber:#B7791F;--red:#9B2C2C;--green:#276749;}
*{box-sizing:border-box}
body{margin:0;font-family:"Plus Jakarta Sans",-apple-system,"Segoe UI",Roboto,Arial,sans-serif;
background:var(--bg);color:var(--ink);font-size:15px;line-height:1.55}
.mockbar{background:var(--gold);color:#1a1a1a;padding:8px 14px;font-size:13px;font-weight:600;text-align:center}
header.top{background:var(--emerald);color:#fff;padding:18px 20px 14px}
header.top h1{margin:0 0 4px;font-size:20px;letter-spacing:-.2px}
header.top p{margin:0;opacity:.86;font-size:13px}
nav.crumb{background:var(--emerald-d);padding:8px 20px;display:flex;flex-wrap:wrap;gap:6px}
nav.crumb a{color:#DFF3EC;text-decoration:none;font-size:12.5px;padding:5px 10px;border-radius:999px;border:1px solid rgba(255,255,255,.18)}
nav.crumb a:hover{background:rgba(255,255,255,.14)}
nav.crumb a.on{background:var(--gold);color:#14261f;border-color:var(--gold);font-weight:700}
main{max-width:1180px;margin:0 auto;padding:22px 18px 60px}
h2{font-size:19px;margin:26px 0 10px;color:var(--emerald-d)}
h3{font-size:16px;margin:18px 0 8px}
p{margin:8px 0}
.muted{color:var(--muted)}
.grid{display:grid;gap:14px}
.g2{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}
.g3{grid-template-columns:repeat(auto-fit,minmax(230px,1fr))}
.g4{grid-template-columns:repeat(auto-fit,minmax(180px,1fr))}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px}
.card h3{margin-top:0}
.kpi{background:#fff;border:1px solid var(--line);border-left:4px solid var(--emerald);border-radius:12px;padding:12px 14px}
.kpi .n{font-size:23px;font-weight:800;color:var(--emerald-d)}
.kpi .l{font-size:12.5px;color:var(--muted)}
table{width:100%;border-collapse:collapse;background:#fff;font-size:13.5px;border:1px solid var(--line);border-radius:10px;overflow:hidden}
th,td{padding:9px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
th{background:#EDF3F0;font-size:12.5px;text-transform:uppercase;letter-spacing:.03em;color:#3E544D}
tr:last-child td{border-bottom:none}
.pill{display:inline-block;padding:2px 9px;border-radius:999px;font-size:11.5px;font-weight:700;white-space:nowrap}
.p-ok{background:#E6F5EC;color:var(--green)}
.p-warn{background:#FFF3D6;color:var(--amber)}
.p-bad{background:#FDE7E7;color:var(--red)}
.p-eoi{background:#EAF1FB;color:var(--blue)}
.p-kunci{background:#FFF3D6;color:var(--amber)}
.p-tempah{background:#FDE7E7;color:var(--red)}
.p-dijual{background:#E4E9E7;color:#4A5B55}
.btn{display:inline-block;background:var(--emerald);color:#fff;text-decoration:none;padding:9px 16px;border-radius:999px;font-weight:700;font-size:13.5px;border:none;cursor:pointer}
.btn.gold{background:var(--gold);color:#1a1a1a}
.btn.ghost{background:#fff;color:var(--emerald);border:1px solid var(--emerald)}
.note{background:#FFFBF0;border:1px solid #EFE0B8;border-left:4px solid var(--gold);border-radius:10px;padding:12px 14px;font-size:13.5px}
.warn{background:#FDF3F3;border:1px solid #F0D2D2;border-left:4px solid var(--red);border-radius:10px;padding:12px 14px;font-size:13.5px}
.ok{background:#EFF8F2;border:1px solid #CFE6D8;border-left:4px solid var(--green);border-radius:10px;padding:12px 14px;font-size:13.5px}
code{background:#EDF3F0;padding:1px 6px;border-radius:6px;font-size:12.5px}
label{display:block;font-size:12.5px;font-weight:700;color:#3E544D;margin:10px 0 4px}
input,select{width:100%;padding:9px 10px;border:1px solid var(--line);border-radius:9px;font-family:inherit;font-size:14px;background:#fff}
.lbl{color:var(--muted);font-weight:700;font-size:12px}
.stack{display:grid;grid-template-columns:190px repeat(10,1fr);gap:4px;align-items:center;font-size:12px}
.u{padding:7px 0;text-align:center;border-radius:6px;font-weight:700;border:1px solid transparent}
.u.t{background:#E6F5EC;color:#276749}
.u.e{background:#EAF1FB;color:#1B5E9B}
.u.k{background:#FFF3D6;color:#8A6116}
.u.b{background:#FDE7E7;color:#9B2C2C}
.u.d{background:#E4E9E7;color:#5C6B66}
.u.bumi{outline:2px dashed #7C4DBE;outline-offset:-2px}
.legend{display:flex;gap:14px;flex-wrap:wrap;font-size:12.5px;color:var(--muted);margin:8px 0 0}
.sq{width:13px;height:13px;border-radius:4px;display:inline-block;vertical-align:-2px;margin-right:5px}
footer{border-top:1px solid var(--line);margin-top:36px;padding-top:14px;font-size:12.5px;color:var(--muted)}
.flow{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:12px;white-space:pre;overflow-x:auto}
@media(max-width:900px){.stack{grid-template-columns:120px repeat(10,1fr);font-size:11px}}
"""

NAV = [
    ("index.html", "Hub SJPB"),
    ("mikrosait-projek.html", "A · Muka Awam"),
    ("unit-lock.html", "B · Kunci Unit"),
    ("ejen.html", "B · Dashboard Ejen"),
    ("papan-jualan.html", "C · Papan Jualan"),
    ("bil-komisen.html", "D · Bil & Komisen"),
    ("pematuhan.html", "E · Pematuhan & Audit"),
    ("reka-bentuk.html", "Reka Bentuk & Peta Jalan"),
]


def page(fn, title, sub, body):
    navs = []
    for h, t in NAV:
        cls = "on" if h == fn else ""
        navs.append('<a href="%s" class="%s">%s</a>' % (h, cls, t))
    bar = ('<div class="mockbar">MOCK-UP / PRATONTON — <b>bukan sistem sebenar</b>. '
           'Fakta projek = data sebenar (Notion/laporan pemaju); data unit, EOI, komisen = '
           '<b>CONTOH struktur</b> kerana inventori unit MT belum wujud. noindex.</div>')
    html = ("<!DOCTYPE html>\n<html lang=\"ms\"><head>\n"
            "<meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
            "<meta name=\"robots\" content=\"noindex,nofollow\">\n"
            "<title>" + title + " — POC SJPB (mock-up)</title>\n"
            "<link rel=\"stylesheet\" href=\"sjpb.css\">\n</head><body>\n" + bar +
            "\n<header class=\"top\"><h1>" + title + "</h1><p>" + sub + "</p></header>\n"
            "<nav class=\"crumb\">" + "".join(navs) + "</nav>\n<main>\n" + body +
            "\n<footer>POC Sistem Jualan Projek Baharu (SJPB) — Mr Tanah / ZMJ Solutions · 15 Sept 2026 · noindex. "
            "Kajian penuh: <code>~/zmp-docs/kajian/kajian-sistem-jualan-projek-baharu-mt-2026-09-15.md</code> (+PDF). "
            "Reka bentuk menunggu kelulusan Zahir sebelum sebarang pelaksanaan ke produksi.</footer>\n"
            "</main></body></html>")
    with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
        f.write(html)
    return fn


def table(headers, rows):
    th = "".join("<th>" + h + "</th>" for h in headers)
    tr = []
    for r in rows:
        tr.append("<tr>" + "".join("<td>" + c + "</td>" for c in r) + "</tr>")
    return "<table><thead><tr>" + th + "</tr></thead><tbody>" + "".join(tr) + "</tbody></table>"


P = {'nama': 'Avalon @ Cybersouth',
     'pemaju': 'Ecolake Residence Sdn Bhd (Avaland Berhad)',
     'dl': '30240/10-2027/0239(A) — sah 12/10/2022 – 11/10/2027',
     'permit': '30240-3/07-2028/0539(N)-(S) — sah 07/07/2025 – 06/07/2028',
     'pbt': 'Majlis Perbandaran Sepang (MP Sepang)',
     'pelan': 'MPSEPANG 600-34/4/316(7)',
     'lokasi': 'Cybersouth, Dengkil',
     'jenis': 'Rumah Teres 2 Tingkat (strata)',
     'unit': '343 unit (fasa berpermit: 166 unit)',
     'pegangan': 'Pajakan 82 tahun — tamat 14 November 2104',
     'siap': 'Julai 2028',
     'harga': 'Dari RM803,800',
     'harga_senarai': 'Senarai berpermit RM1,004,750 – RM1,856,000'}

open(os.path.join(OUT, "sjpb.css"), "w", encoding="utf-8").write(CSS)

# ============================================================ HUB
idx_note = ('<div class="note"><b>Ini POC reka bentuk sistem, bukan laman jualan.</b> Tujuannya: Zahir boleh '
            '<b>klik &amp; uji</b> aliran sebelum sebarang kod produksi dibina — selaras peraturan MT '
            '(mock-up/preview dahulu). Fakta projek (permit, lesen, harga senarai) adalah <b>sebenar</b>; '
            'data peringkat unit/EOI/komisen ditanda <b>CONTOH</b> jujur kerana inventori unit MT belum ada.</div>')

idx_cards = ('<div class="grid g3">'
             '<div class="card"><h3>A · Muka Awam</h3><p class="muted">Mikrosait projek: ketersediaan unit agregat, '
             '<b>EOI RM0</b>, kalkulator ansuran, panel permit iklan &amp; jualan, AI Ali, WhatsApp.</p>'
             '<a class="btn" href="mikrosait-projek.html">Buka →</a></div>'
             '<div class="card"><h3>B · Muka Ejen</h3><p class="muted">Kunci unit bertempoh + buffer, EOI ditugaskan, '
             'pek tempahan (RM0), status pinjaman, komisen berperingkat.</p>'
             '<a class="btn" href="unit-lock.html">Kunci unit →</a> <a class="btn ghost" href="ejen.html">Ejen →</a></div>'
             '<div class="card"><h3>C · Muka MT / Pemaju</h3><p class="muted">Papan jualan (take-up per blok/jenis), '
             'funnel, halangan pinjaman, prestasi ejen.</p><a class="btn" href="papan-jualan.html">Buka →</a></div>'
             '<div class="card"><h3>D · Bil &amp; Komisen</h3><p class="muted">Jadual Ketiga (10% → 15% → … → VP → MOT → '
             'pegangan amanah), gate sijil arkitek, e-invois, komisen dilepas berperingkat.</p>'
             '<a class="btn" href="bil-komisen.html">Buka →</a></div>'
             '<div class="card"><h3>E · Pematuhan &amp; Audit</h3><p class="muted">Gate APDL/DL, status eSPA/HIMS, '
             'consent PDPA, jejak audit, unit Bumi.</p><a class="btn" href="pematuhan.html">Buka →</a></div>'
             '<div class="card"><h3>Reka Bentuk &amp; Peta Jalan</h3><p class="muted">6 lapisan seni bina, model data, '
             '12 aliran, 5 fasa pelaksanaan.</p><a class="btn" href="reka-bentuk.html">Buka →</a></div></div>')

idx_prinsip = ('<div class="grid g3">'
               '<div class="card"><h3>Tiada wang pelanggan di MT</h3><p class="warn">Peraturan 11(2) HDR 1989 '
               '(diperketat P.U.(A) 106/2015): <b>tiada sesiapa — termasuk ejen atau peguam — boleh mengutip '
               'apa-apa bayaran dengan nama apa pun sebelum SPA ditandatangani.</b> Sebab itu modul tempahan MT = '
               '<b>EOI RM0</b>; 10% hanya selepas eSPA, masuk akaun HDA pemaju.</p></div>'
               '<div class="card"><h3>Satu unit, satu kunci</h3><p>Kunci bertempoh (<code>timeLock</code>) + '
               '<b>buffer</b> selepas tamat + jejak siapa/kunci bila. Ini menghapuskan masalah klasik '
               '“tiga ejen janji unit yang sama di bilik pameran”.</p></div>'
               '<div class="card"><h3>Permit = gate automatik</h3><p>Halaman projek hanya terbit &amp; boleh diindeks '
               'jika <b>Lesen Pemaju + Permit Iklan &amp; Jualan</b> sah dan belum luput; jika tidak → '
               '<code>noindex</code> + amaran (amalan MT sedia ada).</p></div></div>')

idx_2026 = table(["Perubahan", "Kesan kepada MT", "Rekaan SJPB"], [
    ["<b>eSPA wajib 1 Jan 2026</b> (HIMS KPKT) — tandatangan digital iDsaya (MyKad + biometrik), e-stamp LHDN SDSAS",
     "MT tidak menjana SPA; tetapi data pembeli/unit mesti tepat supaya SPA tidak tersekat",
     "Kumpul data <b>sedia-HIMS</b> dari peringkat EOI (nama ikut MyKad, no. unit rasmi, TIN) + pemantau status eSPA per unit"],
    ["<b>Larangan bayaran pra-SPA</b> (Peraturan 11(2)) + jam LAD bermula dari tarikh bayaran (keputusan Mahkamah Persekutuan)",
     "Tiada “booking fee” boleh dikutip oleh MT/ejen",
     "Modul tempahan <b>RM0</b>; sebarang kutipan hanya fi perkhidmatan MT (bukan harga unit)"],
    ["<b>Cadangan OTP</b> (RUU Pemajuan Harta Tanah) — boleh tarik diri sebelum SPA",
     "Pembeli mahu tempahan berisiko rendah",
     "EOI/OTP tanpa wang + kunci bertempoh = sejajar arah dasar"],
    ["<b>e-Invois LHDN</b> — fasa 4 (RM1–5 juta) mulai 1 Jan 2026; kelonggaran tanpa penalti hingga 31 Dis 2027; self-billed untuk bayaran komisen",
     "MT perlu TIN ejen (self-billed), TIN pembeli, jejak UUID",
     "Kumpul TIN pada peringkat EOI; modul bil/komisen simpan UUID e-invois"],
    ["<b>PDPA</b> (pindaan 2024) — DPO + notifikasi pelanggaran 72 jam (skala signifikan &gt;1,000 subjek)",
     "MT memegang MyKad/slip gaji/CCRIS",
     "Consent per pembeli, kawalan akses berperanan, prosedur 72 jam"]])

idx_jurang = table(["Jurang", "Keadaan sekarang", "Skrin POC"], [
    ["Inventori unit (blok/tingkat/unit, harga, status, status Bumi)", "Hanya “Bilangan Unit” sebagai teks",
     '<a href="unit-lock.html">B · Kunci Unit</a>'],
    ["EOI / senarai menunggu pra-lancar", "Tiada", '<a href="mikrosait-projek.html">A · Muka Awam</a>'],
    ["Pejabat tempahan + pek dokumen (RM0) + TIN", "Tiada", '<a href="ejen.html">B · Dashboard Ejen</a>'],
    ["Penjejakan eSPA/HIMS + pinjaman per unit", "Dalam WhatsApp/kepala", '<a href="pematuhan.html">E · Pematuhan</a>'],
    ["Komisen berperingkat + self-billed e-invois", "Tiada enjin komisen projek",
     '<a href="bil-komisen.html">D · Bil &amp; Komisen</a>'],
    ["Papan jualan/take-up untuk pemaju", "Tiada", '<a href="papan-jualan.html">C · Papan Jualan</a>']])

index_body = (idx_note +
              "<h2>1. Sistem dalam satu pandangan</h2>" + idx_cards +
              "<h2>2. Tiga prinsip yang membentuk semua skrin</h2>" + idx_prinsip +
              "<h2>3. Perubahan wajib 2026 (ringkas)</h2>" + idx_2026 +
              "<h2>4. Jurang MT yang POC ini isi</h2>" + idx_jurang)

page("index.html", "POC — Sistem Jualan Projek Baharu (SJPB)",
     "Mr Tanah · satu enjin tiga muka: awam · ejen · MT/pemaju — dengan gate pematuhan 2026", index_body)

# ============================================================ A. MIKROSAIT
ketersediaan = table(["Blok", "Tersedia", "EOI", "Dikunci", "Ditempah", "Dijual/Batal"], [
    ["A (Type A — Link Homes)", "14", "9", "3", "12", "18"],
    ["B (Type B — Bumi)", "6", "4", "1", "7", "9"],
    ["C (Type C)", "11", "7", "2", "9", "14"]])

eoi_rows = [("1", "Nurul Huda b. Ismail", "880101-14-****", "012-3** **78", "Type A — 2,004 kps", "WhatsApp"),
            ("2", "Tan Wei Ming", "910213-10-****", "016-7** **21", "Type C — 2,454 kps", "Landing page / GA4"),
            ("3", "Muhammad Farid b. Osman", "870920-01-****", "019-2** **90", "Type B (Bumi)", "Bilik pameran")]

mikro_kad = ('<div class="card"><h3>' + P['nama'] + '</h3>'
             '<p class="muted">' + P['pemaju'] + ' · ' + P['lokasi'] + ', Selangor · ' + P['jenis'] + '</p>'
             '<p><b>' + P['harga'] + '</b> <span class="muted">(' + P['harga_senarai'] + ')</span></p>'
             '<table><tr><th>Bilangan unit</th><td>' + P['unit'] + '</td></tr>'
             '<tr><th>Pegangan</th><td>' + P['pegangan'] + '</td></tr>'
             '<tr><th>Dijangka siap</th><td>' + P['siap'] + '</td></tr>'
             '<tr><th>Status</th><td>Bawah pembinaan · Fasa 1 habis dijual, Fasa 2 dilancarkan Okt 2025</td></tr></table>'
             '<h3>Ketersediaan (agregat, tanpa data peribadi)</h3>' + ketersediaan +
             '<p class="muted" style="font-size:12.5px">Angka unit di atas = <b>CONTOH struktur</b>. Dalam sistem '
             'sebenar, angka datang dari inventori pemaju/HIMS dan hanya jumlah agregat dipaparkan kepada awam.</p>'
             '<p><a class="btn" href="unit-lock.html">Lihat pelan tapak &amp; unit →</a> '
             '<a class="btn gold" href="ejen.html">Tempah / EOI RM0 →</a></p></div>')

mikro_borang = ('<div class="card"><h3>Borang EOI — RM0</h3>'
                '<div class="ok"><b>Tiada bayaran.</b> Peraturan 11(2) HDR 1989 melarang kutipan apa-apa bayaran '
                'sebelum SPA ditandatangani. EOI ini hanya mendaftar minat &amp; keutamaan unit.</div>'
                '<label>Nama penuh (ikut MyKad) *</label><input>'
                '<label>No. Kad Pengenalan *</label><input>'
                '<label>Telefon / WhatsApp *</label><input>'
                '<label>Emel</label><input>'
                '<label>TIN (untuk e-invois — boleh diisi kemudian)</label><input>'
                '<label>Unit / jenis diminati</label><select><option>Type A — Link Homes (2,004–2,038 kps)</option>'
                '<option>Type B (Bumi)</option><option>Type C (2,454 kps)</option></select>'
                '<label>Kaedah pembiayaan</label><select><option>Belum pasti — minta saringan kelayakan</option>'
                '<option>Pinjaman bank</option><option>Tunai</option><option>KWSP/kuasa beli sendiri</option></select>'
                '<label><input type="checkbox" style="width:auto"> Saya bersetuju data saya diproses untuk tujuan '
                'pendaftaran minat (PDPA — versi penuh pada produksi)</label>'
                '<p><button class="btn">Hantar EOI (RM0) →</button> '
                '<a class="btn ghost" href="ejen.html">Minta ejen hubungi →</a></p>'
                '<p class="muted" style="font-size:12.5px">Selepas hantar: borang masuk pangkalan EOI MT → ejen MT/'
                'co-agency ditugaskan → slot lawatan bilik pameran (QR check-in) → kunci unit.</p></div>')

panel_permit = table(["Medan (Peraturan 6)", "Nilai (Avalon @ Cybersouth)", "Status"], [
    ["Lesen Pemaju (DL)", P['dl'], '<span class="pill p-ok">sah — 11/10/2027</span>'],
    ["Permit Iklan &amp; Jualan (APDL)", P['permit'], '<span class="pill p-ok">sah — 06/07/2028</span>'],
    ["Pihak berkuasa tempatan (PBT)", P['pbt'], '<span class="pill p-ok">ada</span>'],
    ["Rujukan pelan diluluskan", P['pelan'], '<span class="pill p-ok">ada</span>'],
    ["Ejen diberi kuasa / agensi", "IQI Realty Sdn Bhd (PEA 2684/2313) + ZMJ Solutions", '<span class="pill p-ok">ada</span>'],
    ["Kuota Bumi / diskaun Bumi", "Kuota 30% (amalan negeri) · diskaun 5–15%", '<span class="pill p-warn">perlu sahkan negeri</span>'],
    ["Amaran permit", "Tiada — semua permit sah", '<span class="pill p-ok">lulus gate → boleh terbit &amp; indeks</span>']])

mikro = ('<div class="note"><b>Perubahan utama berbanding laman projek baharu sekarang:</b> halaman ini menunjukkan '
         '<b>ketersediaan unit</b> + borang <b>EOI RM0</b> + panel permit yang naik taraf jadi gate automatik. '
         'Butang <b>“Lihat projek”</b> dikekalkan (arahan Zahir). Data projek = fakta sebenar.</div>'
         '<h2>Kad projek (mikrosait awam)</h2><div class="grid g2">' + mikro_kad + mikro_borang + '</div>'
         '<h2>Panel Permit Iklan &amp; Jualan (gate automatik)</h2>' + panel_permit +
         '<h2>Aliran awam → EOI</h2><div class="flow">Google/Ads/WhatsApp → mikrosait projek → [ketersediaan unit] '
         '→ [kalkulator ansuran]\n   → EOI RM0 (nama, KP, tel, TIN) → tugaskan ejen MT/co-agency → slot bilik pameran (QR)'
         '\n   → KUNCI UNIT (bertempoh) → Pek tempahan RM0 + dokumen → saringan pembiayaan → eSPA (HIMS) → 10% ke HDA pemaju</div>'
         '<h2>Contoh barisan EOI (pandangan MT — data contoh)</h2>' +
         table(["#", "Nama", "KP (topeng)", "Telefon", "Unit pilihan", "Sumber"], eoi_rows))

page("mikrosait-projek.html", "A · Muka Awam — mikrosait projek &amp; EOI RM0",
     "Ketersediaan unit + EOI tanpa bayaran + panel permit yang menjadi gate automatik", mikro)

# ============================================================ B. KUNCI UNIT
import random
random.seed(7)
rows_grid = []
for blok, code in (("A", "Type A"), ("B", "Type B (Bumi)"), ("C", "Type C")):
    for tingkat in ("03", "02", "01"):
        cells = ['<div class="lbl">Blok ' + blok + ' · ' + code + ' · T' + tingkat + '</div>']
        for i in range(1, 11):
            lab = blok + "-" + tingkat + "-" + ("%02d" % i)
            if blok == "B" and i in (2, 5, 7):
                cls = "u bumi t"
            else:
                r = random.random()
                cls = "u " + ("t" if r < .34 else "e" if r < .55 else "k" if r < .75 else "b" if r < .92 else "d")
            cells.append('<div class="' + cls + '" title="' + lab + '">' + ("%02d" % i) + '</div>')
        rows_grid.append("".join(cells))
grid_html = '<div class="stack">' + "".join(rows_grid) + '</div>'

lock_aktif = table(["Unit", "Ejen", "Jenis kunci", "Mula", "Tamat (timeLock)", "Buffer", "Tindakan"], [
    ["A-02-05", "Faizal (MT)", "Kunci pelanggan", "15/09 10:12", '17/09 10:12 <span class="pill p-warn">47j tinggal</span>', "2 jam", "Sambung · Lepas"],
    ["C-03-09", "Aina (co-agency)", "Kunci pelanggan", "15/09 14:40", '16/09 14:40 <span class="pill p-warn">23j tinggal</span>', "2 jam", "Sambung · Lepas"],
    ["B-01-02", "—", "Kunci pameran (buffer)", "14/09 18:00", '15/09 18:00 <span class="pill p-ok">2j tinggal</span>', "—", "Kunci semula"]])

peraturan_kunci = table(["Peraturan", "Nilai contoh", "Sebab"], [
    ["Tempoh kunci lalai", "48 jam (boleh 24–72)", "Cukup masa hantar dokumen; tidak menyekat unit"],
    ["Buffer selepas kunci tamat", "2 jam", "Elak unit “terapung” antara ejen"],
    ["Had kunci serentak per ejen", "3 unit", "Elak hoarding unit"],
    ["Kunci hanya boleh oleh", "Ejen MT berdaftar projek + co-agency diluluskan", "Kawalan pematuhan"],
    ["Unit Bumi", "Kunci hanya jika kelayakan pembeli disahkan", "Kuota negeri"],
    ["Override", "MT Admin sahaja (diaudit)", "Penyelesaian pertikaian"]])

lock = ('<div class="note">Kunci unit ialah jantung sistem: menyelesaikan masalah #1 jualan pelancaran '
        '(<b>dua ejen janjikan unit sama</b>) dan #2 (<b>unit “dikunci” selama-lamanya oleh ejen yang hilang</b>). '
        'Semua kunci bertempoh, diaudit, dan ada buffer.</div>'
        '<h2>Pelan tapak digital — status unit (contoh struktur)</h2>'
        '<div class="legend">'
        '<span><i class="sq" style="background:#E6F5EC;border:1px solid #9ED0B1"></i>Tersedia</span>'
        '<span><i class="sq" style="background:#EAF1FB;border:1px solid #A9C4E8"></i>EOI</span>'
        '<span><i class="sq" style="background:#FFF3D6;border:1px solid #E8CE8C"></i>Dikunci (bertempoh)</span>'
        '<span><i class="sq" style="background:#FDE7E7;border:1px solid #E9AFAF"></i>Ditempah</span>'
        '<span><i class="sq" style="background:#E4E9E7;border:1px solid #C2CCC8"></i>Dijual / eSPA</span>'
        '<span><i class="sq" style="background:#fff;border:2px dashed #7C4DBE"></i>Unit Bumi</span></div>' + grid_html +
        '<h2>Kunci unit aktif (contoh)</h2>' + lock_aktif +
        '<h2>Peraturan kunci (konfigurasi, bukan kod)</h2>' + peraturan_kunci +
        '<h2>Pek tempahan (RM0) — apa yang dikumpul</h2><div class="grid g2">'
        '<div class="card"><h3>Data pembeli (sedia-HIMS)</h3><ul>'
        '<li>Nama <b>ikut MyKad</b> (ejaan sama) + salinan MyKad</li><li>No. KP/pasport · tarikh lahir · alamat</li>'
        '<li>Telefon/emel · pekerjaan · majikan · pendapatan</li><li><b>TIN</b> (e-invois) · pemilik bersama/pasangan</li>'
        '<li>Consent PDPA (versi + cap masa)</li><li>eKYC ringkas (padanan nama↔MyKad↔swafoto); iDsaya penuh oleh pemaju</li></ul></div>'
        '<div class="card"><h3>Data unit &amp; jualan</h3><ul>'
        '<li>No. unit rasmi · jenis · keluasan · pelan lantai</li>'
        '<li>Harga senarai + <b>diskaun/pakej berstruktur</b> (semua direkod)</li>'
        '<li>Skim bayaran (Jadual G/H) · jenis pinjaman</li><li>Ejen + agensi (MT/co-agency) + kadar komisen</li>'
        '<li>Borang tempahan <b>dijana PDF</b> + no. rujukan untuk sistem pemaju/HIMS</li>'
        '<li>Status: EOI → Dikunci → Ditempah</li></ul></div></div>'
        '<div class="warn"><b>Tiada medan bayaran harga unit dalam mana-mana skrin MT.</b> Pembayaran 10% '
        '(Jadual Ketiga) direkod sebagai <i>milestone</i> sahaja selepas eSPA ditandatangani dan masuk akaun HDA pemaju.</div>')

page("unit-lock.html", "B · Kunci Unit &amp; Pek Tempahan (RM0)",
     "Pelan tapak berwarna, kunci bertempoh + buffer, pek data sedia-HIMS", lock)

# ============================================================ B2. EJEN
ejen_tugas = table(["Pelanggan", "Sumber", "Unit diminati", "Peringkat", "Tindakan seterusnya", "Masa"], [
    ["Nurul Huda b. Ismail", "WhatsApp", "Type A", '<span class="pill p-eoi">EOI</span>', "Panggil &amp; kunci unit", "2j"],
    ["Tan Wei Ming", "Landing / GA4", "Type C", '<span class="pill p-kunci">Dikunci A-02-05</span>', "Kumpul MyKad + TIN", "1j 47m"],
    ["M. Farid b. Osman", "Bilik pameran", "Type B (Bumi)", '<span class="pill p-eoi">EOI</span>', "Sahkan kelayakan Bumi", "1j"],
    ["Lee Ai Ling", "Rujukan pemilik", "Type A", '<span class="pill p-tempah">Ditempah</span>', "Hantar dokumen bank", "—"]])

ejen_komisen = table(["Unit", "Kadar", "Tempahan", "eSPA", "Lulus pinjaman", "VP", "Status bayaran"], [
    ["A-01-04", "1.5% × RM1,020,000", '<span class="pill p-ok">✓</span>', '<span class="pill p-ok">✓</span>',
     '<span class="pill p-ok">✓</span>', '<span class="pill p-warn">—</span>', "<b>60% dibayar</b> (RM9,180)"],
    ["C-03-09", "1.5% × RM1,320,000", '<span class="pill p-ok">✓</span>', '<span class="pill p-ok">✓</span>',
     '<span class="pill p-warn">—</span>', '<span class="pill p-warn">—</span>', "<b>35% dibayar</b> (RM6,930)"],
    ["B-02-02", "1.5% × RM980,000", '<span class="pill p-ok">✓</span>', '<span class="pill p-warn">—</span>',
     '<span class="pill p-warn">—</span>', '<span class="pill p-warn">—</span>', "<b>10% dibayar</b> (RM1,470)"]])

ejen = ('<div class="note">Skrin ini menjawab soalan ejen: <i>“apa unit saya boleh kunci, siapa pelanggan saya setakat '
        'mana, dan bila saya dibayar?”</i> Itulah sebabnya ejen memilih satu projek berbanding projek lain.</div>'
        '<h2>Ringkasan saya hari ini</h2><div class="grid g4">'
        '<div class="kpi"><div class="n">7</div><div class="l">EOI ditugaskan (baru: 3)</div></div>'
        '<div class="kpi"><div class="n">2</div><div class="l">Kunci unit aktif (had 3)</div></div>'
        '<div class="kpi"><div class="n">4</div><div class="l">Tempahan bulan ini</div></div>'
        '<div class="kpi"><div class="n">2</div><div class="l">Menunggu kelulusan pinjaman</div></div></div>'
        '<h2>Tugasan saya</h2>' + ejen_tugas +
        '<h2>Komisen saya (lepas berperingkat — bukan sekali gus)</h2>' + ejen_komisen +
        '<div class="grid g2"><div class="card"><h3>Jadual lepas cadangan (perlu keputusan Zahir)</h3><ul>'
        '<li>10% — tempahan sah + dokumen lengkap</li><li>25% — eSPA ditandatangani</li>'
        '<li>25% — pinjaman diluluskan &amp; LOU diterima</li><li>40% — serah milik kosong (VP)</li></ul>'
        '<p class="muted" style="font-size:12.5px">Selaras amalan industri (MHub: Booking → SPA → Loan → VP). '
        'Jadual mesti dipersetujui <b>bertulis</b> dalam surat lantikan/co-agency.</p></div>'
        '<div class="card"><h3>Alat ejen (kos rendah, impak tinggi)</h3><ul>'
        '<li>Kad kongsi WhatsApp/Telegram per unit (imej + QR)</li>'
        '<li>Kalkulator ansuran + cetakan “pakej bayaran” untuk pelanggan</li>'
        '<li>Templat mesej susulan (5 sentuhan) + peringatan automatik</li>'
        '<li>Papan pendahulu pasukan (unit, nilai, masa respons)</li>'
        '<li>Notifikasi: EOI baharu, kunci hampir tamat, pinjaman ditolak → tukar unit tanpa batal</li></ul></div></div>')

page("ejen.html", "B · Dashboard Ejen Projek",
     "Tugasan, kunci unit, tempahan &amp; komisen berperingkat — alat yang membuatkan ejen memilih projek MT", ejen)

# ============================================================ C. PAPAN JUALAN
funnel = table(["Peringkat", "Bilangan", "Tukar (%)", "Nota"], [
    ["Kunjungan mikrosait (GA4)", "4,812", "—", "Kempen FB/Google + organik"],
    ["EOI RM0", "186", "3.9%", "Kadar tukar sihat untuk pelancaran"],
    ["Kunjungan bilik pameran", "97", "52%", "Check-in QR"],
    ["Kunci unit", "64", "66%", "Had 3 kunci/ejen"],
    ["Tempahan (RM0)", "41", "64%", "Dokumen lengkap: 36"],
    ["eSPA ditandatangani", "33", "80%", "HIMS pemaju"],
    ["Pinjaman diluluskan", "21", "64%", "<b>Perlu semak saringan awal</b> (penanda aras industri lulus: 41.2%)"],
    ["Dijual / selesai", "18", "—", "—"]])

takeup = table(["Blok / jenis", "Jumlah", "Tersedia", "Ditempah", "Dijual", "Take-up", "Purata harga"], [
    ["A — Type A (Link Homes)", "56", "14", "12", "18", "64%", "RM1,180,000"],
    ["B — Type B (Bumi)", "27", "6", "7", "9", "59%", "RM1,021,000"],
    ["C — Type C", "43", "11", "9", "14", "70%", "RM1,410,000"]])

prestasi = table(["Ejen", "EOI", "Tempahan", "Nilai (RM)", "Masa respons purata"], [
    ["Faizal (MT)", "31", "9", "10.8 juta", "2j 05m"],
    ["Aina (co-agency)", "24", "6", "7.3 juta", "3j 40m"],
    ["Hafiz (MT)", "19", "4", "4.6 juta", "5j 12m"]])

papan = ('<h2>Papan jualan ' + P['nama'] + ' (contoh struktur data)</h2><div class="grid g4">'
         '<div class="kpi"><div class="n">166</div><div class="l">Unit fasa berpermit</div></div>'
         '<div class="kpi"><div class="n">62%</div><div class="l">Take-up fasa 1 (103/166)</div></div>'
         '<div class="kpi"><div class="n">41.2%</div><div class="l">Penanda aras lulus pinjaman industri 2025</div></div>'
         '<div class="kpi"><div class="n">RM180</div><div class="l">Penanda aras kos/lead industri</div></div></div>'
         '<h2>Funnel tempahan (bulan semasa)</h2>' + funnel +
         '<h2>Take-up ikut blok &amp; jenis (contoh)</h2>' + takeup +
         '<h2>Halangan &amp; amaran (kenapa jualan tersekat)</h2><div class="grid g2">'
         '<div class="card"><h3>Amaran terbuka</h3><ul>'
         '<li><span class="pill p-bad">3 kes</span> Pinjaman ditolak — perlu tukar bank/pembeli (aliran “tukar unit tanpa batal”)</li>'
         '<li><span class="pill p-warn">5 kes</span> TIN pembeli belum dikumpul → risiko e-invois lewat</li>'
         '<li><span class="pill p-warn">2 unit</span> Unit Bumi dikunci tanpa pengesahan kelayakan</li>'
         '<li><span class="pill p-warn">1 kes</span> Dokumen SPA belum diterima daripada peguam selepas 21 hari</li>'
         '<li><span class="pill p-ok">0</span> Tempahan bertindih (matlamat dikekalkan)</li></ul></div>'
         '<div class="card"><h3>Prestasi ejen (contoh)</h3>' + prestasi + '</div></div>'
         '<h2>Keputusan yang papan ini sokong</h2><ul>'
         '<li><b>Harga/diskaun</b>: unit lambat bergerak dalam blok tertentu → asas pakej berstruktur (bukan rebat gelap).</li>'
         '<li><b>Agihan lead</b>: ejen respons lambat → lead diagih semula (berasaskan data).</li>'
         '<li><b>Bank panel</b>: kadar tolak mengikut bank → tetapan panel &amp; bantuan pra-saringan.</li>'
         '<li><b>Pemaju</b>: laporan mingguan automatik (take-up, halangan, unjuran) — nilai tambah yang membuatkan MT dilantik semula.</li></ul>')

page("papan-jualan.html", "C · Papan Jualan MT / Pemaju",
     "Take-up, funnel, halangan pinjaman, prestasi ejen — bukti yang MT tunjukkan kepada pemaju", papan)

# ============================================================ D. BIL & KOMISEN
bil_rows = [
    ["1", "Selesai tandatangan SPA (eSPA distem)", "10%", "102,000", "eSPA ditandatangani + e-stamp + ke akaun HDA", '<span class="pill p-ok">Dibayar</span>'],
    ["2", "Kerja asas &amp; landas", "10%", "102,000", "Sijil arkitek + notis bertulis", '<span class="pill p-ok">Dibayar</span>'],
    ["3", "Rangka konkrit bertetulang", "15%", "153,000", "Sijil arkitek", '<span class="pill p-ok">Dibayar</span>'],
    ["4", "Dinding + rangka pintu/tingkap", "10%", "102,000", "Sijil arkitek", '<span class="pill p-warn">Dituntut</span>'],
    ["5", "Bumbung, pendawaian, paip, kabel telefon", "10%", "102,000", "Sijil arkitek", '<span class="pill p-warn">Belum</span>'],
    ["6", "Melepa dalam &amp; luar", "10%", "102,000", "Sijil arkitek", '<span class="pill p-warn">Belum</span>'],
    ["7", "Pembetungan", "5%", "51,000", "Sijil arkitek", '<span class="pill p-warn">Belum</span>'],
    ["8", "Parit", "5%", "51,000", "Sijil arkitek", '<span class="pill p-warn">Belum</span>'],
    ["9", "Jalan", "5%", "51,000", "Sijil arkitek", '<span class="pill p-warn">Belum</span>'],
    ["10", "Serah milik kosong (VP) — air &amp; elektrik sedia", "12.5%", "127,500", "Notis VP + kunci diserah", '<span class="pill p-warn">Belum</span>'],
    ["11", "21 hari kerja selepas hakmilik/MOT (mana lebih kemudian)", "2.5%", "25,500", "MOT didaftar", '<span class="pill p-warn">Belum</span>'],
    ["12", "Pegangan amanah peguam: 6 bulan selepas VP", "2.5%", "25,500", "6 bulan selepas VP", '<span class="pill p-warn">Belum</span>'],
    ["13", "Pegangan amanah peguam: 18 bulan selepas VP", "2.5%", "25,500", "18 bulan selepas VP", '<span class="pill p-warn">Belum</span>'],
    ["", "<b>JUMLAH</b>", "<b>100%</b>", "<b>1,020,000</b>", "", ""]]

ledger = table(["Unit", "Ejen", "Kadar", "Asas", "Akru (RM)", "Peristiwa tercapai", "Dilepas (RM)", "Baki (RM)"], [
    ["A-01-04", "Faizal", "1.5%", "RM1,020,000", "15,300", "Tempahan + eSPA + pinjaman", "9,180", "6,120 (menunggu VP)"],
    ["C-03-09", "Aina", "1.5%", "RM1,320,000", "19,800", "Tempahan + eSPA", "6,930", "12,870"],
    ["B-02-02", "Hafiz", "1.5%", "RM980,000", "14,700", "Tempahan", "1,470", "13,230"]])

bil = ('<div class="note">Jadual Ketiga Jadual G ialah <b>kontrak</b>, bukan cadangan. Setiap bil mesti terikat '
       '<b>peristiwa + sijil</b>. Sistem yang menjana bil tanpa sijil = risiko pertikaian &amp; faedah lewat 10%/tahun.</div>'
       '<h2>Milestone bil (Jadual G) — contoh satu unit RM1,020,000</h2>' +
       table(["#", "Peristiwa", "%", "Amaun (RM)", "Gate/bukti diperlukan", "Status"], bil_rows) +
       '<p class="muted" style="font-size:12.5px">Jadual G: siap 24 bulan · LAD 10%/tahun · faedah bayaran lewat 10%/tahun '
       'selepas 21 hari bekerja · tanggungan kecacatan 18 bulan. Jadual H (strata): 36 bulan — tanggungan kecacatan &amp; '
       'jadual bil perlu sahkan salinan terkini sebelum dijadikan gate sistem.</p>'
       '<h2>e-Invois &amp; kutipan (reka bentuk)</h2><div class="grid g3">'
       '<div class="card"><h3>Yang MT jana</h3><ul><li>Invois <b>fi perkhidmatan MT</b> (rendah, tidak berkaitan harga unit) — QR DuitNow/Billplz</li>'
       '<li><b>Self-billed e-invois</b> untuk bayaran komisen kepada ejen individu/proprietor</li>'
       '<li>Rekod UUID e-invois + TIN + cap masa (audit)</li></ul></div>'
       '<div class="card"><h3>Yang pemaju jana</h3><ul><li>Bil kemajuan unit → e-invois kepada pembeli (10%/15%/…/VP/MOT)</li>'
       '<li>Komisen agensi → pemaju mungkin self-billed kepada MT</li>'
       '<li>MT simpan salinan untuk rekonsiliasi (bukan jana semula)</li></ul></div>'
       '<div class="card"><h3>Kawalan</h3><ul><li>TIN dikumpul di peringkat EOI (bukan di hujung)</li>'
       '<li>Bil tanpa sijil → <b>disekat automatik</b></li><li>Peringatan lewat bayar (faedah 10%) + peringatan SPA automatik</li>'
       '<li>LHDN: transaksi tunggal &gt; RM10,000 tidak boleh dikonsolidasi</li></ul></div></div>'
       '<h2>Komisen: akru &amp; pelepasan (contoh ledger)</h2>' + ledger +
       '<div class="ok"><b>Kawalan liabiliti komisen:</b> papan ini menghalang kes klasik “komisen dibayar awal, projek tak siap”. '
       'Baki komisen dipantau sebagai liabiliti; jika tempahan batal, akrual dilaraskan mengikut perjanjian lantikan (bukan dipadam).</div>')

page("bil-komisen.html", "D · Bil Kemajuan, e-Invois &amp; Komisen",
     "Jadual Ketiga sebagai kontrak · gate sijil · e-invois · komisen dilepas berperingkat", bil)

# ============================================================ E. PEMATUHAN
gate_rows = [
    ["Lesen Pemaju (DL) sah", "HDR 1989 — Peraturan 5", "Sekat penerbitan &amp; tempahan jika luput", '<span class="pill p-ok">sah 11/10/2027</span>'],
    ["Permit Iklan &amp; Jualan sah", "HDR 1989 Peraturan 5–6", "Halaman <code>noindex</code> + amaran jika tiada/luput", '<span class="pill p-ok">sah 06/07/2028</span>'],
    ["Satu permit = satu pemajuan/fasa", "Garis panduan KPKT (tiada gabungan/pecahan fasa)", "Daftar permit per fasa; amaran jika bercanggah", '<span class="pill p-ok">fasa 166 unit</span>'],
    ["Tiada bayaran pra-SPA", "Peraturan 11(2) HDR 1989 (P.U.(A) 106/2015)", "Sekat medan bayaran harga dalam modul tempahan", '<span class="pill p-ok">EOI RM0 sahaja</span>'],
    ["eKYC &amp; padanan nama MyKad", "eSPA/HIMS (iDsaya) + amalan sifar ketidakpadanan", "Amaran jika nama tempahan ≠ MyKad", '<span class="pill p-warn">2 kes perlu betulkan ejaan</span>'],
    ["TIN pembeli dikumpul", "e-Invois LHDN", "Sekat penghantaran e-invois tanpa TIN; peringatan", '<span class="pill p-warn">5 kes belum ada TIN</span>'],
    ["Consent PDPA per pembeli", "Akta 709 (pindaan 2024)", "Sekat simpan dokumen sensitif tanpa consent", '<span class="pill p-ok">41/41 ada</span>'],
    ["Kelayakan unit Bumi", "Kuota negeri + Lembaga Perumahan Negeri", "Sekat kunci/tempahan kepada bukan-Bumi", '<span class="pill p-warn">2 unit perlu semak</span>'],
    ["Status eSPA per unit", "eSPA wajib 1 Jan 2026 (HIMS)", "Pemantau: dijana → ditandatangani → distem → disimpan", '<span class="pill p-warn">4 unit menunggu</span>'],
    ["Surat tawaran bank diterima", "Amalan bank + 14 hari selepas SPA", "Peringatan automatik + kesan kepada komisen", '<span class="pill p-ok">21 lulus</span>']]

tarikh_rows = [
    ["Permit iklan &amp; jualan luput", "Tiada pengiklanan/jualan sah dibenarkan", "-90/-30/-7 hari amaran; auto-noindex"],
    ["Lesen pemaju luput", "Sama seperti permit", "idem"],
    ["14 hari minta pinjaman selepas SPA", "Klausa Jadual G (boleh menjejaskan pembeli)", "Peringatan pada pengesahan SPA"],
    ["21 hari bekerja bayar ansuran", "Faedah 10%/tahun", "Peringatan + kiraan faedah automatik"],
    ["Masa serah milik (24 bulan Jadual G)", "LAD 10%/tahun kepada pembeli", "Kiraan LAD automatik + amaran pemaju"],
    ["18 bulan tanggungan kecacatan (Jadual G)", "Liabiliti pemaju tamat", "Peringatan kepada pembeli (hak mereka)"],
    ["Pegangan 2×2.5% peguam", "Wang pembeli dipegang amanah", "Peringatan 6 &amp; 18 bulan"],
    ["72 jam notifikasi pelanggaran PDPA", "Pelanggaran statutori", "Prosedur tindak balas + log insiden"]]

audit_rows = [
    ["15/09 10:12:07", "faizal@mt", "Ejen", "Kunci unit", "Unit A-02-05", "TERSEDIA → DIKUNCI (48j)"],
    ["15/09 10:40:22", "mt.admin", "Admin", "Ubah diskaun", "Unit A-02-05", "RM1,020,000 → RM1,005,000 (pakej 1.5%)"],
    ["15/09 14:40:11", "aina@coagency", "Co-agency", "Kunci unit", "Unit C-03-09", "TERSEDIA → DIKUNCI (24j)"],
    ["15/09 15:02:44", "mt.admin", "Admin", "Sahkan dokumen", "Tempahan T-2026-0087", "Dokumen 6/8 → 8/8"],
    ["15/09 15:31:09", "system", "Sistem", "Gate permit", "Halaman Avalon", "gate: lulus (permit sah)"],
    ["15/09 16:10:55", "mt.admin", "Admin", "Akses dokumen (PDPA)", "MyKad #88", "akses dilog (sebab: pengesahan eSPA)"]]

patuh = ('<h2>Papan pematuhan — gate sebelum terbit, sebelum tempahan, sebelum bayaran</h2>' +
         table(["Gate", "Peraturan/asas", "Tindakan automatik", "Status projek semasa"], gate_rows) +
         '<h2>Pemantau tarikh penting</h2>' +
         table(["Tarikh penting", "Apa jadi jika terlepas", "Pemantauan SJPB"], tarikh_rows) +
         '<h2>Jejak audit (contoh — append-only)</h2>' +
         table(["Cap masa", "Pengguna", "Peranan", "Tindakan", "Objek", "Nilai lama → baharu"], audit_rows) +
         '<div class="note"><b>Nota jujur:</b> data dalam papan ini = <b>contoh struktur</b>. Tujuan POC ialah '
         'menunjukkan <i>apa</i> yang akan dipantau dan <i>bagaimana</i> ia menyekat risiko — bukan mendakwa angka sebenar projek.</div>')

page("pematuhan.html", "E · Pematuhan &amp; Jejak Audit",
     "APDL/DL, eSPA/HIMS, e-invois, PDPA, unit Bumi — sebagai gate automatik, bukan fail Excel", patuh)

# ============================================================ REKA BENTUK
l6 = "L6  BI & AI        papan jualan · take-up · funnel · amaran · AI Ali (FAQ unit)"
l5 = "L5  PEMATUHAN      gate APDL/DL · simpanan permit · consent PDPA · unit Bumi · larangan bayaran pra-SPA · audit"
l4 = "L4  INTEGRASI      HIMS/eSPA (data sedia-HIMS) · MyInvois · Billplz/DuitNow QR · WhatsApp · Drive · GA4 · Notion · sistem pemaju"
l3 = "L3  MUKA           (A) Awam: mikrosait + EOI RM0  |  (B) Ejen: kunci/tempahan/komisen  |  (C) MT/Pemaju: papan & bil  |  (D) Rakan: peguam, bank"
l2 = "L2  ENJIN/API      inventori · kunci · EOI/barisan · tempahan · pembeli/eKYC · pinjaman · eSPA · bil · komisen · dokumen · KPI"
l1 = "L1  DATA           Notion (Projek, Inventori, EOI, Tempahan, Komisen, Dokumen) + Sheets (operasi) + Drive (fail) + audit"

seni = '<h2>Seni bina 6 lapisan</h2><div class="flow">' + "\n".join([l6, l5, l4, l3, l2, l1]) + '</div>'

model_rows = [
    ["Projek", "Nama, Pemaju, DL+luput, Permit+luput, PBT, Pelan, Kuota/Diskaun Bumi, Skim G/H, Slug, Aktif", "Lancar → Membina → Siap"],
    ["Fasa / Blok", "Fasa, Blok, Tingkat, Jenis unit, Permit per fasa", "—"],
    ["Unit", "No. unit, Blok/Tingkat, Jenis, Keluasan, Harga senarai/bersih, <b>Status Bumi</b>, Pelan, Pakej, Pelan bayaran", "<b>TERSEDIA → EOI → DIKUNCI → DITEMPAT → eSPA → PINJAMAN_LULUS → VP → DIJUAL</b> (+BATAL)"],
    ["Kunci Unit", "Unit, Ejen, Mula, Tamat, Jenis, Buffer", "Aktif / Tamat / Ditukar"],
    ["EOI", "Nama, KP, Telefon, Unit pilihan, Keutamaan, Sumber, Consent PDPA", "Menunggu → Dipanggil → Tempahan / Batal"],
    ["Tempahan", "No., Unit, Harga, Pakej, Ejen, Pembeli (+bersama/pasangan), Ref pemaju/HIMS", "Ditempah → eSPA → Aktif → Batal"],
    ["Pembeli", "Nama ikut MyKad, KP, Telefon, Emel, <b>TIN</b>, Pekerjaan, Pendapatan, Status eKYC, Consent", "—"],
    ["Pinjaman", "Bank, Jumlah, Status, Tarikh consent, LOU/LO, Penilai, Luput", "—"],
    ["eSPA", "Ref HIMS, jana, tandatangan (semua pihak), e-stamp SDSAS, fail + hash", "Belum → Dijana → Ditan. → Distem → Disimpan"],
    ["Bil / Milestone", "Peristiwa (%), Sijil, Invois, UUID e-invois, Tarikh, Bayaran", "Belum → Dituntut → Dibayar → Lewat (10%)"],
    ["Serahan / Kecacatan", "Tarikh VP, senarai kecacatan, perbaiki, luput tanggungan", "—"],
    ["Komisen", "Ejen, Kadar, Pencetus, Akru, Lepas, Bayar, Self-billed no.", "Belum akru → Akru → Boleh lepas → Dibayar"],
    ["Dokumen", "Jenis, Pemilik, Akses peranan, Versi", "—"],
    ["Audit", "Pengguna, Peranan, Tindakan, Objek, Nilai lama→baharu, Cap masa", "Kekal (append-only)"]]

aliran_rows = [
    ["A1", "Daftar projek + permit/DL", "MT admin", "Tarikh luput dipantau; terbit hanya jika sah"],
    ["A2", "Terbit mikrosait", "MT", "Jana dari daftar; <code>noindex</code> jika permit belum lengkap; butang Lihat projek wajib"],
    ["A3", "Tarik minat (kempen)", "Pengunjung", "EOI RM0 + kalkulator + AI Ali + WhatsApp + GA4"],
    ["A4", "Barisan &amp; pemanggilan pra-lancar", "MT admin", "Keutamaan + semak duplikasi/kelayakan + slot bilik pameran QR"],
    ["A5", "Kunci unit", "Ejen", "Bertempoh + buffer + jejak"],
    ["A6", "Tempahan RM0 + pek dokumen", "Ejen + MT", "Data sedia-HIMS + TIN + consent + borang PDF"],
    ["A7", "Saringan pembiayaan", "MT pembiayaan", "DSR/kelayakan awal + consent CCRIS + banding 2–3 bank (E7)"],
    ["A8", "eSPA (pemaju/HIMS) → e-stamp", "Pemaju + peguam", "MT pantau; simpan lesen + salinan untuk bank"],
    ["A9", "Bil kemajuan &amp; kutipan", "Peguam/pemaju", "Gate sijil arkitek + peratusan Jadual Ketiga + e-invois"],
    ["A10", "eSPA → pinjaman → VP", "Bank + pemaju", "LAD 10%/tahun; tanggungan 18 bulan; pegangan 2×2.5%"],
    ["A11", "Komisen ejen/agensi", "MT kewangan", "Lepas berperingkat + self-billed e-invois"],
    ["A12", "Pemantauan &amp; BI", "MT/pemaju", "Take-up, kadar lulus pinjaman, masa eSPA, batal"]]

fasa_rows = [
    ["F1", "Daftar projek diperluas + mikrosait v3 + <b>EOI RM0</b> + gate APDL", "Laman projek baharu naik taraf + EOI masuk sistem", "1–2 minggu"],
    ["F2", "Inventori unit + papan grid berwarna + kunci bertempoh + dashboard ejen + pek tempahan", "Ejen kunci &amp; hantar tempahan; sifar bertindih", "2–3 minggu"],
    ["F3", "Pembeli/eKYC + saringan + penghantaran bank + consent + penjejakan eSPA/HIMS + bilik dokumen", "Kes CRM automatik + papan pinjaman/eSPA", "2–3 minggu"],
    ["F4", "Bil milestone (Jadual Ketiga) + e-invois + enjin komisen + self-billed + bayaran fi MT", "Aliran tunai &amp; komisen telus, sedia audit LHDN", "3–4 minggu"],
    ["F5", "BI/papan pemaju + AI Ali + integrasi sistem pemaju + pemantau permit/VP", "Keputusan berasaskan data &amp; automasi", "Berterusan"]]

beli_rows = [
    ["Padan peranan agensi MT", "✗", "✓ paling hampir", "✓ dibina untuk aliran MT"],
    ["Harga", "tidak diterbitkan (Enterprise)", "tidak diterbitkan", "masa Ali; tiada langganan"],
    ["HIMS/eSPA", "✓ Rakan Integrasi KPKT", "✓ ekosistem pemaju", "guna data sedia-HIMS + portal pemaju"],
    ["Integrasi portal/Kes CRM MT", "✗", "✗", "✓"],
    ["Pemilikan data &amp; jenama", "✗", "✗", "✓"],
    ["Masa mula", "2–8 minggu onboarding", "beberapa minggu", "<b>F1: 1–2 minggu</b>"]]

keputusan = ('<h2>Keputusan yang perlu Zahir buat</h2><ol>'
             '<li>Skop: SJPB = <b>lapisan agensi</b> (bukan ganti sistem pemaju) — setuju?</li>'
             '<li>Tempahan kekal <b>RM0 (EOI/OTP)</b> + kunci unit sahaja?</li>'
             '<li>Mula <b>F1</b> untuk projek sedia ada (6 projek di mrtanah.com)?</li>'
             '<li>Untuk projek pemaju bersistem (MHub/PropertyX): SJPB sebagai lapisan agensi?</li>'
             '<li>Jadual pelepasan komisen (cadangan 10/25/25/40) &amp; siapa mengesahkan setiap peringkat?</li>'
             '<li>PDPA: lantik DPO &amp; daftar consent dalam F1 atau F3?</li>'
             '<li>Benarkan MT minta <b>data unit + salinan DL/APDL</b> daripada pemaju untuk papan MT?</li></ol>')

rekabentuk = (seni +
              '<h2>Model data (14 entiti)</h2>' + table(["Entiti", "Medan kunci", "Status"], model_rows) +
              '<h2>12 aliran hujung-ke-hujung</h2>' + table(["#", "Aliran", "Pelaku", "Kunci"], aliran_rows) +
              '<h2>Peta jalan 5 fasa</h2>' + table(["Fasa", "Skop", "Keluaran", "Anggaran"], fasa_rows) +
              '<h2>Beli vs bina</h2>' + table(["Kriteria", "MHub (pemaju)", "PropertyX Agency", "Bina SJPB (cadangan)"], beli_rows) +
              keputusan)

page("reka-bentuk.html", "Reka Bentuk &amp; Peta Jalan SJPB",
     "6 lapisan · 14 entiti data · 12 aliran · 5 fasa — ringkasan untuk keputusan Zahir", rekabentuk)

print("Siap:", sorted(os.listdir(OUT)))
