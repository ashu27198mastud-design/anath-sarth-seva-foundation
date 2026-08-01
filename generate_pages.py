import os

HEADER_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Ananth Sarth Seva Foundation</title>
  <meta name="description" content="Ananth Sarth Seva Foundation empowers rural and tribal communities.">
  
  <link rel="icon" href="{root_path}assets/images/logo-icon.svg" type="image/svg+xml">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" href="{root_path}assets/css/design-system.css">
  <link rel="stylesheet" href="{root_path}assets/css/components.css">
  <link rel="stylesheet" href="{root_path}assets/css/inner-pages.css">
</head>
<body>
  <!-- HEADER -->
  <header class="header" id="header">
    <div class="header__inner container">
      <a href="{root_path}index.html" class="header__logo">
        <img src="{root_path}assets/images/logo-original.jpg" alt="Ananth Sarth Seva Foundation" class="header__logo-img">
      </a>
      <nav class="header__nav" aria-label="Main navigation">
        <ul class="header__nav-list">
          <li class="header__nav-item"><a href="{root_path}index.html" class="header__nav-link">Home</a></li>
          <li class="header__nav-item header__nav-item--has-dropdown">
            <a href="{root_path}about.html" class="header__nav-link {about_active}">About Us</a>
            <ul class="header__dropdown">
              <li><a href="{root_path}about.html#our-story" class="header__dropdown-link">Our Story</a></li>
              <li><a href="{root_path}about.html#objective" class="header__dropdown-link">Objective</a></li>
              <li><a href="{root_path}about.html#vision" class="header__dropdown-link">Vision</a></li>
              <li><a href="{root_path}about.html#mission" class="header__dropdown-link">Mission</a></li>
              <li><a href="{root_path}about.html#how-we-work" class="header__dropdown-link">How We Work</a></li>
              <li><a href="{root_path}about.html#why-trust-us" class="header__dropdown-link">Why Trust Us</a></li>
            </ul>
          </li>
          <li class="header__nav-item header__nav-item--has-dropdown">
            <a href="{root_path}#pillars" class="header__nav-link {programs_active}">Our Programs</a>
            <ul class="header__dropdown">
              <li><a href="{root_path}programs/holistic-learning.html" class="header__dropdown-link">Holistic Learning</a></li>
              <li><a href="{root_path}programs/womens-equity.html" class="header__dropdown-link">Women's Equity</a></li>
              <li><a href="{root_path}programs/resilient-communities.html" class="header__dropdown-link">Resilient Communities</a></li>
              <li><a href="{root_path}programs/inclusive-wellness.html" class="header__dropdown-link">Inclusive Wellness</a></li>
              <li><a href="{root_path}programs/climate-resilience.html" class="header__dropdown-link">Climate Resilience</a></li>
              <li><a href="{root_path}programs/eco-conservation.html" class="header__dropdown-link">Eco-Conservation</a></li>
            </ul>
          </li>
          <li class="header__nav-item header__nav-item--has-dropdown">
            <a href="{root_path}#get-involved" class="header__nav-link {involved_active}">Get Involved</a>
            <ul class="header__dropdown">
              <li><a href="{root_path}donate.html" class="header__dropdown-link">Donate</a></li>
              <li><a href="{root_path}volunteer.html" class="header__dropdown-link">Volunteer</a></li>
              <li><a href="{root_path}careers.html" class="header__dropdown-link">Work With Us</a></li>
              <li><a href="{root_path}partner.html" class="header__dropdown-link">Partner With Us</a></li>
            </ul>
          </li>
          <li class="header__nav-item"><a href="{root_path}impact.html" class="header__nav-link {impact_active}">Impact</a></li>
          <li class="header__nav-item"><a href="{root_path}contact.html" class="header__nav-link {contact_active}">Contact Us</a></li>
        </ul>
      </nav>
      <a href="{root_path}donate.html" class="header__cta btn btn--primary">Donate Now</a>
      <button class="header__mobile-toggle" aria-label="Open menu" aria-expanded="false" id="mobile-toggle">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      </button>
    </div>
  </header>
  
  <div class="mobile-menu" id="mobile-menu" aria-hidden="true">
    <button class="mobile-menu__close" aria-label="Close menu" id="mobile-menu-close">
      <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
    </button>
    <nav aria-label="Mobile navigation">
        <ul class="mobile-menu__list">
            <li class="mobile-menu__item"><a href="{root_path}index.html" class="mobile-menu__link">Home</a></li>
            <li class="mobile-menu__item"><a href="{root_path}about.html" class="mobile-menu__link">About Us</a></li>
            <li class="mobile-menu__item"><a href="{root_path}donate.html" class="mobile-menu__link">Donate</a></li>
            <li class="mobile-menu__item"><a href="{root_path}contact.html" class="mobile-menu__link">Contact Us</a></li>
        </ul>
    </nav>
  </div>

  <main class="inner-page-main">
"""

FOOTER_TEMPLATE = """
  </main>
  
  <footer class="footer">
    <div class="footer__inner container">
      <div class="footer__col">
        <a href="{root_path}index.html" class="footer__logo">
          <img src="{root_path}assets/images/logo-icon.svg" alt="Ananth Sarth Seva Foundation" width="40" height="40">
          <span class="footer__logo-text">Ananth Sarth Seva Foundation</span>
        </a>
        <p class="footer__tagline" style="margin-top: 12px; font-weight: 500;">Serving Humanity, Creating Hope.</p>
        <p class="footer__address" style="margin-top: 16px; font-size: 14px; opacity: 0.8; line-height: 1.6;">
        [CLIENT: REGISTERED OFFICE ADDRESS]<br>
        [CLIENT: PHONE NUMBER]<br>
        <a href="mailto:contact@anathsarthsevafoundation.org" style="color: inherit; text-decoration: underline;">[CLIENT: OFFICIAL EMAIL]</a></p>
      </div>
      <div class="footer__col">
        <h4 class="footer__heading">About Us</h4>
        <ul class="footer__list">
          <li><a href="{root_path}about.html" class="footer__link">Our Story</a></li>
          <li><a href="{root_path}impact.html" class="footer__link">Our Impact</a></li>
          <li><a href="{root_path}careers.html" class="footer__link">Careers</a></li>
          <li><a href="{root_path}partner.html" class="footer__link">Partner with us</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h4 class="footer__heading">Programs</h4>
        <ul class="footer__list">
          <li><a href="{root_path}programs/holistic-learning.html" class="footer__link">Holistic Learning</a></li>
          <li><a href="{root_path}programs/womens-equity.html" class="footer__link">Women's Equity</a></li>
          <li><a href="{root_path}programs/resilient-communities.html" class="footer__link">Resilient Communities</a></li>
          <li><a href="{root_path}programs/inclusive-wellness.html" class="footer__link">Inclusive Wellness</a></li>
          <li><a href="{root_path}programs/climate-resilience.html" class="footer__link">Climate Resilience</a></li>
          <li><a href="{root_path}programs/eco-conservation.html" class="footer__link">Eco-Conservation</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h4 class="footer__heading">Legal & Policies</h4>
        <ul class="footer__list">
          <li><a href="{root_path}privacy.html" class="footer__link">Privacy Policy</a></li>
          <li><a href="{root_path}terms.html" class="footer__link">Terms of Use</a></li>
          <li><a href="{root_path}donation-policy.html" class="footer__link">Donation Policy</a></li>
          <li><a href="{root_path}refund-policy.html" class="footer__link">Refund Policy</a></li>
          <li><a href="{root_path}accessibility.html" class="footer__link">Accessibility Statement</a></li>
        </ul>
      </div>
    </div>
    
    <!-- Transparency Strip -->
    <div class="footer__transparency" style="background-color: rgba(255,255,255,0.05); padding: 16px 0; margin-top: 32px; border-top: 1px solid rgba(255,255,255,0.1); border-bottom: 1px solid rgba(255,255,255,0.1);">
      <div class="container" style="display: flex; flex-wrap: wrap; gap: 24px; justify-content: space-between; font-size: 13px; opacity: 0.8;">
        <span><strong>Reg. No:</strong> [CLIENT: REGISTRATION NUMBER]</span>
        <span><strong>80G No:</strong> [CLIENT: 80G CERTIFICATE NUMBER]</span>
        <span><strong>12A No:</strong> [CLIENT: 12A REGISTRATION NUMBER]</span>
        <span><strong>PAN:</strong> [CLIENT: PAN]</span>
      </div>
    </div>
    
    <div class="footer__bottom">
      <div class="footer__bottom-inner container">
        <span class="footer__copyright">&copy; 2026 Ananth Sarth Seva Foundation. All rights reserved.</span>
      </div>
    </div>
  </footer>

  <script src="{root_path}assets/js/main.js"></script>
  <script src="{root_path}assets/js/animations.js"></script>
</body>
</html>
"""

def build_3d_card(title, desc, icon_svg):
    return f'''
    <div class="feature-card-3d reveal">
        <div class="feature-icon-wrapper">
            {icon_svg}
        </div>
        <h3 class="heading-md">{title}</h3>
        <p class="text-md" style="margin-top: 12px; color: var(--gray);">{desc}</p>
    </div>
    '''

# Unique Icons definition
ICONS = {
    "users": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M16 21v-2a4 4 0 00-4-4H6a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg>',
    "home": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>',
    "accessibility": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><circle cx="16" cy="4" r="1"/><path d="M18 19v-4.83a2 2 0 0 0-1.12-1.8l-3.3-1.66A2 2 0 0 0 12.69 11h-1.38a2 2 0 0 0-.89.21L7.12 12.8a2 2 0 0 0-1.12 1.8V19"/><path d="M12 11V7"/><path d="M16 7h-8"/><circle cx="12" cy="18" r="4"/></svg>',
    "sprout": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M7 20h10"/><path d="M10 20c5.5-2.5.8-6.4 3-10"/><path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5.4-4.8-.3-1.2-.6-2.3-1.9-3-4.2 2.8-.5 4.4 0 5.5.8z"/><path d="M14.1 6a7 7 0 0 0-1.1 4c1.9-.1 3.3-.6 4.3-1.4 1-1 1.6-2.3 1.7-4.6-2.7.1-4 1-4.9 2z"/></svg>',
    "cpu": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><rect x="4" y="4" width="16" height="16" rx="2" ry="2"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/><line x1="20" y1="9" x2="23" y2="9"/><line x1="20" y1="14" x2="23" y2="14"/><line x1="1" y1="9" x2="4" y2="9"/><line x1="1" y1="14" x2="4" y2="14"/></svg>',
    "monitor": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>',
    "graduation": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>',
    "briefcase": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>',
    "lightbulb": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><line x1="9" y1="18" x2="15" y2="18"/><line x1="10" y1="22" x2="14" y2="22"/><path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1.5.5 2.5 1.5 3.5.75.75 1.23 1.52 1.41 2.5"/></svg>',
    "library": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M4 22h16a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v16a2 2 0 0 1-2 2zm0 0a2 2 0 0 1-2-2v-9c0-1.1.9-2 2-2h2"/><path d="M18 14h-8"/><path d="M15 18h-5"/><path d="M10 6h8"/></svg>',
    "hand-heart": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M11 14h2a2 2 0 1 0 0-4h-3c-.6 0-1.1.2-1.4.6L3 16"/><path d="M18 14h-5.2"/><path d="M12 21c-2.3-2.3-5-5-5-8a5 5 0 0 1 10 0 5 5 0 0 1 10 0c0 3-2.7 5.7-5 8L12 21Z"/></svg>',
    "shield-check": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>',
    "heart-pulse": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/><path d="M3.22 12H9.5l.5-1 2 4.5 2-7 1.5 3.5h5.27"/></svg>',
    "gem": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M6 3h12l4 6-10 13L2 9Z"/><path d="M11 3 8 9l4 13"/><path d="M13 3l3 6-4 13"/></svg>',
    "shopping-bag": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>',
    "rocket": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="M12 15l-3-3a22 22 0 0 1 3.82-13.82 2 2 0 0 1 2.94 0A22 22 0 0 1 15 12c0 1.25-.2 2.45-.55 3.58Z"/><path d="M9 15a22 22 0 0 1 5.92 5.92c1.13.35 2.33.55 3.58.55a22 22 0 0 0 3.82-13.82 2 2 0 0 0 0-2.94A22 22 0 0 0 9 15z"/></svg>',
    "factory": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M2 20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8l-7 5V8l-7 5V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2Z"/><path d="M17 18h1"/><path d="M12 18h1"/><path d="M7 18h1"/></svg>',
    "scissors": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><line x1="20" y1="4" x2="8.12" y2="15.88"/><line x1="14.47" y1="14.48" x2="20" y2="20"/><line x1="8.12" y1="8.12" x2="12" y2="12"/></svg>',
    "layers-3": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M12 2L2 7l10 5 10-5-10-5Z"/><path d="M2 12l10 5 10-5"/><path d="M2 17l10 5 10-5"/></svg>',
    "users-round": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M18 21a8 8 0 0 0-16 0"/><circle cx="10" cy="8" r="5"/><path d="M22 20c0-3.37-2-6.5-4-8a5 5 0 0 0-.45-8.3"/></svg>',
    "landmark": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><line x1="3" y1="22" x2="21" y2="22"/><line x1="6" y1="18" x2="6" y2="11"/><line x1="10" y1="18" x2="10" y2="11"/><line x1="14" y1="18" x2="14" y2="11"/><line x1="18" y1="18" x2="18" y2="11"/><polygon points="12 2 20 7 4 7"/></svg>',
    "school": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M22 9 12 4 2 9v11a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2Z"/><path d="M14 22v-4a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v4"/><path d="M18 22v-4a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v4"/><path d="M14 10h.01"/><path d="M10 10h.01"/><path d="M18 10h.01"/><path d="M6 10h.01"/></svg>',
    "trending-up": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/></svg>',
    "trees": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M12 20v-5"/><path d="M9 15h6l-3-4h4L12 4 8 11h4l-3 4z"/><path d="M19 20v-3"/><path d="M17 17h4l-2-3h2l-2-4-2 4h2l-2 3z"/><path d="M5 20v-3"/><path d="M3 17h4l-2-3h2L5 10 3 14h2l-2 3z"/></svg>',
    "wifi": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M5 12.55a11 11 0 0 1 14.08 0"/><path d="M1.42 9a16 16 0 0 1 21.16 0"/><path d="M8.53 16.11a6 6 0 0 1 6.95 0"/><line x1="12" y1="20" x2="12.01" y2="20"/></svg>',
    "package": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><line x1="16.5" y1="9.4" x2="7.5" y2="4.21"/><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>',
    "flask": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M10 2v7.31"/><path d="M14 9.3V1.99"/><path d="M8.5 2h7"/><path d="M14 9.3a6.5 6.5 0 1 1-4 0"/><line x1="5.52" y1="16" x2="18.48" y2="16"/></svg>',
    "store": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="m2 7 4.41-4.41A2 2 0 0 1 7.83 2h8.34a2 2 0 0 1 1.42.59L22 7"/><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"/><path d="M15 22v-4a2 2 0 0 0-2-2h-2a2 2 0 0 0-2 2v4"/><path d="M2 7h20"/><path d="M22 7v3a2 2 0 0 1-2 2v0a2.7 2.7 0 0 1-1.59-.63.7.7 0 0 0-.82 0A2.7 2.7 0 0 1 16 12a2.7 2.7 0 0 1-1.59-.63.7.7 0 0 0-.82 0A2.7 2.7 0 0 1 12 12a2.7 2.7 0 0 1-1.59-.63.7.7 0 0 0-.82 0A2.7 2.7 0 0 1 8 12a2.7 2.7 0 0 1-1.59-.63.7.7 0 0 0-.82 0A2.7 2.7 0 0 1 4 12v0a2 2 0 0 1-2-2V7"/></svg>',
    "recycle": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M7 15.3l1.8 1.8c.8.8 2.2.8 3 0L17 12"/><path d="M21 9v3h-3"/><path d="M17 8.7l-1.8-1.8c-.8-.8-2.2-.8-3 0L7 12"/><path d="M3 15v-3h3"/></svg>',
    "ambulance": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M10 10H6"/><path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2"/><path d="M19 18h2a1 1 0 0 0 1-1v-3.28a1 1 0 0 0-.68-.95l-1.92-.64A3 3 0 0 0 16.45 12H14"/><path d="M8 8v4"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/></svg>',
    "brain": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.24 2.5 2.5 0 0 1 1.98-3A2.5 2.5 0 0 1 9.5 2Z"/><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.24 2.5 2.5 0 0 0-1.98-3A2.5 2.5 0 0 0 14.5 2Z"/></svg>',
    "droplet": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M12 22a7 7 0 0 0 7-7c0-2-1-3.9-3-5.5s-3.5-4-4-6.5c-.5 2.5-2 4.9-4 6.5C6 11.1 5 13 5 15a7 7 0 0 0 7 7z"/></svg>',
    "apple": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M12 20.94c1.5 0 2.75 1.06 4 1.06 3 0 6-8 6-12.22A4.91 4.91 0 0 0 17 5c-2.22 0-4 1.44-5 2-1-.56-2.78-2-5-2a4.9 4.9 0 0 0-5 4.78C2 14 5 22 8 22c1.25 0 2.5-1.06 4-1.06Z"/><path d="M10 2c1 .5 2 2 2 5"/></svg>',
    "video": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="m22 8-6 4 6 4V8Z"/><rect x="2" y="6" width="14" height="12" rx="2" ry="2"/></svg>',
    "leaf": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/></svg>',
    "flower": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M12 7.5a4.5 4.5 0 1 1 4.5 4.5M12 7.5A4.5 4.5 0 1 0 7.5 12M12 7.5V9m-4.5 3a4.5 4.5 0 1 0 4.5 4.5M7.5 12H9m7.5-4.5a4.5 4.5 0 1 1-4.5 4.5m4.5-4.5H15m-3 4.5v1.5"/></svg>',
    "clipboard": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="M12 11h4"/><path d="M12 16h4"/><path d="M8 11h.01"/><path d="M8 16h.01"/></svg>',
    "heart-handshake": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/><path d="M12 5 9.04 7.96a2.17 2.17 0 0 0 0 3.08v0c.82.82 2.13.85 3 .07l2.07-1.9a2.82 2.82 0 0 1 3.79 0l2.96 2.66"/><path d="m18 15-2-2"/><path d="m15 18-2-2"/></svg>',
    "megaphone": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/></svg>',
    "cloud": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M4 14.899A7 7 0 1 1 15.71 8h1.79a4.5 4.5 0 0 1 2.5 8.242"/><path d="M16 14v6"/><path d="M8 14v6"/><path d="M12 16v6"/></svg>',
    "siren": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M7 12a5 5 0 0 1 5-5v0a5 5 0 0 1 5 5v6H7v-6Z"/><path d="M5 20a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v2H5v-2Z"/><path d="M21 12h1"/><path d="M12 2v1"/><path d="M2 12h1"/></svg>',
    "panel": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg>',
    "zap": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
    "mountain": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="m8 3 4 8 5-5 5 15H2L8 3z"/></svg>',
    "map": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "building": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><rect x="4" y="2" width="16" height="20" rx="2" ry="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01"/><path d="M16 6h.01"/><path d="M12 6h.01"/><path d="M12 10h.01"/><path d="M12 14h.01"/><path d="M16 10h.01"/><path d="M16 14h.01"/><path d="M8 10h.01"/><path d="M8 14h.01"/></svg>',
    "radio": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M4.9 19.1C1 15.2 1 8.8 4.9 4.9"/><path d="M7.8 16.2c-2.3-2.3-2.3-6.1 0-8.5"/><circle cx="12" cy="12" r="2"/><path d="M16.2 7.8c2.3 2.3 2.3 6.1 0 8.5"/><path d="M19.1 4.9C23 8.8 23 15.1 19.1 19"/></svg>',
    "hourglass": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M5 22h14"/><path d="M5 2h14"/><path d="M17 22v-4.172a2 2 0 0 0-.586-1.414L12 12l-4.414 4.414A2 2 0 0 0 7 17.828V22"/><path d="M7 2v4.172a2 2 0 0 0 .586 1.414L12 12l4.414-4.414A2 2 0 0 0 17 6.172V2"/></svg>',
    "waves": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M2 6c.6.5 1.2 1 2.5 1C7 7 7 5 9.5 5c2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/><path d="M2 12c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/><path d="M2 18c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/></svg>',
    "shield-plus": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M8 11h8"/><path d="M12 7v8"/></svg>',
    "wind": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M17.7 7.7a2.5 2.5 0 1 1 1.8 4.3H2"/><path d="M9.6 4.6A2 2 0 1 1 11 8H2"/><path d="M12.6 19.4A2 2 0 1 0 14 16H2"/></svg>',
    "binoculars": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M10 10h4"/><path d="M19 7V4a1 1 0 0 0-1-1h-2a1 1 0 0 0-1 1v3"/><path d="M20 21a2 2 0 0 0 2-2v-3.851c0-1.39-2-2.962-2-4.829V8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v11a2 2 0 0 0 2 2z"/><path d="M 9 7 V 4 a 1 1 0 0 0 -1 -1 H 6 a 1 1 0 0 0 -1 1 v 3"/><path d="M 4 21 a 2 2 0 0 1 -2 -2 v -3.851 c 0 -1.39 2 -2.962 2 -4.829 V 8 a 1 1 0 0 1 1 -1 h 4 a 1 1 0 0 1 1 1 v 11 a 2 2 0 0 1 -2 2 Z"/></svg>',
    "shield": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    "handshake": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="m11 17 2 2a1 1 0 1 0 3-3"/><path d="m14 14 2.5 2.5a1 1 0 1 0 3-3l-3.88-3.88a3 3 0 0 0-4.24 0l-.88.88a1 1 0 1 1-3-3l2.81-2.81a5.79 5.79 0 0 1 7.06-.87l.47.28a2 2 0 0 0 1.42.25L21 4"/><path d="m21 3-6 6"/><path d="m14 14-4-4a1 1 0 1 0-3 3"/><path d="m17 11-2.5-2.5a1 1 0 1 0-3 3l3.88 3.88a3 3 0 0 0 4.24 0l.88-.88a1 1 0 1 1 3 3l-2.81 2.81a5.79 5.79 0 0 1-7.06.87l-.47-.28a2 2 0 0 0-1.42-.25L3 20"/><path d="m3 21 6-6"/></svg>',
}




PAGES = {
    "about.html": {
        "title": "About Us",
        "root_path": "",
        "about_active": "header__nav-link--active",
        "programs_active": "",
        "involved_active": "",
        "impact_active": "",
        "contact_active": "",
        "content": """
    <section class="inner-hero watermark-bg" style="background-color: var(--ivory); padding: 180px 0 80px;">
      <div class="container text-center reveal">
        <h1 class="heading-display">About Us</h1>
        <p class="text-lg" style="max-width: 800px; margin: 24px auto 0;">Ananth Sarth Seva Foundation was newly initiated in 2026 and our journey began with a conversation among close friends who came together with the intention of giving back to society.</p>
      </div>
    </section>
    <section id="our-story" class="section watermark-bg">
      <div class="container reveal">
        <h2 class="heading-lg text-center">Our Story</h2>
        <p class="text-md text-center" style="max-width: 800px; margin: 24px auto;">We felt a shared responsibility to give back to the world. Guided by spiritual values of selfless service and interconnectedness, we realized that creating real change requires a complete plan for human dignity and environmental care. What started as a passionate discussion evolved into a lifelong mission. We saw talented people held back by a lack of opportunities, rich traditions fading due to poverty, and ecosystems threatened by climate change. To break this cycle, we decided to combine ancient wisdom with modern innovation.</p>
      </div>
    </section>
    <section id="vision-mission" class="section" style="background-color: var(--white);">
      <div class="container" style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">
        <div id="vision" class="feature-card-3d reveal">
          <div class="feature-icon-wrapper">""" + ICONS["binoculars"] + """</div>
          <h2 class="heading-lg">Vision</h2>
          <p class="text-md" style="margin-top: 16px;">To build a sustainable global future by transforming vulnerable regions into thriving hubs of innovation and conservation.</p>
        </div>
        <div id="mission" class="feature-card-3d reveal">
          <div class="feature-icon-wrapper">""" + ICONS["rocket"] + """</div>
          <h2 class="heading-lg">Mission</h2>
          <p class="text-md" style="margin-top: 16px;">To empower rural and tribal communities across six core pillars: education, women's equity, self-reliance, holistic healthcare, climate action, and conservation.</p>
        </div>
      </div>
    </section>
    <section id="objective" class="section watermark-bg">
      <div class="container reveal">
        <h2 class="heading-lg text-center">Our Objectives</h2>
        <div class="features-grid">
            """ + build_3d_card("Bridging the Knowledge Gap", "Democratising holistic education and tech-driven skills.", ICONS["library"]) + """
            """ + build_3d_card("Digitising Tradition", "Empowering tribal and marginalized women through digital-commerce.", ICONS["store"]) + """
            """ + build_3d_card("Future-Proofing Villages", "Blending indigenous culture with smart technology.", ICONS["cpu"]) + """
            """ + build_3d_card("Tech-Driven Healthcare", "Merging traditional Indian sciences with digital health tech.", ICONS["brain"]) + """
            """ + build_3d_card("Localized Climate Action", "Deploying community-led clean energy models.", ICONS["zap"]) + """
            """ + build_3d_card("Community-Led Conservation", "Activating local populations as technology-enabled guardians.", ICONS["shield"]) + """
        </div>
      </div>
    </section>
    <section id="how-we-work" class="section" style="background-color: var(--ivory);">
      <div class="container reveal">
        <h2 class="heading-lg text-center">How We Work: The Root-to-Rise Model</h2>
        <p class="text-md text-center" style="max-width: 800px; margin: 24px auto;">We don't believe in temporary fixes. Real, lasting change happens when you look at an ecosystem as a whole. Our 4-Step Operational Framework:</p>
        <div class="features-grid">
            """ + build_3d_card("1. Listen & Learn", "We deeply immerse ourselves in rural and tribal communities to map their unique cultural traditions and natural resources.", ICONS["users-round"]) + """
            """ + build_3d_card("2. Bridge & Blend", "We merge ancient traditions and sciences with digital-age skills, modern medical technology, and localized clean energy.", ICONS["handshake"]) + """
            """ + build_3d_card("3. Digitalize & Scale", "We connect local craftsmanship directly to global markets via digital commerce and smart technology.", ICONS["monitor"]) + """
            """ + build_3d_card("4. Transfer Ownership", "We set up local leadership councils to completely manage the initiatives. Our ultimate goal is our own exit.", ICONS["landmark"]) + """
        </div>
      </div>
    </section>
"""
    }
}


PAGES["programs/holistic-learning.html"] = {
    "title": "Holistic Learning",
    "root_path": "../",
    "about_active": "",
    "programs_active": "header__nav-link--active",
    "involved_active": "",
    "impact_active": "",
    "contact_active": "",
    "content": """
    <section class="inner-hero" style="background-color: #E8F4F8; padding: 132px 0 72px;">
      <div class="container text-center reveal">
        <span class="badge" style="background: var(--royal-blue); color: white; margin-bottom: 16px; display: inline-block;">Education</span>
        <h1 class="heading-display">Holistic Learning</h1>
        <p class="text-lg" style="max-width: 640px; margin: 20px auto 0;">Bridging the educational divide by ensuring high-quality, subsidized, or free institutional access for marginalized communities.</p>
        <div class="hero-image-block">
          <img src="../assets/images/programs/holistic-learning.jpg" alt="Learners in an inclusive classroom setting">
        </div>
        <a href="#initiatives" class="hero-scroll-cue">Explore the initiatives ↓</a>
      </div>
    </section>
    <section class="section watermark-bg" id="initiatives">
        <div class="container reveal">
            <div class="features-grid">
                """ + build_3d_card("Inclusive Classrooms", "Ensuring high-quality access for minorities, tribes, and economically weaker sections.", ICONS["users"]) + """
                """ + build_3d_card("Targeted Child Welfare", "Establishing safe residential environments and hostels.", ICONS["home"]) + """
                """ + build_3d_card("Dignity for Differently-Abled", "Building completely accessible learning infrastructure.", ICONS["accessibility"]) + """
                """ + build_3d_card("Rural & Agrarian Empowerment", "Decentralized learning hubs and reading rooms.", ICONS["sprout"]) + """
                """ + build_3d_card("Next-Gen Tech Access", "AI, robotics, and digital innovation hubs for underprivileged youth.", ICONS["cpu"]) + """
                """ + build_3d_card("Phygital Learning Ecosystems", "Merging physical schools with e-learning platforms.", ICONS["monitor"]) + """
                """ + build_3d_card("Grassroots Incubators", "Incubation and research centres helping youth, women and rural innovators turn hyper-local ideas into sustainable livelihood models.", ICONS["lightbulb"]) + """
                """ + build_3d_card("Skill-to-Market Pipelines", "Vocational centres connecting students directly to market-ready employment or entrepreneurship.", ICONS["briefcase"]) + """
                """ + build_3d_card("Lifelong Learning Continuum", "A pathway spanning early-childhood pre-schools through to higher education.", ICONS["graduation"]) + """
                """ + build_3d_card("Supportive Ecosystems", "Digital libraries, reading rooms, coaching centres and safe student hostels to prevent dropouts.", ICONS["library"]) + """
            </div>
        </div>
    </section>
"""
}

PAGES["programs/womens-equity.html"] = {
    "title": "Women's Equity",
    "root_path": "../",
    "about_active": "",
    "programs_active": "header__nav-link--active",
    "involved_active": "",
    "impact_active": "",
    "contact_active": "",
    "content": """
    <section class="inner-hero" style="background-color: #F8E8F4; padding: 132px 0 72px;">
      <div class="container text-center reveal">
        <span class="badge" style="background: var(--royal-blue); color: white; margin-bottom: 16px; display: inline-block;">Women Empowerment</span>
        <h1 class="heading-display">Women's Equity</h1>
        <p class="text-lg" style="max-width: 640px; margin: 20px auto 0;">Breaking gender-based economic barriers by providing marginalized women with financial literacy, livelihood tools, and sustainable opportunities.</p>
        <div class="hero-image-block">
          <img src="../assets/images/programs/womens-equity.jpg" alt="Women running a community enterprise">
        </div>
        <a href="#initiatives" class="hero-scroll-cue">Explore the initiatives ↓</a>
      </div>
    </section>
    <section class="section watermark-bg" id="initiatives">
        <div class="container reveal">
            <div class="features-grid">
                """ + build_3d_card("Socio-Economic Upliftment", "Providing financial literacy and sustainable income-generating opportunities.", ICONS["gem"]) + """
                """ + build_3d_card("Health & Hygiene Security", "Comprehensive menstrual hygiene management to eliminate stigma.", ICONS["heart-pulse"]) + """
                """ + build_3d_card("Safety & Crisis Networks", "Emergency crisis support services to protect women in distress.", ICONS["shield-check"]) + """
                """ + build_3d_card("Digital Commerce Integration", "Training women in e-commerce to connect rural creators to global marketplaces.", ICONS["shopping-bag"]) + """
                """ + build_3d_card("Micro-Entrepreneurship", "Transforming home-based skills into scalable, women-led enterprises.", ICONS["rocket"]) + """
                """ + build_3d_card("Tribal Inclusivity", "Programmes that honour, protect and monetise the traditional knowledge and skills of tribal women.", ICONS["hand-heart"]) + """
                """ + build_3d_card("Modernized Agro-Processing", "Food processing and value-addition units maximising profit from agricultural produce.", ICONS["factory"]) + """
                """ + build_3d_card("Tech-Driven Craft Centers", "Tailoring, apparel and handicraft centres blending heritage design with contemporary global fashion.", ICONS["scissors"]) + """
                """ + build_3d_card("End-to-End Skilling Ecosystems", "Facilities housing physical skill labs and digital tech labs under one roof.", ICONS["layers-3"]) + """
                """ + build_3d_card("Community Leadership Pipelines", "Mentoring grassroots women leaders to run SHGs, cooperatives and production centres independently.", ICONS["users-round"]) + """
            </div>
        </div>
    </section>
"""
}


PAGES["programs/resilient-communities.html"] = {
    "title": "Resilient Communities",
    "root_path": "../",
    "about_active": "",
    "programs_active": "header__nav-link--active",
    "involved_active": "",
    "impact_active": "",
    "contact_active": "",
    "content": """
    <section class="inner-hero" style="background-color: #FDF4E3; padding: 132px 0 72px;">
      <div class="container text-center reveal">
        <span class="badge" style="background: var(--royal-blue); color: white; margin-bottom: 16px; display: inline-block;">Rural & Urban Development</span>
        <h1 class="heading-display">Resilient Communities</h1>
        <p class="text-lg" style="max-width: 640px; margin: 20px auto 0;">Eliminating rural poverty by creating sustainable, local livelihood models that stop forced distress migration to cities.</p>
        <div class="hero-image-block">
          <img src="../assets/images/programs/resilient-communities.jpg" alt="A connected village community and its households">
        </div>
        <a href="#initiatives" class="hero-scroll-cue">Explore the initiatives ↓</a>
      </div>
    </section>
    <section class="section watermark-bg" id="initiatives">
        <div class="container reveal">
            <div class="features-grid">
                """ + build_3d_card("Cultural & Heritage Preservation", "Documenting and protecting tribal arts and indigenous heritage.", ICONS["landmark"]) + """
                """ + build_3d_card("Smart Village Infrastructure", "Transforming traditional villages into tech-enabled hubs.", ICONS["wifi"]) + """
                """ + build_3d_card("Skill ATMs", "Deploying localized training kiosks for automated, on-demand vocational learning.", ICONS["monitor"]) + """
                """ + build_3d_card("Forest Economy Value Chains", "Advanced processing hubs for minor forest produce to maximize local revenue.", ICONS["trees"]) + """
                """ + build_3d_card("Targeted Rural Education", "Tribal hostels and cultural learning spaces preventing dropouts and ensuring safe housing for remote students.", ICONS["school"]) + """
                """ + build_3d_card("Socio-Economic Development", "Sustainable local livelihood models that stop distress migration to cities.", ICONS["trending-up"]) + """
                """ + build_3d_card("Ecological Stewardship", "Community-led conservation through eco-tourism and natural resource management.", ICONS["recycle"]) + """
                """ + build_3d_card("Agro-Innovation Labs", "Smart labs teaching sustainable agriculture, animal husbandry and climate-resilient farming.", ICONS["flask"]) + """
                """ + build_3d_card("Grassroot Enterprise Hubs", "Rural incubation helping artisans and farmers package, brand and market directly to urban consumers.", ICONS["package"]) + """
                """ + build_3d_card("Self-Sustaining Ecosystems", "Community-owned eco-tourism sites and digital hubs feeding profits back into village infrastructure.", ICONS["store"]) + """
            </div>
        </div>
    </section>
"""
}

PAGES["programs/inclusive-wellness.html"] = {
    "title": "Inclusive Wellness",
    "root_path": "../",
    "about_active": "",
    "programs_active": "header__nav-link--active",
    "involved_active": "",
    "impact_active": "",
    "contact_active": "",
    "content": """
    <section class="inner-hero" style="background-color: #E6F7F1; padding: 132px 0 72px;">
      <div class="container text-center reveal">
        <span class="badge" style="background: var(--royal-blue); color: white; margin-bottom: 16px; display: inline-block;">Healthcare</span>
        <h1 class="heading-display">Inclusive Wellness</h1>
        <p class="text-lg" style="max-width: 640px; margin: 20px auto 0;">Bridging the rural-urban medical divide by deploying mobile medical units to provide doorstep diagnostic and healthcare services.</p>
        <div class="hero-image-block">
          <img src="../assets/images/programs/inclusive-wellness.jpg" alt="Healthcare reaching a remote community">
        </div>
        <a href="#initiatives" class="hero-scroll-cue">Explore the initiatives ↓</a>
      </div>
    </section>
    <section class="section watermark-bg" id="initiatives">
        <div class="container reveal">
            <div class="features-grid">
                """ + build_3d_card("Last-Mile Healthcare Access", "Mobile medical units for remote communities.", ICONS["ambulance"]) + """
                """ + build_3d_card("Destigmatising Mental Health", "Accessible counseling and addiction recovery centers.", ICONS["brain"]) + """
                """ + build_3d_card("Telemedicine & Digital Health", "Connecting world-class doctors to patients in remote areas.", ICONS["video"]) + """
                """ + build_3d_card("Integrative Medical Clinics", "Synthesizing Ayurveda and Naturopathy with modern evidence-based medicine.", ICONS["leaf"]) + """
                """ + build_3d_card("Dignified Health & Hygiene", "Menstrual hygiene programmes eliminating taboos and providing safe, affordable solutions.", ICONS["droplet"]) + """
                """ + build_3d_card("Preventative Nutrition Networks", "Targeted nutritional guidance, dietary planning and community wellness camps.", ICONS["apple"]) + """
                """ + build_3d_card("Mind-Body Innovation Hubs", "Yoga and meditation centres addressing lifestyle stress, anxiety and psychosomatic disorders.", ICONS["flower"]) + """
                """ + build_3d_card("Data-Driven Health Camps", "Technology-backed screening mapping regional health trends to prevent outbreaks.", ICONS["clipboard"]) + """
                """ + build_3d_card("Holistic Recovery Frameworks", "Rehabilitation spaces combining physical healing, psychological recovery and nutritional rebuilding.", ICONS["heart-handshake"]) + """
                """ + build_3d_card("Community Health Mobilizers", "Trained local ambassadors running hygiene drives, nutrition counselling and emergency coordination.", ICONS["megaphone"]) + """
            </div>
        </div>
    </section>
"""
}


PAGES["programs/climate-resilience.html"] = {
    "title": "Climate Resilience",
    "root_path": "../",
    "about_active": "",
    "programs_active": "header__nav-link--active",
    "involved_active": "",
    "impact_active": "",
    "contact_active": "",
    "content": """
    <section class="inner-hero" style="background-color: #E8EDF8; padding: 132px 0 72px;">
      <div class="container text-center reveal">
        <span class="badge" style="background: var(--royal-blue); color: white; margin-bottom: 16px; display: inline-block;">Environmental</span>
        <h1 class="heading-display">Climate Resilience</h1>
        <p class="text-lg" style="max-width: 640px; margin: 20px auto 0;">Building the capacity of vulnerable communities to anticipate, endure, and recover from localized climate-induced shocks.</p>
        <div class="hero-image-block">
          <img src="../assets/images/programs/climate-resilience.jpg" alt="Community-led clean energy and climate resilience">
        </div>
        <a href="#initiatives" class="hero-scroll-cue">Explore the initiatives ↓</a>
      </div>
    </section>
    <section class="section watermark-bg" id="initiatives">
        <div class="container reveal">
            <div class="features-grid">
                """ + build_3d_card("Disaster-Resilient Communities", "Implementing village-level early warning systems and risk reduction programs.", ICONS["siren"]) + """
                """ + build_3d_card("Decentralized Clean Energy Grids", "Smart solar, wind, or bio-energy installations for remote community spaces.", ICONS["panel"]) + """
                """ + build_3d_card("Nature-Based Solution Hubs", "Urban micro-forests, wetland restoration, and soil carbon sinks.", ICONS["trees"]) + """
                """ + build_3d_card("Hyper-Local Carbon Mapping", "Data-tracking tools to help rural localities reduce carbon footprints.", ICONS["map"]) + """
                """ + build_3d_card("Grassroots Climate Adaptation", "Building community capacity to anticipate, endure and recover from localised climate shocks.", ICONS["cloud"]) + """
                """ + build_3d_card("Inclusive Green Development", "Equal, affordable access to clean energy for marginalised groups.", ICONS["zap"]) + """
                """ + build_3d_card("Ecological Stewardship", "Community-led environmental guardianship.", ICONS["mountain"]) + """
                """ + build_3d_card("Climate-Smart Infrastructure", "Resilient, disaster-ready village infrastructure.", ICONS["building"]) + """
                """ + build_3d_card("Eco-Innovation Centers", "Local hubs developing and testing green solutions.", ICONS["lightbulb"]) + """
                """ + build_3d_card("Climate Response Networks", "Village-level early warning and coordinated response.", ICONS["radio"]) + """
            </div>
        </div>
    </section>
"""
}

PAGES["programs/eco-conservation.html"] = {
    "title": "Eco-Conservation",
    "root_path": "../",
    "about_active": "",
    "programs_active": "header__nav-link--active",
    "involved_active": "",
    "impact_active": "",
    "contact_active": "",
    "content": """
    <section class="inner-hero" style="background-color: #F1F8E8; padding: 132px 0 72px;">
      <div class="container text-center reveal">
        <span class="badge" style="background: var(--royal-blue); color: white; margin-bottom: 16px; display: inline-block;">Ecosystem & Natural Resources</span>
        <h1 class="heading-display">Eco-Conservation</h1>
        <p class="text-lg" style="max-width: 640px; margin: 20px auto 0;">Engaging local populations in protecting native forests, trees, and endangered wildlife, fostering a harmonious coexistence.</p>
        <div class="hero-image-block">
          <img src="../assets/images/programs/eco-conservation.jpg" alt="Community guardians protecting local ecosystems">
        </div>
        <a href="#initiatives" class="hero-scroll-cue">Explore the initiatives ↓</a>
      </div>
    </section>
    <section class="section watermark-bg" id="initiatives">
        <div class="container reveal">
            <div class="features-grid">
                """ + build_3d_card("Community-Led Conservation", "Protecting native forests, trees, and endangered wildlife.", ICONS["trees"]) + """
                """ + build_3d_card("Revitalising Shared Waters", "Mobilizing citizens for the cleanup and protection of rivers, lakes, and wetlands.", ICONS["waves"]) + """
                """ + build_3d_card("Tech-Driven Eco-Restoration", "Drone-assisted afforestation and AI-mapped soil health tracking.", ICONS["sprout"]) + """
                """ + build_3d_card("Blue & Green Carbon Vaults", "Utilizing wetlands, oceans, and forests as natural carbon sinks.", ICONS["wind"]) + """
                """ + build_3d_card("Intergenerational Equity", "Safeguarding natural resources for future generations.", ICONS["hourglass"]) + """
                """ + build_3d_card("Public Health Protection", "Linking ecosystem health to community wellbeing.", ICONS["users"]) + """
                """ + build_3d_card("Smart Wildlife Monitoring", "Technology-enabled biodiversity and wildlife tracking.", ICONS["binoculars"]) + """
                """ + build_3d_card("Circular Resource Networks", "Closed-loop waste and resource systems at village level.", ICONS["recycle"]) + """
                """ + build_3d_card("Ecosystem Defense Hubs", "Local centres coordinating habitat and forest protection.", ICONS["shield-plus"]) + """
                """ + build_3d_card("Grassroots Eco-Alliances", "Community coalitions acting as technology-enabled environmental guardians.", ICONS["handshake"]) + """
            </div>
        </div>
    </section>
"""
}


PAGES["impact.html"] = {
    "title": "Our Impact",
    "root_path": "",
    "about_active": "",
    "programs_active": "",
    "involved_active": "",
    "impact_active": "header__nav-link--active",
    "contact_active": "",
    "content": """
    <section class="inner-hero" style="background-color: var(--royal-blue); color: white; padding: 180px 0 80px;">
      <div class="container text-center reveal">
        <h1 class="heading-display text-white">Our Impact</h1>
        <p class="text-lg" style="max-width: 800px; margin: 24px auto 0; opacity: 0.9;">Measurable, community-led change driven by the Root-to-Rise model.</p>
      </div>
    </section>
    
    <section class="section" style="background-color: #050538; color: white;">
      <div class="container reveal">
        <div class="stats-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 40px; text-align: center;">
          <div class="stat-card">
            <h3 class="heading-display" style="color: var(--gold);">[CLIENT: NUMBER OF COMMUNITIES REACHED]</h3>
            <p class="text-md">Communities Reached</p>
          </div>
          <div class="stat-card">
            <h3 class="heading-display" style="color: var(--gold);">[CLIENT: NUMBER OF LEARNERS SUPPORTED]</h3>
            <p class="text-md">Learners Supported</p>
          </div>
          <div class="stat-card">
            <h3 class="heading-display" style="color: var(--gold);">[CLIENT: NUMBER OF WOMEN ENTREPRENEURS]</h3>
            <p class="text-md">Women Entrepreneurs Enabled</p>
          </div>
          <div class="stat-card">
            <h3 class="heading-display" style="color: var(--gold);">[CLIENT: HECTARES RESTORED]</h3>
            <p class="text-md">Hectares Restored</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section watermark-bg">
        <div class="container reveal">
            <h2 class="heading-lg text-center">How We Measure</h2>
            <p class="text-md text-center" style="max-width: 800px; margin: 24px auto 40px;">Our impact tracking is tied directly to our Root-to-Rise model, using data-driven metrics to ensure sustained growth and ultimate community independence.</p>
            <div class="features-grid">
                """ + build_3d_card("Holistic Learning", "Tracking student retention, skill acquisition, and transition to higher education.", ICONS["graduation"]) + """
                """ + build_3d_card("Women's Equity", "Measuring micro-enterprise revenue, financial independence, and community leadership roles.", ICONS["gem"]) + """
                """ + build_3d_card("Resilient Communities", "Monitoring rural out-migration rates and localized economic growth.", ICONS["landmark"]) + """
                """ + build_3d_card("Inclusive Wellness", "Health screening coverage, disease prevention rates, and maternal health metrics.", ICONS["heart-pulse"]) + """
                """ + build_3d_card("Climate Resilience", "Adoption rates of clean energy and disaster response readiness.", ICONS["panel"]) + """
                """ + build_3d_card("Eco-Conservation", "Tracking native tree survival rates and wetland biodiversity health.", ICONS["trees"]) + """
            </div>
        </div>
    </section>

    <section class="section" style="background-color: var(--ivory);">
      <div class="container reveal text-center" style="max-width: 800px;">
        <div class="story-block" style="background: white; padding: 40px; border-radius: 24px; box-shadow: 0 10px 40px rgba(10,10,112,0.05);">
            <img src="assets/images/hero/hero-visual.jpg" alt="Beneficiary story" style="width: 120px; height: 120px; border-radius: 50%; object-fit: cover; margin: 0 auto 24px; border: 2px solid var(--gold);">
            <blockquote style="font-size: 20px; font-style: italic; color: var(--gray); line-height: 1.6; margin-bottom: 24px;">"Since the incubator opened, our cooperative has doubled its production. We are now exporting our crafts and my daughters can go to a good school without us leaving the village."</blockquote>
            <p style="font-weight: 600; color: var(--royal-blue);">Priya M.</p>
            <p style="font-size: 14px; color: var(--gray);">Maharashtra</p>
        </div>
        <div style="margin-top: 56px;">
            <a href="donate.html" class="btn btn--primary">Donate Now</a>
            <a href="partner.html" class="btn btn--secondary" style="margin-left: 16px;">Partner With Us</a>
        </div>
      </div>
    </section>
    
    <section class="section" style="background-color: var(--white); text-align: center;">
      <div class="container reveal">
        <h2 class="heading-md">Transparency & Financials</h2>
        <p style="margin-top: 16px;">We are committed to absolute financial transparency. View our latest annual reports and audited financials.</p>
        <a href="[CLIENT: LINK TO FINANCIALS]" class="btn btn--outline" style="margin-top: 24px;">Download Financial Report</a>
      </div>
    </section>
"""
}


PAGES["partner.html"] = {
    "title": "Partner With Us",
    "root_path": "",
    "about_active": "",
    "programs_active": "",
    "involved_active": "header__nav-link--active",
    "impact_active": "",
    "contact_active": "",
    "content": """
    <section class="inner-hero watermark-bg" style="background-color: var(--ivory); padding: 180px 0 80px;">
      <div class="container text-center reveal">
        <h1 class="heading-display">Partner With Us</h1>
        <p class="text-lg" style="max-width: 800px; margin: 24px auto 0;">Collaborate with Ananth Sarth Seva Foundation to create scalable, tech-enabled social change.</p>
      </div>
    </section>
    
    <section class="section" style="background-color: var(--white);">
      <div class="container reveal">
        <div style="max-width: 800px; margin: 0 auto; text-align: center;">
            <h2 class="heading-md">Why Partner With Us?</h2>
            <p style="margin-top: 16px;">We believe that solving complex rural challenges requires cross-sector collaboration. We partner with CSR initiatives, tech innovators, academic institutions, and government bodies to bring the Root-to-Rise model to life.</p>
        </div>
        
        <div class="features-grid" style="margin-top: 56px;">
            """ + build_3d_card("Corporate Social Responsibility (CSR)", "Deploy your CSR funds into traceable, high-impact, and sustainable community projects.", ICONS["briefcase"]) + """
            """ + build_3d_card("Technology Providers", "Provide software, hardware, and digital tools to empower rural innovators.", ICONS["cpu"]) + """
            """ + build_3d_card("Academic Institutions", "Collaborate on research, skill-building curriculums, and student exchange programs.", ICONS["library"]) + """
        </div>
        
        <div style="text-align: center; margin-top: 64px;">
            <p class="text-md">Ready to explore a partnership?</p>
            <a href="contact.html" class="btn btn--primary" style="margin-top: 24px;">Get in Touch</a>
        </div>
      </div>
    </section>
"""
}

def generate_legal_page(title, content):
    return f"""
    <section class="inner-hero" style="background-color: var(--royal-blue); color: white; padding: 160px 0 60px;">
      <div class="container text-center reveal">
        <h1 class="heading-display text-white">{title}</h1>
      </div>
    </section>
    <section class="section" style="background-color: var(--white);">
      <div class="container reveal" style="max-width: 800px; font-size: 16px; line-height: 1.8;">
        {content}
      </div>
    </section>
"""

PAGES["privacy.html"] = {
    "title": "Privacy Policy",
    "root_path": "",
    "about_active": "",
    "programs_active": "",
    "involved_active": "",
    "impact_active": "",
    "contact_active": "",
    "content": generate_legal_page("Privacy Policy", """
        <h2>1. Introduction</h2>
        <p>Ananth Sarth Seva Foundation is committed to protecting your privacy and ensuring the security of your personal information. This Privacy Policy outlines how we collect, use, disclose, and protect the information you provide when using our website and services.</p>
        
        <h2>2. Information We Collect</h2>
        <p>We may collect personal information such as your name, email address, phone number, mailing address, and payment information when you make a donation, volunteer, or contact us. We also collect non-personal data such as browser type, IP address, and pages visited through cookies and analytics tools.</p>
        
        <h2>3. How We Use Your Information</h2>
        <p>Your information is used to process donations, issue receipts (including 80G tax exemption certificates), respond to inquiries, send newsletters and updates (if opted in), and improve our website and services.</p>
        
        <h2>4. Data Sharing and Disclosure</h2>
        <p>We do not sell, trade, or rent your personal information to third parties. We may share necessary information with trusted service providers (e.g., payment gateways) solely for processing transactions or operating our website, under strict confidentiality agreements. We may also disclose information if required by law.</p>
        
        <h2>5. Data Security</h2>
        <p>We implement appropriate technical and organizational measures to safeguard your data against unauthorized access, alteration, disclosure, or destruction. However, no internet transmission is completely secure.</p>
        
        <h2>6. Your Rights</h2>
        <p>You have the right to access, correct, or request deletion of your personal data. To exercise these rights, please contact our Grievance Officer.</p>
        
        <h2>7. Contact Information</h2>
        <p>Grievance Officer: [CLIENT: GRIEVANCE OFFICER NAME/CONTACT]<br>Email: [CLIENT: OFFICIAL EMAIL]<br>Address: [CLIENT: REGISTERED OFFICE ADDRESS]</p>
    """)
}

PAGES["terms.html"] = {
    "title": "Terms of Use",
    "root_path": "",
    "about_active": "",
    "programs_active": "",
    "involved_active": "",
    "impact_active": "",
    "contact_active": "",
    "content": generate_legal_page("Terms of Use", """
        <h2>1. Acceptance of Terms</h2>
        <p>By accessing and using the Ananth Sarth Seva Foundation website, you agree to comply with and be bound by these Terms of Use. If you do not agree to these terms, please refrain from using our website.</p>
        
        <h2>2. Use of Content</h2>
        <p>All content on this website, including text, graphics, logos, and images, is the property of Ananth Sarth Seva Foundation and is protected by copyright laws. You may use this content for personal, non-commercial purposes only. Any other use requires our prior written consent.</p>
        
        <h2>3. User Conduct</h2>
        <p>You agree to use our website for lawful purposes only and in a manner that does not infringe on the rights of, or restrict the use of the site by, any third party. Harassment, defamatory content, and unauthorized access are strictly prohibited.</p>
        
        <h2>4. Donations and Payments</h2>
        <p>All donations made through our website are subject to our Donation and Refund Policies. By making a payment, you confirm that you are authorized to use the provided payment method.</p>
        
        <h2>5. Disclaimer of Warranties</h2>
        <p>The information on this website is provided "as is" without any representations or warranties, express or implied. We do not guarantee that the website will be error-free or uninterrupted.</p>
        
        <h2>6. Limitation of Liability</h2>
        <p>Ananth Sarth Seva Foundation shall not be liable for any direct, indirect, incidental, or consequential damages arising out of your use of or inability to use the website.</p>
        
        <h2>7. Governing Law</h2>
        <p>These terms shall be governed by and construed in accordance with the laws of India. Any disputes shall be subject to the exclusive jurisdiction of the courts in the state where our registered office is located.</p>
    """)
}

PAGES["donation-policy.html"] = {
    "title": "Donation Policy",
    "root_path": "",
    "about_active": "",
    "programs_active": "",
    "involved_active": "",
    "impact_active": "",
    "contact_active": "",
    "content": generate_legal_page("Donation Policy", """
        <h2>1. Purpose of Donations</h2>
        <p>Donations received by Ananth Sarth Seva Foundation are utilized to fund our core programs: Holistic Learning, Women's Equity, Resilient Communities, Inclusive Wellness, Climate Resilience, and Eco-Conservation.</p>
        
        <h2>2. Donation Processing</h2>
        <p>We accept donations via secure online payment gateways, bank transfers, and cheques. All transactions are processed in Indian Rupees (INR) unless otherwise specified.</p>
        
        <h2>3. Tax Exemption (80G)</h2>
        <p>Ananth Sarth Seva Foundation is registered under Section 80G of the Income Tax Act, 1961. Donors are eligible for tax exemption on their contributions as per the prevailing laws. Ensure you provide your PAN details during the donation process to receive a valid 80G receipt.</p>
        
        <h2>4. Receipts</h2>
        <p>A formal receipt and an 80G certificate will be issued for all valid donations. Electronic receipts are typically sent within a few business days following successful payment realization.</p>
        
        <h2>5. Foreign Contributions</h2>
        <p>Currently, we accept foreign contributions only in compliance with the Foreign Contribution (Regulation) Act (FCRA). Please contact us directly if you wish to make an international donation.</p>
    """)
}

PAGES["refund-policy.html"] = {
    "title": "Refund Policy",
    "root_path": "",
    "about_active": "",
    "programs_active": "",
    "involved_active": "",
    "impact_active": "",
    "contact_active": "",
    "content": generate_legal_page("Refund Policy", """
        <h2>1. General Policy</h2>
        <p>Ananth Sarth Seva Foundation treats all donations as voluntary contributions. As a general rule, donations once made cannot be refunded.</p>
        
        <h2>2. Exceptional Circumstances for Refund</h2>
        <p>We may consider refund requests in exceptional circumstances, such as:</p>
        <ul>
            <li>Duplicate transactions due to technical errors.</li>
            <li>Fraudulent use of a credit/debit card.</li>
        </ul>
        
        <h2>3. Requesting a Refund</h2>
        <p>If you believe you are entitled to a refund based on the above criteria, you must submit a written request to [CLIENT: OFFICIAL EMAIL] within 7 days of the transaction date. Your request must include:</p>
        <ul>
            <li>Date of Donation</li>
            <li>Donation Amount</li>
            <li>Transaction ID or Reference Number</li>
            <li>Reason for the refund request</li>
        </ul>
        
        <h2>4. Processing</h2>
        <p>All refund decisions are at the sole discretion of the Foundation's management. If approved, refunds will be processed and credited back to the original source of payment within 10-15 business days.</p>
    """)
}

PAGES["accessibility.html"] = {
    "title": "Accessibility Statement",
    "root_path": "",
    "about_active": "",
    "programs_active": "",
    "involved_active": "",
    "impact_active": "",
    "contact_active": "",
    "content": generate_legal_page("Accessibility Statement", """
        <h2>Our Commitment</h2>
        <p>Ananth Sarth Seva Foundation is committed to ensuring digital accessibility for people with disabilities. We are continually improving the user experience for everyone and applying the relevant accessibility standards.</p>
        
        <h2>Conformance Status</h2>
        <p>The Web Content Accessibility Guidelines (WCAG) defines requirements for designers and developers to improve accessibility for people with disabilities. We strive to conform to WCAG 2.1 level AA standards.</p>
        
        <h2>Key Accessibility Features</h2>
        <ul>
            <li><strong>Clear Hierarchy:</strong> Use of semantic HTML and clear heading structures.</li>
            <li><strong>Keyboard Navigation:</strong> Our site is designed to be navigable using a keyboard.</li>
            <li><strong>Color Contrast:</strong> Text and background colors are chosen to ensure sufficient contrast.</li>
            <li><strong>Alternative Text:</strong> Informative images include descriptive alt text.</li>
        </ul>
        
        <h2>Feedback</h2>
        <p>We welcome your feedback on the accessibility of our website. If you encounter accessibility barriers, please let us know at [CLIENT: OFFICIAL EMAIL]. We try to respond to feedback within 5 business days.</p>
    """)
}

# GENERATION SCRIPT
def generate_pages():
    for filepath, data in PAGES.items():
        html_content = HEADER_TEMPLATE.format(
            title=data["title"],
            root_path=data["root_path"],
            about_active=data["about_active"],
            programs_active=data["programs_active"],
            involved_active=data["involved_active"],
            impact_active=data["impact_active"],
            contact_active=data["contact_active"]
        )
        html_content += data["content"]
        html_content += FOOTER_TEMPLATE.format(
            root_path=data["root_path"]
        )
        
        os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else '.', exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Generated {filepath}")
    print("All pages generated successfully!")

if __name__ == "__main__":
    generate_pages()


