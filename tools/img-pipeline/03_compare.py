"""
원본 SVG와 ChatGPT 결과 PNG를 좌우로 나란히 보여주는 HTML 생성.

사용법:
    uv run python 03_compare.py CH
        예: uv run python 03_compare.py ch12
    원본은 ../../website/public/img/<CH>/*.svg, 결과는 output/<CH>/*.png 에서 매칭.
"""
import argparse
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SVG_BASE = ROOT.parent.parent / "website" / "public" / "img"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("ch")
    args = ap.parse_args()

    svg_dir = SVG_BASE / args.ch
    out_dir = ROOT / "output" / args.ch
    if not svg_dir.is_dir():
        raise SystemExit(f"원본 디렉토리 없음: {svg_dir}")
    if not out_dir.is_dir():
        raise SystemExit(f"결과 디렉토리 없음: {out_dir}")

    rows: list[str] = []
    for svg in sorted(svg_dir.glob("*.svg")):
        png = out_dir / f"{svg.stem}.png"
        before = svg.relative_to(ROOT.parent.parent)
        after = png.relative_to(ROOT) if png.exists() else None
        after_cell = (
            f'<img src="{html.escape(str(after))}">'
            if after
            else '<div class="missing">결과 없음</div>'
        )
        rows.append(
            f"""
        <tr>
          <td class="name">{html.escape(svg.stem)}</td>
          <td><img src="../../{html.escape(str(before))}"></td>
          <td>{after_cell}</td>
        </tr>"""
        )

    html_doc = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>Diagram Comparison — {html.escape(args.ch)}</title>
<style>
  body {{ font-family: -apple-system, sans-serif; margin: 24px; background: #fafafa; color: #1a1a1a; }}
  h1 {{ color: #8B0029; margin-bottom: 4px; }}
  .meta {{ color: #6B7280; margin-bottom: 24px; }}
  table {{ width: 100%; border-collapse: collapse; background: white; box-shadow: 0 1px 3px rgba(0,0,0,.06); }}
  th, td {{ padding: 12px; border-bottom: 1px solid #e5e7eb; vertical-align: top; }}
  th {{ background: #8B0029; color: white; text-align: left; font-weight: 500; }}
  td.name {{ font-weight: 600; width: 180px; color: #8B0029; }}
  td img {{ max-width: 100%; max-height: 420px; border: 1px solid #e5e7eb; background: white; }}
  .missing {{ color: #9ca3af; font-style: italic; padding: 40px; text-align: center; border: 1px dashed #d1d5db; }}
  th.col {{ width: 40%; }}
</style>
</head>
<body>
<h1>다이어그램 비교 — {html.escape(args.ch)}</h1>
<div class="meta">왼쪽: 원본 SVG · 오른쪽: ChatGPT 이미지 생성 결과</div>
<table>
  <thead>
    <tr><th>이름</th><th class="col">Before (SVG)</th><th class="col">After (PNG)</th></tr>
  </thead>
  <tbody>{''.join(rows)}
  </tbody>
</table>
</body>
</html>"""

    out = ROOT / f"compare_{args.ch}.html"
    out.write_text(html_doc, encoding="utf-8")
    print(f"[compare] 작성: {out}")
    print(f"[compare] 열기:  open {out}")


if __name__ == "__main__":
    main()
