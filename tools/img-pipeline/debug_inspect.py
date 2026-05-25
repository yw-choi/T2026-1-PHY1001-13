"""
이전 ChatGPT 채팅에서 모든 이미지 후보를 검사한다.
가장 최근 채팅을 자동으로 열고, 페이지 내 모든 <img>의 src/크기/위치를 덤프.
가장 큰 컨텐츠 이미지를 골라 다운로드.
"""
from __future__ import annotations

import functools
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

print = functools.partial(print, flush=True)
PROFILE_DIR = Path.home() / ".cache" / "playwright-chatgpt-profile"
ROOT = Path(__file__).resolve().parent


def main() -> None:
    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE_DIR),
            headless=False,
            viewport={"width": 1280, "height": 900},
            args=["--disable-blink-features=AutomationControlled"],
        )
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto("https://chatgpt.com/", wait_until="domcontentloaded")
        page.wait_for_timeout(2500)

        # 사이드바에서 가장 최근 채팅 URL 추출 후 직접 navigate
        first_chat = page.locator('a[href^="/c/"]').first
        if first_chat.count():
            href = first_chat.get_attribute("href")
            print(f"[debug] 최근 채팅: https://chatgpt.com{href}")
            page.goto(f"https://chatgpt.com{href}", wait_until="domcontentloaded")
            page.wait_for_timeout(3500)
        else:
            print("[debug] 사이드바에서 채팅 못 찾음")
            ctx.close()
            return

        # 모든 이미지 정보 덤프
        info = page.evaluate(
            """() => {
                return [...document.querySelectorAll('img')].map((img, i) => {
                    const r = img.getBoundingClientRect();
                    return {
                        idx: i,
                        src: img.src,
                        natW: img.naturalWidth,
                        natH: img.naturalHeight,
                        rectW: Math.round(r.width),
                        rectH: Math.round(r.height),
                        alt: img.alt || '',
                        parentTag: img.parentElement?.tagName,
                        inMessage: !!img.closest('[data-message-author-role]'),
                        role: img.closest('[data-message-author-role]')?.getAttribute('data-message-author-role') || '',
                    };
                });
            }"""
        )
        print(f"[debug] 총 이미지 {len(info)}개")
        for x in info:
            print(
                f"  [{x['idx']:>2}] role={x['role']:>9} nat={x['natW']}x{x['natH']} "
                f"rect={x['rectW']}x{x['rectH']} parent={x['parentTag']} "
                f"alt={x['alt'][:30]!r}"
            )
            print(f"        src={x['src'][:120]}")

        # 클릭하면 더 큰 버전이 뜨는지 시도: 가장 큰 assistant 이미지 클릭
        biggest = sorted(
            [x for x in info if x.get("role") == "assistant" and x["natW"] >= 200],
            key=lambda x: x["natW"] * x["natH"],
            reverse=True,
        )
        if biggest:
            target = biggest[0]
            print(f"[debug] 클릭 시도: idx={target['idx']} {target['natW']}x{target['natH']}")
            page.locator("img").nth(target["idx"]).click()
            page.wait_for_timeout(2500)

            # 모달/오버레이의 이미지 확인
            modal_info = page.evaluate(
                """() => {
                    const overlays = [...document.querySelectorAll('[role="dialog"], .modal, [data-state="open"]')];
                    const out = [];
                    for (const ov of overlays) {
                        for (const img of ov.querySelectorAll('img')) {
                            out.push({
                                src: img.src,
                                natW: img.naturalWidth, natH: img.naturalHeight,
                            });
                        }
                    }
                    return out;
                }"""
            )
            print(f"[debug] 모달 이미지 {len(modal_info)}개")
            for x in modal_info:
                print(f"   modal nat={x['natW']}x{x['natH']} src={x['src'][:120]}")

            # 다운로드 버튼이 있으면 누르기 시도
            dl = page.locator('button[aria-label*="ownload"], a[download]').first
            if dl.count():
                with page.expect_download(timeout=15000) as dl_info:
                    dl.click()
                d = dl_info.value
                save = ROOT / f"output/ch12/ladder-fbd_via_download.{d.suggested_filename.split('.')[-1]}"
                save.parent.mkdir(parents=True, exist_ok=True)
                d.save_as(str(save))
                print(f"[debug] 다운로드 완료: {save}")
            else:
                print("[debug] 다운로드 버튼 못 찾음")

        # 백그라운드 실행 호환: 입력 대신 자동 종료
        page.wait_for_timeout(3000)
        ctx.close()


if __name__ == "__main__":
    main()
