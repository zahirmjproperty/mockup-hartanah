#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Susun semula navigasi jadi 2 lapisan (Fasa 1, diluluskan Zahir):
   menu pelanggan di bar utama + dropdown "Untuk Pemilik & Ejen".
   Mengekalkan href relatif sedia ada (portal/ guna ../index.html dsb).
"""
import os, re, sys

REPO = sys.argv[1]
DROPDOWN = ("portal", "bayar", "jual-sewa-develop", "serah-dokumen", "serah-listing",
            "permohonan-sewa", "invoice")

nav_re = re.compile(r'(<nav class="nav" id="nav">)(.*?)(</nav>)', re.S)
chip_re = re.compile(r'(<div class="navchips">)(.*?)(</div>)', re.S)
a_re = re.compile(r'<a\s+([^>]*?)>(.*?)</a>', re.S)

diubah = 0
for akar, _, fail in os.walk(REPO):
    a = akar.replace("\\", "/")
    if "/.git" in a or "/assets" in a or "preview" in a or "/invoice" in a:
        continue
    for f in fail:
        if not f.endswith(".html"):
            continue
        p = os.path.join(akar, f)
        t = open(p).read()
        m = nav_re.search(t)
        if not m:
            continue
        dalam = m.group(2)
        pautan = []
        for at, teks in a_re.findall(dalam):
            href = re.search(r'href="([^"]*)"', at)
            if not href:
                continue
            pautan.append({"href": href.group(1), "teks": re.sub(r"\s+", " ", teks).strip(),
                           "active": 'class="active"' in at, "attr": at})
        if not pautan:
            continue
        utama, bawah = [], []
        for x in pautan:
            h = x["href"].lower()
            if any(d in h for d in DROPDOWN):
                bawah.append(x)
            else:
                utama.append(x)
        if not bawah:
            continue
        def A(x, cls=""):
            c = ' class="active"' if x["active"] else (f' class="{cls}"' if cls else "")
            return f'      <a href="{x["href"]}"{c}>{x["teks"]}</a>'
        nav_baru = "\n" + "\n".join(A(x) for x in utama) + "\n"
        nav_baru += ('      <div class="navdrop">\n'
                     '        <button type="button" aria-haspopup="true">Untuk Pemilik &amp; Ejen ▾</button>\n'
                     '        <div class="menu">\n'
                     + "\n".join("          " + A(x)[6:] for x in bawah) +
                     '\n        </div>\n      </div>\n    ')
        t2 = t[:m.start(2)] + nav_baru + t[m.end(2):]
        # chips: kekalkan 3 utama + pautan pemilik/ejen
        cm = chip_re.search(t2)
        if cm:
            chips = []
            for x in utama[:3]:
                c = 'chip aktif' if x["active"] else 'chip'
                chips.append(f'    <a class="{c}" href="{x["href"]}">{x["teks"]}</a>')
            if bawah:
                chips.append(f'    <a class="chip" href="{bawah[0]["href"]}">Pemilik/Ejen</a>')
            t2 = t2[:cm.start(2)] + "\n" + "\n".join(chips) + "\n  " + t2[cm.end(2):]
        if t2 != t:
            open(p, "w").write(t2)
            diubah += 1
print(f"{REPO}: {diubah} halaman nav disusun semula")
