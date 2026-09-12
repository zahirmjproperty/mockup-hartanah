#!/usr/bin/env python3
"""POC data reader — ambil data NYATA (tanpa nama peribadi) untuk portal POC."""
import json, sys, re, os
sys.path.insert(0, "/home/ubuntu/unit-bil-db")
from unitbil import gsvc, SHEET_ID

OUT = "/home/ubuntu/mockup-hartanah/portal-poc/data/nyata.json"
os.makedirs(os.path.dirname(OUT), exist_ok=True)

svc = gsvc("sheets", "v4")
res = {"sumber": {"unit_bil_sheet": SHEET_ID, "penyelenggaraan_sheet": "1hq58IQSSexqw87-kiY0fnq755Gwc-SIRyqbApPaUlPg"}, "tabs": {}}

def sheet_meta(sid):
    return svc.spreadsheets().get(spreadsheetId=sid, fields="sheets(properties(title,gridProperties))").execute()

def read(sid, tab, rng="A1:U3000"):
    r = svc.spreadsheets().values().get(spreadsheetId=sid, range=f"{tab}!{rng}").execute()
    return r.get("values", [])

# 1. Tab names
for sid, label in [(SHEET_ID, "unit_bil"), ("1hq58IQSSexqw87-kiY0fnq755Gwc-SIRyqbApPaUlPg", "penyelenggaraan")]:
    m = sheet_meta(sid)
    tabs = [s["properties"]["title"] for s in m["sheets"]]
    res["tabs"][label] = tabs
    print(f"## TAB {label}: {tabs}")

def mask(s):
    s = (s or "").strip()
    if not s: return s
    if re.fullmatch(r"[\d\s\-\+]{9,}", s):          # nombor telefon
        return re.sub(r"\d(?=\d{2})", "X", s)
    toks = s.split()
    return " ".join([t[0] + "***" if len(t) > 3 else t for t in toks])

# 2. Unit
unit = read(SHEET_ID, "Unit", "A1:Q3000")
res["unit_header"] = unit[0]
res["unit_rows"] = unit[1:]
print("\n## UNIT header:", unit[0])
for r in unit[1:12]:
    print("   ", [mask(x) for x in r])

# 3. Invois
try:
    inv = read(SHEET_ID, "Invois", "A1:U3000")
    res["invois_header"] = inv[0]
    res["invois_rows"] = inv[1:]
    print("\n## INVOIS header:", inv[0])
    for r in inv[1:9]:
        print("   ", [mask(x) for x in r])
except Exception as e:
    print("INVOIS err", e); res["invois_header"] = []; res["invois_rows"] = []

# 4. Bil (sample terakhir)
bil = read(SHEET_ID, "Bil", "A1:Q3000")
res["bil_header"] = bil[0]; res["bil_rows"] = bil[1:]
print("\n## BIL header:", bil[0], "| jumlah baris:", len(bil[1:]))
for r in bil[1:6]:
    print("   ", [mask(x) for x in r])

# 5. Penyelenggaraan — setiap tab, header + 5 baris
PEN = "1hq58IQSSexqw87-kiY0fnq755Gwc-SIRyqbApPaUlPg"
res["pen"] = {}
for t in res["tabs"]["penyelenggaraan"]:
    try:
        v = read(PEN, t, "A1:T12")
        res["pen"][t] = v
        print(f"\n## PEN tab '{t}': {len(v)} baris")
        for r in v[:6]:
            print("   ", [mask(x) for x in r])
    except Exception as e:
        print("  tab", t, "err", e)

json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("\nSAVED", OUT, os.path.getsize(OUT), "bytes")
