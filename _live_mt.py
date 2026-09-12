#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Port Fasa 1 (reka bentuk + widget AI) ke repo PRODUKSI Mr Tanah (mrtanah-site)."""
import io, json, os, re, shutil, urllib.request
from PIL import Image

MOCK = "/home/ubuntu/mockup-hartanah"
REPO = "/home/ubuntu/mrtanah-site"
UA = {"User-Agent": "Mozilla/5.0"}


def load(p):
    s = open(p).read()
    return json.loads(s[s.index("window.LISTINGS"):].split("=", 1)[1].rsplit(";", 1)[0])


def ambil(url, out, w=1600, q=80):
    d = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
    im = Image.open(io.BytesIO(d)).convert("RGB")
    if im.width > w:
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    im.save(out, "JPEG", quality=q, optimize=True, progressive=True)
    return os.path.getsize(out)


L = load(os.path.join(REPO, "data/listings.js"))
by = lambda t: [x for x in L if x["tracking"] == t][0]

# ---------- 1. aset ----------
os.makedirs(os.path.join(REPO, "assets/fonts"), exist_ok=True)
for f in ("PlusJakartaSans-var.woff2", "Inter-var.woff2"):
    shutil.copy(os.path.join(MOCK, "assets/fonts", f), os.path.join(REPO, "assets/fonts", f))
for f in ("ali-chat.js", "fasa1.js"):
    shutil.copy(os.path.join(MOCK, "assets", f), os.path.join(REPO, "assets", f))
open(os.path.join(REPO, "assets/ali-config.js"), "w").write(
    '/* Endpoint AI "Tanya Ali" (produksi) */\n'
    'window.ALI_API_BASE = "https://api.zahirmjproperty.com";\n'
    'window.ALI_LAMAN = "mt";\n'
    'window.ALI_LISTING_BASE = "listing/";\n')

# ---------- 2. CSS (+ aksen zamrud MT) ----------
css_f1 = open(os.path.join(MOCK, "assets/fasa1.css")).read()
mt_aksen = """
/* Mr Tanah — aksen zamrud (tanah/alam) */
:root{--accent:#059669;--accent-soft:#E6F6F0}
.hero{background:linear-gradient(135deg,#0A1120 0%,#0E3A2C 55%,#059669 100%)}
.f1-bar .f1-b2{background:var(--accent)}
.tech-f1 .verify{background:var(--accent-soft);border-top-color:#BFE6D5;color:#047857}
.f1-tags .tg.g{background:var(--accent-soft);border-color:#BFE6D5;color:#047857}
"""
scss = os.path.join(REPO, "style.css")
s = open(scss).read()
if "FASA 1 — naik taraf reka bentuk" not in s:
    s = s.rstrip() + "\n\n" + css_f1 + mt_aksen
    open(scss, "w").write(s)
    print("style.css MT: blok Fasa 1 + aksen zamrud ditambah")
else:
    print("style.css MT: sudah ada")

# ---------- 3. imej ----------
for nama, trk, idx, w in (("hero.jpg", "MT-0006", 4, 1600),
                          ("seg-pertanian.jpg", "MT-0001", 0, 900),
                          ("seg-banglo.jpg", "MT-0004", 0, 900),
                          ("seg-komersial.jpg", "MT-0019", 0, 900)):
    out = os.path.join(REPO, "assets", nama)
    if not os.path.exists(out):
        try:
            print(nama, ambil(by(trk)["images"][idx], out, w))
        except Exception as e:
            print("GAGAL", nama, e)

# ---------- 4. index.html: hero + trust + segmen ----------
idx_p = os.path.join(REPO, "index.html")
h = open(idx_p).read()
if "hero-f1" not in h:
    hero = '''<section class="hero hero-f1">
  <div class="bg"><img src="assets/hero.jpg" width="1600" height="1200" fetchpriority="high"
    alt="Pemandangan udara kawasan tanah — contoh listing Mr Tanah"></div>
  <div class="veil"></div>
  <div class="container"><div class="inner">
    <span class="eyebrow">Pakar tanah &amp; lot banglo · PEA 2684</span>
    <h1>Cari Tanah &amp; Lot Banglo</h1>
    <p class="lead">Tanah pertanian, lot banglo geran individu, komersial &amp; industri. Kami paparkan keluasan, hakmilik, sekatan dan guna tanah — supaya anda boleh buat keputusan dengan yakin.</p>
    <div class="search-panel" id="searchPanel">
      <div class="deal-tabs" id="dealTabs">
        <button type="button" class="deal-tab active" data-deal="">Semua</button>
        <button type="button" class="deal-tab" data-deal="JUAL">Jual</button>
        <button type="button" class="deal-tab" data-deal="SEWA">Sewa</button>
        <button type="button" class="deal-tab" data-deal="JV">JV</button>
      </div>
      <div class="search-row">
        <input type="text" id="searchInput" placeholder="Cari lokasi, jenis hartanah..." autocomplete="off">
        <select id="stateFilter" aria-label="Negeri"><option value="">Semua Negeri</option></select>
        <select id="typeFilter" aria-label="Jenis"><option value="">Semua Jenis</option></select>
      </div>
      <div class="search-row search-row-2">
        <div class="price-field"><span>Harga min</span>
          <input type="number" id="minPrice" placeholder="cth: 500000" min="0" step="10000"></div>
        <div class="price-field"><span>Harga maks</span>
          <input type="number" id="maxPrice" placeholder="cth: 1000000" min="0" step="10000"></div>
        <select id="sortSelect" aria-label="Susun">
          <option value="newest">Terbaru</option>
          <option value="priceAsc">Harga: Rendah → Tinggi</option>
          <option value="priceDesc">Harga: Tinggi → Rendah</option>
        </select>
        <button class="btn btn-clear" id="clearBtn" type="button">Reset</button>
      </div>
    </div>
  </div></div>
</section>

<section class="trust-f1"><div class="container"><ul>
  <li><span class="ic">🗺️</span>34 listing tanah aktif disemak</li>
  <li><span class="ic">📄</span>Status hakmilik &amp; sekatan dijelaskan awal</li>
  <li><span class="ic">📐</span>Data teknikal tanah dipaparkan</li>
  <li><span class="ic">🤝</span>Ejen berdaftar PEA 2684</li>
</ul></div></section>

<section class="container" style="padding:34px 0 6px">
  <h2 class="f1-hd" style="font-size:clamp(20px,2.4vw,26px);margin-bottom:14px">Pilih jenis tanah</h2>
  <div class="seg-f1">
    <a class="seg" href="#listing" data-seg="tanah">
      <img src="assets/seg-pertanian.jpg" width="900" height="600" loading="lazy" alt="Tanah pertanian">
      <span class="ov"></span><span class="n">Pertanian</span>
      <span class="tx"><h3>Tanah Pertanian &amp; Dusun</h3><p>Sawit, getah, dusun durian, tanah tepi sungai — untuk pertanian &amp; pelaburan.</p></span></a>
    <a class="seg" href="#listing" data-seg="bangunan">
      <img src="assets/seg-banglo.jpg" width="900" height="600" loading="lazy" alt="Lot banglo">
      <span class="ov"></span><span class="n">Lot Banglo</span>
      <span class="tx"><h3>Lot Banglo</h3><p>Lot sedia bina, geran individu, kawasan berpagar atau berhampiran bandar.</p></span></a>
    <a class="seg" href="#listing" data-seg="komersial">
      <img src="assets/seg-komersial.jpg" width="900" height="600" loading="lazy" alt="Tanah komersial dan industri">
      <span class="ov"></span><span class="n">Komersial</span>
      <span class="tx"><h3>Komersial &amp; Industri</h3><p>Tanah komersial, industri &amp; bangunan — potensi pembangunan.</p></span></a>
  </div>
</section>
'''
    m = re.search(r'<section class="hero">.*?</section>', h, re.S)
    if m:
        h = h[:m.start()] + hero + h[m.end():]
        open(idx_p, "w").write(h)
        print("index.html MT: hero diganti + ditulis")
    else:
        print("AMARAN MT: blok hero tidak dijumpai")

# ---------- 5. suntik skrip (langkau preview/) ----------
skrip = ('<script src="assets/fasa1.js?v=1"></script>\n'
         '<script src="assets/ali-config.js?v=1"></script>\n'
         '<script src="assets/ali-chat.js?v=1"></script>\n')
diubah = 0
for akar, _, fail in os.walk(REPO):
    a = akar.replace("\\", "/")
    if "/.git" in a or "/assets" in a or "preview" in a:
        continue
    for f in fail:
        if not f.endswith(".html"):
            continue
        p = os.path.join(akar, f)
        rel = os.path.relpath(REPO, os.path.dirname(p)).replace("\\", "/") or "."
        pre = "" if rel == "." else rel + "/"
        t = open(p).read()
        if "ali-chat.js" in t:
            continue
        s2 = re.sub(r"(</body>)", skrip.replace("assets/", pre + "assets/") + r"\1", t, count=1)
        if s2 != t:
            open(p, "w").write(s2)
            diubah += 1
print(f"MT: skrip disuntik ke {diubah} halaman")

# ---------- 6. listing.js: jadual data teknikal tanah ----------
lp = os.path.join(REPO, "listing.js")
t = open(lp).read()
if "tech-f1" not in t:
    t = t.replace('''  if (l.psf) rows.push(["Harga Tanah (psf)", "RM" + l.psf.toLocaleString("en-MY") + "/sqft"]);
  return `<table class="spec-table">${rows.map(r => `<tr><th>${r[0]}</th><td>${r[1]}</td></tr>`).join("")}</table>`;''',
'''  if (l.psf) rows.push(["Harga Tanah (psf)", "RM" + l.psf.toLocaleString("en-MY") + "/sqft"]);
  // Fasa 1: medan teknikal baharu — papar jika ada, tandakan jika belum ada rekod
  const baharu = [["Jenis Geran", l.jenis_geran], ["Syarat Nyata", l.syarat_nyata],
                  ["Topografi", l.topografi], ["Akses Jalan", l.akses_jalan],
                  ["Kemudahan Asas", l.utiliti], ["Tanaman Sedia Ada", l.tanaman]];
  const kurang = [];
  baharu.forEach(function (b) {
    if (b[1] === "" || b[1] === "-" || b[1]) { if (b[1]) rows.push(b); else kurang.push(b[0]); }
    else kurang.push(b[0]);
  });
  const isTanah = (l.type === "Tanah");
  const jadual = `<table class="${isTanah ? "spec-table" : "spec-table"}">${rows.map(r => `<tr><th>${r[0]}</th><td>${r[1]}</td></tr>`).join("")}</table>`;
  if (isTanah && kurang.length) {
    return `<div class="tech-f1"><div class="hd">Jadual Data Teknikal Tanah <span>Disemak ${l.date || ""}</span></div>` +
      jadual +
      `<div class="verify"><span>Sedang dilengkapkan: ${kurang.join(", ")} — sila WhatsApp kami untuk maklumat terkini.</span></div></div>`;
  }
  if (isTanah) {
    return `<div class="tech-f1"><div class="hd">Jadual Data Teknikal Tanah <span>Disemak ${l.date || ""}</span></div>` + jadual +
      `<div class="verify"><span>✅ Maklumat hakmilik &amp; status listing disemak oleh ejen berdaftar (PEA 2684).</span></div></div>`;
  }
  return jadual;''')
    open(lp, "w").write(t)
    print("listing.js MT: jadual data teknikal ditambah")
else:
    print("listing.js MT: sudah ada")

# ---------- 7. app.js MT: kiraan gambar + anggaran ansuran ----------
ap = os.path.join(REPO, "app.js")
a = open(ap).read()
if "phcount" not in a:
    a = a.replace('''    <div class="badges">${badges.join("")}</div>''',
'''    <div class="badges">${badges.join("")}</div>
    ${(l.images && l.images.length > 1) ? `<span class="phcount">📷 ${l.images.length}</span>` : ""}''')
    open(ap, "w").write(a)
    print("app.js MT: kiraan gambar ditambah")
else:
    print("app.js MT: sudah ada")
print("SIAP MT")
