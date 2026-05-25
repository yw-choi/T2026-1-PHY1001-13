"""
ChatGPT 이미지 생성 파이프라인.
지정된 SVG 파일들을 ChatGPT(gpt-image)에 업로드 → 다듬어진 PNG로 다운로드한다.

사전 준비:
    uv run python 01_login.py   # 최초 1회 로그인

사용법:
    uv run python 02_generate.py CH SVG [SVG ...]
        예: uv run python 02_generate.py ch12 \
              ../../website/public/img/ch12/ladder-fbd.svg

옵션:
    --headed/--headless    브라우저 표시 여부 (기본: headed, 디버깅용)
    --prompt-file PATH     프롬프트 텍스트 파일 (없으면 DEFAULT_PROMPT)
    --out DIR              출력 디렉토리 (기본: output/<CH>)
"""
from __future__ import annotations

import argparse
import functools
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

from playwright.sync_api import Page, TimeoutError as PlaywrightTimeout, sync_playwright

# stdout flush 즉시: 버퍼링 방지
print = functools.partial(print, flush=True)  # type: ignore[assignment]

PROFILE_DIR = Path.home() / ".cache" / "playwright-chatgpt-profile"
ROOT = Path(__file__).resolve().parent
TMP_PNG_DIR = ROOT / "tmp_png"

DEFAULT_PROMPT = """첨부한 이미지는 일반물리 강의 슬라이드용 다이어그램입니다.
이 다이어그램을 더 세련된 일러스트 스타일로 다시 그린 **이미지를 생성해 주세요**(image generation tool 사용).
설명/텍스트 답변 말고 반드시 이미지로 출력해주세요.

물리적 의미를 정확히 보존:
- 힘 벡터의 방향, 시작점, 작용선
- 각도, 길이 비율
- 모든 라벨 텍스트(한글/영문/수식, 첨자 포함)
- 화살촉(arrowhead)을 또렷하고 큼직하게

스타일:
- 색상: 빨강 #8B0029(주요 벡터·요소), 파랑 #2563EB(보조 벡터), 회색 #6B7280(보조선·치수선)
- 흰 배경, 단일 이미지
- 깨끗하고 현대적인 교과서 일러스트 톤
- 텍스트는 sans-serif, 굵고 또렷하게"""


def svg_to_png(svg: Path, out: Path, width: int = 1024) -> Path:
    """rsvg-convert / inkscape / sips 중 사용 가능한 도구로 SVG→PNG."""
    out.parent.mkdir(parents=True, exist_ok=True)
    if shutil.which("rsvg-convert"):
        subprocess.check_call(
            ["rsvg-convert", "-w", str(width), "-o", str(out), str(svg)]
        )
    elif shutil.which("inkscape"):
        subprocess.check_call(
            ["inkscape", str(svg), f"--export-filename={out}", f"--export-width={width}"]
        )
    elif shutil.which("magick"):
        subprocess.check_call(
            ["magick", "-density", "200", str(svg), "-resize", f"{width}x", str(out)]
        )
    else:
        # 최후 수단: sips는 svg 직접 미지원. 그냥 원본 SVG를 업로드.
        return svg
    return out


def upload_file(page: Page, file_path: Path) -> None:
    page.wait_for_selector('input[type="file"]', state="attached", timeout=20000)
    file_input = page.locator('input[type="file"]').first
    file_input.set_input_files(str(file_path))
    # 첨부 미리보기가 떠야 한다
    page.wait_for_timeout(1500)


def submit_prompt(page: Page, prompt: str) -> None:
    composer = page.locator('#prompt-textarea').first
    composer.click()
    composer.fill("")
    composer.type(prompt, delay=5)
    page.wait_for_timeout(500)
    # Send 버튼 클릭 (data-testid 기반)
    send = page.locator('button[data-testid="send-button"]').first
    send.click()


def _candidate_image_srcs(page: Page) -> list[str]:
    """alt='Generated image' 인 이미지 src를 새 → 오래된 순으로 반환. 중복 제거."""
    return page.evaluate(
        """() => {
            const skip = (s) => !s || s.startsWith('data:') || s.startsWith('blob:');
            const seen = new Set();
            const out = [];
            const imgs = [...document.querySelectorAll('img[alt="Generated image"]')];
            // DOM 순서대로면 마지막에 나온 게 가장 최신 → 역순으로 반환
            for (const img of imgs.reverse()) {
                if (skip(img.src) || seen.has(img.src)) continue;
                seen.add(img.src);
                out.push(img.src);
            }
            return out;
        }"""
    )


def wait_for_image(page: Page, timeout_ms: int = 300_000, stable_ms: int = 4000) -> str:
    """가장 최근 컨텐츠 이미지의 src가 stable_ms 동안 안 바뀌면 완료로 간주."""
    deadline = time.time() + timeout_ms / 1000
    last_src = ""
    last_seen_at = 0.0
    while time.time() < deadline:
        # lazy-load 트리거: 응답 영역까지 스크롤
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        srcs = _candidate_image_srcs(page)
        cur = srcs[0] if srcs else ""
        if cur and cur == last_src:
            if (time.time() - last_seen_at) * 1000 >= stable_ms:
                return cur
        else:
            if cur:
                print(f"[wait] 새 이미지 src 감지: {cur[:80]}...")
            last_src = cur
            last_seen_at = time.time()
        page.wait_for_timeout(1500)
    if last_src:
        print(f"[wait] timeout이지만 마지막 src 반환: {last_src[:80]}")
        return last_src
    raise TimeoutError("이미지 응답을 시간 내 받지 못함")


def download_image(page: Page, src: str, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    resp = page.context.request.get(src)
    if not resp.ok:
        raise RuntimeError(f"이미지 다운로드 실패: {resp.status} {src}")
    out.write_bytes(resp.body())


def safe_name(s: str) -> str:
    return re.sub(r"[^\w.-]+", "_", s)


def process_one(page: Page, svg: Path, out_dir: Path, prompt: str) -> Path:
    print(f"[gen] {svg.name} 처리 시작")
    # SVG → PNG 변환 (있으면)
    TMP_PNG_DIR.mkdir(exist_ok=True)
    upload_path = svg_to_png(svg, TMP_PNG_DIR / (svg.stem + ".png"))
    print(f"[gen] 업로드 파일: {upload_path}")

    # 새 채팅 열기
    page.goto("https://chatgpt.com/", wait_until="domcontentloaded")
    page.wait_for_selector("#prompt-textarea", timeout=20000)
    page.wait_for_timeout(1500)

    upload_file(page, upload_path)
    submit_prompt(page, prompt)
    print("[gen] 프롬프트 전송, 이미지 대기...")
    src = wait_for_image(page)
    print(f"[gen] 이미지 src 획득")

    out_path = out_dir / f"{svg.stem}.png"
    download_image(page, src, out_path)
    print(f"[gen] 저장: {out_path}")
    return out_path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("ch", help="챕터 식별자 (예: ch12)")
    ap.add_argument("svgs", nargs="+", type=Path, help="처리할 SVG 파일들")
    ap.add_argument("--headed", dest="headed", action="store_true", default=True)
    ap.add_argument("--headless", dest="headed", action="store_false")
    ap.add_argument("--prompt-file", type=Path)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()

    prompt = DEFAULT_PROMPT
    if args.prompt_file:
        prompt = args.prompt_file.read_text(encoding="utf-8")

    out_dir = args.out or (ROOT / "output" / args.ch)
    out_dir.mkdir(parents=True, exist_ok=True)

    if not PROFILE_DIR.exists():
        sys.exit(f"프로필 없음. 먼저 'uv run python 01_login.py' 실행. ({PROFILE_DIR})")

    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE_DIR),
            headless=not args.headed,
            viewport={"width": 1280, "height": 900},
            args=["--disable-blink-features=AutomationControlled"],
        )
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto("https://chatgpt.com/", wait_until="domcontentloaded")
        try:
            page.wait_for_selector("#prompt-textarea", timeout=15000)
        except PlaywrightTimeout:
            print("[gen] composer 미발견 — 로그인 안 됐거나 UI 변경. 01_login.py 재실행 필요.")
            ctx.close()
            sys.exit(2)

        results: list[tuple[Path, Path | None, str | None]] = []
        for svg in args.svgs:
            try:
                out = process_one(page, svg.resolve(), out_dir, prompt)
                results.append((svg, out, None))
            except Exception as e:
                results.append((svg, None, repr(e)))
                print(f"[gen] 실패: {svg.name} — {e}")

        ctx.close()

    print("\n=== 결과 ===")
    for svg, out, err in results:
        if err:
            print(f"  [FAIL] {svg.name}: {err}")
        else:
            print(f"  [ OK ] {svg.name} -> {out}")


if __name__ == "__main__":
    main()
