# tejaswadhwa.github.io

Personal site. Astro, static, deployed to GitHub Pages by GitHub Actions.

## Run it

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # outputs to dist/
```

## Where things live

| What | Where |
|---|---|
| Name, email, links, affiliations | `src/consts.ts` |
| Design tokens (color, type, spacing) | `src/styles/global.css`, top of file |
| Project schema | `src/content.config.ts` |
| The projects | `src/content/projects/*.md` |
| Page templates | `src/pages/` |
| Generated figures | `public/figures/` |
| Figure generator | `scripts/make_figures.py` |
| Site URL (canonical, sitemap, OG) | `site:` in `astro.config.mjs` |

## Adding or editing a project

Each project is one markdown file in `src/content/projects/`. The frontmatter
schema is enforced at build time, so a missing required field fails the build
rather than shipping a half-written page.

`tier` decides where it appears:

| tier | Homepage section | Treatment |
|---|---|---|
| `selected` | Selected work | Figure, four-up stat strip, full case study |
| `current` | Currently building | One line, near the top |
| `also` | Also built | Compact row |

`order` sorts within a tier, lowest first. Copy `stars-cdp.md` as the smallest
example and `harmonicore.md` as the fullest one.

## Figures

Nothing on this site is drawn by hand. Figures come out of the project code
itself, styled to match the site:

```bash
pip install matplotlib numpy          # plus librosa soundfile for the pitch plot
python scripts/make_figures.py --harmonicore ~/Projects/harmonicore
```

That writes `<name>-light.png` and `<name>-dark.png` into `public/figures/`.
Reference the base name with no extension and the right one loads per theme:

```yaml
figure: "/figures/harmonicore-ringmod"
figureAlt: "SystemVerilog ring modulator output against the Python reference"
```

Leave `figure` out and the slot renders a labelled placeholder instead, using
whatever `figureNote` says.

## Before you ship

```bash
grep -rn "TODO" src/ | wc -l    # should be 0
```
