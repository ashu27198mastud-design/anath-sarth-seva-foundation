document.addEventListener('DOMContentLoaded', () => {
  const amountButtons = Array.from(document.querySelectorAll('[data-donation-amount]'));
  const customAmount = document.getElementById('custom-amount');
  const purposeSelect = document.getElementById('donation-purpose');
  const amountDisplays = document.querySelectorAll('[data-selected-amount]');
  const purposeDisplays = document.querySelectorAll('[data-selected-purpose]');
  const scanInstruction = document.getElementById('scan-instruction');
  const upiLinks = document.querySelectorAll('[data-upi-link]');
  const copyButton = document.getElementById('copy-upi');
  const copyStatus = document.getElementById('copy-status');
  const confirmationLink = document.getElementById('payment-confirmation-link');

  if (!amountButtons.length || !purposeSelect || !upiLinks.length) return;

  const merchant = {
    pa: 'anan7977386@barodampay',
    pn: 'ANANTH SARTH SEVA FOUNDATION',
    cu: 'INR'
  };

  let selectedAmount = 1000;

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
    const purpose = purposeSelect.options[purposeSelect.selectedIndex].text;
    const params = new URLSearchParams({
      pa: merchant.pa,
      pn: merchant.pn,
      tn: `Donation - ${purpose}`,
      cu: merchant.cu
    });

    if (selectedAmount > 0) {
      params.set('am', String(selectedAmount));
    }

    return `upi://pay?${params.toString()}`;
  };

  const updateConfirmationLink = () => {
    if (!confirmationLink) return;

    const purpose = purposeSelect.options[purposeSelect.selectedIndex].text;
    const amountText = selectedAmount > 0 ? formatAmount(selectedAmount) : 'Custom amount';
    const subject = `Donation confirmation - ${merchant.pn}`;
    const body = [
      'Hello Ananth Sarth Seva Foundation,',
      '',
      'I have completed a UPI donation.',
      `Amount: ${amountText}`,
      `Purpose: ${purpose}`,
      `UPI ID: ${merchant.pa}`,
      '',
      'Transaction / UTR number: ',
      'Payment date: ',
      '',
      'Please confirm receipt when convenient.'
    ].join('\n');

    confirmationLink.href = `mailto:contact@anathsarthsevafoundation.org?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
  };

  const updateDonationUI = () => {
    const amountText = formatAmount(selectedAmount);
    const purpose = purposeSelect.options[purposeSelect.selectedIndex].text;
    const upiLink = buildUpiLink();

    amountDisplays.forEach((element) => {
      element.textContent = amountText;
    });

    purposeDisplays.forEach((element) => {
      element.textContent = purpose;
    });

    upiLinks.forEach((link) => {
      link.href = upiLink;
      if (link.matches('[data-dynamic-pay-label]')) {
        link.textContent = selectedAmount > 0
          ? `Pay ${amountText} with UPI`
          : 'Open your UPI app';
      }
    });

    if (scanInstruction) {
      scanInstruction.textContent = selectedAmount > 0
        ? `Scan the QR and enter ${amountText} in your UPI app.`
        : 'Scan the QR and enter your preferred amount in your UPI app.';
    }

    updateConfirmationLink();
  };

  amountButtons.forEach((button) => {
    button.addEventListener('click', () => {
      selectedAmount = Number(button.dataset.donationAmount);

      amountButtons.forEach((item) => {
        item.setAttribute('aria-pressed', String(item === button));
      });

      if (customAmount) customAmount.value = '';
      updateDonationUI();
    });
  });

  if (customAmount) {
    const activateCustomAmount = () => {
      const value = Number(customAmount.value);
      selectedAmount = Number.isFinite(value) && value > 0 ? Math.round(value) : 0;
      amountButtons.forEach((item) => item.setAttribute('aria-pressed', 'false'));
      updateDonationUI();
    };

    customAmount.addEventListener('input', activateCustomAmount);
    customAmount.addEventListener('focus', activateCustomAmount);
  }

  purposeSelect.addEventListener('change', updateDonationUI);

  if (copyButton) {
    copyButton.addEventListener('click', async () => {
      const upiId = merchant.pa;

      try {
        await navigator.clipboard.writeText(upiId);
      } catch (error) {
        const temporaryInput = document.createElement('input');
        temporaryInput.value = upiId;
        temporaryInput.setAttribute('readonly', '');
        temporaryInput.style.position = 'fixed';
        temporaryInput.style.opacity = '0';
        document.body.appendChild(temporaryInput);
        temporaryInput.select();
        document.execCommand('copy');
        temporaryInput.remove();
      }

      copyButton.textContent = 'Copied';
      if (copyStatus) copyStatus.textContent = 'UPI ID copied to clipboard.';

      window.setTimeout(() => {
        copyButton.textContent = 'Copy';
        if (copyStatus) copyStatus.textContent = '';
      }, 2200);
    });
  }

  updateDonationUI();
});
