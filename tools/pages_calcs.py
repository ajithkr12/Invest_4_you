"""Calculators hub (calculators.html) + one page per calculator (dev helper, not deployed).

Formulas here mirror invest4u/js/calculators.js; they are used to write the worked examples,
so the example text always matches what the calculator shows.
"""
import json
from pages_common import *

CHART_JS = '<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js" defer></script>'
CALC_JS = '<script src="js/calculators.js" defer></script>'


# ---------------------------------------------------------------- Formulas (mirror calculators.js)
def sip_fv(p, rate, months):
    i = rate / 12 / 100
    return p * (((1 + i) ** months - 1) / i) * (1 + i)


def emi_amt(p, rate, years):
    r, n = rate / 12 / 100, years * 12
    return p * r * (1 + r) ** n / ((1 + r) ** n - 1)


def rd_fv(m, rate, years):
    n = years * 12
    return sum(m * (1 + rate / 400) ** ((n - k + 1) / 3) for k in range(1, n + 1))


def ppf_fv(y, rate, years):
    r, bal = rate / 100, 0
    for _ in range(years):
        bal = (bal + y) * (1 + r)
    return bal


def stepup_fv(m, s, rate, years):
    i, bal = rate / 12 / 100, 0
    for y in range(years):
        amt = m * (1 + s / 100) ** y
        for _ in range(12):
            bal = (bal + amt) * (1 + i)
    return bal


def swp_final(amount, w, rate, years):
    i, bal = rate / 12 / 100, amount
    for _ in range(years * 12):
        if bal > 0:
            bal = (bal - min(w, bal)) * (1 + i)
    return bal


def retirement_corpus(age=35, retire=60, life=85, exp=40000, inf=6, rb=11, ra=7, sav=500000):
    yt, yi = retire - age, life - retire
    annual = exp * (1 + inf / 100) ** yt * 12
    real = (1 + ra / 100) / (1 + inf / 100) - 1
    corpus = annual * (1 - (1 + real) ** -yi) / real * (1 + real)
    gap = max(0, corpus - sav * (1 + rb / 100) ** yt)
    i, n = rb / 12 / 100, yt * 12
    return corpus, gap * i / (((1 + i) ** n - 1) * (1 + i))


def hlv_gap(age=35, retire=60, income=1200000, exp=30, g=5, d=8, loans=2000000, cover=1000000, sav=500000):
    n, net, g, d = retire - age, income * (1 - exp / 100), g / 100, d / 100
    h = net * (1 - ((1 + g) / (1 + d)) ** n) / (d - g)
    return h, h + loans - cover - sav


def xirr_sip(monthly, years, value):
    n = years * 12
    fv = lambda r: sum(monthly * (1 + r) ** ((n - k + 1) / 12) for k in range(1, n + 1))
    lo, hi = -0.99, 10.0
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if fv(mid) > value else (mid, hi)
    return (lo + hi) / 2 * 100


def ssy_fv(yearly, rate):
    bal = 0
    for y in range(1, 22):
        bal = (bal + (yearly if y <= 15 else 0)) * (1 + rate / 100)
    return bal


def epf_fv(salary, age, contrib=12, inc=5, rate=8.25):
    r, bal = rate / 1200, 0
    for _ in range(58 - age):
        yi = 0
        for _ in range(12):
            bal += salary * contrib / 100 + max(0, salary * 0.12 - min(salary, 15000) * 0.0833)
            yi += bal * r
        bal += yi
        salary *= 1 + inc / 100
    return bal


def _slab(income, bands):
    tax, prev = 0, 0
    for cap, rate in bands:
        if income > prev:
            tax += (min(income, cap) - prev) * rate
        prev = cap
    return tax


def tax_new(income):
    ti = max(0, income - 75000)
    tx = _slab(ti, [(400000, 0), (800000, .05), (1200000, .10), (1600000, .15), (2000000, .20), (2400000, .25), (float('inf'), .30)])
    tx = 0 if ti <= 1200000 else min(tx, ti - 1200000)
    return tx * (1 + (0.15 if ti > 1e7 else 0.10 if ti > 5e6 else 0)) * 1.04


def tax_old(income, deductions, exempt=250000):
    ti = max(0, income - 50000 - deductions)
    tx = _slab(ti, [(exempt, 0), (500000, .05), (1000000, .20), (float('inf'), .30)])
    tx = 0 if ti <= 500000 else tx
    return tx * (1 + (0.15 if ti > 1e7 else 0.10 if ti > 5e6 else 0)) * 1.04


def inr(n):
    """Indian digit grouping: 12,34,567"""
    n = int(round(n))
    s = str(abs(n))
    if len(s) > 3:
        head, tail = s[:-3], s[-3:]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:])
            head = head[:-2]
        if head:
            parts.insert(0, head)
        s = ','.join(parts) + ',' + tail
    return '₹' + s


RISK = True
GROUPS = [('invest', 'Mutual funds &amp; investing', 'chart-line'), ('loans', 'Loans', 'house-user'),
          ('savings', 'Deposits &amp; savings', 'piggy-bank'), ('tax', 'Tax', 'file-invoice-dollar'),
          ('planning', 'Planning', 'route')]

# (key, label, min, max, step, default, unit, hint)
C = [
  dict(id='sip', file='sip-calculator.html', name='SIP Calculator', group='invest', icon='calendar-check',
       short='Estimate what a monthly SIP could grow to.', keywords='sip systematic investment plan mutual fund monthly',
       desc='Free SIP calculator: see what a monthly mutual fund SIP could grow to, with invested amount, estimated returns and total value.',
       headline='Estimated value', rows=[('Amount invested', 'inr'), ('Estimated returns', 'inr'), ('Total value', 'inr')],
       legend=['Amount invested', 'Estimated returns'],
       fields=[('monthly', 'Monthly investment', 500, 100000, 500, 10000, 'inr', ''),
               ('rate', 'Expected return rate (p.a.)', 1, 30, 0.5, 12, 'pct', 'Returns are not guaranteed.'),
               ('years', 'Time period', 1, 40, 1, 10, 'yrs', '')],
       about=['A Systematic Investment Plan (SIP) lets you invest a fixed amount in a mutual fund every month. Because you buy more units when prices are low and fewer when they are high, a SIP averages out your cost over time and builds a steady saving habit.',
              'This calculator shows what your SIP could be worth at the end of the period you choose, assuming a steady annual return.'],
       formula=('FV = P × [ (1 + i)<sup>n</sup> − 1 ] ÷ i × (1 + i)',
                ['<strong>FV</strong>: future value of the SIP', '<strong>P</strong>: monthly investment',
                 '<strong>i</strong>: monthly return (annual rate ÷ 12 ÷ 100)', '<strong>n</strong>: number of monthly instalments']),
       example=lambda: f'Investing {inr(10000)} a month for 10 years at an expected 12% a year: you invest {inr(1200000)}, and the SIP could be worth about <strong>{inr(sip_fv(10000, 12, 120))}</strong>.',
       faqs=[('Is the return in a SIP guaranteed?', '<p>No. Mutual fund returns depend on the market. The calculator uses a steady rate for illustration; real returns will go up and down.</p>'),
             ('What is a good expected return to use?', '<p>Use a conservative figure. Long-term equity funds have historically returned more than debt funds but with much more volatility. We can help you choose realistic assumptions.</p>'),
             ('Can I change or stop my SIP?', '<p>Yes. You can increase, pause or stop most SIPs at any time, although ELSS instalments have a 3-year lock-in each.</p>')],
       related=['stepup', 'lumpsum', 'swp', 'education'], cta=('mutual-funds.html', 'Start a SIP with us'), risk=RISK),

  dict(id='stepup', file='step-up-sip-calculator.html', name='Step-up SIP Calculator', group='invest', icon='arrow-up',
       short='See the effect of raising your SIP every year.', keywords='step up sip top up increase yearly mutual fund',
       desc='Free step-up SIP calculator: see how raising your monthly SIP by a fixed percentage every year boosts your final corpus.',
       headline='Estimated value', rows=[('Amount invested', 'inr'), ('Estimated returns', 'inr'), ('Total value', 'inr'), ('Value without step-up', 'inr')],
       legend=['Amount invested', 'Estimated returns'],
       fields=[('monthly', 'Starting monthly investment', 500, 100000, 500, 10000, 'inr', ''),
               ('stepup', 'Annual step-up', 0, 50, 1, 10, 'pct', 'How much you increase the SIP each year.'),
               ('rate', 'Expected return rate (p.a.)', 1, 30, 0.5, 12, 'pct', 'Returns are not guaranteed.'),
               ('years', 'Time period', 1, 40, 1, 10, 'yrs', '')],
       table=[('Year', ''), ('Monthly SIP', 'inr'), ('Total invested', 'inr'), ('Value at year end', 'inr')],
       about=['A step-up (or top-up) SIP increases your monthly instalment by a fixed percentage every year, usually in line with your salary increases. Small annual increases make a big difference over long periods.',
              'This calculator compares your step-up SIP with a regular SIP of the same starting amount.'],
       formula=('Each year y: monthly SIP = P × (1 + s)<sup>y</sup>; every instalment then grows at the monthly rate until the end',
                ['<strong>P</strong>: starting monthly investment', '<strong>s</strong>: annual step-up (%)', 'The value is the sum of every instalment, compounded monthly']),
       example=lambda: f'Starting at {inr(10000)} a month and raising it by 10% every year, at 12% for 10 years, your SIP could be worth about <strong>{inr(stepup_fv(10000, 10, 12, 10))}</strong>, compared with {inr(sip_fv(10000, 12, 120))} without a step-up.',
       faqs=[('How much should I step up each year?', '<p>Many investors match their expected salary increase, often 5 to 10 percent. Even a small step-up adds up over time.</p>'),
             ('Do all fund houses offer step-up SIPs?', '<p>Most do, usually called a "top-up" or "step-up" facility. You set it up once and the amount increases automatically.</p>'),
             ('Can I stop the step-up later?', '<p>Yes. You can usually stop the top-up or change the SIP amount by submitting a request.</p>')],
       related=['sip', 'lumpsum', 'cagr', 'retirement'], cta=('mutual-funds.html', 'Start a step-up SIP'), risk=RISK),

  dict(id='lumpsum', file='lumpsum-calculator.html', name='Lumpsum Calculator', group='invest', icon='sack-dollar',
       short='Returns on a one-time investment.', keywords='lumpsum lump sum one time mutual fund investment returns',
       desc='Free lumpsum calculator: estimate what a one-time mutual fund investment could grow to over your chosen period.',
       headline='Estimated value', rows=[('Amount invested', 'inr'), ('Estimated returns', 'inr'), ('Total value', 'inr')],
       legend=['Amount invested', 'Estimated returns'],
       fields=[('amount', 'Total investment', 5000, 10000000, 5000, 100000, 'inr', ''),
               ('rate', 'Expected return rate (p.a.)', 1, 30, 0.5, 12, 'pct', 'Returns are not guaranteed.'),
               ('years', 'Time period', 1, 40, 1, 10, 'yrs', '')],
       about=['A lumpsum investment is a single, one-time investment, for example from a bonus, the sale of property or a maturing policy.',
              'This calculator shows what that amount could grow to, assuming it compounds at a steady annual rate.'],
       formula=('FV = P × (1 + r)<sup>n</sup>', ['<strong>P</strong>: amount invested', '<strong>r</strong>: expected annual return', '<strong>n</strong>: number of years']),
       example=lambda: f'{inr(100000)} invested for 10 years at an expected 12% a year could grow to about <strong>{inr(100000 * 1.12 ** 10)}</strong>.',
       faqs=[('Lumpsum or SIP: which is better?', '<p>A lumpsum puts all your money to work at once; a SIP spreads your purchases over time and reduces timing risk. If you have a large sum, a systematic transfer plan (STP) is a middle path.</p>'),
             ('Is the final value guaranteed?', '<p>No. Market-linked returns vary; the calculator assumes a constant rate for illustration.</p>'),
             ('Should I invest a lumpsum in equity funds?', '<p>It depends on your time frame and risk comfort. For shorter goals, debt or hybrid funds may suit better. Talk to us before investing a large amount.</p>')],
       related=['sip', 'cagr', 'fd', 'swp'], cta=('mutual-funds.html', 'Talk to us about investing'), risk=RISK),

  dict(id='swp', file='swp-calculator.html', name='SWP Calculator', group='invest', icon='money-bill-trend-up',
       short='Plan a regular monthly income from your investments.', keywords='swp systematic withdrawal plan monthly income retirement pension',
       desc='Free SWP calculator: plan a regular monthly income from your mutual fund investment and see how long it lasts and what remains.',
       headline='Value at the end', rows=[('Total investment', 'inr'), ('Total withdrawn', 'inr'), ('Final value', 'inr'), ('Withdrawals last', 'months')],
       legend=['Total withdrawn', 'Final value'],
       fields=[('amount', 'Total investment', 10000, 50000000, 10000, 1000000, 'inr', ''),
               ('withdrawal', 'Withdrawal per month', 500, 500000, 500, 8000, 'inr', ''),
               ('rate', 'Expected return rate (p.a.)', 1, 30, 0.5, 8, 'pct', 'Returns are not guaranteed.'),
               ('years', 'Time period', 1, 40, 1, 10, 'yrs', '')],
       table=[('Year', ''), ('Withdrawn in the year', 'inr'), ('Total withdrawn', 'inr'), ('Balance at year end', 'inr')],
       about=['A Systematic Withdrawal Plan (SWP) pays you a fixed amount from your mutual fund investment every month, while the rest stays invested. It is popular with retirees who want a regular income.',
              'This calculator shows how much you would withdraw, what would remain at the end, and whether the money lasts the full period.'],
       formula=('Each month: balance = (balance − withdrawal) × (1 + i)',
                ['The withdrawal is taken at the start of the month', '<strong>i</strong>: monthly return (annual rate ÷ 12 ÷ 100)', 'Withdrawals stop if the balance runs out']),
       example=lambda: f'Investing {inr(1000000)} and withdrawing {inr(8000)} a month for 10 years at an expected 8%: you withdraw {inr(960000)} in total, and about <strong>{inr(swp_final(1000000, 8000, 8, 10))}</strong> could remain.',
       faqs=[('How much can I safely withdraw each month?', '<p>If your withdrawals are higher than what the investment earns, the balance shrinks. Keeping the yearly withdrawal below the expected return helps your money last longer.</p>'),
             ('How are SWP withdrawals taxed?', '<p>Each withdrawal is treated as a partial redemption, so only the gains portion is taxed, as capital gains. Tax rules change, so please check the current rules or ask us.</p>'),
             ('Can I change the withdrawal amount?', '<p>Yes. You can usually change, pause or stop an SWP by submitting a request to the fund house.</p>')],
       related=['retirement', 'lumpsum', 'sip', 'inflation'], cta=('retirement-planning.html', 'Plan your retirement income'), risk=RISK),

  dict(id='cagr', file='cagr-calculator.html', name='CAGR Calculator', group='invest', icon='chart-simple',
       short='Compound annual growth rate of an investment.', keywords='cagr compound annual growth rate returns performance',
       desc='Free CAGR calculator: find the compound annual growth rate of an investment from its starting value, ending value and time period.',
       headline='CAGR', big_fmt='pct', rows=[('Initial value', 'inr'), ('Final value', 'inr'), ('Absolute return', 'pct'), ('CAGR', 'pct')],
       legend=['Initial value', 'Growth'],
       fields=[('initial', 'Initial value', 1000, 100000000, 1000, 100000, 'inr', ''),
               ('final', 'Final value', 1000, 100000000, 1000, 250000, 'inr', ''),
               ('years', 'Time period', 1, 40, 1, 5, 'yrs', '')],
       about=['The Compound Annual Growth Rate (CAGR) is the steady yearly rate at which an investment would have had to grow to go from its starting value to its ending value.',
              'It is a fairer way to compare investments held for different periods than a simple total return.'],
       formula=('CAGR = (FV ÷ PV)<sup>1 ÷ n</sup> − 1', ['<strong>PV</strong>: initial value', '<strong>FV</strong>: final value', '<strong>n</strong>: number of years']),
       example=lambda: f'An investment that grew from {inr(100000)} to {inr(250000)} in 5 years has a CAGR of about <strong>{((250000 / 100000) ** (1 / 5) - 1) * 100:.2f}%</strong>, even though its total return is 150%.',
       faqs=[('What is the difference between CAGR and absolute return?', '<p>Absolute return is the total percentage gain, regardless of time. CAGR spreads that gain evenly over each year, so you can compare investments held for different periods.</p>'),
             ('Does CAGR show volatility?', '<p>No. CAGR smooths out the ups and downs along the way; two investments with the same CAGR can have had very different journeys.</p>'),
             ('Can I use CAGR for SIPs?', '<p>Not directly, because SIP money is invested at different times. For SIPs, XIRR is the right measure; we can calculate it for you.</p>')],
       related=['lumpsum', 'sip', 'inflation', 'compound'], cta=('mutual-funds.html', 'Review your investments'), risk=RISK),

  dict(id='emi', file='emi-calculator.html', name='Loan EMI Calculator', group='loans', icon='house-user',
       short='Monthly EMI for home, car and personal loans.', keywords='emi loan home loan car loan personal loan interest monthly instalment',
       desc='Free loan EMI calculator for home, car and personal loans: see your monthly EMI, total interest and a year-by-year repayment schedule.',
       headline='Monthly EMI', rows=[('Monthly EMI', 'inr'), ('Principal amount', 'inr'), ('Total interest', 'inr'), ('Total amount payable', 'inr')],
       legend=['Principal amount', 'Total interest'],
       presets=[('Home loan', {'amount': 5000000, 'rate': 8.5, 'years': 20}), ('Car loan', {'amount': 800000, 'rate': 9.5, 'years': 5}),
                ('Personal loan', {'amount': 500000, 'rate': 12, 'years': 3})],
       fields=[('amount', 'Loan amount', 10000, 50000000, 10000, 5000000, 'inr', ''),
               ('rate', 'Interest rate (p.a.)', 1, 20, 0.1, 8.5, 'pct', ''),
               ('years', 'Loan tenure', 1, 30, 1, 20, 'yrs', '')],
       table=[('Year', ''), ('Principal paid', 'inr'), ('Interest paid', 'inr'), ('Balance at year end', 'inr')],
       about=['An Equated Monthly Instalment (EMI) is the fixed amount you pay your lender every month until a loan is repaid. Each EMI is part interest and part principal; early on, most of it goes towards interest.',
              'Choose a loan type to load typical values, then adjust the amount, rate and tenure. The year-by-year schedule shows how your balance falls.'],
       formula=('EMI = P × r × (1 + r)<sup>n</sup> ÷ [ (1 + r)<sup>n</sup> − 1 ]',
                ['<strong>P</strong>: loan amount', '<strong>r</strong>: monthly interest rate (annual rate ÷ 12 ÷ 100)', '<strong>n</strong>: number of monthly instalments']),
       example=lambda: f'A home loan of {inr(5000000)} at 8.5% for 20 years has an EMI of about <strong>{inr(emi_amt(5000000, 8.5, 20))}</strong>, and you would pay about {inr(emi_amt(5000000, 8.5, 20) * 240 - 5000000)} in interest over the term.',
       faqs=[('How can I reduce my EMI?', '<p>A longer tenure lowers the EMI but increases the total interest. A larger down payment or a lower interest rate reduces both.</p>'),
             ('Do prepayments help?', '<p>Yes. Part-prepayments reduce the outstanding principal, which cuts the interest you pay. Most floating-rate home loans for individuals have no prepayment charges; check your loan terms.</p>'),
             ('Should I insure my loan?', '<p>If your family would struggle to repay the loan without your income, a term plan that covers the outstanding amount protects them. See our <a href="life-cover-calculator.html">life cover calculator</a>.</p>')],
       related=['hlv', 'fd', 'rd', 'inflation'], cta=('life-insurance.html', 'Protect your loan with life cover'), risk=False),

  dict(id='fd', file='fd-calculator.html', name='FD Calculator', group='savings', icon='building-columns',
       short='Maturity value of a fixed deposit.', keywords='fd fixed deposit bank interest maturity',
       desc='Free FD calculator: find the maturity value and interest earned on a bank fixed deposit with quarterly compounding.',
       headline='Maturity value', rows=[('Amount invested', 'inr'), ('Interest earned', 'inr'), ('Maturity value', 'inr')],
       legend=['Amount invested', 'Interest earned'],
       fields=[('amount', 'Deposit amount', 5000, 50000000, 5000, 100000, 'inr', ''),
               ('rate', 'Interest rate (p.a.)', 1, 15, 0.1, 7, 'pct', 'Check your bank\'s current rate; senior citizens often get a higher rate.'),
               ('years', 'Time period', 1, 10, 1, 5, 'yrs', '')],
       about=['A fixed deposit (FD) earns a fixed rate of interest for a set period. Most Indian banks compound FD interest quarterly, which this calculator assumes.',
              'Interest on FDs is taxable at your income-tax slab rate, and banks may deduct TDS.'],
       formula=('A = P × (1 + r ÷ 4)<sup>4t</sup>', ['<strong>P</strong>: deposit amount', '<strong>r</strong>: annual interest rate', '<strong>t</strong>: time in years (compounded quarterly)']),
       example=lambda: f'A deposit of {inr(100000)} for 5 years at 7% would mature at about <strong>{inr(100000 * (1 + 7 / 400) ** 20)}</strong>.',
       faqs=[('Is FD interest taxable?', '<p>Yes. It is added to your income and taxed at your slab rate. Banks deduct TDS above a threshold unless you submit Form 15G or 15H where eligible.</p>'),
             ('Can I break an FD early?', '<p>Usually yes, but banks may charge a penalty and pay a lower rate for the period the money was held.</p>'),
             ('FD or debt mutual fund?', '<p>FDs offer fixed returns; debt funds offer market-linked returns and more flexibility. We can explain which suits your goal.</p>')],
       related=['rd', 'ppf', 'compound', 'lumpsum'], cta=('financial-checkup.html', 'Get a free financial checkup'), risk=False),

  dict(id='rd', file='rd-calculator.html', name='RD Calculator', group='savings', icon='calendar',
       short='Maturity value of a recurring deposit.', keywords='rd recurring deposit monthly bank post office',
       desc='Free RD calculator: see the maturity value and interest on a monthly recurring deposit with quarterly compounding.',
       headline='Maturity value', rows=[('Amount invested', 'inr'), ('Interest earned', 'inr'), ('Maturity value', 'inr')],
       legend=['Amount invested', 'Interest earned'],
       fields=[('monthly', 'Monthly deposit', 500, 200000, 500, 5000, 'inr', ''),
               ('rate', 'Interest rate (p.a.)', 1, 15, 0.1, 7, 'pct', 'Check your bank\'s current rate.'),
               ('years', 'Time period', 1, 10, 1, 5, 'yrs', '')],
       about=['A recurring deposit (RD) lets you save a fixed amount every month and earn fixed-deposit interest on it. It is a simple way to build a habit of saving for a short-term goal.',
              'This calculator assumes quarterly compounding, as most Indian banks use.'],
       formula=('M = Σ R × (1 + r ÷ 4)<sup>k ÷ 3</sup>', ['<strong>R</strong>: monthly deposit', '<strong>r</strong>: annual interest rate', '<strong>k</strong>: months each instalment stays invested, summed over every instalment']),
       example=lambda: f'Depositing {inr(5000)} a month for 5 years at 7%, you invest {inr(300000)} and the RD would mature at about <strong>{inr(rd_fv(5000, 7, 5))}</strong>.',
       faqs=[('What happens if I miss an instalment?', '<p>Banks usually charge a small penalty for late instalments, and several missed instalments may close the account.</p>'),
             ('Is RD interest taxable?', '<p>Yes, at your income-tax slab rate, like FD interest.</p>'),
             ('RD or SIP?', '<p>An RD gives a fixed return with no market risk; a SIP in mutual funds can grow more over long periods but its value moves with the market.</p>')],
       related=['fd', 'sip', 'ppf', 'compound'], cta=('financial-checkup.html', 'Get a free financial checkup'), risk=False),

  dict(id='ppf', file='ppf-calculator.html', name='PPF Calculator', group='savings', icon='landmark',
       short='Maturity value of your Public Provident Fund.', keywords='ppf public provident fund tax free 80c government',
       desc='Free PPF calculator: estimate the maturity value of your Public Provident Fund account with yearly contributions and a year-by-year table.',
       headline='Maturity value', rows=[('Amount invested', 'inr'), ('Interest earned', 'inr'), ('Maturity value', 'inr')],
       legend=['Amount invested', 'Interest earned'],
       fields=[('yearly', 'Yearly investment', 500, 150000, 500, 150000, 'inr', 'PPF allows ₹500 to ₹1.5 lakh a year.'),
               ('rate', 'Interest rate (p.a.)', 1, 15, 0.1, 7.1, 'pct', 'The government sets the PPF rate every quarter. Check the current rate.'),
               ('years', 'Time period', 15, 50, 5, 15, 'yrs', 'PPF runs for 15 years and can be extended in blocks of 5.')],
       table=[('Year', ''), ('Deposit', 'inr'), ('Interest', 'inr'), ('Balance at year end', 'inr')],
       about=['The Public Provident Fund (PPF) is a government-backed savings scheme with a 15-year term. Deposits qualify for deduction under Section 80C (old tax regime), and the interest and maturity amount are tax-free.',
              'This calculator assumes you deposit the same amount at the start of each year and that the interest rate stays the same.'],
       formula=('Each year: balance = (balance + deposit) × (1 + r)', ['<strong>r</strong>: annual PPF interest rate', 'Deposits made by 5 April earn interest for the whole year']),
       example=lambda: f'Investing {inr(150000)} every year for 15 years at 7.1%, you invest {inr(2250000)} and the account could be worth about <strong>{inr(ppf_fv(150000, 7.1, 15))}</strong> at maturity.',
       faqs=[('Can I withdraw from PPF before 15 years?', '<p>Partial withdrawals are allowed from the 7th financial year, within limits. Loans against the balance are available from the 3rd to the 6th year.</p>'),
             ('Is the PPF rate fixed?', '<p>No. The government reviews it every quarter, so your actual returns may differ from this estimate.</p>'),
             ('What happens after 15 years?', '<p>You can withdraw the full amount, or extend the account in blocks of 5 years, with or without fresh deposits.</p>')],
       related=['fd', 'sip', 'rd', 'compound'], cta=('tax-planning.html', 'Plan your tax savings'), risk=False),

  dict(id='compound', file='compound-interest-calculator.html', name='Compound Interest Calculator', group='savings', icon='percent',
       short='Growth with yearly, quarterly or monthly compounding.', keywords='compound interest compounding frequency growth',
       desc='Free compound interest calculator: see how your money grows with yearly, half-yearly, quarterly or monthly compounding.',
       headline='Total value', rows=[('Principal amount', 'inr'), ('Interest earned', 'inr'), ('Total value', 'inr')],
       legend=['Principal', 'Interest earned'],
       fields=[('amount', 'Principal amount', 1000, 50000000, 1000, 100000, 'inr', ''),
               ('rate', 'Interest rate (p.a.)', 1, 30, 0.1, 8, 'pct', ''),
               ('years', 'Time period', 1, 40, 1, 10, 'yrs', '')],
       select=('freq', 'Compounding frequency', [('1', 'Yearly'), ('2', 'Half-yearly'), ('4', 'Quarterly'), ('12', 'Monthly')], '4'),
       about=['Compound interest is interest earned on both your original money and on the interest it has already earned. The more often interest is compounded, and the longer you stay invested, the faster your money grows.'],
       formula=('A = P × (1 + r ÷ f)<sup>f × t</sup>', ['<strong>P</strong>: principal', '<strong>r</strong>: annual interest rate', '<strong>f</strong>: compounding periods per year', '<strong>t</strong>: time in years']),
       example=lambda: f'{inr(100000)} at 8% for 10 years, compounded quarterly, grows to about <strong>{inr(100000 * (1 + 0.08 / 4) ** 40)}</strong>. Compounded yearly, it would be {inr(100000 * 1.08 ** 10)}.',
       faqs=[('What is the difference between simple and compound interest?', '<p>Simple interest is paid only on your original amount. Compound interest is also paid on interest already earned, so it grows faster over time.</p>'),
             ('Why does compounding frequency matter?', '<p>More frequent compounding adds interest to your balance sooner, so the next period\'s interest is slightly higher. The effect grows with higher rates and longer periods.</p>')],
       related=['fd', 'lumpsum', 'cagr', 'inflation'], cta=('financial-checkup.html', 'Get a free financial checkup'), risk=False),

  dict(id='retirement', file='retirement-calculator.html', name='Retirement Calculator', group='planning', icon='person-cane',
       short='How much you need to retire, and the SIP to get there.', keywords='retirement corpus pension planning',
       desc='Free retirement calculator: estimate the corpus you need at retirement, allowing for inflation, and the monthly SIP needed to build it.',
       headline='Corpus needed at retirement', rows=[('Monthly expenses at retirement', 'inr'), ('Your savings will grow to', 'inr'), ('Shortfall to cover', 'inr'), ('Monthly SIP needed', 'inr')],
       legend=['Covered by current savings', 'Shortfall'],
       fields=[('age', 'Your age today', 18, 65, 1, 35, 'yrs', ''),
               ('retireAge', 'Retirement age', 40, 75, 1, 60, 'yrs', ''),
               ('lifeAge', 'Plan until age', 60, 100, 1, 85, 'yrs', 'Plan for a long life: many people now live into their late 80s.'),
               ('expenses', 'Monthly expenses today', 5000, 500000, 1000, 40000, 'inr', ''),
               ('inflation', 'Expected inflation', 2, 12, 0.5, 6, 'pct', ''),
               ('returnBefore', 'Return before retirement', 4, 16, 0.5, 11, 'pct', ''),
               ('returnAfter', 'Return after retirement', 3, 12, 0.5, 7, 'pct', ''),
               ('savings', 'Retirement savings so far', 0, 50000000, 50000, 500000, 'inr', '')],
       about=['Your retirement savings may need to last 25 years or more, while prices keep rising. This calculator estimates the corpus you need on the day you retire to cover your expenses, rising with inflation, until the age you plan for.',
              'It then shows how much your current savings could grow to, and the monthly SIP needed to close any gap.'],
       formula=('Corpus = yearly expenses at retirement × [ 1 − (1 + g)<sup>−N</sup> ] ÷ g × (1 + g)',
                ['<strong>g</strong>: real return after retirement, (1 + return) ÷ (1 + inflation) − 1', '<strong>N</strong>: years in retirement', 'Expenses at retirement = today\'s expenses × (1 + inflation)<sup>years to retirement</sup>']),
       example=lambda: f'Aged 35 with monthly expenses of {inr(40000)}, retiring at 60 and planning until 85 (6% inflation, 11% return before and 7% after retirement): you may need a corpus of about <strong>{inr(retirement_corpus()[0])}</strong>. With {inr(500000)} saved already, a SIP of about {inr(retirement_corpus()[1])} a month could close the gap.',
       faqs=[('How much will I need to retire?', '<p>It depends on your expenses, inflation, and how long retirement lasts. Use the calculator for an estimate, and book a free checkup to build a plan.</p>'),
             ('When should I start saving?', '<p>As early as possible. Money invested in your 20s and 30s has far longer to grow, so the monthly amount needed is much smaller.</p>'),
             ('How do I get a regular income after retiring?', '<p>Annuities and systematic withdrawal plans are common options. Try our <a href="swp-calculator.html">SWP calculator</a>.</p>')],
       related=['swp', 'sip', 'inflation', 'stepup'], cta=('retirement-planning.html', 'Plan your retirement'), risk=RISK),

  dict(id='hlv', file='life-cover-calculator.html', name='Life Cover Calculator', group='planning', icon='umbrella',
       short='How much life insurance your family needs (HLV).', keywords='life cover life insurance human life value hlv term plan',
       desc='Free life cover calculator using the Human Life Value method: find how much life insurance your family would need to replace your income.',
       headline='Additional cover recommended', rows=[('Income replacement (Human Life Value)', 'inr'), ('Outstanding loans', 'inr'), ('Total cover needed', 'inr'), ('Existing cover and savings', 'inr'), ('Additional cover recommended', 'inr')],
       legend=['Existing cover and savings', 'Additional cover needed'],
       fields=[('age', 'Your age today', 18, 65, 1, 35, 'yrs', ''),
               ('retireAge', 'Planned retirement age', 40, 75, 1, 60, 'yrs', ''),
               ('income', 'Annual income', 100000, 10000000, 50000, 1200000, 'inr', ''),
               ('expensePct', 'Spent on yourself', 10, 60, 5, 30, 'pct', 'The share of your income used for your own expenses, which your family would no longer need.'),
               ('growth', 'Expected income growth', 0, 12, 0.5, 5, 'pct', ''),
               ('discount', 'Discount rate', 4, 12, 0.5, 8, 'pct', 'A rate close to safe long-term returns.'),
               ('loans', 'Outstanding loans', 0, 50000000, 50000, 2000000, 'inr', ''),
               ('cover', 'Existing life cover', 0, 50000000, 50000, 1000000, 'inr', ''),
               ('savings', 'Savings and investments', 0, 50000000, 50000, 500000, 'inr', '')],
       about=['The Human Life Value (HLV) method estimates the value of your future income to your family: the money you would have contributed, after your own expenses, until retirement, in today\'s terms.',
              'Add your outstanding loans, subtract the cover and savings you already have, and the result is the additional life cover to consider.'],
       formula=('HLV = C × [ 1 − ((1 + g) ÷ (1 + d))<sup>n</sup> ] ÷ (d − g)',
                ['<strong>C</strong>: yearly income after your own expenses', '<strong>g</strong>: expected income growth', '<strong>d</strong>: discount rate', '<strong>n</strong>: years to retirement']),
       example=lambda: f'A 35-year-old earning {inr(1200000)} a year and spending 30% on themselves, retiring at 60, has a Human Life Value of about {inr(hlv_gap()[0])}. Adding a {inr(2000000)} home loan and subtracting {inr(1500000)} of existing cover and savings suggests about <strong>{inr(hlv_gap()[1])}</strong> of additional cover.',
       faqs=[('Is HLV the only way to decide my cover?', '<p>No. A quick rule of thumb is 10 to 15 times your annual income plus loans. HLV is more precise because it uses your actual income, expenses and years to retirement.</p>'),
             ('Which policy gives the most cover for the premium?', '<p>A term plan. It pays only if you die during the term, so the premium is far lower than for endowment plans with the same cover.</p>'),
             ('Should I review my cover?', '<p>Yes: after marriage, a child, a new loan or a big pay rise. Book a free checkup and we\'ll review it with you.</p>')],
       related=['emi', 'education', 'retirement', 'inflation'], cta=('life-insurance.html', 'Review your life cover'), risk=False),

  dict(id='education', file='child-education-calculator.html', name='Child Education Calculator', group='planning', icon='graduation-cap',
       short='Future cost of education and the monthly saving needed.', keywords='child education college fees goal planning',
       desc='Free child education calculator: estimate the future cost of your child\'s education and the monthly SIP needed to fund it.',
       headline='Future cost of the course', rows=[('Your savings will grow to', 'inr'), ('Shortfall to cover', 'inr'), ('Monthly SIP needed', 'inr')],
       legend=['Covered by current savings', 'Shortfall'],
       fields=[('cost', 'Cost of the course today', 100000, 10000000, 50000, 1500000, 'inr', ''),
               ('years', 'Years until it\'s needed', 1, 25, 1, 15, 'yrs', ''),
               ('inflation', 'Education inflation', 4, 15, 0.5, 8, 'pct', 'Education costs have typically risen faster than general prices.'),
               ('rate', 'Expected annual return', 4, 16, 0.5, 11, 'pct', ''),
               ('savings', 'Savings set aside so far', 0, 10000000, 25000, 100000, 'inr', '')],
       about=['Education costs in India have risen faster than general prices. This calculator projects today\'s course fee forward using an education inflation rate, then works out the monthly SIP needed to reach it, after allowing for what you have already saved.'],
       formula=('Future cost = today\'s cost × (1 + education inflation)<sup>years</sup>', ['The monthly SIP needed is worked out from the shortfall, the expected return and the months remaining']),
       example=lambda: f'A course costing {inr(1500000)} today may cost about <strong>{inr(1500000 * 1.08 ** 15)}</strong> in 15 years at 8% education inflation.',
       faqs=[('What education inflation should I use?', '<p>Estimates of 8 to 10 percent a year are common for professional courses in India; studying abroad can rise even faster.</p>'),
             ('What if something happens to me before the goal?', '<p>A term plan or a child plan with waiver of premium keeps the goal funded. We can help you size the cover.</p>'),
             ('Is it too late to start for a teenager?', '<p>No, but shorter time frames call for safer investments and a larger monthly amount.</p>')],
       related=['sip', 'stepup', 'inflation', 'hlv'], cta=('child-education.html', 'Plan your child\'s education'), risk=RISK),

  dict(id='inflation', file='inflation-calculator.html', name='Inflation Calculator', group='planning', icon='arrow-trend-up',
       short='What today\'s prices may be in the future.', keywords='inflation future cost purchasing power prices',
       desc='Free inflation calculator: see what today\'s prices may be in the future, and how much your money will be worth.',
       headline='Future cost', rows=[('Cost today', 'inr'), ('Future cost', 'inr'), ('Increase', 'inr'), ('Today\'s amount will be worth', 'inr')],
       legend=['Cost today', 'Increase'],
       fields=[('amount', 'Cost today', 1000, 100000000, 1000, 100000, 'inr', ''),
               ('rate', 'Expected inflation (p.a.)', 1, 15, 0.5, 6, 'pct', ''),
               ('years', 'Time period', 1, 50, 1, 10, 'yrs', '')],
       about=['Inflation means prices rise over time, so the same amount of money buys less in the future. This calculator shows what something costing a given amount today may cost later, and what today\'s money will be worth in future terms.'],
       formula=('Future cost = cost today × (1 + inflation)<sup>years</sup>', ['Value of today\'s money = amount ÷ (1 + inflation)<sup>years</sup>']),
       example=lambda: f'At 6% inflation, something costing {inr(100000)} today may cost about <strong>{inr(100000 * 1.06 ** 10)}</strong> in 10 years, and {inr(100000)} then will buy what about {inr(100000 / 1.06 ** 10)} buys today.',
       faqs=[('Why does inflation matter for planning?', '<p>Goals such as retirement and education are years away, so their future cost is much higher than today\'s price. Plans that ignore inflation fall short.</p>'),
             ('What inflation rate should I use?', '<p>General consumer inflation in India has often been between 4 and 7 percent; education and healthcare costs have often risen faster.</p>')],
       related=['retirement', 'education', 'compound', 'cagr'], cta=('financial-checkup.html', 'Get a free financial checkup'), risk=False),
]
C += [
  dict(id='mfreturns', file='mutual-fund-returns-calculator.html', name='Mutual Fund Returns Calculator', group='invest', icon='chart-pie',
       short='Returns on a SIP or a lumpsum in one place.', keywords='mutual fund returns sip lumpsum one time monthly',
       desc='Free mutual fund returns calculator: estimate the value of a monthly SIP or a one-time lumpsum investment.',
       headline='Estimated value', rows=[('Amount invested', 'inr'), ('Estimated returns', 'inr'), ('Total value', 'inr')],
       legend=['Amount invested', 'Estimated returns'],
       select=[('mode', 'Investment type', [('1', 'SIP (monthly)'), ('2', 'Lumpsum (one-time)')], '1')], selects_first=True,
       fields=[('amount', 'Investment amount', 500, 10000000, 500, 10000, 'inr', 'Monthly amount for a SIP, or the one-time amount for a lumpsum.'),
               ('rate', 'Expected return rate (p.a.)', 1, 30, 0.5, 12, 'pct', 'Returns are not guaranteed.'),
               ('years', 'Time period', 1, 40, 1, 10, 'yrs', '')],
       about=['Mutual fund returns depend on how you invest. A SIP adds a fixed amount every month; a lumpsum puts all the money to work at once.',
              'Choose SIP or lumpsum, enter the amount, an expected return and the time period, and see what your investment could grow to.'],
       formula=('SIP: FV = P × [ (1 + i)<sup>n</sup> − 1 ] ÷ i × (1 + i) · Lumpsum: FV = P × (1 + r)<sup>t</sup>',
                ['<strong>P</strong>: monthly (SIP) or one-time (lumpsum) amount', '<strong>i</strong>: monthly return; <strong>r</strong>: annual return', '<strong>n</strong>: months; <strong>t</strong>: years']),
       example=lambda: f'A SIP of {inr(10000)} a month for 10 years at 12% could grow to about <strong>{inr(sip_fv(10000, 12, 120))}</strong>; a one-time {inr(500000)} at 12% for 10 years could grow to about {inr(500000 * 1.12 ** 10)}.',
       faqs=[('Which is better: SIP or lumpsum?', '<p>A SIP spreads your buying over time and suits regular income. A lumpsum can do better when markets rise steadily, but carries more timing risk.</p>'),
             ('Are these returns guaranteed?', '<p>No. Mutual fund returns vary with the market. The calculator uses a steady rate for illustration only.</p>')],
       related=['sip', 'lumpsum', 'xirr', 'stepup'], cta=('mutual-funds.html', 'Talk to us about investing'), risk=RISK),

  dict(id='xirr', file='xirr-calculator.html', name='XIRR Calculator', group='invest', icon='magnifying-glass-chart',
       short='Your real annual return on a monthly SIP.', keywords='xirr sip return annualised irr internal rate of return',
       desc='Free XIRR calculator for SIPs: find the annualised return on your monthly mutual fund SIP from its current value.',
       headline='XIRR', big_fmt='pct', rows=[('Amount invested', 'inr'), ('Current value', 'inr'), ('Gain', 'inr'), ('Absolute return', 'pct'), ('XIRR (annualised)', 'pct')],
       legend=['Amount invested', 'Gain'],
       fields=[('monthly', 'Monthly SIP amount', 500, 100000, 500, 10000, 'inr', ''),
               ('years', 'SIP period', 1, 30, 1, 5, 'yrs', ''),
               ('value', 'Current value of the investment', 1000, 50000000, 1000, 850000, 'inr', '')],
       about=['XIRR (extended internal rate of return) is the right way to measure the return on a SIP, because each instalment has been invested for a different length of time. It gives one annualised figure you can compare with an FD rate or another fund.',
              'This calculator assumes equal monthly instalments at the start of each month. For irregular amounts or dates, use the XIRR function in a spreadsheet, or ask us.'],
       formula=('Find r such that Σ P × (1 + r)<sup>t<sub>k</sub></sup> = current value',
                ['<strong>P</strong>: each monthly instalment', '<strong>t<sub>k</sub></strong>: years each instalment has been invested', 'Solved numerically (the calculator searches for r)']),
       example=lambda: f'Investing {inr(10000)} a month for 5 years ({inr(600000)} in total), now worth {inr(850000)}, is an XIRR of about <strong>{xirr_sip(10000, 5, 850000):.2f}%</strong> a year, although the absolute return is {(850000 - 600000) / 600000 * 100:.1f}%.',
       faqs=[('Why not use CAGR for a SIP?', '<p>CAGR assumes all the money was invested on day one. With a SIP, later instalments have had less time to grow, so XIRR gives a fairer annual figure.</p>'),
             ('Can XIRR be negative?', '<p>Yes. If the current value is less than what you invested, the XIRR is negative.</p>')],
       related=['cagr', 'sip', 'mfreturns', 'lumpsum'], cta=('mutual-funds.html', 'Review your investments'), risk=RISK),

  dict(id='ssy', file='sukanya-samriddhi-yojana-calculator.html', name='Sukanya Samriddhi Yojana Calculator', group='savings', icon='child-dress',
       short='Maturity value of your daughter\'s SSY account.', keywords='sukanya samriddhi yojana ssy girl child daughter government scheme 80c',
       desc='Free Sukanya Samriddhi Yojana (SSY) calculator: estimate the maturity value of your daughter\'s SSY account, with a year-by-year table.',
       headline='Maturity value', rows=[('Total investment', 'inr'), ('Interest earned', 'inr'), ('Maturity value', 'inr'), ('Daughter\'s age at maturity', 'years')],
       legend=['Amount invested', 'Interest earned'],
       fields=[('yearly', 'Yearly investment', 250, 150000, 250, 100000, 'inr', 'SSY allows ₹250 to ₹1.5 lakh a year.'),
               ('age', 'Daughter\'s age when the account is opened', 0, 10, 1, 2, 'yrs', 'The account can be opened until she turns 10.'),
               ('rate', 'Interest rate (p.a.)', 1, 12, 0.1, 8.2, 'pct', 'The government sets the SSY rate every quarter.')],
       table=[('Year', ''), ('Deposit', 'inr'), ('Interest', 'inr'), ('Balance at year end', 'inr')],
       about=['Sukanya Samriddhi Yojana is a government savings scheme for a girl child. You deposit for 15 years, and the account matures 21 years after it is opened. Deposits qualify under Section 80C (old tax regime), and the interest and maturity amount are tax-free.',
              'This calculator assumes the same deposit at the start of each year and a constant interest rate.'],
       formula=('Years 1–15: balance = (balance + deposit) × (1 + r); years 16–21: balance × (1 + r)', ['<strong>r</strong>: annual SSY interest rate, compounded yearly']),
       example=lambda: f'Depositing {inr(100000)} a year for 15 years ({inr(1500000)} in total) at 8.2% could give about <strong>{inr(ssy_fv(100000, 8.2))}</strong> at maturity.',
       note='Based on the scheme rules for deposits (15 years), maturity (21 years) and the 8.2% rate set for recent quarters. The government revises the rate every quarter.',
       faqs=[('Who can open an SSY account?', '<p>A parent or guardian, for a girl child below 10 years of age, at a post office or authorised bank. Up to two accounts per family are allowed, with exceptions for twins.</p>'),
             ('Can I withdraw early?', '<p>Up to 50% of the balance can be withdrawn for her education once she turns 18. The account can also be closed after 18 for her marriage.</p>')],
       related=['ppf', 'education', 'sip', 'fd'], cta=('child-education.html', 'Plan your daughter\'s future'), risk=False),

  dict(id='epf', file='epf-calculator.html', name='EPF Calculator', group='savings', icon='briefcase',
       short='Your Employees\' Provident Fund balance at 58.', keywords='epf pf provident fund employee employer retirement',
       desc='Free EPF calculator: estimate your Employees\' Provident Fund balance at retirement from your salary, contributions and yearly increments.',
       headline='EPF balance at 58', rows=[('Your contributions', 'inr'), ('Employer contributions (to EPF)', 'inr'), ('Interest earned', 'inr'), ('Balance at 58', 'inr')],
       legend=['Contributions', 'Interest earned'],
       fields=[('salary', 'Monthly basic salary + DA', 5000, 300000, 1000, 30000, 'inr', ''),
               ('age', 'Your age', 18, 57, 1, 30, 'yrs', ''),
               ('contribution', 'Your contribution', 12, 20, 1, 12, 'pct', '12% is standard; more is voluntary (VPF).'),
               ('increase', 'Expected yearly salary increase', 0, 15, 0.5, 5, 'pct', ''),
               ('rate', 'EPF interest rate (p.a.)', 5, 12, 0.05, 8.25, 'pct', 'Declared by EPFO each year.')],
       table=[('Age', ''), ('Total contributions', 'inr'), ('Total interest', 'inr'), ('Balance', 'inr')],
       about=['Both you and your employer contribute 12% of your basic salary and DA every month. Your full share goes to EPF. Of your employer\'s share, 8.33% of wages (on wages up to ₹15,000 a month) goes to the Employees\' Pension Scheme and the rest to your EPF.',
              'Interest accrues on the monthly balance and is credited once a year. This calculator estimates your EPF balance at 58; the pension (EPS) is not included.'],
       formula=('Each month: EPF += your share + (12% of pay − EPS share); interest = Σ monthly balance × r ÷ 12, credited yearly',
                ['EPS share = 8.33% × min(pay, ₹15,000)', '<strong>r</strong>: EPF interest rate declared by EPFO']),
       example=lambda: f'Starting at age 30 on a basic salary of {inr(30000)} a month, rising 5% a year, at 8.25%, your EPF could be worth about <strong>{inr(epf_fv(30000, 30))}</strong> at 58.',
       note='Assumes the standard 12% contributions, the ₹15,000 EPS wage ceiling and an 8.25% interest rate. EPFO declares the rate every year, and the rules may change.',
       faqs=[('Is EPF interest tax-free?', '<p>Interest on your contributions up to ₹2.5 lakh a year (₹5 lakh where the employer does not contribute) is tax-free; interest on amounts above that is taxable.</p>'),
             ('Can I withdraw EPF before retirement?', '<p>Partial withdrawals are allowed for purposes such as housing, education, marriage and medical needs, subject to EPFO rules.</p>')],
       related=['retirement', 'ppf', 'inflation', 'swp'], cta=('retirement-planning.html', 'Plan your retirement'), risk=False),

  dict(id='incometax', file='income-tax-calculator.html', name='Income Tax Calculator', group='tax', icon='file-invoice-dollar',
       short='Compare your tax under the old and new regimes.', keywords='income tax old regime new regime slab 87a salary',
       desc='Free income tax calculator: compare your tax under the old and new regimes for salaried individuals, using FY 2025-26 slabs.',
       headline='Lowest tax payable', rows=[('Taxable income (new regime)', 'inr'), ('Tax under new regime', 'inr'), ('Taxable income (old regime)', 'inr'), ('Tax under old regime', 'inr'), ('Better option', 'regime'), ('You save', 'inr')],
       legend=['New regime tax', 'Old regime tax'],
       fields=[('income', 'Annual salary income', 100000, 10000000, 10000, 1500000, 'inr', ''),
               ('deductions', 'Deductions claimed (old regime)', 0, 1000000, 5000, 200000, 'inr', 'For example 80C, 80D, HRA exemption and home-loan interest.')],
       select=[('agegroup', 'Your age', [('1', 'Below 60'), ('2', '60 to 79'), ('3', '80 and above')], '1')],
       about=['India has two income tax regimes. The new regime has lower slab rates and a higher rebate but allows almost no deductions; the old regime has higher rates but lets you claim deductions such as 80C, 80D and HRA.',
              'Enter your salary and the deductions you would claim, and the calculator shows your tax under both, including the standard deduction, rebate under Section 87A and 4% health and education cess.'],
       formula=('Tax = slab tax on (income − standard deduction − deductions), less rebate, plus surcharge, plus 4% cess',
                ['New regime: standard deduction ₹75,000; no tax up to ₹12 lakh taxable income (rebate u/s 87A)', 'Old regime: standard deduction ₹50,000; rebate up to ₹5 lakh taxable income']),
       example=lambda: f'On a salary of {inr(1500000)} with {inr(200000)} of deductions, tax is about <strong>{inr(tax_new(1500000))}</strong> under the new regime and {inr(tax_old(1500000, 200000))} under the old regime.',
       note='Uses FY 2025-26 slabs (Budget 2025) for salaried individuals. It does not include marginal relief on surcharge, other income or special rates, and tax rules change every year. This is an estimate, not tax advice.',
       faqs=[('Which regime should I choose?', '<p>If your deductions are small, the new regime usually costs less. If you claim large deductions (80C, 80D, HRA, home loan), the old regime may still be better. Compare both each year.</p>'),
             ('Can I switch regimes?', '<p>Salaried individuals can choose each year when filing their return. People with business income have more limited options.</p>')],
       related=['ppf', 'sip', 'gst', 'epf'], cta=('tax-planning.html', 'Plan your tax savings'), risk=False),

  dict(id='gst', file='gst-calculator.html', name='GST Calculator', group='tax', icon='receipt',
       short='Add or remove GST from a price.', keywords='gst goods and services tax cgst sgst inclusive exclusive',
       desc='Free GST calculator: add GST to a price or find the GST included in it, with the CGST and SGST split.',
       headline='Total amount', rows=[('Net amount (before GST)', 'inr'), ('CGST', 'inr'), ('SGST', 'inr'), ('Total GST', 'inr'), ('Total amount', 'inr')],
       legend=['Net amount', 'GST'],
       select=[('mode', 'Calculation', [('1', 'Add GST to the amount'), ('2', 'Amount already includes GST')], '1'),
               ('gstrate', 'GST rate', [('3', '3%'), ('5', '5%'), ('18', '18%'), ('40', '40%')], '18')], selects_first=True,
       fields=[('amount', 'Amount', 100, 10000000, 100, 10000, 'inr', '')],
       about=['GST is added to most goods and services in India. Within a state it is split equally into CGST and SGST; for sales between states it is charged as IGST at the full rate.',
              'Choose whether to add GST to a price or to find the GST already included in it, and pick the rate.'],
       formula=('Add GST: GST = amount × rate · Remove GST: net = amount ÷ (1 + rate), GST = amount − net', ['CGST = SGST = GST ÷ 2 (sales within a state)']),
       example=lambda: f'{inr(10000)} plus 18% GST is <strong>{inr(11800)}</strong>: {inr(900)} CGST + {inr(900)} SGST. A price of {inr(11800)} including 18% GST has a net value of {inr(10000)}.',
       note='Rates shown follow the simplified GST structure (5%, 18% and 40%, plus 3% for items such as gold). Check the rate that applies to your goods or services.',
       faqs=[('What is the difference between CGST, SGST and IGST?', '<p>For sales within a state, GST is split equally between the centre (CGST) and the state (SGST). For sales between states, the full rate is charged as IGST.</p>'),
             ('Is GST charged on insurance premiums?', '<p>GST treatment of insurance premiums has changed in recent reforms and differs by product. Ask us about your policy.</p>')],
       related=['incometax', 'compound', 'inflation', 'cagr'], cta=('financial-checkup.html', 'Get a free financial checkup'), risk=False),
]
BY_ID = {c['id']: c for c in C}



# ---------------------------------------------------------------- Markup helpers
def range_field(cid, key, label, lo, hi, step, val, unit, hint):
    rid = f'{cid}-{key}'
    pre = '<span aria-hidden="true">₹</span>' if unit == 'inr' else ''
    suf = {'pct': '<span aria-hidden="true">%</span>', 'yrs': '<span aria-hidden="true">yrs</span>'}.get(unit, '')
    unit_word = {'inr': 'in rupees', 'pct': 'in percent', 'yrs': 'in years'}[unit]
    h = f'\n            <span class="range-field__hint" id="{rid}-hint">{hint}</span>' if hint else ''
    desc = f' aria-describedby="{rid}-hint"' if hint else ''
    return f'''          <div class="range-field">
            <div class="range-field__top">
              <label for="{rid}">{label}</label>
              <span class="range-field__value">{pre}<input type="number" data-key="{key}" min="{lo}" max="{hi}" step="{step}" value="{val}" inputmode="decimal" aria-label="{label}, {unit_word}">{suf}</span>
            </div>
            <input class="range" type="range" id="{rid}" data-key="{key}" min="{lo}" max="{hi}" step="{step}" value="{val}"{desc}>{h}
          </div>'''


def calc_panel(c):
    parts = []
    if c.get('presets'):
        btns = '\n'.join(f'''            <button class="chip" type="button" aria-pressed="{'true' if i == 0 else 'false'}" data-preset='{json.dumps(vals)}'>{label}</button>'''
                         for i, (label, vals) in enumerate(c['presets']))
        parts.append(f'''          <div class="calc-presets" role="group" aria-label="Loan type">
{btns}
          </div>''')
    selects = c.get('select') or []
    if isinstance(selects, tuple):
        selects = [selects]
    sel_html = []
    for key, label, opts, default in selects:
        options = ''.join(f'<option value="{v}"{" selected" if v == default else ""}>{t}</option>' for v, t in opts)
        sel_html.append(f'''          <div class="field">
            <label for="{c["id"]}-{key}">{label}</label>
            <select class="select" id="{c["id"]}-{key}" data-key="{key}">{options}</select>
          </div>''')
    fields = [range_field(c['id'], *f) for f in c['fields']]
    parts += (sel_html + fields) if c.get('selects_first') else (fields + sel_html)
    rows = '\n'.join(f'            <div><dt>{r}</dt><dd data-fmt="{fmt}">–</dd></div>' for r, fmt in c['rows'])
    legend = '\n'.join(f'            <li><span class="calc__swatch" style="background:{col}"></span><span>{lab}</span></li>'
                       for col, lab in zip(['#9DB9D9', '#00ACA8'], c['legend']))
    table = ''
    if c.get('table'):
        th = ''.join(f'<th scope="col"{f" data-fmt={chr(34)}{fmt}{chr(34)}" if fmt else ""}>{h}</th>' for h, fmt in c['table'])
        table = f'''
      <details class="calc-schedule">
        <summary>{I("table-list")} Year-by-year breakdown</summary>
        <div class="table-wrap">
          <table>
            <thead><tr>{th}</tr></thead>
            <tbody></tbody>
          </table>
        </div>
      </details>'''
    return f'''    <div class="calc-panel" data-calc="{c["id"]}">
      <div class="calc">
        <div class="calc__inputs">
{chr(10).join(parts)}
        </div>
        <div class="calc__result">
          <p class="calc__headline">{c["headline"]}</p>
          <p class="calc__big" data-fmt="{c.get("big_fmt", "inr")}">–</p>
          <div class="calc__chart"><canvas width="240" height="240" role="img" aria-label="Chart"></canvas></div>
          <ul class="calc__legend">
{legend}
          </ul>
          <dl class="calc__rows">
{rows}
          </dl>
          <p class="sr-only calc__summary" aria-live="polite"></p>
          <a class="btn btn--block" href="{c["cta"][0]}">{c["cta"][1]}</a>
          <p class="calc__note">Illustrative estimates only, based on the assumptions you choose. Actual returns, rates and costs will vary.</p>
        </div>
      </div>{table}
    </div>'''


def related_list(c):
    return '\n'.join(f'''            <li><a href="{BY_ID[r]["file"]}">{I(BY_ID[r]["icon"])} {BY_ID[r]["name"]}</a></li>''' for r in c['related'])


# ---------------------------------------------------------------- Pages
def lead(c):
    text = c['desc'].split(': ', 1)[-1]
    return text[0].upper() + text[1:]


def calc_page(c):
    formula, vars_ = c['formula']
    var_list = '\n'.join(f'          <li>{v}</li>' for v in vars_)
    about = '\n        '.join(f'<p>{p}</p>' for p in c['about'])
    risk = f'\n        {MF_RISK}' if c.get('risk') else ''
    note = (f'\n        <!-- TODO: check these rules/rates against the current financial year -->\n        <div class="notice">{I("shield")}<p>{c["note"]}</p></div>') if c.get('note') else ''
    body = main(
        banner(c['name'], [('Calculators', 'calculators.html'), (c['name'], None)], lead(c), img='calculators'),
        f'''  <section class="section bg-alt" aria-label="{c["name"]}">
    <div class="container">
      <noscript><p class="notice">This calculator needs JavaScript. Please enable it, or <a href="contact.html">contact us</a> for a personal estimate.</p></noscript>
{calc_panel(c)}
    </div>
  </section>''',
        f'''  <section class="section" aria-labelledby="about-title">
    <div class="container with-aside">
      <div class="prose">
        <h2 id="about-title">About the {c["name"].replace(" Calculator", "").replace("Loan ", "loan ")} calculator</h2>
        {about}

        <h2>How to use it</h2>
        <ol>
          <li>Move the sliders, or type a value into each box.</li>
          <li>Watch the results and chart update as you go.</li>
          <li>Try different assumptions to see what changes the outcome most, then talk to us about a plan.</li>
        </ol>

        <h2>The formula</h2>
        <p class="formula"><code>{formula}</code></p>
        <ul>
{var_list}
        </ul>

        <h2>Example</h2>
        <p>{c["example"]()}</p>{risk}{note}
      </div>
      <aside class="aside-sticky" aria-label="Related calculators">
        <nav class="aside-card" aria-label="Related calculators">
          <h2>Related calculators</h2>
          <ul class="service-nav">
{related_list(c)}
          </ul>
          <a class="link-arrow mt-6" href="calculators.html">All calculators {I("arrow-right")}</a>
        </nav>
        <div class="aside-card aside-card--brand">
          <h2>Want a plan, not just a number?</h2>
          <p>Book a free financial checkup and we'll turn these estimates into a plan.</p>
          <a class="btn btn--block mt-6" href="financial-checkup.html">Book Free Checkup</a>
        </div>
      </aside>
    </div>
  </section>''',
        faq(c['faqs'], 'faq', heading=f'{c["name"]}: common questions'),
        cta_band('Want a plan, not just a number?', 'Book a free financial checkup and we\'ll turn these estimates into a plan that fits your life.'),
    )
    page(c['file'], c['name'], c['desc'], body, sub_current=c['file'], banner_img='calculators',
         extra_scripts=AOS_JS + '\n' + CHART_JS + '\n' + CALC_JS)


def hub():
    groups = []
    for gid, gname, gicon in GROUPS:
        cards = '\n'.join(f'''          <li class="calc-card" data-keywords="{c["name"].lower()} {c["keywords"]}">
            <a href="{c["file"]}">
              <span class="icon-circle">{I(c["icon"])}</span>
              <span class="calc-card__text"><strong>{c["name"]}</strong><span>{c["short"]}</span></span>
              {I("arrow-right", "calc-card__arrow")}
            </a>
          </li>''' for c in C if c['group'] == gid)
        groups.append(f'''      <section class="calc-group" aria-labelledby="group-{gid}">
        <h2 id="group-{gid}">{I(gicon)} {gname}</h2>
        <ul class="calc-grid">
{cards}
        </ul>
      </section>''')
    body = main(
        banner('Financial Calculators', [('Calculators', None)], f'{len(C)} free calculators for investing, loans, savings and planning. Pick one to get a quick, illustrative estimate.', img='calculators'),
        f'''  <section class="section bg-alt" aria-label="All calculators">
    <div class="container">
      <div class="calc-search" data-aos="fade-up">
        <label for="calc-search">Find a calculator</label>
        <input class="input" id="calc-search" type="search" placeholder="Try &quot;EMI&quot;, &quot;SIP&quot; or &quot;retirement&quot;" autocomplete="off" data-calc-search>
        <p class="calc-search__count" aria-live="polite" data-calc-count></p>
      </div>
{chr(10).join(groups)}
      <p class="notice" hidden data-calc-empty>{I("magnifying-glass-chart")}<span>No calculator matches that search. <a href="contact.html">Ask us</a> and we'll work it out with you.</span></p>
      <div class="mt-6">{MF_RISK}</div>
    </div>
  </section>''',
        cta_band('Want a plan, not just a number?', 'Book a free financial checkup and we\'ll turn these estimates into a plan that fits your life.'),
    )
    page('calculators.html', 'Financial Calculators', 'Free financial calculators: SIP, step-up SIP, lumpsum, SWP, CAGR, loan EMI, FD, RD, PPF, compound interest, retirement, life cover and more.',
         body, sub_current='calculators.html', banner_img='calculators', extra_scripts=AOS_JS + '\n' + CALC_JS)


def build_all_calcs():
    hub()
    for c in C:
        calc_page(c)


if __name__ == '__main__':
    build_all_calcs()
