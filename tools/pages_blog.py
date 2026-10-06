"""Blog / Financial Education: reusable components + pages (dev helper, not deployed).
Content lives in blog_data.py. Components: blog_card, category_filter, featured_articles,
article_header, related_articles. Pages: home section (via {{blog}} in index-main.html),
blog.html (filters, search, load more) and one blog-<slug>.html page per article."""
import datetime
from pages_common import *
from blog_data import CATEGORIES, ARTICLES

CAT = {k: (label, icon) for k, label, icon in CATEGORIES}
EDU_NOTE = 'This article is for general education only and is not personal financial, tax or legal advice.'
TAX_NOTE = 'Tax rules change from year to year. Figures here reflect the rules at the time of writing; please verify the current rules or consult a tax professional before acting.'


def url(a):
    return f'blog-{a["slug"]}.html'


def nice_date(iso):
    d = datetime.date.fromisoformat(iso)
    return f'{d.day} {d.strftime("%b %Y")}'


def by_date(items):
    return sorted(items, key=lambda a: a['date'], reverse=True)


# ---------------------------------------------------------------- Components
def blog_media(a, big=False):
    """Category illustration (inline SVG icon on a brand gradient): no image request, crisp at any size."""
    label, icon = CAT[a['category']]
    cls = 'blog-media blog-media--' + a['category'] + (' blog-media--big' if big else '')
    return f'<div class="{cls}" aria-hidden="true"><span class="blog-media__icon">{I(icon)}</span></div>'


def blog_card(a, heading='h3'):
    label, _ = CAT[a['category']]
    search = f'{a["title"]} {a["excerpt"]} {label}'.lower().replace('"', '')
    return f'''        <article class="blog-card" data-category="{a["category"]}" data-search="{search}">
          {blog_media(a)}
          <div class="blog-card__body">
            <span class="blog-card__cat">{label}</span>
            <{heading} class="blog-card__title"><a href="{url(a)}">{a["title"]}</a></{heading}>
            <p class="blog-card__excerpt">{a["excerpt"]}</p>
            <div class="blog-card__meta">
              <span><time datetime="{a["date"]}">{nice_date(a["date"])}</time> · {a["minutes"]} min read</span>
              <span class="blog-card__more" aria-hidden="true">Read More {I("arrow-right")}</span>
            </div>
          </div>
        </article>'''


def category_filter(label='Filter articles by category'):
    chips = ['<button class="chip" type="button" data-filter="all" aria-pressed="true">All topics</button>']
    chips += [f'<button class="chip" type="button" data-filter="{k}" aria-pressed="false">{I(icon)} {name}</button>' for k, name, icon in CATEGORIES]
    return f'<div class="blog-filter" role="group" aria-label="{label}">\n          ' + '\n          '.join(chips) + '\n        </div>'


def featured_articles():
    """Home page section: featured first; JS shows 3 for the chosen category (no-JS: the first 3)."""
    ordered = [a for a in by_date(ARTICLES) if a['featured']] + [a for a in by_date(ARTICLES) if not a['featured']]
    cards = '\n'.join(blog_card(a) for a in ordered)
    return f'''  <!-- ============ 11b. Blog / Financial Education (built from tools/blog_data.py) ============ -->
  <section class="section blog-home" id="learn" aria-labelledby="learn-title">
    <div class="container">
      <div class="section-head" data-aos="fade-up">
        <span class="eyebrow">Financial Education</span>
        <h2 id="learn-title">Financial Knowledge for Better Decisions</h2>
        <p>Learn the basics of insurance, investments, retirement, tax planning, and family financial planning, all in one place.</p>
      </div>
      <div class="blog" data-blog data-limit="3">
        {category_filter()}
        <p class="sr-only" aria-live="polite" data-blog-count></p>
        <div class="blog-grid">
{cards}
        </div>
      </div>
      <div class="text-center mt-6"><a class="btn btn--lg" href="blog.html">View All Articles {I("arrow-right", "icon--arrow")}</a></div>
    </div>
  </section>

'''


def article_header(a):
    label, _ = CAT[a['category']]
    return f'''  <section class="page-banner article-banner">
    <img class="page-banner__bg" src="assets/images/banners/blog.webp" alt="" width="1920" height="640" fetchpriority="high">
    <div class="container">
      <a class="eyebrow eyebrow--light article-banner__cat" href="blog.html?cat={a["category"]}">{label}</a>
      <h1>{a["title"]}</h1>
      <p class="article-meta"><span>By the Invest 4U team</span><span><time datetime="{a["date"]}">{nice_date(a["date"])}</time></span><span>{a["minutes"]} min read</span></p>
      {crumbs([("Home", "index.html"), ("Blog", "blog.html"), (a["title"], None)])}
    </div>
  </section>'''


def related_articles(a, n=3):
    same = [x for x in by_date(ARTICLES) if x['category'] == a['category'] and x['slug'] != a['slug']]
    other = [x for x in by_date(ARTICLES) if x['category'] != a['category']]
    picks = (same + other)[:n]
    return f'''  <section class="section bg-alt" aria-labelledby="related-title">
    <div class="container">
      <div class="section-head" data-aos="fade-up">
        <span class="eyebrow">Keep learning</span>
        <h2 id="related-title">Related articles</h2>
      </div>
      <div class="blog-grid">
{chr(10).join(blog_card(x) for x in picks)}
      </div>
    </div>
  </section>'''


def next_steps():
    return f'''  <section class="cta-band bg-brand next-steps" aria-labelledby="next-title">
    <div class="container">
      <span class="eyebrow eyebrow--light">Have a question?</span>
      <h2 id="next-title">Talk it through with an advisor</h2>
      <p>Every family's situation is different. We're happy to explain how this applies to you, at no cost.</p>
      <ul class="next-steps__grid">
        <li><a class="next-step" href="contact.html">{I("calendar-check")}<strong>Book a Free Consultation</strong><span>Meet us at our office, at home or online.</span></a></li>
        <li><a class="next-step" href="tel:+919847046614">{I("phone")}<strong>Talk to an Advisor</strong><span>Call +91 98470 46614, Mon to Sat, 9 to 6:30.</span></a></li>
        <li><a class="next-step" href="financial-checkup.html">{I("clipboard-check")}<strong>Get a Free Financial Review</strong><span>A complete check of your cover, savings and goals.</span></a></li>
      </ul>
    </div>
  </section>'''


# ---------------------------------------------------------------- Pages
def article_page(a):
    label, _ = CAT[a['category']]
    notices = [f'<div class="notice">{I("lightbulb")}<p>{EDU_NOTE}</p></div>']
    if a.get('notice') == 'tax' or a['category'] == 'tax':
        notices.append(f'<div class="notice notice--warning">{I("triangle-exclamation")}<p>{TAX_NOTE}</p></div>')
    if a['category'] in ('investments', 'retirement'):
        notices.append(MF_RISK)
    others = '\n'.join(f'            <li><a href="blog.html?cat={k}">{name}</a></li>' for k, name, _ in CATEGORIES)
    body = main(
        article_header(a),
        f'''  <section class="section">
    <div class="container with-aside">
      <article class="prose article-body">
        {blog_media(a, big=True)}
        {a["body"].strip()}
        <div class="article-notices">
          {chr(10).join("          " + n for n in notices).strip()}
        </div>
      </article>
      <aside class="aside-sticky" aria-label="More from the blog">
        <div class="aside-card aside-card--brand">
          <h2>Want personal guidance?</h2>
          <p>Book a free financial checkup and we'll look at your situation together.</p>
          <a class="btn btn--block mt-6" href="financial-checkup.html">Book Free Checkup</a>
        </div>
        <nav class="aside-card" aria-label="Blog categories">
          <h2>Browse topics</h2>
          <ul class="toc">
{others}
            <li><a href="blog.html">All articles</a></li>
          </ul>
        </nav>
      </aside>
    </div>
  </section>''',
        related_articles(a),
        next_steps(),
    )
    jsonld = {"@context": "https://schema.org", "@type": "Article", "headline": a['title'], "description": a['excerpt'],
              "articleSection": label, "datePublished": a['date'], "dateModified": a['date'],
              "author": {"@type": "Organization", "name": "Invest 4U Solutions"},
              "publisher": {"@type": "Organization", "name": "Invest 4U Solutions", "logo": {"@type": "ImageObject", "url": "https://www.invest4u.in/assets/images/logo.png"}},
              "image": "https://www.invest4u.in/assets/images/og-image.jpg", "mainEntityOfPage": f"https://www.invest4u.in/{url(a)}"}
    page(url(a), a['title'], a['excerpt'], body, banner_img='blog', jsonld=jsonld, og_type='article', published=a['date'])


def blog_page():
    cards = '\n'.join(blog_card(a, 'h2') for a in by_date(ARTICLES))
    body = main(
        banner('Financial Knowledge for Better Decisions', [('Blog', None)],
               'Plain-language guides to insurance, investments, retirement, tax and family financial planning, written for families and first-time investors.',
               img='blog', eyebrow='Blog &amp; Financial Education'),
        f'''  <section class="section bg-alt" aria-label="Articles">
    <div class="container">
      <div class="blog" data-blog data-page-size="6">
        <div class="blog-toolbar">
          {category_filter()}
          <div class="blog-search">
            <label class="sr-only" for="blog-search">Search articles</label>
            {I("magnifying-glass-chart")}
            <input class="input" id="blog-search" type="search" placeholder="Search articles" autocomplete="off" data-blog-search>
          </div>
        </div>
        <p class="blog-count" aria-live="polite" data-blog-count></p>
        <div class="blog-grid">
{cards}
        </div>
        <p class="notice" hidden data-blog-empty>{I("magnifying-glass-chart")}<span>No articles match that search. Try another word, or <a href="contact.html">ask us your question</a>.</span></p>
        <div class="text-center mt-6"><button class="btn btn--outline" type="button" hidden data-blog-more>Load more articles</button></div>
      </div>
    </div>
  </section>''',
        next_steps(),
    )
    page('blog.html', 'Blog: Financial Knowledge for Better Decisions',
         'Plain-language guides from Invest 4U Solutions on insurance, SIPs and mutual funds, retirement, tax saving and family financial planning.',
         body, banner_img='blog')


def legacy_redirect():
    """Old sample article URL: send visitors (and search engines) to its new address."""
    new = 'blog-how-much-life-insurance-do-you-need.html'
    open(SITE + 'blog-article.html', 'w').write(f'''<!doctype html>
<html lang="en-IN">
<head>
  <meta charset="utf-8">
  <title>Moved | Invest 4U Solutions</title>
  <meta name="robots" content="noindex">
  <link rel="canonical" href="https://www.invest4u.in/{new}">
  <meta http-equiv="refresh" content="0; url={new}">
</head>
<body>
  <p>This article has moved to <a href="{new}">How Much Life Insurance Do You Really Need?</a></p>
</body>
</html>
''')
    print('wrote blog-article.html (redirect)')


def build_all_blog():
    blog_page()
    for a in ARTICLES:
        article_page(a)
    legacy_redirect()


if __name__ == '__main__':
    build_all_blog()
