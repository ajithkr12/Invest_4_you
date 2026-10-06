"""Seven service detail pages + services.html overview (dev helper, not deployed)."""
from pages_common import *

OLD_REGIME = 'Deductions under Sections 80C and 80D are available only under the old tax regime.'

SERVICES = [
  dict(
    slug='life-insurance', name='Life Insurance', icon='people-roof', short='Protect your family\'s income and future goals.',
    title='Life Insurance in Kochi',
    lead='Future value protection: long-term security and financial stability for you and your loved ones.',
    desc='Life insurance advice in Kochi since 1992: term, endowment and whole-life plans, LIC policies, tax savings under Section 80C and full claim support.',
    intro=["Safeguarding your tomorrow begins with the choices you make today. Our Future Value Protection solutions are designed to provide long-term security and financial stability for you and your loved ones. By combining foresight with smart planning, they help preserve the value you've built over time, so your goals, dreams and responsibilities stay protected even in the face of life's uncertainties.",
           "Whether you're planning for your family's future, securing assets or preparing for unforeseen events, our approach helps you stay confident and resilient through every stage of life. As a trusted LIC partner since 1992, we help you choose the right cover and stay with you for every renewal, revival and claim."],
    callout=('1 in 10', 'By many estimates, only about one in ten Indians has life insurance, and many who do are under-insured. The gap is widest in young families with a home loan and a single income.',
             'TODO: confirm this statistic and cite its source (carried over from the current site).'),
    benefits=[('people-roof', 'Income replacement', 'A lump sum for your family to cover living costs, education and goals if you\'re not there.'),
              ('file-invoice-dollar', 'Tax savings', 'Premiums qualify for deduction under Section 80C, up to ₹1.5 lakh a year. Maturity and death benefits may be tax-free under Section 10(10D), subject to conditions.'),
              ('house-user', 'Loan protection', 'Clear a home, car or education loan so your family isn\'t left with debt.'),
              ('piggy-bank', 'Disciplined saving', 'Endowment and money-back plans combine protection with regular, guaranteed-style saving.'),
              ('user-shield', 'Riders for extra cover', 'Add accidental death, critical illness or waiver-of-premium riders for a small extra premium.'),
              ('hand-holding-medical', 'Claim support', 'We help your family with every form and follow-up, so a claim is settled with as little stress as possible.')],
    audience=['Young earners starting a family', 'Parents with children still in school or college', 'Home loan borrowers', 'Self-employed professionals and business owners', 'Single-income households', 'Anyone with an old policy they haven\'t reviewed in years'],
    steps=[('Work out your cover', 'We estimate the cover you need from your income, expenses, loans and goals, using the Human Life Value method.'),
           ('Compare plans', 'We explain term, endowment, money-back and whole-life options and what each one costs.'),
           ('Apply with confidence', 'We help with the proposal form, medical tests and documents, and check every detail before it\'s submitted.'),
           ('Lifelong service', 'Nominations, revivals, policy loans, maturity payouts and claims: we handle them with you.')],
    faqs=[('How much life cover do I need?', '<p>A common rule of thumb is 10 to 15 times your annual income, plus any outstanding loans. A better answer comes from your actual expenses and goals. Try our <a href="life-cover-calculator.html">life cover calculator</a> or ask us for a free review.</p>'),
          ('What is the difference between term and endowment plans?', '<p>A term plan pays only if you die during the policy term, which makes it the cheapest way to buy a large cover. An endowment plan also pays a maturity amount if you survive the term, so the premium is much higher for the same cover.</p>'),
          ('Can I have more than one policy?', '<p>Yes. Many families combine a term plan for high cover with an endowment or money-back plan for savings. You must disclose existing policies when you apply.</p>'),
          ('What happens if I miss a premium?', '<p>Most policies allow a grace period, usually 15 or 30 days depending on how often you pay. After that the policy lapses, but it can often be revived within a set period by paying the arrears. We\'ll remind you and help with revival.</p>'),
          ('How do you help with a claim?', '<p>We guide your family through the documents the insurer needs, submit the claim, and follow up until it is settled. There is no charge for this support.</p>')],
  ),
  dict(
    slug='health-insurance', name='Health Insurance', icon='heart-pulse', short='Cashless care and claim support.',
    title='Health Insurance for Your Family',
    lead='Financial security and peace of mind for you and your loved ones during medical challenges.',
    desc='Health insurance advice in Kochi: family floater, senior citizen and top-up plans, cashless hospitalisation, Section 80D tax savings and hands-on claim support.',
    intro=['Good health is the foundation of a fulfilling life, and being prepared for the unexpected is essential to maintaining it. Our Health Protection Solutions are designed to give you and your loved ones financial security and peace of mind during medical challenges, and to support access to quality healthcare when it matters most.',
           'By managing healthcare expenses effectively and minimising financial strain, our approach keeps your focus on recovery and overall well-being. With thoughtful planning and reliable protection, you can live with confidence, knowing that your health, family and future are secure.'],
    callout=None,
    benefits=[('hospital', 'Cashless hospitalisation', 'Treatment at network hospitals without paying the bill yourself, subject to policy terms.'),
              ('people-group', 'Family floater cover', 'One sum insured shared by your whole family, usually at a lower premium than separate policies.'),
              ('stethoscope', 'Before and after hospital', 'Most plans cover related expenses for a set number of days before and after admission.'),
              ('file-invoice-dollar', 'Tax savings under 80D', 'Deduct up to ₹25,000 a year for your family\'s premiums, and up to ₹50,000 more for senior citizen parents.'),
              ('layer-group', 'Top-up and super top-up', 'Raise your cover affordably on top of an existing or employer policy.'),
              ('hand-holding-medical', 'Claim support', 'We help with pre-authorisation, documents and follow-ups with the insurer.')],
    audience=['Young families buying their first policy', 'Parents and senior citizens', 'Employees who rely only on group cover from work', 'Self-employed people and freelancers', 'People with pre-existing conditions', 'Anyone whose current cover feels too small'],
    steps=[('Understand your needs', 'Family members, ages, health history and the hospitals you prefer.'),
           ('Compare policies', 'Room-rent limits, waiting periods, co-pay and network hospitals, side by side.'),
           ('Buy and onboard', 'We make sure every health condition is declared correctly so claims aren\'t rejected later.'),
           ('Claims and renewals', 'Help at the hospital desk, with reimbursement paperwork, and a review at every renewal.')],
    faqs=[('Is my employer\'s group health cover enough?', '<p>Group cover usually ends when you leave the job and is often small for a family. A personal policy, or a top-up on your group cover, protects you between jobs and after retirement.</p>'),
          ('What is a waiting period?', '<p>Most policies don\'t cover certain illnesses, and conditions you already have, for an initial period, often two to four years. Starting early means the waiting period is over by the time you are more likely to need it.</p>'),
          ('What is the difference between cashless and reimbursement claims?', '<p>With a cashless claim at a network hospital, the insurer settles the bill directly after approving it. With reimbursement, you pay first and claim the money back with your bills and reports.</p>'),
          ('Can I move my policy to another insurer?', '<p>Yes. IRDAI rules allow you to port your health policy to another insurer at renewal while keeping credit for waiting periods already served. Apply well before your renewal date and we\'ll help with the process.</p>'),
          ('How much tax can I save?', f'<p>Under Section 80D you can deduct up to ₹25,000 a year for yourself, your spouse and children (₹50,000 if you are a senior citizen), plus up to ₹25,000 for parents (₹50,000 if they are senior citizens). {OLD_REGIME}</p>')],
  ),
  dict(
    slug='corporate-insurance', name='Corporate Insurance', icon='building-shield', short='Business continuity for companies of every size.',
    title='Corporate Insurance for Businesses',
    lead='Safeguard your organisation against unforeseen challenges, for continuity, resilience and long-term growth.',
    desc='Corporate insurance in Kochi for SMEs and companies at Infopark: property, group health, group term life, liability, marine and key person cover.',
    intro=['Every successful business is built on a foundation of stability and foresight. Our Corporate Protection Solutions are designed to safeguard your organisation against unforeseen challenges, ensuring continuity, resilience and long-term growth.',
           'From protecting key assets and leadership to managing operational risks and employee well-being, we help businesses strengthen their defences while they focus on their core goals. With the right protection strategy in place, your enterprise can thrive with confidence, ready to navigate uncertainties and seize new opportunities.'],
    callout=None,
    benefits=[('fire', 'Property and fire', 'Buildings, stock, machinery and equipment against fire, flood and other perils.'),
              ('people-group', 'Group health', 'Health cover for employees and their families, a benefit that helps you hire and keep good people.'),
              ('user-shield', 'Group term life', 'Low-cost life cover for your whole team, with a single policy to manage.'),
              ('scale-balanced', 'Liability cover', 'Protection against claims from customers, visitors or third parties.'),
              ('truck', 'Marine and transit', 'Goods in transit by road, rail, sea or air.'),
              ('user-tie', 'Key person insurance', 'Protect the business against the loss of a founder or critical employee.')],
    audience=['Small and medium businesses', 'IT and ITES companies at Infopark', 'Shops, traders and distributors', 'Manufacturers and workshops', 'Clinics and professional firms', 'Start-ups hiring their first employees'],
    steps=[('Risk review', 'We visit your premises and understand your assets, people and contracts.'),
           ('Design and quotes', 'We recommend the covers you need and get quotes from several insurers.'),
           ('Placement', 'We handle proposals, surveys and documentation until the policies are issued.'),
           ('Renewals and claims', 'Endorsements as your business changes, timely renewals and full claim support.')],
    faqs=[('Does a small business really need insurance?', '<p>Small businesses are often the least able to absorb a loss. A single fire or theft can wipe out stock and savings. Basic property and liability cover is usually affordable.</p>'),
          ('Can group health cover include employees\' families?', '<p>Yes. Most group health policies can cover spouses, children and sometimes parents, with the premium shared between employer and employee if you choose.</p>'),
          ('What happens when our business changes?', '<p>New premises, stock levels or team size can be added by endorsement during the year. We review everything at renewal so you\'re never under-insured.</p>'),
          ('Will you help us make a claim?', '<p>Yes. We coordinate with the insurer and surveyor, help you prepare documents and follow up until the claim is settled.</p>')],
  ),
  dict(
    slug='mutual-funds', name='Mutual Funds', icon='chart-line', short='Equity, debt and liquid funds for your goals.',
    title='Mutual Fund Investments',
    lead='Equity, debt and liquid funds chosen for your goals, your time frame and your comfort with risk.',
    desc='Mutual fund investments through an AMFI-registered distributor in Kochi: SIPs, ELSS tax-saving funds, debt and liquid funds, with regular portfolio reviews.',
    intro=['Mutual funds pool money from many investors and invest it in shares, bonds or money-market instruments, managed by professional fund managers and regulated by SEBI.',
           'As an AMFI-registered Mutual Fund Distributor (ARN-XXXXX), we help you understand the options, match schemes to your goals, complete your KYC and set up SIPs, and then review your portfolio with you regularly. We are a distributor, not a SEBI-registered investment adviser.'],
    callout=None,
    benefits=[('chart-line', 'Equity funds', 'For long-term goals such as retirement and education, where you can ride out market ups and downs.'),
              ('building-columns', 'Debt funds', 'For more stable returns over shorter periods, investing in bonds and government securities.'),
              ('wallet', 'Liquid funds', 'A home for your emergency fund or idle cash, with easy access.'),
              ('calendar-check', 'SIPs', 'Invest a fixed amount every month and build wealth with discipline.'),
              ('file-invoice-dollar', 'ELSS tax-saving funds', 'Qualify for deduction under Section 80C, with a 3-year lock-in.'),
              ('rotate', 'Regular reviews', 'We check your portfolio against your goals and rebalance when needed.')],
    audience=['First-time investors', 'Salaried people starting a monthly SIP', 'Parents saving for education', 'Anyone planning for retirement', 'Retirees wanting a regular income through a withdrawal plan', 'People with idle cash in a savings account'],
    steps=[('Goals and risk profile', 'What you are investing for, when you need the money and how much volatility you can live with.'),
           ('Scheme selection and KYC', 'We explain suitable schemes and help you complete KYC with PAN, Aadhaar and bank details.'),
           ('Start investing', 'Lump sum or SIP, set up online or on paper.'),
           ('Review regularly', 'Periodic reviews to keep your investments aligned with your goals.')],
    faqs=[('What is a SIP?', '<p>A Systematic Investment Plan invests a fixed amount in a scheme every month. It builds a saving habit and averages your purchase cost over time. See what a SIP could grow to with our <a href="sip-calculator.html">SIP calculator</a>.</p>'),
          ('How much risk is involved?', '<p>It depends on the scheme. Equity funds can rise and fall sharply in the short term; debt and liquid funds are generally more stable but are not risk-free. Every scheme shows a riskometer, and we\'ll explain it before you invest.</p>'),
          ('What do I need for KYC?', '<p>Usually your PAN, Aadhaar or another address proof, a photograph and your bank details. KYC is done once and works across fund houses.</p>'),
          ('Can I withdraw my money at any time?', '<p>Open-ended schemes can generally be redeemed on any business day, though exit loads may apply for early withdrawal. ELSS funds have a 3-year lock-in.</p>'),
          ('How are you paid?', '<p>As a distributor we receive commission from the fund house on investments made through us in regular plans. This is included in the scheme\'s expense ratio; you pay us no separate fee. Direct plans have no distributor commission. We\'re happy to explain the difference.</p>')],
    risk=True,
  ),
  dict(
    slug='retirement-planning', name='Retirement Planning', icon='person-cane', short='A steady income after work.',
    title='Retirement Planning',
    lead='Lasting peace of mind and financial independence for the years after work.',
    desc='Retirement planning in Kochi: estimate your retirement corpus, save through SIPs and pension plans, and plan a regular income and health cover for later years.',
    intro=["Planning for retirement is about more than just saving: it's about creating lasting peace of mind and financial independence for the years ahead. Our Retirement Solutions are designed to help you build a strong foundation for a comfortable and fulfilling future.",
           'Through disciplined planning and strategic wealth management, we help make sure your resources keep supporting your lifestyle and aspirations long after your working years. With the right approach, you can look forward to retirement as a new beginning: secure, confident and full of possibilities.'],
    callout=None,
    benefits=[('calculator', 'Know your number', 'An estimate of the corpus you need, allowing for inflation and how long you may live.'),
              ('calendar-check', 'Save steadily', 'SIPs and pension plans that grow your savings month by month.'),
              ('money-bill-trend-up', 'Regular income', 'Annuities and systematic withdrawal plans that pay you every month after retirement.'),
              ('heart-pulse', 'Health cover for later years', 'A health policy that continues after your employer\'s cover ends.'),
              ('user-shield', 'Protect the plan', 'Life cover so your spouse is looked after if something happens to you.'),
              ('file-signature', 'Nominations in order', 'Up-to-date nominations on every policy and investment.')],
    audience=['People in their 20s and 30s who want to start early', 'People in their 40s and 50s who need to catch up', 'Those retiring in the next few years', 'Self-employed people without a pension', 'Couples planning together'],
    steps=[('Estimate your need', 'Your expected expenses, inflation, retirement age and life expectancy.'),
           ('Plan your savings', 'How much to invest each month, and where.'),
           ('Choose products', 'A mix of mutual funds, pension plans and insurance suited to you.'),
           ('Review and draw down', 'Yearly reviews, and a plan for a regular income once you retire.')],
    faqs=[('How much will I need to retire?', '<p>It depends on your expenses, inflation and how long your retirement lasts. Our <a href="retirement-calculator.html">retirement calculator</a> gives a quick estimate, and we can refine it with you.</p>'),
          ('When should I start?', '<p>As early as you can. Money invested in your 20s and 30s has far longer to grow, so the monthly amount you need is much smaller.</p>'),
          ('Should I buy an annuity or use a withdrawal plan?', '<p>An annuity pays a fixed income for life but is less flexible. A systematic withdrawal plan from mutual funds keeps your money invested and accessible, but the income isn\'t guaranteed. Many retirees use a mix.</p>'),
          ('What about rising prices?', '<p>Inflation reduces what your money can buy every year. Your plan should include some growth investments, even after you retire, so your income keeps pace.</p>')],
    risk=True,
  ),
  dict(
    slug='child-education', name='Child Education Planning', icon='graduation-cap', short='Fund your children\'s education on time.',
    title='Child Education Planning',
    lead='Start early and save steadily, so your children\'s education is paid for when the time comes.',
    desc='Child education planning in Kochi: estimate future education costs, save through SIPs and child plans, and protect the goal with life cover.',
    intro=['The cost of professional courses in India has risen much faster than general prices, and a degree abroad costs many times more. Saving early is the surest way to meet the bill without loans.',
           'We help you put a figure on each child\'s education goal, choose the right mix of investments, and protect the plan so it continues even if something happens to you.'],
    callout=None,
    benefits=[('calculator', 'A clear target', 'Today\'s course fees projected forward with education inflation.'),
              ('calendar-check', 'Monthly SIPs', 'Steady investing matched to the number of years you have.'),
              ('user-shield', 'Waiver of premium', 'Child plans that keep paying into the goal if the parent is no longer there.'),
              ('umbrella', 'Life cover for parents', 'A term plan sized to cover the education goal.'),
              ('file-invoice-dollar', 'Tax benefits', 'Premiums and ELSS investments can qualify under Section 80C.'),
              ('route', 'Milestone reviews', 'We move money to safer options as the admission year gets closer.')],
    audience=['Parents of newborns and young children', 'Parents of teenagers catching up', 'Families planning for study abroad', 'Grandparents who want to contribute'],
    steps=[('Set the goal', 'Course, country, and the year your child will need the money.'),
           ('Calculate', 'The future cost and the monthly amount needed to reach it.'),
           ('Invest and protect', 'SIPs, child plans and term cover, set up together.'),
           ('Review each year', 'Adjust as costs, income and plans change.')],
    faqs=[('How much will my child\'s education cost?', '<p>Take today\'s fees for the course you have in mind and allow for education inflation, often estimated at 8 to 10 percent a year. Our <a href="child-education-calculator.html">education calculator</a> does the maths for you.</p>'),
          ('Which is better: a child plan or mutual funds?', '<p>They do different jobs. A child insurance plan protects the goal if a parent dies; mutual funds usually offer more growth over long periods. Many families use both.</p>'),
          ('What if something happens to me?', '<p>A term plan or a child plan with waiver of premium keeps the goal funded. We size the cover to the goal.</p>'),
          ('Is it too late to start for my teenager?', '<p>It\'s never too late, but the plan will be different: shorter time frames call for safer investments and a larger monthly amount.</p>')],
    risk=True,
  ),
  dict(
    slug='tax-planning', name='Tax Planning', icon='file-invoice-dollar', short='Make the most of 80C and 80D.',
    title='Tax Planning',
    lead='Save tax the smart way, with investments and insurance that also serve your goals.',
    desc='Tax planning in Kochi: Section 80C and 80D deductions, ELSS, life and health insurance, and help choosing between the old and new tax regimes.',
    intro=['Many people rush into tax-saving products in March and end up with investments they don\'t need. Planning early in the year means every rupee you save on tax also works towards a real goal.',
           'We help you use the deductions available to you, compare the old and new tax regimes for your situation, and choose insurance and investments that make sense beyond the tax benefit.'],
    callout=None,
    benefits=[('file-invoice-dollar', 'Section 80C, up to ₹1.5 lakh', 'Life insurance premiums, ELSS, PPF, and other eligible investments.'),
              ('heart-pulse', 'Section 80D', 'Health insurance premiums for your family and your parents.'),
              ('scale-balanced', 'Old or new regime?', 'We compare both for your income and deductions so you can choose.'),
              ('chart-line', 'ELSS funds', 'Equity funds with the shortest lock-in among 80C options: three years.'),
              ('calendar-check', 'Plan early', 'Spread investments through the year instead of a March rush.'),
              ('clipboard-list', 'Proofs made easy', 'Premium receipts and statements ready for your employer or tax filing.')],
    audience=['Salaried employees submitting investment proofs', 'Self-employed people and professionals', 'Families paying health premiums for parents', 'Anyone unsure which tax regime suits them'],
    steps=[('Review your income', 'Salary, other income and the deductions you already have.'),
           ('Compare regimes', 'Old versus new, for your numbers.'),
           ('Choose investments', 'Insurance and ELSS or other options that fit your goals.'),
           ('Keep records', 'Receipts and statements organised for filing.')],
    faqs=[('Should I choose the old or the new tax regime?', f'<p>It depends on your income and how many deductions you claim. {OLD_REGIME} We\'ll compare both for you; for complex situations we recommend confirming with a chartered accountant.</p>'),
          ('When should I make tax-saving investments?', '<p>Early in the financial year. Monthly SIPs in ELSS or regular premiums spread the cost and avoid rushed decisions in March.</p>'),
          ('How long is the ELSS lock-in?', '<p>Three years from each investment. With a SIP, each instalment has its own three-year lock-in.</p>'),
          ('Do health premiums for my parents count?', '<p>Yes. Under Section 80D you can claim up to ₹25,000 for parents\' premiums, or ₹50,000 if either parent is a senior citizen, on top of your own family\'s limit.</p>')],
    tax_note=True,
  ),
]


# The four questions every service page answers: What is it? Why do I need it? (How we help and the CTA are built below.)
WHAT_WHY = {
    'life-insurance': dict(
        what=['Life insurance is a contract with an insurer: you pay a regular premium, and if you die during the policy term, the insurer pays your family a lump sum (the sum assured). Some plans, such as endowment and money-back policies, also pay out if you survive the term.',
              'The simplest form, a term plan, gives the largest cover for the lowest premium because it only pays on death.'],
        why='If your family depends on your income, losing it would leave them with the same bills, loans and goals, but no way to pay for them. Life insurance makes sure that money is still there.',
        risks=['Day-to-day expenses with no income coming in', 'A home or car loan your family would have to repay', "Children's education and other goals left unfunded", 'Savings used up to cover the gap']),
    'health-insurance': dict(
        what=['Health insurance pays your hospital bills when you or a family member is admitted for treatment. At a network hospital it can pay the hospital directly (cashless); elsewhere you pay first and claim the money back.',
              'A family floater covers everyone in one policy with a shared sum insured.'],
        why='Medical costs in India have risen far faster than incomes, and a single hospital stay can cost lakhs. Without cover, that money comes out of your savings or goals, often when you can least afford it.',
        risks=['A large hospital bill draining years of savings', 'Borrowing or selling investments in an emergency', "Losing your employer's group cover when you change jobs or retire", 'Higher premiums and waiting periods if you start late']),
    'corporate-insurance': dict(
        what=['Corporate insurance is a set of policies that protect a business: its premises, stock and equipment, its people (group health and group term life), its liability to others, and key individuals the business depends on.',
              'Each policy is chosen to match the risks your particular business faces.'],
        why='A fire, flood, accident, lawsuit or the loss of a key person can stop a business overnight. Insurance pays for the damage and keeps the business running while you recover, instead of draining its capital.',
        risks=['Damage to premises, stock or machinery', 'Claims from customers, visitors or third parties', "Losing a founder or key employee", 'Employees without health cover for themselves and their families']),
    'mutual-funds': dict(
        what=["A mutual fund pools money from many investors and invests it in shares, bonds or money-market instruments, managed by a professional fund manager and regulated by SEBI. You own units of the fund, and their value rises and falls with the fund's investments.",
              'You can invest a lump sum, or a fixed amount every month through a SIP.'],
        why="Money left in a savings account loses value to inflation every year. Mutual funds give you a regulated, diversified way to grow your savings towards goals such as education, a home or retirement, at a level of risk that suits you.",
        risks=['Savings that do not keep pace with rising prices', 'Goals that need more growth than a deposit can give', 'Putting all your money in one company or one type of asset', 'Investing without a plan, or stopping when markets fall']),
    'retirement-planning': dict(
        what=["Retirement planning means working out how much money you will need to live on after you stop working, and building a plan to get there: how much to save, where to invest it, and how to turn it into a regular income when you retire.",
              'It also covers the protection you will need along the way, such as health cover and life insurance.'],
        why='Most people in India do not have a pension. With longer lives and rising prices, your savings may need to last 25 years or more. Starting late, or without a plan, can mean running short just when you can no longer earn.',
        risks=['Savings running out in later years', 'Inflation steadily reducing what your money can buy', 'Medical costs rising as you get older', 'Depending on children for day-to-day expenses']),
    'child-education': dict(
        what=["Child education planning means putting a figure on what your child's education will cost, allowing for fees that rise every year, and building savings to meet that cost on time.",
              'It usually combines regular investing (such as a SIP) with life cover, so the plan continues even if something happens to a parent.'],
        why="Education costs in India have risen much faster than general prices, and professional courses or study abroad can cost many times today's fees. Without planning, families often end up taking expensive loans or compromising on choices.",
        risks=['Fees rising faster than your savings', 'Large education loans at a young age', "Having to compromise on your child's choice of course", 'The plan stopping if a parent is no longer there']),
    'tax-planning': dict(
        what=['Tax planning means using the deductions and exemptions the law allows, such as those under Sections 80C and 80D, and choosing the right tax regime, so you pay the tax you owe and no more.',
              'Good tax planning chooses investments and insurance that you would want anyway, and treats the tax saving as a bonus.'],
        why='Without a plan, many people either miss deductions they are entitled to, or rush into products in March that do not suit their goals. Both cost money, every year.',
        risks=['Paying more tax than necessary', "Last-minute investments that do not fit your goals", 'Choosing the wrong regime for your income', 'Missing proofs when your employer or the tax department asks']),
}
STEP_TITLES = ['Consultation', 'Comparison', 'Plan &amp; set-up', 'Ongoing support']

from services_extra import EXTRA, GOAL_SERVICES, LEGAL_NOTE
for _e in EXTRA:
    WHAT_WHY[_e['slug']] = _e.pop('why')
    SERVICES.append(_e)
BY_SLUG = {s['slug']: s for s in SERVICES}


def goal_of(slug):
    for gid, (title, slugs) in GOAL_SERVICES.items():
        if slug in slugs:
            return gid, title, slugs
    return None, 'Our services', [s['slug'] for s in SERVICES]


def service_nav(current):
    cur = ' aria-current="page"'
    gid, title, slugs = goal_of(current)
    items = [f'<li><a href="{x}.html"{cur if x == current else ""}>{BY_SLUG[x]["name"]} {I("chevron-right")}</a></li>' for x in slugs]
    items.append(f'<li><a href="services.html">All services {I("chevron-right")}</a></li>')
    return '\n            '.join(items)


def service_page(s):
    qa = WHAT_WHY[s['slug']]
    lname = s['name'].lower()
    what = '\n          '.join(f'<p>{p}</p>' for p in qa['what'])
    how_intro = '\n          '.join(f'<p>{p}</p>' for p in s['intro'])
    callout = ''
    if s.get('callout'):
        num, text, todo = s['callout']
        callout = f'''
          <!-- {todo} -->
          <div class="stat-callout mt-6" data-aos="fade-up">
            <span class="stat-callout__num">{num}</span>
            <p>{text}</p>
          </div>'''
    notices = ''
    if s.get('risk'):
        notices += f'\n          <div class="mt-6">{MF_RISK}</div>'
    if s.get('legal'):
        notices += f'\n          <div class="notice mt-6">{I("scale-balanced")}<p>{LEGAL_NOTE}</p></div>'
    if s.get('tax_note'):
        notices += f'\n          <div class="notice mt-6">{I("shield")}<p>{OLD_REGIME} Tax rules change from year to year; this page is general information, not tax advice.</p></div>'

    risks = '\n'.join(f'          <li>{r}</li>' for r in qa['risks'])
    benefits = '\n'.join(f'''        <li class="benefit" data-aos="fade-up"{f' data-aos-delay="{(i % 2) * 100}"' if i % 2 else ''}>
          <span class="icon-circle">{I(ic)}</span>
          <div><h3>{t}</h3><p>{d}</p></div>
        </li>''' for i, (ic, t, d) in enumerate(s['benefits']))
    audience = '\n'.join(f'        <li>{I("circle-check")}<span>{a}</span></li>' for a in s['audience'])
    steps = '\n'.join(f'''        <li class="timeline__step" data-aos="fade-up" data-aos-delay="{i * 150}">
          <span class="timeline__num" aria-hidden="true">0{i + 1}</span>
          <div>
            <h3>{STEP_TITLES[i]}</h3>
            <p>{d}</p>
          </div>
        </li>''' for i, (t, d) in enumerate(s['steps']))

    body = main(
        banner(s['title'], [('Services', 'services.html'), (s['name'], None)], s['lead']),
        # 1. What is it?
        f'''  <section class="section" aria-labelledby="what-title">
    <div class="container with-aside">
      <div>
        <div class="prose" data-aos="fade-up">
          <span class="eyebrow">What is it?</span>
          <h2 id="what-title">{s.get("what_title", f"What is {lname}?")}</h2>
          {what}
        </div>{callout}{notices}
      </div>
      <aside class="aside-sticky" aria-label="More services and help">
        <div class="aside-card aside-card--brand">
          <h2>Talk to an advisor</h2>
          <p>Get a free, no-obligation review of your {lname} needs.</p>
          <a class="btn btn--block mt-6" href="contact.html?service={s['slug']}">Book a free consultation</a>
        </div>
        <nav class="aside-card" aria-label="{goal_of(s['slug'])[1]}">
          <h2>{goal_of(s['slug'])[1]}</h2>
          <ul class="service-nav">
            {service_nav(s['slug'])}
          </ul>
        </nav>
      </aside>
    </div>
  </section>''',
        # 2. Why do I need it?
        f'''  <section class="section bg-alt" aria-labelledby="why-title">
    <div class="container">
      <div class="section-head" data-aos="fade-up">
        <span class="eyebrow">Why do I need it?</span>
        <h2 id="why-title">The risk {lname} addresses</h2>
        <p>{qa['why']}</p>
      </div>
      <div class="why-risks" data-aos="fade-up">
        <h3>Without it, you could face</h3>
        <ul class="why-risks__list">
{risks}
        </ul>
      </div>
      <h3 class="why-benefits__title" data-aos="fade-up">What {lname} gives you</h3>
      <ul class="benefits">
{benefits}
      </ul>
    </div>
  </section>''',
        f'''  <section class="section" aria-labelledby="audience-title">
    <div class="container split">
      <div data-aos="fade-right">
        <span class="eyebrow">Who it's for</span>
        <h2 id="audience-title">Is this right for you?</h2>
        <p class="text-muted">If any of these sound like you, a short conversation with us is a good place to start.</p>
        <a class="btn mt-6" href="contact.html?service={s['slug']}">Ask us a question</a>
      </div>
      <ul class="audience" data-aos="fade-left">
{audience}
      </ul>
    </div>
  </section>''',
        # 3. How can Invest 4U help?
        f'''  <section class="section bg-alt" aria-labelledby="how-title">
    <div class="container">
      <div class="section-head" data-aos="fade-up">
        <span class="eyebrow">How can Invest 4U help?</span>
        <h2 id="how-title">Consultation, comparison, planning and ongoing support</h2>
      </div>
      <div class="prose how-intro" data-aos="fade-up">
          {how_intro}
      </div>
      <ol class="timeline" data-inview>
        <li class="timeline__line" aria-hidden="true"></li>
{steps}
      </ol>
    </div>
  </section>''',
        faq(s['faqs'], 'faq', heading=f'{s["name"]}: common questions', bg=''),
        # 4. What should I do next?
        f'''  <section class="cta-band bg-brand next-steps" aria-labelledby="next-title">
    <div class="container">
      <span class="eyebrow eyebrow--light">What should I do next?</span>
      <h2 id="next-title">Take the first step, at no cost</h2>
      <p>Choose whatever suits you. There is no fee and no obligation.</p>
      <ul class="next-steps__grid">
        <li><a class="next-step" href="contact.html?service={s['slug']}">{I("calendar-check")}<strong>Book a Free Consultation</strong><span>Meet us at our office, at home or online.</span></a></li>
        <li><a class="next-step" href="tel:+919847046614">{I("phone")}<strong>Talk to an Advisor</strong><span>Call +91 98470 46614, Mon to Sat, 9 to 6:30.</span></a></li>
        <li><a class="next-step" href="financial-checkup.html">{I("clipboard-check")}<strong>Get a Free Financial Review</strong><span>A complete check of your cover, savings and goals.</span></a></li>
      </ul>
    </div>
  </section>''',
    )
    page(f'{s["slug"]}.html', s['title'], s['desc'], body, current=None, sub_current=f'{s["slug"]}.html',
         banner_img='service-detail')


def services_overview():
    body = main(
        banner('Our Services', [('Services', None)], 'Insurance, investments and planning under one roof, with one team that knows your whole picture.', img='services'),
        f'''  <section class="section bg-alt" id="services" aria-labelledby="services-title">
    <div class="container">
      <div class="section-head" data-aos="fade-up">
        <span class="eyebrow">Products &amp; Services</span>
        <h2 id="services-title">What Would You Like to Achieve?</h2>
        <p>Start with your goal, not a product. Choose a service to learn more, or book a free checkup and we'll look at everything together.</p>
      </div>
{goal_grid(with_ids=True)}
      <p class="for-business" data-aos="fade-up">{I("building-shield")} <span>For businesses: <a href="corporate-insurance.html">Corporate Insurance</a>, protecting your premises, people and key staff.</span></p>
    </div>
  </section>''',
        f'''  <section class="section" id="wealth" aria-labelledby="wealth-title">
    <div class="container service-row">
      <div class="media-frame bracket" data-aos="fade-right">
        <!-- TODO: replace with a real photo -->
        <img src="assets/images/services/wealth-planning.webp" alt="A couple reviewing their long-term financial plan (placeholder image)" width="1200" height="800" loading="lazy">
      </div>
      <div data-aos="fade-left">
        <span class="eyebrow">Wealth Creation &amp; Estate Planning</span>
        <h2 id="wealth-title">Wealth that lasts for generations</h2>
        <p>True wealth goes beyond accumulation: it's about creating enduring value that supports your ambitions and secures your future. Our Wealth Creation solutions focus on building a strong and resilient financial foundation through strategic planning, smart investments and continuous growth.</p>
        <p>By aligning your financial goals with a clear roadmap, we help you unlock opportunities, make the most of your investments and build prosperity that lasts for generations.</p>
        <p>We also help you get the basics of estate planning right: up-to-date nominations on every policy and investment, clear records for your family, and pointers on when to speak to a lawyer about a will.</p>
        <ul class="tick-list">
          <li>Long-term goal-based portfolios</li>
          <li>Diversification across equity, debt and insurance</li>
          <li>Nominations and records your family can find</li>
          <li>Regular reviews as your wealth grows</li>
        </ul>
        <div class="btn-group"><a class="btn" href="wealth-creation.html">Wealth Creation</a><a class="btn btn--outline" href="estate-planning.html">Estate Planning</a></div>
      </div>
    </div>
    <div class="container mt-6">{MF_RISK}</div>
  </section>''',
        cta_band(),
    )
    page('services.html', 'Our Services', 'Life, health and corporate insurance, mutual funds, retirement, child education and tax planning from Invest 4U Solutions in Kochi, since 1992.',
         body, current='services.html', banner_img='services')


if __name__ == '__main__':
    for s in SERVICES:
        service_page(s)
    services_overview()
