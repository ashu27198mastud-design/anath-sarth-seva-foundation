// ============================================================
// NAV.JS — Header scroll, mobile panel, dropdowns
// ============================================================

(function () {
  'use strict';

  // Load the responsive override from the same asset root as this script.
  // This works for both root pages and nested /programs pages.
  (function loadResponsiveStyles () {
    if (document.querySelector('link[data-responsive-layout]')) return;

    const currentScript = document.currentScript || Array.from(document.scripts).find(function (script) {
      return /assets\/js\/nav\.js(?:\?.*)?$/.test(script.src || '');
    });

    const href = currentScript && currentScript.src
      ? new URL('../css/responsive.css', currentScript.src).href
      : 'assets/css/responsive.css';

    const stylesheet = document.createElement('link');
    stylesheet.rel = 'stylesheet';
    stylesheet.href = href;
    stylesheet.dataset.responsiveLayout = 'true';
    document.head.appendChild(stylesheet);
  })();

  const header     = document.getElementById('header');
  const menuBtn    = document.getElementById('menu-btn');
  const mobileNav  = document.getElementById('mobile-nav');
  const closeBtn   = document.getElementById('mobile-nav-close');
  const overlay    = document.querySelector('.mobile-nav__overlay');
  const accordionToggles = document.querySelectorAll('.mobile-nav__accordion-toggle');

  // ── Scroll behaviour ──────────────────────────────────────
  function updateHeader () {
    if (!header) return;
    const isHero = header.classList.contains('header--transparent');
    if (!isHero) return;
    if (window.scrollY > 60) {
      header.classList.add('header--scrolled');
    } else {
      header.classList.remove('header--scrolled');
    }
  }

  window.addEventListener('scroll', updateHeader, { passive: true });
  updateHeader();

  // ── Mobile panel ─────────────────────────────────────────
  function openMenu () {
    if (!mobileNav) return;
    mobileNav.classList.add('is-open');
    document.body.style.overflow = 'hidden';
    if (menuBtn) menuBtn.setAttribute('aria-expanded', 'true');
    if (closeBtn) closeBtn.focus();
  }

  function closeMenu () {
    if (!mobileNav) return;
    mobileNav.classList.remove('is-open');
    document.body.style.overflow = '';
    if (menuBtn) menuBtn.setAttribute('aria-expanded', 'false');
    if (menuBtn) menuBtn.focus();
  }

  if (menuBtn)   menuBtn.addEventListener('click', openMenu);
  if (closeBtn)  closeBtn.addEventListener('click', closeMenu);
  if (overlay)   overlay.addEventListener('click', closeMenu);

  // Close on Escape
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeMenu();
  });

  // ── Mobile accordions ─────────────────────────────────────
  accordionToggles.forEach(function (toggle) {
    toggle.addEventListener('click', function () {
      const expanded = this.getAttribute('aria-expanded') === 'true';
      // Close all others
      accordionToggles.forEach(function (t) {
        t.setAttribute('aria-expanded', 'false');
        const body = t.nextElementSibling;
        if (body) body.classList.remove('is-open');
      });
      // Toggle current
      this.setAttribute('aria-expanded', String(!expanded));
      const body = this.nextElementSibling;
      if (body) body.classList.toggle('is-open', !expanded);
    });
  });

})();
