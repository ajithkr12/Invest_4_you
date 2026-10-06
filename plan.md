# Plan: Invest 4U Solutions website rebuild

Source brief: [website-build-prompt.md](website-build-prompt.md) · Task checklist: [task.md](task.md)

## Status (28 Sep 2026)

Phases 0–6 are done, plus an extra piece of work: a "More" menu with 14 calculators, modelled on groww.in. Phases 7 (QA) and 8 (handover/README) remain. The site has 37 HTML pages, and 35 of them are in the sitemap. Every page so far passes axe (WCAG 2.1 AA) at 1440px and 390px, with no console errors and no broken internal links. Launch still depends on client content (see §8).

## 1. Goal

Build a static, multi-page marketing site for **Invest 4U Solutions** (K & VK Invest 4U Advisory Services LLP), Kochi, since 1992, to replace the Wix site at invest4u.in. It must run by opening `index.html` locally and deploy to any basic host with no build step.

## 2. Constraints and key decisions

| Area | Decision |
|---|---|
| Stack | Plain HTML5, CSS3, vanilla ES6+. No framework or bundler at runtime: the deployable folder is plain static files. |
| Page assembly | Header, footer and `<head>` are repeated in every page, not injected with JS (a fetch-based include breaks under `file://` and hurts SEO). A dev-only Python script, `tools/build_all.py`, assembles every page from `tools/partials/` so they stay identical. |
| Fonts | **Switzer** (variable, 100–900), self-hosted in `assets/fonts/` as `'Switzer-Variable'` for headings and body. Licence: ITF Free Font License (`Switzer-LICENSE-FFL.txt`). No Google Fonts. No font preload, because it causes a CORS error when a page is opened from disk. |
| CDN libs | AOS (all pages); Swiper (home only); Chart.js (calculator pages only). All from cdnjs, scripts `defer`. |
| Icons | Inline SVG copied from Font Awesome Free (CC BY 4.0, source in `tools/fa-svgs/`), not the Font Awesome webfont, to keep pages light. |
| CSS | One `css/style.css`, mobile-first, tokens on `:root`, breakpoints 576/768/1024/1280. |
| JS | `js/main.js`: shared behaviour, each feature exits early if its markup is missing. `js/calculators.js`: calculator engine, calculator pages only. |
| Colour and contrast | Palette from the logo. Teal buttons use **navy text** (white on teal is 2.8:1). `#007A77` for teal text on white. Two deviations from the brief for AA: body grey `#5B6B80` (was `#64748B`), and panels with white text use `--gradient-brand-text`, which ends on darker teal. |
| Forms | Web3Forms, with the access key as a `TODO:` placeholder. Honeypot plus JS validation. Without a key the form tells the visitor to call rather than faking success. The contact and checkup forms share one submit path. |
| Service preselect | `contact.html?service=<value>` preselects the dropdown. |
| Hero | No brand-colour overlay on the hero video (client request; the brief asked for a navy/teal gradient). Instead a neutral dark shade (`.hero__media::after`): 62%→28% black left-to-right on desktop, an even 50% on phones. No text shadow on hero or nav text. Inner-page banners keep the gradient overlay. |
| Motion | `prefers-reduced-motion` turns off autoplay, video, AOS, counters, the marquee and Ken Burns. The hero has a pause button (WCAG 2.2.2). Testimonials don't autoplay. |
| Media | WebP images; lazy-load everything below the fold. Hero video loads only on screens 768px and wider, not under reduced motion or Save-Data; phones get posters. Target is under 3 MB per MP4 (currently exceeded, see task.md). |
| Compliance | Every footer carries IRDAI/LIC code, AMFI ARN/EUIN and LLPIN placeholders plus the MF risk line. The firm is described as an AMFI-registered distributor, never a "SEBI-registered investment adviser". Tax benefits are stated as old-regime only. |
| Consistent figures | 33+ years, since 1992, 10,000+ clients, 2 offices, everywhere. |
| Placeholders | Visible `[TO BE PROVIDED]`, `[Year]` or yellow "draft" labels, plus `TODO:` comments (about 165), so nothing ships by accident. |
| 404 | Uses `<base href="/">` so it works when a host serves it from any missing URL. Side effect: it looks unstyled when opened from disk. |

## 3. Folder structure

```
Invest_4U_Solutions/
├── website-build-prompt.md, plan.md, task.md
├── invest4u/                 ← deploy this folder only
│   ├── 37 × *.html           (see §5)
│   ├── css/style.css
│   ├── js/main.js, js/calculators.js
│   ├── assets/images/        logo(.png/.webp), logo-white, favicon-32, apple-touch-icon, icon-512, og-image.jpg,
│   │                         about-*, founder, team/, awards/, partners/ (SVG), services/, banners/, blog/
│   ├── assets/videos/        hero-1..3.mp4 + desktop/mobile WebP posters
│   ├── favicon.ico, sitemap.xml, robots.txt
│   └── (README.md, Phase 8)
└── tools/                    ← dev only, never deployed
    ├── build_all.py          rebuild every page + sitemap.xml + robots.txt
    ├── build.py              page assembler (partials, icons, nav state, breadcrumb JSON-LD)
    ├── build_index.py, build_styleguide.py
    ├── pages_common.py       banner, CTA band, FAQ, shared blocks
    ├── pages_services.py     services overview + 7 service pages (content as data)
    ├── pages_core.py         about, contact, checkup, downloads, pay-online
    ├── pages_calcs.py        calculators hub + 14 calculator pages (content + formulas)
    ├── pages_misc.py         blog, article, legal pages, 404
    ├── partials/             head, header (incl. More menu), footer, loader
    ├── src/                  index-main.html, styleguide-main.html
    └── fa-svgs/              Font Awesome Free SVG source + licence
```

**Workflow:** edit content in `tools/`, run `python3 tools/build_all.py`, then open `invest4u/index.html`. Editing the HTML in `invest4u/` directly also works, but the next rebuild overwrites it.

## 4. Architecture

### CSS (`style.css`, in order)

1. Tokens · 2. Reset and base · 3. Layout utilities and section backgrounds · 4. Components (buttons, titles and bracket motif, tick list, cards, notices, forms, multi-step progress, choice chips, copy buttons, accordion, breadcrumb) · 5. Header, top bar, nav, Services dropdown, **More mega-menu**, mobile menu · 6. Footer and disclosure strip · 7. Floating elements · 8. Sections (hero, stats, about, founder, services, checkup, timeline, why-us, marquee, testimonials, awards and lightbox, contact, page banner, CTA band, prose, milestones, service detail, downloads, pay online, calculators, hub, blog, 404) · 10. Reduced motion

### `main.js`

`initLoader`, `initHeader` (solid and shrink on scroll), `initMobileNav` (focus trap, Esc), `initSubmenus` (Services and More: hover, click, Esc, click-outside), `initSmoothScroll`, `initBackToTop`, `initHeroSlider` (fade, 7s, pause button, only the active video plays, inactive slides are `inert`), `initTestimonials`, `initCounters`, `initInView`, `initLightbox` (`<dialog>`), `initForms` (validation, honeypot, Web3Forms, `?service=`, multi-step), `initAccordions`, `initCopyButtons`, `initAOS`, `setYear`.

### `calculators.js`

- **Registry:** one pure function per calculator returns `{ big, rows, chart, table?, summary }`.
- **Markup contract:** `[data-calc]` panel; `.range` paired with `input[type=number]` or `select`, linked by `data-key`; `[data-preset]` chips; `data-fmt` (`inr`, `pct`, `months`) on outputs; optional `.calc-schedule` table.
- **Also handles:** hub search, and redirecting the old `calculators.html#…` links.
- **Worked examples:** each page's example is computed by the matching Python formula in `pages_calcs.py`, so text and calculator always agree.

### SEO

Every page has a unique title and description, canonical, Open Graph and Twitter tags (image size and alt), and favicon links. JSON-LD: `FinancialService` (home, contact), `Article` (blog post), and `BreadcrumbList` on every inner page, generated from the visible breadcrumb. The sitemap is generated, noindex pages are excluded, and robots.txt disallows the style guide.

## 5. Pages (37)

- **Home:** index
- **Company:** about, contact, downloads, pay-online, financial-checkup
- **Services (8):** services overview (incl. `#wealth`); life-insurance, health-insurance, corporate-insurance, mutual-funds, retirement-planning, child-education, tax-planning
- **Calculators (15):** calculators hub, plus:
  - *Mutual funds & investing:* sip, step-up-sip, lumpsum, swp, cagr
  - *Loans:* emi (home, car and personal presets)
  - *Deposits & savings:* fd, rd, ppf, compound-interest
  - *Planning:* retirement, life-cover, child-education, inflation
- **Blog:** blog, blog-article
- **Legal:** privacy-policy (DPDP Act 2023), terms, disclaimer, grievance
- **Utility:** 404 (noindex), styleguide (internal, noindex; delete before launch if not wanted)

**Navigation:** Home · About · Services ▾ · Downloads · Pay Online · Contact · **More ▾** (calculators mega-menu) · Free Financial Checkup CTA. The nav fits on one line from 1024px; the CTA shortens to "Free Checkup" below 1280px.

## 6. Build phases

| Phase | Output | Status |
|---|---|---|
| 0. Setup | Folders, logo conversion and reversed logo, favicon, placeholder media | Done |
| 1. Design system | Tokens, base, components; style guide page | Done |
| 2. Shell | Header, footer, floating elements, core JS | Done |
| 3. Home page | All sections, sliders, counters, lightbox, contact form, JSON-LD | Done |
| 4. Shared JS | Accordion, multi-step form, copy buttons | Done |
| 5. Inner pages | About, services, 7 service pages, contact, checkup, downloads, pay online, blog, legal, 404 | Done |
| 6. SEO | Meta audit, breadcrumb JSON-LD, sitemap.xml, robots.txt, build_all.py | Done |
| Extra | "More" menu, calculators hub, 14 calculator pages | Done |
| 7. QA | W3C validation, Lighthouse mobile ≥ 90 ×4, keyboard/screen reader, reduced motion, responsive, cross-browser | **Next** |
| 8. Handover | README.md: placeholders, swapping media and colours, form key, rebuild, deploy | To do |

## 7. Risks

- **Hero video weight:** the current MP4s are 30, 26 and 11 MB. Two are 4K and one has an audio track, against a 3 MB target. This is the biggest Lighthouse risk. Compress them before Phase 7.
- **Third-party requests:** Google Maps, Fonts and cdnjs can fail or slow the page (one transient 500 from Google was seen during testing). The site degrades gracefully: AOS content stays visible and the calculators show without the chart.
- **Stale figures:** PPF rate, FD/RD/loan rates and tax limits change. They are marked in the copy and in task.md.
- **Rebuild overwrites hand edits** in `invest4u/*.html`. Edit in `tools/` or accept that manual edits are lost on rebuild.

## 8. Open questions for the client

- **Regulatory IDs:** IRDAI/LIC agency code, AMFI ARN and EUIN, LLPIN, grievance officer.
- **Partners:** confirmed list and permission to use their logos.
- **Payment details:** bank account, IFSC, UPI ID and QR, all tied to the single verified number +91 98470 46614.
- **Content approval:** founder message, real consented testimonials, milestone years, award names, years and bodies, team details.
- **Media:** founder, team and award photos; final hero videos, compressed, with matching posters.
- **Links and data:** exact claim-form and LIC pay URLs; social profile URLs; map pin and geo coordinates; a source for the "1 in 10 Indians" life insurance statistic.
- **Legal:** lawyer review of the privacy, terms, disclaimer and grievance pages; dates, retention period and response times.
- **Form service:** Web3Forms account and access key.
