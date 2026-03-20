import { test, expect } from '@playwright/test';
import {
  SIMULATIONS, simUrl, waitForSimReady,
  getCanvasSnapshot, setSlider,
} from './sim-helpers';

/**
 * Interactivity tests:
 * - Moving sliders changes the canvas rendering
 * - Play/start buttons trigger animation (canvas changes over time)
 * - Reset button restores initial state
 */

for (const sim of SIMULATIONS) {
  test.describe(`${sim} — interactivity`, () => {
    test('slider changes update canvas', async ({ page }) => {
      await page.goto(simUrl(sim));
      await waitForSimReady(page);

      const sliders = await page.locator('.controls input[type="range"]').all();
      if (sliders.length === 0) return;

      const before = await getCanvasSnapshot(page);

      // Change first slider to a different value
      const slider = sliders[0];
      const id = await slider.getAttribute('id');
      const min = parseFloat(await slider.getAttribute('min') || '0');
      const max = parseFloat(await slider.getAttribute('max') || '1');
      const mid = (min + max) / 2;
      const current = parseFloat(await slider.inputValue());

      // Move to a value different from current
      const newVal = Math.abs(current - min) > Math.abs(current - max)
        ? min : max;

      if (id) {
        await setSlider(page, `#${id}`, newVal);
      }

      const after = await getCanvasSnapshot(page);
      expect(after).not.toBe(before);
    });

    test('play button triggers animation', async ({ page }) => {
      await page.goto(simUrl(sim));
      await waitForSimReady(page);

      // Look for play/start button
      const playBtn = page.locator('.play-btn, .btn-primary').first();
      const isVisible = await playBtn.isVisible().catch(() => false);
      if (!isVisible) return;

      const before = await getCanvasSnapshot(page);
      await playBtn.click();
      // Wait for a few frames of animation
      await page.waitForTimeout(500);
      const after = await getCanvasSnapshot(page);

      // Canvas should change during animation
      // (some sims might not animate without specific params, use soft assertion)
      expect.soft(after, 'Canvas should change after play').not.toBe(before);
    });

    test('reset restores initial state', async ({ page }) => {
      await page.goto(simUrl(sim));
      await waitForSimReady(page);

      const initial = await getCanvasSnapshot(page);

      // Find and click play
      const playBtn = page.locator('.play-btn, .btn-primary').first();
      if (await playBtn.isVisible().catch(() => false)) {
        await playBtn.click();
        await page.waitForTimeout(300);
      }

      // Change a slider
      const sliders = await page.locator('.controls input[type="range"]').all();
      if (sliders.length > 0) {
        const id = await sliders[0].getAttribute('id');
        const max = parseFloat(await sliders[0].getAttribute('max') || '10');
        if (id) await setSlider(page, `#${id}`, max);
      }

      // Find and click reset
      const resetBtn = page.locator('.reset-btn, .btn-secondary').first();
      if (await resetBtn.isVisible().catch(() => false)) {
        await resetBtn.click();
        await page.waitForTimeout(200);
      }

      const afterReset = await getCanvasSnapshot(page);
      // After reset, canvas should be back to initial (or very close)
      // This is a soft check because some sims have stochastic elements
      expect.soft(afterReset).toBe(initial);
    });
  });
}
