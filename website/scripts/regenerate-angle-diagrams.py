#!/usr/bin/env python3
"""Regenerate SVG diagrams whose angle arcs must be geometry-derived.

The important rule is that every angle arc is produced from
origin + radius + start/end math angles. The emitted path also carries
data-angle-* attributes so the validator can catch hand-edited drift.
"""

from __future__ import annotations

from dataclasses import dataclass
from html import escape
import math
from pathlib import Path
import re
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "public" / "img"

RED = "#8B0029"
BLUE = "#2563EB"
GRAY = "#6B7280"
LIGHT = "#F3F4F6"
BLACK = "#1a1a1a"
WHITE = "#ffffff"


def fmt(x: float) -> str:
    if abs(x) < 1e-9:
        x = 0
    s = f"{x:.1f}"
    return s[:-2] if s.endswith(".0") else s


def pt(o: tuple[float, float], r: float, deg: float) -> tuple[float, float]:
    a = math.radians(deg)
    return (o[0] + r * math.cos(a), o[1] - r * math.sin(a))


def angle_of(dx: float, dy_screen: float) -> float:
    return math.degrees(math.atan2(-dy_screen, dx))


def marker_defs(prefix: str) -> str:
    return f"""  <defs>
    <marker id="{prefix}R" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="{RED}"/></marker>
    <marker id="{prefix}B" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="{BLUE}"/></marker>
    <marker id="{prefix}G" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="{GRAY}"/></marker>
  </defs>"""


def svg(w: int, h: int, body: list[str], prefix: str = "a") -> str:
    return "\n".join(
        [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" font-family="sans-serif">',
            marker_defs(prefix),
            '  <rect width="100%" height="100%" fill="white"/>',
            *body,
            "</svg>",
            "",
        ]
    )


def attrs(**kw: object) -> str:
    out: list[str] = []
    for k, v in kw.items():
        if v is None:
            continue
        out.append(f'{k.replace("_", "-")}="{escape(str(v), quote=True)}"')
    return " ".join(out)


def line(x1: float, y1: float, x2: float, y2: float, color: str, width: float = 2,
         marker: str | None = None, dash: str | None = None, opacity: float | None = None) -> str:
    marker_attr = f' marker-end="url(#{marker})"' if marker else ""
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    opacity_attr = f' opacity="{fmt(opacity)}"' if opacity is not None else ""
    return (
        f'  <line x1="{fmt(x1)}" y1="{fmt(y1)}" x2="{fmt(x2)}" y2="{fmt(y2)}" '
        f'stroke="{color}" stroke-width="{fmt(width)}" fill="none"'
        f'{marker_attr}{dash_attr}{opacity_attr}/>'
    )


def text(x: float, y: float, value: str, color: str = BLACK, size: int = 14,
         anchor: str | None = None, weight: str | None = None, italic: bool = False,
         rotate: float | None = None) -> str:
    tr = f' transform="rotate({fmt(rotate)},{fmt(x)},{fmt(y)})"' if rotate is not None else ""
    anchor_attr = f' text-anchor="{anchor}"' if anchor else ""
    weight_attr = f' font-weight="{weight}"' if weight else ""
    italic_attr = ' font-style="italic"' if italic else ""
    return (
        f'  <text x="{fmt(x)}" y="{fmt(y)}"{tr} font-size="{size}" fill="{color}"'
        f'{anchor_attr}{weight_attr}{italic_attr}>{escape(value)}</text>'
    )


def circle(cx: float, cy: float, r: float, fill: str = LIGHT, stroke: str = GRAY, width: float = 2) -> str:
    return f'  <circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(r)}" fill="{fill}" stroke="{stroke}" stroke-width="{fmt(width)}"/>'


def rect(x: float, y: float, w: float, h: float, fill: str = LIGHT, stroke: str = GRAY,
         width: float = 1, rx: float | None = None, rotate: tuple[float, float, float] | None = None) -> str:
    rot = f' transform="rotate({fmt(rotate[0])},{fmt(rotate[1])},{fmt(rotate[2])})"' if rotate else ""
    rx_attr = f' rx="{fmt(rx)}"' if rx is not None else ""
    return (
        f'  <rect x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" height="{fmt(h)}"'
        f'{rx_attr} fill="{fill}" stroke="{stroke}" '
        f'stroke-width="{fmt(width)}"{rot}/>'
    )


def polygon(points: list[tuple[float, float]], fill: str = LIGHT, stroke: str = GRAY,
            width: float = 2, dash: str | None = None, opacity: float | None = None) -> str:
    pts = " ".join(f"{fmt(x)},{fmt(y)}" for x, y in points)
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    opacity_attr = f' opacity="{fmt(opacity)}"' if opacity is not None else ""
    return (
        f'  <polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="{fmt(width)}"'
        f'{dash_attr}{opacity_attr}/>'
    )


def path(d: str, color: str, width: float = 2, fill: str = "none",
         marker: str | None = None, dash: str | None = None, opacity: float | None = None) -> str:
    marker_attr = f' marker-end="url(#{marker})"' if marker else ""
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    opacity_attr = f' opacity="{fmt(opacity)}"' if opacity is not None else ""
    return (
        f'  <path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{fmt(width)}"'
        f'{marker_attr}{dash_attr}{opacity_attr}/>'
    )


def angle_arc(o: tuple[float, float], r: float, start: float, end: float, color: str,
              width: float = 1.5, dash: str | None = None) -> str:
    s = pt(o, r, start)
    e = pt(o, r, end)
    delta = end - start
    large = 1 if abs(delta) > 180 else 0
    sweep = 0 if delta >= 0 else 1
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'  <path d="M {fmt(s[0])},{fmt(s[1])} A {fmt(r)},{fmt(r)} 0 {large},{sweep} {fmt(e[0])},{fmt(e[1])}" '
        f'fill="none" stroke="{color}" stroke-width="{fmt(width)}"{dash_attr} '
        f'data-angle-origin="{fmt(o[0])},{fmt(o[1])}" data-angle-radius="{fmt(r)}" '
        f'data-angle-start="{fmt(start)}" data-angle-end="{fmt(end)}"/>'
    )


def angle_label(o: tuple[float, float], r: float, start: float, end: float, label: str,
                color: str, size: int = 16, offset: float = 16) -> str:
    mid = start + (end - start) / 2
    x, y = pt(o, r + offset, mid)
    return text(x, y + 5, label, color=color, size=size, anchor="middle", italic=True, weight="bold")


def arrow_from(origin: tuple[float, float], length: float, deg: float, color: str, marker: str,
               width: float = 2.5, dash: str | None = None) -> str:
    x, y = pt(origin, length, deg)
    return line(origin[0], origin[1], x, y, color, width, marker=marker, dash=dash)


def unit(deg: float) -> tuple[float, float]:
    a = math.radians(deg)
    return math.cos(a), -math.sin(a)


def add(p: tuple[float, float], v: tuple[float, float], scale: float = 1) -> tuple[float, float]:
    return p[0] + v[0] * scale, p[1] + v[1] * scale


def write(rel: str, data: str) -> None:
    path = IMG / rel
    path.write_text(data, encoding="utf-8")


def gen_ch03_vector_components() -> str:
    o = (80, 350)
    p = (460, 100)
    theta = angle_of(p[0] - o[0], p[1] - o[1])
    body = [
        line(80, 350, 600, 350, GRAY, 2, "vcG"),
        line(80, 350, 80, 40, GRAY, 2, "vcG"),
        text(610, 355, "x", GRAY, 15, italic=True),
        text(70, 35, "y", GRAY, 15, italic=True),
        text(65, 370, "O", GRAY, 14),
        line(o[0], o[1], p[0], p[1], RED, 2.5, "vcR"),
        text(290, 195, "a", RED, 18, weight="bold", italic=True),
        line(o[0], o[1], p[0], o[1], BLUE, 2, "vcB"),
        line(p[0], o[1], p[0], p[1], BLUE, 2, "vcB"),
        line(p[0], o[1], p[0], p[1], GRAY, 1, dash="4 3"),
        text(270, 385, "aₓ = a cos θ", BLUE, 14, italic=True),
        text(478, 230, "aᵧ = a sin θ", BLUE, 14, italic=True),
        angle_arc(o, 60, 0, theta, RED, 1.5),
        angle_label(o, 60, 0, theta, "θ", RED, 16),
        rect(445, 335, 15, 15, "none", GRAY, 1),
        text(160, 160, "a = √(aₓ² + aᵧ²)", GRAY, 14, italic=True),
    ]
    return svg(650, 420, body, "vc")


def gen_ch03_dot_product() -> str:
    o = (100, 300)
    a_tip = (550, 300)
    b_tip = (420, 110)
    phi = angle_of(b_tip[0] - o[0], b_tip[1] - o[1])
    proj = o[0] + (b_tip[0] - o[0]) * math.cos(math.radians(phi))
    body = [
        line(*o, *a_tip, RED, 2.5, "dpR"),
        line(*o, *b_tip, BLUE, 2.5, "dpB"),
        text(330, 330, "a", RED, 18, weight="bold", italic=True),
        text(240, 180, "b", BLUE, 18, weight="bold", italic=True),
        angle_arc(o, 80, 0, phi, GRAY, 1.5),
        angle_label(o, 80, 0, phi, "φ", GRAY, 16),
        line(b_tip[0], b_tip[1], proj, 300, GRAY, 1, dash="4 3"),
        line(o[0], o[1], proj, 300, GRAY, 2, "dpG"),
        rect(proj - 15, 285, 15, 15, "none", GRAY, 1),
        line(o[0], 345, proj, 345, GRAY, 1),
        line(o[0], 345, o[0], 340, GRAY, 1),
        line(proj, 345, proj, 340, GRAY, 1),
        text((o[0] + proj) / 2, 360, "b cos φ  (b의 a 방향 사영)", GRAY, 14, anchor="middle", italic=True),
        text(450, 80, "a · b = ab cos φ", RED, 16, weight="bold"),
        text(450, 110, "= (a 방향 b의 사영) × a", GRAY, 14),
    ]
    return svg(700, 400, body, "dp")


def gen_ch03_cross_product() -> str:
    o = (80, 320)
    a_tip = (320, 320)
    b_tip = (250, 190)
    phi = angle_of(b_tip[0] - o[0], b_tip[1] - o[1])
    body = [
        text(200, 30, "외적의 기하학적 의미", GRAY, 15, anchor="middle", weight="bold"),
        polygon([o, a_tip, (490, 190), b_tip], LIGHT, RED, 1, dash="4 3"),
        line(*o, *a_tip, RED, 2.5, "cpR"),
        line(*o, *b_tip, BLUE, 2.5, "cpB"),
        line(o[0], o[1], o[0], 80, GRAY, 2.5, "cpG"),
        text(200, 345, "a", RED, 18, weight="bold", italic=True),
        text(140, 240, "b", BLUE, 18, weight="bold", italic=True),
        text(52, 190, "c", GRAY, 16, weight="bold", italic=True),
        text(40, 210, "= a × b", GRAY, 12),
        angle_arc(o, 70, 0, phi, GRAY, 1.5),
        angle_label(o, 70, 0, phi, "φ", GRAY, 16),
        text(260, 270, "넓이 = ab sin φ", RED, 13),
        text(268, 288, "= |a × b|", RED, 13),
        line(400, 30, 400, 400, LIGHT, 2),
        text(570, 30, "오른손 법칙", GRAY, 15, anchor="middle", weight="bold"),
        line(490, 300, 600, 300, RED, 2.5, "cpR"),
        line(490, 300, 560, 210, BLUE, 2.5, "cpB"),
        line(490, 300, 490, 100, GRAY, 2.5, "cpG"),
        text(545, 330, "a", RED, 16, italic=True),
        text(510, 245, "b", BLUE, 16, italic=True),
        text(498, 180, "a × b", GRAY, 14),
        path("M 570 290 C 590 260, 580 240, 555 225", GRAY, 1.2, marker="cpG"),
        text(595, 260, "손가락", GRAY, 12),
        text(595, 276, "감는 방향", GRAY, 12),
        text(440, 370, "1. 오른손 손가락을 a 방향으로", GRAY, 13),
        text(440, 390, "2. b 방향으로 감아 쥔다", GRAY, 13),
        text(440, 410, "3. 엄지 방향 = a × b 방향", GRAY, 13),
    ]
    return svg(750, 435, body, "cp")


def gen_ch04_projectile_decomposition() -> str:
    o = (80, 380)
    speed = 145
    theta = 53
    tip = pt(o, speed, theta)
    vx_tip = (o[0] + speed * math.cos(math.radians(theta)), o[1])
    body = [
        line(40, 380, 680, 380, GRAY, 2, "pdG"),
        line(80, 400, 80, 45, GRAY, 2, "pdG"),
        text(690, 385, "x", GRAY, 14, italic=True),
        text(68, 40, "y", GRAY, 14, italic=True),
        path("M 80,380 C 215,190 420,170 650,380", RED, 2.5),
        line(*o, *tip, RED, 2.5, "pdR"),
        line(o[0], o[1], vx_tip[0], vx_tip[1], BLUE, 2, "pdB"),
        line(vx_tip[0], vx_tip[1], tip[0], tip[1], BLUE, 2, "pdB"),
        line(vx_tip[0], vx_tip[1], tip[0], tip[1], GRAY, 1, dash="4 3"),
        text(170, 250, "v₀", RED, 15, weight="bold", italic=True),
        text(165, 405, "v₀ cos θ₀", BLUE, 14, italic=True),
        text(vx_tip[0] + 8, (vx_tip[1] + tip[1]) / 2, "v₀ sin θ₀", BLUE, 14, italic=True),
        angle_arc(o, 34, 0, theta, GRAY, 1.5),
        angle_label(o, 34, 0, theta, "θ₀", GRAY, 14),
        text(330, 80, "vₓ 일정, vᵧ만 중력가속도 때문에 변함", GRAY, 14, anchor="middle"),
    ]
    return svg(720, 430, body, "pd")


def incline_triangle(body: list[str], pts: list[tuple[float, float]]) -> None:
    body.append(polygon(pts, LIGHT, GRAY, 2))


def gen_ch05_fbd_inclined_plane() -> str:
    theta = math.degrees(math.atan2(250, 310))
    body: list[str] = []
    incline_triangle(body, [(40, 380), (350, 380), (350, 130)])
    angle_arc((40, 380), 60, 0, theta, GRAY, 1.3)
    body.append(angle_label((40, 380), 60, 0, theta, "θ", GRAY, 14))
    body.append(f'  <g transform="translate(230,275) rotate({fmt(-theta)})">')
    body.append(rect(-30, -30, 60, 60, LIGHT, BLACK, 2, rx=3))
    body.append(text(0, 5, "m", BLACK, 14, anchor="middle", weight="bold"))
    body.append("  </g>")
    body += [
        line(410, 30, 410, 420, GRAY, 1, dash="4 3"),
        text(610, 40, "자유물체도 (FBD)", RED, 14, anchor="middle", weight="bold"),
        circle(600, 230, 5, BLACK, BLACK, 0),
    ]
    c = (600, 230)
    x_up = theta
    y_up = theta + 90
    body += [
        arrow_from(c, 140, x_up, GRAY, "ipG", 1, dash="4 3"),
        text(*add(c, unit(x_up), 150), "x", GRAY, 14, italic=True),
        arrow_from(c, 140, y_up, GRAY, "ipG", 1, dash="4 3"),
        text(*add(c, unit(y_up), 150), "y", GRAY, 14, italic=True),
        arrow_from(c, 132, y_up, RED, "ipR", 2.5),
        text(530, 130, "Fₙ", RED, 14, weight="bold", italic=True),
        arrow_from(c, 130, -90, RED, "ipR", 2.5),
        text(620, 358, "mg", RED, 14, weight="bold", italic=True),
        arrow_from(c, 80, x_up, RED, "ipR", 2.5),
        text(672, 185, "f", RED, 14, weight="bold", italic=True),
        arrow_from(c, 104, x_up + 180, BLUE, "ipB", 1, dash="4 3"),
        text(480, 300, "mg sin θ", BLUE, 14, weight="bold"),
        arrow_from(c, 130, y_up + 180, BLUE, "ipB", 1, dash="4 3"),
        text(665, 330, "mg cos θ", BLUE, 14, weight="bold"),
        angle_arc(c, 42, -90, -90 + theta, BLUE, 1.3),
        angle_label(c, 42, -90, -90 + theta, "θ", BLUE, 14),
        text(600, 405, "좌표축: 빗면을 따라 x, 수직으로 y", GRAY, 14, anchor="middle"),
        text(600, 425, "Fₙ = mg cos θ", GRAY, 14, anchor="middle"),
    ]
    return svg(800, 450, body, "ip")


def gen_ch06_incline_fbd() -> str:
    theta = math.degrees(math.atan2(220, 500))
    c = (380, 277)
    body: list[str] = [
        polygon([(60, 390), (560, 390), (560, 170)], LIGHT, GRAY, 2),
    ]
    for x in range(60, 561, 40):
        body.append(line(x, 396, x - 10, 406, GRAY, 1))
    angle_arc((560, 390), 50, 180, 180 - theta, GRAY, 1.3)
    body.append(angle_label((560, 390), 50, 180, 180 - theta, "θ", GRAY, 14))
    body.append(f'  <g transform="translate(380,275) rotate({fmt(-theta)})">')
    body.append(rect(-28, -28, 56, 56, LIGHT, BLACK, 2, rx=3))
    body.append(text(0, 5, "m", BLACK, 14, anchor="middle", weight="bold", italic=True))
    body.append("  </g>")
    x_down = 180 + theta
    x_up = theta
    y_up = theta + 90
    body += [
        arrow_from(c, 113, -90, RED, "ifR", 2.5),
        text(393, 383, "mg", RED, 14, weight="bold", italic=True),
        arrow_from((380, 275), 103, y_up, BLUE, "ifB", 2.5),
        text(322, 175, "N", BLUE, 14, weight="bold", italic=True),
        arrow_from((380, 275), 88, x_down, RED, "ifR", 2.5),
        text(282, 322, "f", RED, 14, weight="bold", italic=True),
        arrow_from(c, 82, x_up, GRAY, "ifG", 1, dash="4 3"),
        text(462, 238, "mg sin θ", GRAY, 14, italic=True),
        arrow_from(c, 92, y_up + 180, GRAY, "ifG", 1, dash="4 3"),
        text(428, 348, "mg cos θ", GRAY, 14, italic=True),
        arrow_from((120, 145), 60, x_up, GRAY, "ifG", 1),
        text(*add((120, 145), unit(x_up), 70), "x", GRAY, 14, italic=True),
        arrow_from((120, 145), 60, y_up, GRAY, "ifG", 1),
        text(*add((120, 145), unit(y_up), 70), "y", GRAY, 14, italic=True),
        text(620, 220, "x: mg sin θ − f = ma", BLACK, 14, anchor="middle"),
        text(620, 245, "y: N − mg cos θ = 0", BLACK, 14, anchor="middle"),
    ]
    return svg(700, 450, body, "if")


def gen_ch06_banked_curve() -> str:
    theta = math.degrees(math.atan2(180, 290))
    c = (540, 228)
    body: list[str] = [
        text(180, 30, "경사 곡선 (Banked Curve)", BLACK, 14, anchor="middle", weight="bold"),
        polygon([(40, 340), (330, 340), (330, 160)], LIGHT, GRAY, 2),
        angle_arc((330, 340), 45, 180, 180 - theta, GRAY, 1.3),
        angle_label((330, 340), 45, 180, 180 - theta, "θ", GRAY, 14),
        f'  <g transform="translate(240,235) rotate({fmt(-theta)})">',
        rect(-28, -20, 56, 40, WHITE, BLACK, 2, rx=4),
        text(0, 5, "차량", BLACK, 14, anchor="middle", weight="bold"),
        "  </g>",
        line(40, 235, 80, 235, RED, 1, dash="4 3"),
        text(40, 215, "← 원 중심", RED, 14),
        text(540, 30, "힘 분석 (마찰 없음)", BLACK, 14, anchor="middle", weight="bold"),
        rect(515, 230, 50, 40, WHITE, BLACK, 2, rx=3),
        text(540, 255, "m", BLACK, 14, anchor="middle", weight="bold", italic=True),
        arrow_from((540, 272), 118, -90, RED, "bcR", 2.5),
        text(555, 380, "mg", RED, 14, weight="bold", italic=True),
        arrow_from(c, 128, 90 + theta, BLUE, "bcB", 2.5),
        text(472, 108, "N", BLUE, 14, weight="bold", italic=True),
        arrow_from(c, 118, 90, GRAY, "bcG", 1, dash="4 3"),
        text(555, 118, "N cos θ", GRAY, 14, italic=True),
        arrow_from(c, 55, 180, GRAY, "bcG", 1, dash="4 3"),
        text(482, 220, "N sin θ", GRAY, 14, italic=True),
        line(*pt(c, 128, 90 + theta), c[0], pt(c, 128, 90 + theta)[1], GRAY, 1, dash="4 3"),
        line(*pt(c, 128, 90 + theta), pt(c, 128, 90 + theta)[0], c[1], GRAY, 1, dash="4 3"),
        angle_arc(c, 38, 90, 90 + theta, GRAY, 1.3),
        angle_label(c, 38, 90, 90 + theta, "θ", GRAY, 14),
        text(440, 242, "← 원 중심", RED, 14, weight="bold"),
        rect(120, 360, 480, 70, LIGHT, "none", 0, rx=8),
        text(360, 382, "수직 방향: N cos θ = mg", BLACK, 14, anchor="middle"),
        text(360, 402, "수평 방향 (구심): N sin θ = mv²/R", BLACK, 14, anchor="middle"),
        text(360, 422, "→  tan θ = v² / (Rg)", RED, 14, anchor="middle", weight="bold"),
    ]
    return svg(720, 450, body, "bc")


def gen_ch07_work_constant_force() -> str:
    o = (170, 220)
    f_tip = (420, 100)
    phi = angle_of(f_tip[0] - o[0], f_tip[1] - o[1])
    body = [
        rect(100, 185, 70, 70, LIGHT, BLACK, 2, rx=3),
        text(135, 227, "m", BLACK, 14, anchor="middle", weight="bold"),
        line(40, 255, 660, 255, GRAY, 1),
    ]
    for x in range(50, 191, 20):
        body.append(line(x, 255, x - 10, 265, GRAY, 1))
    body += [
        line(135, 290, 430, 290, GRAY, 2.5, "wcG"),
        text(285, 315, "d", GRAY, 14, anchor="middle", weight="bold", italic=True),
        line(*o, *f_tip, RED, 2.5, "wcR"),
        text(430, 100, "F", RED, 14, weight="bold", italic=True),
        line(o[0], o[1], f_tip[0], o[1], BLUE, 2, "wcB", dash="4 3"),
        line(f_tip[0], o[1], f_tip[0], f_tip[1], BLUE, 2, "wcB", dash="4 3"),
        text(310, 210, "F cos φ", BLUE, 14, anchor="middle", weight="bold"),
        text(460, 165, "F sin φ", BLUE, 14, weight="bold"),
        rect(408, 208, 12, 12, "none", BLUE, 1),
        angle_arc(o, 70, 0, phi, RED, 1.3),
        angle_label(o, 70, 0, phi, "φ", RED, 14),
        text(300, 350, "W = Fd cos φ", RED, 14, anchor="middle", italic=True),
        text(540, 150, "F cos φ : 일을 하는 성분", BLUE, 14),
        text(540, 175, "F sin φ : 일을 하지 않는 성분", GRAY, 14),
    ]
    return svg(700, 400, body, "wc")


def gen_ch09_elastic_collision_2d() -> str:
    o = (470, 200)
    v1 = (564, 118)
    v2 = (601, 286)
    th1 = angle_of(v1[0] - o[0], v1[1] - o[1])
    th2 = angle_of(v2[0] - o[0], v2[1] - o[1])
    body = [
        line(375, 30, 375, 320, GRAY, 1, dash="4 3"),
        text(188, 30, "충돌 전", BLACK, 14, anchor="middle", weight="bold"),
        line(40, 200, 350, 200, GRAY, 1, "ecG", dash="4 3"),
        text(358, 205, "x", GRAY, 14, italic=True),
        circle(100, 200, 22, LIGHT, BLACK, 2),
        text(100, 206, "m₁", BLACK, 14, anchor="middle", weight="bold"),
        line(127, 200, 200, 200, RED, 2.5, "ecR"),
        text(165, 188, "v₁ᵢ", RED, 14, anchor="middle", weight="bold", italic=True),
        circle(270, 200, 26, LIGHT, BLACK, 2),
        text(270, 206, "m₂", BLACK, 14, anchor="middle", weight="bold"),
        text(270, 247, "(정지)", GRAY, 13, anchor="middle"),
        text(562, 30, "충돌 후", BLACK, 14, anchor="middle", weight="bold"),
        line(400, 200, 720, 200, GRAY, 1, "ecG", dash="4 3"),
        text(728, 205, "x", GRAY, 14, italic=True),
        circle(*o, 4, GRAY, GRAY, 0),
        circle(590, 105, 22, LIGHT, BLACK, 2),
        text(590, 111, "m₁", BLACK, 14, anchor="middle", weight="bold"),
        line(476, 194, *v1, RED, 2.5, "ecR"),
        text(505, 140, "v₁f", RED, 14, weight="bold", italic=True),
        angle_arc(o, 40, 0, th1, RED, 1.2),
        angle_label(o, 40, 0, th1, "θ₁", RED, 14),
        circle(630, 300, 26, LIGHT, BLACK, 2),
        text(630, 306, "m₂", BLACK, 14, anchor="middle", weight="bold"),
        line(476, 206, *v2, BLUE, 2.5, "ecB"),
        text(555, 275, "v₂f", BLUE, 14, weight="bold", italic=True),
        angle_arc(o, 45, 0, th2, BLUE, 1.2),
        angle_label(o, 45, 0, th2, "θ₂", BLUE, 14),
        rect(60, 340, 630, 85, LIGHT, RED, 1, rx=8),
        text(375, 365, "2차원 탄성 충돌 보존법칙", RED, 14, anchor="middle", weight="bold"),
        text(375, 390, "x : m₁v₁ᵢ = m₁v₁f cosθ₁ + m₂v₂f cosθ₂", RED, 14, anchor="middle"),
        text(375, 415, "y : 0 = m₁v₁f sinθ₁ − m₂v₂f sinθ₂", BLUE, 14, anchor="middle"),
    ]
    return svg(750, 440, body, "ec")


def gen_ch10_angular_position() -> str:
    c = (300, 225)
    theta = 40.2
    pnt = pt(c, 160, theta)
    body = [
        circle(*c, 160, LIGHT, GRAY, 2),
        circle(*c, 4, BLACK, BLACK, 0),
        text(285, 250, "O", BLACK, 14, weight="bold"),
        line(*c, 470, 225, GRAY, 1, dash="4 3"),
        text(475, 230, "기준선", GRAY, 14),
        line(*c, *pnt, RED, 2.5, "apR"),
        circle(*pnt, 6, RED, RED, 0),
        text(pnt[0] + 13, pnt[1] - 4, "P", RED, 14, weight="bold"),
        text(370, 165, "r", RED, 14, weight="bold", italic=True),
        angle_arc(c, 50, 0, theta, RED, 2),
        angle_label(c, 50, 0, theta, "θ", RED, 14),
        angle_arc(c, 160, 0, theta, BLUE, 2.5),
        text(460, 165, "s", BLUE, 14, weight="bold", italic=True),
        rect(40, 370, 280, 55, LIGHT, GRAY, 1, rx=8),
        text(180, 395, "θ = s / r  (rad)", RED, 16, anchor="middle", weight="bold"),
        text(180, 415, "1 rev = 2π rad = 360°", GRAY, 14, anchor="middle"),
        angle_arc(c, 50, 230, 310, GRAY, 1.2),
        text(275, 310, "+ 방향 (반시계)", GRAY, 14),
        text(300, 55, "회전축 (지면에 수직)", GRAY, 14, anchor="middle"),
        circle(*c, 8, "none", GRAY, 1),
    ]
    return svg(700, 450, body, "ap")


def gen_ch10_linear_angular_relation() -> str:
    c = (280, 220)
    theta = 35
    pnt = pt(c, 150, theta)
    tang = theta + 90
    body = [
        circle(*c, 150, LIGHT, GRAY, 2),
        circle(*c, 4, BLACK, BLACK, 0),
        text(265, 240, "O", BLACK, 14, weight="bold"),
        line(*c, *pnt, GRAY, 1, dash="4 3"),
        text(330, 195, "r", GRAY, 14, italic=True),
        circle(*pnt, 7, RED, RED, 0),
        text(pnt[0] + 12, pnt[1] - 9, "P", RED, 16, weight="bold"),
        arrow_from(pnt, 95, tang, BLUE, "laB", 2.5),
        text(pnt[0] - 65, pnt[1] - 86, "v = ωr", BLUE, 14, weight="bold", italic=True),
        arrow_from((pnt[0] + 11, pnt[1] + 11), 52, tang, BLUE, "laB", 1.5, dash="4 3"),
        text(pnt[0] + 8, pnt[1] - 43, "aₜ = αr", BLUE, 14, italic=True),
        line(pnt[0], pnt[1], 330, 185, RED, 2.5, "laR"),
        text(300, 190, "aᵣ = ω²r", RED, 14, italic=True),
        text(300, 207, "(구심)", RED, 14),
        angle_arc(c, 50, 230, 310, RED, 2),
        text(265, 300, "ω", RED, 14, weight="bold", italic=True),
        rect(490, 40, 240, 185, LIGHT, GRAY, 1, rx=8),
        text(610, 68, "선형-각 관계", RED, 14, anchor="middle", weight="bold"),
        text(510, 98, "호 길이:", BLACK, 14),
        text(640, 98, "s = θr", BLUE, 14, weight="bold", italic=True),
        text(510, 125, "접선 속력:", BLACK, 14),
        text(640, 125, "v = ωr", BLUE, 14, weight="bold", italic=True),
        text(510, 152, "접선 가속도:", BLACK, 14),
        text(648, 152, "aₜ = αr", BLUE, 14, weight="bold", italic=True),
        text(510, 179, "구심 가속도:", BLACK, 14),
        text(648, 179, "aᵣ = ω²r", RED, 14, weight="bold", italic=True),
        line(500, 195, 720, 195, GRAY, 1),
        text(610, 213, "모든 각도는 라디안(rad)", GRAY, 14, anchor="middle"),
        rect(pnt[0] - 10, pnt[1] - 10, 8, 8, "none", GRAY, 1, rotate=(-55, pnt[0], pnt[1])),
    ]
    return svg(750, 450, body, "la")


def gen_torque_definition() -> str:
    axis = (160, 230)
    pnt = (410, 160)
    r_ang = angle_of(pnt[0] - axis[0], pnt[1] - axis[1])
    f_end = (420, 30)
    f_ang = angle_of(f_end[0] - pnt[0], f_end[1] - pnt[1])
    body = [
        f'  <ellipse cx="300" cy="230" rx="200" ry="130" fill="{LIGHT}" stroke="{GRAY}" stroke-width="2"/>',
        text(300, 340, "강체", GRAY, 14, anchor="middle"),
        circle(*axis, 5, BLACK, BLACK, 0),
        circle(*axis, 10, "none", BLACK, 1),
        text(140, 265, "회전축", BLACK, 14, weight="bold"),
        line(*axis, *pnt, GRAY, 2.5, "tdG"),
        text(275, 185, "r", GRAY, 14, weight="bold", italic=True),
        circle(*pnt, 6, RED, RED, 0),
        text(398, 148, "P", RED, 14, weight="bold"),
        line(*pnt, *f_end, RED, 2.5, "tdR"),
        text(428, 35, "F", RED, 14, weight="bold", italic=True),
        arrow_from(pnt, 78, r_ang, GRAY, "tdG", 1, dash="4 3"),
        angle_arc(pnt, 40, r_ang, f_ang, RED, 1.5),
        angle_label(pnt, 40, r_ang, f_ang, "φ", RED, 14),
        line(401, 283, 424, 20, GRAY, 1, dash="4 3"),
        text(435, 22, "힘의 작용선", GRAY, 14),
        line(160, 230, 403, 249, BLUE, 1.5, dash="4 3"),
        rect(396, 242, 8, 8, "none", BLUE, 1, rotate=(-86, 403, 249)),
        text(240, 228, "모멘트 팔", BLUE, 14, weight="bold"),
        text(248, 258, "r sin φ", BLUE, 14, italic=True),
        rect(490, 300, 240, 90, LIGHT, GRAY, 1, rx=8),
        text(610, 328, "토크 (torque)", RED, 14, anchor="middle", weight="bold"),
        text(610, 355, "τ = rF sin φ", BLACK, 16, anchor="middle", italic=True),
        text(610, 380, "단위: N·m (뉴턴미터)", GRAY, 14, anchor="middle"),
    ]
    return svg(750, 450, body, "td")


def gen_ch11_angular_momentum_definition() -> str:
    o = (160, 300)
    pnt = (400, 160)
    r_ang = angle_of(pnt[0] - o[0], pnt[1] - o[1])
    p_ang = 90
    body = [
        line(400, 40, 400, 400, GRAY, 1.5, dash="5 4"),
        line(o[0], o[1], 395, 300, BLUE, 2, dash="6 3"),
        rect(388, 288, 12, 12, "none", BLUE, 1.5),
        text(280, 325, "r sin φ", BLUE, 18, anchor="middle", weight="bold", italic=True),
        line(*o, 392, 166, BLUE, 3, "lmB"),
        text(262, 252, "r", BLUE, 26, weight="bold", italic=True),
        circle(*o, 6, BLACK, BLACK, 0),
        text(145, 325, "O", BLACK, 22, weight="bold"),
        circle(95, 220, 18, "none", RED, 2.5),
        circle(95, 220, 5, RED, RED, 0),
        text(69, 226, "ℓ", RED, 24, anchor="end", weight="bold", italic=True),
        text(69, 248, "지면 밖", GRAY, 13, anchor="end"),
        circle(*pnt, 11, LIGHT, GRAY, 2.5),
        text(420, 156, "m", BLACK, 20, italic=True),
        line(400, 153, 400, 40, RED, 3, "lmR"),
        text(416, 65, "p = mv", RED, 24, weight="bold", italic=True),
        angle_arc(pnt, 28, r_ang, p_ang, GRAY, 1.5),
        angle_label(pnt, 28, r_ang, p_ang, "φ", GRAY, 18),
    ]
    return svg(700, 440, body, "lm")


def gen_ch11_torque_cross_product() -> str:
    o = (140, 320)
    pnt = (380, 160)
    f_end = (495, 211)
    r_ang = angle_of(pnt[0] - o[0], pnt[1] - o[1])
    f_ang = angle_of(f_end[0] - pnt[0], f_end[1] - pnt[1])
    body = [
        circle(*o, 6, BLACK, BLACK, 0),
        text(125, 345, "O", BLACK, 22, weight="bold"),
        line(220, 86, 560, 237, GRAY, 1.5, dash="5 4"),
        text(568, 245, "힘의 작용선", GRAY, 14),
        line(140, 320, 256, 105, BLUE, 2, dash="6 3"),
        rect(251, 100, 11, 11, "none", BLUE, 1.5, rotate=(24, 256.5, 105.5)),
        text(158, 208, "r sin φ", BLUE, 18, weight="bold", italic=True),
        line(*o, *pnt, BLUE, 3, "tcB"),
        text(240, 252, "r", BLUE, 26, weight="bold", italic=True),
        circle(*pnt, 5, BLACK, BLACK, 0),
        text(372, 148, "P", BLACK, 18, anchor="end"),
        line(*pnt, *f_end, RED, 3, "tcR"),
        text(510, 220, "F", RED, 26, weight="bold", italic=True),
        angle_arc(pnt, 30, f_ang, r_ang, GRAY, 1.5),
        angle_label(pnt, 30, f_ang, r_ang, "φ", GRAY, 18),
        circle(80, 130, 18, "none", RED, 2.5),
        line(67, 117, 93, 143, RED, 2.5),
        line(93, 117, 67, 143, RED, 2.5),
        text(106, 138, "τ", RED, 24, weight="bold", italic=True),
        text(57, 172, "지면 안쪽", GRAY, 13),
    ]
    return svg(700, 420, body, "tc")


def gen_ch11_precession_vectors() -> str:
    c = (220, 195)
    dphi = 25
    l1 = pt(c, 150, 0)
    l2 = pt(c, 145, dphi)
    body = [
        text(220, 28, "위에서 본 모습 (top view)", GRAY, 15, anchor="middle"),
        circle(*c, 150, "none", GRAY, 1.5),
        circle(*c, 4, GRAY, GRAY, 0),
        text(205, 218, "O", GRAY, 14),
        line(*c, *l1, RED, 2.5, "pvR"),
        text(340, 225, "L(t)", RED, 17, weight="bold", italic=True),
        line(*c, *l2, RED, 2, "pvR", dash="5 3"),
        text(360, 122, "L(t+dt)", RED, 17, weight="bold", italic=True),
        line(*l1, *l2, BLUE, 2.5, "pvB"),
        text(388, 155, "dL", BLUE, 18, weight="bold", italic=True),
        text(388, 175, "= τ dt", BLUE, 14),
        angle_arc(c, 55, 0, dphi, GRAY, 1.5),
        angle_label(c, 55, 0, dphi, "dφ", GRAY, 17),
        angle_arc(c, 150, 50, 130, GRAY, 2),
        text(225, 60, "세차 방향", GRAY, 14, anchor="middle"),
        text(250, 355, "|dL| = L · dφ = τ · dt = Mgr · dt", GRAY, 16, anchor="middle"),
    ]
    return svg(500, 380, body, "pv")


def gen_ch11_gyroscope_precession() -> str:
    pivot = (251, 340)
    wheel = (460, 210)
    theta = 90 - angle_of(wheel[0] - pivot[0], wheel[1] - pivot[1])
    axis_ang = 90 - theta
    body = [
        line(50, 440, 530, 440, GRAY, 2),
    ]
    for x in range(70, 511, 40):
        body.append(line(x, 440, x - 15, 455, GRAY, 1))
    body += [
        rect(240, 340, 22, 100, LIGHT, GRAY, 2, rx=1),
        rect(222, 430, 58, 10, LIGHT, GRAY, 2, rx=2),
        line(251, 335, 251, 50, GRAY, 1, dash="5 4"),
        text(260, 58, "z", GRAY, 16, italic=True),
        f'  <ellipse cx="251" cy="210" rx="209" ry="65" fill="none" stroke="{GRAY}" stroke-width="1.5" stroke-dasharray="6 5"/>',
        line(251, 340, 42, 210, GRAY, 1.5, dash="5 4", opacity=0.4),
        circle(*pivot, 4, BLACK, BLACK, 0),
        text(228, 358, "O (지지점)", GRAY, 15, anchor="end"),
        line(*pivot, *wheel, BLACK, 3),
        angle_arc(pivot, 65, 90, axis_ang, GRAY, 1.5),
        angle_label(pivot, 65, 90, axis_ang, "θ", GRAY, 20),
        f'  <ellipse cx="460" cy="210" rx="10" ry="55" transform="rotate(-32,460,210)" fill="{LIGHT}" stroke="{GRAY}" stroke-width="2.5"/>',
        circle(*wheel, 3, GRAY, GRAY, 0),
        line(278, 310, 436, 211, RED, 3, "gpR"),
        text(420, 196, "L", RED, 24, weight="bold", italic=True),
        line(474, 201, 535, 163, BLUE, 2.5, "gpB"),
        text(543, 170, "ω", BLUE, 22, weight="bold", italic=True),
        line(460, 265, 460, 390, BLUE, 2.5, "gpB"),
        text(475, 382, "Mg", BLUE, 20, weight="bold", italic=True),
        text(368, 296, "r", GRAY, 18, anchor="middle", italic=True),
        f'  <path d="M 290,80 A 42,14 0 0,0 212,80" fill="none" stroke="{RED}" stroke-width="2.5" marker-end="url(#gpR)"/>',
        text(251, 62, "Ω", RED, 22, anchor="middle", weight="bold", italic=True),
        text(600, 260, "τ = r × Mg", RED, 18, anchor="middle"),
        text(600, 282, "수평, L에 ⊥", GRAY, 14, anchor="middle"),
    ]
    return svg(700, 500, body, "gp")


def gen_ch11_rolling_ramp_fbd() -> str:
    corner = (660, 430)
    theta = math.degrees(math.atan2(300, 600))
    body = [
        polygon([(60, 430), (660, 430), (660, 130)], LIGHT, GRAY, 2),
        line(60, 430, 700, 430, GRAY, 2),
    ]
    for x in range(80, 641, 40):
        body.append(line(x, 430, x - 15, 448, GRAY, 1.2))
    body += [
        angle_arc(corner, 60, 180, 180 - theta, GRAY, 1.5),
        angle_label(corner, 60, 180, 180 - theta, "θ", GRAY, 20),
        circle(341, 243, 42, LIGHT, GRAY, 2.5),
        circle(341, 243, 3, GRAY, GRAY, 0),
        text(341, 252, "M", BLACK, 22, anchor="middle", weight="bold", italic=True),
        angle_arc((341, 243), 47, 66, 132, BLUE, 2.5),
        text(372, 204, "ω", BLUE, 20, weight="bold", italic=True),
        line(341, 287, 341, 372, RED, 3, "rrR"),
        text(356, 368, "Mg", RED, 22, weight="bold", italic=True),
        line(360, 280, 320, 200, BLUE, 3, "rrB"),
        text(295, 195, "N", BLUE, 22, anchor="end", weight="bold", italic=True),
        line(360, 280, 427, 247, RED, 3, "rrR"),
        text(438, 248, "fₛ", RED, 22, weight="bold", italic=True),
        circle(360, 280, 3.5, BLACK, BLACK, 0),
        line(341, 243, 271, 278, GRAY, 2.5, "rrG", dash="6 4"),
        text(200, 276, "a_com", GRAY, 20, weight="bold", italic=True),
        line(110, 110, 65.3, 132.4, GRAY, 2, "rrG"),
        text(52, 143, "x", GRAY, 20, weight="bold", italic=True),
        line(110, 110, 87.6, 65.3, GRAY, 2, "rrG"),
        text(78, 60, "y", GRAY, 20, weight="bold", italic=True),
    ]
    return svg(720, 500, body, "rr")


def gen_ch11_yoyo_fbd() -> str:
    body = [
        rect(160, 42, 80, 10, GRAY, GRAY, 0, rx=3),
        line(200, 52, 200, 247, GRAY, 1.5),
        circle(200, 268, 75, LIGHT, GRAY, 2.5),
        circle(200, 268, 20, WHITE, GRAY, 1.5),
        circle(200, 268, 3, GRAY, GRAY, 0),
        line(200, 248, 200, 108, RED, 2.5, "yyR"),
        text(215, 168, "T", RED, 18, weight="bold", italic=True),
        line(200, 348, 200, 468, BLUE, 2.5, "yyB"),
        text(215, 448, "Mg", BLUE, 18, weight="bold", italic=True),
        line(200, 304, 275, 304, GRAY, 1, dash="4 3"),
        text(237, 322, "R", GRAY, 15, anchor="middle", italic=True),
        line(220, 268, 280, 238, GRAY, 0.8, dash="3 2"),
        circle(220, 268, 2, GRAY, GRAY, 0),
        text(284, 242, "R₀", GRAY, 14, italic=True),
        angle_arc((200, 268), 75, 115, 65, BLUE, 2),
        text(240, 202, "α", BLUE, 16, italic=True),
        line(95, 250, 95, 348, GRAY, 2, "yyG", dash="6 4"),
        text(42, 310, "a_com", GRAY, 15, weight="bold", italic=True),
    ]
    return svg(400, 500, body, "yy")


def gen_ch12_ladder_fbd() -> str:
    base = (150, 440)
    top = (450, 100)
    theta = angle_of(top[0] - base[0], top[1] - base[1])
    body = [
        rect(450, 40, 22, 400, LIGHT, GRAY, 2),
        line(40, 440, 470, 440, GRAY, 2),
    ]
    for y in range(60, 421, 40):
        body.append(line(472, y, 488, y + 16, GRAY, 1))
    for x in range(60, 421, 40):
        body.append(line(x, 440, x - 12, 456, GRAY, 1))
    body += [
        line(*base, *top, BLACK, 2.5),
        angle_arc(base, 60, 0, theta, GRAY, 1.3),
        angle_label(base, 60, 0, theta, "θ", GRAY, 20),
        circle(305, 276, 4, RED, RED, 0),
        line(305, 276, 305, 360, RED, 2.5, "ldR"),
        text(320, 355, "mg", RED, 22, weight="bold", italic=True),
        line(450, 100, 370, 100, BLUE, 2.5, "ldB"),
        text(395, 86, "F_w", BLUE, 22, weight="bold", italic=True),
        line(150, 440, 150, 360, BLUE, 2.5, "ldB"),
        text(125, 380, "N", BLUE, 22, anchor="end", weight="bold", italic=True),
        line(155, 432, 225, 432, RED, 2.5, "ldR"),
        text(190, 424, "f", RED, 22, anchor="middle", weight="bold", italic=True),
        circle(*base, 4, BLACK, BLACK, 0),
    ]
    return svg(620, 500, body, "ld")


def gen_ch12_crane_boom_fbd() -> str:
    pivot = (82, 370)
    tip = (480, 130)
    theta = angle_of(tip[0] - pivot[0], tip[1] - pivot[1])
    body = [
        rect(60, 40, 22, 380, LIGHT, GRAY, 2),
    ]
    for y in range(60, 381, 40):
        body.append(line(60, y, 44, y + 16, GRAY, 1))
    body += [
        line(*pivot, *tip, BLACK, 2.5),
        line(82, 130, *tip, GRAY, 2),
        text(220, 118, "케이블", GRAY, 16),
        angle_arc(pivot, 70, 0, theta, GRAY, 1.3),
        angle_label(pivot, 70, 0, theta, "θ", GRAY, 20),
        line(tip[0], tip[1], tip[0], 160, GRAY, 2),
        rect(455, 160, 50, 50, "#E5E7EB", BLACK, 2),
        text(480, 192, "M", BLACK, 22, anchor="middle", weight="bold", italic=True),
        line(480, 210, 480, 295, RED, 2.5, "cbR"),
        text(496, 290, "Mg", RED, 22, weight="bold", italic=True),
        line(280, 250, 280, 335, RED, 2.5, "cbR"),
        text(294, 328, "mg", RED, 22, weight="bold", italic=True),
        line(475, 130, 395, 130, BLUE, 2.5, "cbB"),
        text(430, 148, "T", BLUE, 22, anchor="middle", weight="bold", italic=True),
        circle(*pivot, 5, RED, RED, 0),
        line(82, 370, 82, 285, BLUE, 2.5, "cbB"),
        text(60, 305, "F_v", BLUE, 22, anchor="end", weight="bold", italic=True),
        line(82, 370, 170, 370, BLUE, 2.5, "cbB"),
        text(135, 392, "F_h", BLUE, 22, weight="bold", italic=True),
    ]
    return svg(740, 480, body, "cb")


def gen_ch15_pendulum_geometry() -> str:
    pivot = (360, 72)
    bob = (486.8, 310.4)
    string_angle = angle_of(bob[0] - pivot[0], bob[1] - pivot[1])
    body = [
        rect(278, 42, 164, 22, LIGHT, GRAY, 2, rx=5),
        line(360, 72, 360, 352, GRAY, 1.5, dash="6 5"),
        angle_arc(pivot, 270, -90, string_angle, GRAY, 1.8, dash="6 5"),
        angle_arc(pivot, 52, -90, string_angle, RED, 2.5),
        angle_label(pivot, 52, -90, string_angle, "θ", RED, 18),
        circle(*pivot, 8, GRAY, GRAY, 0),
        line(*pivot, *bob, BLACK, 3),
        text(424, 200, "L", BLACK, 18, anchor="middle", weight="bold", italic=True),
        line(*bob, 438.0, 218.6, BLUE, 4.5, "pgB"),
        text(438, 251, "T", BLUE, 18, anchor="middle", weight="bold", italic=True),
        line(*bob, bob[0], 420, RED, 4.5, "pgR"),
        text(524, 385, "mg", RED, 18, anchor="middle", weight="bold"),
        line(*bob, 401.2, 355.9, RED, 4.5, "pgR"),
        text(419, 384, "mg sinθ", RED, 18, anchor="middle", weight="bold"),
        circle(*bob, 34, LIGHT, GRAY, 2.5),
        text(bob[0], bob[1] + 12, "m", BLACK, 34, anchor="middle", weight="bold", italic=True),
    ]
    return svg(800, 460, body, "pg")


def gen_ch15_reference_circle() -> str:
    c = (350, 220)
    pnt = (446, 105)
    theta = angle_of(pnt[0] - c[0], pnt[1] - c[1])
    body = [
        line(130, 220, 642, 220, GRAY, 2, "rcG"),
        line(350, 55, 350, 376, GRAY, 1.6, dash="7 6"),
        text(660, 227, "x", GRAY, 20, italic=True),
        circle(*c, 150, LIGHT, GRAY, 2.2),
        circle(*c, 5.5, GRAY, GRAY, 0),
        text(328, 244, "O", GRAY, 20, anchor="middle", weight="bold"),
        line(*c, *pnt, RED, 4),
        circle(*pnt, 11, RED, RED, 0),
        text(482, 96, "P′", RED, 23, anchor="middle", weight="bold"),
        line(pnt[0], pnt[1], pnt[0], c[1], GRAY, 1.6, dash="7 6"),
        circle(pnt[0], c[1], 10, BLUE, BLUE, 0),
        text(477, 253, "P", BLUE, 23, anchor="middle", weight="bold"),
        angle_arc(c, 55, 0, theta, RED, 2.7),
        angle_label(c, 55, 0, theta, "θ", RED, 20),
        line(350, 252, pnt[0], 252, BLUE, 3.2, "rcB"),
        line(350, 220, 350, 262, BLUE, 1.6),
        line(pnt[0], 220, pnt[0], 262, BLUE, 1.6),
        text(405, 285, "x(t)", BLUE, 20, anchor="middle", weight="bold", italic=True),
        text(396, 151, "xₘ", RED, 20, anchor="middle", weight="bold", italic=True),
        line(pnt[0], pnt[1], pnt[0], c[1], GRAY, 1.2, dash="3 5"),
    ]
    return svg(800, 430, body, "rc")


def gen_ch16_phasor_addition() -> str:
    c = (200, 220)
    a1, l1 = 20, 120
    a2, l2 = 72, 105
    p1 = pt(c, l1, a1)
    p2 = pt(c, l2, a2)
    res = (p1[0] + p2[0] - c[0], p1[1] + p2[1] - c[1])
    beta = angle_of(res[0] - c[0], res[1] - c[1])
    body = [
        text(350, 25, "위상자(Phasor) 덧셈", RED, 17, anchor="middle", weight="bold"),
        line(50, 220, 400, 220, GRAY, 1, dash="4 3"),
        line(200, 350, 200, 70, GRAY, 1, dash="4 3"),
        angle_arc(c, 135, 85, 135, GRAY, 1.5),
        text(185, 80, "ω", GRAY, 14, anchor="middle", italic=True),
        line(*c, *p1, BLUE, 2.5, "phB"),
        text((c[0] + p1[0]) / 2, (c[1] + p1[1]) / 2 - 12, "yₘ₁", BLUE, 15, weight="bold", italic=True),
        line(*c, *p2, RED, 2.5, "phR"),
        text((c[0] + p2[0]) / 2 + 12, (c[1] + p2[1]) / 2, "yₘ₂", RED, 15, weight="bold", italic=True),
        line(*p1, *res, RED, 1.3, dash="5 3"),
        line(*p2, *res, BLUE, 1.3, dash="5 3"),
        line(*c, *res, GRAY, 2.4, "phG"),
        text((c[0] + res[0]) / 2 + 12, (c[1] + res[1]) / 2 - 8, "y′ₘ", GRAY, 15, weight="bold", italic=True),
        angle_arc(c, 38, a1, a2, RED, 1.5),
        angle_label(c, 38, a1, a2, "φ", RED, 14),
        angle_arc(c, 58, 0, beta, GRAY, 1.5),
        angle_label(c, 58, 0, beta, "β", GRAY, 13),
        rect(460, 80, 220, 275, LIGHT, GRAY, 1, rx=8),
        text(570, 110, "파동 합성", RED, 14, anchor="middle", weight="bold"),
        text(475, 140, "y₁ = yₘ₁ sin(kx − ωt)", BLUE, 13, italic=True),
        text(475, 170, "y₂ = yₘ₂ sin(kx − ωt + φ)", RED, 13, italic=True),
        line(475, 185, 665, 185, GRAY, 0.8),
        text(475, 210, "합성파:", BLACK, 13, weight="bold"),
        text(475, 235, "y′ = y′ₘ sin(kx − ωt + β)", GRAY, 13, italic=True),
        text(475, 265, "y′ₘ = 위상자 벡터합의 크기", BLACK, 12),
        text(475, 290, "β = 합성 위상자의 각도", BLACK, 12),
        line(475, 302, 665, 302, GRAY, 0.8),
        text(475, 325, "같은 진폭(yₘ₁=yₘ₂=yₘ)일 때:", GRAY, 12),
        text(475, 345, "y′ₘ = |2yₘ cos(φ/2)|", RED, 12, weight="bold", italic=True),
    ]
    return svg(700, 380, body, "ph")


def gen_ch16_wave_speed_string() -> str:
    center = (340, 250)
    R = 130
    th = 16
    left = pt(center, R, 90 + th)
    right = pt(center, R, 90 - th)
    body = [
        text(350, 30, "줄 위의 펄스 (펄스와 함께 움직이는 기준틀)", BLACK, 15, anchor="middle", weight="bold"),
        line(40, 220, 220, 220, BLACK, 2.5),
        path("M220,220 Q280,120 340,120 Q400,120 460,220", BLACK, 2.5),
        line(460, 220, 640, 220, BLACK, 2.5),
        angle_arc(center, R, 90 + th, 90 - th, RED, 3),
        text(340, 105, "Δl", RED, 13, anchor="middle", weight="bold"),
        circle(*center, 3, GRAY, GRAY, 0),
        text(350, 265, "O", GRAY, 12, italic=True),
        line(*center, *left, GRAY, 1, dash="4 3"),
        line(*center, *right, GRAY, 1, dash="4 3"),
        text(305, 195, "R", GRAY, 14, italic=True),
        angle_arc(center, 24, 90, 90 + th, GRAY, 1.2),
        angle_label(center, 24, 90, 90 + th, "θ", GRAY, 12, offset=9),
        angle_arc(center, 24, 90, 90 - th, GRAY, 1.2),
        angle_label(center, 24, 90, 90 - th, "θ", GRAY, 12, offset=9),
        line(*left, 270, 145, RED, 2.5, "wsR"),
        text(255, 155, "τ", RED, 14, weight="bold", italic=True),
        line(*right, 410, 145, RED, 2.5, "wsR"),
        text(418, 155, "τ", RED, 14, weight="bold", italic=True),
        line(150, 220, 100, 220, BLUE, 2.5, "wsB"),
        text(125, 240, "v", BLUE, 13, anchor="middle", weight="bold", italic=True),
        line(560, 220, 510, 220, BLUE, 2.5, "wsB"),
        text(535, 240, "v", BLUE, 13, anchor="middle", weight="bold", italic=True),
        line(340, 118, 340, 165, RED, 2, "wsR"),
        text(355, 150, "F", RED, 13, weight="bold"),
        rect(80, 290, 540, 90, LIGHT, GRAY, 1, rx=8),
        text(350, 315, "F = ma :  τ Δl/R = (μ Δl) v²/R", BLACK, 13, anchor="middle"),
        text(350, 345, "v = √(τ/μ)", RED, 16, anchor="middle", weight="bold", italic=True),
        text(350, 370, "τ : 장력(tension), μ : 선밀도(linear density)", GRAY, 12, anchor="middle"),
    ]
    return svg(700, 400, body, "ws")


def gen_ch17_mach_cone() -> str:
    source = (590, 210)
    old = (190, 210)
    radius = 170
    dist = source[0] - old[0]
    theta = math.degrees(math.asin(radius / dist))
    upper_ang = 180 - theta
    lower_ang = 180 + theta
    upper_end = pt(source, 430, upper_ang)
    lower_end = pt(source, 430, lower_ang)
    body = [
        text(375, 28, "마하 원뿔과 충격파 (vₛ > v)", RED, 15, anchor="middle", weight="bold"),
    ]
    for cx, r, op in [(190, 170, "30"), (270, 136, "40"), (350, 102, "55"), (430, 68, "77"), (510, 34, "99")]:
        body.append(circle(cx, 210, 3 if cx != 190 else 4, GRAY, GRAY, 0))
        body.append(f'  <circle cx="{cx}" cy="210" r="{r}" fill="none" stroke="#2563EB{op}" stroke-width="1.2"/>')
    body += [
        text(190, 235, "S₁", GRAY, 10, anchor="middle"),
        circle(*source, 8, RED, RED, 0),
        text(605, 207, "S", RED, 14, weight="bold"),
        line(600, 210, 660, 210, RED, 2.5, "mcR"),
        text(640, 198, "vₛ", RED, 13, weight="bold", italic=True),
        line(*source, *upper_end, RED, 2.5),
        line(*source, *lower_end, RED, 2.5),
        text(350, 72, "충격파 면 (Mach cone)", RED, 12, anchor="middle", weight="bold", rotate=-(theta)),
        angle_arc(source, 40, 180, upper_ang, GRAY, 1.5),
        angle_label(source, 40, 180, upper_ang, "θ", GRAY, 14),
        line(190, 395, 590, 395, GRAY, 1),
        line(190, 388, 190, 402, GRAY, 1.5),
        line(590, 388, 590, 402, GRAY, 1.5),
        text(390, 412, "vₛ t", GRAY, 12, anchor="middle", italic=True),
        line(190, 210, 190, 40, GRAY, 0.8, dash="3 3"),
        text(168, 130, "vt", GRAY, 12, anchor="middle", italic=True),
        rect(440, 310, 280, 70, LIGHT, GRAY, 1, rx=8),
        text(580, 335, "sin θ = v / vₛ", RED, 14, anchor="middle", weight="bold"),
        text(580, 360, "Ma = vₛ / v  (Mach number)", GRAY, 13, anchor="middle"),
    ]
    return svg(750, 440, body, "mc")


GENERATORS = {
    "ch03/vector-components.svg": gen_ch03_vector_components,
    "ch03/dot-product.svg": gen_ch03_dot_product,
    "ch03/cross-product.svg": gen_ch03_cross_product,
    "ch04/projectile-decomposition.svg": gen_ch04_projectile_decomposition,
    "ch05/fbd-inclined-plane.svg": gen_ch05_fbd_inclined_plane,
    "ch06/incline-fbd.svg": gen_ch06_incline_fbd,
    "ch06/banked-curve.svg": gen_ch06_banked_curve,
    "ch07/work-constant-force.svg": gen_ch07_work_constant_force,
    "ch09/elastic-collision-2d.svg": gen_ch09_elastic_collision_2d,
    "ch10/angular-position.svg": gen_ch10_angular_position,
    "ch10/linear-angular-relation.svg": gen_ch10_linear_angular_relation,
    "ch10/torque-definition.svg": gen_torque_definition,
    "ch11/angular-momentum-definition.svg": gen_ch11_angular_momentum_definition,
    "ch11/torque-cross-product.svg": gen_ch11_torque_cross_product,
    "ch11/precession-vectors.svg": gen_ch11_precession_vectors,
    "ch11/gyroscope-precession.svg": gen_ch11_gyroscope_precession,
    "ch11/rolling-ramp-fbd.svg": gen_ch11_rolling_ramp_fbd,
    "ch11/yoyo-fbd.svg": gen_ch11_yoyo_fbd,
    "ch12/ladder-fbd.svg": gen_ch12_ladder_fbd,
    "ch12/crane-boom-fbd.svg": gen_ch12_crane_boom_fbd,
    "ch15/pendulum-geometry.svg": gen_ch15_pendulum_geometry,
    "ch15/reference-circle.svg": gen_ch15_reference_circle,
    "ch16/phasor-addition.svg": gen_ch16_phasor_addition,
    "ch16/wave-speed-string.svg": gen_ch16_wave_speed_string,
    "ch17/mach-cone.svg": gen_ch17_mach_cone,
}


@dataclass
class AngleError:
    file: str
    message: str


def validate_angle_metadata(rel: str) -> list[AngleError]:
    path = IMG / rel
    root = ET.parse(path).getroot()
    errors: list[AngleError] = []
    ns = "{http://www.w3.org/2000/svg}"
    for elem in root.iter():
        if not elem.tag.endswith("path"):
            continue
        if "data-angle-origin" not in elem.attrib:
            continue
        cx, cy = [float(v) for v in elem.attrib["data-angle-origin"].split(",")]
        r = float(elem.attrib["data-angle-radius"])
        start = float(elem.attrib["data-angle-start"])
        end = float(elem.attrib["data-angle-end"])
        want_s = pt((cx, cy), r, start)
        want_e = pt((cx, cy), r, end)
        nums = [float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", elem.attrib["d"])]
        if len(nums) < 9:
            errors.append(AngleError(rel, "angle path has too few numeric fields"))
            continue
        got_s = (nums[0], nums[1])
        got_e = (nums[-2], nums[-1])
        for name, got, want in [("start", got_s, want_s), ("end", got_e, want_e)]:
            if abs(got[0] - want[0]) > 0.11 or abs(got[1] - want[1]) > 0.11:
                errors.append(AngleError(rel, f"{name} point drifted: got {got}, want {want}"))
    return errors


def main() -> None:
    for rel, gen in GENERATORS.items():
        write(rel, gen())

    errors: list[AngleError] = []
    for rel in GENERATORS:
        ET.parse(IMG / rel)
        errors.extend(validate_angle_metadata(rel))

    if errors:
        for err in errors:
            print(f"{err.file}: {err.message}")
        raise SystemExit(1)

    print(f"regenerated {len(GENERATORS)} angle-controlled SVGs")


if __name__ == "__main__":
    main()
