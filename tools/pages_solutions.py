"""'Solutions For' audience pages (dev helper, not deployed).
Each page explains an audience's insurance, investment and planning needs in simple terms,
linking every need to the relevant service page or calculator."""
from pages_common import *

# (slug, menu label, title, icon, banner, lead, desc, intro, needs{protect, invest, plan}, steps, faqs, flags)
# needs: list of (need, plain explanation, link, link text)
AUDIENCES = [
  dict(slug='for-families', label='For Families', title='Financial Solutions for Families', icon='people-roof', img='services',
       lead='Protect the people you love today, and build towards the goals you share for tomorrow.',
       desc='Financial planning for families in Kochi: life and health insurance, SIPs for family goals, children\'s education and retirement planning, explained simply.',
       intro=['Every family juggles today\'s expenses with tomorrow\'s goals: a home, the children\'s education, a comfortable retirement. A sudden illness or the loss of an income can upset all of it.',
              'We help families put the essentials in place first, protection for the people who depend on you, and then build steady savings towards each goal.'],
       protect=[('Life cover for the earning members', 'If something happens to you, your family keeps its income, home and plans.', 'term-insurance.html', 'Term insurance'),
                ('Health cover for everyone', 'One family floater policy pays hospital bills for the whole family.', 'health-insurance.html', 'Health insurance'),
                ('Your home and vehicle', 'Cover against fire, theft, floods and accidents.', 'general-insurance.html', 'General insurance')],
       invest=[('Regular saving with a SIP', 'A fixed amount each month, growing towards your family\'s goals.', 'sip-investment.html', 'SIP investment'),
               ('An emergency fund', 'Three to six months of expenses kept somewhere safe and easy to reach.', 'mutual-funds.html', 'Liquid funds'),
               ('Tax-saving that fits your goals', 'Use Section 80C and 80D deductions on investments you would want anyway.', 'tax-planning.html', 'Tax planning')],
       plan=[('Children\'s education', 'Put a figure on future fees and save steadily to meet them.', 'child-education.html', 'Child education planning'),
             ('Retirement', 'Make sure you never have to depend on your children.', 'retirement-planning.html', 'Retirement planning'),
             ('Nominations and a will', 'So everything you have built reaches your family smoothly.', 'estate-planning.html', 'Estate planning')],
       faqs=[('Where should a family start?', '<p>With protection: adequate life cover for each earning member and health cover for everyone. Then an emergency fund, then saving for goals.</p>'),
             ('How much life cover does our family need?', '<p>Usually 10 to 15 times the annual income of each earning member, plus loans. Try our <a href="life-cover-calculator.html">life cover calculator</a>.</p>'),
             ('Is a family floater better than separate policies?', '<p>For young families a floater is usually more affordable. Older parents are often better covered by a separate policy. We will compare both for you.</p>')]),

  dict(slug='for-nris', label='For NRIs', title='Financial Solutions for NRIs', icon='earth-asia', img='contact',
       lead='Invest in India and look after your family back home, from wherever you live.',
       desc='Financial services for NRIs from Kochi: mutual fund investments in India, life and health cover for family, and help managing policies and assets remotely.',
       intro=['Living abroad, you may want to invest in India, support parents at home and keep your Indian policies and assets in order, without flying back for every form.',
              'We work with NRI clients by phone, WhatsApp and video call, help with KYC and paperwork, and act as your trusted point of contact in Kochi.'],
       protect=[('Health cover for parents in India', 'Medical costs for ageing parents can be large; the right policy protects your savings.', 'health-insurance.html', 'Health insurance'),
                ('Life cover for your family', 'Make sure dependants in India are protected if something happens to you.', 'term-insurance.html', 'Term insurance'),
                ('Servicing existing LIC policies', 'Premiums, revivals, nominations and claims handled for you.', 'life-insurance.html', 'Life insurance')],
       invest=[('Mutual funds in India', 'Invest through your NRE or NRO account after completing NRI KYC.', 'mutual-funds.html', 'Mutual funds'),
               ('Monthly SIPs from abroad', 'Build wealth in India steadily, in rupees.', 'sip-investment.html', 'SIP investment'),
               ('Long-term wealth in India', 'A plan for the money you intend to use when you return or retire.', 'wealth-creation.html', 'Wealth creation')],
       plan=[('Return-to-India planning', 'A corpus and income plan for when you come home.', 'retirement-planning.html', 'Retirement planning'),
             ('Children\'s education', 'In India or abroad, planned in the right currency.', 'child-education.html', 'Child education planning'),
             ('Assets and nominations in India', 'Keep property, policies and investments in order for your family.', 'estate-planning.html', 'Estate planning')],
       faqs=[('Can NRIs invest in Indian mutual funds?', '<p>Yes, through an NRE or NRO bank account once NRI KYC is complete. Some fund houses restrict investments from residents of certain countries, such as the US and Canada, so we check which schemes are open to you.</p>'),
             ('Do I need to visit India to invest?', '<p>Usually not. Most paperwork, KYC and transactions can be done online or by courier. We guide you through each step.</p>'),
             ('How are my investments taxed?', '<p>Tax depends on the investment, the type of account and the tax treaty with your country of residence. Please confirm with a chartered accountant; we can work alongside yours.</p>')],
       note='Rules for NRI investments, repatriation and tax change from time to time and depend on your country of residence. This page is general information, not tax advice.'),

  dict(slug='for-business-owners', label='For Business Owners', title='Financial Solutions for Business Owners', icon='briefcase', img='financial-checkup',
       lead='Protect your business, your family and your own future, all of which depend on you.',
       desc='Financial planning for business owners in Kochi: shop and key-person insurance, personal cover, retirement planning without a pension, tax planning and succession.',
       intro=['As a business owner, your business and your family both depend on you. You may have no employer pension, no group health cover and an income that varies year to year.',
              'We help you protect the business and your family, build personal wealth outside the business, and plan for the day you hand it on.'],
       protect=[('Your premises, stock and equipment', 'Cover against fire, theft and other damage.', 'general-insurance.html', 'Shop and office insurance'),
                ('Key-person and partnership cover', 'Money for the business if you or a partner can no longer work.', 'succession-planning.html', 'Succession planning'),
                ('Personal life and health cover', 'Protection for your family that does not depend on the business.', 'term-insurance.html', 'Term insurance')],
       invest=[('Wealth outside the business', 'Do not keep everything in one basket; build personal investments too.', 'wealth-creation.html', 'Wealth creation'),
               ('SIPs that fit uneven income', 'Start with a comfortable amount and add lump sums in good years.', 'sip-investment.html', 'SIP investment'),
               ('Tax planning', 'Use the deductions available to you, and choose the right regime.', 'tax-planning.html', 'Tax planning')],
       plan=[('Your own retirement', 'No pension means you need a plan of your own.', 'retirement-planning.html', 'Retirement planning'),
             ('Succession', 'Who takes over the business, and how it is funded.', 'succession-planning.html', 'Succession planning'),
             ('Estate planning', 'Clear nominations and a will so your family is not left in difficulty.', 'estate-planning.html', 'Estate planning')],
       faqs=[('Is business insurance expensive?', '<p>Basic cover for premises, stock and liability is often affordable compared with the loss it protects against. We compare quotes from several insurers.</p>'),
             ('What is key-person insurance?', '<p>A life policy taken by the business on someone it depends on, so it receives money to cope if that person dies.</p>'),
             ('How do I plan for retirement with an uneven income?', '<p>Set a base SIP you can always afford and top it up with lump sums in good years. Our <a href="retirement-calculator.html">retirement calculator</a> helps you find the target.</p>')]),

  dict(slug='for-corporates', label='For Corporate Companies', title='Financial Solutions for Corporate Companies', icon='building', img='about',
       lead='Protect your organisation and look after your people, with one partner for every policy.',
       desc='Corporate insurance and employee benefits from our Infopark, Kochi branch: group health, group term life, property, liability and key-person cover.',
       intro=['Companies need protection for their assets and operations, and attractive benefits to hire and keep good people. Managing many policies and renewals takes time away from running the business.',
              'From our branch at Infopark, Kakkanad, we design, place and service corporate insurance and employee benefits, and support your HR team with every claim.'],
       protect=[('Property, assets and operations', 'Fire, machinery, stock and business interruption cover.', 'corporate-insurance.html', 'Corporate insurance'),
                ('Liability', 'Protection against claims from customers, visitors and third parties.', 'corporate-insurance.html', 'Liability cover'),
                ('Key people', 'Cover for the founders and leaders the company depends on.', 'succession-planning.html', 'Key-person insurance')],
       invest=[('Group health insurance', 'Hospital cover for employees and their families, a valued benefit.', 'corporate-insurance.html', 'Group health'),
               ('Group term life', 'Low-cost life cover for your whole team under one policy.', 'corporate-insurance.html', 'Group term life'),
               ('Investment awareness for employees', 'Sessions that help your team understand SIPs, tax and protection.', 'contact.html?service=corporate-insurance', 'Ask us about a session')],
       plan=[('One partner for renewals', 'All policies tracked and renewed on time.', 'corporate-insurance.html', 'Corporate insurance'),
             ('Claims support for HR', 'We handle insurer follow-ups so your team does not have to.', 'corporate-insurance.html', 'Claim support'),
             ('Annual cover review', 'Cover updated as your headcount, premises and contracts change.', 'contact.html?service=corporate-insurance', 'Book a review')],
       invest_title='Employee benefits',
       plan_title='Ongoing service',
       faqs=[('Can group health cover include employees\' families?', '<p>Yes. Most group policies can cover spouses and children, and sometimes parents.</p>'),
             ('How quickly can group cover be set up?', '<p>Usually within a few working days once the employee data and proposal are ready.</p>'),
             ('Do you work with start-ups?', '<p>Yes. We help growing teams start with essential cover and add to it as they grow.</p>')]),

  dict(slug='for-parents', label='For Parents', title='Financial Solutions for Parents', icon='children', img='blog',
       lead='Give your children the best start, and make sure they are protected whatever happens.',
       desc='Financial planning for parents in Kochi: life and health cover, children\'s education and marriage planning, Sukanya Samriddhi and SIPs for your child\'s future.',
       intro=['Becoming a parent changes your financial priorities overnight. You want to give your children every opportunity, and make sure they are looked after even if you are not there.',
              'We help parents protect their family, put a figure on education and other big goals, and start saving early so the money is there on time.'],
       protect=[('Life cover sized to your children\'s needs', 'Enough to cover their upbringing and education if something happens to you.', 'term-insurance.html', 'Term insurance'),
                ('Health cover including the children', 'A family floater that covers hospital bills for everyone.', 'health-insurance.html', 'Health insurance'),
                ('Plans that continue without you', 'Child plans with waiver of premium keep paying into the goal.', 'child-education.html', 'Child plans')],
       invest=[('A SIP for each child', 'Start early: small monthly amounts grow significantly over 15 years or more.', 'sip-investment.html', 'SIP investment'),
               ('Sukanya Samriddhi Yojana for daughters', 'A government-backed savings scheme with tax benefits.', 'sukanya-samriddhi-yojana-calculator.html', 'SSY calculator'),
               ('Education goal calculator', 'See what a course may cost by the time your child needs it.', 'child-education-calculator.html', 'Education calculator')],
       plan=[('Higher education', 'In India or abroad, planned with rising fees in mind.', 'child-education.html', 'Child education planning'),
             ('Marriage', 'A dedicated fund so you do not need loans later.', 'marriage-planning.html', 'Marriage planning'),
             ('Guardianship and a will', 'Decide who would look after your children and their money.', 'estate-planning.html', 'Estate planning')],
       faqs=[('When should we start saving for our child?', '<p>As early as possible. Starting when a child is born gives 15 to 18 years for savings to grow, so the monthly amount needed is much smaller.</p>'),
             ('Is Sukanya Samriddhi better than mutual funds?', '<p>They do different jobs: SSY offers government-backed, tax-free returns; equity funds can grow more over long periods but go up and down. Many parents use both.</p>'),
             ('Why do parents need a will?', '<p>A will lets you name a guardian for your children and decide how your assets are used for them. A lawyer can help you prepare one.</p>')]),

  dict(slug='for-young-professionals', label='For Young Professionals', title='Financial Solutions for Young Professionals', icon='user-graduate', img='calculators',
       lead='Start early, build good habits and let time do the heavy lifting.',
       desc='Financial planning for young professionals in Kochi: start a SIP, get your own health and term cover, save tax smartly and plan goals like a home or travel.',
       intro=['Your first years of earning are the best time to build good money habits. Time is your biggest advantage: money invested in your twenties has decades to grow.',
              'We help you set up the basics, an emergency fund, your own health cover and a monthly SIP, and plan for goals like a home, travel or further studies.'],
       protect=[('Your own health insurance', 'Group cover from work ends when you change jobs; a personal policy stays with you.', 'health-insurance.html', 'Health insurance'),
                ('Term cover once someone depends on you', 'Premiums are lowest when you are young and healthy.', 'term-insurance.html', 'Term insurance'),
                ('An emergency fund', 'Three to six months of expenses, kept safe and easy to reach.', 'mutual-funds.html', 'Liquid funds')],
       invest=[('Start a SIP early', 'Even a small monthly amount grows significantly over decades.', 'sip-investment.html', 'SIP investment'),
               ('Step it up each year', 'Increase your SIP with every pay rise.', 'step-up-sip-calculator.html', 'Step-up SIP calculator'),
               ('Smart tax saving', 'Choose the right regime and investments that suit your goals.', 'tax-planning.html', 'Tax planning')],
       plan=[('Your goals', 'A home, a car, travel or further studies, each with a number and a date.', 'goal-based-planning.html', 'Goal-based planning'),
             ('Retirement, early', 'Starting in your twenties makes retirement far easier to fund.', 'retirement-calculator.html', 'Retirement calculator'),
             ('Avoiding debt traps', 'Use credit cards and loans wisely while you build savings.', 'financial-checkup.html', 'Free financial checkup')],
       faqs=[('I have just started working. What should I do first?', '<p>Build an emergency fund, take a personal health policy and start a SIP, even a small one. Add term cover once someone depends on your income.</p>'),
             ('Is my company\'s health cover enough?', '<p>It usually ends when you leave the job and may be small. A personal policy, bought while you are young and healthy, protects you between jobs.</p>'),
             ('How much should I invest each month?', '<p>A common guideline is to save at least 20% of your take-home pay. Our <a href="sip-calculator.html">SIP calculator</a> shows what different amounts could grow to.</p>')]),
]


def need_cards(items):
    return '\n'.join(f'''            <li class="need">
              <h4>{n}</h4>
              <p>{d}</p>
              <a class="link-arrow" href="{u}">{t} {I("arrow-right")}</a>
            </li>''' for n, d, u, t in items)


def audience_page(a):
    intro = '\n          '.join(f'<p>{p}</p>' for p in a['intro'])
    cols = [('shield-heart', 'Protection', a['protect']),
            ('seedling', a.get('invest_title', 'Investment'), a['invest']),
            ('route', a.get('plan_title', 'Planning'), a['plan'])]
    columns = '\n'.join(f'''        <div class="needs-col" data-aos="fade-up"{f' data-aos-delay="{i * 100}"' if i else ''}>
          <h3 class="needs-col__title"><span class="needs-col__icon">{I(ic)}</span>{t}</h3>
          <ul class="needs-list">
{need_cards(items)}
          </ul>
        </div>''' for i, (ic, t, items) in enumerate(cols))
    note = f'\n      <div class="notice mt-6">{I("shield")}<p>{a["note"]}</p></div>' if a.get('note') else ''
    others = '\n'.join(f'          <li><a href="{x["slug"]}.html">{x["label"]}</a></li>' for x in AUDIENCES if x['slug'] != a['slug'])
    body = main(
        banner(a['title'], [('Solutions', None), (a['label'], None)][1:], a['lead'], img=a['img'], eyebrow='Solutions For'),
        f'''  <section class="section" aria-labelledby="intro-title">
    <div class="container container--narrow text-center" data-aos="fade-up">
      <span class="eyebrow">{a['label']}</span>
      <h2 id="intro-title">Your money, in simple terms</h2>
      <div class="solution-intro">
          {intro}
      </div>
    </div>
  </section>''',
        f'''  <section class="section bg-alt" aria-labelledby="needs-title">
    <div class="container">
      <div class="section-head" data-aos="fade-up">
        <span class="eyebrow">What you need</span>
        <h2 id="needs-title">Your insurance, investment and planning needs</h2>
        <p>Each item links to a page that explains it in more detail.</p>
      </div>
      <div class="needs-grid">
{columns}
      </div>{note}
      <div class="mt-6">{MF_RISK}</div>
    </div>
  </section>''',
        f'''  <section class="section" aria-labelledby="how-title">
    <div class="container">
      <div class="section-head" data-aos="fade-up">
        <span class="eyebrow">How can Invest 4U help?</span>
        <h2 id="how-title">Consultation, comparison, planning and ongoing support</h2>
      </div>
      <ol class="timeline" data-inview>
        <li class="timeline__line" aria-hidden="true"></li>
        <li class="timeline__step" data-aos="fade-up"><span class="timeline__num" aria-hidden="true">01</span><div><h3>Consultation</h3><p>A free conversation about your situation, priorities and goals.</p></div></li>
        <li class="timeline__step" data-aos="fade-up" data-aos-delay="150"><span class="timeline__num" aria-hidden="true">02</span><div><h3>Comparison</h3><p>Options from several insurers and fund houses, explained side by side.</p></div></li>
        <li class="timeline__step" data-aos="fade-up" data-aos-delay="300"><span class="timeline__num" aria-hidden="true">03</span><div><h3>Plan &amp; set-up</h3><p>A clear, prioritised plan, with all the paperwork handled for you.</p></div></li>
        <li class="timeline__step" data-aos="fade-up" data-aos-delay="450"><span class="timeline__num" aria-hidden="true">04</span><div><h3>Ongoing support</h3><p>Renewals, reviews and claims support for as long as you need us.</p></div></li>
      </ol>
    </div>
  </section>''',
        faq(a['faqs'], 'faq', heading=f'{a["label"]}: common questions'),
        f'''  <section class="section section--sm" aria-labelledby="other-title">
    <div class="container text-center">
      <h2 id="other-title" class="solution-others__title">Solutions for others</h2>
      <ul class="solution-others">
{others}
      </ul>
    </div>
  </section>''',
        f'''  <section class="cta-band bg-brand next-steps" aria-labelledby="next-title">
    <div class="container">
      <span class="eyebrow eyebrow--light">What should I do next?</span>
      <h2 id="next-title">Take the first step, at no cost</h2>
      <p>Choose whatever suits you. There is no fee and no obligation.</p>
      <ul class="next-steps__grid">
        <li><a class="next-step" href="contact.html">{I("calendar-check")}<strong>Book a Free Consultation</strong><span>Meet us at our office, at home or online.</span></a></li>
        <li><a class="next-step" href="tel:+919847046614">{I("phone")}<strong>Talk to an Advisor</strong><span>Call +91 98470 46614, Mon to Sat, 9 to 6:30.</span></a></li>
        <li><a class="next-step" href="financial-checkup.html">{I("clipboard-check")}<strong>Get a Free Financial Review</strong><span>A complete check of your cover, savings and goals.</span></a></li>
      </ul>
    </div>
  </section>''',
    )
    page(f'{a["slug"]}.html', a['title'], a['desc'], body, sub_current=f'{a["slug"]}.html', banner_img=a['img'])


def build_all_solutions():
    for a in AUDIENCES:
        audience_page(a)


if __name__ == '__main__':
    build_all_solutions()
