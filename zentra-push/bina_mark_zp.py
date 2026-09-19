#!/usr/bin/env python3
"""bina_mark_zp.py — jana tanda jenama ZENTRA PUSH (PNG) untuk sidebar + ikon."""
import os

from PIL import Image, ImageDraw, ImageFont

NAVY = (11, 27, 46)
GOLD = (201, 162, 39)
GOLD_L = (232, 206, 134)
OUT = "/home/ubuntu/zentra-push/assets"
os.makedirs(OUT, exist_ok=True)


def font(sz):
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"):
        if os.path.exists(p):
            return ImageFont.truetype(p, sz)
    return ImageFont.load_default()


def mark(size, bg=NAVY, ring=True, transparent=False):
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0) if transparent else bg + (255,))
    d = ImageDraw.Draw(im)
    if not transparent:
        r = int(size * 0.22)
        # sudut bulat: segi empat navy
        d.rounded_rectangle([0, 0, size - 1, size - 1], radius=r, fill=bg + (255,))
    pad = int(size * 0.10)
    if ring:
        d.ellipse([pad, pad, size - pad, size - pad], outline=GOLD + (255,), width=max(2, size // 64))
    # teks ZP
    f = font(int(size * 0.40))
    txt = "ZP"
    bb = d.textbbox((0, 0), txt, font=f)
    d.text(((size - (bb[2] - bb[0])) / 2 - bb[0],
            (size - (bb[3] - bb[1])) / 2 - bb[1]), txt, font=f, fill=GOLD_L + (255,))
    # garis bawah emas
    w = int(size * 0.34)
    y = int(size * 0.71)
    d.rounded_rectangle([(size - w) // 2, y, (size + w) // 2, y + max(2, size // 90)],
                        radius=size // 90, fill=GOLD + (255,))
    return im


mark(512).save(f"{OUT}/zp-mark.png")
mark(512, transparent=True, ring=True).save(f"{OUT}/zp-mark-512.png")
for s in (192, 180, 32):
    mark(512).resize((s, s), Image.LANCZOS).save(
        {192: "/home/ubuntu/zentra-push/icons/zp-icon-192.png",
         180: "/home/ubuntu/zentra-push/icons/zp-apple-touch-icon.png",
         32: "/home/ubuntu/zentra-push/icons/zp-favicon.png"}[s])
print("siap:", os.listdir(OUT))
