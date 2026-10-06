"""Shared building blocks for inner pages (dev helper, not deployed)."""
import re
from build import *

SRC = TOOLS + 'src/'
INDEX_MAIN = open(SRC + 'index-main.html').read()


def I(name, extra=''):
    """Icon token, expanded by build()."""
    return '{{icon:' + name + ('|' + extra if extra else '') + '}}'


def _slice(text, start, end, include_end=True):
    a = text.index(start)
    b = text.index(end, a) + (len(end) if include_end else 0)
    return text[a:b]


# Reused straight from the home page so they never drift apart
CONTACT_FORM = _slice(INDEX_MAIN, '<form class="form" data-contact-form', '</form>')
AWARDS_GRID = _slice(INDEX_MAIN, '<div class="grid grid--3 awards-grid" data-lightbox-group>', '        </figure>\n      </div>')
LIGHTBOX = _slice(INDEX_MAIN, '<!-- Awards lightbox -->', '</dialog>')
FOUNDER_PHOTO = _slice(INDEX_MAIN, '<div class="founder__photo"', '<span class="bracket-corner bracket-corner--br" aria-hidden="true"></span>\n      </div>')
FOUNDER_SIGN = _slice(INDEX_MAIN, '<figcaption class="founder__sign">', '</figcaption>')

INNER_HEAD = AOS_CSS
INNER_SCRIPTS = AOS_JS

CALL = f'<a class="btn btn--outline-white" href="tel:+919847046614">{I("phone")} +91 98470 46614</a>'


def crumbs(items):
    """items: list of (label, href or None for the current page)."""
    lis = []
    for label, href in items:
        lis.append(f'<li><a href="{href}">{label}</a></li>' if href else f'<li><span aria-current="page">{label}</span></li>')
    return ('<nav class="breadcrumb" aria-label="Breadcrumb">\n          <ol>\n            '
            + '\n            '.join(lis) + '\n          </ol>\n        </nav>')


def banner(title, trail, lead='', img='service-detail', eyebrow=''):
    """Page banner with the only <h1> on the page. trail: breadcrumb items after Home."""
    eb = f'<span class="eyebrow eyebrow--light">{eyebrow}</span>\n        ' if eyebrow else ''
    ld = f'<p class="page-banner__lead">{lead}</p>\n        ' if lead else ''
    return f'''  <section class="page-banner">
    <img class="page-banner__bg" src="assets/images/banners/{img}.webp" alt="" width="1920" height="640" fetchpriority="high">
    <div class="container">
      {eb}<h1>{title}</h1>
      {ld}{crumbs([("Home", "index.html")] + trail)}
    </div>
  </section>'''


def cta_band(heading='Not sure where to start?', text='Book your free financial checkup. It takes about 30 minutes and costs nothing.'):
    return f'''  <section class="cta-band bg-brand" aria-labelledby="cta-title">
    <div class="container cta-band__inner">
      <div>
        <h2 id="cta-title">{heading}</h2>
        <p>{text}</p>
      </div>
      <div class="btn-group">
        <a class="btn btn--lg" href="financial-checkup.html">Book Free Checkup {I("arrow-right", "icon--arrow")}</a>
        {CALL.replace('class="btn ', 'class="btn btn--lg ')}
      </div>
    </div>
  </section>'''


def faq(items, prefix, heading='Frequently Asked Questions', eyebrow='FAQs', bg='bg-alt'):
    rows = []
    for i, (q, a) in enumerate(items, 1):
        rows.append(f'''        <div class="accordion__item">
          <h3 class="accordion__heading">
            <button class="accordion__trigger" type="button" id="{prefix}-{i}-btn" aria-expanded="false" aria-controls="{prefix}-{i}">
              {q}
              {I("chevron-down")}
            </button>
          </h3>
          <div class="accordion__panel" id="{prefix}-{i}" role="region" aria-labelledby="{prefix}-{i}-btn">
            <div class="accordion__panel-inner">{a}</div>
          </div>
        </div>''')
    return f'''  <section class="section {bg}" id="faq" aria-labelledby="{prefix}-title">
    <div class="container container--narrow">
      <div class="section-head" data-aos="fade-up">
        <span class="eyebrow">{eyebrow}</span>
        <h2 id="{prefix}-title">{heading}</h2>
      </div>
      <div class="accordion" data-accordion data-aos="fade-up">
{chr(10).join(rows)}
      </div>
    </div>
  </section>'''


def main(*parts, extra_after=''):
    return '<main id="main">\n' + '\n\n'.join(parts) + '\n</main>' + ('\n\n' + extra_after if extra_after else '')


MF_RISK = (f'<div class="notice">{I("shield")}<p><strong>Mutual fund investments are subject to market risks, '
           'read all scheme related documents carefully.</strong> Past performance is not indicative of future returns.</p></div>')

REG_LIST = '''<!-- TODO: client to provide every [TO BE PROVIDED] value -->
      <dl class="reg-list">
        <div><dt>Legal name</dt><dd>K &amp; VK Invest 4U Advisory Services LLP</dd></div>
        <div><dt>LLPIN</dt><dd>[TO BE PROVIDED]</dd></div>
        <div><dt>IRDAI registration / LIC agency code</dt><dd>[TO BE PROVIDED]</dd></div>
        <div><dt>AMFI-registered Mutual Fund Distributor</dt><dd>ARN-XXXXX · EUIN [TO BE PROVIDED]</dd></div>
      </dl>
      <p class="text-muted mt-6">We are an AMFI-registered mutual fund distributor and an insurance agency. We are not a SEBI-registered investment adviser.</p>'''


def page(out, title, desc, body, **kw):
    kw.setdefault('extra_head', INNER_HEAD)
    kw.setdefault('extra_scripts', INNER_SCRIPTS)
    img = kw.pop('banner_img', None)
    if img:
        kw['preload'] = f'<link rel="preload" as="image" href="assets/images/banners/{img}.webp" fetchpriority="high">'
    build(out, title, desc, body, **kw)


# ---------------------------------------------------------------- Goal-based services (home, Services page, navbar, footer)
# (id, icon, title, one-line description, [(service, link)], (more link, label))
GOALS = [
    ('protect-family', 'shield-heart', 'Protect Your Family', 'Make sure the people you love are looked after, whatever happens.',
     [('Life Insurance', 'life-insurance.html'), ('Term Insurance', 'term-insurance.html'), ('Health Insurance', 'health-insurance.html'), ('General Insurance', 'general-insurance.html')],
     ('life-insurance.html', 'Protect your family')),
    ('grow-wealth', 'seedling', 'Grow Your Wealth', 'Make your savings work harder with disciplined, goal-matched investing.',
     [('Mutual Funds', 'mutual-funds.html'), ('SIP', 'sip-investment.html'), ('Wealth Creation', 'wealth-creation.html'), ('Tax Planning', 'tax-planning.html')],
     ('mutual-funds.html', 'Start growing your wealth')),
    ('plan-future', 'route', 'Plan Your Future', 'Put a clear plan and a number behind the milestones that matter to you.',
     [('Retirement Planning', 'retirement-planning.html'), ("Child's Education", 'child-education.html'), ('Marriage Planning', 'marriage-planning.html'), ('Goal-Based Planning', 'goal-based-planning.html')],
     ('goal-based-planning.html', 'Plan your future')),
    ('protect-legacy', 'landmark', 'Protect Your Legacy', 'Pass on what you have built to the next generation, smoothly and clearly.',
     [('Estate Planning', 'estate-planning.html'), ('Succession Planning', 'succession-planning.html'), ('Wealth Transfer', 'wealth-transfer.html')],
     ('estate-planning.html', 'Protect your legacy')),
]


def goal_grid(with_ids=False):
    """The 2 × 2 goal cards + 'Not sure where to start?' card (same markup as the home page)."""
    cards = []
    for i, (gid, ic, title, desc, items, (more, more_label)) in enumerate(GOALS):
        delay = ' data-aos-delay="100"' if i % 2 else ''
        ident = f' id="{gid}"' if with_ids else ''
        chips = '\n'.join(f'            <li><a href="{h}">{n}</a></li>' for n, h in items)
        cards.append(f'''        <article class="goal-card"{ident} data-aos="fade-up"{delay}>
          <span class="goal-card__icon">{I(ic)}</span>
          <div class="goal-card__body">
            <h3>{title}</h3>
            <p>{desc}</p>
            <ul class="goal-card__chips" aria-label="{title}: services">
{chips}
            </ul>
            <a class="link-arrow" href="{more}">{more_label} {I("arrow-right")}</a>
          </div>
        </article>''')
    return '      <div class="goal-grid">\n' + '\n'.join(cards) + '''
        <article class="card card--cta goal-grid__cta" data-aos="fade-up">
          <h3>Not sure where to start?</h3>
          <p>Book a free financial checkup and we'll help you work out what you need, and what you don't.</p>
          <a class="btn" href="financial-checkup.html">Book Free Checkup</a>
        </article>
      </div>'''


# ---------------------------------------------------------------- Partners (home page section component)
# Logo files live in invest4u/assets/images/partners/. TODO: client to confirm the list and logo permissions.
PARTNER_LOGOS = {
    'cams': ('cams.svg', 500, 176, 'CAMS'),
    'lic': ('lic.webp', 150, 83, 'LIC of India'),
    'star-health': ('star-health.webp', 203, 89, 'Star Health'),
    'united-india': ('united-india.webp', 185, 89, 'United India Insurance'),
    'national-insurance': ('national-insurance.webp', 191, 89, 'National Insurance'),
    'icici-lombard': ('icici-lombard.webp', 247, 89, 'ICICI Lombard'),
}
PARTNER_CATEGORIES = [
    ('chart-line', 'Investment Partners', ['cams']),
    ('user-shield', 'Life Insurance Partners', ['lic']),
    ('heart-pulse', 'Health Insurance Partners', ['star-health']),
    ('umbrella', 'General Insurance Partners', ['united-india', 'national-insurance', 'icici-lombard']),
]


def partner_card(icon, title, keys, delay=0):
    logos = '\n'.join(
        f'            <li class="partner-card__logo"><img src="assets/images/partners/{f}" alt="{alt}" width="{w}" height="{h}" loading="lazy"></li>'
        for f, w, h, alt in (PARTNER_LOGOS[k] for k in keys))
    d = f' data-aos-delay="{delay}"' if delay else ''
    return f'''        <article class="partner-card" data-aos="fade-up"{d}>
          <h3 class="partner-card__title"><span class="partner-card__icon">{I(icon)}</span>{title}</h3>
          <ul class="partner-card__logos" aria-label="{title}">
{logos}
          </ul>
        </article>'''


def partner_grid():
    return '      <div class="partner-grid">\n' + '\n'.join(
        partner_card(ic, t, k, (i % 2) * 100) for i, (ic, t, k) in enumerate(PARTNER_CATEGORIES)) + '\n      </div>'


def redirect_page(old, new, title):
    """A tiny noindex page at an old address that forwards to the new one (static-host friendly)."""
    open(SITE + old, 'w').write(f'''<!doctype html>
<html lang="en-IN">
<head>
  <meta charset="utf-8">
  <title>Moved | Invest 4U Solutions</title>
  <meta name="robots" content="noindex">
  <link rel="canonical" href="https://www.invest4u.in/{new}">
  <meta http-equiv="refresh" content="0; url={new}">
</head>
<body>
  <p>This page has moved to <a href="{new}">{title}</a>.</p>
</body>
</html>
''')
    print('wrote', old, '(redirect to', new + ')')
