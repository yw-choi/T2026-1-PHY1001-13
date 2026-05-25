"""특정 ChatGPT 채팅 URL에서 alt='Generated image' 이미지를 다운로드."""
from __future__ import annotations

import functools
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

print = functools.partial(print, flush=True)
PROFILE_DIR = Path.home() / ".cache" / "playwright-chatgpt-profile"


def main() -> None:
    if len(sys.argv) < 3:
        sys.exit("사용법: download_existing.py CHAT_URL OUT_PATH")
    chat_url = sys.argv[1]
    out_path = Path(sys.argv[2])
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE_DIR),
            headless=False,
            viewport={"width": 1280, "height": 900},
            args=["--disable-blink-features=AutomationControlled"],
        )
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto(chat_url, wait_until="domcontentloaded")
        # 채팅 컨텐츠 로드 대기
        for _ in range(20):
            page.wait_for_timeout(1000)
            n = page.evaluate("() => document.querySelectorAll('img').length")
            print(f"  [dl] img count = {n}")
            if n >= 6:
                break

        # 페이지 끝까지 스크롤 (lazy load 트리거)
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(2500)

        all_imgs = page.evaluate(
            """() => [...document.querySelectorAll('img')].map(i => ({
                alt: i.alt, natW: i.naturalWidth, natH: i.naturalHeight,
                src: i.src
            }))"""
        )
        print(f"[dl] 전체 img {len(all_imgs)}개")
        for i, x in enumerate(all_imgs):
            print(f"  [{i}] alt={x['alt']!r:20} {x['natW']}x{x['natH']}  src={x['src'][:80]}")

        srcs = [x["src"] for x in all_imgs if x.get("alt") == "Generated image"]
        print(f"[dl] Generated image 후보 {len(srcs)}개")

        if not srcs:
            ctx.close()
            sys.exit("생성된 이미지 없음")

        # 가장 최근(마지막 DOM)
        target = srcs[-1]
        resp = page.context.request.get(target)
        if not resp.ok:
            sys.exit(f"다운로드 실패: {resp.status}")
        out_path.write_bytes(resp.body())
        print(f"[dl] 저장: {out_path} ({len(resp.body())} bytes)")
        ctx.close()


if __name__ == "__main__":
    main()
