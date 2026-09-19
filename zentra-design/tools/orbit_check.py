#!/usr/bin/env python3
"""orbit_check.py — proof that the gold light really travels around the button.

Why the test is built this way
------------------------------
`--za` is registered with `inherits: false`, so it lives on the PSEUDO-ELEMENT.
An inline `style="--za:45deg"` on the <a> therefore cannot reach it — an earlier
attempt at this harness did exactly that and (correctly) measured no movement.
The reliable way to pin a CSS animation to an arbitrary phase is to PAUSE it and
use a NEGATIVE animation-delay: `--fd: -1.80s` shows the frame at t=1.80s.
That is deterministic, unlike --virtual-time-budget, which does not reliably
advance a Houdini @property animation.

Measurement is analytic, not threshold-guessed:
    ring     = outer RING_BAND device px of the button rect
    interior = button rect inset by CORE_INSET device px
The angle is the circular mean of ring pixels weighted by
max(0, luminance - ring median), so a uniform brightening cannot fake a
travelling highlight.

Checks
  1 PHASE SWEEP   paused at 8 phases: 8 distinct angles, monotonic, ~1 full turn
  2 NO FADE       brightness floor across all phases (the old approach's failure)
  3 CONTAINMENT   the light stays on the ring, never leaks over the label
  4 PARITY        same measurement on the old rotate-the-element approach

Usage: python3 tools/orbit_check.py
"""
import math
import os
import subprocess
import sys

from PIL import Image

CSS = "/home/ubuntu/zentra-design/assets/zentra.css"
TMP = "/tmp/zb_orbit_final"
os.makedirs(TMP, exist_ok=True)

DSF = 2
W_CSS, H_CSS = 620, 240
BW, BH = 380, 66
X0, Y0 = int((W_CSS - BW) / 2) * DSF, int((H_CSS - BH) / 2) * DSF
X1, Y1 = X0 + BW * DSF, Y0 + BH * DSF
RING_BAND, CORE_INSET = 8 * DSF, 16 * DSF
CX, CY = (X0 + X1) / 2.0, (Y0 + Y1) / 2.0
DUR = 3.6
NPHASE = 8

SHELL = """<!DOCTYPE html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="file://{css}">
<style>
  html,body{{margin:0;padding:0;background:rgb(11,27,46);}}
  body{{width:{w}px;height:{h}px;display:grid;place-items:center;}}
  .zbtn--box{{width:{bw}px;height:{bh}px;box-sizing:border-box;}}
  .zbtn-face{{width:100%;height:100%;justify-content:center;}}
  .zbtn-face b{{font-size:15px;letter-spacing:.06em;}}
  .zbtn-face .sm{{display:block;font-size:10px;font-weight:400;opacity:.75;}}
  .zbtn--noring::before,.zbtn--noring::after{{display:none;}}
  .zbtn--noring{{background:transparent;}}
  .zp-broke{{position:relative;display:block;border-radius:16px;padding:4px;
    width:{bw}px;height:{bh}px;box-sizing:border-box;}}
  .zp-broke::before{{content:"";position:absolute;inset:0;border-radius:16px;
    padding:4px;
    background:conic-gradient(from 0deg,transparent 0deg,transparent 250deg,
      #fff3c4 280deg,#f4d888 300deg,#c9a227 320deg,#fff3c4 340deg,
      transparent 355deg,transparent 360deg);
    -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
    -webkit-mask-composite:xor;mask-composite:exclude;
    animation:rotate-glow 2.2s linear infinite;pointer-events:none;z-index:0;}}
  @keyframes rotate-glow{{to{{transform:rotate(360deg);}}}}
  .zp-broke--frozen::before{{animation-play-state:paused;
    animation-delay:var(--fd,0s);}}
  .zp-broke-face{{position:relative;z-index:1;display:flex;align-items:center;
    justify-content:center;width:100%;height:100%;border-radius:12px;
    background:linear-gradient(180deg,#17273f,#0d1a2c);color:#f4d888;
    font:600 13px/1.2 system-ui;letter-spacing:.06em;}}
</style></head><body>
{body}
</body></html>
"""

NEW = ('<a class="zbtn zbtn--lg zbtn--box zbtn--frozen {cls}" style="--fd:{fd}" href="#">'
       '<span class="zbtn-face"><span style="font-size:19px">&#10132;</span>'
       '<span><b>LOGIN TO ZENTRA ASSET</b>'
       '<span class="sm">Access Your Asset Management System</span></span>'
       '</span></a>')
OLD = ('<div class="zp-broke zp-broke--frozen" style="--fd:{fd}" >'
       '<span class="zp-broke-face">OLD APPROACH</span></div>')


def render(body):
    html = os.path.join(TMP, "b.html")
    png = os.path.join(TMP, "b.png")
    open(html, "w").write(SHELL.format(css=CSS, w=W_CSS, h=H_CSS,
                                       bw=BW, bh=BH, body=body))
    if os.path.exists(png):
        os.remove(png)
    subprocess.run(
        ["google-chrome", "--headless=new", "--disable-gpu", "--no-sandbox",
         "--hide-scrollbars", f"--force-device-scale-factor={DSF}",
         "--virtual-time-budget=900", f"--window-size={W_CSS},{H_CSS}",
         f"--screenshot={png}", f"file://{html}"],
        capture_output=True, timeout=180)
    return Image.open(png).convert("RGB")


def _bands(im):
    px, (Wp, Hp) = im.load(), im.size
    ring, core = [], []
    for y in range(max(0, Y0), min(Hp, Y1)):
        for x in range(max(0, X0), min(Wp, X1)):
            p = px[x, y]
            l = (0.2126 * p[0] + 0.7152 * p[1] + 0.0722 * p[2]) / 255.0
            edge = (x < X0 + RING_BAND or x >= X1 - RING_BAND or
                    y < Y0 + RING_BAND or y >= Y1 - RING_BAND)
            if edge:
                ring.append((x, y, l))
            elif (X0 + CORE_INSET <= x < X1 - CORE_INSET and
                  Y0 + CORE_INSET <= y < Y1 - CORE_INSET):
                core.append(l)
    return ring, core


def measure(im):
    """-> (angle_deg|None, bright_px, core_top_decile)"""
    ring, core = _bands(im)
    L = sorted(p[2] for p in ring)
    med, hi = L[len(L) // 2], L[int(len(L) * 0.999)]
    thr = med + 0.25 * (hi - med)
    sx = sy = sw = 0.0
    n = 0
    for x, y, l in ring:
        w = l - med
        if w <= 0 or l < thr:
            continue
        th = math.atan2(y - CY, x - CX)
        sx += math.cos(th) * w
        sy += math.sin(th) * w
        sw += w
        n += 1
    ang = (math.degrees(math.atan2(sy, sx)) % 360) if sw > 0 else None
    core.sort()
    top = core[int(len(core) * 0.90):]
    return ang, n, (sum(top) / max(1, len(top)))


def main():
    fails, notes = [], []
    print(f"button rect (device px): x {X0}..{X1}  y {Y0}..{Y1}  "
          f"centre ({CX:.0f},{CY:.0f})")
    print(f"ring {RING_BAND} px | core inset {CORE_INSET} px | "
          f"cycle {DUR}s | method: paused animation + negative delay\n")

    ctl_ang, ctl_px, ctl_core = measure(render(NEW.format(cls="zbtn--noring",
                                                          fd="0s")))
    print(f"CONTROL (ring hidden) -> core highlight {ctl_core:.3f}\n")

    results = {}
    for label, tpl in (("NEW", NEW), ("OLD", OLD)):
        rows = []
        for i in range(NPHASE):
            fd = f"-{DUR * i / NPHASE:.2f}s"
            ang, n, core = measure(render(tpl.format(cls="", fd=fd) if label == "NEW"
                                          else tpl.format(fd=fd)))
            rows.append((fd, ang, n, core))
        results[label] = rows

    print("1/2. PHASE SWEEP  (paused at 8 phases covering one full cycle)")
    print(f"{'':4}{'frame':>7} {'angle':>8} {'step':>8} {'ring px':>8} {'face':>7}")
    print("-" * 50)
    for label in ("NEW", "OLD"):
        rows = results[label]
        angs = [r[1] for r in rows]
        print(f"  {label}")
        uw, prev = [], None
        for i, (fd, ang, n, core) in enumerate(rows):
            if ang is None:
                print(f"      {i:>5} {'-':>8} {'-':>8} {n:>8} {core:>7.3f}")
                continue
            if prev is None:
                uw.append(ang)
                step = 0.0
            else:
                d = (ang - prev) % 360
                step = d if d < 180 else d - 360
                uw.append(uw[-1] + step)
            prev = ang
            print(f"      {i:>5} {ang:>8.1f} {step:>+8.1f} {n:>8} {core:>7.3f}")
        steps = [round(uw[i + 1] - uw[i], 1) for i in range(len(uw) - 1)]
        sweep = uw[-1] - uw[0] if len(uw) > 1 else 0.0
        distinct = len({round(a, 1) for a in angs if a is not None})
        counts = [r[2] for r in rows]
        fmins = [r[3] for r in rows]
        print(f"      distinct angles {distinct}/{len(rows)} | "
              f"sweep {sweep:.0f} deg | mono={all(s > 0 for s in steps)}")
        print(f"      ring px {min(counts)}..{max(counts)} | "
              f"face {min(fmins):.3f}..{max(fmins):.3f}\n")

        if label == "NEW":
            if distinct < len(rows):
                fails.append(f"only {distinct}/{len(rows)} distinct angles")
            if not all(s > 0 for s in steps):
                fails.append("motion is not monotonic")
            if abs(sweep) < 250:
                fails.append(f"sweep only {sweep:.0f} deg (want ~360)")
            if min(counts) < 0.5 * max(counts):
                fails.append(f"light fades to {min(counts)} px "
                             f"(peak {max(counts)})")
            new_min, new_max = min(counts), max(counts)
            face_ok = max(fmins) < ctl_core + 0.05
            print(f"3. CONTAINMENT   face highlight max {max(fmins):.3f} vs "
                  f"control {ctl_core:.3f} -> {'PASS' if face_ok else 'FAIL'}\n")
            if not face_ok:
                fails.append("light leaks onto the label")
        else:
            old_min, old_max = min(counts), max(counts)

    print("4. PARITY (bright-ring pixels per frame)")
    print(f"   NEW {new_min}..{new_max}   OLD {old_min}..{old_max}")
    print(f"   dimmest-frame ratio NEW/OLD = {new_min/max(1,old_min):.1f}x")
    if new_min / max(1, old_min) < 3:
        notes.append("NEW is not decisively steadier than OLD")

    print("\nVERDICT")
    for n in notes:
        print(f"  [note] {n}")
    if fails:
        for f in fails:
            print(f"  [FAIL] {f}")
        return 1
    print("  [PASS] all 8 phases distinct; light travels one full turn in one "
          "direction; brightness never fades; stays on the ring; never covers the label")
    return 0


if __name__ == "__main__":
    sys.exit(main())
