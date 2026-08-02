// ============================================================
// UTILS.JS — Reveal on scroll, counter animation, RtR steps
// ============================================================

(function () {
  'use strict';

  // ── Reveal on scroll ─────────────────────────────────────
  const revealEls = document.querySelectorAll('.reveal');

  if ('IntersectionObserver' in window && revealEls.length) {
    const revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    revealEls.forEach(function (el) { revealObserver.observe(el); });
  } else {
    // Fallback: show everything immediately
    revealEls.forEach(function (el) { el.classList.add('visible'); });
  }

  // ── Staggered reveal ─────────────────────────────────────
  document.querySelectorAll('[data-stagger]').forEach(function (group) {
    const children = group.querySelectorAll('.reveal');
    children.forEach(function (child, i) {
      child.style.transitionDelay = (i * 80) + 'ms';
    });
  });

  // ── Root-to-Rise active step on scroll ───────────────────
  const rtrSteps = document.querySelectorAll('.rtr-step');
  if (rtrSteps.length && 'IntersectionObserver' in window) {
    const stepObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-active');
        }
      });
    }, { threshold: 0.4 });
    rtrSteps.forEach(function (step) { stepObserver.observe(step); });
  }

  // ── Donation amount selector ──────────────────────────────
  const amountBtns = document.querySelectorAll('.amount-btn');
  const customInput = document.getElementById('custom-amount');
  amountBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      amountBtns.forEach(function (b) { b.classList.remove('is-active'); });
      this.classList.add('is-active');
      if (customInput) customInput.value = '';
    });
  });
  if (customInput) {
    customInput.addEventListener('input', function () {
      amountBtns.forEach(function (b) { b.classList.remove('is-active'); });
    });
  }

  // ── Pillar selector ───────────────────────────────────────
  const pillarBtns = document.querySelectorAll('.pillar-btn');
  pillarBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      pillarBtns.forEach(function (b) { b.classList.remove('is-active'); });
      this.classList.add('is-active');
    });
  });

  // ── Newsletter form ───────────────────────────────────────
  const newsletterForms = document.querySelectorAll('.footer__newsletter-form');
  newsletterForms.forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      const input = form.querySelector('.footer__newsletter-input');
      if (input && input.value.trim()) {
        input.value = 'Thank you for subscribing!';
        input.disabled = true;
        const btn = form.querySelector('button');
        if (btn) btn.disabled = true;
      }
    });
  });

  // ── Premium UPI donation module ───────────────────────────
  if (document.querySelector('.donate-grid') && !document.querySelector('script[data-upi-donation-module]')) {
    const donationScript = document.createElement('script');
    donationScript.src = 'assets/js/donate-upi.js';
    donationScript.async = false;
    donationScript.dataset.upiDonationModule = 'true';
    document.body.appendChild(donationScript);
  }

})();
