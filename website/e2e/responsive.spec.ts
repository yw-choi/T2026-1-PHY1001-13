import { test, expect } from '@playwright/test';
import { SIMULATIONS, simUrl, waitForSimReady, collectConsoleErrors } from './sim-helpers';

/**
 * Responsive layout tests:
 * - Mobile viewport (375x667): vertical layout, no horizontal overflow
 * - Tablet viewport (768x1024): layout adapts
 * - Canvas and controls both visible at each size
 */

const MOBILE = { width: 375, height: 667 };
const TABLET = { width: 768, height: 1024 };

for (const sim of SIMULATIONS) {
  test.describe(`${sim} — responsive`, () => {
    test('mobile layout: vertical stack, no overflow', async ({ browser }) => {
      const context = await browser.newContext({ viewport: MOBILE });
      const page = await context.newPage();
      const errors = collectConsoleErrors(page);

      await page.goto(simUrl(sim));
      await waitForSimReady(page);

      // No JS errors
      expect(errors).toEqual([]);

      // Container should be column direction
      const layout = await page.evaluate(() => {
        const container = document.querySelector('.container') as HTMLElement;
        const style = getComputedStyle(container);
        return {
          flexDir: style.flexDirection,
          bodyScrollWidth: document.body.scrollWidth,
          viewportWidth: window.innerWidth,
        };
      });
      expect(layout.flexDir).toBe('column');
      // No horizontal overflow
      expect(layout.bodyScrollWidth).toBeLessThanOrEqual(layout.viewportWidth + 1);

      // Both canvas and controls visible
      await expect(page.locator('canvas')).toBeVisible();
      await expect(page.locator('.controls')).toBeVisible();

      await context.close();
    });

    test('tablet layout: no JS errors, canvas visible', async ({ browser }) => {
      const context = await browser.newContext({ viewport: TABLET });
      const page = await context.newPage();
      const errors = collectConsoleErrors(page);

      await page.goto(simUrl(sim));
      await waitForSimReady(page);

      expect(errors).toEqual([]);
      await expect(page.locator('canvas')).toBeVisible();
      await expect(page.locator('.controls')).toBeVisible();

      await context.close();
    });
  });
}
