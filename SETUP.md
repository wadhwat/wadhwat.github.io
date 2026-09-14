# Getting this live

## 1. Repo

Name it **`<your-github-username>.github.io`** and make it **public**.

Public is not optional on a free account: GitHub Pages will only publish from a
private repo on Pro, Team or Enterprise. It is also the right choice anyway. The
site is public by definition, and a public repo with real commit history is a
small positive signal on its own.

Nothing sensitive goes in here. Contact details you are happy to publish, and
nothing from an employer.

```bash
cd site
git init -b main
git add -A
git commit -m "Initial site"
git remote add origin git@github.com:wadhwat/wadhwat.github.io.git
git push -u origin main
```

## 2. Turn on Pages

1. Settings → Pages → Build and deployment → **Source: GitHub Actions**
2. Push. The workflow in `.github/workflows/deploy.yml` runs on its own.
3. When it goes green, `https://wadhwat.github.io` is live.

That is the quick version running. Everything below is optional polish.

## 3. Custom domain, when you have one

1. Buy `tejaswadhwa.com` (Cloudflare Registrar or Namecheap, about $12/yr).
2. At the registrar, add:
   ```
   A     @    185.199.108.153
   A     @    185.199.109.153
   A     @    185.199.110.153
   A     @    185.199.111.153
   CNAME www  wadhwat.github.io
   ```
3. Settings → Pages → Custom domain → `tejaswadhwa.com` → Save. GitHub writes
   the `CNAME` file into the repo itself, so you do not need to create one.
4. Wait for the DNS check, then tick **Enforce HTTPS**.
5. Change `site:` in `astro.config.mjs` to the new domain and push. That is the
   only code change the domain needs.

DNS takes anywhere from two minutes to a few hours. Nothing is broken if it does
not resolve immediately.

## 4. Fill in the content

```bash
grep -rn "TODO" src/
```

Priority order:

1. `src/consts.ts` — email, GitHub, LinkedIn. Five minutes; every page uses them.
2. `src/content/projects/harmonicore.md` — the stats, then "What broke". Finish
   this one file completely before touching the others.
3. `src/content/projects/socet-scoreboard.md`
4. The three in-progress ones, which are short.
5. `src/pages/about.astro` — the one paragraph that is actually yours.

## 5. Figures

```bash
pip install matplotlib numpy
python scripts/make_figures.py --harmonicore ~/Projects/harmonicore
```

The ring modulator figure needs `v2-effects/ring_mod_output.csv`, which
`make ring_mod_verify` produces. The pitch figure additionally needs
`pip install librosa soundfile`.

Then set `figure: "/figures/harmonicore-ringmod"` in the frontmatter.

## 6. Ship checks

- [ ] `grep -rn "TODO" src/` returns nothing
- [ ] Open it on your phone
- [ ] Lighthouse 95+ on all four categories
- [ ] Every linked GitHub repo has a README that stands on its own
- [ ] LinkedIn: custom URL claimed, website field set, projects in Featured
- [ ] GitHub profile: website field set
- [ ] Submit the domain to Google Search Console
