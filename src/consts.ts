// Everything that appears on every page. Edit these first.

export const SITE = {
  name: 'Tejas Wadhwa',
  tagline: 'Computer Engineering, Purdue',
  description:
    'Computer Engineering student at Purdue building systems that cross the hardware–software line: real-time DSP on FPGAs, embedded firmware, PCB design, and the software on top.',

  email: 'tejaswadhwa@gmail.com',
  github: 'https://github.com/wadhwat',
  linkedin: 'https://www.linkedin.com/in/tejas-wadhwa/',
  // Swap for the real domain when you buy one; also change `site:` in astro.config.mjs.
  domain: 'https://wadhwat.github.io',

  gradDate: 'May 2028',
} as const;

export const NAV = [
  { href: '/projects/', label: 'Projects' },
  { href: '/about/', label: 'About' },
] as const;

// The vitals strip under the hero. Three real teams beats three broad fields.
export const AFFILIATIONS = [
  { label: 'RTL & FPGA', value: 'Audio DSP · Scoreboard' },
  { label: 'ASIC design', value: 'Digital FM receiver · STARS' },
  { label: 'Embedded systems', value: 'STM32 · Raspberry Pi · Sensors' },
] as const;

// Bump this whenever you touch the Currently building section.
export const CURRENT_UPDATED = 'September 2026';

// Order matters — this is the order categories appear on /projects.
export const CATEGORIES = [
  'RTL & FPGA',
  'Signal Processing',
  'Embedded & Firmware',
  'Hardware Design',
  'AI Systems',
] as const;
