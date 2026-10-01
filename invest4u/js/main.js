/* ==========================================================================
   Invest 4U Solutions: shared site script
   Every init function exits early when its elements aren't on the page,
   so this one file is safe to load on every page.
   ========================================================================== */
(function () {
  'use strict';

  var root = document.documentElement;
  root.classList.remove('no-js');
  root.classList.add('js');

  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  var desktopMQ = window.matchMedia('(min-width: 1024px)');

  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }

  var FOCUSABLE = 'a[href], button:not([disabled]), input:not([disabled]):not([type="hidden"]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])';

  /* ---------- Header: solid + shrink on scroll ---------- */
  function initHeader() {
    var header = $('.site-header');
    if (!header) return;
    var ticking = false;

    function update() {
      header.classList.toggle('is-scrolled', window.scrollY > 40);
      ticking = false;
    }
    window.addEventListener('scroll', function () {
      if (!ticking) {
        window.requestAnimationFrame(update);
        ticking = true;
      }
    }, { passive: true });
    update();
  }

  /* ---------- Mobile navigation: slide-in panel with focus trap ---------- */
  function initMobileNav() {
    var header = $('.site-header');
    var toggle = $('.hamburger');
    var nav = $('#site-nav');
    var overlay = $('.nav-overlay');
    if (!header || !toggle || !nav) return;

    function isOpen() { return toggle.getAttribute('aria-expanded') === 'true'; }

    function open() {
      toggle.setAttribute('aria-expanded', 'true');
      toggle.setAttribute('aria-label', 'Close menu');
      nav.classList.add('is-open');
      header.classList.add('menu-open');
      if (overlay) overlay.classList.add('is-visible');
      document.body.classList.add('no-scroll');
      var first = $(FOCUSABLE, nav);
      if (first) window.setTimeout(function () { first.focus(); }, 50);
      document.addEventListener('keydown', onKeydown);
    }

    function close(returnFocus) {
      toggle.setAttribute('aria-expanded', 'false');
      toggle.setAttribute('aria-label', 'Open menu');
      nav.classList.remove('is-open');
      header.classList.remove('menu-open');
      if (overlay) overlay.classList.remove('is-visible');
      document.body.classList.remove('no-scroll');
      document.removeEventListener('keydown', onKeydown);
      if (returnFocus) toggle.focus();
    }

    // Esc closes; Tab cycles between the toggle and the links inside the panel
    function onKeydown(e) {
      if (e.key === 'Escape') { close(true); return; }
      if (e.key !== 'Tab') return;
      var items = [toggle].concat($$(FOCUSABLE, nav).filter(function (el) { return el.offsetParent !== null; }));
      var first = items[0];
      var last = items[items.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }

    toggle.addEventListener('click', function () { isOpen() ? close(false) : open(); });
    if (overlay) overlay.addEventListener('click', function () { close(true); });

    // Close after following a link (e.g. an in-page anchor)
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a') && isOpen()) close(false);
    });

    desktopMQ.addEventListener('change', function (e) { if (e.matches && isOpen()) close(false); });
  }

  /* ---------- Services dropdown / mobile accordion ---------- */
  function initSubmenus() {
    $$('.submenu-toggle').forEach(function (btn) {
      var menu = document.getElementById(btn.getAttribute('aria-controls'));
      var item = btn.closest('.nav__item');
      if (!menu || !item) return;

      function set(open) {
        btn.setAttribute('aria-expanded', String(open));
        menu.classList.toggle('is-open', open);
      }

      btn.addEventListener('click', function () {
        set(btn.getAttribute('aria-expanded') !== 'true');
      });

      item.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && btn.getAttribute('aria-expanded') === 'true') {
          e.stopPropagation();
          set(false);
          btn.focus();
        }
      });

      // Desktop: close when focus or a click leaves the item
      item.addEventListener('focusout', function (e) {
        if (desktopMQ.matches && !item.contains(e.relatedTarget)) set(false);
      });
      document.addEventListener('click', function (e) {
        if (desktopMQ.matches && !item.contains(e.target)) set(false);
      });
    });
  }

  /* ---------- In-page anchors: move focus to the target after scrolling ---------- */
  function initSmoothScroll() {
    document.addEventListener('click', function (e) {
      var link = e.target.closest('a[href^="#"]');
      if (!link) return;
      var id = link.getAttribute('href').slice(1);
      if (!id) return;
      var target = document.getElementById(id);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: reducedMotion.matches ? 'auto' : 'smooth', block: 'start' });
      if (!target.hasAttribute('tabindex')) target.setAttribute('tabindex', '-1');
      target.focus({ preventScroll: true });
      history.pushState(null, '', '#' + id);
    });
  }

  /* ---------- Back to top ---------- */
  function initBackToTop() {
    var btn = $('.back-to-top');
    if (!btn) return;
    var ticking = false;
    window.addEventListener('scroll', function () {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(function () {
        btn.classList.toggle('is-visible', window.scrollY > 600);
        ticking = false;
      });
    }, { passive: true });
    btn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: reducedMotion.matches ? 'auto' : 'smooth' });
      var skip = $('.skip-link');
      if (skip) skip.focus({ preventScroll: true });
    });
  }

  /* ---------- Home preloader ----------
     Progress follows real loading (fonts, page, first hero image), shown for at least 1.2s and never
     more than 4s. Full version once per browser session; repeat visits and reduced motion: quick fade. */
  function initLoader() {
    var loader = $('.page-loader');
    if (!loader) return;
    var seen = false;
    try { seen = window.sessionStorage.getItem('i4u-loaded') === '1'; } catch (err) { seen = false; }
    var pct = $('.page-loader__pct', loader);
    var start = performance.now();
    var MIN = 1200, MAX = 4000;
    var loaded = false, finished = false, shown = 0;

    root.classList.add('loader-lock');

    function finish() {
      if (finished) return;
      finished = true;
      loader.classList.add('is-done');
      root.classList.remove('loader-lock');
      try { window.sessionStorage.setItem('i4u-loaded', '1'); } catch (err) { /* private mode */ }
      window.setTimeout(function () { loader.remove(); }, 500);
    }

    if (seen || reducedMotion.matches) {
      loader.classList.add('is-quick');
      window.setTimeout(finish, 150);
      return;
    }

    if (document.readyState === 'complete') loaded = true;
    else window.addEventListener('load', function () { loaded = true; });

    function tick() {
      var elapsed = performance.now() - start;
      // Creep towards 90% while loading; run to 100% once loaded (after the minimum time) or at the 4s cap
      var goal = (loaded && elapsed >= MIN) || elapsed >= MAX ? 1 : Math.min(0.9, elapsed / MIN * 0.9);
      shown += (goal - shown) * 0.12;
      if (goal - shown < 0.004) shown = goal;
      loader.style.setProperty('--progress', shown.toFixed(3));
      if (pct) pct.textContent = Math.round(shown * 100) + '%';
      if (shown >= 1) { window.setTimeout(finish, 200); return; }
      window.requestAnimationFrame(tick);
    }
    window.requestAnimationFrame(tick);
  }


  /* ---------- AOS scroll animations (off under reduced motion) ---------- */
  function initAOS() {
    if (!$('[data-aos]')) return;
    if (typeof window.AOS === 'undefined') { root.classList.add('no-aos'); return; }
    window.AOS.init({
      once: true,
      duration: 700,
      easing: 'ease-out-cubic',
      offset: 60,
      disable: function () { return reducedMotion.matches; }
    });
  }

  /* ---------- Generic "in view" trigger for CSS-driven animations ([data-inview]) ---------- */
  function initInView() {
    var els = $$('[data-inview]');
    if (!els.length) return;
    if (!('IntersectionObserver' in window)) {
      els.forEach(function (el) { el.classList.add('is-inview'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-inview');
        io.unobserve(entry.target);
      });
    }, { threshold: 0.3 });
    els.forEach(function (el) { io.observe(el); });
  }

  /* ---------- Count-up numbers ----------
     Markup holds the final value (for no-JS and SEO); screen readers get the final value too. */
  function initCounters() {
    var groups = $$('[data-counters]');
    if (!groups.length || reducedMotion.matches || !('IntersectionObserver' in window)) return;

    function format(el, n) { return el.hasAttribute('data-plain') ? String(n) : n.toLocaleString('en-IN'); }

    function run(el) {
      var to = Number(el.getAttribute('data-count'));
      var from = Number(el.getAttribute('data-count-from') || 0);
      var duration = 1800;
      var start = null;
      function step(ts) {
        if (start === null) start = ts;
        var p = Math.min((ts - start) / duration, 1);
        var eased = 1 - Math.pow(1 - p, 3);
        el.textContent = format(el, Math.round(from + (to - from) * eased));
        if (p < 1) window.requestAnimationFrame(step);
      }
      window.requestAnimationFrame(step);
    }

    groups.forEach(function (group) {
      var counters = $$('[data-count]', group);
      counters.forEach(function (el) {
        var value = el.closest('.stat__value') || el;
        var sr = document.createElement('span');
        sr.className = 'sr-only';
        sr.textContent = value.textContent.trim();
        value.parentNode.insertBefore(sr, value);
        value.setAttribute('aria-hidden', 'true');
        el.textContent = format(el, Number(el.getAttribute('data-count-from') || 0));
      });
      var io = new IntersectionObserver(function (entries) {
        if (!entries[0].isIntersecting) return;
        counters.forEach(run);
        io.disconnect();
      }, { threshold: 0.4 });
      io.observe(group);
    });
  }

  /* ---------- Hero video slider ----------
     Videos load only on 768px+ screens, without reduced motion or data saver; phones keep the posters.
     Only the active slide's video plays. Inactive slides are inert so their links can't be tabbed to. */
  function initHeroSlider() {
    var el = $('.hero-swiper');
    if (!el || typeof window.Swiper === 'undefined') return;
    var hero = el.closest('.hero');
    var toggle = $('.hero__toggle', hero);
    var slides = $$('.swiper-slide', el);
    var saveData = navigator.connection && navigator.connection.saveData;
    var useVideo = window.matchMedia('(min-width: 768px)').matches && !reducedMotion.matches && !saveData;
    var paused = false;

    function sync(swiper) {
      slides.forEach(function (slide, i) {
        var active = i === swiper.activeIndex;
        slide.inert = !active;
        var video = $('video', slide);
        if (!video) return;
        if (active && useVideo && !paused) {
          if (!video.src) {
            video.addEventListener('playing', function () { video.classList.add('is-playing'); }, { once: true });
            video.src = video.getAttribute('data-src');
          }
          var p = video.play();
          if (p && p.catch) p.catch(function () { /* autoplay blocked: poster stays visible */ });
        } else if (video.src) {
          video.pause();
        }
      });
    }

    var swiper = new window.Swiper(el, {
      effect: 'fade',
      fadeEffect: { crossFade: true },
      speed: 900,
      rewind: true,
      autoplay: reducedMotion.matches ? false : { delay: 7000, disableOnInteraction: false, pauseOnMouseEnter: true },
      pagination: { el: $('.hero__pagination', hero), clickable: true },
      navigation: { nextEl: $('.hero__next', hero), prevEl: $('.hero__prev', hero) },
      keyboard: { enabled: true, onlyInViewport: true },
      a11y: { enabled: true, paginationBulletMessage: 'Go to slide {{index}}' },
      on: {
        init: function (s) { sync(s); },
        slideChange: function (s) { sync(s); }
      }
    });

    // Pause / play control (WCAG 2.2.2). Not needed when nothing auto-advances.
    if (!toggle) return;
    if (reducedMotion.matches) { toggle.hidden = true; return; }
    toggle.addEventListener('click', function () {
      paused = !paused;
      toggle.setAttribute('aria-pressed', String(paused));
      toggle.setAttribute('aria-label', paused ? 'Play slideshow' : 'Pause slideshow');
      if (paused) swiper.autoplay.stop(); else swiper.autoplay.start();
      sync(swiper);
    });
  }

  /* ---------- Testimonials: scroll-driven 3D card cloud ----------
     Sets --p (0 → 1) on the section while its sticky panel is pinned; CSS turns --p into the
     camera flight through the cards. Phones (<768px) and reduced motion use the static layouts. */
  function initTestimonialCloud() {
    var section = $('.tc');
    if (!section) return;
    var wideMQ = window.matchMedia('(min-width: 768px)');
    var ticking = false;

    function update() {
      ticking = false;
      if (!wideMQ.matches || reducedMotion.matches) { section.style.removeProperty('--p'); return; }
      var r = section.getBoundingClientRect();
      var total = section.offsetHeight - window.innerHeight;
      var p = total > 0 ? Math.min(1, Math.max(0, -r.top / total)) : 0;
      section.style.setProperty('--p', p.toFixed(4));
    }
    function request() {
      if (!ticking) { ticking = true; window.requestAnimationFrame(update); }
    }
    window.addEventListener('scroll', request, { passive: true });
    window.addEventListener('resize', request);
    update();
  }

  /* ---------- Awards lightbox (native <dialog>) ---------- */
  function initLightbox() {
    var dlg = $('.lightbox');
    var groups = $$('[data-lightbox-group]');
    if (!dlg || !groups.length || typeof dlg.showModal !== 'function') return;
    var img = $('img', dlg);
    var name = $('.award__name', dlg);
    var meta = $('.award__meta', dlg);
    var items = [];
    var index = 0;
    var opener = null;

    function show(i) {
      index = (i + items.length) % items.length;
      var fig = items[index];
      var src = $('img', fig);
      img.src = src.currentSrc || src.src;
      img.alt = src.alt;
      name.textContent = $('.award__name', fig).textContent;
      meta.textContent = $('.award__meta', fig).textContent;
    }

    groups.forEach(function (group) {
      $$('.award', group).forEach(function (fig) {
        var i = items.push(fig) - 1;
        $('.award__btn', fig).addEventListener('click', function () {
          opener = this;
          show(i);
          dlg.showModal();
        });
      });
    });

    $('.lightbox__close', dlg).addEventListener('click', function () { dlg.close(); });
    $('.lightbox__prev', dlg).addEventListener('click', function () { show(index - 1); });
    $('.lightbox__next', dlg).addEventListener('click', function () { show(index + 1); });
    dlg.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') show(index - 1);
      if (e.key === 'ArrowRight') show(index + 1);
    });
    dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); }); // backdrop
    dlg.addEventListener('close', function () { if (opener) opener.focus(); });
  }

  /* ---------- Forms: validation, honeypot, Web3Forms submit, optional multi-step ----------
     Any form with [data-contact-form]. Add [data-multistep] and wrap groups of fields in
     <fieldset class="form-step" data-title="…"> to split it into steps with a progress bar.
     Optional data-success="…" overrides the thank-you message. */
  function initForms() {
    var forms = $$('[data-contact-form]');
    if (!forms.length) return;
    var serviceParam = new URLSearchParams(window.location.search).get('service');

    var validators = {
      name: function (v) { return v.trim().length >= 2; },
      phone: function (v) { return /^(?:\+?91|0)?[6-9]\d{9}$/.test(v.replace(/[\s()-]/g, '')); },
      email: function (v) { return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim()); }
    };

    forms.forEach(function (form) {
      var status = $('.form-status', form);
      var submit = $('[type="submit"]', form);
      var select = form.querySelector('[name="service"]');
      var fields = $$('input, select, textarea', form).filter(function (el) {
        return el.closest('.field') && (el.required || validators[el.name]);
      });
      var steps = form.hasAttribute('data-multistep') ? $$('.form-step', form) : [];
      var current = 0;

      // ?service=checkup preselects the dropdown
      if (serviceParam && select) {
        var match = $$('option', select).filter(function (o) { return o.value === serviceParam; })[0];
        if (match) select.value = serviceParam;
      }

      function check(el) {
        var ok;
        if (el.type === 'radio') ok = !el.required || !!form.querySelector('input[name="' + el.name + '"]:checked');
        else if (el.type === 'checkbox') ok = !el.required || el.checked;
        else if (!el.value.trim()) ok = !el.required;
        else ok = validators[el.name] ? validators[el.name](el.value) : true;
        el.closest('.field').classList.toggle('is-invalid', !ok);
        el.setAttribute('aria-invalid', String(!ok));
        return ok;
      }

      // Validate a set of fields; radios in one group are checked once
      function validate(list) {
        var seen = {};
        return list.filter(function (el) {
          if (el.type === 'radio') {
            if (seen[el.name]) return false;
            seen[el.name] = true;
          }
          return !check(el);
        });
      }

      function setStatus(type, message) {
        status.className = 'form-status is-' + type;
        status.textContent = message;
      }

      function clearStatus() {
        status.className = 'form-status';
        status.textContent = '';
      }

      fields.forEach(function (el) {
        var evt = el.type === 'checkbox' || el.type === 'radio' || el.tagName === 'SELECT' ? 'change' : 'blur';
        el.addEventListener(evt, function () { if (el.type === 'checkbox' || el.type === 'radio' || el.value) check(el); });
        el.addEventListener('input', function () {
          if (el.closest('.field').classList.contains('is-invalid')) check(el);
        });
      });

      /* Multi-step: show one fieldset at a time and keep the progress bar in sync */
      function showStep(i, focus) {
        current = Math.max(0, Math.min(i, steps.length - 1));
        steps.forEach(function (step, n) { step.hidden = n !== current; });
        var pct = ((current + 1) / steps.length) * 100;
        var bar = $('.progress__bar', form);
        var track = $('[role="progressbar"]', form);
        if (bar) bar.style.width = pct + '%';
        if (track) track.setAttribute('aria-valuenow', String(current + 1));
        $$('[data-step-current]', form).forEach(function (el) { el.textContent = current + 1; });
        $$('[data-step-title]', form).forEach(function (el) { el.textContent = steps[current].getAttribute('data-title') || ''; });
        $$('.progress__steps li', form).forEach(function (li, n) {
          li.classList.toggle('is-done', n < current);
          li.classList.toggle('is-active', n === current);
          if (n === current) li.setAttribute('aria-current', 'step'); else li.removeAttribute('aria-current');
        });
        if (focus) {
          var legend = $('legend', steps[current]);
          var target = legend || steps[current];
          target.setAttribute('tabindex', '-1');
          target.focus({ preventScroll: true });
          form.scrollIntoView({ behavior: reducedMotion.matches ? 'auto' : 'smooth', block: 'start' });
        }
      }

      function stepFields(i) {
        return fields.filter(function (el) { return steps[i].contains(el); });
      }

      function next() {
        var invalid = validate(stepFields(current));
        if (invalid.length) { invalid[0].focus(); return; }
        clearStatus();
        showStep(current + 1, true);
      }

      if (steps.length) {
        $$('[data-step-next]', form).forEach(function (btn) { btn.addEventListener('click', next); });
        $$('[data-step-prev]', form).forEach(function (btn) {
          btn.addEventListener('click', function () { clearStatus(); showStep(current - 1, true); });
        });
        showStep(0, false);
      }

      form.addEventListener('submit', function (e) {
        e.preventDefault();
        // Enter on an earlier step moves forward instead of submitting
        if (steps.length && current < steps.length - 1) { next(); return; }
        clearStatus();

        var invalid = validate(fields);
        if (invalid.length) {
          if (steps.length) {
            var at = steps.indexOf(invalid[0].closest('.form-step'));
            if (at > -1 && at !== current) showStep(at, false);
          }
          invalid[0].focus();
          return;
        }

        // Honeypot ticked: a bot. Pretend it worked and send nothing.
        if (form.botcheck && form.botcheck.checked) {
          form.reset();
          setStatus('success', 'Thank you! Your message has been sent.');
          return;
        }

        var key = form.getAttribute('data-access-key');
        if (!key || key.indexOf('YOUR_') === 0) {
          console.warn('Contact form: set data-access-key to your Web3Forms access key.'); // TODO
          setStatus('error', "Our online form isn't connected yet. Please call +91 97475 46614 or message us on WhatsApp.");
          return;
        }

        var data = new FormData(form);
        data.append('access_key', key);
        var label = submit.innerHTML;
        submit.setAttribute('aria-busy', 'true');
        submit.textContent = 'Sending…';

        fetch(form.action, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
          .then(function (res) {
            return res.json().catch(function () { return {}; }).then(function (json) {
              if (!res.ok || json.success === false) throw new Error(json.message || res.status);
            });
          })
          .then(function () {
            form.reset();
            fields.forEach(function (el) {
              el.closest('.field').classList.remove('is-invalid');
              el.removeAttribute('aria-invalid');
            });
            if (steps.length) showStep(0, false);
            setStatus('success', form.getAttribute('data-success') ||
              'Thank you! Your message has been sent. An advisor will contact you within one working day.');
            status.setAttribute('tabindex', '-1');
            status.focus();
          })
          .catch(function () {
            setStatus('error', 'Sorry, your message could not be sent. Please try again, or call us on +91 97475 46614.');
          })
          .then(function () {
            submit.removeAttribute('aria-busy');
            submit.innerHTML = label;
          });
      });
    });
  }

  /* ---------- FAQ accordion ----------
     [data-accordion] (add ="single" to keep one panel open). Each .accordion__trigger has
     aria-controls pointing at its .accordion__panel. Without JS every answer stays visible. */
  function initAccordions() {
    $$('[data-accordion]').forEach(function (acc) {
      var single = acc.getAttribute('data-accordion') === 'single';
      var triggers = $$('.accordion__trigger', acc);

      function set(btn, open, animate) {
        var panel = document.getElementById(btn.getAttribute('aria-controls'));
        var item = btn.closest('.accordion__item');
        if (!panel) return;
        btn.setAttribute('aria-expanded', String(open));
        if (item) item.classList.toggle('is-open', open);

        if (!animate || reducedMotion.matches) {
          panel.hidden = !open;
          panel.style.height = '';
          return;
        }
        var done = function () {
          panel.removeEventListener('transitionend', done);
          window.clearTimeout(timer);
          if (!open) panel.hidden = true;
          panel.style.height = '';
        };
        var timer = window.setTimeout(done, 500); // fallback if transitionend never fires
        panel.addEventListener('transitionend', done);
        if (open) {
          panel.hidden = false;
          panel.style.height = '0px';
          void panel.offsetHeight; // reflow so the transition starts from 0
          panel.style.height = panel.scrollHeight + 'px';
        } else {
          panel.style.height = panel.scrollHeight + 'px';
          void panel.offsetHeight;
          panel.style.height = '0px';
        }
      }

      triggers.forEach(function (btn) {
        set(btn, btn.getAttribute('aria-expanded') === 'true', false);
        btn.addEventListener('click', function () {
          var open = btn.getAttribute('aria-expanded') !== 'true';
          if (open && single) {
            triggers.forEach(function (other) {
              if (other !== btn && other.getAttribute('aria-expanded') === 'true') set(other, false, true);
            });
          }
          set(btn, open, true);
        });
      });
    });
  }

  /* ---------- Copy-to-clipboard buttons ----------
     <button class="copy-btn" data-copy="text to copy" aria-label="Copy account number">…
     <span class="copy-btn__label">Copy</span></button>   (or data-copy-target="#element-id") */
  function initCopyButtons() {
    var buttons = $$('[data-copy], [data-copy-target]');
    if (!buttons.length) return;
    var live = document.createElement('div');
    live.className = 'sr-only';
    live.setAttribute('aria-live', 'polite');
    document.body.appendChild(live);

    function fallbackCopy(text) {
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.setAttribute('readonly', '');
      ta.style.position = 'fixed';
      ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      var ok = false;
      try { ok = document.execCommand('copy'); } catch (err) { ok = false; }
      ta.remove();
      return ok ? Promise.resolve() : Promise.reject(new Error('copy failed'));
    }

    buttons.forEach(function (btn) {
      var label = $('.copy-btn__label', btn);
      var original = label ? label.textContent : '';
      var timer;
      btn.addEventListener('click', function () {
        var target = btn.getAttribute('data-copy-target');
        var text = btn.getAttribute('data-copy') || (target && document.querySelector(target) ? document.querySelector(target).textContent.trim() : '');
        if (!text) return;
        var attempt = navigator.clipboard && window.isSecureContext
          ? navigator.clipboard.writeText(text).catch(function () { return fallbackCopy(text); })
          : fallbackCopy(text);
        attempt.then(function () {
          btn.classList.add('is-copied');
          if (label) label.textContent = 'Copied';
          live.textContent = 'Copied ' + text + ' to the clipboard';
        }, function () {
          if (label) label.textContent = 'Press Ctrl+C';
          live.textContent = 'Could not copy automatically. Please select and copy the text.';
        }).then(function () {
          window.clearTimeout(timer);
          timer = window.setTimeout(function () {
            btn.classList.remove('is-copied');
            if (label) label.textContent = original;
          }, 2000);
        });
      });
    });
  }

  /* ---------- Footer year ---------- */
  function setYear() {
    $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
  }

  /* ---------- Boot ---------- */
  function init() {
    initLoader();
    initHeader();
    initMobileNav();
    initSubmenus();
    initSmoothScroll();
    initBackToTop();
    initHeroSlider();
    initTestimonialCloud();
    initCounters();
    initInView();
    initLightbox();
    initForms();
    initAccordions();
    initCopyButtons();
    initAOS();
    setYear();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
