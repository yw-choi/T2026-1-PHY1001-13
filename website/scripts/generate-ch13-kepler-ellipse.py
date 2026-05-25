#!/usr/bin/env python3
# /// script
# dependencies = [
#   "matplotlib>=3.10",
#   "numpy>=2.0",
# ]
# ///
"""Generate the Chapter 13 Kepler ellipse diagram."""

from __future__ import annotations

from pathlib import Path
import re

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "public" / "img" / "ch13" / "kepler-ellipse.svg"

SOGANG_RED = "#8B0029"
BLUE = "#2563EB"
GRAY = "#374151"
GRID = "#D1D5DB"
TEXT = "#111827"
LIGHT_GRAY = "#F3F4F6"


def main() -> None:
    mpl.use("Agg")
    mpl.rcParams.update(
        {
            "svg.fonttype": "none",
            "svg.hashsalt": "phy1001-ch13-kepler-ellipse",
            "font.family": ["Apple SD Gothic Neo", "DejaVu Sans"],
            "font.size": 13,
            "axes.unicode_minus": False,
        }
    )

    a = 1.0
    e = 0.55
    c = e * a
    b = a * np.sqrt(1 - e**2)

    t = np.linspace(0, 2 * np.pi, 900)
    x = a * np.cos(t)
    y = b * np.sin(t)

    fig, ax = plt.subplots(figsize=(7.8, 4.6), dpi=100)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    ax.plot(x, y, color=SOGANG_RED, lw=3.2, solid_capstyle="round", zorder=3)

    # Main construction lines.
    ax.plot([-a, a], [0, 0], color=GRAY, lw=1.2, ls=(0, (4, 4)), zorder=1)
    ax.plot([0, 0], [0, b], color=GRAY, lw=1.2, ls=(0, (4, 4)), zorder=1)

    # Foci and center.
    ax.scatter([-c], [0], s=360, color=SOGANG_RED, zorder=5)
    ax.scatter([c], [0], s=72, facecolor="white", edgecolor=GRAY, lw=2.0, zorder=5)
    ax.scatter([0], [0], s=32, color=GRAY, zorder=5)

    label_box = dict(boxstyle="round,pad=0.18", facecolor="white", edgecolor="none", alpha=0.94)
    ax.text(-c, -0.24, "태양\n(초점)", ha="center", va="top", color=SOGANG_RED, fontsize=14, fontweight="bold")
    ax.text(c + 0.09, 0.08, "다른 초점", ha="left", va="bottom", color=GRAY, fontsize=12, bbox=label_box)
    ax.text(0.03, 0.10, "중심", ha="left", va="bottom", color=GRAY, fontsize=12, bbox=label_box)

    ax.annotate(
        "",
        xy=(a, -0.10),
        xytext=(0, -0.10),
        arrowprops=dict(arrowstyle="<->", color=GRAY, lw=1.6, shrinkA=0, shrinkB=0),
    )
    ax.text(0.5, -0.17, r"$a$", ha="center", va="top", color=TEXT, fontsize=16, fontweight="bold", bbox=label_box)

    ax.annotate(
        "",
        xy=(0.08, b),
        xytext=(0.08, 0),
        arrowprops=dict(arrowstyle="<->", color=GRAY, lw=1.5, shrinkA=0, shrinkB=0),
    )
    ax.text(0.14, 0.5 * b, r"$b$", ha="left", va="center", color=TEXT, fontsize=16, fontweight="bold", bbox=label_box)

    ax.annotate(
        "",
        xy=(0, 0.10),
        xytext=(-c, 0.10),
        arrowprops=dict(arrowstyle="<->", color=GRAY, lw=1.5, shrinkA=0, shrinkB=0),
    )
    ax.text(-0.5 * c, 0.17, r"$c=ea$", ha="center", va="bottom", color=TEXT, fontsize=14, fontweight="bold", bbox=label_box)

    ax.text(-a, 0.16, r"근일점 $R_p=a(1-e)$", ha="center", va="bottom", color=SOGANG_RED, fontsize=13, fontweight="bold", bbox=label_box)
    ax.text(a, 0.16, r"원일점 $R_a=a(1+e)$", ha="center", va="bottom", color=BLUE, fontsize=13, fontweight="bold", bbox=label_box)

    ax.text(
        0.76,
        0.76,
        r"$e=c/a$",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=16,
        fontweight="bold",
        color=TEXT,
        bbox=dict(boxstyle="round,pad=0.38", facecolor=LIGHT_GRAY, edgecolor=GRID),
    )

    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(-1.22, 1.22)
    ax.set_ylim(-0.96, 0.92)
    ax.axis("off")

    fig.subplots_adjust(left=0.03, right=0.97, top=0.94, bottom=0.06)
    fig.savefig(OUT, format="svg", transparent=False)

    svg = OUT.read_text(encoding="utf-8")
    svg = re.sub(r'width="[^"]+" height="[^"]+"', 'width="780" height="460"', svg, count=1)
    svg = re.sub(r"\n\s*<dc:date>.*?</dc:date>", "", svg, count=1)
    svg = re.sub(
        r"(<svg[^>]*>)",
        r"\1\n  <title>Kepler first law ellipse diagram</title>\n"
        r"  <desc>An elliptical orbit with the Sun at one focus, showing semimajor axis, semiminor axis, focus distance, perihelion, and aphelion.</desc>",
        svg,
        count=1,
    )
    svg = "\n".join(line.rstrip() for line in svg.splitlines()) + "\n"
    OUT.write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    main()
