# Tasks: Invest 4U Solutions website

Brief: [website-build-prompt.md](website-build-prompt.md) · Plan: [plan.md](plan.md)

Legend: `[ ]` todo · `[x]` done · `[~]` in progress · `[!]` blocked on client

**Status (28 Sep 2026):** Phases 0–6 and the extra calculators work are done. **Next: Phase 7 (QA), then Phase 8 (README).** Rebuild all pages with `python3 tools/build_all.py`.

---

## Phase 0: Setup

- [x] Create folder structure (`css/`, `js/`, `assets/images/{awards,partners,services,banners,team,blog}`, `assets/videos/`); partials now live in `tools/partials/`
- [x] Convert `invest logo.png.avif` to `assets/images/logo.png` + `logo.webp`
- [x] Create white/reversed logo `assets/images/logo-white.png`
- [x] Generate `favicon.ico` (+ `apple-touch-icon.png`) from the logo mark
- [x] Add placeholder hero videos `hero-1/2/3.mp4` + WebP posters (desktop + mobile). Generated locally as branded slow-zoom clips (~110 KB each)
- [x] Real hero videos added (`hero-1/2/3.mp4`)
- [ ] **Compress hero videos to < 3 MB each.** Currently 30 MB, 26 MB and 11 MB; hero-1 and hero-2 are 4K, and hero-3 has an audio track. For example: `ffmpeg -i in.mp4 -vf scale=1280:-2 -an -c:v libx264 -crf 28 -preset slow -movflags +faststart -t 12 out.mp4`
- [x] Posters (`hero-N.webp` 1920×1080, `hero-N-mobile.webp` 828×1472) regenerated from the new videos (27–56 KB each)
- [x] Brand-colour overlay removed from the hero at the client's request; eyebrow switched to white
- [x] Neutral dark shade over the hero image/video (black 62%→28% left-to-right on desktop, 50% on phones); text shadows on hero and nav text removed (client request)
- [x] Fixed: prev/next arrows were still showing on phones (CSS order bug)
- [x] Add placeholder images (founder, team, awards, partners, service banners, about collage, OG image), all WebP
- [x] Founder photo: real portrait from the current invest4u.in site (`kk.webp`), on a light brand background with the cut-out edge faded (640×800); used on Home and About

## Phase 1: Design system (`css/style.css`)

- [x] `:root` tokens: palette from brief, gradients, spacing, radius (12–16px), shadow, type scale
- [x] ~~Google Fonts: Poppins + Inter~~, replaced by **Switzer** (self-hosted variable font, `assets/fonts/`, ITF Free Font License) for headings and body
- [x] Reset, base typography, `:focus-visible` rings, `.sr-only`, skip link
- [x] Layout: container, section spacing, grid helpers, breakpoints 576/768/1024/1280
- [x] Section backgrounds: white, alt `#F4F8FB`, tint `#E6F7F6`, dark gradient, brand gradient
- [x] Buttons: primary (teal bg + navy text → navy/white hover), secondary, outline, white-outline; shine hover; gradient focus border
- [x] Section title with teal bracket/L-corner motif; tick-mark list bullets
- [x] Cards (lift + teal top border on hover), accordion, form fields + error states, breadcrumb
- [x] `@media (prefers-reduced-motion: reduce)` kills animations/transitions

## Phase 2: Global shell

- [x] Top info bar (phone, email, hours) on navy
- [x] Header: logo, nav (Home, About, Services ▾, Downloads, Pay Online, Contact, More ▾), "Free Financial Checkup" CTA ("Free Checkup" below 1280px)
- [x] Services dropdown (hover + keyboard)
- [x] Mobile hamburger → slide-in menu, animated icon, focus trap, Esc closes
- [x] Sticky header: transparent over hero → white + shadow + shrink on scroll
- [x] Footer 4 columns: white logo + about + "Since 1992" + "Financial Architects"; Quick Links; Services; both offices
- [x] Social icons (FB, IG, YouTube, WhatsApp `wa.me/919747546614`, LinkedIn), `target="_blank" rel="noopener"`, `aria-label`s
- [x] Regulatory disclosure strip (IRDAI/LIC code, AMFI ARN/EUIN, LLPIN, MF risk line)
- [x] Bottom bar: © JS year + Privacy · Terms · Disclaimer · Grievance
- [x] Floating WhatsApp button (pulse), back-to-top, page loader (≤ 1s)
- [x] Save reference copies in `tools/partials/` (head, header, footer + floating, loader)
- [x] `styleguide.html` dev page showing tokens, components and the shell (noindex; delete before launch if not wanted)
- [x] axe check on the style guide: 0 violations at 1440px and 390px; no console errors
- [x] `js/main.js` core: header, mobile nav, smooth scroll, back-to-top, loader, year

## Phase 3: Home page (`index.html`)

- [x] 1. Hero Swiper: 3 video slides, gradient overlay, eyebrow "Financial Architects", fade-up text per slide, 7s autoplay, dots, arrows, pause on hover, scroll indicator, poster fallback on mobile / reduced motion, preload first poster
- [x] 2. Stats strip: 33+ years · 10,000+ clients · Since 1992 · 2 offices; IntersectionObserver count-up
- [x] 3. About: overlapping image collage, "Guiding Investors for Over Three Decades", copy, 4-point tick list, "Know More About Us"
- [x] 4. Founder message: framed photo (K.N. Krishnankutty), quote icon, 80–120 word message (`TODO:` client approval), signature
- [x] 5. Services: 8 cards, 3/2/1 columns, staggered AOS, "Learn more →" links
- [x] 6. Free Checkup card: gradient card on tint band, 3 steps + animated connector, "Book Free Checkup" → `contact.html?service=checkup`
- [x] 7. How We Work: 4-step timeline (horizontal desktop / vertical mobile)
- [x] 8. Why Choose Us: 6 icon cards
- [x] 9. Partners marquee (CSS infinite, grayscale → colour), placeholder name tiles
- [x] Real partner logos: LIC, Star Health, ICICI Lombard, United India, National Insurance (the client's own copies from invest4u.in) and CAMS (official SVG); shown as white tiles in the marquee and on Downloads
- [ ] `[!]` Confirm the partner list, permission to display each logo, and higher-resolution logo files (current ones are ~90px tall)
- [x] 10. Testimonials Swiper on navy: avatar/initials, name, location, 5 stars (`TODO:` real consented reviews)
- [x] 11. Awards gallery with captions (name, year, body) + lightbox
- [x] 12. Contact: details (click-to-call, mailto, hours, both offices) + form + Google Map embed
- [x] MF market-risk line on page
- [x] JSON-LD `FinancialService`/`LocalBusiness`
- [x] Checks: axe 0 violations (1440px + 390px), no console errors, no horizontal scroll, form tested with a mocked Web3Forms response, reduced-motion path tested
- [ ] `[!]` Confirm geo coordinates in the JSON-LD and the map pin

- [x] Testimonials rebuilt as a scroll-driven 3D card cloud modelled on groww.in: "Trusted by 10,000+ families since 1992" headline + Book Free Checkup, 17 cards at different depths that fly past as you scroll (sticky 230vh section); phones get a swipeable row, reduced motion / no JS a plain grid
- [ ] `[!]` Replace the 17 sample testimonials with real, consented reviews

## Phase 4: Shared JS features (`js/main.js`)

- [x] Swiper init (hero + testimonials), only active slide video plays
- [x] Counters
- [x] AOS init (off under reduced motion)
- [x] FAQ accordion (smooth height, `aria-expanded`/`aria-controls`, optional single-open mode, all answers visible without JS)
- [x] Lightbox (keyboard: Esc, arrows; focus return)
- [x] Form validation: required fields, phone (Indian 10-digit), email, consent; inline errors; honeypot; Web3Forms submit (`TODO:` key); success message
- [x] `?service=` query param preselects the dropdown
- [x] Multi-step form with progress bar (checkup page): per-step validation, Enter advances, Back keeps answers, shares the contact form's submit code
- [x] Copy-to-clipboard buttons (pay-online), with fallback and screen-reader announcement
- [x] Demos of all three in `styleguide.html`; axe 0 violations; home page form re-tested after the refactor

## Phase 5: Inner pages

Common to each: page banner (image + overlay + h1 + breadcrumb), CTA band "Not sure where to start? Book your free financial checkup".

- [x] Build inner-page template (banner + CTA band)
- [x] `about.html`: story, milestone timeline (years marked `[Year]` for the client), mission/vision, core values, founder full message, team placeholders, awards, both offices, regulatory details
- [x] `services.html`: overview grid of all services (incl. Wealth Creation & Estate Planning section `#wealth`)
- [x] Service-detail template: intro, key benefits, who it's for, how we help (steps), FAQ accordion, CTA
  - [x] `life-insurance.html`: "only 10% of Indians insured" gap, 80C up to ₹1.5 lakh
  - [x] `health-insurance.html`: cashless care, claim support, 80D
  - [x] `corporate-insurance.html`
  - [x] `mutual-funds.html`: equity/debt/liquid, AMFI ARN, **market-risk disclaimer**
  - [x] `retirement-planning.html`
  - [x] `child-education.html`
  - [x] `tax-planning.html`: 80C / 80D
- [x] `financial-checkup.html`: benefits, 3-step process, multi-step form
- [x] `calculators.html` + `js/calculators.js`: first version (4 tabbed calculators), later replaced by the hub + 14 pages (see "Added" below)
- [x] `downloads.html`: insurer cards → official claim form links (United India, ICICI Lombard, National, LIC, Star Health, CAMS), new tab
- [x] `pay-online.html`: LIC payment link, bank transfer card with copy buttons, UPI ID + QR placeholder, prominent fraud-safety notice
- [x] `contact.html`: full form, both office cards with maps, hours, WhatsApp/call buttons, FAQs, JSON-LD
- [x] `blog.html` + `blog-article.html` sample template
- [x] `privacy-policy.html` (DPDP Act 2023)
- [x] `terms.html`
- [x] `disclaimer.html`
- [x] `grievance.html` (officer placeholder, escalation, IRDAI Bima Bharosa, Insurance Ombudsman, SEBI SCORES, SMART ODR)
- [x] `404.html` branded
- [x] Checks: axe 0 violations and exactly one h1 on all 23 pages at 1440px and 390px; no console errors; no horizontal scroll; no broken internal links, anchors or duplicate ids
- [x] Calculator results verified against independent calculations
- [x] 404 tested over HTTP from a nested URL (`<base href="/">` keeps assets working)
- [ ] `[!]` Legal pages: lawyer review; fill in dates, retention period and response times
- [ ] `[!]` Replace insurer home-page links on Downloads and Pay Online with the exact claim-form / LIC pay pages
- [ ] `[!]` Confirm the "1 in 10 Indians" statistic on the life insurance page, with a source

## Phase 6: SEO

- [x] Unique `<title>` + meta description on every page
- [x] Open Graph + Twitter tags + canonical on every page
- [x] Favicon links on every page
- [x] `sitemap.xml` (all pages except 404)
- [x] `robots.txt`
- [x] Single `<h1>` per page; check heading order
- [x] Audit: titles ≤ 65 chars, descriptions 100–160 chars, no duplicates, canonical = og:url, no skipped heading levels
- [x] `og:image` size + alt text, `twitter:image:alt`; `og:type=article` + publish date on the blog article
- [x] BreadcrumbList JSON-LD generated from the visible breadcrumb on every inner page (now 35); all 38 JSON-LD blocks parse
- [x] `tools/build_all.py` rebuilds every page and regenerates sitemap.xml (now 35 URLs, noindex pages excluded) and robots.txt
- [x] Partials moved out of the deployable folder to `tools/partials/`
- [ ] After launch: submit sitemap.xml in Google Search Console and test pages with Google's Rich Results Test

## Phase 7: QA

_Already automated during the build: axe on every page at 1440px and 390px, console errors, horizontal overflow, internal links and anchors, duplicate ids, calculator maths. Phase 7 adds the checks below._

- [ ] Compress hero videos first (see Phase 0); they will dominate the Performance score
- [ ] W3C HTML validation, all pages
- [ ] No console errors, all pages
- [ ] Lighthouse mobile ≥ 90 for Performance / Accessibility / Best Practices / SEO (home + 2 inner pages)
- [ ] Contrast check (AA) incl. buttons and teal text
- [ ] Keyboard-only walkthrough: menu, dropdown, sliders, accordion, lightbox, forms
- [ ] `prefers-reduced-motion` walkthrough
- [ ] Responsive check at 360 / 576 / 768 / 1024 / 1280 / 1440
- [ ] Form test end-to-end (valid, invalid, honeypot, success)
- [ ] All internal links resolve; no duplicate pages (no "copy-of-home")
- [ ] Consistent figures everywhere (33+, since 1992, 10,000+)
- [ ] Works opened via `file://` and via a local server
- [ ] Cross-browser: Chrome, Safari (incl. iOS), Firefox, Edge

## Phase 8: Handover

- [ ] Every placeholder marked with `TODO:`
- [ ] `README.md`: placeholder list, replacing videos/images, changing colours (tokens), setting the form key, deployment steps

---

## Added: "More" menu with calculators (modelled on groww.in/calculators)

- [x] "More" mega-menu in the navbar (desktop hover/keyboard, mobile accordion), grouped: Mutual funds & investing · Loans · Deposits & savings · Planning
- [x] Calculators hub `calculators.html`: grouped cards + search; old `calculators.html#sip|retirement|hlv|education` links redirect to the new pages
- [x] 14 calculator pages, each with inputs, results, doughnut chart, about, formula, worked example, FAQs, related calculators:
  SIP, Step-up SIP, Lumpsum, SWP, CAGR, Loan EMI (home/car/personal presets + yearly schedule), FD, RD, PPF (yearly table), Compound interest, Retirement, Life cover (HLV), Child education, Inflation
- [x] All 14 verified against independent Python formulas; worked examples are generated from the same formulas
- [x] Navbar fits on one line from 1024px (CTA shortens to "Free Checkup" below 1280px)
- [x] Sitemap now 35 URLs; axe clean on all new pages at 1440px and 390px
- [ ] `[!]` Confirm current PPF rate (7.1% default) and typical FD/RD/loan rates before launch
- [x] 6 more calculators (from the client's list; Lumpsum, SWP, PPF, FD, RD and EMI already existed): Mutual Fund Returns (SIP/lumpsum), XIRR (monthly SIP), Sukanya Samriddhi Yojana, EPF, Income Tax (old vs new regime, FY 2025-26 slabs) and GST (add/remove, CGST/SGST split). New "Tax" group; More menu now 5 columns. 20 calculators in total; sitemap 41 URLs
- [x] Fixed across all calculators: typed values are used exactly (the slider no longer rounds them), and negative amounts keep their minus sign
- [ ] `[!]` Each year: update the Income Tax slabs (FY 2025-26 now), and check the GST rates and the SSY / EPF / PPF interest rates
- [ ] Optional later: HRA, gratuity, NPS calculators

- [x] Slide 1 kept video-only (client choice); the page `<h1>` is a visually hidden heading in the hero
- [ ] Regenerate hero-1 posters (`hero-1.webp`, `hero-1-mobile.webp`) from the new `hero-1.mp4`; phones show the poster, which is from the old video
- [ ] Remove the unused 30 MB `assets/videos/hero-10.mp4` before deploying

## Waiting on client `[!]`

- [ ] IRDAI registration / LIC agency code
- [ ] AMFI ARN + EUIN
- [ ] LLPIN
- [ ] Grievance officer name, email, phone
- [ ] Confirmed partner list + logo permission + high-res logo files
- [ ] Bank details, UPI ID, QR code
- [ ] Higher-resolution founder photo (current source is only 350px wide) + approval of founder message
- [ ] Real testimonials (with consent)
- [ ] Award images + names, years, awarding bodies
- [ ] Milestone dates
- [ ] Team photos and names
- [ ] Social profile URLs (Facebook, YouTube, LinkedIn)
- [ ] Web3Forms / form service account
- [ ] Exact claim-form URLs per insurer and LIC's direct pay page
- [ ] Source for the "1 in 10 Indians have life insurance" statistic
- [ ] Map pin and geo coordinates for both offices
- [ ] Lawyer review of the legal pages; dates, retention period, response times
- [ ] Current PPF / FD / RD / loan rates to use as calculator defaults
- [ ] Compressed final hero videos
