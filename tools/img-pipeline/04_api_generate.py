"""
OpenAI gpt-image-2 (Image 2.0) 직접 호출로 SVG 다이어그램 리디자인.
환경변수 OPENAI_API_KEY 필요.

사용법:
    OPENAI_API_KEY=... uv run python 04_api_generate.py CH SVG [SVG ...]
        예: OPENAI_API_KEY=... uv run python 04_api_generate.py ch12 \\
              ../../website/public/img/ch12/ladder-fbd.svg

옵션:
    --model NAME           기본 gpt-image-2
    --size W x H           기본 1024x1024 (정사각). 1536x1024, 1024x1536도 가능
    --quality high|medium|low  기본 high
    --out DIR              기본 output_api/<CH>
"""
from __future__ import annotations

import argparse
import base64
import functools
import os
import shutil
import subprocess
import sys
from pathlib import Path

from openai import OpenAI

print = functools.partial(print, flush=True)
ROOT = Path(__file__).resolve().parent
TMP_PNG_DIR = ROOT / "tmp_png_api"

DEFAULT_PROMPT = """첨부 이미지는 일반물리(역학) 강의 슬라이드용 자유물체도/다이어그램이다.
원본의 물리적 의미를 정확히 보존하면서 더 세련된 일러스트 스타일로 다시 그려라.

엄격히 보존할 것:
- 모든 힘 벡터의 방향, 작용점, 작용선
- 각도(예: θ), 길이 비율, 치수선
- 모든 라벨 텍스트(한글/영문/수식, 첨자 포함). 예: F_w, F_L, F_R, σ, ε, σ_y, ε_u 등
- 화살촉(arrowhead)은 또렷하고 큼직하게 그릴 것
- 그래프(예: 응력-변형 곡선)는 곡선 자체를 반드시 그릴 것

스타일:
- 색상 팔레트: 빨강 #8B0029(주요 벡터/요소), 파랑 #2563EB(보조 벡터), 회색 #6B7280(보조선/치수선)
- 흰 배경, 단일 정적 이미지
- sans-serif, 깔끔한 교과서 톤
"""


def svg_to_png(svg: Path, out: Path, width: int = 1536) -> Path:
    out.parent.mkdir(parents=True, exist_ok=True)
    if shutil.which("magick"):
        subprocess.check_call(
            ["magick", "-density", "200", "-background", "white",
             str(svg), "-resize", f"{width}x", str(out)]
        )
    elif shutil.which("rsvg-convert"):
        subprocess.check_call(
            ["rsvg-convert", "-w", str(width), "-b", "white", "-o", str(out), str(svg)]
        )
    else:
        return svg
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("ch")
    ap.add_argument("svgs", nargs="+", type=Path)
    ap.add_argument("--model", default="gpt-image-2")
    ap.add_argument("--size", default="1024x1024")
    ap.add_argument("--quality", default="high", choices=["high", "medium", "low", "auto"])
    ap.add_argument("--prompt-file", type=Path)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()

    if not os.environ.get("OPENAI_API_KEY"):
        sys.exit("OPENAI_API_KEY 환경변수 미설정")

    prompt = args.prompt_file.read_text(encoding="utf-8") if args.prompt_file else DEFAULT_PROMPT
    out_dir = args.out or (ROOT / "output_api" / args.ch)
    out_dir.mkdir(parents=True, exist_ok=True)

    client = OpenAI()

    results: list[tuple[Path, Path | None, str | None]] = []
    for svg in args.svgs:
        svg = svg.resolve()
        print(f"[api] {svg.name} 처리 시작")
        png_in = svg_to_png(svg, TMP_PNG_DIR / (svg.stem + ".png"))
        print(f"[api] 입력 PNG: {png_in}")

        try:
            with open(png_in, "rb") as f:
                resp = client.images.edit(
                    model=args.model,
                    image=f,
                    prompt=prompt,
                    size=args.size,
                    quality=args.quality,
                    n=1,
                )
            datum = resp.data[0]
            png_bytes: bytes
            if getattr(datum, "b64_json", None):
                png_bytes = base64.b64decode(datum.b64_json)
            elif getattr(datum, "url", None):
                # url 방식은 별도 fetch 필요
                import urllib.request
                with urllib.request.urlopen(datum.url) as r:
                    png_bytes = r.read()
            else:
                raise RuntimeError("응답에 b64_json/url 둘 다 없음")

            out_path = out_dir / f"{svg.stem}.png"
            out_path.write_bytes(png_bytes)
            print(f"[api] 저장: {out_path} ({len(png_bytes)} bytes)")
            results.append((svg, out_path, None))
        except Exception as e:
            print(f"[api] 실패: {svg.name} — {e}")
            results.append((svg, None, repr(e)))

    print("\n=== 결과 ===")
    for svg, out, err in results:
        if err:
            print(f"  [FAIL] {svg.name}: {err}")
        else:
            print(f"  [ OK ] {svg.name} -> {out}")


if __name__ == "__main__":
    main()
