import { test, expect } from '@playwright/test';
import { SIMULATIONS, simUrl, waitForSimReady, collectConsoleErrors } from './sim-helpers';

/**
 * Basic rendering tests for every simulation:
 * - No JS errors on load
 * - Canvas exists and has non-zero dimensions
 * - KaTeX CSS loaded (stylesheet present)
 * - At least one KaTeX-rendered element exists
 * - Controls panel is visible
 */

for (const sim of SIMULATIONS) {
  test.describe(sim, () => {
    test('loads without JS errors', async ({ page }) => {
      const errors = collectConsoleErrors(page);
      await page.goto(simUrl(sim));
      await waitForSimReady(page);
      expect(errors).toEqual([]);
    });

    test('canvas renders with non-zero size', async ({ page }) => {
      await page.goto(simUrl(sim));
      await waitForSimReady(page);
      const canvasInfo = await page.evaluate(() => {
        const c = document.querySelector('canvas') as HTMLCanvasElement;
        return c ? { width: c.width, height: c.height, clientW: c.clientWidth, clientH: c.clientHeight } : null;
      });
      expect(canvasInfo).not.toBeNull();
      expect(canvasInfo!.width).toBeGreaterThan(0);
      expect(canvasInfo!.height).toBeGreaterThan(0);
      expect(canvasInfo!.clientW).toBeGreaterThan(0);
      expect(canvasInfo!.clientH).toBeGreaterThan(0);
    });

    test('KaTeX is loaded and renders formulas', async ({ page }) => {
      await page.goto(simUrl(sim));
      await waitForSimReady(page);
      // KaTeX CSS should be loaded
      const hasKatexCSS = await page.evaluate(() => {
        return Array.from(document.styleSheets).some(s =>
          s.href?.includes('katex')
        );
      });
      expect(hasKatexCSS).toBe(true);

      // At least one .katex element should exist
      const katexCount = await page.locator('.katex').count();
      expect(katexCount).toBeGreaterThan(0);
    });

    test('controls panel is visible', async ({ page }) => {
      await page.goto(simUrl(sim));
      await waitForSimReady(page);
      const controls = page.locator('.controls');
      await expect(controls).toBeVisible();
    });
  });
}
