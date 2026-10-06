"""Dev helper (not deployed): assembles a page from invest4u/partials + a <main> fragment and inlines Font Awesome icons ({{icon:name}}). Output is plain static HTML."""
import re, sys, json

SITE = '/Users/ajithk/projects/Invest_4U_Solutions/invest4u/'
TOOLS = '/Users/ajithk/projects/Invest_4U_Solutions/tools/'
FA = TOOLS + 'fa-svgs/'
ALIAS = {'location': 'solid/location-dot', 'facebook': 'brands/facebook-f', 'linkedin': 'brands/linkedin-in',
         'shield': 'solid/shield-halved', 'clock': 'regular/clock', 'whatsapp': 'brands/whatsapp',
         'instagram': 'brands/instagram', 'youtube': 'brands/youtube'}

SWIPER_CSS = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Swiper/11.0.5/swiper-bundle.min.css">'
SWIPER_JS = '<script src="https://cdnjs.cloudflare.com/ajax/libs/Swiper/11.0.5/swiper-bundle.min.js" defer></script>'
AOS_CSS = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css">'
AOS_JS = '<script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js" defer></script>'


def icon(m):
    name, _, extra = m.group(1).partition('|')
    path = ALIAS.get(name) or next(p for p in (f'solid/{name}', f'regular/{name}', f'brands/{name}')
                                   if __import__('os').path.exists(FA + p + '.svg'))
    s = open(FA + path + '.svg').read()
    vb = re.search(r'viewBox="([^"]+)"', s).group(1)
    d = re.search(r' d="([^"]+)"', s).group(1)
    cls = 'icon' + (' ' + extra if extra else '')
    return f'<svg class="{cls}" viewBox="{vb}" aria-hidden="true"><path d="{d}"/></svg>'


def part(n):
    return re.sub(r'^\s*<!--.*?-->\s*', '', open(TOOLS + f'partials/{n}.html').read(), count=1, flags=re.S).strip()


def indent(s, n):
    return '\n'.join((' ' * n + l if l.strip() else l) for l in s.splitlines())


def breadcrumb_jsonld(main, canonical):
    """BreadcrumbList structured data, read from the page's visible breadcrumb."""
    nav = re.search(r'<nav class="breadcrumb".*?</nav>', main, re.S)
    if not nav:
        return None
    items = []
    for m in re.finditer(r'<li>(?:<a href="([^"]+)">(.*?)</a>|<span aria-current="page">(.*?)</span>)</li>', nav.group(0)):
        href, label = (m.group(1), m.group(2)) if m.group(1) else (None, m.group(3))
        url = canonical if href is None else 'https://www.invest4u.in/' + ('' if href == 'index.html' else href)
        name = re.sub(r'<[^>]+>', '', label).replace('&amp;', '&')
        items.append({'@type': 'ListItem', 'position': len(items) + 1, 'name': name, 'item': url})
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': items} if items else None


def build(out, title, desc, main, current=None, sub_current=None, extra_head='', extra_scripts='',
          loader=False, solid=False, jsonld=None, full_title=None, robots=None, preload='', og_type='website', published=None):
    head = part('head')
    page = out[:-5]
    canonical = 'https://www.invest4u.in/' + ('' if page == 'index' else out)
    ft = full_title or f'{title} | Invest 4U Solutions'
    head = (head.replace('{{Page title}} | Invest 4U Solutions', ft)
                .replace('{{Unique 140–160 character description}}', desc)
                .replace('{{Same as meta description}}', desc)
                .replace('https://www.invest4u.in/{{page}}.html', canonical))
    if og_type != 'website':
        extra = f'<meta property="og:type" content="{og_type}">'
        if published:
            extra += f'\n<meta property="article:published_time" content="{published}">'
        head = head.replace('<meta property="og:type" content="website">', extra)
    if robots:
        head = head.replace('<meta name="theme-color"', f'<meta name="robots" content="{robots}">\n<meta name="theme-color"')
    head = head.replace('<link rel="stylesheet" href="css/style.css">',
                        (preload + '\n' if preload else '') + (extra_head + '\n' if extra_head else '') + '<link rel="stylesheet" href="css/style.css">')
    head = head.replace('<script src="js/main.js" defer></script>',
                        (extra_scripts + '\n' if extra_scripts else '') + '<script src="js/main.js" defer></script>')
    if jsonld:
        if jsonld.get('@type') == 'FinancialService':
            head += '\n<!-- TODO: confirm the geo coordinates, and add the official YouTube URL to "sameAs" -->'
        head += '\n<script type="application/ld+json">\n' + json.dumps(jsonld, indent=2, ensure_ascii=False) + '\n</script>'
    crumbs = breadcrumb_jsonld(main, canonical)
    if crumbs:
        head += '\n<script type="application/ld+json">\n' + json.dumps(crumbs, indent=2, ensure_ascii=False) + '\n</script>'

    header = part('header')
    if solid:
        header = header.replace('<header class="site-header">', '<header class="site-header site-header--solid">')
    if current:
        header = header.replace(f'<a class="nav__link" href="{current}">', f'<a class="nav__link" href="{current}" aria-current="page">')
    if sub_current:
        # Mark the dropdown (Services or More) that contains the current page, and the link itself
        blocks = re.split(r'(?=<li class="nav__item nav__item--has-sub)', header)
        for i, blk in enumerate(blocks):
            if f'href="{sub_current}"' in blk and blk.startswith('<li class="nav__item nav__item--has-sub'):
                blocks[i] = re.sub(r'^<li class="(nav__item nav__item--has-sub[^"]*)"', r'<li class="\1 is-active"', blk)
        header = ''.join(blocks)
        # A service page not listed in the menu (e.g. Corporate Insurance) still highlights Services
        if ' is-active"' not in header and sub_current.endswith('.html') and not sub_current.endswith('calculator.html') and sub_current != 'calculators.html':
            header = header.replace('<li class="nav__item nav__item--has-sub nav__item--more">', '<li class="nav__item nav__item--has-sub nav__item--more is-active">', 1)
        header = re.sub(f'<a href="{re.escape(sub_current)}"', f'<a href="{sub_current}" aria-current="page"', header)
        header = header.replace(f'<a class="mega__all" href="{sub_current}">', f'<a class="mega__all" href="{sub_current}" aria-current="page">')

    body = (part('loader') + '\n\n' if loader else '') + header + '\n\n' + main.strip() + '\n\n' + part('footer')
    html = f'''<!doctype html>
<html lang="en-IN" class="no-js">
<head>
{indent(head, 2)}
</head>
<body>
{body}
</body>
</html>
'''
    html = re.sub(r'\{\{icon:([\w|-]+(?: [\w-]+)*)\}\}', icon, html)
    assert '{{' not in html, re.findall(r'\{\{[^}]*\}\}', html)[:5]
    open(SITE + out, 'w').write(html)
    print('wrote', out, len(html) // 1024, 'KB')
