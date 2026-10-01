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

CALL = f'<a class="btn btn--outline-white" href="tel:+919747546614">{I("phone")} +91 97475 46614</a>'


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
