import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

/**
 * One markdown file per project in src/content/projects/.
 * The schema is strict on purpose: a missing required field fails the
 * build rather than quietly shipping a half-written page.
 */
const projects = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/projects' }),
  schema: z.object({
    title: z.string(),
    /** One sentence. Shows on the index and under the title. */
    hook: z.string(),

    /**
     * Which homepage section this belongs to.
     *   selected — finished work, full case study, figure + stat strip
     *   current  — in progress, one line in Currently building
     *   also     — smaller finished work, compact row
     */
    tier: z.enum(['selected', 'current', 'also']),

    status: z.enum(['shipped', 'in-progress']),
    /** Lower sorts first within its tier. */
    order: z.number().default(50),

    /** Shown in the left column of current/compact rows, e.g. "SoCET" or "Hackathon". */
    where: z.string().optional(),

    categories: z.array(z.string()).min(1),
    dates: z.string(),

    /** What YOU did, specifically. Not optional; it is the test most student sites fail. */
    role: z.string(),

    /** Path under public/, e.g. "/figures/harmonicore-pitch.png". Omitted renders a labelled placeholder. */
    figure: z.string().optional(),
    figureAlt: z.string().optional(),
    /** Text shown in the placeholder box when there is no figure yet. */
    figureNote: z.string().optional(),

    /** The four-up strip under a feature. Exactly 4 reads best. */
    stats: z
      .array(z.object({ label: z.string(), value: z.string(), todo: z.boolean().default(false) }))
      .default([]),

    /** Rendered as the results table at the end of a case study. */
    results: z.array(z.object({ metric: z.string(), value: z.string() })).default([]),

    links: z.array(z.object({ label: z.string(), href: z.string() })).default([]),
    draft: z.boolean().default(false),
  }),
});

export const collections = { projects };
