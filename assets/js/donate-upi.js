(function () {
  'use strict';

  const existingGrid = document.querySelector('.donate-grid');
  if (!existingGrid) return;

  document.body.classList.add('upi-donation-page');

  if (!document.querySelector('link[href="assets/css/donate-upi.css"]')) {
    const stylesheet = document.createElement('link');
    stylesheet.rel = 'stylesheet';
    stylesheet.href = 'assets/css/donate-upi.css';
    document.head.appendChild(stylesheet);
  }

  const section = existingGrid.closest('section');
  if (section) section.classList.add('donation-experience');

  existingGrid.outerHTML = `
    <div class="donation-intro">
      <div class="donation-intro__copy">
        <span class="eyebrow" aria-hidden="true">Direct UPI Contribution</span>
        <h2 id="donate-form-heading">Choose your contribution.</h2>
        <p>Select an amount and purpose. Mobile visitors can open an installed UPI app directly; desktop visitors can scan the Bank of Baroda merchant QR.</p>
      </div>
      <div class="donation-trust" aria-label="Payment assurances">
        <span class="donation-trust__pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>Bank-issued QR</span>
        <span class="donation-trust__pill"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 10h18"/></svg>UPI payment</span>
      </div>
    </div>

    <div class="donation-checkout-grid">
      <section class="donation-config" aria-labelledby="donation-config-title">
        <span class="panel-step">Step 01</span>
        <h3 class="panel-title" id="donation-config-title">Set your donation</h3>

        <div class="form-group">
          <span class="field-label">Choose an amount</span>
          <div class="amount-selector" role="group" aria-label="Preset donation amounts">
            <button type="button" class="amount-btn is-active" data-amount="500">₹500</button>
            <button type="button" class="amount-btn" data-amount="1000">₹1,000</button>
            <button type="button" class="amount-btn" data-amount="2500">₹2,500</button>
            <button type="button" class="amount-btn" data-amount="5000">₹5,000</button>
          </div>
          <label for="custom-amount" class="sr-only">Enter a custom donation amount</label>
          <div class="custom-amount-wrap">
            <span class="custom-amount-wrap__symbol" aria-hidden="true">₹</span>
            <input type="number" id="custom-amount" class="form-control" min="1" step="1" inputmode="numeric" placeholder="Enter a whole-rupee amount" autocomplete="off" aria-describedby="custom-amount-help">
          </div>
          <p id="custom-amount-help" class="upi-copy-status" aria-live="polite"></p>
        </div>

        <div class="form-group">
          <span class="field-label">Choose a purpose</span>
          <div class="pillar-selector" role="group" aria-label="Donation purpose">
            <button type="button" class="pillar-btn is-active" data-pillar="where-needed">💛 Where Most Needed</button>
            <button type="button" class="pillar-btn" data-pillar="learning">📚 Holistic Learning</button>
            <button type="button" class="pillar-btn" data-pillar="women">🌸 Women's Equity</button>
            <button type="button" class="pillar-btn" data-pillar="communities">🏡 Resilient Communities</button>
            <button type="button" class="pillar-btn" data-pillar="wellness">🏥 Inclusive Wellness</button>
            <button type="button" class="pillar-btn" data-pillar="climate">☀️ Climate Resilience</button>
            <button type="button" class="pillar-btn" data-pillar="eco">🌿 Eco-Conservation</button>
          </div>
        </div>

        <div class="donation-allocation-note">
          <div class="donation-allocation-note__icon"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 2 2 7l10 5 10-5-10-5Z"/><path d="m2 17 10 5 10-5"/><path d="m2 12 10 5 10-5"/></svg></div>
          <div><h3>Purpose-led contribution</h3><p>Your selected purpose is included in the mobile UPI payment note. Where programme-specific allocation is not practicable, funds may be applied to the area of greatest need.</p></div>
        </div>

        <div class="donation-security-note">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="11" width="18" height="10" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
          <span>Never share your UPI PIN, OTP or banking password. Confirm the foundation name inside your UPI app before authorising payment.</span>
        </div>
      </section>

      <section class="upi-payment-card" aria-labelledby="upi-payment-title">
        <div class="upi-payment-card__accent"></div>
        <div class="upi-payment-card__body">
          <div class="upi-merchant">
            <div class="upi-merchant__identity">
              <div class="upi-merchant__logo"><img src="assets/images/logo-icon.svg" alt="" aria-hidden="true"></div>
              <div>
                <span class="upi-merchant__bank">Bank of Baroda merchant UPI</span>
                <h3 class="upi-merchant__name" id="upi-payment-title">ANANTH SARTH SEVA FOUNDATION</h3>
              </div>
            </div>
            <span class="upi-merchant__status"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m9 12 2 2 4-4"/><circle cx="12" cy="12" r="10"/></svg>Merchant QR</span>
          </div>

          <div class="upi-selection-summary">
            <div>
              <span class="upi-selection-summary__label">Selected contribution</span>
              <strong class="upi-selection-summary__amount" data-selected-amount>₹500</strong>
            </div>
            <p class="upi-selection-summary__purpose">For <strong data-selected-purpose>Where Most Needed</strong></p>
          </div>

          <div class="upi-desktop-flow">
            <div class="upi-qr-frame"><img src="assets/images/payment/upi-donation-qr.svg" alt="UPI QR code for Ananth Sarth Seva Foundation" width="552" height="552" loading="eager"></div>
            <div class="upi-scan-copy">
              <h3>Scan and pay</h3>
              <p id="scan-instruction">Scan the merchant QR and enter ₹500 in your UPI app.</p>
              <span class="upi-scan-copy__tag">Use any UPI-enabled app</span>
            </div>
          </div>

          <a class="upi-open-button" data-upi-link data-dynamic-pay-label href="upi://pay?pa=anan7977386%40barodampay&amp;pn=ANANTH%20SARTH%20SEVA%20FOUNDATION&amp;tn=Donation%20-%20Where%20Most%20Needed&amp;am=500&amp;cu=INR">Pay ₹500 with UPI</a>

          <details class="upi-mobile-qr">
            <summary>Show QR for payment from another device</summary>
            <img src="assets/images/payment/upi-donation-qr.svg" alt="UPI QR code for Ananth Sarth Seva Foundation" width="552" height="552" loading="lazy">
          </details>

          <div class="upi-id-copy">
            <div class="upi-id-copy__content"><span class="upi-id-copy__label">UPI ID</span><span class="upi-id-copy__value">anan7977386@barodampay</span></div>
            <button type="button" class="upi-copy-button" id="copy-upi">Copy</button>
          </div>
          <p class="upi-copy-status" id="copy-status" role="status" aria-live="polite"></p>

          <div class="upi-steps" aria-label="UPI donation steps">
            <div class="upi-step"><span class="upi-step__number">01</span><strong>Open or scan</strong><span>Use the UPI button or scan the merchant QR.</span></div>
            <div class="upi-step"><span class="upi-step__number">02</span><strong>Verify merchant</strong><span>Confirm the foundation name before payment.</span></div>
            <div class="upi-step"><span class="upi-step__number">03</span><strong>Authorise safely</strong><span>Enter your UPI PIN only inside your UPI app.</span></div>
          </div>

          <div class="payment-confirmation">
            <h3>Completed the payment?</h3>
            <p>Share the transaction or UTR number with the Foundation for acknowledgement and reconciliation.</p>
            <a id="payment-confirmation-link" href="mailto:contact@anathsarthsevafoundation.org">Share payment confirmation <span aria-hidden="true">→</span></a>
          </div>

          <p class="payment-legal">Tax benefits, acknowledgements and receipts are subject to applicable law and the Foundation's valid statutory approvals. UPI payment limits and processing are controlled by your bank and UPI app.</p>
        </div>
      </section>
    </div>`;

  if (!document.querySelector('.mobile-upi-bar')) {
    document.body.insertAdjacentHTML('beforeend', `
      <div class="mobile-upi-bar" aria-label="Mobile donation action">
        <div class="mobile-upi-bar__amount"><span>Selected donation</span><strong data-selected-amount>₹500</strong></div>
        <a class="mobile-upi-bar__link" data-upi-link href="upi://pay?pa=anan7977386%40barodampay&amp;pn=ANANTH%20SARTH%20SEVA%20FOUNDATION&amp;tn=Donation%20-%20Where%20Most%20Needed&amp;am=500&amp;cu=INR">Pay with UPI</a>
      </div>`);
  }

  const amountButtons = Array.from(document.querySelectorAll('[data-amount]'));
  const pillarButtons = Array.from(document.querySelectorAll('[data-pillar]'));
  const customAmount = document.getElementById('custom-amount');
  const amountHelp = document.getElementById('custom-amount-help');
  const amountDisplays = document.querySelectorAll('[data-selected-amount]');
  const purposeDisplays = document.querySelectorAll('[data-selected-purpose]');
  const scanInstruction = document.getElementById('scan-instruction');
  const upiLinks = document.querySelectorAll('[data-upi-link]');
  const dynamicPayLabel = document.querySelector('[data-dynamic-pay-label]');
  const copyButton = document.getElementById('copy-upi');
  const copyStatus = document.getElementById('copy-status');
  const confirmationLink = document.getElementById('payment-confirmation-link');

  const merchant = {
    pa: 'anan7977386@barodampay',
    pn: 'ANANTH SARTH SEVA FOUNDATION',
    cu: 'INR'
  };

  const purposeLabels = {
    'where-needed': 'Where Most Needed',
    learning: 'Holistic Learning',
    women: "Women's Equity",
    communities: 'Resilient Communities',
    wellness: 'Inclusive Wellness',
    climate: 'Climate Resilience',
    eco: 'Eco-Conservation'
  };

  let selectedAmount = 500;
  let selectedPurpose = 'where-needed';

  const isValidAmount = (amount) => Number.isInteger(amount) && amount >= 1;

  const formatAmount = (amount) => {
    if (!isValidAmount(amount)) return 'Choose amount';
    return new Intl.NumberFormat('en-IN', {
      style: 'currency',
      currency: 'INR',
      maximumFractionDigits: 0
    }).format(amount);
  };

  const buildUpiLink = () => {
    const params = new URLSearchParams({
      pa: merchant.pa,
      pn: merchant.pn,
      tn: `Donation - ${purposeLabels[selectedPurpose]}`,
      cu: merchant.cu
    });
    if (isValidAmount(selectedAmount)) params.set('am', String(selectedAmount));
    return `upi://pay?${params.toString()}`;
  };

  const updateConfirmationLink = () => {
    if (!confirmationLink) return;
    const amountText = isValidAmount(selectedAmount) ? formatAmount(selectedAmount) : 'Amount not selected';
    const subject = `Donation confirmation - ${merchant.pn}`;
    const body = [
      'Hello Ananth Sarth Seva Foundation,',
      '',
      'I have completed a UPI donation.',
      `Amount: ${amountText}`,
      `Purpose: ${purposeLabels[selectedPurpose]}`,
      `UPI ID: ${merchant.pa}`,
      '',
      'Transaction / UTR number: ',
      'Payment date: ',
      '',
      'Please confirm receipt when convenient.'
    ].join('\n');
    confirmationLink.href = `mailto:contact@anathsarthsevafoundation.org?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
  };

  const setPaymentAvailability = (enabled, upiLink) => {
    upiLinks.forEach((link) => {
      link.classList.toggle('is-disabled', !enabled);
      link.setAttribute('aria-disabled', String(!enabled));
      link.style.pointerEvents = enabled ? '' : 'none';
      link.style.opacity = enabled ? '' : '0.55';
      if (enabled) link.href = upiLink;
      else link.removeAttribute('href');
    });
  };

  const updateUI = () => {
    const enabled = isValidAmount(selectedAmount);
    const amountText = formatAmount(selectedAmount);
    const purposeText = purposeLabels[selectedPurpose];
    const upiLink = buildUpiLink();

    amountDisplays.forEach((node) => { node.textContent = amountText; });
    purposeDisplays.forEach((node) => { node.textContent = purposeText; });
    setPaymentAvailability(enabled, upiLink);

    if (dynamicPayLabel) {
      dynamicPayLabel.textContent = enabled ? `Pay ${amountText} with UPI` : 'Enter a whole-rupee amount';
    }

    if (scanInstruction) {
      scanInstruction.textContent = enabled
        ? `Scan the merchant QR and enter ${amountText} in your UPI app.`
        : 'Enter a valid whole-rupee amount before proceeding.';
    }

    updateConfirmationLink();
  };

  amountButtons.forEach((button) => {
    button.addEventListener('click', () => {
      selectedAmount = Number(button.dataset.amount);
      amountButtons.forEach((item) => item.classList.toggle('is-active', item === button));
      customAmount.value = '';
      customAmount.setCustomValidity('');
      if (amountHelp) amountHelp.textContent = '';
      updateUI();
    });
  });

  customAmount.addEventListener('input', () => {
    const rawValue = customAmount.value.trim();
    const value = Number(rawValue);
    const valid = rawValue !== '' && Number.isInteger(value) && value >= 1;

    selectedAmount = valid ? value : 0;
    amountButtons.forEach((item) => item.classList.remove('is-active'));

    const validationMessage = rawValue === '' || valid
      ? ''
      : 'Enter a whole-rupee amount of ₹1 or more.';

    customAmount.setCustomValidity(validationMessage);
    if (amountHelp) amountHelp.textContent = validationMessage;
    updateUI();
  });

  customAmount.addEventListener('blur', () => {
    if (customAmount.value && !customAmount.checkValidity()) customAmount.reportValidity();
  });

  pillarButtons.forEach((button) => {
    button.addEventListener('click', () => {
      selectedPurpose = button.dataset.pillar;
      pillarButtons.forEach((item) => item.classList.toggle('is-active', item === button));
      updateUI();
    });
  });

  upiLinks.forEach((link) => {
    link.addEventListener('click', (event) => {
      if (!isValidAmount(selectedAmount)) event.preventDefault();
    });
  });

  if (copyButton) {
    copyButton.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(merchant.pa);
      } catch (error) {
        const fallback = document.createElement('input');
        fallback.value = merchant.pa;
        fallback.setAttribute('readonly', '');
        fallback.style.position = 'fixed';
        fallback.style.opacity = '0';
        document.body.appendChild(fallback);
        fallback.select();
        document.execCommand('copy');
        fallback.remove();
      }

      copyButton.textContent = 'Copied';
      if (copyStatus) copyStatus.textContent = 'UPI ID copied to clipboard.';
      window.setTimeout(() => {
        copyButton.textContent = 'Copy';
        if (copyStatus) copyStatus.textContent = '';
      }, 2200);
    });
  }

  updateUI();
})();
