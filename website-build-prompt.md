# Prompt: Build the new Invest 4U Solutions website (HTML / CSS / JS)

> Copy everything below this line into your AI coding tool (Claude, Cursor, etc.) or hand it to a developer.

---

## Role and goal
You are a senior front-end developer and UI designer. Build a complete, modern, responsive, multi-page marketing website **from scratch** for **Invest 4U Solutions** (legal name: **K & VK Invest 4U Advisory Services LLP**), an insurance and investment advisory firm in Kochi, Kerala, operating since 1992. It replaces the current Wix site at https://www.invest4u.in.

Use **plain HTML5, CSS3 and vanilla JavaScript (ES6+)** only. No frameworks and no build step, so the site can be uploaded to any basic host. Small CDN libraries are allowed where listed below.

## Tech requirements
- Semantic HTML5 (`header`, `nav`, `main`, `section`, `article`, `footer`), one `<h1>` per page.
- One shared stylesheet `css/style.css` using CSS custom properties for the colour palette, spacing and typography; one `js/main.js`.
- Mobile-first responsive layout with CSS Grid and Flexbox. Breakpoints: 576px, 768px, 1024px, 1280px.
- Header and footer are identical on every page (repeat the markup, or inject them with a small JS include).
- Allowed CDN libraries: **AOS** (scroll animations), **Swiper.js** (hero and testimonial sliders), **Font Awesome** or inline SVG (icons), Google Fonts.
- Accessibility: WCAG 2.1 AA contrast, `alt` text on every image, visible focus states, keyboard-operable menu and slider, `aria-label` on icon-only links, respect `prefers-reduced-motion` (turn off autoplay and animations).
- Performance: WebP images with `loading="lazy"` (except the hero), `preload` the first hero video poster, compressed MP4 hero videos (under 3 MB each, muted, `playsinline`) with a poster image fallback, defer all JS.
- SEO on every page: unique `<title>` and meta description, Open Graph and Twitter tags, canonical URL, favicon. Add `sitemap.xml` and `robots.txt`.
- Add **JSON-LD structured data** of type `FinancialService` / `LocalBusiness` on the home and contact pages, with name, address, phone, email, opening hours, geo coordinates and social profile URLs.

## Brand and colour scheme (taken from the official logo)
The logo reads **"Invest4U"** with the tagline **"FINANCIAL ARCHITECTS"**. "Invest" is in deep navy, and a teal tick replaces the dot on the "i". "4U" is navy inside a teal open bracket or frame, and the tagline sits below in navy capitals. Use the logo file `assets/images/logo.png` (and create a white/reversed version for dark backgrounds). Show the tagline "Financial Architects" in the site, for example in the hero eyebrow text and the footer.

Exact colours sampled from the logo:
- **Logo Navy `#013364`**: primary brand colour
- **Logo Teal `#00ACA8`**: secondary / accent colour

```css
:root {
  /* Brand (from logo) */
  --color-primary:       #013364; /* logo navy */
  --color-primary-dark:  #0A2540; /* darker navy for footer, overlays */
  --color-primary-light: #1B4F8A; /* hover state for navy */
  --color-accent:        #00ACA8; /* logo teal: icons, lines, highlights, CTA backgrounds */
  --color-accent-dark:   #007A77; /* teal for text/links on white (AA 5.2:1) */
  --color-accent-light:  #E6F7F6; /* pale teal tint for section backgrounds */

  /* Neutrals */
  --color-bg:            #FFFFFF; /* main page background */
  --color-bg-alt:        #F4F8FB; /* alternate section background (cool off-white) */
  --color-bg-tint:       #E6F7F6; /* teal-tint band (checkup card, stats strip) */
  --color-bg-dark:       #0A2540; /* dark sections: founder message, footer */
  --color-text:          #334155; /* body text */
  --color-heading:       #013364; /* headings */
  --color-muted:         #64748B;
  --color-border:        #DCE6EE;
  --color-white:         #FFFFFF;

  /* Gradients */
  --gradient-brand: linear-gradient(135deg, #013364 0%, #00ACA8 100%);
  --gradient-hero:  linear-gradient(120deg, rgba(1,51,100,.88) 0%, rgba(1,51,100,.65) 55%, rgba(0,172,168,.45) 100%);
  --gradient-dark:  linear-gradient(180deg, #013364 0%, #0A2540 100%);
}
```

### Background colour per section
| Section | Background | Text / accents |
|---|---|---|
| Header, transparent over hero | transparent, then `#FFFFFF` with shadow on scroll | navy links, teal active underline |
| Top info bar | `#013364` | white text, teal icons |
| Hero video slider | video + `--gradient-hero` overlay | white headings, teal eyebrow "Financial Architects" |
| Stats counter strip | `--gradient-brand` | white numbers |
| About | `#FFFFFF` | navy headings, teal checkmarks |
| Founder message | `--gradient-dark` (navy) | white text, teal quote mark and frame shape |
| Services | `#F4F8FB` | white cards, teal icon circles, top border turns teal on hover |
| Free Checkup card | `#E6F7F6` band with a `--gradient-brand` card inside | white text |
| How we work timeline | `#FFFFFF` | teal connecting line, navy step numbers |
| Why choose us | `#F4F8FB` | |
| Partners marquee | `#FFFFFF` | grayscale logos, colour on hover |
| Testimonials | `#013364` | white cards, teal stars/quote marks |
| Awards | `#F4F8FB` | |
| Contact | `#FFFFFF` form card on `#F4F8FB` | teal focus rings |
| CTA band (inner pages) | `--gradient-brand` | white |
| Footer | `#0A2540`, bottom bar `#061A2E` | white/light text, teal hover, teal social icon circles |
| Inner page banner | image + `--gradient-hero` overlay | white |

### Button and colour rules (accessibility)
- **Primary button**: background `#00ACA8` (teal) with **navy text `#013364`** (contrast 4.5:1). On hover, use a navy background with white text. Do **not** put white text on the teal (only 2.8:1, which fails).
- **Secondary button**: a navy `#013364` background with white text, or a navy outline.
- On dark navy backgrounds, use a teal button with navy text, or white outline buttons.
- Use `--color-accent-dark` `#007A77` for teal text or links on white; use the bright teal only for icons, lines, shapes and large headings.
- Fonts: **Poppins** or **Montserrat** for headings (600 to 700), which matches the logo's bold geometric sans. Use **Inter** or **Open Sans** for body text (400). Load them from Google Fonts.
- Style: clean, premium and trustworthy. Use generous white space, rounded cards (12 to 16px radius), soft navy-tinted shadows (`0 10px 30px rgba(1,51,100,.08)`) and teal accent lines. Borrow the logo's **open bracket / frame shape** as a decorative motif (teal L-shaped corners on images, section titles and the founder photo frame) and the **tick mark** as the checklist bullet icon.
- Logo on the left of the header; white/reversed logo in the footer.

## Global header (all pages)
- Logo on the left. On the right: Home, About, Services (dropdown listing each service page), Downloads, Pay Online, Contact.
- A **"Free Financial Checkup"** CTA button (teal background, navy text).
- The header is sticky. It is transparent over the hero and turns solid with a shadow on scroll (JS).
- On mobile, a hamburger opens a slide-in menu with an animated icon.
- An optional thin top bar shows the phone number, email and "Mon to Sat 9:00 AM to 6:30 PM".

## Home page (`index.html`): sections in this order

### 1. Hero video slider
- Full-viewport (100vh) slider built with Swiper, with **at least 2 or 3 slides, each with a background video** (autoplay, muted, loop, playsinline) and the gradient overlay on top.
- Each slide has an animated headline, a subtext line and two CTA buttons. Animate the text with a fade-up on slide change.
  - Slide 1: "Empower Your Financial Future". Subtext: "Expert investment guidance and personalised advice for every stage of your financial journey." CTAs: "Get Free Financial Checkup" and "Explore Services".
  - Slide 2: "Protect What Matters Most". Subtext: "Life, health and corporate insurance solutions trusted by families since 1992." CTAs: "Talk to an Advisor" and "Our Services".
  - Slide 3: "Grow Your Wealth with Confidence". Subtext: "Mutual funds, retirement and child education planning tailored to your goals." CTA: "Start Planning".
- Include autoplay (7s), pagination dots, prev/next arrows, a scroll-down indicator and pause on hover.
- Use placeholder stock videos (for example from Pexels, themed on family, office meetings and growth charts) and name the files `assets/videos/hero-1.mp4` and so on, so they can be swapped.

### 2. Stats / counter strip
Show animated count-up numbers, triggered when the strip scrolls into view (IntersectionObserver): **33+ Years of Experience** · **10,000+ Happy Clients** · **Since 1992** · **2 Offices**. Keep these numbers identical on every page.

### 3. About section
- A two-column layout with an image collage (2 or 3 overlapping images, animated in) and text.
- Small label "About Us", title "Guiding Investors for Over Three Decades", and a 2 to 3 paragraph description. Base it on this: founded in 1992 in Tripunithura; a trusted partner of LIC of India; formally registered in 2025 as K & VK Invest 4U Advisory Services LLP; a "service first" approach with time-tested solutions for short and long-term goals.
- A checklist of 3 or 4 key points (Personalised planning, Transparent advice, Lifelong service, Claim support).
- CTA button "Know More About Us" linking to about.html.

### 4. Message from the Founder
- A split layout: a large photo of **K.N. Krishnankutty, Founder & Managing Director** (placeholder `assets/images/founder.jpg`) in a styled frame with an accent shape behind it.
- A quote-style message with a large quotation mark icon, about 80 to 120 words, in his voice, on trust, three decades of serving families, and the mission of making every family financially secure. Mark it clearly as placeholder text for the client to approve.
- A signature-style name, his title, and an optional signature image.

### 5. Services
- Section title "Comprehensive Financial Solutions Tailored for You".
- A responsive card grid (3 columns on desktop, 2 on tablet, 1 on mobile). Each card has an icon, a title, a short description and a "Learn more →" link to its service page. Cards lift and change colour on hover and appear with staggered AOS animations.
- Cards:
  - Life Insurance: family income protection
  - Health Insurance: cashless care and claim support
  - Corporate Insurance: business continuity
  - Mutual Funds: equity, debt and liquid funds
  - Retirement Planning: guaranteed income after work
  - Child Education Planning: securing children's future
  - Tax Planning: 80C / 80D savings
  - Wealth Creation & Estate Planning

### 6. Free Financial Health Checkup (feature card / CTA banner)
- A highlighted full-width card with a gradient background: "Your Financial Health, Our Priority: Get a Free Checkup". Explain the 3 steps (Share your goals, Get a personalised review, Follow a clear plan) with icons and an animated connecting line.
- Button: "Book Free Checkup" (opens the contact page with the service preselected, e.g. `contact.html?service=checkup`).

### 7. How We Work (process timeline)
"Your Journey with Invest 4U: Simple, Transparent, Personalised". Show 4 steps (Consultation, Analysis, Recommendation, Ongoing Support) as an animated horizontal timeline on desktop and a vertical one on mobile.

### 8. Why Choose Us cards
Four to six icon cards: 33+ years of experience, 10,000+ clients, multi-insurer options, claim assistance, doorstep service, free reviews.

### 9. Insurance and fund partners
An infinite logo marquee (CSS animation) showing LIC of India, Star Health, ICICI Lombard, United India Insurance, National Insurance and CAMS. Show only partners the client confirms.

### 10. Testimonials slider
A Swiper carousel of client reviews with photo or initials avatar, name, location and 5-star rating. Use placeholder reviews and note that they must be replaced with real, consented reviews.

### 11. Awards & Recognition
A gallery of award images, **each with a caption** (award name, year, awarding body), and a lightbox on click. The current site shows award images without captions; fix that.

### 12. Contact section
- Two columns: contact details (both office addresses, phone numbers, email, hours, with click-to-call and mailto links) and a **contact form**.
- Form fields: Full Name*, Phone*, Email*, Service interested in (dropdown), Preferred contact time, Message, and a consent checkbox* reading "I agree to the Privacy Policy and consent to be contacted".
- Validate in JS with inline error messages and show a success message after sending. Submit through **Formspree / Web3Forms / EmailJS** (leave a placeholder key) or a simple PHP `mail()` script. Add a honeypot field for spam protection.
- Below the form, embed a Google Map for the Tripunithura head office.

### 13. Footer
- Four columns: (1) white logo, a short about text and "Since 1992"; (2) Quick Links; (3) Services; (4) Contact details for both offices.
- **Social media icons**: Facebook, Instagram, YouTube, WhatsApp (`https://wa.me/919747546614`) and LinkedIn, with hover animations. Open them in a new tab with `rel="noopener"`.
- A **regulatory disclosure strip** (see the compliance section below).
- Bottom bar: "© <current year set by JS> K & VK Invest 4U Advisory Services LLP. All rights reserved." with links to Privacy Policy · Terms of Use · Disclaimer · Grievance Redressal.

### Floating elements (all pages)
- A floating **WhatsApp chat button** (bottom right, with a pulse animation).
- A **back-to-top** button that appears after scrolling.
- An optional page loader showing an animated logo, lasting at most 1s.

## Inner pages
Each inner page gets a page banner (background image, overlay, page title, breadcrumb), the shared header and footer, and a CTA band at the bottom ("Not sure where to start? Book your free financial checkup").

1. **about.html**: company story, a timeline of milestones (1992 founded, LIC partnership, 10,000 clients, Infopark branch, 2025 LLP registration; the client confirms the dates), mission and vision cards, core values, the founder profile with the full message, team section (placeholder cards), awards with captions, both office locations.
2. **services.html**: overview grid of all services linking to detail pages.
3. **Service detail pages**: `life-insurance.html`, `health-insurance.html`, `corporate-insurance.html`, `mutual-funds.html`, `retirement-planning.html`, `child-education.html`, `tax-planning.html`. Each has an intro, key benefits (icon list), who it's for, how we help (steps), an **FAQ accordion (JS)** and a CTA. Carry over content from the current site, for example on life insurance: the "only 10% of Indians have life insurance" protection-gap message and tax savings under Section 80C up to ₹1.5 lakh. The mutual-funds page must show the market-risk disclaimer.
4. **financial-checkup.html** (new): landing page for the free checkup, with benefits, the 3-step process and a short multi-step form (JS progress bar).
5. **calculators.html** (new, optional but recommended): SIP calculator, retirement corpus calculator, life cover (Human Life Value) calculator and child education goal calculator. Use vanilla JS with range sliders, show results as animated numbers, and add a simple Chart.js doughnut chart.
6. **downloads.html**: cards with insurer logos linking to official claim forms: United India Insurance, ICICI Lombard, National Insurance, LIC forms, Star Health, CAMS mutual fund forms. Open them in a new tab.
7. **pay-online.html**: payment options as cards: LIC Direct Pay (link to the official LIC portal), bank transfer (NEFT/RTGS/IMPS: account holder name *K & VK Invest 4U Advisory Services LLP*, account number, bank, branch, IFSC, with a "copy" button per field) and UPI/Google Pay (a UPI ID and QR code). Add a prominent **fraud-safety notice**: "We accept payments only to the accounts listed on this page. We never ask for OTPs or payments to personal numbers. Verify by calling +91 97475 46614." Use a single verified payment number that matches the contact numbers. (Today's site shows a GPay number that isn't one of the contact numbers.)
8. **contact.html**: full contact form (as on the home page), both office cards with maps, hours, WhatsApp and call buttons, and FAQs.
9. **blog.html** (optional): a card grid for financial tips articles, useful for SEO, plus 1 sample article template.

### Pages missing from the current site (must add)
10. **privacy-policy.html**: what data the forms collect, why, how it's stored, who it's shared with, retention, user rights and a grievance contact. Write it in line with India's DPDP Act 2023.
11. **terms.html**: terms of use of the website.
12. **disclaimer.html**: insurance is the subject matter of solicitation; mutual fund investments are subject to market risks, so read all scheme-related documents carefully; past performance is not indicative of future returns; content is for information only.
13. **grievance.html**: grievance officer name, email and phone, escalation steps, and links to IRDAI Bima Bharosa and SEBI SCORES.
14. **404.html**: a branded not-found page with links home.

## Compliance and trust requirements
The current site shows **no regulatory details**. The new site must include placeholders the client fills in, shown in the footer of every page and on the About and relevant service pages:
- IRDAI registration / LIC agency code / insurance agent licence number: `[TO BE PROVIDED]`
- AMFI-registered Mutual Fund Distributor, **ARN-XXXXX**, EUIN: `[TO BE PROVIDED]` (Invest 4U must not call itself a SEBI-registered investment adviser unless it is one.)
- The standard MF line, *"Mutual fund investments are subject to market risks, read all scheme related documents carefully"*, on the home page, the mutual funds page and the footer.
- The LLP identification number (LLPIN) in the footer.
- Consistent claims everywhere: one figure for years in business (33+, since 1992) and one client count (10,000+). The current site says both "10,000+" and "hundreds", and both 32 and 33 years.

## Content and data to use
- Business: Invest 4U Solutions / K & VK Invest 4U Advisory Services LLP. Founder & MD: K.N. Krishnankutty. Since 1992.
- Head office: Vaikkom Road, Kannankulangara, Tripunithura, Kochi, Kerala 682301.
- Branch: Ground Floor, Thapasya Building, Infopark, Kakkanad, Kochi.
- Phones: +91 97475 46614 (primary), +91 98470 71373, +91 98470 46614.
- Email: info@invest4u.in (enquiries), service@invest4u.in (support).
- Hours: Monday to Saturday 9:00 AM to 6:30 PM, closed Sunday.
- Social: Facebook (one official page), Instagram @invest4u.in, YouTube channel, LinkedIn, WhatsApp.
- Rewrite copy to be clear and benefit-focused, and avoid unverifiable claims.

## Animations and interactions
- AOS fade-up, zoom-in and slide effects on sections, with staggered delays on card grids.
- Hero text entrance animation per slide, and a Ken Burns or slow zoom on video posters.
- Counters that count up, and cards that lift with a colour sweep on hover.
- Buttons with a shine or slide hover, and a gradient border on focus.
- Smooth scrolling for anchor links; the header shrinks on scroll.
- An infinite partner-logo marquee.
- FAQ accordion with smooth height transitions.
- All motion disabled under `prefers-reduced-motion: reduce`.

## Folder structure
```
invest4u/
├── index.html, about.html, services.html, contact.html, downloads.html,
│   pay-online.html, financial-checkup.html, calculators.html, blog.html,
│   life-insurance.html, health-insurance.html, corporate-insurance.html,
│   mutual-funds.html, retirement-planning.html, child-education.html, tax-planning.html,
│   privacy-policy.html, terms.html, disclaimer.html, grievance.html, 404.html
├── css/style.css
├── js/main.js            (nav, sliders, counters, forms, accordion, back-to-top)
├── js/calculators.js
├── assets/images/        (logo.png, logo-white.png, founder.jpg, awards/, partners/, services/)
├── assets/videos/        (hero-1.mp4, hero-2.mp4, hero-3.mp4 + posters)
├── favicon.ico, sitemap.xml, robots.txt
```

## Deliverables and acceptance checklist
- [ ] All pages above, working locally by opening index.html.
- [ ] Hero slider with at least 2 videos, text animation and a mobile fallback to poster images.
- [ ] About, Founder message, Services, Checkup card, Testimonials, Awards with captions, Contact form and Footer with social icons on the home page.
- [ ] Privacy, Terms, Disclaimer and Grievance pages, plus regulatory placeholders in the footer.
- [ ] No duplicate pages (the current site has a stray "copy-of-home" page).
- [ ] Lighthouse score of 90+ for Performance, Accessibility, Best Practices and SEO on mobile.
- [ ] No console errors, a valid W3C HTML, and a working, tested form.
- [ ] Every placeholder (text, images, IDs, keys) marked with `TODO:` comments and listed in a `README.md`, together with how to replace videos and colours and how to deploy.
