"""Blog / Financial Education content (data only; layout lives in pages_blog.py).

Each article: slug (becomes blog-<slug>.html), category key, title, excerpt, date (ISO), minutes,
featured (shown on the home page), body (HTML: h2/h3, p, ul/ol), notice ('mf' | 'tax' | 'legal' | None).
Content is general education, not personal advice. Worked examples match the site's calculators.
"""

CATEGORIES = [
    ('insurance', 'Insurance', 'shield-heart'),
    ('investments', 'Investments', 'chart-line'),
    ('retirement', 'Retirement', 'person-cane'),
    ('tax', 'Tax', 'file-invoice-dollar'),
    ('family-planning', 'Family Planning', 'people-roof'),
]

ARTICLES = [
  dict(slug='how-much-life-insurance-do-you-need', category='insurance', date='2026-09-01', minutes=6, featured=False,
       title='How Much Life Insurance Do You Really Need?',
       excerpt='A simple way to work out the right life cover for your family, and the common mistakes to avoid.',
       body='''
<p><strong>Life insurance exists for one reason: to replace your income if you are no longer there to earn it.</strong> The right amount depends on what your family would need, not on what a policy happens to offer.</p>
<h2>Start with the rule of thumb</h2>
<p>A common starting point is cover of <strong>10 to 15 times your annual income</strong>. For someone earning ₹10 lakh a year, that means ₹1 crore to ₹1.5 crore. It is quick, but it ignores loans, savings and the age of your children.</p>
<h2>A better way: add up what your family would need</h2>
<ol>
  <li><strong>Income replacement:</strong> the income your family would lose, less what you spend on yourself, until you would have retired.</li>
  <li><strong>Loans:</strong> your home loan, car loan and any other debts.</li>
  <li><strong>Big goals:</strong> children's education and marriage, if you want them funded regardless.</li>
  <li><strong>Minus what you already have:</strong> existing life cover, savings and investments.</li>
</ol>
<p>This is the Human Life Value approach. Our <a href="life-cover-calculator.html">life cover calculator</a> does the maths in a minute.</p>
<h2>Term or endowment?</h2>
<p>A <a href="term-insurance.html">term plan</a> gives the most cover for the least premium because it pays only on death. Endowment and money-back plans also return money if you survive, so the same premium buys far less cover.</p>
<h2>Common mistakes</h2>
<ul>
  <li>Buying cover based only on the premium you can spare.</li>
  <li>Forgetting to include loans.</li>
  <li>Relying only on employer group cover, which ends when you leave the job.</li>
  <li>Not updating nominees after marriage or the birth of a child.</li>
</ul>'''),

  dict(slug='health-insurance-basics', category='insurance', date='2026-09-08', minutes=6, featured=True,
       title='Health Insurance Basics: What to Check Before You Buy',
       excerpt='Room-rent limits, waiting periods, co-payment and network hospitals: the details that decide whether a claim is paid in full.',
       body='''
<p>Two health policies with the same sum insured can pay very different amounts when you are admitted to hospital. The difference is in the details. Here is what to look for.</p>
<h2>1. Sum insured and type of policy</h2>
<ul>
  <li><strong>Individual policy:</strong> each person has their own sum insured.</li>
  <li><strong>Family floater:</strong> one sum insured shared by the family. Usually cheaper for young families.</li>
  <li><strong>Top-up / super top-up:</strong> extra cover that starts after a set amount, a low-cost way to increase protection.</li>
</ul>
<h2>2. Room-rent limits</h2>
<p>Some policies cap the room rent, for example at 1% of the sum insured per day. If you choose a costlier room, other charges may be reduced in proportion too. Look for policies with no room-rent cap or a generous one.</p>
<h2>3. Waiting periods</h2>
<p>Most policies do not cover certain illnesses, and conditions you already have, for an initial period, often two to four years. Starting early means these periods are over before you are more likely to need them.</p>
<h2>4. Co-payment and sub-limits</h2>
<p>A co-payment means you pay a share of every claim, say 10% or 20%. Sub-limits cap what is paid for specific treatments. Both lower the premium, but they also lower what you receive.</p>
<h2>5. Network hospitals and claims</h2>
<p>At a network hospital the insurer can settle the bill directly (cashless). Check that good hospitals near you are in the network, and how claims are handled.</p>
<h2>A quick checklist</h2>
<ul>
  <li>Is the sum insured enough for a major illness in a good hospital in your city?</li>
  <li>Any room-rent cap, co-payment or disease sub-limits?</li>
  <li>How long are the waiting periods?</li>
  <li>Does cover continue for life, and what happens to the premium as you age?</li>
</ul>
<p>Learn more about <a href="health-insurance.html">health insurance</a>, or read <a href="blog-section-80d-explained.html">Section 80D explained</a> for the tax benefit.</p>'''),

  dict(slug='term-insurance-explained', category='insurance', date='2026-08-25', minutes=5, featured=False,
       title='Term Insurance Explained in Plain Language',
       excerpt='Why term insurance gives the largest cover for the lowest premium, and how to choose the right policy term and riders.',
       body='''
<p>Term insurance is the simplest kind of life insurance: you pay a premium for a fixed period, and if you die during that period your family receives the sum assured. If you survive, nothing is paid back. That is exactly why it is so affordable.</p>
<h2>Why choose term insurance?</h2>
<ul>
  <li><strong>High cover, low cost:</strong> the same premium that buys a small endowment policy can buy a far larger term cover.</li>
  <li><strong>Clear purpose:</strong> it protects your family's income, loans and goals, nothing else.</li>
  <li><strong>Fixed premium:</strong> usually locked when you buy, so starting younger costs less for the whole term.</li>
</ul>
<h2>Choosing the policy term</h2>
<p>Choose cover that lasts until your responsibilities are likely to be over: loans repaid and children independent. For many people that means until age 60 or 65.</p>
<h2>Riders worth knowing</h2>
<ul>
  <li><strong>Accidental death benefit:</strong> extra payout if death is due to an accident.</li>
  <li><strong>Critical illness:</strong> a lump sum on diagnosis of listed illnesses.</li>
  <li><strong>Waiver of premium:</strong> future premiums are waived if you become disabled.</li>
</ul>
<h2>The one rule you must follow</h2>
<p>Disclose everything honestly when you apply: smoking, alcohol, existing illnesses and other policies. Non-disclosure is a common reason claims are disputed.</p>
<p>See how much cover you may need with our <a href="life-cover-calculator.html">life cover calculator</a>, or read about <a href="term-insurance.html">term insurance</a>.</p>'''),

  dict(slug='sip-basics-beginners-guide', category='investments', date='2026-09-15', minutes=5, featured=True,
       title="SIP Basics: A Beginner's Guide",
       excerpt='Understand how Systematic Investment Plans work and how they can help you build a long-term investment habit.',
       body='''
<p>A Systematic Investment Plan (SIP) lets you invest a fixed amount in a mutual fund at regular intervals, usually every month, by automatic debit from your bank account. It is one of the simplest ways to start investing.</p>
<h2>How a SIP works</h2>
<p>Each instalment buys units of the fund at that day's price. When prices are low you get more units; when prices are high you get fewer. Over time this averages out your purchase cost, which is called <strong>rupee-cost averaging</strong>.</p>
<h2>An example</h2>
<p>Suppose you invest ₹10,000 a month for 10 years, a total of ₹12 lakh. If the investment earned 12% a year, it could grow to about ₹23.2 lakh. If it earned less, or if markets fell near the end, it would be worth less. <strong>Returns are not guaranteed</strong>; the figures only show how compounding works.</p>
<h2>Why SIPs suit beginners</h2>
<ul>
  <li><strong>Discipline:</strong> investing happens automatically every month.</li>
  <li><strong>Small start:</strong> many SIPs can begin from a few hundred rupees.</li>
  <li><strong>No timing:</strong> you do not need to guess the "right" moment to invest.</li>
  <li><strong>Flexibility:</strong> you can usually increase, pause or stop a SIP.</li>
</ul>
<h2>Getting started</h2>
<ol>
  <li>Decide what you are investing for and when you need the money.</li>
  <li>Complete KYC with your PAN, Aadhaar and bank details.</li>
  <li>Choose a scheme that matches your goal and comfort with risk.</li>
  <li>Set up the SIP and review it once a year; consider stepping it up as your income grows.</li>
</ol>
<p>Try our <a href="sip-calculator.html">SIP calculator</a> or <a href="step-up-sip-calculator.html">step-up SIP calculator</a>, or read about <a href="sip-investment.html">SIP investment</a>.</p>'''),

  dict(slug='common-investment-mistakes', category='investments', date='2026-08-18', minutes=5, featured=False,
       title='7 Common Investment Mistakes and How to Avoid Them',
       excerpt='From chasing past returns to stopping SIPs in a falling market: simple habits that protect your long-term wealth.',
       body='''
<p>Most investment mistakes are not about choosing the wrong fund. They are about behaviour. Here are seven common ones, and how to avoid them.</p>
<ol>
  <li><strong>Investing without a goal.</strong> Link every investment to a purpose and a date, so you know how much risk you can take.</li>
  <li><strong>Chasing last year's top performer.</strong> Past performance does not guarantee future returns. Look at consistency, costs and fit with your goal.</li>
  <li><strong>Stopping SIPs when markets fall.</strong> Falling markets mean your SIP buys more units. Stopping at that point can hurt long-term results.</li>
  <li><strong>Putting everything in one place.</strong> Spread your money across asset types so one bad patch does not undo your plan.</li>
  <li><strong>Ignoring inflation.</strong> Money that earns less than inflation loses buying power every year.</li>
  <li><strong>Skipping insurance.</strong> Without health and life cover, one emergency can force you to sell investments at the wrong time.</li>
  <li><strong>Never reviewing.</strong> Check your plan once a year and after big life changes.</li>
</ol>
<h2>A simple habit to start with</h2>
<p>Before any investment, ask three questions: What is this money for? When will I need it? What happens if it falls 20% in the short term? If you are unsure, it is worth talking to someone first.</p>
<p>Related: <a href="blog-sip-basics-beginners-guide.html">SIP basics</a> and <a href="wealth-creation.html">wealth creation</a>.</p>'''),

  dict(slug='how-much-do-you-need-to-retire', category='retirement', date='2026-09-22', minutes=6, featured=True,
       title='How Much Do You Need for Retirement?',
       excerpt='A step-by-step way to estimate your retirement corpus, allowing for inflation and a long retirement.',
       body='''
<p>Most of us will spend 20 to 30 years in retirement, and prices keep rising throughout. Estimating your target corpus is the first step to a plan that works.</p>
<h2>Step 1: Today's monthly expenses</h2>
<p>Start with what you spend today and remove costs that will end, such as EMIs and children's school fees.</p>
<h2>Step 2: Allow for inflation</h2>
<p>At 6% inflation, ₹40,000 of monthly expenses today becomes about <strong>₹1.72 lakh a month in 25 years</strong>. This is the single biggest factor people underestimate.</p>
<h2>Step 3: How long retirement lasts</h2>
<p>Plan for a long life, at least to 85. Your savings must keep paying out, and keep growing a little, throughout.</p>
<h2>Step 4: The corpus</h2>
<p>For someone aged 35 who plans to retire at 60, with ₹40,000 of monthly expenses today, 6% inflation and a 7% return after retirement, the corpus needed at 60 could be around <strong>₹4.6 crore</strong>. That figure surprises most people, which is why starting early matters so much.</p>
<h2>Step 5: Close the gap</h2>
<p>Subtract what your existing savings may grow to, then work out the monthly investment needed for the rest. Our <a href="retirement-calculator.html">retirement calculator</a> does all five steps for you.</p>
<h2>Do not forget</h2>
<ul>
  <li>Health insurance that continues after your employer's cover ends.</li>
  <li>An emergency fund, separate from your retirement corpus.</li>
  <li>A plan for a regular income, such as a <a href="swp-calculator.html">systematic withdrawal plan</a>.</li>
</ul>
<p>These examples are estimates based on assumptions; actual returns and costs will vary. Read more about <a href="retirement-planning.html">retirement planning</a>.</p>'''),

  dict(slug='start-retirement-planning-early', category='retirement', date='2026-08-11', minutes=4, featured=False,
       title='Why Starting Retirement Planning Early Makes a Big Difference',
       excerpt='Ten extra years of saving can matter more than doubling your contribution. Here is how compounding works in your favour.',
       body='''
<p>The most powerful tool in retirement planning is not a particular investment. It is time.</p>
<h2>The power of compounding</h2>
<p>When your investments earn returns, those returns can earn returns too. The longer this continues, the faster your money grows, so the money you invest in your 20s and 30s has the most time to work.</p>
<h2>An illustration</h2>
<p>Two people each invest ₹5,000 a month, assuming the same 10% annual return:</p>
<ul>
  <li><strong>Asha starts at 25</strong> and invests until 60: 35 years.</li>
  <li><strong>Ravi starts at 35</strong> and invests until 60: 25 years.</li>
</ul>
<p>Asha invests only ₹6 lakh more than Ravi, but because her money has ten extra years to compound, she could end up with more than twice as much. The exact figures depend on actual returns, which are not guaranteed, but the pattern holds.</p>
<h2>What if you are starting late?</h2>
<ul>
  <li>Invest a larger share of your income now.</li>
  <li>Increase your SIP every year with a <a href="step-up-sip-calculator.html">step-up</a>.</li>
  <li>Consider working a little longer or adjusting your retirement lifestyle.</li>
</ul>
<p>Whatever your age, the best time to start is today. See <a href="blog-how-much-do-you-need-to-retire.html">how much you need for retirement</a>.</p>'''),

  dict(slug='section-80c-explained', category='tax', date='2026-09-12', minutes=5, featured=True, notice='tax',
       title='Section 80C Explained: Your Guide to Tax-Saving Investments',
       excerpt='What qualifies under Section 80C, how the ₹1.5 lakh limit works, and how to choose options that also serve your goals.',
       body='''
<p>Section 80C of the Income-tax Act lets you reduce your taxable income by up to <strong>₹1.5 lakh a year</strong> through certain investments and payments. It is available <strong>only under the old tax regime</strong>.</p>
<h2>What qualifies under 80C?</h2>
<ul>
  <li><strong>Life insurance premiums</strong> for yourself, your spouse and children.</li>
  <li><strong>ELSS mutual funds:</strong> equity funds with a 3-year lock-in, the shortest among 80C options.</li>
  <li><strong>PPF:</strong> a 15-year government-backed scheme with tax-free interest.</li>
  <li><strong>Employee Provident Fund (EPF)</strong> contributions.</li>
  <li><strong>Sukanya Samriddhi Yojana</strong> for a girl child.</li>
  <li><strong>National Savings Certificate (NSC)</strong> and 5-year tax-saver fixed deposits.</li>
  <li><strong>Home loan principal repayment</strong> and children's tuition fees (up to two children).</li>
</ul>
<h2>Choose for the goal, not just the tax</h2>
<p>Your EPF contribution may already use part of the limit. For the rest, pick options that fit a real goal: PPF or SSY for safe long-term saving, ELSS for long-term growth, term insurance for protection.</p>
<h2>Old regime or new?</h2>
<p>The new regime has lower rates but does not allow 80C deductions. Whether 80C is worth it depends on your income and your total deductions. Compare both with our <a href="income-tax-calculator.html">income tax calculator</a>.</p>
<h2>Plan early</h2>
<p>Spread tax-saving investments through the year instead of rushing in March. Read about <a href="tax-planning.html">tax planning</a> and <a href="blog-section-80d-explained.html">Section 80D</a>.</p>'''),

  dict(slug='section-80d-explained', category='tax', date='2026-08-28', minutes=4, featured=False, notice='tax',
       title='Section 80D Explained: Tax Benefits on Health Insurance',
       excerpt='How much you can deduct for health insurance premiums for your family and your parents, and what else qualifies.',
       body='''
<p>Section 80D lets you deduct premiums paid for health insurance from your taxable income, separately from the Section 80C limit. Like 80C, it is available <strong>only under the old tax regime</strong>.</p>
<h2>The limits</h2>
<ul>
  <li><strong>Yourself, spouse and children:</strong> up to ₹25,000 a year (₹50,000 if you are a senior citizen).</li>
  <li><strong>Parents:</strong> an additional ₹25,000 (₹50,000 if either parent is a senior citizen).</li>
  <li><strong>Preventive health check-ups:</strong> up to ₹5,000, within the limits above.</li>
</ul>
<h2>An example</h2>
<p>If you are 40 and pay ₹22,000 for your family floater, and ₹38,000 for a policy for your senior-citizen parents, you could claim ₹22,000 + ₹38,000 = <strong>₹60,000</strong> under 80D.</p>
<h2>Points to remember</h2>
<ul>
  <li>Pay premiums by any mode other than cash to claim the deduction (cash is allowed only for preventive check-ups).</li>
  <li>Keep premium receipts for your employer or your return.</li>
  <li>Buy health cover for its protection first; the tax saving is a bonus.</li>
</ul>
<p>Read <a href="blog-health-insurance-basics.html">health insurance basics</a> or <a href="blog-section-80c-explained.html">Section 80C explained</a>.</p>'''),

  dict(slug='child-education-planning-guide', category='family-planning', date='2026-09-18', minutes=5, featured=True,
       title="Planning for Your Child's Education: A Step-by-Step Guide",
       excerpt="Education costs rise faster than prices in general. Here is how to set a target and build the savings in time.",
       body='''
<p>A professional degree in India, or a course abroad, can cost many times today's fees by the time your child is ready. A clear plan takes the stress out of it.</p>
<h2>Step 1: Choose the goal</h2>
<p>Pick a likely course and country, and find today's total cost: tuition, accommodation and living expenses.</p>
<h2>Step 2: Allow for education inflation</h2>
<p>Education costs often rise by 8% to 10% a year. At 8%, a course costing ₹15 lakh today could cost about <strong>₹47.6 lakh in 15 years</strong>.</p>
<h2>Step 3: Work out the monthly saving</h2>
<p>Subtract what your existing savings may grow to, then calculate the monthly investment needed for the rest. Our <a href="child-education-calculator.html">child education calculator</a> does this for you.</p>
<h2>Step 4: Choose the right mix</h2>
<ul>
  <li><strong>10 or more years away:</strong> long-term SIPs in growth-oriented funds can play a larger role.</li>
  <li><strong>3 to 5 years away:</strong> gradually move money into safer options.</li>
  <li><strong>For daughters:</strong> consider <a href="sukanya-samriddhi-yojana-calculator.html">Sukanya Samriddhi Yojana</a> as a safe component.</li>
</ul>
<h2>Step 5: Protect the plan</h2>
<p>If something happened to you, would the savings continue? Adequate <a href="term-insurance.html">term cover</a>, or a child plan with waiver of premium, keeps the goal funded.</p>
<p>Read more about <a href="child-education.html">child education planning</a>.</p>'''),

  dict(slug='building-a-family-financial-plan', category='family-planning', date='2026-08-04', minutes=6, featured=False,
       title='Building a Financial Plan for Your Family',
       excerpt='Protection, an emergency fund, goals and a will: the five building blocks of a family financial plan, in the right order.',
       body='''
<p>A family financial plan does not need to be complicated. It needs the right building blocks, in the right order.</p>
<h2>1. Protection first</h2>
<ul>
  <li><strong>Life cover</strong> for each earning member, typically 10 to 15 times income plus loans.</li>
  <li><strong>Health cover</strong> for everyone, through a family floater or separate policies.</li>
</ul>
<h2>2. An emergency fund</h2>
<p>Keep three to six months of expenses somewhere safe and easy to access, so a job loss or emergency does not force you to break long-term investments.</p>
<h2>3. List your goals</h2>
<p>Write down each goal with a cost and a date: a home, children's education and marriage, retirement, travel. Our article on <a href="blog-child-education-planning-guide.html">education planning</a> shows how to put a number on one.</p>
<h2>4. Invest for each goal</h2>
<p>Match each goal with an investment that suits its time frame: safer options for short-term goals, growth-oriented options such as <a href="blog-sip-basics-beginners-guide.html">SIPs</a> for long-term ones.</p>
<h2>5. Protect what you have built</h2>
<p>Keep nominations up to date on every policy and investment, and make a will with a lawyer so your family is not left with paperwork and disputes. See <a href="estate-planning.html">estate planning</a>.</p>
<h2>Review every year</h2>
<p>Check your plan each year and after big events such as marriage, a new child or a change of job.</p>
<p>Not sure where to start? A <a href="financial-checkup.html">free financial checkup</a> is a good first step.</p>'''),
]
