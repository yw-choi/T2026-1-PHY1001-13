#!/usr/bin/env node
/**
 * Generate PDF files from print-friendly lecture pages.
 *
 * Usage: node scripts/generate-pdfs.mjs
 *
 * Prerequisites:
 *   - `npm run build` must have been run first
 *   - Playwright browsers installed (`npx playwright install chromium`)
 */

import { chromium } from '@playwright/test';
import { execSync, spawn } from 'child_process';
import { existsSync, mkdirSync, readdirSync } from 'fs';
import { join, resolve } from 'path';

const ROOT = resolve(import.meta.dirname, '..');
const DIST = join(ROOT, 'dist');
const OUT_DIR = join(ROOT, 'public', 'pdf');

if (!existsSync(DIST)) {
  console.error('Error: dist/ not found. Run `npm run build` first.');
  process.exit(1);
}

// Find all lecture IDs from the build output
const lecturesDir = join(DIST, 'lectures');
if (!existsSync(lecturesDir)) {
  console.error('Error: dist/lectures/ not found.');
  process.exit(1);
}

const lectureIds = readdirSync(lecturesDir, { withFileTypes: true })
  .filter((d) => d.isDirectory())
  .map((d) => d.name)
  .sort();

if (lectureIds.length === 0) {
  console.log('No lectures found.');
  process.exit(0);
}

mkdirSync(OUT_DIR, { recursive: true });

// Start Astro preview server (handles base path correctly)
const PORT = 4173;

console.log('Starting preview server...');
const server = spawn('npx', ['astro', 'preview', '--port', String(PORT)], {
  cwd: ROOT,
  stdio: ['ignore', 'pipe', 'pipe'],
});

// Wait for server to be ready
await new Promise((resolve) => {
  const onData = (data) => {
    const text = data.toString();
    if (text.includes('localhost') || text.includes('Local')) {
      server.stdout.off('data', onData);
      resolve();
    }
  };
  server.stdout.on('data', onData);
  // Fallback timeout
  setTimeout(resolve, 5000);
});

console.log(`Server running on port ${PORT}`);
console.log(`Found ${lectureIds.length} lectures: ${lectureIds.join(', ')}`);

const browser = await chromium.launch();
const context = await browser.newContext();

for (const id of lectureIds) {
  const printDir = join(DIST, 'lectures', id, 'print');
  if (!existsSync(printDir)) {
    console.log(`  Skipping ${id} (no print page)`);
    continue;
  }

  const url = `http://localhost:${PORT}/PHY1001/lectures/${id}/print/`;
  const outPath = join(OUT_DIR, `${id}.pdf`);

  console.log(`  Generating ${id}...`);

  const page = await context.newPage();
  await page.goto(url, { waitUntil: 'networkidle' });

  // Wait for all web fonts (KaTeX + Noto Sans KR) to load
  await page.waitForFunction(() => document.fonts.ready.then(() => true), { timeout: 10000 }).catch(() => {});
  await page.waitForTimeout(500);

  await page.pdf({
    path: outPath,
    format: 'A4',
    printBackground: true,
    margin: { top: '12mm', bottom: '12mm', left: '16mm', right: '16mm' },
  });

  await page.close();
  console.log(`    → ${outPath}`);
}

await browser.close();
server.kill();

console.log(`\nDone! PDFs saved to ${OUT_DIR}`);
