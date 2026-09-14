// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  // The one URL the build needs. Used for canonical links, the sitemap,
  // and OG image URLs. Before you own the domain, use the github.io one:
  //   site: 'https://wadhwat.github.io',
  // After you point the domain at Pages, switch it here and nothing else changes.
  site: 'https://wadhwat.github.io',
  integrations: [sitemap()],
  markdown: {
    shikiConfig: { theme: 'github-light', wrap: true },
  },
});
