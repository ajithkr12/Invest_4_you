"""Calculators, blog, legal pages and 404 (dev helper, not deployed)."""
from pages_common import *

CHART_JS = '<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js" defer></script>'
CALC_JS = '<script src="js/calculators.js" defer></script>'

# Blog and articles are built by pages_blog.py (content in blog_data.py).


# ---------------------------------------------------------------- Legal pages
def legal(out, title, desc, lead, sections, updated='[Date]', review=True):
    toc = '\n'.join(f'            <li><a href="#{sid}">{h}</a></li>' for sid, h, _ in sections)
    content = '\n\n'.join(f'        <h2 id="{sid}">{h}</h2>\n        {html}' for sid, h, html in sections)
    note = '\n        <!-- TODO: have this page reviewed by a lawyer before launch -->' if review else ''
    body = main(
        banner(title, [(title, None)], lead, img='legal'),
        f'''  <section class="section">
    <div class="container with-aside">
      <div class="prose">{note}
        <p class="updated">Last updated: {updated} <!-- TODO: set the date when approved --></p>
{content}
      </div>
      <aside class="aside-sticky" aria-label="On this page">
        <nav class="aside-card" aria-label="Contents">
          <h2>On this page</h2>
          <ul class="toc">
{toc}
          </ul>
        </nav>
        <div class="aside-card">
          <h2>Questions?</h2>
          <p>Email <a href="mailto:service@invest4u.in">service@invest4u.in</a> or call <a href="tel:+919847046614">+91 98470 46614</a>.</p>
        </div>
      </aside>
    </div>
  </section>''',
        cta_band(),
    )
    page(out, title, desc, body, banner_img='legal')


GRIEVANCE_CONTACT = '''<ul>
          <li><strong>Grievance Officer:</strong> [Name TO BE PROVIDED]</li>
          <li><strong>Email:</strong> <a href="mailto:service@invest4u.in">service@invest4u.in</a> <!-- TODO: confirm or use a dedicated grievance address --></li>
          <li><strong>Phone:</strong> <a href="tel:+919847046614">+91 98470 46614</a></li>
          <li><strong>Address:</strong> K &amp; VK Invest 4U Advisory Services LLP, Vaikkom Road, Kannankulangara, Tripunithura, Kochi, Kerala 682301</li>
        </ul>'''


def privacy():
    s = [
        ('who', 'Who we are', '<p>This website is run by K &amp; VK Invest 4U Advisory Services LLP ("Invest 4U", "we", "us"), Vaikkom Road, Kannankulangara, Tripunithura, Kochi, Kerala 682301. For the purposes of the Digital Personal Data Protection Act, 2023 (DPDP Act), we are the Data Fiduciary for the personal data you share with us through this website.</p>'),
        ('collect', 'What we collect', '''<p>We collect only what you choose to give us through our forms:</p>
        <ul>
          <li><strong>Contact form:</strong> your name, phone number, email address, the service you're interested in, your preferred contact time and your message.</li>
          <li><strong>Financial checkup form:</strong> your name, age group, the goals you select, whether you have existing insurance, your phone number and email address.</li>
        </ul>
        <p>We do not use analytics or advertising cookies on this website. <!-- TODO: update this section if analytics are added --> Some pages load content from third parties (Google Fonts, Google Maps and our script libraries), which may receive your IP address and browser details when you visit.</p>'''),
        ('why', 'Why we use it', '''<p>We use your details only to:</p>
        <ul>
          <li>respond to your enquiry and arrange a consultation or checkup;</li>
          <li>prepare advice and quotes you have asked for;</li>
          <li>keep records we are required to keep by law or by the regulators who supervise insurance and mutual fund distribution.</li>
        </ul>
        <p>We will not use your details for marketing unrelated to your enquiry without your separate consent, and we never sell your data.</p>'''),
        ('consent', 'Your consent', '<p>By ticking the consent box on our forms, you agree that we may use the details you provide for the purposes above. You can withdraw your consent at any time by emailing us. Withdrawing consent does not affect anything we did lawfully before you withdrew it, but we may no longer be able to help with your enquiry.</p>'),
        ('share', 'Who we share it with', '''<ul>
          <li><strong>Our form provider</strong> (Web3Forms), which delivers your form submission to our email inbox. <!-- TODO: confirm the form service used --></li>
          <li><strong>Insurers and mutual fund houses</strong>, only when you ask us to proceed with a policy or investment, and only the details they need.</li>
          <li><strong>Regulators and authorities</strong>, where the law requires it.</li>
        </ul>'''),
        ('store', 'How we store and protect it', '<p>Form submissions reach our business email account, which is protected by password and access controls. Only staff who need your details to help you can see them. Paper records at our offices are kept in locked storage.</p>'),
        ('retain', 'How long we keep it', '<p>If you don\'t become a client, we delete your enquiry within [12 months] of our last contact. <!-- TODO: confirm the retention period --> If you become a client, we keep your records for as long as you are a client and afterwards for as long as insurance and mutual fund regulations require.</p>'),
        ('rights', 'Your rights', '''<p>Under the DPDP Act you have the right to:</p>
        <ul>
          <li>ask what personal data we hold about you and how we use it;</li>
          <li>ask us to correct, complete or update it;</li>
          <li>ask us to erase it, unless we must keep it by law;</li>
          <li>withdraw your consent;</li>
          <li>have your complaint resolved by our Grievance Officer; and</li>
          <li>nominate someone to exercise these rights on your behalf in the event of death or incapacity.</li>
        </ul>
        <p>To use any of these rights, contact our Grievance Officer below. We will respond within [30 days]. <!-- TODO: confirm response time --></p>'''),
        ('grievance', 'Grievance Officer', GRIEVANCE_CONTACT + '\n        <p>If you are not satisfied with our response, you may complain to the Data Protection Board of India.</p>'),
        ('changes', 'Changes to this policy', '<p>We may update this policy from time to time. The date at the top of this page shows when it last changed.</p>'),
    ]
    legal('privacy-policy.html', 'Privacy Policy', 'How Invest 4U Solutions collects, uses, stores and protects your personal data, and your rights under the Digital Personal Data Protection Act, 2023.',
          'How we collect, use and protect your personal data, in line with the Digital Personal Data Protection Act, 2023.', s)


def terms():
    s = [
        ('about', 'About these terms', '<p>These terms apply to your use of www.invest4u.in (the "website"), run by K &amp; VK Invest 4U Advisory Services LLP. By using the website you accept them. If you don\'t agree, please don\'t use the website.</p>'),
        ('info', 'Information only', '<p>The content on this website is general information. It is not personal financial, tax or legal advice, and it is not an offer to sell any product. Please speak to us before making any decision, and read the policy or scheme documents carefully. See our <a href="disclaimer.html">Disclaimer</a>.</p>'),
        ('calculators', 'Calculators', '<p>Our calculators give illustrative estimates based on the assumptions you enter. They are not a guarantee or a forecast of returns, costs or cover.</p>'),
        ('use', 'Using the website', '''<p>You agree not to:</p>
        <ul>
          <li>use the website for anything unlawful or misleading;</li>
          <li>submit false information or someone else's details without their permission;</li>
          <li>try to disrupt, damage or gain unauthorised access to the website.</li>
        </ul>'''),
        ('ip', 'Intellectual property', '<p>The Invest 4U name and logo, and the text, design and images on this website, belong to us or our licensors. Partner names and logos belong to their owners and are shown to identify the products we distribute.</p>'),
        ('links', 'Links to other websites', '<p>We link to insurers, fund houses, regulators and payment pages for your convenience. We are not responsible for the content or security of those websites.</p>'),
        ('payments', 'Payments', '<p>Pay only through the options listed on our <a href="pay-online.html">Pay Online</a> page. We are not responsible for payments made to any other account.</p>'),
        ('liability', 'Limitation of liability', '<p>We take care to keep the website accurate and available, but we don\'t guarantee that it is error-free or uninterrupted. To the extent the law allows, we are not liable for any loss arising from your use of the website or reliance on its content.</p>'),
        ('law', 'Governing law', '<p>These terms are governed by the laws of India. The courts in Ernakulam, Kerala have jurisdiction.</p>'),
        ('changes', 'Changes', '<p>We may update these terms at any time. The date at the top shows the latest version.</p>'),
    ]
    legal('terms.html', 'Terms of Use', 'Terms of use for the Invest 4U Solutions website, run by K & VK Invest 4U Advisory Services LLP, Kochi.',
          'The terms that apply when you use this website.', s)


def disclaimer():
    s = [
        ('insurance', 'Insurance', '<p><strong>Insurance is the subject matter of solicitation.</strong> For more details on risk factors, terms and conditions, please read the sales brochure and policy wording carefully before concluding a sale. Benefits, premiums and tax treatment depend on the specific policy and the insurer\'s terms.</p>'),
        ('mf', 'Mutual funds', f'''{MF_RISK}
        <p>We are an AMFI-registered Mutual Fund Distributor (ARN-XXXXX). We are not a SEBI-registered investment adviser. Past performance of any scheme is not indicative of future returns. The value of investments can go down as well as up.</p>'''),
        ('info', 'General information only', '<p>Everything on this website is for general information. It is not personal advice and does not take your individual circumstances into account. Please consult us, and read all product documents, before making any financial decision.</p>'),
        ('tax', 'Tax', '<p>Tax benefits mentioned on this website, including under Sections 80C, 80D and 10(10D) of the Income-tax Act, depend on current tax law and your circumstances, and are available only under the old tax regime where stated. Tax laws change. Please confirm with a tax professional.</p>'),
        ('calculators', 'Calculators', '<p>Calculator results are illustrations based on the assumptions you enter. They are not guaranteed and should not be the only basis for a decision.</p>'),
        ('third', 'Third-party websites', '<p>Links to insurers, fund houses, regulators and payment websites are provided for convenience. We don\'t control them and aren\'t responsible for their content.</p>'),
    ]
    legal('disclaimer.html', 'Disclaimer', 'Important information about insurance solicitation, mutual fund market risks, tax and the general nature of the content on the Invest 4U Solutions website.',
          'Important information about insurance, mutual funds and the content of this website.', s)


def grievance():
    s = [
        ('commitment', 'Our commitment', '<p>If something has gone wrong, we want to put it right quickly. You can raise any complaint about our service, a policy or an investment made through us, free of charge.</p>'),
        ('step1', 'Step 1: Contact us', f'''<p>Call or email us with your name, policy or folio number and a short description of the problem.</p>
        {GRIEVANCE_CONTACT}
        <p>We will acknowledge your complaint within [2 working days] and aim to resolve it within [14 days]. <!-- TODO: confirm timelines --></p>'''),
        ('step2', 'Step 2: The insurer or fund house', '<p>If your complaint is about a policy or a scheme, you can also contact the insurer\'s or fund house\'s grievance cell directly. We will help you find the right contact.</p>'),
        ('step3', 'Step 3: Regulators and ombudsman', '''<p>If you are not satisfied with the response, you can escalate:</p>
        <div class="table-wrap">
        <table>
          <thead><tr><th scope="col">For</th><th scope="col">Where to go</th></tr></thead>
          <tbody>
            <tr><td>Insurance complaints</td><td>IRDAI's <a href="https://bimabharosa.irdai.gov.in/" target="_blank" rel="noopener">Bima Bharosa portal<span class="sr-only"> (opens in a new tab)</span></a>, or the <a href="https://www.cioins.co.in/" target="_blank" rel="noopener">Insurance Ombudsman<span class="sr-only"> (opens in a new tab)</span></a> (there is an office in Kochi)</td></tr>
            <tr><td>Mutual fund complaints</td><td>SEBI's <a href="https://scores.sebi.gov.in/" target="_blank" rel="noopener">SCORES portal<span class="sr-only"> (opens in a new tab)</span></a>, and then online dispute resolution through <a href="https://smartodr.in/" target="_blank" rel="noopener">SMART ODR<span class="sr-only"> (opens in a new tab)</span></a></td></tr>
            <tr><td>Personal data</td><td>Our Grievance Officer, then the Data Protection Board of India (see our <a href="privacy-policy.html">Privacy Policy</a>)</td></tr>
          </tbody>
        </table>
        </div>'''),
        ('info', 'What to include', '''<ul>
          <li>Your full name and phone number</li>
          <li>Policy number or mutual fund folio number</li>
          <li>What happened, with dates</li>
          <li>Copies of any relevant documents or messages</li>
        </ul>'''),
    ]
    legal('grievance.html', 'Grievance Redressal', 'How to raise a complaint with Invest 4U Solutions, our Grievance Officer, and how to escalate to IRDAI Bima Bharosa, the Insurance Ombudsman or SEBI SCORES.',
          'How to raise a complaint, and how to escalate it if you are not satisfied.', s)


def not_found():
    body = f'''<main id="main">
  <section class="error-page">
    <div class="container container--narrow">
      <p class="error-page__code" aria-hidden="true">404</p>
      <h1>Sorry, we couldn't find that page</h1>
      <p class="text-muted">The page may have moved, or the link may be wrong. Let's get you back on track.</p>
      <div class="btn-group mt-6">
        <a class="btn btn--lg" href="index.html">Go to the home page</a>
        <a class="btn btn--lg btn--outline" href="contact.html">Contact us</a>
      </div>
      <ul class="link-list">
        <li><a href="services.html">Our services</a></li>
        <li><a href="financial-checkup.html">Free financial checkup</a></li>
        <li><a href="calculators.html">Calculators</a></li>
        <li><a href="pay-online.html">Pay online</a></li>
      </ul>
    </div>
  </section>
</main>'''
    build('404.html', 'Page Not Found', 'The page you were looking for could not be found. Go to the Invest 4U Solutions home page or contact us.',
          body, solid=True, robots='noindex')
    # Resolve assets from the site root so the page works when served for any missing URL (e.g. /a/b/c)
    path = SITE + '404.html'
    html = open(path).read().replace('<meta charset="utf-8">', '<meta charset="utf-8">\n  <!-- Resolve assets from the site root, so this page works when the host serves it for any missing URL (e.g. /a/b/c). -->\n  <base href="/">', 1)
    open(path, 'w').write(html)


if __name__ == '__main__':
    privacy()
    terms()
    disclaimer()
    grievance()
    not_found()
