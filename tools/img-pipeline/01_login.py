"""
ChatGPT 최초 로그인 + 세션 저장.
실행하면 보이는 브라우저가 뜨고 chatgpt.com으로 간다. 사용자가 로그인하면
프로필이 ~/.cache/playwright-chatgpt-profile 에 영속화되어
이후 02_generate.py 가 같은 세션을 재사용한다.

사용법:
    uv run python 01_login.py
로그인 후 브라우저 창을 직접 닫으면 종료.
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

PROFILE_DIR = Path.home() / ".cache" / "playwright-chatgpt-profile"
PROFILE_DIR.mkdir(parents=True, exist_ok=True)


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
        print(f"[login] profile={PROFILE_DIR}")
        print("[login] 브라우저에서 로그인 후 창을 닫으세요.")
        # 사용자가 창을 닫을 때까지 대기
        try:
            page.wait_for_event("close", timeout=0)
        except Exception:
            pass
        ctx.close()


if __name__ == "__main__":
    main()
