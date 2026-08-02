document.addEventListener('DOMContentLoaded', () => {
  const amountButtons = Array.from(document.querySelectorAll('[data-amount]'));
  const pillarButtons = Array.from(document.querySelectorAll('[data-pillar]'));
  const customAmount = document.getElementById('custom-amount');
  const amountDisplays = document.querySelectorAll('[data-selected-amount]');
  const purposeDisplays = document.querySelectorAll('[data-selected-purpose]');
  const scanInstruction = document.getElementById('scan-instruction');
  const upiLinks = document.querySelectorAll('[data-upi-link]');
  const dynamicPayLabel = document.querySelector('[data-dynamic-pay-label]');
  const copyButton = document.getElementById('copy-upi');
  const copyStatus = document.getElementById('copy-status');
  const confirmationLink = document.getElementById('payment-confirmation-link');

  if (!amountButtons.length || !pillarButtons.length || !upiLinks.length) return;

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

  const formatAmount = (amount) => {
    const value = Number(amount);
    if (!Number.isFinite(value) || value <= 0) return 'Choose amount';
    return new Intl.NumberFormat('en-IN', {
      style: 'currency',
      currency: 'INR',
      maximumFractionDigits: 0
    }).format(value);
  };

  const buildUpiLink = () => {
    const params = new URLSearchParams({
      pa: merchant.pa,
      pn: merchant.pn,
      tn: `Donation - ${purposeLabels[selectedPurpose]}`,
      cu: merchant.cu
    });
    if (selectedAmount > 0) params.set('am', String(selectedAmount));
    return `upi://pay?${params.toString()}`;
  };

  const updateConfirmationLink = () => {
    if (!confirmationLink) return;
    const amountText = selectedAmount > 0 ? formatAmount(selectedAmount) : 'Custom amount';
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

  const updateUI = () => {
    const amountText = formatAmount(selectedAmount);
    const purposeText = purposeLabels[selectedPurpose];
    const upiLink = buildUpiLink();

    amountDisplays.forEach((node) => { node.textContent = amountText; });
    purposeDisplays.forEach((node) => { node.textContent = purposeText; });
    upiLinks.forEach((link) => { link.href = upiLink; });

    if (dynamicPayLabel) {
      dynamicPayLabel.textContent = selectedAmount > 0
        ? `Pay ${amountText} with UPI`
        : 'Open your UPI app';
    }

    if (scanInstruction) {
      scanInstruction.textContent = selectedAmount > 0
        ? `Scan the merchant QR and enter ${amountText} in your UPI app.`
        : 'Scan the merchant QR and enter your preferred amount in your UPI app.';
    }

    updateConfirmationLink();
  };

  amountButtons.forEach((button) => {
    button.addEventListener('click', () => {
      selectedAmount = Number(button.dataset.amount);
      amountButtons.forEach((item) => item.classList.toggle('is-active', item === button));
      if (customAmount) customAmount.value = '';
      updateUI();
    });
  });

  if (customAmount) {
    const activateCustomAmount = () => {
      const value = Number(customAmount.value);
      selectedAmount = Number.isFinite(value) && value > 0 ? Math.round(value) : 0;
      amountButtons.forEach((item) => item.classList.remove('is-active'));
      updateUI();
    };
    customAmount.addEventListener('input', activateCustomAmount);
    customAmount.addEventListener('focus', activateCustomAmount);
  }

  pillarButtons.forEach((button) => {
    button.addEventListener('click', () => {
      selectedPurpose = button.dataset.pillar;
      pillarButtons.forEach((item) => item.classList.toggle('is-active', item === button));
      updateUI();
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
});
