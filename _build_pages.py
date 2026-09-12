#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Jana 5 halaman mock-up Fasa 1 daripada data listing SEBENAR."""
import json, os
from urllib.parse import quote

BASE = "/home/ubuntu/mockup-hartanah"
M = json.load(open(os.path.join(BASE, "img-map.json")))
A = M["assets"]


def load(p):
    s = open(p).read()
    return json.loads(s[s.index("window.LISTINGS"):].split("=", 1)[1].rsplit(";", 1)[0])


Z = load("/home/ubuntu/zahir-web/data/listings.js")
MT = load("/home/ubuntu/mrtanah-site/data/listings.js")
by = lambda arr, t: [x for x in arr if x["tracking"] == t][0]

ZP_IDS = ["COA-0001", "COA-0002", "COA-0003", "COA-0007", "COA-0008", "COA-0009"]
MT_IDS = ["MT-0001", "MT-0004", "MT-0010", "MT-0018", "MT-0019", "MT-0002"]

PAGES = [("index.html", "Hub"), ("zmp-utama.html", "ZMP · Utama"), ("zmp-butiran.html", "ZMP · Butiran"),
         ("mt-utama.html", "MT · Utama"), ("mt-butiran-tanah.html", "MT · Butiran Tanah"),
         ("temujanji.html", "Borang Temujanji")]


def switcher(cur):
    return ('<div class="switch">' + "".join(
        f'<a href="{f}" class="{"on" if f == cur else ""}">{n}</a>' for f, n in PAGES) + "</div>")


def mockbar(txt):
    return f'<div class="mockbar">MOCK-UP CADANGAN — bukan laman sebenar. Data &amp; gambar ASAL dari listing sedia ada. {txt}</div>'


def head(title, desc, brand, listing=None):
    attr = f' data-listing="{listing}"' if listing else ""
    return f"""<!DOCTYPE html>
<html lang="ms"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preload" href="assets/fonts/PlusJakartaSans-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/mockup.css?v=2">
</head>
<body class="brand-{brand}"{attr}>
"""


def header(brand, active):
    if brand == "zmp":
        name, sub, wa, num, tagline = "Zahir MJ Property", "Hartanah Dipercayai", "60122310119", "012-2310119", "PEA 2684"
        nav = """<a href="zmp-utama.html" class="{a1}">Utama</a>
      <div class="drop"><button>Cari Hartanah ▾</button><div class="menu">
        <div class="grp">Mengikut segmen</div>
        <a href="zmp-utama.html">Rumah Subsale</a><a href="zmp-utama.html">Projek Baharu</a>
        <a href="zmp-utama.html">Komersial</a>
        <div class="grp">Lain-lain</div>
        <a href="zmp-utama.html">Semua Listing (63 aktif)</a></div></div>
      <a href="zmp-utama.html" class="{a2}">Kalkulator</a>
      <a href="zmp-utama.html" class="{a3}">Tentang</a>""".format(a1="active" if active == "utama" else "", a2="", a3="")
        owner = """<div class="grp">Untuk Pemilik &amp; Ejen</div>
        <a href="#">Portal Pengurusan</a><a href="#">Serah Listing</a><a href="#">Serah Dokumen</a>
        <a href="#">Bayaran &amp; Invois</a><a href="#">Mohon Sewa</a>"""
    else:
        name, sub, wa, num, tagline = "Mr Tanah", "Pakar Tanah &amp; Hartanah Malaysia", "60163119076", "016-3119076", "PEA 2684"
        nav = """<a href="mt-utama.html" class="{a1}">Utama</a>
      <div class="drop"><button>Tanah &amp; Lot ▾</button><div class="menu">
        <div class="grp">Mengikut jenis</div>
        <a href="mt-utama.html">Tanah Pertanian / Dusun</a><a href="mt-utama.html">Lot Banglo</a>
        <a href="mt-utama.html">Tanah Komersial &amp; Industri</a>
        <div class="grp">Lain-lain</div>
        <a href="mt-utama.html">Semua Listing (34 aktif)</a></div></div>
      <a href="mt-utama.html" class="{a2}">Kalkulator</a>
      <a href="mt-utama.html" class="{a3}">Tentang</a>""".format(a1="active" if active == "utama" else "", a2="", a3="")
        owner = """<div class="grp">Untuk Pemilik &amp; Ejen</div>
        <a href="#">Portal Pengurusan</a><a href="#">Serah Listing</a><a href="#">Serah Dokumen</a>"""
    return f"""<header class="site-header"><div class="wrap hdr">
  <a class="brand" href="{brand if False else ('zmp-utama.html' if brand=='zmp' else 'mt-utama.html')}">
    <span class="mark">{'Z' if brand=='zmp' else 'MT'}</span>
    <span><strong>{name}</strong><small>{sub} · {tagline}</small></span></a>
  <nav class="nav" id="nav">{nav}
    <div class="drop"><button>Untuk Pemilik &amp; Ejen ▾</button><div class="menu">{owner}</div></div>
  </nav>
  <a class="btn btn-accent btn-sm" href="https://wa.me/{wa}" target="_blank" rel="noopener">📲 {num}</a>
  <button class="navtoggle" id="navToggle" aria-label="Menu">☰</button>
</div></header>"""


def footer(brand):
    name, num, wa = ("Zahir MJ Property", "012-2310119", "60122310119") if brand == "zmp" else ("Mr Tanah", "016-3119076", "60163119076")
    return f"""<footer><div class="wrap">
 <div class="fcols">
  <div><h4>{name}</h4>
    <p style="color:#9FB0C4;font-size:13.5px;max-width:300px">Ejen hartanah berdaftar (PEA 2684) · DNA Workspace, Seksyen 9, Bandar Baru Bangi, Selangor.</p>
    <p style="margin-top:12px"><a class="btn btn-accent btn-sm" href="https://wa.me/{wa}">📲 WhatsApp {num}</a></p></div>
  <div><h4>Hartanah</h4><ul><li><a href="#">Semua listing</a></li><li><a href="#">Rumah subsale</a></li>
    <li><a href="#">Projek baharu</a></li><li><a href="#">Tanah &amp; lot banglo</a></li><li><a href="#">Projek berbilang unit</a></li></ul></div>
  <div><h4>Untuk Pemilik &amp; Ejen</h4><ul><li><a href="#">Portal pengurusan</a></li><li><a href="#">Serah listing</a></li>
    <li><a href="#">Serah dokumen</a></li><li><a href="#">Bayaran &amp; invois</a></li><li><a href="#">Mohon sewa</a></li></ul></div>
  <div><h4>Alat &amp; Bantuan</h4><ul><li><a href="#">Kalkulator pinjaman</a></li><li><a href="#">Semak kelayakan &amp; DSR</a></li>
    <li><a href="#">Tentang kami</a></li><li><a href="#">Dasar &amp; privasi</a></li><li><a href="#">Hubungi / temujanji</a></li></ul></div>
 </div>
 <div class="fbot"><span>© 2026 {name}. Semua hak terpelihara.</span>
   <span>MOCK-UP preview — disediakan oleh Ali untuk semakan Zahir MJ</span></div>
</div></footer>
<div class="mbar">
  <a class="btn btn-ghost" href="#senarai">🔎 Cari Hartanah</a>
  <a class="btn btn-accent" href="https://wa.me/{wa}" target="_blank" rel="noopener">📲 WhatsApp</a>
</div>
<div class="lb" id="lightbox"><button aria-label="Tutup">✕</button><img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt="Pratonton gambar"></div>
<script src="assets/mockup.js?v=2"></script>
<script src="assets/ali-config.js?v=1"></script>
<script src="assets/ali-chat.js?v=2"></script>
</body></html>"""


def ansuran(price):
    if not price:
        return None
    loan = price * 0.90
    r = 0.04 / 12
    n = 35 * 12
    return round(loan * r / (1 - (1 + r) ** -n))


def wa_link(num, txt):
    return f"https://wa.me/{num}?text={quote(txt)}"


def deals(l):
    """jenis boleh string ATAU array (listing dual JUAL+SEWA)."""
    j = l.get("jenis") or "JUAL"
    return j if isinstance(j, list) else [j]


def badges(l):
    b = "".join(f'<span class="bdg bdg-{d.lower()}">{d}</span>' for d in deals(l))
    if l.get("status") == "BARU":
        b += '<span class="bdg bdg-new">Baru disenaraikan</span>'
    return b


def card_z(l):
    a = A[l["tracking"]]
    mbl = ansuran(l["price"])
    specs = []
    if l.get("bedrooms"):
        specs.append(f'<span>🛏 {l["bedrooms"]} bilik</span>')
    if l.get("bathrooms"):
        specs.append(f'<span>🛁 {l["bathrooms"]} bilik air</span>')
    sz = l.get("built_up") if l.get("built_up") not in (None, "-", "") else l.get("land_area")
    if sz:
        specs.append(f"<span>⬛ {sz}</span>")
    tags = [f'<span class="tg">{l["type"]}</span>']
    if l.get("tenure"):
        tags.append(f'<span class="tg g">{l["tenure"]}</span>')
    bdg = badges(l)
    sewa = f'<small>· Sewa {l["sewa_label"]}</small>' if l.get("sewa_price") else ""
    return f"""<article class="card">
 <div class="ph">
   <img src="{a['card']}" width="700" height="525" loading="lazy" alt="{l['title']} — {l['location']}">
   <div class="badges">{bdg}</div>
   <button class="save" data-id="{l['tracking']}" aria-label="Simpan listing">♡</button>
   <span class="phcount">📷 {len(l['images'])}</span>
 </div>
 <div class="bd">
   <h3>{l['title']}</h3>
   <div class="loc">📍 {l['location']}</div>
   <div class="price">{l['price_label']} {f'<small>· anggaran RM {mbl:,}/bln</small>' if mbl else ''}{sewa}</div>
   <div class="specs">{''.join(specs)}</div>
   <div class="tags">{''.join(tags)}</div>
   <div class="acts">
     <a class="btn btn-accent" href="{wa_link('60122310119', f"Salam, saya berminat dengan {l['title']} ({l['tracking']}) — {l['location']}. Boleh saya dapat maklumat lanjut?")}" target="_blank" rel="noopener">WhatsApp</a>
     <a class="btn btn-ghost" href="{l['map_url']}" target="_blank" rel="noopener">Peta</a>
   </div>
   <div class="foot"><span>{l['tracking']}</span><span>Dikemas kini {l.get('date','')}</span></div>
 </div></article>"""


def card_mt(l):
    a = A[l["tracking"]]
    specs = [f'<span>📐 {l["land_area"]}</span>'] if l.get("land_area") else []
    if l.get("psf"):
        specs.append(f'<span>💰 RM{l["psf"]}/sqft</span>')
    tags = [f'<span class="tg g">{l["kategori"]}</span>']
    if l.get("tenure"):
        tags.append(f'<span class="tg">{l["tenure"]}</span>')
    if l.get("sekatan") and l["sekatan"] not in ("Open", "Tidak dinyatakan"):
        tags.append(f'<span class="tg gold">{l["sekatan"]}</span>')
    if l.get("zoning") and l["zoning"] != "Tidak dinyatakan":
        tags.append(f'<span class="tg">Guna tanah: {l["zoning"]}</span>')
    bdg = badges(l) + f'<span class="bdg bdg-green">{l["kategori"]}</span>'
    sewa = f'<small>· Sewa {l["sewa_label"]}</small>' if l.get("sewa_price") else ""
    return f"""<article class="card">
 <div class="ph">
   <img src="{a['card']}" width="700" height="525" loading="lazy" alt="{l['title']} — {l['location']}">
   <div class="badges">{bdg}</div>
   <button class="save" data-id="{l['tracking']}" aria-label="Simpan listing">♡</button>
   <span class="phcount">📷 {len(l['images'])}</span>
 </div>
 <div class="bd">
   <h3>{l['title']}</h3>
   <div class="loc">📍 {l['location']}</div>
   <div class="price">{l['price_label']} {f'<small>· RM{l["psf"]}/sqft</small>' if l.get('psf') else ''}{sewa}</div>
   <div class="specs">{''.join(specs)}</div>
   <div class="tags">{''.join(tags)}</div>
   <div class="acts">
     <a class="btn btn-accent" href="{wa_link('60163119076', f"Salam, saya berminat dengan {l['title']} ({l['tracking']}) — {l['location']}. Boleh saya dapat maklumat lanjut & set tarikh lawatan?")}" target="_blank" rel="noopener">WhatsApp</a>
     <a class="btn btn-ghost" href="{l['map_url']}" target="_blank" rel="noopener">Peta</a>
   </div>
   <div class="foot"><span>{l['tracking']}</span><span>Dikemas kini {l.get('date','')}</span></div>
 </div></article>"""


def search_panel(brand):
    if brand == "zmp":
        tabs = [("all", "Semua"), ("jual", "Jual"), ("sewa", "Sewa"), ("jv", "JV")]
        f2 = '<select aria-label="Jenis hartanah"><option>Rumah Teres</option><option>Semi-D</option><option>Bungalow</option><option>Apartmen / Kondo</option><option>Komersial</option></select>'
        f3 = '<select aria-label="Bilik"><option>Bilik: apa-apa</option><option>3+ bilik</option><option>4+ bilik</option><option>5+ bilik</option></select>'
        ph = "Cari kawasan, contoh: Bangi / Cyberjaya"
    else:
        tabs = [("all", "Semua"), ("pertanian", "Tanah Pertanian"), ("banglo", "Lot Banglo"), ("komersial", "Komersial")]
        f2 = '<select aria-label="Jenis tanah"><option>Pertanian / Dusun</option><option>Lot Banglo</option><option>Komersial &amp; Industri</option><option>Bangunan</option></select>'
        f3 = '<select aria-label="Keluasan"><option>Keluasan: apa-apa</option><option>&lt; 10,000 sqft</option><option>0.25 – 1 ekar</option><option>&gt; 1 ekar</option></select>'
        ph = "Cari kawasan, contoh: Janda Baik / Presint 10"
    tabhtml = "".join(f'<button type="button" class="tab {"on" if k=="all" else ""}" data-seg="{k}">{v}</button>' for k, v in tabs)
    return f"""<div class="search">
 <div class="tabs">{tabhtml}</div>
 <div class="sgrid">
   <div class="fld"><label for="q">Lokasi / kata kunci</label><input id="q" type="text" placeholder="{ph}"></div>
   <div class="fld"><label>Jenis</label>{f2}</div>
   <div class="fld"><label>Saiz / bilik</label>{f3}</div>
   <div class="fld go"><label>&nbsp;</label><button class="btn btn-navy" type="button">🔎 Cari</button></div>
 </div>
</div>"""


def trust(items):
    return '<div class="trust"><div class="wrap"><ul>' + "".join(
        f'<li><span class="ic">{i}</span>{t}</li>' for i, t in items) + "</ul></div></div>"


# ============================================================ HUB
hub = head("Mock-up Fasa 1 — Cadangan reka bentuk web Zahir MJ Property &amp; Mr Tanah",
           "Preview mock-up cadangan reka bentuk laman hartanah.", "zmp")
hub += mockbar("Klik kad di bawah untuk buka setiap halaman.") + switcher("index.html") + """
<div class="wrap hub">
  <h1 style="font-size:clamp(24px,3.4vw,34px)">Mock-up Fasa 1 — cadangan reka bentuk</h1>
  <p class="muted" style="max-width:760px;margin-top:10px">Ini <b>preview sahaja</b> (noindex, tidak disambung ke laman sebenar).
  Semua <b>data, harga, gambar dan penerangan adalah SEBENAR</b> dari listing sedia ada — diambil dari
  <code>data/listings.js</code> kedua-dua repo. Tiada repo production disentuh.</p>
  <div class="hubgrid">
    <div class="hubcard"><h3>🏘 Zahir MJ Property — Utama</h3>
      <p class="muted" style="font-size:14px">Hero berimej sebenar + carian di hero, trust strip, 3 segmen, kad v2 (ansuran bulanan, kiraan gambar, badge), testimoni, widget kalkulator, footer 4 lajur, bar WhatsApp melekat pada telefon.</p>
      <ul><li>Navy dominan + hijau aksen (1 butang aksen sahaja)</li><li>Font jenama: Plus Jakarta Sans + Inter (self-host)</li><li>Navigasi dari 9 item → 4 + dropdown "Pemilik &amp; Ejen"</li></ul>
      <a class="btn btn-navy" href="zmp-utama.html">Buka mock-up →</a></div>
    <div class="hubcard"><h3>🌿 Mr Tanah — Utama</h3>
      <p class="muted" style="font-size:14px">Hero drone sebenar, carian ikut segmen tanah, kad tanah v2 dengan chip teknikal (keluasan, hakmilik, sekatan, guna tanah), blok peta + kemudahan, CTA WhatsApp.</p>
      <ul><li>Aksen zamrud (tanah/alam) + emas untuk lot premium</li><li>Kad tanah menonjolkan GERAN / HAKMILIK / KELUASAN</li><li>Peta + pautan Waze/Google percuma (tiada API berbayar)</li></ul>
      <a class="btn btn-navy" href="mt-utama.html">Buka mock-up →</a></div>
    <div class="hubcard"><h3>🏡 Zahir MJ Property — Butiran (contoh rumah)</h3>
      <p class="muted" style="font-size:14px">Galeri + thumbnail, panel harga melekat dengan anggaran ansuran, data teknikal, blok kemudahan + peta, borang temujanji lawatan.</p>
      <ul><li>Contoh: COA-0001 (Rumah Teres Bangi, RM560,000)</li><li>Nota: ZMP tiada listing TANAH aktif sekarang — jadi contoh rumah digunakan</li></ul>
      <a class="btn btn-navy" href="zmp-butiran.html">Buka mock-up →</a></div>
    <div class="hubcard"><h3>📐 Mr Tanah — Butiran TANAH (utama)</h3>
      <p class="muted" style="font-size:14px">Halaman butiran tanah baharu dengan <b>Jadual Data Teknikal Tanah</b> — memaparkan data yang sudah ada dalam rekod (keluasan, pegangan, kategori guna tanah, sekatan, zoning) + medan baharu yang perlu diisi.</p>
      <ul><li>Contoh: MT-0023 (Bungalow Land Presint 10, RM2.6 juta, Freehold)</li><li>Medan belum ada data ditanda jujur "perlu diisi"</li></ul>
      <a class="btn btn-navy" href="mt-butiran-tanah.html">Buka mock-up →</a></div>
  </div>
  <div class="hubcard" style="margin-top:18px">
    <h3>Apa yang berubah (Fasa 1)</h3>
    <ul style="columns:2;column-gap:30px">
      <li>Hero: imej hartanah sebenar (bukan gradien)</li>
      <li>Navigasi 2 lapisan (pelanggan vs pemilik/ejen)</li>
      <li>Kad v2: anggaran ansuran, kiraan gambar, badge, butang Simpan</li>
      <li>Jadual Data Teknikal Tanah (pembeza utama MT)</li>
      <li>Blok peta + jarak kemudahan + pautan Waze</li>
      <li>Bar WhatsApp melekat pada telefon</li>
      <li>Font jenama + nisbah warna 60/30/10</li>
      <li>Imej WebP (kad ≤ ~120 KB) + width/height (elak CLS)</li>
      <li>Testimoni &amp; borang temujanji (tempat dinyatakan — perlu data sebenar)</li>
    </ul>
    <p class="note" style="margin-top:14px">Belum disambung dalam mock-up ini (Fasa 2): GA4 + Meta Pixel, carian berfungsi, peta interaktif, halaman kawasan.</p>
    <p style="margin-top:14px"><b>Borang berfungsi:</b> <a href="temujanji.html">borang tempahan lawatan tapak</a> — diisi oleh pelawat, terus rekod + notifikasi WhatsApp/Telegram kepada Zahir. AI "Tanya Ali" akan beri <b>butang borang</b> secara automatik apabila pelawat menyebut lawatan tapak, kelayakan pinjaman, atau nak serah listing.</p>
  </div>
</div></body></html>"""
open(os.path.join(BASE, "index.html"), "w").write(hub)

# ============================================================ ZMP UTAMA
z_utama = head("MOCK-UP · Zahir MJ Property — Utama", "Cadangan reka bentuk laman utama Zahir MJ Property.", "zmp")
z_utama += mockbar("Halaman: Utama (Zahir MJ Property)") + switcher("zmp-utama.html")
z_utama += header("zmp", "utama")
z_utama += f"""
<section class="hero hero-tall">
 <div class="bg"><img src="img/{M['hero_z']}" width="1700" height="1133" fetchpriority="high" alt="Rumah teres dua tingkat, Putrajaya — contoh listing Zahir MJ Property"></div>
 <div class="veil"></div>
 <div class="wrap hero-in">
   <span class="eyebrow">Ejen berdaftar PEA 2684 · Selangor, KL &amp; Putrajaya</span>
   <h1>Cari Hartanah Idaman Anda</h1>
   <p class="lead">Listing terkini dari ejen hartanah profesional — rumah, semi-D, tanah &amp; komersial. Setiap unit melalui semakan status pemilikan dan harga pasaran.</p>
   {search_panel('zmp')}
   <div class="quick"><a href="#">Rumah bawah RM600K</a><a href="#">Freehold Selangor</a>
     <a href="#">Bangi &amp; Putrajaya</a><a href="#">Projek baharu</a></div>
 </div>
</section>
""" + trust([("✅", "63 listing aktif disemak status pemilikan"),
               ("⚡", "Balasan WhatsApp pada hari sama"),
               ("🧮", "Kalkulator ansuran &amp; semak kelayakan percuma"),
               ("🤝", "PEA 2684 — ejen hartanah berdaftar")]) + f"""
<section>
 <div class="wrap">
  <div class="sec-head"><div><h2>Mula dari mana?</h2><p>Pilih segmen yang anda cari.</p></div></div>
  <div class="segs">
   <a class="seg" href="#senarai"><img src="{A['COA-0001']['card']}" width="700" height="525" loading="lazy" alt="Rumah subsale"><span class="ov"></span>
     <span class="n">59 listing</span><span class="tx"><h3>Rumah Subsale</h3><p>Rumah teres, semi-D, banglo, apartmen — unit sedia didiami &amp; renovasi.</p></span></a>
   <a class="seg" href="#senarai"><img src="{A['COA-0007']['card']}" width="700" height="525" loading="lazy" alt="Projek baharu"><span class="ov"></span>
     <span class="n">3 projek</span><span class="tx"><h3>Projek Berbilang Unit</h3><p>Projek dengan beberapa unit — halaman perbandingan unit &amp; pelan lantai.</p></span></a>
   <a class="seg" href="#senarai"><img src="{A['COA-0003']['card']}" width="700" height="525" loading="lazy" alt="Komersial"><span class="ov"></span>
     <span class="n">4 listing</span><span class="tx"><h3>Komersial</h3><p>Kedai, pejabat &amp; bangunan untuk pelaburan dan perniagaan.</p></span></a>
  </div>
 </div>
</section>
<section class="alt" id="senarai">
 <div class="wrap">
  <div class="sec-head"><div><h2>Listing Terpilih</h2><p>Setiap kad memaparkan harga, anggaran ansuran, saiz dan status hakmilik.</p></div>
   <a class="more" href="#">Lihat semua 63 listing →</a></div>
  <div class="grid">{''.join(card_z(by(Z, t)) for t in ZP_IDS)}</div>
 </div>
</section>
<section>
 <div class="wrap">
  <div class="mapblk">
    <div class="map"><img src="img/{M['hero_z']}" width="1700" height="1133" loading="lazy" alt="Gambaran kawasan sekitar Bangi &amp; Putrajaya">
      <span class="pin">Bangi · Putrajaya · Cyberjaya</span></div>
    <div class="side">
      <h3>Fokus kawasan kami</h3>
      <p class="muted" style="font-size:14.5px">Kami mengkhusus hartanah di koridor Bangi – Putrajaya – Cyberjaya – Kajang.</p>
      <ul class="amin">
        <li><span>🏫 Sekolah &amp; institusi</span><b>UKM · GMI · UNIKL</b></li>
        <li><span>🏥 Hospital</span><b>Hospital Pakar AnNur</b></li>
        <li><span>🛣 Lebuhraya</span><b>LEKAS · SILK · Plus</b></li>
        <li><span>🚉 Pengangkutan</span><b>KTM Bangi · MRT Putrajaya</b></li>
        <li><span>🛒 Beli-belah</span><b>Bangi Gateway · IOI City Mall</b></li>
      </ul>
      <p><a class="btn btn-ghost btn-sm" href="#">Lihat listing kawasan ini →</a></p>
    </div>
  </div>
 </div>
</section>
<section class="alt">
 <div class="wrap">
  <div class="sec-head"><div><h2>Apa kata pelanggan</h2>
    <p class="ribbon">CONTOH — perlu diganti dengan testimoni SEBENAR sebelum terbit</p></div></div>
  <div class="tms">
   <div class="tm"><div class="stars">★★★★★</div><p>“Senang berurusan, semua maklumat hakmilik dijelaskan awal. Rumah saya terjual dalam 6 minggu.”</p>
     <div class="who">Nama Pelanggan<small>Pemilik rumah, Bandar Baru Bangi</small></div></div>
   <div class="tm"><div class="stars">★★★★★</div><p>“Dibantu kira kelayakan dan DSR sebelum pilih rumah. Proses bank jadi laju.”</p>
     <div class="who">Nama Pelanggan<small>Pembeli pertama, Cyberjaya</small></div></div>
   <div class="tm"><div class="stars">★★★★★</div><p>“Kami berurusan dari luar negara — semua diselesaikan melalui WhatsApp dan video call.”</p>
     <div class="who">Nama Pelanggan<small>Pelabur, Singapura</small></div></div>
  </div>
 </div>
</section>
<section>
 <div class="wrap">
  <div class="calc">
    <div><h2>Kira ansuran sebelum berjumpa ejen</h2>
      <p>Anggaran berdasarkan kadar 4.00% p.a., tempoh 35 tahun dan pembiayaan 90%. Angka sebenar bergantung kepada bank dan profil peminjam.</p></div>
    <div class="calcbox" data-calc>
      <label for="hrg">Harga hartanah</label>
      <div class="val">RM 560,000</div>
      <input id="hrg" type="range" min="150000" max="3000000" step="10000" value="560000">
      <div style="display:flex;justify-content:space-between;font-size:11.5px;color:#9FB0C4;margin:6px 0 16px"><span>RM150K</span><span>RM3J</span></div>
      <div class="out">Anggaran ansuran bulanan<small style="margin-bottom:4px"></small><b>RM —</b></div>
      <p style="margin-top:14px"><a class="btn btn-accent btn-sm" href="#">Semak kelayakan penuh &amp; DSR →</a></p>
    </div>
  </div>
 </div>
</section>
""" + footer("zmp")
open(os.path.join(BASE, "zmp-utama.html"), "w").write(z_utama)

# ============================================================ MT UTAMA
mt_utama = head("MOCK-UP · Mr Tanah — Utama", "Cadangan reka bentuk laman utama Mr Tanah.", "mt")
mt_utama += mockbar("Halaman: Utama (Mr Tanah)") + switcher("mt-utama.html")
mt_utama += header("mt", "utama")
mt_utama += f"""
<section class="hero hero-tall">
 <div class="bg"><img src="img/{M['hero_m']}" width="1700" height="1133" fetchpriority="high" alt="Pemandangan udara kawasan tanah — contoh listing Mr Tanah"></div>
 <div class="veil"></div>
 <div class="wrap hero-in">
   <span class="eyebrow">Pakar tanah &amp; lot banglo · Selangor, Pahang, N. Sembilan, Putrajaya</span>
   <h1>Cari Tanah &amp; Lot Banglo</h1>
   <p class="lead">Tanah pertanian, lot banglo geran individu, tanah komersial &amp; industri. Kami paparkan keluasan, hakmilik, geran dan akses jalan — supaya anda boleh buat keputusan dengan yakin.</p>
   {search_panel('mt')}
   <div class="quick"><a href="#">Tanah pertanian</a><a href="#">Lot banglo geran individu</a>
     <a href="#">Freehold</a><a href="#">Bawah 1 ekar</a></div>
 </div>
</section>
""" + trust([("🗺️", "34 listing tanah aktif disemak"), ("📄", "Status hakmilik &amp; geran dijelaskan awal"),
               ("📐", "Data teknikal tanah dipaparkan penuh"), ("🤝", "PEA 2684 — ejen berdaftar")]) + f"""
<section>
 <div class="wrap">
  <div class="sec-head"><div><h2>Pilih jenis tanah</h2><p>Setiap segmen ada cara penilaian yang berbeza — kami sediakan data yang betul-betul anda perlukan.</p></div></div>
  <div class="segs">
   <a class="seg" href="#senarai"><img src="{A['MT-0001']['card']}" width="700" height="525" loading="lazy" alt="Tanah pertanian"><span class="ov"></span>
     <span class="n">9 listing</span><span class="tx"><h3>Tanah Pertanian &amp; Dusun</h3><p>Sawit, getah, dusun durian, tanah tepi sungai — untuk pertanian &amp; pelaburan.</p></span></a>
   <a class="seg" href="#senarai"><img src="{A['MT-0004']['card']}" width="700" height="525" loading="lazy" alt="Lot banglo"><span class="ov"></span>
     <span class="n">11 listing</span><span class="tx"><h3>Lot Banglo &amp; Perumahan</h3><p>Lot sedia bina, geran individu, kawasan berpagar atau berhampiran bandar.</p></span></a>
   <a class="seg" href="#senarai"><img src="{A['MT-0019']['card']}" width="700" height="525" loading="lazy" alt="Tanah komersial"><span class="ov"></span>
     <span class="n">12 listing</span><span class="tx"><h3>Komersial, Bangunan &amp; Industri</h3><p>Tanah komersial, industri &amp; bangunan — potensi pembangunan.</p></span></a>
  </div>
 </div>
</section>
<section class="alt" id="senarai">
 <div class="wrap">
  <div class="sec-head"><div><h2>Tanah &amp; Lot Terpilih</h2><p>Keluasan, hakmilik, sekatan dan guna tanah dipaparkan terus pada kad.</p></div>
   <a class="more" href="#">Lihat semua 34 listing →</a></div>
  <div class="grid">{''.join(card_mt(by(MT, t)) for t in MT_IDS)}</div>
 </div>
</section>
<section>
 <div class="wrap">
  <div class="mapblk">
    <div class="map"><img src="img/peta-mt.webp" width="1200" height="900" loading="lazy" alt="Gambaran kawasan tanah di Hulu Langat">
      <span class="pin">Hulu Langat · Janda Baik · Putrajaya</span></div>
    <div class="side">
      <h3>Cari ikut kawasan</h3>
      <p class="muted" style="font-size:14.5px">Halaman kawasan akan dibina pada Fasa 2 — setiap kawasan mendapat halaman sendiri untuk carian Google.</p>
      <ul class="amin">
        <li><span>Selangor</span><b>20 listing</b></li>
        <li><span>Pahang (Janda Baik dll.)</span><b>4 listing</b></li>
        <li><span>Putrajaya</span><b>4 listing</b></li>
        <li><span>Kuala Lumpur</span><b>3 listing</b></li>
        <li><span>Melaka &amp; N. Sembilan</span><b>3 listing</b></li>
      </ul>
      <p><a class="btn btn-ghost btn-sm" href="#">Buka peta semua listing →</a></p>
    </div>
  </div>
 </div>
</section>
<section class="alt">
 <div class="wrap">
  <div class="sec-head"><div><h2>Kenapa beli tanah melalui Mr Tanah</h2></div></div>
  <div class="tms">
   <div class="tm"><div class="stars" style="color:var(--accent-2)">📄</div><p><b>Semakan dokumen awal.</b> Status hakmilik, sekatan dan guna tanah diperiksa sebelum diterbitkan.</p></div>
   <div class="tm"><div class="stars" style="color:var(--accent-2)">📐</div><p><b>Data teknikal penuh.</b> Keluasan, topografi, akses jalan dan utiliti dipaparkan, bukan sekadar gambar.</p></div>
   <div class="tm"><div class="stars" style="color:var(--accent-2)">🚗</div><p><b>Lawatan tapak diatur.</b> Kami temankan anda ke tapak dan tunjukkan sempadan lot sebenar.</p></div>
  </div>
  <div style="margin-top:20px" class="ribbon">CONTOH — kotak ini boleh diganti dengan testimoni sebenar pembeli tanah</div>
 </div>
</section>
""" + footer("mt")
open(os.path.join(BASE, "mt-utama.html"), "w").write(mt_utama)
# ============================================================ ZMP BUTIRAN
l = by(Z, "COA-0001")
mbl = ansuran(l["price"])
lt, ll = l["title"], l["location"]
G = [f"coa-0001-g{i}" for i in range(1, 7)]
gal = f"""<div class="gal">
 <div class="main"><img id="galMain" src="img/{G[0]}-big.webp" width="1200" height="750" fetchpriority="high"
   data-zoom="img/{G[0]}-big.webp" alt="{lt} — {ll}"></div>
 <div class="thumbs">{''.join(f'<img src="img/{g}-th.webp" width="320" height="320" loading="lazy" data-big="img/{g}-big.webp" data-zoom="img/{g}-big.webp" alt="Foto {i+1} {lt}" class="{"on" if i==0 else ""}">' for i, g in enumerate(G))}</div>
</div>"""

z_det = head(f"MOCK-UP · {l['title']} | Zahir MJ Property", "Cadangan halaman butiran listing.", "zmp")
z_det += mockbar("Halaman: Butiran listing (contoh rumah)") + switcher("zmp-butiran.html")
z_det += header("zmp", "")
z_det += f"""<div class="wrap"><div class="crumbs">Utama › Rumah Subsale › <span class="muted">{l['title']}</span></div></div>
<div class="wrap detail">
 <div>
  {gal}
  <div class="dhead"><h1>{l['title']}</h1>
    <div class="loc" style="font-size:15px">📍 {l['location']} · <span class="muted">{l['tracking']}</span></div></div>
  <div class="blocks" style="margin-top:18px">
   <div class="blk"><h2>Penerangan</h2><p>{l.get('description') or '—'}</p></div>
   <div class="blk"><h2>Sorotan</h2><ul class="hl">{''.join(f'<li>{h}</li>' for h in (l.get('highlights') or []))}</ul></div>
   <div class="tech">
     <div class="hd">Data Teknikal Hartanah <span>Disemak {l.get('date','')}</span></div>
     <table>
       <tr><th>Jenis hartanah</th><td>{l['type']}</td></tr>
       <tr><th>Hakmilik (tenure)</th><td class="ok">{l['tenure']}</td></tr>
       <tr><th>Luas tanah</th><td>{l['land_area']}</td></tr>
       <tr><th>Luas binaan</th><td>{l['built_up']}</td></tr>
       <tr><th>Bilik tidur / bilik air</th><td>{l['bedrooms']} bilik · {l['bathrooms']} bilik air</td></tr>
       <tr><th>Harga per kaki persegi</th><td>RM{l.get('psf') or '—'}/sqft</td></tr>
       <tr><th>Sekatan</th><td>—</td></tr>
       <tr><th>Status</th><td>{l['status']}</td></tr>
     </table>
     <div class="verify"><span>✅ Maklumat hakmilik &amp; status listing disemak oleh ejen berdaftar (PEA 2684).</span>
       <a class="btn btn-ghost btn-sm" href="#">Minta salinan dokumen</a></div>
   </div>
   <div class="blk"><h2>Kemudahan berdekatan</h2>
     <ul class="hl">{''.join(f'<li>{x}</li>' for x in (l.get('amenities') or []))}{''.join(f'<li>{x}</li>' for x in (l.get('nearby') or []))}</ul></div>
   <div class="mapblk">
     <div class="map"><img src="img/{G[2]}-big.webp" width="1200" height="750" loading="lazy" alt="Kawasan sekitar {l['location']}"><span class="pin">{l['location']}</span></div>
     <div class="side"><h3>Lokasi &amp; akses</h3>
       <ul class="amin"><li><span>Keluar lebuhraya</span><b>LEKAS / SILK</b></li>
         <li><span>KTM</span><b>Stesen Bangi</b></li><li><span>Masjid</span><b>±500 m</b></li>
         <li><span>Sekolah</span><b>±1 km</b></li></ul>
       <div style="display:flex;gap:8px;flex-wrap:wrap"><a class="btn btn-navy btn-sm" href="{l['map_url']}" target="_blank" rel="noopener">🗺 Google Maps</a>
         <a class="btn btn-ghost btn-sm" href="https://waze.com/ul?q={quote(l['location'])}" target="_blank" rel="noopener">🚗 Waze</a></div></div>
   </div>
   <div class="blk faq"><h2>Soalan lazim</h2>
     <details open><summary>Boleh saya buat lawatan tapak?</summary><p>Boleh — pilih tarikh pada borang di kanan, kami akan konfirmasi melalui WhatsApp.</p></details>
     <details><summary>Adakah harga boleh dirunding?</summary><p>Harga dan syarat dirunding terus dengan pemilik melalui ejen. Hubungi kami untuk maklumat terkini.</p></details>
     <details><summary>Siapa yang uruskan urusan bank &amp; peguam?</summary><p>Kami boleh cadangkan panel bank dan peguam, tetapi anda bebas memilih.</p></details>
   </div>
   <div class="blk"><h2>Nak lawat unit ini?</h2>
     <p class="muted" style="font-size:14.5px">Isi maklumat ringkas — kami akan WhatsApp anda untuk tetapkan tarikh.</p>
     <div class="form" style="margin-top:12px">
       <div class="fld"><label>Nama</label><input type="text" placeholder="Nama penuh"></div>
       <div class="fld"><label>No. WhatsApp</label><input type="text" placeholder="01x-xxx xxxx"></div>
       <div class="fld full"><label>Tarikh &amp; masa cadangan</label><input type="text" placeholder="cth: Sabtu pagi / Ahad 3 ptg"></div>
       <div class="full"><a class="btn btn-accent" href="temujanji.html?laman=zmp&amp;kod={l['tracking']}&amp;tajuk={quote(l['title'])}" target="_blank" rel="noopener">📅 Isi borang lawatan tapak</a></div>
     </div>
     <p class="note">Mock-up: borang belum disambung. Fasa 2 akan hantar ke Google Sheet + notifikasi WhatsApp.</p></div>
  </div>
 </div>
 <aside class="panel">
   <div class="p">{l['price_label']}</div>
   <div class="psf">RM{l.get('psf') or '—'}/sqft · {l['land_area']}</div>
   <div class="inst">Anggaran ansuran bulanan<b>RM {mbl:,}</b><small style="font-weight:500">4.00% · 35 tahun · 90% pembiayaan</small></div>
   <div class="acts">
     <a class="btn btn-accent" href="{wa_link('60122310119', f"Salam, saya berminat dengan {l['title']} ({l['tracking']}). Boleh saya dapatkan maklumat lanjut dan set tarikh viewing?")}" target="_blank" rel="noopener">💬 Tanya mengenai unit ini</a>
     <a class="btn btn-ghost" href="tel:+60122310119">📞 Panggil {l['tracking'] and '012-2310119'}</a>
     <button class="btn btn-ghost save" data-id="{l['tracking']}" style="position:static;width:auto;height:auto;border-radius:11px">♡ Simpan</button>
   </div>
   <div class="agent"><span class="av">Z</span><div><b>Zahir MJ Property</b><small>Ejen berdaftar PEA 2684 · balas dalam hari sama</small></div></div>
   <p class="note" style="margin-top:14px">Harga &amp; ketersediaan boleh berubah. Sahkan semula sebelum membuat tawaran.</p>
 </aside>
</div>
""" + footer("zmp")
open(os.path.join(BASE, "zmp-butiran.html"), "w").write(z_det)

# ============================================================ MT BUTIRAN TANAH
t = by(MT, "MT-0023")
tt, tl = t["title"], t["location"]
GM = [f"mt-0023-g{i}" for i in range(1, 7)]
galm = f"""<div class="gal">
 <div class="main"><img id="galMain" src="img/{GM[0]}-big.webp" width="1200" height="750" fetchpriority="high"
   data-zoom="img/{GM[0]}-big.webp" alt="{tt} — {tl}"></div>
 <div class="thumbs">{''.join(f'<img src="img/{g}-th.webp" width="320" height="320" loading="lazy" data-big="img/{g}-big.webp" data-zoom="img/{g}-big.webp" alt="Foto {i+1} {tt}" class="{"on" if i==0 else ""}">' for i, g in enumerate(GM))}</div>
</div>"""

ROW_ADA = lambda k, v: f'<tr><th>{k}</th><td>{v}</td></tr>'
ROW_BARU = lambda k: f'<tr><th>{k}</th><td class="muted" style="font-weight:500">Belum ada dalam rekod — perlu diisi <span class="tg gold" style="margin-left:6px">medan baharu</span></td></tr>'

mt_det = head(f"MOCK-UP · {t['title']} | Mr Tanah", "Cadangan halaman butiran tanah Mr Tanah.", "mt",
              listing=f"{t['tracking']} | {t['title']} | {t.get('location','')} | {t.get('price_label','')}")
mt_det += mockbar("Halaman: Butiran TANAH (contoh)") + switcher("mt-butiran-tanah.html")
mt_det += header("mt", "")
mt_det += f"""<div class="wrap"><div class="crumbs">Utama › Tanah › Lot Banglo › <span class="muted">{t['title']}</span></div></div>
<div class="wrap detail">
 <div>
  {galm}
  <div class="dhead"><h1>{t['title']}</h1>
    <div class="loc" style="font-size:15px">📍 {t['location']} · <span class="muted">{t['tracking']}</span></div>
    <div class="tags" style="margin-top:10px">
      <span class="tg g">{t['kategori']}</span><span class="tg g">{t['tenure']}</span>
      <span class="tg">{t['sekatan']}</span><span class="tg">Guna tanah: {t['zoning']}</span></div></div>
  <div class="blocks" style="margin-top:18px">
   <div class="tech">
     <div class="hd">Jadual Data Teknikal Tanah <span>Disemak {t.get('date','')}</span></div>
     <table>
       {ROW_ADA('Keluasan', f"{t['land_area']} · RM{t.get('psf')}/sqft")}
       {ROW_ADA('Pegangan (tenure)', t['tenure'])}
       {ROW_ADA('Kategori guna tanah', t['kategori'])}
       {ROW_ADA('Zoning', t['zoning'])}
       {ROW_ADA('Sekatan', t['sekatan'])}
       {ROW_BARU('Jenis geran (individu / kongsi)')}
       {ROW_BARU('Syarat nyata')}
       {ROW_BARU('Topografi (rata / landai / berbukit)')}
       {ROW_BARU('Akses jalan')}
       {ROW_BARU('Kemudahan asas (TNB / air / telco)')}
       {ROW_BARU('Tanaman sedia ada')}
       {ROW_ADA('Status semakan', f"MyLOT / i-Plan — {t.get('date','')}")}
     </table>
     <div class="verify"><span>✅ Data di atas adalah daripada rekod sedia ada; medan bertanda "medan baharu" perlu diisi oleh pasukan Mr Tanah.</span>
       <a class="btn btn-ghost btn-sm" href="#">Minta pelan &amp; geran</a></div>
   </div>
   <div class="blk"><h2>Penerangan</h2><p>{t.get('description') or '—'}</p></div>
   <div class="blk"><h2>Sorotan</h2><ul class="hl">{''.join(f'<li>{x}</li>' for x in (t.get('highlights') or []))}</ul></div>
   <div class="mapblk">
     <div class="map"><img src="img/peta-mt.webp" width="1200" height="900" loading="lazy" alt="Peta kawasan {t['location']}"><span class="pin">{t['location']}</span></div>
     <div class="side"><h3>Lokasi &amp; akses</h3>
       <ul class="amin">{''.join(f'<li><span>{x.split(" (")[0]}</span><b>{x.split(" (")[1].rstrip(")") if " (" in x else "berdekatan"}</b></li>' for x in (t.get('nearby') or []))}</ul>
       <div style="display:flex;gap:8px;flex-wrap:wrap">
         <a class="btn btn-navy btn-sm" href="{t['map_url']}" target="_blank" rel="noopener">🗺 Google Maps</a>
         <a class="btn btn-ghost btn-sm" href="https://waze.com/ul?q={quote(t['location'])}" target="_blank" rel="noopener">🚗 Waze</a></div>
       <p class="note">Fasa 2: peta interaktif dengan sempadan lot (polygon) yang boleh ditekan.</p></div>
   </div>
   <div class="blk"><h2>Kemudahan &amp; persekitaran</h2><ul class="hl">{''.join(f'<li>{x}</li>' for x in (t.get('amenities') or []))}</ul></div>
   <div class="blk"><h2>Potensi &amp; analisis ringkas</h2>
     <p style="font-size:14.5px">Harga RM{t.get('psf')}/sqft bagi {t['land_area']} dalam kawasan {t['location']}. Pada Fasa 3, blok ini boleh memaparkan carta harga komparabel kawasan (sumber transaksi &amp; iklan sedia ada) supaya pembeli nampak nilai sebenar sebelum berunding.</p>
     <div class="ribbon" style="margin-top:12px">Analisis komparabel = Fasa 3 (perlu data transaksi kawasan)</div></div>
   <div class="blk"><h2>Nak lihat tapak ini?</h2>
     <p class="muted" style="font-size:14.5px">Kami boleh atur lawatan tapak dan tunjukkan sempadan lot serta akses jalan sebenar.</p>
     <div class="cta2" style="margin-top:12px">
       <a class="btn btn-accent" href="{wa_link('60163119076', f"Salam, saya berminat dengan {t['title']} ({t['tracking']}) — {t['location']}. Boleh saya dapatkan maklumat lanjut dan set tarikh lawatan tapak?")}" target="_blank" rel="noopener">💬 Tanya lot ini di WhatsApp</a>
       <a class="btn btn-ghost" href="temujanji.html?laman=mt&amp;kod={t['tracking']}&amp;tajuk={quote(t['title'])}" target="_blank" rel="noopener">📅 Isi borang lawatan tapak</a>
     </div>
     <div class="form" style="margin-top:14px">
       <div class="fld"><label>Nama</label><input type="text" placeholder="Nama penuh"></div>
       <div class="fld"><label>No. WhatsApp</label><input type="text" placeholder="01x-xxx xxxx"></div>
     </div>
     <p class="note">Mock-up: borang belum disambung ke sistem.</p></div>
   <div class="blk faq"><h2>Soalan lazim tentang tanah ini</h2>
     <details open><summary>Apa maksud "Freehold · Open"?</summary><p>Freehold = pegangan kekal; Open = tiada sekatan pemilikan (boleh dimiliki semua kaum).</p></details>
     <details><summary>Boleh bina banglo sendiri?</summary><p>Kategori guna tanah <b>{t['kategori']}</b> dengan zoning <b>{t['zoning']}</b>. Syarat nyata dan had pembangunan perlu disemak di pihak berkuasa tempatan sebelum membina.</p></details>
     <details><summary>Macam mana nak tahu sempadan lot?</summary><p>Pelan sebenar dan pelan sempadan boleh diminta melalui butang "Minta pelan &amp; geran" — dokumen penuh dihantar terus kepada pembeli yang serius.</p></details>
   </div>
  </div>
 </div>
 <aside class="panel">
   <div class="p">{t['price_label']}</div>
   <div class="psf">RM{t.get('psf')}/sqft · {t['land_area']}</div>
   <div class="inst">RUJUKAN PEMAJU &amp; BANK<b>Boleh dirunding</b><small style="font-weight:500">Kami bantu proses pembiayaan tanah</small></div>
   <div class="acts">
     <a class="btn btn-accent" href="{wa_link('60163119076', f"Salam, saya berminat dengan {t['title']} ({t['tracking']}).")}"target="_blank" rel="noopener">💬 WhatsApp Mr Tanah</a>
     <a class="btn btn-ghost" href="tel:+60163119076">📞 016-3119076</a>
     <button class="btn btn-ghost save" data-id="{t['tracking']}" style="position:static;width:auto;height:auto;border-radius:11px">♡ Simpan lot ini</button>
   </div>
   <div class="agent"><span class="av" style="background:var(--accent)">MT</span><div><b>Mr Tanah</b><small>Ejen berdaftar PEA 2684 — pakar tanah</small></div></div>
   <p class="note" style="margin-top:14px">Gambar, keluasan dan status hakmilik disemak sebelum diterbitkan. Pelan &amp; geran penuh hanya diberikan kepada pembeli serius.</p>
 </aside>
</div>
""" + footer("mt")
open(os.path.join(BASE, "mt-butiran-tanah.html"), "w").write(mt_det)

print("SEMUA 5 halaman siap:", sorted(f for f in os.listdir(BASE) if f.endswith(".html")))

