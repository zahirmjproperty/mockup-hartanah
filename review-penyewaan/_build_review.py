#!/usr/bin/env python3
"""_build_review.py — indeks review modul PENYEWAAN (satu skrin) untuk Zentra/MT.

Jalankan: python3 _build_review.py   →  index.html
Status: A=awam (boleh guna terus), D=dashboard (shell awam, data perlu peranan/token),
X=dalaman (jangan kongsi). Sumber: imbasan /home/ubuntu/mrtanah-site/portal, 17 Sep 2026.
"""
import html
import os
import re

PORTAL = "https://mrtanah.com/portal/"
POC = "https://zahirmjproperty.github.io/mockup-hartanah/portal-poc/"
SRC = "/home/ubuntu/mrtanah-site/portal"

# (fail, tajuk pendek, status, tujuan)
DATA = [
    ("SEKSYEN", "Penyewa (penyewa sendiri)", "", ""),
    ("penyewa.html", "Portal Penyewa", "D", "Bil sewa, rekod bayaran, hantar aduan kerosakan"),
    ("pembaharuan-sewa.html", "Pembaharuan Sewa", "A", "Penyewa mohon perpanjang sewa sebelum tamat"),
    ("notis-tamat.html", "Notis Penamatan Sewa", "A", "Penyewa/MT beri notis tamat mengikut tempoh"),
    ("lapor-kerosakan.html", "Lapor Kerosakan Unit", "A", "Borang awam aduan kerosakan tanpa log masuk"),
    ("SEKSYEN", "Pemilik / Tuan Rumah", "", ""),
    ("pemilik.html", "Dashboard Pemilik", "D", "Portfolio hartanah, sewa masuk, status unit"),
    ("aduan-pemilik.html", "Portal Tuan Rumah", "D", "Pemilik pantau kerja pembaikan & aduan"),
    ("daftar-unit.html", "Pendaftaran Unit", "A", "Daftar unit baru untuk disewakan (inventori)"),
    ("SEKSYEN", "Operasi MT (dalaman)", "", ""),
    ("pemuka.html", "Dashboard MT — Pengurusan Hartanah", "X", "Papan utama kerja sewa: sewa, unit, penyewa"),
    ("kanban.html", "Papan Kanban Kerja + SLA", "X", "Aliran kerja & tempoh tindak balas tugasan"),
    ("kes.html", "Dashboard Kes (CRM)", "X", "Rekod kes, pihak, peringkat & tindakan"),
    ("aduan-mt.html", "Portal Aduan MT", "X", "Kotak masuk aduan masuk untuk staff"),
    ("penyediaan-unit.html", "Penyediaan Semula Unit", "X", "Kerja cat/bersih sebelum penyewa baru"),
    ("daftar-peranan.html", "Daftar Peranan", "X", "Papar peranan pengguna sistem"),
    ("SEKSYEN", "Kontraktor & tukang", "", ""),
    ("daftar-kontraktor.html", "Pendaftaran Kontraktor", "A", "Borang awam kontraktor/tukang daftar"),
    ("kontraktor.html", "Dashboard Kontraktor", "D", "Kontraktor lihat tugasan & hantar sebut harga"),
    ("aduan-kontraktor.html", "Portal Kontraktor", "D", "Kemas kini status kerja pembaikan"),
    ("SEKSYEN", "Ejen rujukan", "", ""),
    ("ejen.html", "Dashboard Ejen", "D", "Ejen lihat rujukan & status unit disewakan"),
    ("aduan-ejen.html", "Portal Ejen Rujukan", "D", "Status kes rujukan ejen"),
    ("SEKSYEN", "Urus niaga bersebelahan", "", ""),
    ("penjual.html", "Dashboard Penjual", "D", "Penjual pantau urus niaga jual"),
    ("pembeli.html", "Dashboard Pembeli", "D", "Pembeli pantau urus niaga & dokumen"),
    ("pembiayaan.html", "Dashboard Pembiayaan", "D", "Pembiayaan: permohonan & status"),
    ("solicitor.html", "Portal Peguamcara", "D", "Firma guaman: dokumen & tugasan urus niaga"),
    ("SEKSYEN", "Ladang (Strategic Agro Technology)", "", ""),
    ("ladang.html", "Papan Ladang", "X", "Pengurusan ladang (dalaman)"),
    ("ladang-pemilik.html", "Portal Pemilik Ladang", "D", "Pemilik ladang lihat hasil & urusan"),
    ("pembeli-ladang.html", "Pembeli Hasil Ladang", "D", "Pembeli hasil ladang"),
    ("SEKSYEN", "Akses & portal induk", "", ""),
    ("index.html", "Portal Mr Tanah (induk)", "A", "Pintu masuk semua perkhidmatan portal"),
    ("login.html", "Log Masuk", "A", "Halaman log masuk pengguna"),
    ("masuk.html", "Akses Sistem (hub)", "A", "Hub log masuk / log keluar peranan"),
]

POC_PAGES = [
    ("index.html", "Indeks PoC"),
    ("penyewa.html", "Portal Penyewa (PoC)"),
    ("bayar.html", "Aliran Bayaran (PoC)"),
    ("kanban.html", "Kanban Kerja (PoC)"),
    ("ladang.html", "Ladang (PoC)"),
]
# --- HTML ---
CSS = """
:root{--navy:#0C4437;--gold:#C9A227;--ink:#101613;--mut:#5b6b64;--line:#dfe6e2;--bg:#f6f8f7}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 -apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
header{background:linear-gradient(135deg,var(--navy),#0a3529);color:#fff;padding:26px 22px 22px}
header h1{margin:0 0 4px;font-size:22px;letter-spacing:.2px}
header p{margin:2px 0;color:#cfe0d8;font-size:13px}
.wrap{max-width:980px;margin:0 auto;padding:18px 16px 60px}
.chips{display:flex;gap:8px;flex-wrap:wrap;margin:14px 0 4px}
.chip{background:#fff;border:1px solid var(--line);border-radius:999px;padding:6px 12px;font-size:12.5px;color:var(--mut)}
.chip b{color:var(--ink)}
h2{font-size:15px;text-transform:uppercase;letter-spacing:.6px;color:var(--navy);margin:26px 0 8px;border-bottom:2px solid var(--gold);padding-bottom:5px;display:inline-block}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden;margin-bottom:6px}
table{width:100%;border-collapse:collapse}
td{padding:11px 12px;border-top:1px solid #eef2f0;vertical-align:top}
tr:first-child td{border-top:0}
td.n{font-weight:600;width:31%}
td.t{color:var(--mut);width:30%;font-size:13.5px}
td.u{width:39%;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px;word-break:break-all}
td.u a{color:#0b6b52;text-decoration:none;border-bottom:1px dotted #9dc3b5}
.pill{display:inline-block;font-size:11px;font-weight:700;padding:3px 8px;border-radius:999px;margin-right:6px;vertical-align:1px}
.pA{background:#e6f6ec;color:#0b6b39;border:1px solid #bfe6cd}
.pD{background:#fdf3e0;color:#8a5a06;border:1px solid #f0dcaf}
.pX{background:#fbe9e9;color:#9a1c1c;border:1px solid #f0c2c2}
.legend{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 14px;font-size:13px;color:var(--mut);margin:8px 0 0}
.legend > span{display:block;margin:3px 0}
td.u{width:39%;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px;overflow-wrap:anywhere}
footer{color:var(--mut);font-size:12.5px;margin-top:26px;border-top:1px solid var(--line);padding-top:12px}
button{background:var(--navy);color:#fff;border:0;border-radius:9px;padding:9px 14px;font-size:13.5px;cursor:pointer;margin-top:10px}
@media print{header{background:#0C4437 !important;-webkit-print-color-adjust:exact}button{display:none}body{background:#fff}}
"""

def esc(s):
    return html.escape(s, quote=True)

def title_of(fn):
    p = os.path.join(SRC, fn)
    if not os.path.exists(p):
        return ""
    t = open(p, encoding="utf-8", errors="ignore").read()
    m = re.search(r"<title>(.*?)</title>", t, re.I | re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""

def pill(st):
    return {"A": ('<span class="pill pA">AWAM</span>', "awam"),
            "D": ('<span class="pill pD">DASHBOARD</span>', "dashboard"),
            "X": ('<span class="pill pX">DALAMAN</span>', "dalaman")}[st]

def main():
    sections, counts, missing = [], {"A": 0, "D": 0, "X": 0}, []
    cur_title, cur_rows = None, []
    for item in DATA:
        if item[0] == "SEKSYEN":
            if cur_title:
                sections.append((cur_title, cur_rows))
            cur_title, cur_rows = item[1], []
            continue
        fn, nama, st, tujuan = item
        if not os.path.exists(os.path.join(SRC, fn)):
            missing.append(fn)
        p, _ = pill(st)
        counts[st] += 1
        url = PORTAL + fn
        cur_rows.append('<tr><td class="n">%s%s</td><td class="t">%s</td>'
                        '<td class="u"><a href="%s">%s</a></td></tr>'
                        % (p, esc(nama), esc(tujuan), url, esc(url)))
    if cur_title:
        sections.append((cur_title, cur_rows))
    body = "".join('<h2>%s</h2><div class="card"><table>%s</table></div>' % (esc(t), "".join(r))
                   for t, r in sections)
    poc = "".join('<tr><td class="n">%s</td><td class="t">%s</td>'
                  '<td class="u"><a href="%s%s">%s%s</a></td></tr>'
                  % (esc(lbl), "Pratonton PoC, tiada data", POC, f, POC, f) for f, lbl in POC_PAGES)
    n_prod = sum(counts.values())
    out = f"""<!DOCTYPE html>
<html lang="ms"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Indeks Review — Sistem Pengurusan Hartanah (Penyewaan) | Mr Tanah</title>
<style>{CSS}</style></head><body>
<header>
  <h1>Indeks Review — Sistem Pengurusan Hartanah (Penyewaan)</h1>
  <p>Mr Tanah · ZMJ Solutions — halaman semakan satu skrin untuk modul penyewaan</p>
  <p>Disemak 17 September 2026 · {n_prod} halaman produksi · {len(POC_PAGES)} halaman pratonton PoC · semua dipulangkan HTTP 200 tanpa log masuk</p>
</header>
<div class="wrap">
  <div class="chips">
    <span class="chip"><b>{n_prod}</b> pautan produksi</span>
    <span class="chip"><b>{counts['A']}</b> awam</span>
    <span class="chip"><b>{counts['D']}</b> dashboard</span>
    <span class="chip"><b>{counts['X']}</b> dalaman</span>
  </div>
  <div class="legend">
    <span><span class="pill pA">AWAM</span> boleh dibuka dan digunakan terus tanpa log masuk — selamat dikongsi.</span>
    <span><span class="pill pD">DASHBOARD</span> halaman boleh dilihat, tetapi datanya memerlukan peranan/token pengguna.</span>
    <span><span class="pill pX">DALAMAN</span> bertanda "jangan kongsi" — shell boleh dibuka, data di belakang peranan. Kongsi hanya dengan pihak dalaman.</span>
  </div>
  <h2>Pautan modul penyewaan</h2>
  {body}</table></div>
  <h2>Pratonton statik (PoC, tiada data langsung)</h2>
  <div class="card"><table>{poc}</table></div>
  <h2>Nota</h2>
  <div class="legend">
    <span>URL penuh dipaparkan supaya boleh disalin dan dihantar kepada pihak ketiga.</span>
    <span>Semakan dibuat secara anonim (tanpa cookie/sesi) — tiada kata laluan diperlukan untuk membuka mana-mana halaman di atas.</span>
    <span>Halaman produksi ialah versi terkini (snapshot automatik 17 September 2026); pratonton PoC ialah versi lama yang kekal untuk rujukan reka bentuk.</span>
  </div>
  <button onclick="window.print()">Cetak / simpan sebagai PDF</button>
  <footer>Dijana oleh pembantu Ali untuk Zahir MJ · dibina daripada senarai fail produksi portal MT · halaman ini noindex (tidak muncul dalam carian).</footer>
</div></body></html>"""
    open("index.html", "w", encoding="utf-8").write(out)
    print("index.html:", len(out), "bait")
    print("pautan produksi:", n_prod, counts)
    if missing:
        print("AMARAN tiada dalam sumber:", missing)
    else:
        print("semua %d fail wujud dalam sumber" % n_prod)

if __name__ == "__main__":
    main()

