import { Page, expect } from '@playwright/test';

/** All new simulation filenames (no legacy) */
export const SIMULATIONS = [
  'angular-momentum',
  'atwood-machine',
  'centripetal-force',
  'circular-motion',
  'collision-1d',
  'collision-2d',
  'dot-cross-product',
  'energy-conservation',
  'free-fall',
  'incline-friction',
  'kinematics-graphs',
  'ladder-equilibrium',
  'moment-of-inertia',
  'newton2nd',
  'potential-energy-curve',
  'projectile-motion',
  'relative-motion-2d',
  'rolling-race',
  'rotation-kinematics',
  'scale-explorer',
  'spring-work',
  'stress-strain',
  'vector-addition',
  'work-energy',
];

export function simUrl(name: string) {
  return `http://localhost:4173/${name}.html`;
}

/**
 * Wait for the simulation to fully load:
 * - DOM ready
 * - Canvas rendered (non-zero size)
 * - KaTeX loaded (if present)
 */
export async function waitForSimReady(page: Page) {
  await page.waitForLoadState('domcontentloaded');
  // Wait for canvas to be present and sized
  await page.waitForFunction(() => {
    const c = document.querySelector('canvas');
    return c && c.width > 0 && c.height > 0;
  }, {}, { timeout: 8000 });
  // Wait for KaTeX to finish rendering (at least one .katex element)
  await page.waitForFunction(() => {
    return document.querySelectorAll('.katex').length > 0;
  }, {}, { timeout: 5000 }).catch(() => {
    // Some sims might not have visible KaTeX initially
  });
}

/** Rect type for overlap detection */
export interface Rect {
  x: number;
  y: number;
  width: number;
  height: number;
  label: string;
}

/**
 * Get bounding boxes of all visible KaTeX overlay labels.
 * Returns an array of { x, y, width, height, label } rects.
 */
export async function getOverlayLabelRects(page: Page): Promise<Rect[]> {
  return page.evaluate(() => {
    const labels = document.querySelectorAll('.canvas-overlay .katex-label, .canvas-overlay .graph-title');
    const rects: { x: number; y: number; width: number; height: number; label: string }[] = [];
    labels.forEach(el => {
      const htmlEl = el as HTMLElement;
      if (htmlEl.style.display === 'none' || htmlEl.offsetWidth === 0) return;
      const r = htmlEl.getBoundingClientRect();
      if (r.width > 0 && r.height > 0) {
        rects.push({ x: r.x, y: r.y, width: r.width, height: r.height, label: htmlEl.id || htmlEl.textContent?.slice(0, 30) || '' });
      }
    });
    return rects;
  });
}

/**
 * Get bounding boxes of all visible interactive controls (sliders, buttons, selects)
 * and info panels.
 */
export async function getControlRects(page: Page): Promise<Rect[]> {
  return page.evaluate(() => {
    const selectors = '.controls input[type="range"], .controls button, .controls select, .info-box, .theorem-box, .formula-box';
    const elems = document.querySelectorAll(selectors);
    const rects: { x: number; y: number; width: number; height: number; label: string }[] = [];
    elems.forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.width > 0 && r.height > 0) {
        rects.push({ x: r.x, y: r.y, width: r.width, height: r.height, label: (el as HTMLElement).id || el.tagName });
      }
    });
    return rects;
  });
}

/** Check if two rects overlap (with a tolerance margin) */
export function rectsOverlap(a: Rect, b: Rect, margin = 0): boolean {
  return !(
    a.x + a.width + margin <= b.x ||
    b.x + b.width + margin <= a.x ||
    a.y + a.height + margin <= b.y ||
    b.y + b.height + margin <= a.y
  );
}

/** Find all overlapping pairs among a set of rects */
export function findOverlaps(rects: Rect[], margin = 0): [Rect, Rect][] {
  const overlaps: [Rect, Rect][] = [];
  for (let i = 0; i < rects.length; i++) {
    for (let j = i + 1; j < rects.length; j++) {
      if (rectsOverlap(rects[i], rects[j], margin)) {
        overlaps.push([rects[i], rects[j]]);
      }
    }
  }
  return overlaps;
}

/**
 * Get a canvas pixel snapshot for change detection.
 * Returns base64 data URL of the canvas.
 */
export async function getCanvasSnapshot(page: Page): Promise<string> {
  return page.evaluate(() => {
    const c = document.querySelector('canvas') as HTMLCanvasElement;
    return c ? c.toDataURL('image/png') : '';
  });
}

/**
 * Move a slider to a new value and wait for redraw.
 */
export async function setSlider(page: Page, selector: string, value: number) {
  await page.evaluate(({ sel, val }) => {
    const slider = document.querySelector(sel) as HTMLInputElement;
    if (!slider) return;
    slider.value = String(val);
    slider.dispatchEvent(new Event('input', { bubbles: true }));
    slider.dispatchEvent(new Event('change', { bubbles: true }));
  }, { sel: selector, val: value });
  // Brief wait for requestAnimationFrame to process
  await page.waitForTimeout(100);
}

/** Collect JS console errors during page load */
export function collectConsoleErrors(page: Page): string[] {
  const errors: string[] = [];
  page.on('console', msg => {
    if (msg.type() === 'error') errors.push(msg.text());
  });
  page.on('pageerror', err => {
    errors.push(err.message);
  });
  return errors;
}
