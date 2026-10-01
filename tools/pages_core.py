"""About, Contact, Financial Checkup, Downloads, Pay Online (dev helper, not deployed)."""
from pages_common import *
from pages_common import _slice
from build_index import ORG

STATS = _slice(INDEX_MAIN, '<section class="stats bg-brand"', '</section>')
CONTACT_GRID = _slice(INDEX_MAIN, '<div class="contact__grid">', '<div class="map"', include_end=False).rstrip()
STYLEGUIDE = open(SRC + 'styleguide-main.html').read()
CHECKUP_FORM = _slice(STYLEGUIDE, '<form class="form contact-form" data-contact-form data-multistep', '</form>').replace('sg-ms-', 'ck-')
CHECKUP_STEPS = _slice(INDEX_MAIN, '<ol class="steps" data-inview>', '</ol>')

WA = f'<a class="btn" href="https://wa.me/919747546614" target="_blank" rel="noopener">{I("whatsapp")} WhatsApp us<span class="sr-only"> (opens in a new tab)</span></a>'


def offices(heading_level=3):
    h = f'h{heading_level}'
    return f'''      <div class="grid grid--2">
        <article class="card office-card" data-aos="fade-up">
          <!-- TODO: confirm the map pin for the head office -->
          <iframe src="https://www.google.com/maps?q=Kannankulangara%2C+Tripunithura%2C+Kochi%2C+Kerala+682301&amp;output=embed" title="Map of the Invest 4U head office in Tripunithura" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
          <div class="office-card__body">
            <span class="badge">Head office</span>
            <{h} class="mt-6">Tripunithura</{h}>
            <address>Vaikkom Road, Kannankulangara, Tripunithura, Kochi, Kerala 682301</address>
            <p class="mt-6">Mon to Sat, 9:00 AM to 6:30 PM · Closed Sunday</p>
            <div class="btn-group">
              <a class="btn btn--sm" href="tel:+919747546614">{I("phone")} Call +91 97475 46614</a>
              <a class="btn btn--sm btn--outline" href="https://www.google.com/maps/dir/?api=1&amp;destination=Kannankulangara%2C+Tripunithura%2C+Kochi" target="_blank" rel="noopener">Get directions<span class="sr-only"> (opens in a new tab)</span></a>
            </div>
          </div>
        </article>
        <article class="card office-card" data-aos="fade-up" data-aos-delay="100">
          <!-- TODO: confirm the map pin for the Infopark branch -->
          <iframe src="https://www.google.com/maps?q=Thapasya+Building%2C+Infopark%2C+Kakkanad%2C+Kochi&amp;output=embed" title="Map of the Invest 4U branch at Infopark, Kakkanad" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
          <div class="office-card__body">
            <span class="badge">Branch</span>
            <{h} class="mt-6">Infopark, Kakkanad</{h}>
            <address>Ground Floor, Thapasya Building, Infopark, Kakkanad, Kochi</address>
            <p class="mt-6">Mon to Sat, 9:00 AM to 6:30 PM · Closed Sunday</p>
            <div class="btn-group">
              <a class="btn btn--sm" href="tel:+919847071373">{I("phone")} Call +91 98470 71373</a>
              <a class="btn btn--sm btn--outline" href="https://www.google.com/maps/dir/?api=1&amp;destination=Thapasya+Building%2C+Infopark%2C+Kakkanad%2C+Kochi" target="_blank" rel="noopener">Get directions<span class="sr-only"> (opens in a new tab)</span></a>
            </div>
          </div>
        </article>
      </div>'''


# ---------------------------------------------------------------- About
def about():
    milestones = [
        ('1992', 'Founded in Tripunithura', 'K.N. Krishnankutty starts advising local families on life insurance from Tripunithura.'),
        ('[Year]', 'Trusted LIC partner', 'Invest 4U builds a long relationship with LIC of India, serving thousands of policyholders.'),
        ('[Year]', 'Beyond life insurance', 'We add health and corporate insurance and mutual funds, so families can plan everything in one place.'),
        ('[Year]', '10,000 clients', 'Our family of clients passes 10,000, almost entirely through word of mouth.'),
        ('[Year]', 'Infopark branch opens', 'A second office at Thapasya Building, Infopark, Kakkanad brings us closer to working professionals and businesses.'),
        ('2025', 'Registered as an LLP', 'The firm is formally registered as K & VK Invest 4U Advisory Services LLP.'),
    ]
    ms = '\n'.join(f'''        <li class="milestone" data-aos="fade-up">
          <span class="milestone__year">{y}</span>
          <h3>{t}</h3>
          <p>{d}</p>
        </li>''' for y, t, d in milestones)
    values = [('handshake', 'Trust', 'We recommend only what we would choose for our own family.'),
              ('eye', 'Transparency', 'Clear costs, clear trade-offs and plain language, always.'),
              ('heart', 'Service first', 'Renewals, revivals and claims matter as much as the first sale.'),
              ('people-group', 'Relationships for life', 'Many of our clients have been with us for decades, and now their children are too.'),
              ('scale-balanced', 'Fair advice', 'We compare options across insurers and fund houses.'),
              ('lock', 'Confidentiality', 'Your financial details stay private and secure.')]
    vc = '\n'.join(f'''        <div class="card feature" data-aos="fade-up"{f' data-aos-delay="{(i % 3) * 100}"' if i % 3 else ''}>
          <span class="icon-circle">{I(ic)}</span>
          <div><h3>{t}</h3><p>{d}</p></div>
        </div>''' for i, (ic, t, d) in enumerate(values))
    team = '\n'.join(f'''        <article class="team-card" data-aos="fade-up"{f' data-aos-delay="{(i - 1) * 100}"' if i > 1 else ''}>
          <div class="team-card__photo bracket"><img src="assets/images/team/team-{i}.webp" alt="Team member {i} (placeholder photo)" width="600" height="700" loading="lazy"></div>
          <h3>[Team member name]</h3>
          <p>[Role]</p>
        </article>''' for i in range(1, 5))

    body = main(
        banner('About Invest 4U Solutions', [('About', None)], 'Guiding families and businesses in Kochi since 1992, with service that lasts a lifetime.', img='about', eyebrow='Financial Architects'),
        f'''  <section class="section" aria-labelledby="story-title">
    <div class="container split">
      <div class="about-collage" data-aos="fade-right">
        <div class="about-collage__main bracket">
          <!-- TODO: replace with a real photo of the office or team -->
          <img src="assets/images/about-2.webp" alt="The Invest 4U office (placeholder image)" width="800" height="900" loading="lazy">
        </div>
        <div class="about-collage__sub" data-aos="zoom-in" data-aos-delay="250">
          <img src="assets/images/about-1.webp" alt="An advisor meeting clients (placeholder image)" width="800" height="600" loading="lazy">
        </div>
        <div class="about-collage__badge" data-aos="zoom-in" data-aos-delay="400"><div><strong>1992</strong>where our story began</div></div>
      </div>
      <div data-aos="fade-left">
        <span class="eyebrow">Our story</span>
        <h2 id="story-title">Three decades of trust, one family at a time</h2>
        <p>Invest 4U began in 1992 in Tripunithura, when our founder K.N. Krishnankutty started helping neighbours and friends protect their families with life insurance. Word spread, and a small practice became one of the area's most trusted names for insurance advice.</p>
        <p>Over the years we have been a trusted partner of LIC of India and have added health and corporate insurance, mutual funds and long-term financial planning, so our clients can look after everything in one place. Today we serve more than 10,000 clients from two offices, in Tripunithura and at Infopark, Kakkanad.</p>
        <p>In 2025 we formally registered as K &amp; VK Invest 4U Advisory Services LLP. What hasn't changed is our approach: service first, time-tested solutions for short and long-term goals, and support long after the paperwork is done.</p>
      </div>
    </div>
  </section>''',
        STATS,
        f'''  <section class="section" aria-labelledby="milestones-title">
    <div class="container">
      <div class="section-head" data-aos="fade-up">
        <span class="eyebrow">Our journey</span>
        <h2 id="milestones-title">Milestones since 1992</h2>
        <p class="placeholder-note">TODO: client to confirm the years shown as [Year]</p>
      </div>
      <ol class="milestones">
{ms}
      </ol>
    </div>
  </section>''',
        f'''  <section class="section bg-alt" aria-labelledby="mv-title">
    <div class="container">
      <h2 id="mv-title" class="sr-only">Mission and vision</h2>
      <div class="grid grid--2">
        <div class="mv-card mv-card--mission" data-aos="fade-right">
          <span class="icon-circle">{I("bullseye")}</span>
          <h3>Our mission</h3>
          <p>To make every family we serve financially secure, through honest advice, the right protection and service that lasts a lifetime.</p>
        </div>
        <div class="mv-card mv-card--vision" data-aos="fade-left">
          <span class="icon-circle">{I("eye")}</span>
          <h3>Our vision</h3>
          <p>To be Kochi's most trusted financial architects: the first call a family makes when they want to protect what they have and plan for what they want.</p>
        </div>
      </div>
    </div>
  </section>''',
        f'''  <section class="section" aria-labelledby="values-title">
    <div class="container">
      <div class="section-head" data-aos="fade-up">
        <span class="eyebrow">What we stand for</span>
        <h2 id="values-title">Our core values</h2>
      </div>
      <div class="grid grid--3">
{vc}
      </div>
    </div>
  </section>''',
        f'''  <section class="section founder bg-dark" id="founder" aria-labelledby="founder-title">
    <div class="container founder__grid">
      {FOUNDER_PHOTO}

      <figure class="founder__quote" data-aos="fade-left">
        <span class="eyebrow">Message from the Founder</span>
        <h2 id="founder-title">K.N. Krishnankutty, Founder &amp; Managing Director</h2>
        <div class="founder__quote-mark">{I("quote-left")}</div>
        <!-- TODO: DRAFT message written for layout. The client must review, edit and approve it before launch. -->
        <blockquote>
          <p>When I started advising families in Tripunithura in 1992, I made a simple promise: treat every client's money as carefully as my own. Three decades later, that promise still guides everything we do.</p>
          <p>We have sat with families as they bought their first policy, planned their children's education and prepared for retirement, and we have stood beside them when they needed to make a claim. Those moments, when a policy we recommended years earlier finally does its job, are why we do this work.</p>
          <p>Today a new generation, many of them the children of our first clients, trusts us with their plans. Our mission is unchanged: to help every family we serve become financially secure, through honest advice and service that lasts a lifetime. Thank you for your trust.</p>
        </blockquote>
        <p class="placeholder-note">Draft message: awaiting approval from the founder</p>
        {FOUNDER_SIGN}
      </figure>
    </div>
  </section>''',
        f'''  <section class="section" aria-labelledby="team-title">
    <div class="container">
      <div class="section-head" data-aos="fade-up">
        <span class="eyebrow">Our team</span>
        <h2 id="team-title">The people behind Invest 4U</h2>
        <p class="placeholder-note">TODO: add team photos, names and roles</p>
      </div>
      <div class="grid grid--4">
{team}
      </div>
    </div>
  </section>''',
        f'''  <section class="section bg-alt" aria-labelledby="awards-title">
    <div class="container">
      <div class="section-head" data-aos="fade-up">
        <span class="eyebrow">Awards &amp; Recognition</span>
        <h2 id="awards-title">Recognised for service and performance</h2>
      </div>
      {AWARDS_GRID}
    </div>
  </section>''',
        f'''  <section class="section" aria-labelledby="offices-title">
    <div class="container">
      <div class="section-head" data-aos="fade-up">
        <span class="eyebrow">Visit us</span>
        <h2 id="offices-title">Our offices</h2>
      </div>
{offices()}
    </div>
  </section>''',
        f'''  <section class="section bg-alt" aria-labelledby="reg-title">
    <div class="container container--narrow">
      <div class="section-head" data-aos="fade-up">
        <span class="eyebrow">Registrations</span>
        <h2 id="reg-title">Regulatory information</h2>
      </div>
      {REG_LIST}
    </div>
  </section>''',
        cta_band(),
        extra_after=LIGHTBOX,
    )
    page('about.html', 'About Us', 'Invest 4U Solutions has guided families in Kochi since 1992. Meet our founder K.N. Krishnankutty, our team, our values and our two offices.',
         body, current='about.html', banner_img='about')


# ---------------------------------------------------------------- Contact
CONTACT_FAQS = [
    ('How quickly will you reply?', '<p>We reply to messages within one working day. For anything urgent, call +91 97475 46614 during office hours.</p>'),
    ('Can you visit me at home or at work?', '<p>Yes. We offer doorstep service across Kochi. Mention a convenient time in your message or when you call.</p>'),
    ('Do you charge for a consultation?', '<p>No. Your first consultation and our <a href="financial-checkup.html">financial checkup</a> are free, with no obligation.</p>'),
    ('What should I bring to a meeting?', '<p>Any existing policy documents, mutual fund statements and a rough idea of your monthly expenses and goals. Don\'t worry if you don\'t have everything.</p>'),
    ('I need help with a claim. Who do I contact?', '<p>Call us or email <a href="mailto:service@invest4u.in">service@invest4u.in</a> with your policy number, and we\'ll guide you through the next steps.</p>'),
]


def contact():
    body = main(
        banner('Contact Us', [('Contact', None)], 'Call, WhatsApp, email or visit one of our offices. An advisor will get back to you within one working day.', img='contact'),
        f'''  <section class="section section--sm bg-navy" aria-label="Quick contact">
    <div class="container cta-band__inner">
      <div>
        <h2 class="mt-0">Prefer to talk now?</h2>
        <p>We're available Monday to Saturday, 9:00 AM to 6:30 PM.</p>
      </div>
      <div class="btn-group">
        <a class="btn btn--lg" href="tel:+919747546614">{I("phone")} Call +91 97475 46614</a>
        {WA.replace('class="btn"', 'class="btn btn--lg btn--outline-white"')}
      </div>
    </div>
  </section>''',
        f'''  <section class="section bg-alt" id="contact" aria-labelledby="contact-title">
    <div class="container">
      <div class="section-head" data-aos="fade-up">
        <span class="eyebrow">Get in touch</span>
        <h2 id="contact-title">Talk to an advisor</h2>
        <p>Tell us a little about what you need and we'll call you back at a time that suits you.</p>
      </div>
      {CONTACT_GRID}
    </div>
  </section>''',
        f'''  <section class="section" aria-labelledby="offices-title">
    <div class="container">
      <div class="section-head" data-aos="fade-up">
        <span class="eyebrow">Visit us</span>
        <h2 id="offices-title">Our offices</h2>
      </div>
{offices()}
    </div>
  </section>''',
        faq(CONTACT_FAQS, 'faq', heading='Questions before you get in touch'),
        cta_band(),
    )
    page('contact.html', 'Contact Us', 'Contact Invest 4U Solutions in Tripunithura and Infopark, Kochi. Call +91 97475 46614, WhatsApp, email info@invest4u.in or send us a message.',
         body, current='contact.html', banner_img='contact', jsonld=ORG)


# ---------------------------------------------------------------- Financial checkup
def checkup():
    gets = [('shield', 'Protection gaps', 'Whether your life and health cover would really be enough.'),
            ('layer-group', 'Overlaps and waste', 'Policies or funds that duplicate each other or no longer fit.'),
            ('bullseye', 'Goal check', 'Whether you\'re on track for education, retirement and other goals.'),
            ('file-invoice-dollar', 'Tax savings', 'Deductions you may be missing under 80C and 80D.'),
            ('file-signature', 'Nominations', 'Whether every policy and investment has an up-to-date nominee.'),
            ('route', 'A clear action list', 'Simple, prioritised next steps, with no obligation to buy.')]
    gl = '\n'.join(f'''        <li class="benefit" data-aos="fade-up"{' data-aos-delay="100"' if i % 2 else ''}>
          <span class="icon-circle">{I(ic)}</span>
          <div><h3>{t}</h3><p>{d}</p></div>
        </li>''' for i, (ic, t, d) in enumerate(gets))
    faqs = [('Is the checkup really free?', '<p>Yes. There is no fee and no obligation to buy anything.</p>'),
            ('How long does it take?', '<p>About 30 to 45 minutes, at our office, at your home or over a video call.</p>'),
            ('What should I bring?', '<p>Your existing policy documents, recent mutual fund statements and a rough idea of your monthly expenses. If you don\'t have them all, we can still start.</p>'),
            ('Will you share my details with anyone?', '<p>No. We use your details only to prepare your checkup and contact you. See our <a href="privacy-policy.html">Privacy Policy</a>.</p>')]
    body = main(
        banner('Free Financial Health Checkup', [('Free Financial Checkup', None)], 'In one friendly conversation, see where you stand on protection, savings and tax, and get a clear plan. Free, with no obligation.', img='financial-checkup'),
        f'''  <section class="section" aria-labelledby="gets-title">
    <div class="container">
      <div class="section-head" data-aos="fade-up">
        <span class="eyebrow">What you get</span>
        <h2 id="gets-title">A complete picture of your finances</h2>
      </div>
      <ul class="benefits">
{gl}
      </ul>
    </div>
  </section>''',
        f'''  <section class="section bg-tint" aria-labelledby="process-title">
    <div class="container">
      <div class="checkup-card" data-aos="zoom-in">
        <div>
          <span class="eyebrow">How it works</span>
          <h2 id="process-title">Three simple steps</h2>
          <p>No jargon and no pressure. Just an honest look at where you are and what to do next.</p>
        </div>
        <div>
          {CHECKUP_STEPS}
        </div>
      </div>
    </div>
  </section>''',
        f'''  <section class="section bg-alt" id="book" aria-labelledby="book-title">
    <div class="container container--narrow">
      <div class="section-head" data-aos="fade-up">
        <span class="eyebrow">Book your checkup</span>
        <h2 id="book-title">Request your free checkup</h2>
        <p>Three short steps. We'll call you within one working day to fix a time.</p>
      </div>
      <!-- TODO: set the Web3Forms access key in data-access-key -->
      {CHECKUP_FORM}
    </div>
  </section>''',
        faq(faqs, 'faq', heading='Checkup questions', bg=''),
        cta_band('Prefer to talk first?', 'Call or WhatsApp us and we\'ll answer any questions before you book.'),
    )
    page('financial-checkup.html', 'Free Financial Health Checkup', 'Book a free financial health checkup with Invest 4U in Kochi: review your insurance, savings, goals and tax in one conversation, with no obligation.',
         body, banner_img='financial-checkup')


# ---------------------------------------------------------------- Downloads
LOGOS = {'lic': ('lic.webp', 150, 83), 'star-health': ('star-health.webp', 203, 89), 'icici-lombard': ('icici-lombard.webp', 247, 89),
         'united-india': ('united-india.webp', 185, 89), 'national-insurance': ('national-insurance.webp', 191, 89), 'cams': ('cams.svg', 500, 176)}
DOWNLOADS = [
    ('united-india', 'United India Insurance', 'https://uiic.co.in/', ['Health claim forms', 'Motor claim forms', 'Proposal and KYC forms']),
    ('icici-lombard', 'ICICI Lombard', 'https://www.icicilombard.com/', ['Health claim forms', 'Motor claim forms', 'Travel claim forms']),
    ('national-insurance', 'National Insurance', 'https://nationalinsurance.nic.co.in/', ['Health claim forms', 'Motor claim forms', 'Property claim forms']),
    ('lic', 'LIC of India', 'https://licindia.in/', ['Death and maturity claim forms', 'Nomination and assignment forms', 'Policy revival and loan forms']),
    ('star-health', 'Star Health', 'https://www.starhealth.in/', ['Claim form (Part A and B)', 'Pre-authorisation form', 'Portability form']),
    ('cams', 'CAMS (mutual funds)', 'https://www.camsonline.com/Investors/Service-requests/Download-Forms', ['Transaction slips', 'Change of bank or address', 'Nomination forms']),
]


def downloads():
    cards = '\n'.join(f'''        <article class="card download-card" data-aos="fade-up"{f' data-aos-delay="{(i % 3) * 100}"' if i % 3 else ''}>
          <div class="download-card__logo"><img src="assets/images/partners/{LOGOS[slug][0]}" alt="{name}" width="{LOGOS[slug][1]}" height="{LOGOS[slug][2]}" loading="lazy"></div>
          <h3>{name}</h3>
          <ul>
            {''.join(f'<li>{I("file-arrow-down")} {f}</li>' for f in forms)}
          </ul>
          <!-- TODO: replace with the exact claim-forms page URL for {name} once confirmed -->
          <a class="btn btn--sm" href="{url}" target="_blank" rel="noopener">Official forms {I("arrow-up-right-from-square")}<span class="sr-only"> for {name} (opens in a new tab)</span></a>
        </article>''' for i, (slug, name, url, forms) in enumerate(DOWNLOADS))
    body = main(
        banner('Downloads', [('Downloads', None)], 'Claim, service and transaction forms from our insurance and mutual fund partners, straight from their official websites.', img='downloads'),
        f'''  <section class="section bg-alt" aria-labelledby="dl-title">
    <div class="container">
      <div class="section-head" data-aos="fade-up">
        <span class="eyebrow">Forms</span>
        <h2 id="dl-title">Claim and service forms</h2>
        <p>Each link opens the partner's official website in a new tab, so you always get the latest version.</p>
      </div>
      <div class="grid grid--3">
{cards}
      </div>
      <div class="notice mt-6" data-aos="fade-up">{I("hand-holding-medical")}<p><strong>Need help with a form or a claim?</strong> Call us on <a href="tel:+919747546614">+91 97475 46614</a> or email <a href="mailto:service@invest4u.in">service@invest4u.in</a>. We'll tell you exactly which form you need and help you fill it in.</p></div>
    </div>
  </section>''',
        cta_band(),
    )
    page('downloads.html', 'Downloads: Claim & Service Forms', 'Download claim and service forms for LIC, Star Health, ICICI Lombard, United India, National Insurance and CAMS from their official websites.',
         body, current='downloads.html', banner_img='downloads')


# ---------------------------------------------------------------- Pay online
def copy_row(label, value, aria, vid=None):
    return f'''            <div class="copy-row">
              <dt>{label}</dt>
              <dd><span class="copy-row__value"{f' id="{vid}"' if vid else ''}>{value}</span> <button class="copy-btn" type="button" data-copy="{value}" aria-label="Copy {aria}">{I("copy")}<span class="copy-btn__label">Copy</span></button></dd>
            </div>'''


def pay_online():
    body = main(
        banner('Pay Online', [('Pay Online', None)], 'Pay your premium or investment safely using one of the verified options below.', img='pay-online'),
        f'''  <section class="section" aria-labelledby="fraud-title">
    <div class="container container--narrow">
      <div class="fraud-notice" role="note" data-aos="fade-up">
        <h2 id="fraud-title">{I("triangle-exclamation")} Stay safe from payment fraud</h2>
        <p><strong>We accept payments only to the accounts listed on this page. We never ask for OTPs or payments to personal numbers.</strong></p>
        <p class="mt-0">Verify by calling <a href="tel:+919747546614">+91 97475 46614</a> before you pay if anything looks unusual.</p>
      </div>
    </div>
  </section>''',
        f'''  <section class="section bg-alt" aria-labelledby="options-title">
    <div class="container">
      <div class="section-head" data-aos="fade-up">
        <span class="eyebrow">Payment options</span>
        <h2 id="options-title">Choose how to pay</h2>
      </div>
      <div class="grid grid--3">
        <article class="card pay-card" data-aos="fade-up">
          <div class="pay-card__head"><span class="icon-circle">{I("umbrella")}</span><h3>LIC premium</h3></div>
          <p>Pay LIC premiums directly on LIC of India's official website using net banking, card or UPI. You'll get an instant receipt from LIC.</p>
          <ul class="tick-list">
            <li>Keep your policy number and date of birth ready</li>
            <li>Only use the official licindia.in website</li>
          </ul>
          <!-- TODO: link directly to LIC's official "Pay Direct" page once confirmed -->
          <a class="btn btn--block" href="https://licindia.in/" target="_blank" rel="noopener">Go to LIC's official site {I("arrow-up-right-from-square")}<span class="sr-only"> (opens in a new tab)</span></a>
        </article>

        <article class="card pay-card" data-aos="fade-up" data-aos-delay="100">
          <div class="pay-card__head"><span class="icon-circle">{I("building-columns")}</span><h3>Bank transfer</h3></div>
          <p>NEFT, RTGS or IMPS to our current account.</p>
          <!-- TODO: client to provide and verify every bank detail below -->
          <dl class="copy-list">
{copy_row('Account name', 'K &amp; VK Invest 4U Advisory Services LLP', 'account name')}
{copy_row('Account number', '[TO BE PROVIDED]', 'account number')}
{copy_row('Bank', '[TO BE PROVIDED]', 'bank name')}
{copy_row('Branch', '[TO BE PROVIDED]', 'branch')}
{copy_row('IFSC', '[TO BE PROVIDED]', 'IFSC code')}
          </dl>
        </article>

        <article class="card pay-card" data-aos="fade-up" data-aos-delay="200">
          <div class="pay-card__head"><span class="icon-circle">{I("qrcode")}</span><h3>UPI / Google Pay</h3></div>
          <p>Scan the QR code or pay to our UPI ID from any UPI app.</p>
          <!-- TODO: client to provide the verified UPI ID and QR image (linked to +91 97475 46614 or the LLP account only) -->
          <dl class="copy-list">
{copy_row('UPI ID', '[TO BE PROVIDED]', 'UPI ID')}
{copy_row('UPI number', '+91 97475 46614', 'UPI number')}
          </dl>
          <div class="qr" role="img" aria-label="UPI QR code placeholder">QR code<br>[TO BE PROVIDED]</div>
        </article>
      </div>
    </div>
  </section>''',
        f'''  <section class="section" aria-labelledby="after-title">
    <div class="container container--narrow">
      <div class="section-head" data-aos="fade-up">
        <span class="eyebrow">After you pay</span>
        <h2 id="after-title">Get your receipt</h2>
      </div>
      <ol class="timeline" data-inview>
        <li class="timeline__line" aria-hidden="true"></li>
        <li class="timeline__step" data-aos="fade-up"><span class="timeline__num" aria-hidden="true">01</span><div><h3>Pay</h3><p>Use one of the verified options above.</p></div></li>
        <li class="timeline__step" data-aos="fade-up" data-aos-delay="150"><span class="timeline__num" aria-hidden="true">02</span><div><h3>Share proof</h3><p>Send the screenshot or transaction ID on WhatsApp to +91 97475 46614.</p></div></li>
        <li class="timeline__step" data-aos="fade-up" data-aos-delay="300"><span class="timeline__num" aria-hidden="true">03</span><div><h3>Receipt</h3><p>We confirm and send your receipt within one working day.</p></div></li>
        <li class="timeline__step" data-aos="fade-up" data-aos-delay="450"><span class="timeline__num" aria-hidden="true">04</span><div><h3>Questions?</h3><p>Call us any time during office hours.</p></div></li>
      </ol>
    </div>
  </section>''',
        cta_band(),
    )
    page('pay-online.html', 'Pay Online', 'Pay your LIC premium or investment safely: verified LIC payment link, bank transfer and UPI details for K & VK Invest 4U Advisory Services LLP.',
         body, current='pay-online.html', banner_img='pay-online')


if __name__ == '__main__':
    about()
    contact()
    checkup()
    downloads()
    pay_online()
