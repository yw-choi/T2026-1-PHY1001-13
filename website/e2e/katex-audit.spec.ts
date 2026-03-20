import { test, expect } from '@playwright/test';
import { SIMULATIONS, simUrl, waitForSimReady } from './sim-helpers';

/**
 * KaTeX audit: detect plain-text math on canvas that should be KaTeX.
 *
 * Strategy: Intercept ctx.fillText calls and flag any that contain
 * mathematical subscripts (₁₂₃), superscripts, Greek letters,
 * or formula patterns (=, /, ×) that should be rendered with KaTeX.
 */

// Patterns that indicate math content that should be KaTeX-rendered
const MATH_PATTERNS = [
  /[₀₁₂₃₄₅₆₇₈₉ₐₑᵢₒᵤ]/,  // Unicode subscripts
  /[⁰¹²³⁴⁵⁶⁷⁸⁹]/,          // Unicode superscripts
  /[αβγδεζηθκλμνξπρστφχψω]/, // Greek lowercase
  /[ΓΔΘΛΞΠΣΦΨΩ]/,            // Greek uppercase
  /\bkg·m\/s\b/,             // Unit with middle dot
  /\bN·m\b/,                 // Torque unit
  /\b[A-Za-z]_[A-Za-z0-9]/,  // Subscript notation like K_i, v_1
  /Δ[A-Z]/,                   // Delta notation
  /→/,                         // Arrow (vector)
];

// Whitelist: patterns that are OK as plain canvas text
const PLAIN_TEXT_OK = [
  /^\d+(\.\d+)?$/,            // Pure numbers
  /^[+-]?\d+(\.\d+)?\s*(m|s|kg|N|J|W|Pa|MPa|GPa|Hz|rad|°)?\s*$/,  // Number + unit
  /^[xyvtaFm]$/,              // Single variable letter
  /^0$/,                       // Zero
  /^(x|v|a|F|U|K|E|W|p|L|I|τ|ω|α|θ|T|N|f)$/,  // Single physics symbol
];

for (const sim of SIMULATIONS) {
  test(`${sim} — audit canvas text for unconverted math`, async ({ page }) => {
    // Inject a hook before page loads to capture ctx.fillText calls
    await page.addInitScript(() => {
      (window as any).__canvasTextCalls = [];
      const origGetContext = HTMLCanvasElement.prototype.getContext;
      HTMLCanvasElement.prototype.getContext = function (...args: any[]) {
        const ctx = origGetContext.apply(this, args as any);
        if (ctx && args[0] === '2d') {
          const origFillText = ctx.fillText.bind(ctx);
          ctx.fillText = function (text: string, x: number, y: number, maxWidth?: number) {
            (window as any).__canvasTextCalls.push({
              text: String(text),
              x, y,
              font: ctx.font,
            });
            return origFillText(text, x, y, maxWidth);
          };
        }
        return ctx;
      };
    });

    await page.goto(simUrl(sim));
    await waitForSimReady(page);
    // Trigger a redraw
    await page.waitForTimeout(200);

    const calls: { text: string; x: number; y: number; font: string }[] =
      await page.evaluate(() => (window as any).__canvasTextCalls || []);

    const suspiciousTexts: string[] = [];

    for (const call of calls) {
      const text = call.text.trim();
      if (!text) continue;

      // Skip if it's pure whitelist
      if (PLAIN_TEXT_OK.some(p => p.test(text))) continue;

      // Flag if it matches math patterns
      for (const pattern of MATH_PATTERNS) {
        if (pattern.test(text)) {
          suspiciousTexts.push(text);
          break;
        }
      }
    }

    // Report findings (soft assertion — this is an audit, not a blocker)
    if (suspiciousTexts.length > 0) {
      const unique = [...new Set(suspiciousTexts)];
      console.log(`[${sim}] Plain-text math on canvas (${unique.length}):`, unique.join(' | '));
      // Soft fail — these should eventually be converted to KaTeX overlays
      expect.soft(unique.length,
        `Found ${unique.length} plain-text math strings on canvas: ${unique.join(', ')}`
      ).toBe(0);
    }
  });
}
