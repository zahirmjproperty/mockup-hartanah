#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""uji_konsistensi.py — memastikan semua halaman Zentra Hub padan dengan assets/levels.js (Tier A)."""
import os, re, json, sys

D = os.path.dirname(os.path.abspath(__file__))
lv = open(os.path.join(D, "assets/levels.js"), encoding="utf-8").read()
LAD = {}
for m in re.finditer(r"\{id:'(L\d)', tier:'([^']+)',\s*comm:(\d+), bonus:(\d+), total:(\d+), ovrCap:(\d+)", lv):
    LAD[m.group(1)] = {"tier": m.group(2), "total": int(m.group(5)), "cap": int(m.group(6))}

masalah = []
for f in sorted(os.listdir(D)):
    if not f.endswith(".html"):
        continue
    s = open(os.path.join(D, f), encoding="utf-8").read()
    # 1) label "L# · Tier" mesti padan
    for m in re.finditer(r"(L\d) · ([^·<'\"]{2,30}?)(?: · (\d+)%)?(?=['\"<]|$)", s):
        lid, tier, pct = m.group(1), m.group(2).strip(), m.group(3)
        if lid not in LAD:
            masalah.append((f, "kod level tidak dikenali", m.group(0))); continue
        mnum = re.match(r"^(\d+)%?\)?", tier)
        if mnum:
            if int(mnum.group(1)) != LAD[lid]["total"]:
                masalah.append((f, "peratus tidak padan", "%s: %s vs %s%%" % (lid, mnum.group(1), LAD[lid]["total"])))
            continue
        if tier.rstrip('%').isdigit():
            if int(tier.rstrip('%')) != LAD[lid]["total"]:
                masalah.append((f, "peratus tidak padan", "%s: %s vs %s%%" % (lid, tier, LAD[lid]["total"])))
            continue
        if tier == LAD[lid]["tier"] + " cap 10%":
            continue
        if tier != LAD[lid]["tier"]:
            masalah.append((f, "tier tidak padan", "%s vs %s (%s)" % (lid, tier, LAD[lid]["tier"])))
        if pct and int(pct) != LAD[lid]["total"]:
            masalah.append((f, "peratus tidak padan", "%s: %s%% vs %s%%" % (lid, pct, LAD[lid]["total"])))
    # 2) jawatan tidak boleh muncul pada level yang salah
    for m in re.finditer(r"(Team Leader|Group Leader)[^<]{0,40}?(\d{2})%", s):
        jt, pct = m.group(1), int(m.group(2))
        jadual = {"Team Leader": 85, "Group Leader": 90}[jt]
        if pct != jadual:
            masalah.append((f, "jawatan pada peratus salah", "%s · %s%% (jangka %s%%)" % (jt, pct, jadual)))
    # 2b) format lama '· Level N' = tidak konsisten
    for m in re.finditer(r"· Level (\d)", s):
        masalah.append((f, "format lama (· Level N)", m.group(0)))
    # 3) kod akaun: komisen 602-100 tidak boleh sama dengan marketing reward
    kods = set(re.findall(r"602-\d+", s))
    if "602-100" in kods and "602-150" not in kods and "Marketing" in s:
        masalah.append((f, "kod akaun tidak dipisahkan", "Marketing reward tiada 602-150"))

print("levels.js: %d level (%s)" % (len(LAD), ", ".join("%s=%s%%" % (k, v["total"]) for k, v in sorted(LAD.items()))))
if masalah:
    print("\n❌ %d percanggahan:" % len(masalah))
    for f, jenis, butir in masalah:
        print("  - %-18s %-30s %s" % (f, jenis, butir))
    sys.exit(1)
print("\n✅ LULUS — semua halaman padan dengan levels.js")
