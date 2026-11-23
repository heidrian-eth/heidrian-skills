#!/usr/bin/env python3
"""Measure colour roles and area shares in an image (an artwork or a screenshot of your UI).

Usage:  python3 measure_palette.py IMAGE [-k 6] [--crop l,t,r,b]
  -k      number of clusters (rerun at 9 if a small accent is swallowed)
  --crop  fractions to cut from each side (e.g. .05,.05,.05,.05 to drop a frame)

Prints, per cluster: median real pixel (hex), area share, CIELAB lightness L and chroma C.
Use it in the Stage 4 budget check: ground share, ink share and signal share against the kit budgets
(e.g. "signal <= 1%", "grounds >= 75%"). Needs Pillow and numpy.
"""
import argparse
import numpy as np
from PIL import Image


def to_lab(rgb):
    c = rgb / 255.0
    c = np.where(c > 0.04045, ((c + 0.055) / 1.055) ** 2.4, c / 12.92)
    M = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]])
    xyz = c @ M.T / np.array([0.95047, 1.0, 1.08883])
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    return np.stack([116 * f[:, 1] - 16, 500 * (f[:, 0] - f[:, 1]), 200 * (f[:, 1] - f[:, 2])], 1)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("image"); ap.add_argument("-k", type=int, default=6); ap.add_argument("--crop")
    a = ap.parse_args()
    im = Image.open(a.image).convert("RGB")
    if a.crop:
        l, t, r, b = map(float, a.crop.split(","))
        W, H = im.size
        im = im.crop((int(W * l), int(H * t), int(W * (1 - r)), int(H * (1 - b))))
    im.thumbnail((240, 240))
    px = np.asarray(im, dtype=float).reshape(-1, 3)
    lab = to_lab(px)
    rng = np.random.default_rng(0)
    cent = [lab[rng.integers(len(lab))]]
    for _ in range(1, a.k):  # k-means++ init
        d = np.min(((lab[:, None] - np.array(cent)[None]) ** 2).sum(-1), 1)
        cent.append(lab[rng.choice(len(lab), p=d / d.sum())])
    cent = np.array(cent)
    for _ in range(40):
        lbl = np.argmin(((lab[:, None] - cent[None]) ** 2).sum(-1), 1)
        new = np.array([lab[lbl == j].mean(0) if (lbl == j).any() else cent[j] for j in range(a.k)])
        if np.allclose(new, cent, atol=1e-3):
            break
        cent = new
    rows = []
    for j in range(a.k):
        m = lbl == j
        if m.any():
            rgb = np.median(px[m], 0)
            rows.append((m.mean(), "#%02X%02X%02X" % tuple(int(round(v)) for v in rgb), cent[j]))
    for share, hx, c in sorted(rows, key=lambda r: -r[0]):
        print(f"{hx}  {share * 100:5.1f}%   L={c[0]:.0f}  C={np.hypot(c[1], c[2]):.0f}")


if __name__ == "__main__":
    main()
