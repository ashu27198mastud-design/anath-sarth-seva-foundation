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
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
  
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
        <p class="footer__tagline mt-12 fw-500">Serving Humanity, Creating Hope.</p>
        <p class="footer__address mt-16 text-sm opacity-80 lh-16">
        [CLIENT: REGISTERED OFFICE ADDRESS]<br>
        [CLIENT: PHONE NUMBER]<br>
        <a href="mailto:contact@anathsarthsevafoundation.org" class="link--inherit">[CLIENT: OFFICIAL EMAIL]</a></p>
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
    <div class="footer__transparency footer__transparency">
      <div class="container footer__bottom">
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

def build_3d_card(title, desc, icon_svg, idx="01"):
    return f'''
    <div class="feature-card-3d reveal" data-idx="{idx}">
        <div class="feature-icon-wrapper">
            {icon_svg}
        </div>
        <h3 class="t-h3">{title}</h3>
        <p class="text-md mt-12 text-muted">{desc}</p>
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


