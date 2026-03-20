import { test, expect } from '@playwright/test';
import {
  SIMULATIONS, simUrl, waitForSimReady,
  getOverlayLabelRects, getControlRects, findOverlaps, setSlider,
} from './sim-helpers';

/**
 * Overlap detection tests:
 * - KaTeX overlay labels should not overlap each other at default state
 * - After slider interactions, labels should not overlap
 * - Controls should not overflow or overlap each other
 */

for (const sim of SIMULATIONS) {
  test.describe(`${sim} — overlap`, () => {
    test('overlay labels do not overlap at default state', async ({ page }) => {
      await page.goto(simUrl(sim));
      await waitForSimReady(page);

      const rects = await getOverlayLabelRects(page);
      if (rects.length < 2) return; // nothing to check

      const overlaps = findOverlaps(rects);
      if (overlaps.length > 0) {
        const desc = overlaps.map(([a, b]) =>
          `"${a.label}" ↔ "${b.label}"`
        ).join(', ');
        expect.soft(overlaps.length, `Overlay labels overlap: ${desc}`).toBe(0);
      }
    });

    test('overlay labels do not overlap after slider extremes', async ({ page }) => {
      await page.goto(simUrl(sim));
      await waitForSimReady(page);

      // Find all sliders
      const sliders = await page.locator('.controls input[type="range"]').all();
      if (sliders.length === 0) return;

      // Test each slider at min, then max
      for (const slider of sliders) {
        const id = await slider.getAttribute('id');
        const min = await slider.getAttribute('min');
        const max = await slider.getAttribute('max');

        if (id && min) {
          await setSlider(page, `#${id}`, parseFloat(min));
          const rectsMin = await getOverlayLabelRects(page);
          const overlapsMin = findOverlaps(rectsMin);
          if (overlapsMin.length > 0) {
            const desc = overlapsMin.map(([a, b]) =>
              `"${a.label}" ↔ "${b.label}"`
            ).join(', ');
            expect.soft(overlapsMin.length,
              `Overlap at ${id}=min(${min}): ${desc}`
            ).toBe(0);
          }
        }

        if (id && max) {
          await setSlider(page, `#${id}`, parseFloat(max));
          const rectsMax = await getOverlayLabelRects(page);
          const overlapsMax = findOverlaps(rectsMax);
          if (overlapsMax.length > 0) {
            const desc = overlapsMax.map(([a, b]) =>
              `"${a.label}" ↔ "${b.label}"`
            ).join(', ');
            expect.soft(overlapsMax.length,
              `Overlap at ${id}=max(${max}): ${desc}`
            ).toBe(0);
          }
        }
      }
    });

    test('control elements do not overflow viewport', async ({ page }) => {
      await page.goto(simUrl(sim));
      await waitForSimReady(page);

      const viewport = page.viewportSize()!;
      const rects = await getControlRects(page);

      for (const rect of rects) {
        expect.soft(
          rect.x + rect.width <= viewport.width + 2,
          `Control "${rect.label}" overflows right edge`
        ).toBe(true);
        expect.soft(
          rect.y + rect.height <= viewport.height + 2,
          `Control "${rect.label}" overflows bottom edge`
        ).toBe(true);
      }
    });
  });
}
