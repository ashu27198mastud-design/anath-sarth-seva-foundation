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
        if (entry.isIntersecting) entry.target.classList.add('is-active');
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

  // ── Enquiry forms (volunteer, contact, careers, newsletter) ──
  // The site is static, so a plain POST returns an error from the web server.
  // If FORM_ENDPOINT is set (e.g. a Formspree, Web3Forms or Google Apps Script
  // URL that accepts form POSTs and replies with JSON), submissions are sent
  // there. Until then, the visitor's email app opens with every answer filled
  // in, addressed to the foundation, so nothing they typed is lost.
  const FORM_ENDPOINT = '';
  const CONTACT_EMAIL = 'contact@anathsarthsevafoundation.org';

  const FORM_COPY = {
    'Volunteer application form': {
      subject: 'Volunteer application',
      sent: 'Thank you. Your application has reached the foundation. We aim to reply by email within 5 working days.',
      mail: 'Your email app has opened with your application filled in. Press Send there to complete it. We aim to reply within 5 working days.'
    },
    'Contact form': {
      subject: 'Website enquiry',
      sent: 'Thank you. Your message has reached the foundation. We aim to reply by email within 5 working days.',
      mail: 'Your email app has opened with your message filled in. Press Send there to complete it.'
    },
    'Career expression of interest form': {
      subject: 'Career expression of interest',
      sent: 'Thank you. Your interest has reached the foundation. We will contact you if a suitable role opens.',
      mail: 'Your email app has opened with your details filled in. Press Send there to complete it.'
    },
    'Newsletter subscription': {
      subject: 'Please add me to the newsletter',
      sent: 'Thank you. You are on the list for programme updates.',
      mail: 'Your email app has opened with a subscribe request. Press Send there to join the list.'
    }
  };

  const fieldLabel = function (form, field) {
    const label = field.id ? form.querySelector('label[for="' + field.id + '"]') : field.closest('label');
    const text = label ? label.textContent : field.name;
    return text.replace(/\*/g, '').replace(/\s+/g, ' ').trim().split('. See our')[0];
  };

  const collect = function (form) {
    const lines = [];
    Array.prototype.forEach.call(form.elements, function (field) {
      if (!field.name || field.type === 'submit' || field.type === 'button') return;
      if (field.type === 'checkbox') {
        lines.push((field.name === 'consent' ? 'Consent given' : fieldLabel(form, field)) + ': ' + (field.checked ? 'Yes' : 'No'));
        return;
      }
      const value = (field.value || '').trim();
      if (value) lines.push(fieldLabel(form, field) + ': ' + value);
    });
    return lines;
  };

  // keepForm: for the email-app hand-off we cannot know whether the visitor
  // actually sent the email, so the filled-in form stays on the page and the
  // panel offers to reopen the email or copy the message instead.
  const showConfirmation = function (form, message, mailto) {
    const previous = form.parentNode.querySelector('.form-confirmation');
    if (previous) previous.remove();
    const panel = document.createElement('div');
    panel.className = 'form-confirmation';
    panel.setAttribute('role', 'status');
    panel.setAttribute('tabindex', '-1');
    const heading = document.createElement('strong');
    heading.textContent = form.classList.contains('footer__newsletter-form') ? 'Almost there' : 'What happens next';
    const text = document.createElement('p');
    text.textContent = message;
    panel.appendChild(heading);
    panel.appendChild(text);
    if (mailto) {
      const actions = document.createElement('div');
      actions.className = 'form-confirmation__actions';
      const reopen = document.createElement('a');
      reopen.href = mailto.href;
      reopen.textContent = 'Open email again';
      const copyBtn = document.createElement('button');
      copyBtn.type = 'button';
      copyBtn.textContent = 'Copy my message';
      copyBtn.addEventListener('click', function () {
        const done = function () { copyBtn.textContent = 'Copied. Paste it into an email to ' + CONTACT_EMAIL; };
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(mailto.body).then(done, function () { window.prompt('Copy your message:', mailto.body); });
        } else {
          window.prompt('Copy your message:', mailto.body);
        }
      });
      actions.appendChild(reopen);
      actions.appendChild(copyBtn);
      panel.appendChild(actions);
      form.insertAdjacentElement('beforebegin', panel);
    } else {
      form.hidden = true;
      form.insertAdjacentElement('afterend', panel);
    }
    panel.focus();
  };

  const showError = function (form, message) {
    let error = form.querySelector('.form-error');
    if (!error) {
      error = document.createElement('p');
      error.className = 'form-error';
      error.setAttribute('role', 'alert');
      form.appendChild(error);
    }
    error.textContent = message;
  };

  document.querySelectorAll('form[data-ajax-form]').forEach(function (form) {
    const copy = FORM_COPY[form.dataset.ajaxForm] || FORM_COPY['Contact form'];
    form.addEventListener('submit', function (event) {
      event.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }

      const button = form.querySelector('[type="submit"]');
      const lines = collect(form);

      if (!FORM_ENDPOINT) {
        const body = lines.join('\n') + '\n\nSent from the website (' + location.pathname + ')';
        const href = 'mailto:' + CONTACT_EMAIL + '?subject=' + encodeURIComponent(copy.subject) + '&body=' + encodeURIComponent(body);
        window.location.href = href;
        showConfirmation(form, copy.mail + ' If nothing opened, copy your message below and email it to ' + CONTACT_EMAIL + '. Your answers are still in the form.', { href: href, body: body });
        return;
      }

      const original = button ? button.textContent : '';
      if (button) { button.disabled = true; button.textContent = 'Sending…'; }
      const data = new FormData(form);
      data.append('_subject', copy.subject);
      data.append('form', form.dataset.ajaxForm);

      fetch(FORM_ENDPOINT, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
        .then(function (response) {
          if (!response.ok) throw new Error('HTTP ' + response.status);
          showConfirmation(form, copy.sent);
        })
        .catch(function () {
          if (button) { button.disabled = false; button.textContent = original; }
          showError(form, 'We could not send this just now. Your answers are still here; please try again, or email ' + CONTACT_EMAIL + '.');
        });
    });
  });

  // ── Premium UPI donation module ───────────────────────────
  const donationGrid = document.querySelector('.donate-grid');
  if (donationGrid) {
    // The hosted site is static. Never allow the legacy form to POST to Nginx,
    // which would otherwise return HTTP 405 while the enhanced UI is loading.
    const legacyDonationForm = donationGrid.querySelector('form');
    if (legacyDonationForm) {
      legacyDonationForm.addEventListener('submit', function (event) {
        event.preventDefault();
      });
    }

    const loadEmbeddedPaymentStyles = function () {
      if (document.querySelector('link[data-upi-embedded-styles]')) return;
      const embeddedStyles = document.createElement('link');
      embeddedStyles.rel = 'stylesheet';
      embeddedStyles.href = 'assets/css/donate-upi-embedded.css?v=20260802-1';
      embeddedStyles.dataset.upiEmbeddedStyles = 'true';
      document.head.appendChild(embeddedStyles);
    };

    const existingDonationScript = document.querySelector('script[data-upi-donation-module]');
    if (!existingDonationScript) {
      const donationScript = document.createElement('script');
      donationScript.src = 'assets/js/donate-upi.js?v=20261107';
      donationScript.async = false;
      donationScript.dataset.upiDonationModule = 'true';
      donationScript.addEventListener('load', loadEmbeddedPaymentStyles, { once: true });
      document.body.appendChild(donationScript);
    } else {
      loadEmbeddedPaymentStyles();
    }
  }

})();
