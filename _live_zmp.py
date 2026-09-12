#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Port Fasa 1 (reka bentuk + widget AI) ke repo PRODUKSI Zahir MJ Property (zahir-web)."""
import io, json, os, re, shutil, urllib.request
from PIL import Image

MOCK = "/home/ubuntu/mockup-hartanah"
REPO = "/home/ubuntu/zahir-web"
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
    'window.ALI_LAMAN = "zmp";\n'
    'window.ALI_LISTING_BASE = "listing/";\n')

# ---------- 2. CSS ----------
css_f1 = open(os.path.join(MOCK, "assets/fasa1.css")).read()
scss = os.path.join(REPO, "style.css")
s = open(scss).read()
if "FASA 1 — naik taraf reka bentuk" not in s:
    s = s.rstrip() + "\n\n" + css_f1
    open(scss, "w").write(s)
    print("style.css: blok Fasa 1 ditambah")
else:
    print("style.css: sudah ada blok Fasa 1")

# ---------- 3. imej hero + segmen ----------
for nama, trk, idx, w in (("hero.jpg", "COA-0010", 0, 1600),
                          ("seg-rumah.jpg", "COA-0001", 0, 900),
                          ("seg-apartmen.jpg", "COA-0007", 0, 900),
                          ("seg-komersial.jpg", "COA-0003", 0, 900)):
    out = os.path.join(REPO, "assets", nama)
    if not os.path.exists(out):
        try:
            print(nama, ambil(by(trk)["images"][idx], out, w))
        except Exception as e:
            print("GAGAL", nama, e)

# ---------- 4. index.html ----------
idx_p = os.path.join(REPO, "index.html")
h = open(idx_p).read()
if "hero-f1" not in h:
    hero_baru = '''<section class="hero hero-f1">
  <div class="bg"><img src="assets/hero.jpg" width="1600" height="1067" fetchpriority="high"
    alt="Rumah teres dua tingkat — contoh listing Zahir MJ Property"></div>
  <div class="veil"></div>
  <div class="container">
    <div class="inner">
      <span class="eyebrow">Ejen berdaftar PEA 2684 · Selangor, KL &amp; Putrajaya</span>
      <h1>Cari Hartanah Idaman Anda</h1>
      <p class="lead">Listing terkini dari ejen hartanah profesional — rumah, semi-D, tanah &amp; komersial. Semua unit melalui semakan status pemilikan dan harga pasaran.</p>
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
    </div>
  </div>
</section>

<section class="trust-f1"><div class="container"><ul>
  <li><span class="ic">✅</span>63 listing aktif disemak status pemilikan</li>
  <li><span class="ic">⚡</span>Balasan WhatsApp pada hari sama</li>
  <li><span class="ic">🧮</span>Kalkulator &amp; semak kelayakan percuma</li>
  <li><span class="ic">🤝</span>Ejen berdaftar PEA 2684</li>
</ul></div></section>

<section class="container" style="padding:34px 0 6px">
  <h2 class="f1-hd" style="font-size:clamp(20px,2.4vw,26px);margin-bottom:14px">Mula dari mana?</h2>
  <div class="seg-f1">
    <a class="seg" href="#listing" data-seg="teres">
      <img src="assets/seg-rumah.jpg" width="900" height="600" loading="lazy" alt="Rumah subsale">
      <span class="ov"></span><span class="n">Rumah</span>
      <span class="tx"><h3>Rumah Subsale</h3><p>Rumah teres, semi-D, banglo &amp; apartmen — unit sedia didiami atau direnovasi.</p></span></a>
    <a class="seg" href="#listing" data-seg="apartmen">
      <img src="assets/seg-apartmen.jpg" width="900" height="600" loading="lazy" alt="Apartmen dan kondo">
      <span class="ov"></span><span class="n">Apartmen</span>
      <span class="tx"><h3>Apartmen &amp; Kondo</h3><p>Pilihan rumah pertama dan pelaburan sewa di koridor Bangi – Putrajaya – Cyberjaya.</p></span></a>
    <a class="seg" href="#listing" data-seg="komersial">
      <img src="assets/seg-komersial.jpg" width="900" height="600" loading="lazy" alt="Hartanah komersial">
      <span class="ov"></span><span class="n">Komersial</span>
      <span class="tx"><h3>Komersial</h3><p>Kedai, pejabat &amp; bangunan untuk perniagaan atau pelaburan.</p></span></a>
  </div>
</section>
'''
    # ganti blok hero lama
    m = re.search(r'<section class="hero">.*?</section>', h, re.S)
    if m:
        h = h[:m.start()] + hero_baru + h[m.end():]
        open(idx_p, "w").write(h)
        print("index.html: hero diganti + ditulis")
    else:
        print("AMARAN: blok hero lama tidak dijumpai")

# ---------- 5. skrip Fasa 1 + AI pada SEMUA halaman ----------
skrip = ('<script src="assets/fasa1.js?v=1"></script>\n'
         '<script src="assets/ali-config.js?v=1"></script>\n'
         '<script src="assets/ali-chat.js?v=1"></script>\n')
diubah = 0
for akar, _, fail in os.walk(REPO):
    if "/.git" in akar or "/assets" in akar:
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
print(f"skrip disuntik ke {diubah} halaman")

# ---------- 6. app.js: kad v2 ----------
ap = os.path.join(REPO, "app.js")
a = open(ap).read()
if "f1-save" not in a:
    a = a.replace('''  return `<a class="card-media" href="${link}" aria-label="${l.title}">
    ${inner}
    <div class="badges">${badges.join("")}</div>
  </a>`;''',
'''  const bil = (l.images && l.images.length) ? l.images.length : 0;
  const kira = bil > 1 ? `<span class="phcount">📷 ${bil}</span>` : "";
  return `<a class="card-media" href="${link}" aria-label="${l.title}">
    ${inner}
    <div class="badges">${badges.join("")}</div>
    ${kira}
  </a>`;''')
    a = a.replace('''  const oldPrice = l.price_old ? `<span class="price-old">${fmt(l.price_old)}</span>` : "";''',
'''  const oldPrice = l.price_old ? `<span class="price-old">${fmt(l.price_old)}</span>` : "";
  // anggaran ansuran (4.00% p.a., 35 tahun, 90% pembiayaan)
  let inst = "";
  if (l.price) {
    const loan = l.price * 0.9, r = 0.04 / 12, n = 35 * 12;
    const m = Math.round(loan * r / (1 - Math.pow(1 + r, -n)));
    inst = `<div class="price-inst">~ ${fmt(m)}/bln (anggaran)</div>`;
  }''')
    a = a.replace('''      <div class="price-row"><span class="price">${l.price_label}</span>${oldPrice}</div>''',
'''      <div class="price-row"><span class="price">${l.price_label}</span>${oldPrice}</div>
      ${inst}''')
    open(ap, "w").write(a)
    print("app.js: kad v2 (kiraan gambar + anggaran ansuran) ditambah")
else:
    print("app.js: sudah dikemas kini")
print("SIAP")
