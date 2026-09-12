#!/usr/bin/env python3
"""Jana mock-up Fasa 1 (5 halaman) daripada data listing SEBENAR + imej sebenar.
Output: /home/ubuntu/mockup-hartanah/*.html + img/*.webp
Preview sahaja — tiada sentuh repo production."""
import json, os, re, io, urllib.request, html
from PIL import Image

BASE = "/home/ubuntu/mockup-hartanah"
IMG  = os.path.join(BASE, "img")
RAW  = os.path.join(BASE, "raw")
os.makedirs(IMG, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120 Safari/537.36"}


def load(path):
    src = open(path).read()
    return json.loads(src[src.index("window.LISTINGS"):].split("=", 1)[1].rsplit(";", 1)[0])


def fetch(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=45).read()


def save_webp(data, name, width, q=78):
    im = Image.open(io.BytesIO(data)).convert("RGB")
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    p = os.path.join(IMG, name)
    im.save(p, "WEBP", quality=q, method=5)
    return name, os.path.getsize(p), im.size


def optimise(data, base, q=78):
    """Simpan 3 saiz (kad 700 / butiran 1200 / thumb 320) -> WebP."""
    out = {}
    im = Image.open(io.BytesIO(data)).convert("RGB")
    for tag, w, qq in (("card", 700, q), ("big", 1200, q + 2), ("th", 320, 72)):
        c = im.copy()
        if c.width > w:
            c = c.resize((w, round(c.height * w / c.width)), Image.LANCZOS)
        p = os.path.join(IMG, f"{base}-{tag}.webp")
        c.save(p, "WEBP", quality=qq, method=5)
        out[tag] = f"img/{base}-{tag}.webp"
    return out


# ---------------- pilih listing sebenar ----------------
z = load("/home/ubuntu/zahir-web/data/listings.js")
m = load("/home/ubuntu/mrtanah-site/data/listings.js")

def pick(arr, keys, n, cats=None):
    seen, out = set(), []
    pool = [l for l in arr if l.get("active") and (l.get("images") or [])
            and (not cats or (l.get(keys) or "-") in cats)]
    for l in pool:                                  # lulus 1: satu setiap kategori
        k = l.get(keys) or "-"
        if k in seen:
            continue
        seen.add(k); out.append(l)
    for l in pool:                                  # lulus 2: penuhkan kuota
        if len(out) >= n:
            break
        if l not in out:
            out.append(l)
    return out[:n]

ZP = pick(z, "type", 6)
MT = pick(m, "kategori", 6, cats=["Pertanian", "Perumahan", "Bangunan", "Komersial", "Perindustrian"])

print("ZMP pilih:", [(x["tracking"], x["type"]) for x in ZP])
print("MT  pilih:", [(x["tracking"], x["kategori"]) for x in MT])

RATE, YEARS, MARGIN = 0.0400, 35, 0.90


def ansuran(price):
    if not price:
        return None
    loan = price * MARGIN
    r = RATE / 12
    n = YEARS * 12
    return round(loan * r / (1 - (1 + r) ** -n))


def wa(num, txt):
    from urllib.parse import quote
    return f"https://wa.me/{num}?text={quote(txt)}"


# ---------------- imej ----------------
assets = {}
for l in ZP + MT:
    trk = l["tracking"]
    try:
        data = fetch(l["images"][0])
        assets[trk] = optimise(data, trk.lower())
    except Exception as e:
        print("GAGAL imej", trk, e)

# hero
hero_z = None
try:
    data = fetch([x for x in z if x["tracking"] == "COA-0010"][0]["images"][1])
    hero_z = save_webp(data, "hero-zmp.webp", 1700, 80)[0]
except Exception as e:
    hero_z = assets["COA-0010"]["big"]
    print("hero z fallback", e)

hero_m = None
for cand, idx in (("MT-0006", 4), ("MT-0023", 0)):
    try:
        l = [x for x in m if x["tracking"] == cand][0]
        data = fetch(l["images"][idx])
        hero_m = save_webp(data, "hero-mt.webp", 1700, 80)[0]
        break
    except Exception as e:
        print("hero mt cuba", cand, e)
if not hero_m:
    hero_m = "hero-mt.webp"

# imej peta statik (drone/gambaran kawasan) untuk blok peta
try:
    l = [x for x in m if x["tracking"] == "MTCOA-0012"][0]
    save_webp(fetch(l["images"][0]), "peta-mt.webp", 1200, 76)
except Exception as e:
    print("peta gagal", e)

# galeri butiran
def galeri(tracking, src, n=6):
    out = []
    for i, u in enumerate(src[:n]):
        try:
            out.append(optimise(fetch(u), f"{tracking.lower()}-g{i+1}"))
        except Exception as e:
            print("galeri gagal", tracking, i, e)
    return out

GAL_Z = galeri("COA-0001", [x for x in z if x["tracking"] == "COA-0001"][0]["images"], 6)
GAL_M = galeri("MT-0003", [x for x in m if x["tracking"] == "MT-0003"][0]["images"], 6)

json.dump({"assets": assets, "hero_z": hero_z, "hero_m": hero_m}, open(os.path.join(BASE, "img-map.json"), "w"))
print("imej siap. jumlah fail:", len(os.listdir(IMG)))
