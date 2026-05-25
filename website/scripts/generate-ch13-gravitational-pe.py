#!/usr/bin/env python3
# /// script
# dependencies = [
#   "matplotlib>=3.10",
#   "numpy>=2.0",
# ]
# ///
"""Generate the Chapter 13 gravitational potential energy figure."""

from __future__ import annotations

from pathlib import Path
import re

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "public" / "img" / "ch13" / "gravitational-pe.svg"

SOGANG_RED = "#8B0029"
GRAY = "#374151"
GRID = "#D1D5DB"
TEXT = "#111827"


def main() -> None:
    mpl.use("Agg")
    mpl.rcParams.update(
        {
            "svg.fonttype": "none",
            "svg.hashsalt": "phy1001-ch13-gravitational-pe",
            "font.family": ["Apple SD Gothic Neo", "DejaVu Sans"],
            "font.size": 13,
            "axes.unicode_minus": False,
            "axes.linewidth": 1.0,
            "xtick.major.width": 0.9,
            "ytick.major.width": 0.9,
        }
    )

    x = np.linspace(0.33, 8.0, 1200)
    u = -1.0 / x

    fig, ax = plt.subplots(figsize=(7.6, 4.7), dpi=100)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    y_min = -1.3
    ax.plot(x, u, color=SOGANG_RED, lw=3.3, solid_capstyle="round", zorder=4)

    ax.axhline(0, color=GRAY, lw=1.15, linestyle=(0, (4, 4)), zorder=0)

    label_box = dict(boxstyle="round,pad=0.18", facecolor="white", edgecolor="none", alpha=0.92)
    ax.text(4.35, -0.34, r"$U(r)=-GMm/r$", color=SOGANG_RED, fontsize=18, fontweight="bold", bbox=label_box)

    ax.set_xlim(0.0, 8.25)
    ax.set_ylim(y_min, 0.14)
    ax.set_xticks([0, 1, 2, 4, 6, 8])
    ax.set_yticks([-1.0, -0.5, 0.0])
    ax.set_yticklabels(["-1", "-0.5", "0"])
    ax.tick_params(axis="both", colors=TEXT, labelsize=13, length=5)

    for side in ["top", "right"]:
        ax.spines[side].set_visible(False)
    for side in ["left", "bottom"]:
        ax.spines[side].set_color(GRAY)
        ax.spines[side].set_linewidth(1.15)

    ax.grid(axis="y", color=GRID, alpha=0.7, linewidth=0.8)

    ax.set_xlabel(r"$r/R$", fontsize=15, color=TEXT, labelpad=8)
    ax.set_ylabel("")
    ax.text(
        0.0,
        1.04,
        r"$U/(GMm/R)$",
        transform=ax.transAxes,
        fontsize=15,
        color=TEXT,
        ha="left",
        va="bottom",
    )
    ax.text(
        0.5,
        1.085,
        "중력 퍼텐셜에너지 곡선",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=17,
        fontweight="bold",
        color=SOGANG_RED,
    )

    fig.subplots_adjust(left=0.12, right=0.955, top=0.82, bottom=0.15)
    fig.savefig(OUT, format="svg", transparent=False)

    svg = OUT.read_text(encoding="utf-8")
    svg = re.sub(r'width="[^"]+" height="[^"]+"', 'width="760" height="470"', svg, count=1)
    svg = re.sub(r"\n\s*<dc:date>.*?</dc:date>", "", svg, count=1)
    svg = re.sub(
        r"(<svg[^>]*>)",
        r"\1\n  <title>Gravitational potential energy curve</title>\n"
        r"  <desc>The dimensionless gravitational potential energy U/(GMm/R) follows -R/r and approaches zero from below as r goes to infinity.</desc>",
        svg,
        count=1,
    )
    svg = "\n".join(line.rstrip() for line in svg.splitlines()) + "\n"
    OUT.write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    main()
