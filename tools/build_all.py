"""Rebuild every page, then write sitemap.xml and robots.txt (dev helper, not deployed).

Usage:  python3 tools/build_all.py
"""
import datetime, glob, os, re

import build_index, build_styleguide, pages_services, pages_core, pages_misc, pages_calcs
from build import SITE

BASE = 'https://www.invest4u.in/'


def build_pages():
    build_index.main()
    build_styleguide.main()
    for s in pages_services.SERVICES:
        pages_services.service_page(s)
    pages_services.services_overview()
    for fn in (pages_core.about, pages_core.contact, pages_core.checkup, pages_core.downloads, pages_core.pay_online):
        fn()
    pages_calcs.build_all_calcs()
    for fn in (pages_misc.blog, pages_misc.article, pages_misc.privacy,
               pages_misc.terms, pages_misc.disclaimer, pages_misc.grievance, pages_misc.not_found):
        fn()


def priority(page):
    if page == 'index.html':
        return '1.0'
    if page in ('services.html', 'financial-checkup.html', 'contact.html', 'about.html'):
        return '0.9'
    if page in ('privacy-policy.html', 'terms.html', 'disclaimer.html', 'grievance.html'):
        return '0.3'
    return '0.7'


def write_sitemap():
    today = datetime.date.today().isoformat()
    urls = []
    for path in sorted(glob.glob(SITE + '*.html')):
        page = os.path.basename(path)
        html = open(path).read()
        if re.search(r'<meta name="robots" content="[^"]*noindex', html):
            continue  # 404, styleguide
        loc = BASE + ('' if page == 'index.html' else page)
        urls.append(f'  <url>\n    <loc>{loc}</loc>\n    <lastmod>{today}</lastmod>\n    <priority>{priority(page)}</priority>\n  </url>')
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + '\n'.join(urls) + '\n</urlset>\n')
    open(SITE + 'sitemap.xml', 'w').write(xml)
    print('wrote sitemap.xml with', len(urls), 'URLs')


def write_robots():
    open(SITE + 'robots.txt', 'w').write(
        'User-agent: *\n'
        'Allow: /\n'
        'Disallow: /styleguide.html\n'
        '\n'
        f'Sitemap: {BASE}sitemap.xml\n')
    print('wrote robots.txt')


if __name__ == '__main__':
    build_pages()
    write_sitemap()
    write_robots()
