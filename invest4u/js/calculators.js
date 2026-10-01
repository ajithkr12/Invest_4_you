/* ==========================================================================
   Invest 4U Solutions: financial calculators
   Used by calculators.html (hub: search + legacy links) and every *-calculator.html page.

   Each calculator panel is [data-calc="<id>"]. Inputs are a .range slider plus a paired
   number input sharing data-key, or a <select data-key>. Outputs:
     .calc__big[data-fmt]            headline figure
     .calc__rows dd[data-fmt]        one <dd> per row returned by the calculator
     canvas                          doughnut (Chart.js), optional
     .calc-schedule table            year-by-year table, optional
     [data-preset]                   buttons that load a set of input values
   Formats: inr, pct, months. Results are illustrative only.
   ========================================================================== */
(function () {
  'use strict';

  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var COLORS = ['#9DB9D9', '#00ACA8']; // light steel blue + logo teal, both visible on the dark result panel

  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }

  var inr = new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR', maximumFractionDigits: 0 });
  function money(n) {
    var r = Math.round(n);
    return r < 0 ? '−' + inr.format(-r) : inr.format(r);   // losses keep their sign
  }

  function format(fmt, n) {
    if (fmt === 'pct') return (isFinite(n) ? n : 0).toFixed(2) + '%';
    if (fmt === 'months') {
      var m = Math.round(n);
      var y = Math.floor(m / 12);
      var r = m % 12;
      return (y ? y + (y === 1 ? ' yr' : ' yrs') : '') + (y && r ? ' ' : '') + (r || !y ? r + (r === 1 ? ' mth' : ' mths') : '');
    }
    if (fmt === 'years') return Math.round(n) + ' yrs';
    if (fmt === 'regime') return n === 1 ? 'New regime' : n === 2 ? 'Old regime' : 'Same either way';
    return money(n);
  }

  /* ---------- Shared maths ---------- */
  // Future value of a monthly SIP (payments at the start of each month)
  function sipFV(monthly, annualRate, months) {
    var i = annualRate / 12 / 100;
    if (!i) return monthly * months;
    return monthly * ((Math.pow(1 + i, months) - 1) / i) * (1 + i);
  }
  // Monthly SIP needed to reach a target
  function sipNeeded(target, annualRate, months) {
    if (target <= 0 || months <= 0) return 0;
    var i = annualRate / 12 / 100;
    if (!i) return target / months;
    return target * i / ((Math.pow(1 + i, months) - 1) * (1 + i));
  }

  // Indian income tax: slab tax for [upTo, rate] bands
  function slabTax(income, bands) {
    var tax = 0, prev = 0;
    for (var i = 0; i < bands.length; i++) {
      var cap = bands[i][0];
      if (income > prev) tax += (Math.min(income, cap) - prev) * bands[i][1];
      prev = cap;
    }
    return tax;
  }
  // Surcharge on income tax (no marginal relief on surcharge, see page note)
  function surcharge(tax, taxable) {
    return tax * (taxable > 10000000 ? 0.15 : taxable > 5000000 ? 0.10 : 0);
  }

  /* ---------- Calculators: each returns { big, rows, chart, table?, summary } ---------- */
  var CALCS = {
    sip: function (v) {
      var months = v.years * 12;
      var total = sipFV(v.monthly, v.rate, months);
      var invested = v.monthly * months;
      return {
        big: total,
        rows: [invested, total - invested, total],
        chart: [['Amount invested', invested], ['Estimated returns', total - invested]],
        summary: 'Investing ' + money(v.monthly) + ' a month for ' + v.years + ' years could grow to about ' + money(total) + '.'
      };
    },

    stepup: function (v) {
      var i = v.rate / 12 / 100;
      var bal = 0, invested = 0, table = [];
      for (var y = 0; y < v.years; y++) {
        var m = v.monthly * Math.pow(1 + v.stepup / 100, y);
        for (var k = 0; k < 12; k++) { bal = (bal + m) * (1 + i); invested += m; }
        table.push([y + 1, m, invested, bal]);
      }
      var flat = sipFV(v.monthly, v.rate, v.years * 12);
      return {
        big: bal,
        rows: [invested, bal - invested, bal, flat],
        chart: [['Amount invested', invested], ['Estimated returns', bal - invested]],
        table: table,
        summary: 'Raising your SIP by ' + v.stepup + '% a year could grow it to about ' + money(bal) + ', compared with ' + money(flat) + ' without a step-up.'
      };
    },

    lumpsum: function (v) {
      var total = v.amount * Math.pow(1 + v.rate / 100, v.years);
      return {
        big: total,
        rows: [v.amount, total - v.amount, total],
        chart: [['Amount invested', v.amount], ['Estimated returns', total - v.amount]],
        summary: money(v.amount) + ' invested for ' + v.years + ' years could grow to about ' + money(total) + '.'
      };
    },

    swp: function (v) {
      // Each month: withdraw at the start, then the remaining balance earns a month's return
      var i = v.rate / 12 / 100;
      var bal = v.amount, withdrawn = 0, lasted = 0, table = [], yearOut = 0;
      for (var m = 1; m <= v.years * 12; m++) {
        if (bal > 0) {
          var w = Math.min(v.withdrawal, bal);
          bal = (bal - w) * (1 + i);
          withdrawn += w;
          yearOut += w;
          if (w >= v.withdrawal) lasted = m;
        }
        if (m % 12 === 0) { table.push([m / 12, yearOut, withdrawn, bal]); yearOut = 0; }
      }
      var fullTerm = lasted >= v.years * 12;
      return {
        big: bal,
        rows: [v.amount, withdrawn, bal, lasted],
        chart: [['Total withdrawn', withdrawn], ['Final value', bal]],
        table: table,
        summary: fullTerm
          ? 'Withdrawing ' + money(v.withdrawal) + ' a month, your investment could last the full ' + v.years + ' years and still be worth about ' + money(bal) + '.'
          : 'At ' + money(v.withdrawal) + ' a month, your money may run out after ' + format('months', lasted) + '.'
      };
    },

    cagr: function (v) {
      var years = Math.max(v.years, 0.1);
      var cagr = v.initial > 0 ? (Math.pow(v.final / v.initial, 1 / years) - 1) * 100 : 0;
      var abs = v.initial > 0 ? (v.final - v.initial) / v.initial * 100 : 0;
      return {
        big: cagr,
        rows: [v.initial, v.final, abs, cagr],
        chart: [['Initial value', v.initial], ['Growth', Math.max(0, v.final - v.initial)]],
        summary: 'Growing from ' + money(v.initial) + ' to ' + money(v.final) + ' in ' + v.years + ' years is a CAGR of ' + format('pct', cagr) + '.'
      };
    },

    emi: function (v) {
      var r = v.rate / 12 / 100;
      var n = Math.round(v.years * 12);
      var emi = r ? v.amount * r * Math.pow(1 + r, n) / (Math.pow(1 + r, n) - 1) : v.amount / n;
      var total = emi * n;
      var bal = v.amount, table = [], yp = 0, yi = 0;
      for (var m = 1; m <= n; m++) {
        var interest = bal * r;
        var principal = Math.min(emi - interest, bal);
        bal -= principal; yp += principal; yi += interest;
        if (m % 12 === 0 || m === n) { table.push([Math.ceil(m / 12), yp, yi, Math.max(0, bal)]); yp = 0; yi = 0; }
      }
      return {
        big: emi,
        rows: [emi, v.amount, total - v.amount, total],
        chart: [['Principal amount', v.amount], ['Total interest', total - v.amount]],
        table: table,
        summary: 'Your EMI would be about ' + money(emi) + ' a month, with ' + money(total - v.amount) + ' paid in interest over ' + v.years + ' years.'
      };
    },

    fd: function (v) {
      // Quarterly compounding, the norm for Indian bank FDs
      var total = v.amount * Math.pow(1 + v.rate / 400, 4 * v.years);
      return {
        big: total,
        rows: [v.amount, total - v.amount, total],
        chart: [['Amount invested', v.amount], ['Interest earned', total - v.amount]],
        summary: 'A fixed deposit of ' + money(v.amount) + ' for ' + v.years + ' years at ' + v.rate + '% could mature at about ' + money(total) + '.'
      };
    },

    rd: function (v) {
      // Each monthly instalment compounds quarterly for the months it stays invested
      var n = v.years * 12, total = 0;
      for (var k = 1; k <= n; k++) total += v.monthly * Math.pow(1 + v.rate / 400, (n - k + 1) / 3);
      var invested = v.monthly * n;
      return {
        big: total,
        rows: [invested, total - invested, total],
        chart: [['Amount invested', invested], ['Interest earned', total - invested]],
        summary: 'Depositing ' + money(v.monthly) + ' a month for ' + v.years + ' years could mature at about ' + money(total) + '.'
      };
    },

    ppf: function (v) {
      // Deposit at the start of each year; interest compounds yearly
      var r = v.rate / 100, bal = 0, table = [];
      for (var y = 1; y <= v.years; y++) {
        var interest = (bal + v.yearly) * r;
        bal = bal + v.yearly + interest;
        table.push([y, v.yearly, interest, bal]);
      }
      var invested = v.yearly * v.years;
      return {
        big: bal,
        rows: [invested, bal - invested, bal],
        chart: [['Amount invested', invested], ['Interest earned', bal - invested]],
        table: table,
        summary: 'Investing ' + money(v.yearly) + ' a year in PPF for ' + v.years + ' years could grow to about ' + money(bal) + '.'
      };
    },

    compound: function (v) {
      var f = v.freq || 1;
      var total = v.amount * Math.pow(1 + v.rate / 100 / f, f * v.years);
      return {
        big: total,
        rows: [v.amount, total - v.amount, total],
        chart: [['Principal', v.amount], ['Interest earned', total - v.amount]],
        summary: money(v.amount) + ' at ' + v.rate + '% for ' + v.years + ' years grows to about ' + money(total) + '.'
      };
    },

    // Mutual fund returns: SIP (mode 1) or lumpsum (mode 2)
    mfreturns: function (v) {
      var sip = v.mode === 1;
      var invested = sip ? v.amount * v.years * 12 : v.amount;
      var total = sip ? sipFV(v.amount, v.rate, v.years * 12) : v.amount * Math.pow(1 + v.rate / 100, v.years);
      return {
        big: total,
        rows: [invested, total - invested, total],
        chart: [['Amount invested', invested], ['Estimated returns', total - invested]],
        summary: (sip ? 'A SIP of ' + money(v.amount) + ' a month' : 'A lumpsum of ' + money(v.amount)) + ' for ' + v.years + ' years could grow to about ' + money(total) + '.'
      };
    },

    // XIRR of a monthly SIP: instalments at the start of each month, valued at the end of the period
    xirr: function (v) {
      var n = Math.round(v.years * 12);
      var invested = v.monthly * n;
      function fv(r) {
        var s = 0;
        for (var k = 1; k <= n; k++) s += v.monthly * Math.pow(1 + r, (n - k + 1) / 12);
        return s;
      }
      var lo = -0.99, hi = 10;
      if (fv(hi) < v.value) lo = hi;
      for (var it = 0; it < 200 && hi - lo > 1e-9; it++) {
        var mid = (lo + hi) / 2;
        if (fv(mid) > v.value) hi = mid; else lo = mid;
      }
      var r = (lo + hi) / 2 * 100;
      return {
        big: r,
        rows: [invested, v.value, v.value - invested, (v.value - invested) / invested * 100, r],
        chart: [['Amount invested', invested], ['Gain', Math.max(0, v.value - invested)]],
        summary: 'A SIP of ' + money(v.monthly) + ' a month for ' + v.years + ' years, now worth ' + money(v.value) + ', has an XIRR of about ' + format('pct', r) + '.'
      };
    },

    // Sukanya Samriddhi Yojana: deposits for 15 years, matures 21 years after opening; yearly compounding
    ssy: function (v) {
      var r = v.rate / 100, bal = 0, table = [];
      for (var y = 1; y <= 21; y++) {
        var dep = y <= 15 ? v.yearly : 0;
        var interest = (bal + dep) * r;
        bal = bal + dep + interest;
        table.push([y, dep, interest, bal]);
      }
      var invested = v.yearly * 15;
      return {
        big: bal,
        rows: [invested, bal - invested, bal, v.age + 21],
        chart: [['Amount invested', invested], ['Interest earned', bal - invested]],
        table: table,
        summary: 'Depositing ' + money(v.yearly) + ' a year for 15 years could give about ' + money(bal) + ' when your daughter is ' + (v.age + 21) + '.'
      };
    },

    // EPF: employee share into EPF; employer 12% minus the EPS pension share (8.33% of wages up to ₹15,000).
    // Interest accrues monthly on the running balance and is credited at the end of each year.
    epf: function (v) {
      var years = Math.max(1, 58 - v.age), r = v.rate / 100 / 12;
      var salary = v.salary, bal = 0, emp = 0, er = 0, interestTotal = 0, table = [];
      for (var y = 1; y <= years; y++) {
        var yInterest = 0;
        for (var m = 0; m < 12; m++) {
          var e = salary * v.contribution / 100;
          var eps = Math.min(salary, 15000) * 0.0833;
          var c = Math.max(0, salary * 0.12 - eps);
          bal += e + c; emp += e; er += c;
          yInterest += bal * r;
        }
        bal += yInterest; interestTotal += yInterest;
        table.push([v.age + y, (emp + er), interestTotal, bal]);
        salary *= 1 + v.increase / 100;
      }
      return {
        big: bal,
        rows: [emp, er, interestTotal, bal],
        chart: [['Contributions', emp + er], ['Interest earned', interestTotal]],
        table: table,
        summary: 'Your EPF balance could be about ' + money(bal) + ' at age 58.'
      };
    },

    // Income tax, FY 2025-26 rules (Budget 2025). Salaried; standard deduction in both regimes; 4% cess.
    incometax: function (v) {
      var newTaxable = Math.max(0, v.income - 75000);
      var tNew = slabTax(newTaxable, [[400000, 0], [800000, .05], [1200000, .10], [1600000, .15], [2000000, .20], [2400000, .25], [Infinity, .30]]);
      if (newTaxable <= 1200000) tNew = 0;                                   // rebate u/s 87A
      else tNew = Math.min(tNew, newTaxable - 1200000);                     // marginal relief just above ₹12 lakh
      tNew = (tNew + surcharge(tNew, newTaxable)) * 1.04;

      var exempt = v.agegroup === 3 ? 500000 : v.agegroup === 2 ? 300000 : 250000;
      var oldTaxable = Math.max(0, v.income - 50000 - v.deductions);
      var tOld = slabTax(oldTaxable, [[exempt, 0], [500000, .05], [1000000, .20], [Infinity, .30]]);
      if (oldTaxable <= 500000) tOld = 0;                                    // rebate u/s 87A
      tOld = (tOld + surcharge(tOld, oldTaxable)) * 1.04;

      var better = Math.abs(tNew - tOld) < 1 ? 0 : tNew < tOld ? 1 : 2;
      return {
        big: Math.min(tNew, tOld),
        rows: [newTaxable, tNew, oldTaxable, tOld, better, Math.abs(tNew - tOld)],
        chart: [['New regime tax', tNew], ['Old regime tax', tOld]],
        summary: better === 0 ? 'Your tax is about the same under both regimes: ' + money(tNew) + '.'
          : 'The ' + (better === 1 ? 'new' : 'old') + ' regime saves you about ' + money(Math.abs(tNew - tOld)) + ' (tax ' + money(Math.min(tNew, tOld)) + ').'
      };
    },

    // GST: mode 1 = add GST to a price, mode 2 = price already includes GST
    gst: function (v) {
      var rate = v.gstrate / 100;
      var net = v.mode === 1 ? v.amount : v.amount / (1 + rate);
      var tax = net * rate;
      return {
        big: net + tax,
        rows: [net, tax / 2, tax / 2, tax, net + tax],
        chart: [['Net amount', net], ['GST', tax]],
        summary: 'Net ' + money(net) + ' plus GST of ' + money(tax) + ' at ' + v.gstrate + '% makes ' + money(net + tax) + '.'
      };
    },

    inflation: function (v) {
      var future = v.amount * Math.pow(1 + v.rate / 100, v.years);
      var worth = v.amount / Math.pow(1 + v.rate / 100, v.years);
      return {
        big: future,
        rows: [v.amount, future, future - v.amount, worth],
        chart: [['Cost today', v.amount], ['Increase', future - v.amount]],
        summary: 'Something costing ' + money(v.amount) + ' today may cost about ' + money(future) + ' in ' + v.years + ' years.'
      };
    },

    retirement: function (v) {
      var retireAge = Math.max(v.retireAge, v.age + 1);
      var lifeAge = Math.max(v.lifeAge, retireAge + 1);
      var yearsTo = retireAge - v.age;
      var yearsIn = lifeAge - retireAge;
      var inf = v.inflation / 100;
      var monthlyAtRetirement = v.expenses * Math.pow(1 + inf, yearsTo);
      var annual = monthlyAtRetirement * 12;
      var real = (1 + v.returnAfter / 100) / (1 + inf) - 1;
      // Present value, at retirement, of inflation-rising withdrawals made at the start of each year
      var corpus = Math.abs(real) < 1e-9 ? annual * yearsIn : annual * (1 - Math.pow(1 + real, -yearsIn)) / real * (1 + real);
      var savingsFV = v.savings * Math.pow(1 + v.returnBefore / 100, yearsTo);
      var gap = Math.max(0, corpus - savingsFV);
      var sip = sipNeeded(gap, v.returnBefore, yearsTo * 12);
      return {
        big: corpus,
        rows: [monthlyAtRetirement, savingsFV, gap, sip],
        chart: [['Covered by current savings', Math.min(savingsFV, corpus)], ['Shortfall', gap]],
        summary: 'You may need about ' + money(corpus) + ' at retirement. To close the gap, invest about ' + money(sip) + ' a month.'
      };
    },

    hlv: function (v) {
      var years = Math.max(1, v.retireAge - v.age);
      var net = v.income * (1 - v.expensePct / 100);
      var g = v.growth / 100;
      var d = v.discount / 100;
      // Present value of your future income contribution to the family, growing each year
      var hlv = Math.abs(d - g) < 1e-9 ? net * years / (1 + d) : net * (1 - Math.pow((1 + g) / (1 + d), years)) / (d - g);
      var need = hlv + v.loans;
      var have = v.cover + v.savings;
      var gap = Math.max(0, need - have);
      return {
        big: gap,
        rows: [hlv, v.loans, need, have, gap],
        chart: [['Existing cover and savings', Math.min(have, need)], ['Additional cover needed', gap]],
        summary: 'Your family may need about ' + money(need) + ' in total. After existing cover and savings, consider about ' + money(gap) + ' of additional life cover.'
      };
    },

    education: function (v) {
      var cost = v.cost * Math.pow(1 + v.inflation / 100, v.years);
      var savingsFV = v.savings * Math.pow(1 + v.rate / 100, v.years);
      var gap = Math.max(0, cost - savingsFV);
      var sip = sipNeeded(gap, v.rate, v.years * 12);
      return {
        big: cost,
        rows: [savingsFV, gap, sip],
        chart: [['Covered by current savings', Math.min(savingsFV, cost)], ['Shortfall', gap]],
        summary: 'The course may cost about ' + money(cost) + ' in ' + v.years + ' years. Invest about ' + money(sip) + ' a month to get there.'
      };
    }
  };

  /* ---------- Animated numbers ---------- */
  function tween(el, to) {
    var fmt = el.getAttribute('data-fmt') || 'inr';
    var from = Number(el.getAttribute('data-value') || 0);
    el.setAttribute('data-value', to);
    if (reducedMotion || from === to || fmt === 'months' || fmt === 'regime' || fmt === 'years') { el.textContent = format(fmt, to); return; }
    var start = null;
    var duration = 450;
    if (el._raf) window.cancelAnimationFrame(el._raf);
    function step(ts) {
      if (start === null) start = ts;
      var p = Math.min((ts - start) / duration, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = format(fmt, from + (to - from) * eased);
      if (p < 1) el._raf = window.requestAnimationFrame(step);
    }
    el._raf = window.requestAnimationFrame(step);
  }

  /* ---------- One calculator panel ---------- */
  function setupPanel(panel) {
    var calc = CALCS[panel.getAttribute('data-calc')];
    if (!calc) return;
    var ranges = $$('.range', panel);
    var selects = $$('select[data-key]', panel);
    var presets = $$('[data-preset]', panel);
    var big = $('.calc__big', panel);
    var rowEls = $$('.calc__rows dd', panel);
    var summary = $('.calc__summary', panel);
    var canvas = $('canvas', panel);
    var tbody = $('.calc-schedule tbody', panel);
    var chart = null;
    var summaryTimer;

    // Prefer the exact typed number (clamped to the slider's range); the slider itself snaps to its step
    function values() {
      var v = {};
      ranges.forEach(function (range) {
        var number = numberFor(range);
        var n = number && number.value !== '' && !isNaN(Number(number.value)) ? Number(number.value) : Number(range.value);
        v[range.getAttribute('data-key')] = Math.min(Math.max(n, Number(range.min)), Number(range.max));
      });
      selects.forEach(function (el) { v[el.getAttribute('data-key')] = Number(el.value); });
      return v;
    }

    function paintTrack(range) {
      range.style.setProperty('--pct', ((range.value - range.min) / (range.max - range.min) * 100) + '%');
    }

    function numberFor(range) {
      return panel.querySelector('input[type="number"][data-key="' + range.getAttribute('data-key') + '"]');
    }

    function setValue(key, val) {
      var range = panel.querySelector('.range[data-key="' + key + '"]');
      if (range) {
        range.value = val;
        var number = numberFor(range);
        if (number) number.value = range.value;
        paintTrack(range);
      }
      var select = panel.querySelector('select[data-key="' + key + '"]');
      if (select) select.value = val;
    }

    function renderTable(rows) {
      if (!tbody || !rows) return;
      var fmts = $$('.calc-schedule thead th', panel).map(function (th) { return th.getAttribute('data-fmt'); });
      tbody.innerHTML = rows.map(function (row) {
        return '<tr>' + row.map(function (cell, i) {
          return i === 0 ? '<th scope="row">' + cell + '</th>' : '<td>' + format(fmts[i] || 'inr', cell) + '</td>';
        }).join('') + '</tr>';
      }).join('');
    }

    function update() {
      var result = calc(values());
      tween(big, result.big);
      result.rows.forEach(function (value, i) { if (rowEls[i]) tween(rowEls[i], value); });
      if (chart) {
        chart.data.labels = result.chart.map(function (c) { return c[0]; });
        chart.data.datasets[0].data = result.chart.map(function (c) { return Math.max(0, Math.round(c[1])); });
        chart.update();
      }
      if (canvas) canvas.setAttribute('aria-label', result.chart.map(function (c) { return c[0] + ': ' + money(c[1]); }).join(', '));
      renderTable(result.table);
      // Announce a short summary once the user stops adjusting
      window.clearTimeout(summaryTimer);
      summaryTimer = window.setTimeout(function () { if (summary) summary.textContent = result.summary; }, 700);
    }

    ranges.forEach(function (range) {
      var number = numberFor(range);
      paintTrack(range);
      range.addEventListener('input', function () {
        if (number) number.value = range.value;
        paintTrack(range);
        update();
      });
      if (!number) return;
      number.addEventListener('input', function () {
        var n = Number(number.value);
        if (number.value === '' || isNaN(n)) return;
        range.value = Math.min(Math.max(n, Number(range.min)), Number(range.max));
        paintTrack(range);
        update();
      });
      number.addEventListener('change', function () {
        var n = Math.min(Math.max(Number(number.value) || Number(range.min), Number(range.min)), Number(range.max));
        number.value = n;
        range.value = n;
        paintTrack(range);
        update();
      });
    });
    selects.forEach(function (s) { s.addEventListener('change', update); });

    presets.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var data = JSON.parse(btn.getAttribute('data-preset'));
        Object.keys(data).forEach(function (key) { setValue(key, data[key]); });
        presets.forEach(function (b) { b.setAttribute('aria-pressed', String(b === btn)); });
        update();
      });
    });

    if (canvas && typeof window.Chart !== 'undefined') {
      chart = new window.Chart(canvas, {
        type: 'doughnut',
        data: { labels: [], datasets: [{ data: [], backgroundColor: COLORS, borderColor: '#0A2540', borderWidth: 3, hoverOffset: 6 }] },
        options: {
          cutout: '68%',
          responsive: true,
          maintainAspectRatio: true,
          animation: reducedMotion ? false : { duration: 500 },
          plugins: {
            legend: { display: false },
            tooltip: { callbacks: { label: function (ctx) { return ' ' + ctx.label + ': ' + money(ctx.raw); } } }
          }
        }
      });
    } else if (canvas) {
      canvas.closest('.calc__chart').hidden = true;
    }

    update();
  }

  /* ---------- Hub: search filter ---------- */
  function setupHub() {
    var input = $('[data-calc-search]');
    if (!input) return;
    var cards = $$('.calc-card');
    var groups = $$('.calc-group');
    var count = $('[data-calc-count]');
    var empty = $('[data-calc-empty]');

    input.addEventListener('input', function () {
      var q = input.value.trim().toLowerCase();
      var shown = 0;
      cards.forEach(function (card) {
        var match = !q || card.getAttribute('data-keywords').indexOf(q) > -1;
        card.hidden = !match;
        if (match) shown++;
      });
      groups.forEach(function (g) { g.hidden = !$$('.calc-card', g).some(function (c) { return !c.hidden; }); });
      if (empty) empty.hidden = shown > 0;
      if (count) count.textContent = q ? shown + (shown === 1 ? ' calculator' : ' calculators') + ' found' : '';
    });
  }

  /* ---------- Old tabbed links (calculators.html#sip etc.) now have their own pages ---------- */
  function redirectLegacyHash() {
    if (!$('[data-calc-search]')) return;
    var map = { sip: 'sip-calculator.html', retirement: 'retirement-calculator.html', hlv: 'life-cover-calculator.html', education: 'child-education-calculator.html' };
    var target = map[window.location.hash.slice(1)];
    if (target) window.location.replace(target);
  }

  function init() {
    redirectLegacyHash();
    $$('[data-calc]').forEach(setupPanel);
    setupHub();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
