// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  site: 'https://yw-choi.github.io',
  base: '/PHY1001/',
  devToolbar: { enabled: false },
  vite: {
    plugins: [tailwindcss()],
  },
});
