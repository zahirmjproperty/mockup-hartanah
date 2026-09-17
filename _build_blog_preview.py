#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Penjana PRATONTON blog "Isu Tanah RM450K" untuk DUA jenama (Mr Tanah + Zahir MJ Property).

Prinsip (skill static-site-design-rollout):
  - JANGAN salin aset: salin header/footer daripada halaman PRODUKSI, tulis semula laluan
    aset kepada URL MUTLAK domain masing-masing.
  - Setiap penggantian mesti GAGAL KUAT (raise SystemExit) kalau teks sumber tiada.
  - Setiap halaman: noindex + bar "PRATONTON — bukan laman produksi".
Keluaran: /home/ubuntu/mockup-hartanah/blog-isu-tanah/{index,mt-blog,mt-artikel,zmp-blog,zmp-artikel}.html
"""
import os
import re

MT_REPO = "/home/ubuntu/mrtanah-site"
ZMP_REPO = "/home/ubuntu/zahir-web"
MT_BASE = "https://mrtanah.com/"
ZMP_BASE = "https://zahirmjproperty.com/"
OUT = "/home/ubuntu/mockup-hartanah/blog-isu-tanah"
os.makedirs(OUT, exist_ok=True)


def baca(p):
    return open(p, encoding="utf-8").read()


def kerat(html, mula, akhir, label):
    i = html.find(mula)
    j = html.find(akhir, i)
    if i < 0 or j < 0:
        raise SystemExit(f"GAGAL: blok '{label}' tidak dijumpai")
    return html[i:j + len(akhir)]


def ganti(t, lama, baharu, label):
    n = t.count(lama)
    if n == 0:
        raise SystemExit(f"GAGAL: teks tidak dijumpai untuk '{label}'")
    print(f"  ok  {label}: {n} padanan")
    return t.replace(lama, baharu)


def absolut(blk, base):
    blk = blk.replace('href="/"', f'href="{base}"')
    blk = blk.replace('href="/#', f'href="{base}#')
    blk = blk.replace('src="/', f'src="{base}')
    blk = re.sub(r'(src|href)="(?!https?:|#|mailto:|tel:|data:)([^"]+)"',
                 lambda m: f'{m.group(1)}="{base}{m.group(2)}"', blk)
    return blk


BANNER = ('<div style="background:#0f172a;color:#fff;font:600 13px/1.5 system-ui,sans-serif;'
          'padding:9px 14px;text-align:center">PRATONTON — bukan laman produksi · '
          '<a href="index.html" style="color:#7ee2a8">hub pratonton</a></div>\n')

NOINDEX = '<meta name="robots" content="noindex,nofollow">'

TAJUK = "Tanah RM450K, Tiada Jalan Masuk: 7 Semakan Sebelum Anda Bayar"
DESK = ("Isu tanah RM450,000 tanpa jalan masuk tular Julai 2026. Ini 7 semakan wajib — carian hakmilik, "
        "rezab jalan, ismen, hak lalulalang Borang 28A — sebelum anda bayar.")

ARTIKEL = [
    '<p class="about-bio" style="color:#6f7d88;font-size:14px">Artikel · 6 minit bacaan · 18 September 2026 '
    '· oleh <strong>Zahir MJ</strong> (Ejen Hartanah Berdaftar, PEA 2684)</p>',

    '<h2>Tanah dibeli tunai, jalan masuk jadi masalah</h2>',
    '<p>Julai 2026, seorang usahawan kosmetik tampil di media sosial meluahkan rasa terkilan. Katanya dia '
    'membeli sebidang tanah secara tunai bernilai <strong>RM450,000</strong>, tetapi tersekat apabila berdepan '
    'masalah jalan masuk ke tanah itu. Lebih rumit, dia mendakwa sebahagian kawasan yang dipagar sebenarnya '
    'terletak atas tanah milik orang lain.</p>',
    '<p>Agensi hartanah yang mengendalikan urus niaga tersebut, <strong>Landsworth Properties Sdn Bhd '
    '(E(1)1959)</strong>, mengeluarkan kenyataan rasmi pada 17 Julai 2026. Antara yang dinyatakan:</p>',
    '<blockquote style="border-left:3px solid #059669;margin:14px 0;padding:6px 0 6px 16px;color:#37474f">'
    '<p>Pihak agensi memandang serius perkara itu dan sedang menjalankan semakan menyeluruh — meneliti semua '
    'dokumen, rekod komunikasi serta mendapatkan penjelasan daripada REN yang terlibat bagi memastikan isu '
    'dinilai secara adil, telus dan berdasarkan fakta. Agensi menghormati hak semua pihak untuk mendapatkan '
    'penyelesaian melalui saluran undang-undang, dan meminta orang ramai <strong>tidak membuat sebarang andaian '
    'atau spekulasi</strong> sehingga semakan selesai. Pihaknya juga menegaskan akan melindungi hak dan reputasi '
    'agensi, kakitangan serta REN di bawahnya, dan tindakan undang-undang boleh diambil sekiranya terdapat '
    'penyebaran kenyataan palsu, mengelirukan atau berunsur fitnah.</p></blockquote>',
    '<p><em>Kenyataan itu dipetik sepertimana dilaporkan media. Kes ini belum diputuskan oleh mana-mana '
    'mahkamah, dan kami tidak membuat tuduhan terhadap mana-mana pihak.</em></p>',

    '<h2>Kenapa jalan masuk boleh jadi mimpi ngeri</h2>',
    '<p>Tanah di Malaysia tidak semestinya mempunyai jalan keluar ke jalan awam. Dalam urusan tanah, keadaan '
    'ini dipanggil <strong>tanah terkunci</strong> — tanah lapisan kedua atau ketiga yang tidak bersempadan '
    'dengan jalan. Tiga punca yang paling kerap:</p>',
    '<ol><li><strong>Tiada rezab jalan sejak awal.</strong> Tanah pertanian lama dipecah tanpa menyediakan jalan '
    'untuk lot belakang. Lot depan kemudian membina rumah dan menutup habis tanahnya.</li>',
    '<li><strong>Laluan ikut tanah orang tanpa hak berdaftar.</strong> Ada "izin" lisan atau persefahaman baik '
    'antara jiran. Bila tanah bertukar tangan, izin itu tamat.</li>',
    '<li><strong>Pagar melebihi sempadan.</strong> Jiran atau penjual asal memagar lebih daripada hakmiliknya — '
    'sedangkan di atas geran, garisan itu jelas lain.</li></ol>',
    '<p>Kesannya bukan sekadar susah masuk kereta. Tanah tanpa akses sukar dimajukan, sukar mendapat kelulusan '
    'pelan bangunan, sukar dinilaikan bank, dan harganya boleh jatuh jauh di bawah harga yang anda bayar.</p>',

    '<h2>7 semakan sebelum anda bayar</h2>',
    '<h3>1. Carian rasmi di Pejabat Tanah — jangan bergantung pada salinan geran penjual</h3>',
    '<p>Minta <strong>carian hakmilik rasmi</strong>, bukan salinan foto geran. Semak nama pemilik berdaftar, '
    'luas, bebanan (gadaian, kaveat, lien), sekatan kepentingan dan kategori kegunaan tanah. Kalau nama di geran '
    'bukan nama pihak yang anda berurusan dengannya, berhenti dan tanya — banyak penipuan tanah bermula di situ.</p>',

    '<h3>2. Sahkan akses, bukan andaikan akses</h3>',
    '<p>Tanya satu soalan tepat kepada penjual atau ejen: <strong>"Jalan masuk ke tanah ini apa statusnya?"'
    '</strong> Hanya tiga jawapan yang boleh diterima:</p>',
    '<ul><li>Tanah bersempadan terus dengan <strong>jalan kerajaan yang digazet</strong>; atau</li>',
    '<li>Ada <strong>ismen (easement) yang didaftarkan</strong> atas tanah jiran untuk laluan — ismen wajib '
    'didaftarkan (s.286 Kanun Tanah Negara), dan ismen yang tidak didaftarkan tidak boleh dikuatkuasakan; atau</li>',
    '<li>Ada <strong>hak lalulalang Pentadbir Tanah</strong> yang sudah diwujudkan dan dimemorialkan dalam geran.</li></ul>',
    '<p>"Boleh lalu, semua orang lalu" bukan status. Itu kebiasaan — dan kebiasaan boleh berubah bila jiran bertukar.</p>',

    '<h3>3. Ukur sempadan sebelum percaya pagar</h3>',
    '<p>Lantik <strong>juruukur tanah berlesen</strong> untuk sahkan sempadan sebenar. Ia kos tambahan, tetapi jauh '
    'lebih murah daripada membeli tanah yang sebahagiannya milik orang lain. Dalam kes tular di atas, dakwaan '
    '"pagar terletak atas tanah orang lain" itulah yang menjadikan urusan itu berbelit.</p>',

    '<h3>4. Semak kategori tanah dan apa yang dibenarkan</h3>',
    '<p>Tanah pertanian tidak boleh terus dibina rumah tanpa kelulusan tukar syarat. Tanah Simpanan Melayu / lot '
    'Bumiputera ada sekatan pemilikan dan pindahmilik. Semak juga zoning dengan pihak berkuasa tempatan — termasuk '
    'sama ada tanah itu berada dalam kawasan rezab yang akan diambil untuk jalan atau pembangunan.</p>',

    '<h3>5. Jangan bayar tunai tanpa struktur yang betul</h3>',
    '<p>Pembayaran tunai besar tanpa instrumen berdaftar adalah risiko yang paling senang dielak. Amalan yang '
    'betul: perjanjian jual beli disediakan peguam anda sendiri, wang dipegang sebagai <em>stakeholder</em>, '
    'pindahmilik didaftarkan, dan hak anda dilindungi melalui kaveat/lien sebelum bayaran penuh dilepaskan. '
    'Kalau penjual mendesak tunai "sekarang juga", itu bendera merah.</p>',

    '<h3>6. Semak latar ejen dan firma — dan faham peranan mereka</h3>',
    '<p>Ejen hartanah berdaftar wajib memaparkan nama, nombor pendaftaran (REN/PEA) dan nombor firma (E) pada iklan. '
    'Ejen juga tidak boleh memberi kenyataan mengelirukan tentang status akses tanah. Jika maklumat yang diberikan '
    'terbukti tidak benar, pembeli boleh mengemukakan aduan kepada <strong>Lembaga Penilai, Pentaksir dan Ejen '
    'Hartanah (LPEPH)</strong>. Satu lagi: ejen hartanah tidak boleh memegang wang pelanggan bagi urusan pemilikan '
    'tanah — bayaran hendaklah melalui peguam atau pihak berkuasa berkanun.</p>',

    '<h3>7. Kalau sudah terkunci, ini jalan penyelesaiannya</h3>',
    '<p>Anda tidak semestinya terperangkap. Dua saluran:</p>',
    '<ul><li><strong>Ismen (rundingan).</strong> Runding dengan pemilik tanah lapisan hadapan untuk membeli '
    'sebahagian laluan atau mewujudkan hak laluan — kemudian <strong>daftarkan</strong> ismen tersebut.</li>',
    '<li><strong>Hak lalulalang Pentadbir Tanah.</strong> Jika rundingan gagal, pemilik tanah boleh memohon kepada '
    'Pentadbir Tanah untuk mewujudkan hak lalulalang melalui <strong>Borang 28A (s.390 KTN)</strong>. Jika sudah ada '
    'hak lalulalang sedia ada, boleh mohon berkongsi melalui <strong>Borang 28C (s.394)</strong>. Bila perintah '
    'dibuat, hak itu dimemorialkan ke atas geran (<strong>Borang 28B, s.391</strong>) — bermakna ia kekal berdaftar '
    'dan terikat pada tanah, bukan bergantung pada budi bicara sesiapa.</li></ul>',
    '<p>Proses ini makan masa, ada kos ukur dan pampasan, dan pihak Pentadbir biasanya menggalakkan penyelesaian '
    'ismen dahulu. Tetapi ia wujud — dan itulah sebabnya status akses <strong>wajib</strong> disahkan '
    '<em>sebelum</em> wang bertukar tangan, bukan selepas.</p>',

    '<h2>Bagaimana kami uruskan isu ini</h2>',
    '<p>Tanah ialah sebahagian besar urus niaga kami. Sebab itu setiap listing tanah kami rekod '
    '<strong>status akses</strong> (bersempadan jalan digazet / ada ismen berdaftar / belum ada akses berdaftar), '
    'dan kami sebut perkara ini di depan, bukan sembunyi dalam lampiran.</p>',
    '<p>Kami juga tidak memaparkan gambar geran atau pelan hakmilik di laman awam. Dokumen hakmilik adalah untuk '
    'pemeriksaan pembeli serius, melalui kami, dengan kehadiran pemilik — bukan ditayang sebagai bahan jualan.</p>',
]

FAQ = [
    ("Boleh ke beli tanah yang tiada jalan masuk?",
     "Boleh dari segi undang-undang, tetapi ia urusan berisiko tinggi. Sebelum bayar, pastikan sama ada akses boleh "
     "diwujudkan melalui ismen berdaftar atau permohonan hak lalulalang kepada Pentadbir Tanah (Borang 28A, s.390 KTN). "
     "Jika tiada jalan penyelesaian yang jelas, harga tanah itu tidak boleh dinilai seperti tanah yang bersempadan jalan."),
    ("Apa beza ismen dan hak lalulalang Pentadbir Tanah?",
     "Ismen ialah hak yang diwujudkan melalui <strong>persetujuan</strong> antara pemilik tanah, lalu didaftarkan ke atas "
     "hakmilik (Borang 17A, s.286 KTN). Hak lalulalang Pentadbir Tanah pula <strong>diwujudkan oleh perintah Pentadbir "
     "Tanah</strong> apabila tiada persetujuan dicapai (s.388–391 KTN), dan perintah itu dimemorialkan ke atas geran "
     "supaya ia mengikat pemilik-pemilik kemudian."),
    ("Berapa lama dan berapa kos proses hak lalulalang?",
     "Tempoh bergantung kepada pejabat tanah dan sama ada ada bantahan; dalam pengalaman am ia mengambil beberapa bulan, "
     "bukan minggu. Ada kos ukur dan pampasan kepada pemilik tanah yang dilalui. Angka tepat perlu disemak dengan "
     "pejabat tanah daerah berkenaan — kami tidak mahu memberi angka yang tidak sahih."),
]

RUJUKAN = [
    "Kenyataan rasmi Landsworth Properties Sdn Bhd bertarikh 17 Julai 2026 (sepertimana dilaporkan Oh! Media / Newswav).",
    "Kanun Tanah Negara 1965 — s.282–291 (ismen), s.388–391 (hak lalulalang Pentadbir Tanah); Borang 28A (s.390), "
    "28B (s.391), 28C (s.394).",
    "Borang rasmi hak lalulalang pejabat tanah negeri (contoh Borang 28A/28B/28C — PTG Melaka, PTG Perak).",
]


def badan_artikel(jenama, lain):
    h = ['<section class="about-section">']
    h += ARTIKEL
    h.append('</section>')
    h.append('<section class="about-section"><h2>Soalan Lazim</h2>')
    for s, j in FAQ:
        h.append(f'<details class="faq"><summary>{s}</summary><p>{j}</p></details>')
    h.append('</section>')
    h.append('<section class="cta-card"><h2>Nak semak status akses tanah anda?</h2>'
             '<p>Hantar maklumat lot dan geran — kami semak akses, sekatan dan kategori tanah sebelum anda buat tawaran.</p>'
             '<div class="cta-actions">'
             '<a class="btn btn-wa" href="https://wa.me/60163119076?text=Assalamualaikum%20dan%20salam%20sejahtera%2C%20'
             'saya%20nak%20semak%20status%20akses%20tanah." target="_blank" rel="noopener">📲 WhatsApp</a>'
             f'<a class="btn btn-outline" href="{lain}">Lihat versi jenama satu lagi</a></div></section>')
    h.append('<section class="about-section"><h2>Rujukan</h2><ul>')
    for r in RUJUKAN:
        h.append(f'<li>{r}</li>')
    h.append('</ul><p style="color:#6f7d88;font-size:13px">Artikel ini maklumat am, bukan nasihat guaman. Setiap urus '
             'niaga tanah ada faktanya sendiri — dapatkan nasihat peguam anda sendiri.</p></section>')
    h.append('<section class="about-section"><p class="about-bio">'
             f'{jenama} · Zahiruddin bin Mat Jailaini (PEA 2684) · IQI Realty Sdn Bhd (E(1)1584)</p></section>')
    return "\n".join(h)


def halaman(tajuk, deskripsi, hero_h1, hero_p, isi, repo, base, nav_blog, aktif):
    src = baca(os.path.join(repo, "tentang.html"))
    header = absolut(kerat(src, '<header class="site-header">', "</header>", "header"), base)
    footer = absolut(kerat(src, '<footer class="site-footer">', "</footer>", "footer"), base)
    # tambah item nav "Artikel" pada pratonton (cadangan struktur blog)
    lama_nav = f'<a href="{base}tentang.html" class="active">Tentang</a>'
    cls_art = ' class="active"' if aktif == "artikel" else ""
    cls_tta = ' class="active"' if aktif == "tentang" else ""
    baharu_nav = (f'<a href="{nav_blog}"{cls_art}>Artikel</a>\n'
                  f'      <a href="{base}tentang.html"{cls_tta}>Tentang</a>')
    header2 = ganti(header, lama_nav, baharu_nav, "nav Artikel")
    return f"""<!DOCTYPE html>
<html lang="ms">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{NOINDEX}
<title>{tajuk}</title>
<meta name="description" content="{deskripsi}">
<link rel="stylesheet" href="{base}style.css?v=67">
</head>
<body>
{BANNER}{header2}

<section class="hero hero-about">
  <div class="container">
    <h1>{hero_h1}</h1>
    <p>{hero_p}</p>
  </div>
</section>

<main class="container main about-wrap">
{isi}
</main>

{footer}
</body>
</html>
"""


def kad(link, tajuk, ringkas, status, jenis=""):
    tanda = ('<span style="display:inline-block;background:#e6f6f0;color:#047857;border-radius:999px;'
             'padding:2px 10px;font-size:12px;font-weight:600">Siap</span>') if status == "siap" else \
            ('<span style="display:inline-block;background:#f1f3f5;color:#6f7d88;border-radius:999px;'
             'padding:2px 10px;font-size:12px;font-weight:600">Akan datang</span>')
    return (f'<a class="service" href="{link}"><span class="s-icon">{jenis}</span>'
            f'<h3>{tajuk}</h3><p>{ringkas}</p>{tanda}</a>')


def badan_blog(base_blog):
    h = ['<section class="about-section"><h2>Artikel &amp; Panduan</h2>',
         '<p class="about-bio">Panduan praktikal tentang tanah dan hartanah di Malaysia — ditulis supaya '
         'pembeli faham risikonya sebelum bayar.</p>',
         '<div class="service-grid">',
         kad("artikel.html", "Tanah RM450K, Tiada Jalan Masuk: 7 Semakan Sebelum Anda Bayar",
             "Isu viral Julai 2026 dijadikan pelajaran: cara sahkan akses, ismen dan hak lalulalang (Borang 28A) "
             "sebelum wang bertukar tangan.", "siap", "🌳"),
         kad("#", "Penyewa Bermasalah: Hak Pemilik Tanpa Akta Sewa Kediaman",
             "Apa yang boleh dan tidak boleh dibuat pemilik apabila penyewa enggan keluar — dan kenapa perjanjian "
             "sewa bertulis penting. <em>Belum ditulis.</em>", "akan datang", "🔑"),
         kad("#", "Rumah Siap Tak Terjual (Overhang): Apa Maksudnya Untuk Penjual",
             "33,094 unit siap tak terjual (NAPIC 1H2026) — apa yang pembeli dan penjual perlu faham tentang "
             "harga, lokasi dan kelayakan pinjaman. <em>Belum ditulis.</em>", "akan datang", "🏠"),
         '</div></section>',
         '<section class="cta-card"><h2>Nak cadangan topik artikel?</h2>'
         '<p>Beritahu kami soalan yang paling kerap pelanggan tanya — kami tulis jawapannya.</p>'
         '<div class="cta-actions"><a class="btn btn-wa" href="https://wa.me/60163119076" target="_blank" '
         'rel="noopener">📲 WhatsApp</a></div></section>']
    return "\n".join(h)


# ---------------------------------------------------------------- jana halaman
print("=== artikel ===")
p_art = os.path.join(OUT, "mt-artikel.html")
open(p_art, "w", encoding="utf-8").write(halaman(
    f"{TAJUK} — Mr Tanah", DESK, TAJUK, "Mr Tanah · Artikel pematuhan &amp; panduan tanah",
    badan_artikel("Mr Tanah", "zmp-artikel.html"), MT_REPO, MT_BASE, "mt-blog.html", "artikel"))
p_art2 = os.path.join(OUT, "zmp-artikel.html")
open(p_art2, "w", encoding="utf-8").write(halaman(
    f"{TAJUK} — Zahir MJ Property", DESK, TAJUK, "Zahir MJ Property · Artikel pematuhan &amp; panduan hartanah",
    badan_artikel("Zahir MJ Property", "mt-artikel.html"), ZMP_REPO, ZMP_BASE, "zmp-blog.html", "artikel"))

print("=== indeks blog ===")
p_blog = os.path.join(OUT, "mt-blog.html")
open(p_blog, "w", encoding="utf-8").write(halaman(
    "Artikel &amp; Panduan — Mr Tanah", "Panduan tanah & hartanah Malaysia: semakan sebelum beli, sewa dan "
    "pematuhan.", "Artikel &amp; Panduan", "Mr Tanah · Panduan tanah &amp; hartanah",
    badan_blog("mt"), MT_REPO, MT_BASE, "mt-blog.html", "artikel"))
p_blog2 = os.path.join(OUT, "zmp-blog.html")
open(p_blog2, "w", encoding="utf-8").write(halaman(
    "Artikel &amp; Panduan — Zahir MJ Property", "Panduan tanah & hartanah Malaysia: semakan sebelum beli, "
    "sewa dan pematuhan.", "Artikel &amp; Panduan", "Zahir MJ Property · Panduan hartanah",
    badan_blog("zmp"), ZMP_REPO, ZMP_BASE, "zmp-blog.html", "artikel"))

HUB = """<!DOCTYPE html>
<html lang="ms"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex,nofollow">
<title>PRATONTON — Blog Isu Tanah RM450K (Mr Tanah + Zahir MJ Property)</title>
<style>
:root{--ink:#0F172A;--mut:#64748B;--grn:#059669;--bg:#F6F8FA}
*{box-sizing:border-box}body{margin:0;font:16px/1.65 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--ink);background:var(--bg)}
.wrap{max-width:900px;margin:0 auto;padding:34px 20px 60px}
h1{font-size:clamp(22px,3.4vw,32px);margin:0 0 6px}.sub{color:var(--mut);margin:0 0 22px}
.tag{display:inline-block;background:#0f172a;color:#fff;font-size:12px;font-weight:700;letter-spacing:.04em;padding:4px 10px;border-radius:999px}
.card{background:#fff;border:1px solid #E3E8EE;border-radius:14px;padding:20px;margin:16px 0;box-shadow:0 1px 2px rgba(15,23,42,.04)}
.card h2{margin:0 0 10px;font-size:18px}ul{margin:8px 0 0;padding-left:20px}li{margin:6px 0}
a.btn{display:inline-block;background:var(--grn);color:#fff;text-decoration:none;font-weight:600;padding:9px 15px;border-radius:9px;margin:6px 8px 0 0}
a.alt{background:#fff;color:var(--ink);border:1px solid #CBD5E1}
.mut{color:var(--mut);font-size:14px}
</style></head><body><div class="wrap">
<span class="tag">PRATONTON — BUKAN LAMAN PRODUKSI</span>
<h1>Blog: "Isu Tanah RM450K, Tiada Jalan Masuk"</h1>
<p class="sub">Draf blog + struktur seksyen Artikel, dalam <strong>dua kulit jenama</strong> — untuk Zahir pilih
sebelum apa-apa diterbitkan. Produksi <strong>tidak disentuh</strong>: halaman ini memuatkan CSS/aset terus
daripada <em>mrtanah.com</em> dan <em>zahirmjproperty.com</em>.</p>

<div class="card"><h2>1. Mr Tanah (mrtanah.com)</h2>
<p class="mut">Artikel penuh + indeks blog dalam kulit Mr Tanah.</p>
<a class="btn" href="mt-artikel.html">Baca artikel — kulit Mr Tanah</a>
<a class="btn alt" href="mt-blog.html">Indeks Artikel (Mr Tanah)</a></div>

<div class="card"><h2>2. Zahir MJ Property (zahirmjproperty.com)</h2>
<p class="mut">Artikel sama, kulit Zahir MJ Property — beza warna aksen, nama jenama, nombor telefon dan nav.</p>
<a class="btn" href="zmp-artikel.html">Baca artikel — kulit ZMP</a>
<a class="btn alt" href="zmp-blog.html">Indeks Artikel (ZMP)</a></div>

<div class="card"><h2>Apa yang berubah berbanding laman sekarang</h2>
<ul>
<li><strong>Seksyen Artikel</strong> (nav baharu) + indeks blog: 1 artikel siap, 2 tajuk "akan datang" (tidak direka).</li>
<li><strong>Artikel</strong>: nama agensi disebut (Landsworth Properties Sdn Bhd, E(1)1959) dengan petikan
kenyataan rasmi 17 Julai 2026; nama pembeli <em>tidak</em> disebut.</li>
<li>Hak berkanun dinyatakan dengan rujukan: ismen s.286 KTN; hak lalulalang s.388–391; Borang 28A (s.390),
28B (s.391), 28C (s.394).</li>
<li>Bahagian "Bagaimana kami uruskan isu ini" — dasar sedia ada (status akses direkod; geran/pelan tidak
ditayang awam).</li>
<li>Penafian: "maklumat am, bukan nasihat guaman" + nota kes belum diputuskan mahkamah.</li>
</ul></div>

<div class="card"><h2>Cara lulus</h2>
<ol><li>Buka dua pautan di atas (artikel + indeks).</li>
<li>Pilih laman mana: <strong>MT</strong>, <strong>ZMP</strong>, atau <strong>kedua-dua</strong>.</li>
<li>Balas: <em>"LULUS &amp; TERBIT di MT"</em> (atau ZMP / kedua-dua) — atau senaraikan pembetulan.</li></ol>
<p class="mut">Selepas lulus: bina halaman sebenar dalam repo produksi (canonical, sitemap, cache bust,
blok identiti penuh), pratonton produksi = 0 penanda sebelum terbit.</p></div>

<div class="card"><h2>Nota penting</h2>
<p class="mut">Halaman pratonton ini <code>noindex,nofollow</code> — tidak akan muncul di Google.
Jika Zahir mahu versi yang menamakan pembeli juga, ia perlu kelulusan bertulis (risiko fitnah).</p></div>
</div></body></html>
"""
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(HUB)

# ---------------------------------------------------------------- semakan
print("\n=== SEMAKAN ===")
for f in sorted(os.listdir(OUT)):
    p = os.path.join(OUT, f)
    t = baca(p)
    print(f"  {f:22s} {os.path.getsize(p):7d} bait  noindex={'YA' if 'noindex' in t else 'TIDAK'}")
    if "@@" in t:
        raise SystemExit("GAGAL: token @@ tertinggal")
print("\nSIAP — keluaran dalam", OUT)
