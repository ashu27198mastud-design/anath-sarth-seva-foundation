"""
build_site.py — Generates all inner pages for Ananth Sarth Seva Foundation
Run: python build_site.py
"""
import os

# ── Shared snippets ─────────────────────────────────────────────────────────

FONTS = '<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">'

def css(root=''):
    return f"""  <link rel="stylesheet" href="{root}assets/css/tokens.css">
  <link rel="stylesheet" href="{root}assets/css/base.css">
  <link rel="stylesheet" href="{root}assets/css/header.css">
  <link rel="stylesheet" href="{root}assets/css/footer.css">
  <link rel="stylesheet" href="{root}assets/css/pages.css">"""

def scripts(root=''):
    return f"""  <script src="{root}assets/js/nav.js" defer></script>
  <script src="{root}assets/js/utils.js" defer></script>"""

def sr_only():
    return '<style>.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}</style>'

def header(root='', active=''):
    nav_items = [
        ('index.html', 'Home'),
        ('about.html', 'About Us'),
        ('root-to-rise.html', 'Root-to-Rise'),
        ('programs/index.html', 'Our Programs'),
        ('impact.html', 'Impact'),
        ('transparency.html', 'Transparency'),
        ('contact.html', 'Contact'),
    ]
    links = ''
    for href, label in nav_items:
        active_cls = ' header__nav-link--active" aria-current="page' if label == active else ''
        if label == 'Our Programs':
            links += f'''<li class="header__nav-item header__nav-item--has-dropdown">
            <a href="{root}programs/index.html" class="header__nav-link{active_cls}">
              Our Programs
              <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
            </a>
            <div class="header__dropdown" role="menu">
              <a href="{root}programs/holistic-learning.html" class="header__dropdown-item" role="menuitem"><span class="header__dropdown-icon" style="background:rgba(26,92,154,.12);">📚</span><span class="header__dropdown-text"><span class="header__dropdown-name">Holistic Learning</span><span class="header__dropdown-desc">Education, digital skills &amp; lifelong learning</span></span></a>
              <a href="{root}programs/womens-equity.html" class="header__dropdown-item" role="menuitem"><span class="header__dropdown-icon" style="background:rgba(181,107,82,.12);">🌸</span><span class="header__dropdown-text"><span class="header__dropdown-name">Women's Equity</span><span class="header__dropdown-desc">Livelihoods, safety &amp; community leadership</span></span></a>
              <a href="{root}programs/resilient-communities.html" class="header__dropdown-item" role="menuitem"><span class="header__dropdown-icon" style="background:rgba(139,105,20,.12);">🏡</span><span class="header__dropdown-text"><span class="header__dropdown-name">Resilient Communities</span><span class="header__dropdown-desc">Rural enterprise &amp; cultural heritage</span></span></a>
              <a href="{root}programs/inclusive-wellness.html" class="header__dropdown-item" role="menuitem"><span class="header__dropdown-icon" style="background:rgba(26,122,114,.12);">🏥</span><span class="header__dropdown-text"><span class="header__dropdown-name">Inclusive Wellness</span><span class="header__dropdown-desc">Healthcare access &amp; integrative wellbeing</span></span></a>
              <a href="{root}programs/climate-resilience.html" class="header__dropdown-item" role="menuitem"><span class="header__dropdown-icon" style="background:rgba(26,122,78,.12);">☀️</span><span class="header__dropdown-text"><span class="header__dropdown-name">Climate Resilience</span><span class="header__dropdown-desc">Clean energy &amp; climate adaptation</span></span></a>
              <a href="{root}programs/eco-conservation.html" class="header__dropdown-item" role="menuitem"><span class="header__dropdown-icon" style="background:rgba(27,94,32,.12);">🌿</span><span class="header__dropdown-text"><span class="header__dropdown-name">Eco-Conservation</span><span class="header__dropdown-desc">Forests, water &amp; biodiversity</span></span></a>
              <div class="header__dropdown-footer"><a href="{root}programs/index.html" class="header__dropdown-all">View all programs →</a></div>
            </div>
          </li>'''
        else:
            links += f'<li class="header__nav-item"><a href="{root}{href}" class="header__nav-link{active_cls}">{label}</a></li>\n          '
    return f'''<header class="header header--solid" id="header" role="banner">
    <div class="header__inner container">
      <a href="{root}index.html" class="header__logo" aria-label="Ananth Sarth Seva Foundation — Home">
        <img src="{root}assets/images/logo-full.png" alt="Ananth Sarth Seva Foundation" class="header__logo-img" width="210" height="64" loading="eager">
      </a>
      <nav class="header__nav" aria-label="Main navigation">
        <ul class="header__nav-list" role="list">
          {links}
        </ul>
      </nav>
      <div class="header__actions">
        <a href="{root}volunteer.html" class="header__btn header__btn--outline btn">Volunteer</a>
        <a href="{root}donate.html" class="header__btn header__btn--donate btn">Donate Now</a>
      </div>
      <button class="header__menu-btn" id="menu-btn" aria-label="Open navigation menu" aria-expanded="false" aria-controls="mobile-nav">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 12h18M3 6h18M3 18h18"/></svg>
      </button>
    </div>
  </header>
  <div class="mobile-nav" id="mobile-nav" aria-modal="true" role="dialog" aria-label="Navigation">
    <div class="mobile-nav__overlay" aria-hidden="true"></div>
    <div class="mobile-nav__panel">
      <div class="mobile-nav__head">
        <a href="{root}index.html" aria-label="Home"><img src="{root}assets/images/logo-full.png" alt="Ananth Sarth Seva Foundation" class="mobile-nav__logo-img" width="178" height="54" loading="lazy"></a>
        <button class="mobile-nav__close" id="mobile-nav-close" aria-label="Close navigation"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M18 6L6 18M6 6l12 12"/></svg></button>
      </div>
      <nav class="mobile-nav__body" aria-label="Mobile navigation">
        <a href="{root}index.html" class="mobile-nav__link">Home</a>
        <a href="{root}about.html" class="mobile-nav__link">About Us</a>
        <a href="{root}root-to-rise.html" class="mobile-nav__link">Root-to-Rise</a>
        <button class="mobile-nav__accordion-toggle" aria-expanded="false" aria-controls="mob-programs">Our Programs <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button>
        <div class="mobile-nav__accordion-body" id="mob-programs">
          <a href="{root}programs/holistic-learning.html" class="mobile-nav__sub-link">📚 Holistic Learning</a>
          <a href="{root}programs/womens-equity.html" class="mobile-nav__sub-link">🌸 Women's Equity</a>
          <a href="{root}programs/resilient-communities.html" class="mobile-nav__sub-link">🏡 Resilient Communities</a>
          <a href="{root}programs/inclusive-wellness.html" class="mobile-nav__sub-link">🏥 Inclusive Wellness</a>
          <a href="{root}programs/climate-resilience.html" class="mobile-nav__sub-link">☀️ Climate Resilience</a>
          <a href="{root}programs/eco-conservation.html" class="mobile-nav__sub-link">🌿 Eco-Conservation</a>
          <a href="{root}programs/index.html" class="mobile-nav__sub-link">→ View All Programs</a>
        </div>
        <a href="{root}impact.html" class="mobile-nav__link">Impact</a>
        <a href="{root}transparency.html" class="mobile-nav__link">Transparency</a>
        <a href="{root}contact.html" class="mobile-nav__link">Contact</a>
      </nav>
      <div class="mobile-nav__foot">
        <a href="{root}volunteer.html" class="btn btn--ghost">Volunteer</a>
        <a href="{root}donate.html" class="btn btn--primary">Donate Now</a>
      </div>
    </div>
  </div>'''

def footer(root=''):
    return f'''<footer class="footer" role="contentinfo">
    <div class="footer__newsletter">
      <div class="container">
        <div class="footer__newsletter-inner">
          <div class="footer__newsletter-text">
            <h3>Stay connected to the movement.</h3>
            <p>Updates on programs, impact and opportunities — directly to your inbox.</p>
          </div>
          <form class="footer__newsletter-form" aria-label="Newsletter subscription">
            <label for="newsletter-email" class="sr-only">Email address</label>
            <input type="email" id="newsletter-email" class="footer__newsletter-input" placeholder="Your email address" autocomplete="email" required>
            <button type="submit" class="btn btn--primary">Subscribe</button>
          </form>
        </div>
      </div>
    </div>
    <div class="footer__body">
      <div class="container">
        <div class="footer__grid">
          <div class="footer__brand">
            <img src="{root}assets/images/logo-full.png" alt="Ananth Sarth Seva Foundation" class="footer__brand-logo" width="210" height="64" loading="lazy">
            <p class="footer__brand-tagline">Ancient wisdom. Modern innovation. Community ownership. Building self-reliant communities from strong roots.</p>
            <div class="footer__social" role="list" aria-label="Social media links">
              <a href="#" class="footer__social-link" aria-label="LinkedIn" role="listitem"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16 8a6 6 0 016 6v7h-4v-7a2 2 0 00-2-2 2 2 0 00-2 2v7h-4v-7a6 6 0 016-6zM2 9h4v12H2zm2-5a2 2 0 110 4 2 2 0 010-4z"/></svg></a>
              <a href="#" class="footer__social-link" aria-label="Instagram" role="listitem"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg></a>
            </div>
          </div>
          <div>
            <div class="footer__col-title">Foundation</div>
            <ul class="footer__col-links" role="list">
              <li><a href="{root}about.html" class="footer__col-link">About Us</a></li>
              <li><a href="{root}root-to-rise.html" class="footer__col-link">Root-to-Rise Model</a></li>
              <li><a href="{root}about.html#team" class="footer__col-link">Leadership</a></li>
              <li><a href="{root}transparency.html" class="footer__col-link">Governance</a></li>
            </ul>
          </div>
          <div>
            <div class="footer__col-title">Programs</div>
            <ul class="footer__col-links" role="list">
              <li><a href="{root}programs/holistic-learning.html" class="footer__col-link">Holistic Learning</a></li>
              <li><a href="{root}programs/womens-equity.html" class="footer__col-link">Women's Equity</a></li>
              <li><a href="{root}programs/resilient-communities.html" class="footer__col-link">Resilient Communities</a></li>
              <li><a href="{root}programs/inclusive-wellness.html" class="footer__col-link">Inclusive Wellness</a></li>
              <li><a href="{root}programs/climate-resilience.html" class="footer__col-link">Climate Resilience</a></li>
              <li><a href="{root}programs/eco-conservation.html" class="footer__col-link">Eco-Conservation</a></li>
            </ul>
          </div>
          <div>
            <div class="footer__col-title">Get Involved</div>
            <ul class="footer__col-links" role="list">
              <li><a href="{root}donate.html" class="footer__col-link">Donate</a></li>
              <li><a href="{root}volunteer.html" class="footer__col-link">Volunteer</a></li>
              <li><a href="{root}partner.html" class="footer__col-link">Partner With Us</a></li>
              <li><a href="{root}careers.html" class="footer__col-link">Work With Us</a></li>
              <li><a href="{root}contact.html" class="footer__col-link">Contact</a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="footer__bottom">
      <div class="container">
        <div class="footer__bottom-inner">
          <p class="footer__copy">© 2026 Ananth Sarth Seva Foundation. All rights reserved.</p>
          <nav class="footer__bottom-links" aria-label="Legal links">
            <a href="{root}privacy.html">Privacy Policy</a>
            <a href="{root}terms.html">Terms of Use</a>
            <a href="{root}transparency.html">Transparency</a>
          </nav>
        </div>
      </div>
    </div>
  </footer>'''

def page(title, description, content, active='', root='', og_image='hero/hero-visual.jpg', path=''):
    domain = '[CLIENT: PRODUCTION DOMAIN]'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Ananth Sarth Seva Foundation</title>
  <meta name="description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Ananth Sarth Seva Foundation">
  <meta property="og:title" content="{title} | Ananth Sarth Seva Foundation">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="https://{domain}/assets/images/{og_image}">
  <meta property="og:url" content="https://{domain}/{path}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="{root}assets/images/logo-icon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  {FONTS}
{css(root)}
</head>
<body>
  <a href="#main" class="skip-link">Skip to content</a>
  {header(root, active)}
  <main id="main">
{content}
  </main>
  {footer(root)}
  {scripts(root)}
  {sr_only()}
</body>
</html>'''


# ── Page content builders ────────────────────────────────────────────────────

def page_hero_html(root, title, subtitle, desc, img, img_alt, breadcrumb_label, eyebrow):
    return f'''    <section class="page-hero" aria-labelledby="page-hero-heading">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="{root}index.html">Home</a>
          <span class="sep" aria-hidden="true">/</span>
          <span aria-current="page">{breadcrumb_label}</span>
        </nav>
        <div class="page-hero__inner">
          <div class="page-hero__content">
            <span class="eyebrow" aria-hidden="true">{eyebrow}</span>
            <h1 class="page-hero__heading" id="page-hero-heading">{title}</h1>
            <p class="page-hero__desc">{desc}</p>
          </div>
          <div class="page-hero__image" aria-hidden="true">
            <img src="{root}{img}" alt="{img_alt}" width="560" height="380" loading="eager" decoding="async">
          </div>
        </div>
      </div>
    </section>'''


# ── ABOUT ───────────────────────────────────────────────────────────────────
def build_about():
    content = page_hero_html('', 'About Ananth Sarth Seva Foundation',
        '', 'A foundation born from friendship, guided by Seva — selfless service — and committed to building communities that are educated, healthy, self-reliant and free.',
        'assets/images/hero/hero-visual.jpg', 'Founders in conversation', 'About Us', 'Our Story')
    content += '''
    <section class="section" aria-labelledby="mission-heading" id="mission">
      <div class="container">
        <div class="reveal" style="max-width:800px; margin: 0 auto; text-align:center;">
          <span class="eyebrow" aria-hidden="true">Vision &amp; Mission</span>
          <h2 class="h2" id="mission-heading">We do not believe in temporary fixes.</h2>
          <div class="divider" style="margin-inline:auto;" aria-hidden="true"></div>
          <p class="lead" style="margin-inline:auto;">We help communities grow from strong roots into self-reliant ecosystems — combining cultural wisdom, modern technology and local leadership.</p>
        </div>
      </div>
    </section>

    <section class="section section--tinted" aria-labelledby="values-heading">
      <div class="container">
        <header class="section-header section-header--center reveal">
          <span class="eyebrow" aria-hidden="true">Our Values</span>
          <h2 class="h2" id="values-heading">The principles that guide everything.</h2>
          <div class="divider" aria-hidden="true"></div>
        </header>
        <div class="about-values" data-stagger>
          <div class="value-card reveal"><div class="value-card__icon" aria-hidden="true">🙏</div><h3 class="value-card__name">Seva</h3><p class="value-card__desc">Selfless service as the foundation of everything we do — not charity, but dignity and partnership.</p></div>
          <div class="value-card reveal"><div class="value-card__icon" aria-hidden="true">🌿</div><h3 class="value-card__name">Interconnectedness</h3><p class="value-card__desc">All life is connected. Our programs reflect this — addressing education, health, economy and environment together.</p></div>
          <div class="value-card reveal"><div class="value-card__icon" aria-hidden="true">🌱</div><h3 class="value-card__name">Sustainability</h3><p class="value-card__desc">Programs designed for long-term self-reliance — not short-term intervention cycles that leave communities dependent.</p></div>
          <div class="value-card reveal"><div class="value-card__icon" aria-hidden="true">🏛️</div><h3 class="value-card__name">Community Ownership</h3><p class="value-card__desc">Success is when local leaders, not our team, are running the programs they once needed help to start.</p></div>
          <div class="value-card reveal"><div class="value-card__icon" aria-hidden="true">⚖️</div><h3 class="value-card__name">Dignity</h3><p class="value-card__desc">We refuse to reduce people to problems to be solved. Every community carries its own intelligence and strength.</p></div>
          <div class="value-card reveal"><div class="value-card__icon" aria-hidden="true">💡</div><h3 class="value-card__name">Innovation</h3><p class="value-card__desc">Ancient wisdom and modern technology are not opposites — they are partners in building lasting community resilience.</p></div>
        </div>
      </div>
    </section>

    <section class="section section--dark" id="team" aria-labelledby="team-heading">
      <div class="container">
        <header class="section-header section-header--center reveal">
          <span class="eyebrow" aria-hidden="true">The Team</span>
          <h2 class="h2" id="team-heading" style="color:var(--white);">Different expertise. One shared purpose.</h2>
          <div class="divider" style="margin-inline:auto;" aria-hidden="true"></div>
          <p class="lead" style="margin-inline:auto;">The founding team brings together professionals across technology, social research, environmental science, business, healthcare and education.</p>
        </header>
        <div class="team-grid" data-stagger style="--team-note: block;">
          <div class="team-card reveal"><div class="team-card__photo" aria-hidden="true">👤</div><div class="team-card__body"><div class="team-card__name">[Founder Name]</div><div class="team-card__role">Founder &amp; Director</div><span class="team-card__expertise">Technology &amp; Innovation</span></div></div>
          <div class="team-card reveal"><div class="team-card__photo" aria-hidden="true">👤</div><div class="team-card__body"><div class="team-card__name">[Co-founder]</div><div class="team-card__role">Co-founder</div><span class="team-card__expertise">Social &amp; Cultural Research</span></div></div>
          <div class="team-card reveal"><div class="team-card__photo" aria-hidden="true">👤</div><div class="team-card__body"><div class="team-card__name">[Team Member]</div><div class="team-card__role">Program Lead</div><span class="team-card__expertise">Environmental Science</span></div></div>
          <div class="team-card reveal"><div class="team-card__photo" aria-hidden="true">👤</div><div class="team-card__body"><div class="team-card__name">[Team Member]</div><div class="team-card__role">Operations</div><span class="team-card__expertise">Healthcare &amp; Wellness</span></div></div>
        </div>
        <p style="text-align:center; margin-top:var(--s5); font:400 var(--text-sm)/1 var(--font-body); color:rgba(255,255,255,.5); font-style:italic;">Team details will be updated as the foundation grows.</p>
      </div>
    </section>

    <section class="section" aria-label="Call to action">
      <div class="container" style="text-align:center; max-width:640px; margin-inline:auto;">
        <h2 class="h3 reveal">Ready to be part of the movement?</h2>
        <p class="lead reveal" style="margin-block:var(--s3) var(--s5); margin-inline:auto;">Whether you contribute time, expertise or resources — every form of Seva matters.</p>
        <div class="btn-group reveal" style="justify-content:center;">
          <a href="volunteer.html" class="btn btn--primary">Join the Seva Network</a>
          <a href="contact.html" class="btn btn--secondary">Get in Touch</a>
        </div>
      </div>
    </section>'''
    return page('About Us', 'Learn about Ananth Sarth Seva Foundation — our origin, values, team and the mission that guides everything we do.', content, 'About Us', '', 'hero/hero-visual.jpg', 'about.html')


# ── ROOT-TO-RISE ─────────────────────────────────────────────────────────────
def build_root_to_rise():
    steps = [
        ('01', 'Listen &amp; Learn', 'Immerse in communities to understand traditions, local strengths, natural resources, challenges and existing indigenous knowledge.', 'Before any program is designed, our team spends time in communities — listening, observing and learning from people who have lived in these landscapes for generations. We study what is working, what local knowledge already exists, and what communities themselves say they need.', '"Begin with the community, not with an external assumption."'),
        ('02', 'Bridge &amp; Blend', 'Combine ancient knowledge, traditional practices, digital skills, modern healthcare, clean energy and contemporary market access.', 'The second phase is about building bridges — between traditional wisdom and modern capability. We do not ask communities to abandon their culture in exchange for opportunity. We work to preserve identity while creating pathways to education, health, livelihood and environmental stewardship.', '"Preserve identity while creating future-ready opportunity."'),
        ('03', 'Digitalise &amp; Scale', 'Use digital marketplaces, cloud platforms, telemedicine, data tracking, smart technology and real-time impact measurement.', 'Once foundational programs are running locally, we introduce technology to extend their reach and scale their impact. Digital marketplaces connect artisans and farmers to wider markets. Telemedicine brings specialists to remote clinics. Data platforms track outcomes and ensure accountability.', '"Connect local innovation with wider opportunity."'),
        ('04', 'Transfer Ownership', 'Build local leadership councils, women-led committees, community governance, operational capability and financial sustainability.', 'The final and most important phase is transition. From the very beginning, every program is designed to become community-owned. We build governance structures, train local leaders, establish women-led committees and create financial models that communities can sustain independently.', '"Success means the community no longer depends on daily external support."'),
    ]
    steps_html = ''
    for num, title, subtitle, desc, core in steps:
        steps_html += f'''      <div class="rtr-page-step reveal">
        <div class="rtr-page-step__num" aria-hidden="true">{num}</div>
        <div class="rtr-page-step__body">
          <div class="rtr-page-step__label">Step {num}</div>
          <h2 class="rtr-page-step__title">{title}</h2>
          <p style="font:500 var(--text-base)/1.5 var(--font-body); color:var(--muted); margin-bottom:var(--s2);">{subtitle}</p>
          <p class="rtr-page-step__desc">{desc}</p>
          <div class="rtr-page-step__core">{core}</div>
        </div>
      </div>\n'''

    content = page_hero_html('', 'The Root-to-Rise Model', '', 'A four-phase methodology for building communities that are genuinely self-reliant — combining indigenous wisdom, modern technology and local ownership.',
        'assets/images/hero/hero-visual.jpg', 'Community members in discussion', 'Root-to-Rise', 'Our Methodology')
    content += f'''
    <section class="section section--tinted" aria-label="Model introduction">
      <div class="container">
        <div class="reveal" style="max-width:720px; margin:0 auto; text-align:center;">
          <span class="eyebrow" aria-hidden="true">The Foundation</span>
          <h2 class="h2">From local roots to lasting ownership.</h2>
          <div class="divider" style="margin-inline:auto;" aria-hidden="true"></div>
          <p class="lead" style="margin-inline:auto;">We do not believe in temporary fixes. Every program we design follows this four-phase model — ensuring that communities move from participants to leaders to owners.</p>
        </div>
      </div>
    </section>
    <section class="section" aria-labelledby="rtr-steps-heading">
      <div class="container">
        <h2 class="h3 reveal" id="rtr-steps-heading" style="margin-bottom:var(--s6);">Four phases. One continuous journey.</h2>
{steps_html}
      </div>
    </section>
    <section class="section section--dark" aria-label="Root-to-rise CTA">
      <div class="container" style="text-align:center; max-width:640px; margin-inline:auto;">
        <h2 class="h3 reveal" style="color:var(--white);">Want to support this model in action?</h2>
        <p class="lead reveal" style="margin-block:var(--s3) var(--s5); margin-inline:auto;">Partner with us, volunteer your expertise or contribute to specific programs.</p>
        <div class="btn-group reveal" style="justify-content:center;">
          <a href="programs/index.html" class="btn btn--primary">Explore Programs</a>
          <a href="partner.html" class="btn btn--ghost">Partner With Us</a>
        </div>
      </div>
    </section>'''
    return page('Root-to-Rise Model', 'The Root-to-Rise model is a four-phase approach to building self-reliant communities through listening, bridging, scaling and transferring ownership.', content, 'Root-to-Rise', '', 'hero/hero-visual.jpg', 'root-to-rise.html')


# ── PROGRAMS OVERVIEW ─────────────────────────────────────────────────────────
def build_programs_index():
    programs = [
        ('holistic-learning.html', 'Holistic Learning', 'assets/images/programs/holistic-learning.jpg', 'Learners in an inclusive classroom', 'Making quality education, digital skills, AI, robotics and lifelong learning accessible to underserved communities.'),
        ('womens-equity.html', "Women's Equity", 'assets/images/programs/womens-equity.jpg', 'Women entrepreneurs', 'Supporting women through healthcare, safety, financial literacy, livelihood opportunities and community leadership.'),
        ('resilient-communities.html', 'Resilient Communities', 'assets/images/programs/resilient-communities.jpg', 'A connected village', 'Combining cultural preservation, smart-village infrastructure, rural innovation and sustainable livelihoods.'),
        ('inclusive-wellness.html', 'Inclusive Wellness', 'assets/images/programs/inclusive-wellness.jpg', 'Healthcare access', 'Bringing mobile healthcare, telemedicine, nutrition, mental health support and integrative wellness to underserved regions.'),
        ('climate-resilience.html', 'Climate Resilience', 'assets/images/programs/climate-resilience.jpg', 'Clean energy', 'Helping communities prepare for climate risks through clean energy, early-warning systems and resilient infrastructure.'),
        ('eco-conservation.html', 'Eco-Conservation', 'assets/images/programs/eco-conservation.jpg', 'Community conservation', 'Empowering communities to protect forests, water, biodiversity, wildlife and natural ecosystems.'),
    ]
    cards = ''
    for href, name, img, img_alt, desc in programs:
        cards += f'''          <a href="{href}" class="prog-overview-card reveal">
            <div class="prog-overview-card__image"><img src="../{img}" alt="{img_alt}" width="400" height="300" loading="lazy"></div>
            <div class="prog-overview-card__body">
              <h3 class="prog-overview-card__name">{name}</h3>
              <p class="prog-overview-card__desc">{desc}</p>
              <span class="pillar-card__link" aria-hidden="true">Explore Program →</span>
            </div>
          </a>\n'''

    content = page_hero_html('../', 'Our Six Programs', '', 'Six interlocking programs addressing education, equity, health, community resilience, climate and conservation — designed to strengthen each other.',
        'assets/images/hero/hero-visual.jpg', 'Community members', 'Programs', 'Six Pillars')
    content += f'''
    <section class="section section--tinted" aria-labelledby="programs-overview-heading">
      <div class="container">
        <header class="section-header section-header--center reveal">
          <span class="eyebrow" aria-hidden="true">All Programs</span>
          <h2 class="h2" id="programs-overview-heading">Six pillars. One connected ecosystem.</h2>
          <div class="divider" aria-hidden="true"></div>
          <p class="lead" style="margin-inline:auto;">Improving one part of a community strengthens every other part.</p>
        </header>
        <div class="programs-overview-grid" data-stagger>
{cards}        </div>
      </div>
    </section>
    <section class="section section--dark" aria-label="Programs CTA">
      <div class="container" style="text-align:center; max-width:640px; margin-inline:auto;">
        <h2 class="h3 reveal" style="color:var(--white);">Interested in supporting a specific program?</h2>
        <div class="btn-group reveal" style="justify-content:center; margin-top:var(--s4);">
          <a href="../donate.html" class="btn btn--primary">Donate to a Program</a>
          <a href="../partner.html" class="btn btn--ghost">Become a Program Partner</a>
        </div>
      </div>
    </section>'''
    return page('Our Programs', "Explore the six interlocking programs of Ananth Sarth Seva Foundation across education, women's equity, resilient communities, wellness, climate and conservation.", content, 'Our Programs', '../', 'hero/hero-visual.jpg', 'programs/index.html')


# ── PROGRAMME PAGE BUILDER ───────────────────────────────────────────────────
def build_program(slug, name, desc, img, img_alt, challenge, objectives, interventions, pillar_accent, icon, og_desc):
    root = '../'
    objs_html = ''
    for i, obj in enumerate(objectives, 1):
        objs_html += f'''          <div class="prog-objective reveal">
            <div class="prog-objective__num" aria-hidden="true">{i:02d}</div>
            <p class="prog-objective__text">{obj}</p>
          </div>\n'''
    ints_html = ''
    for emoji, text in interventions:
        ints_html += f'          <div class="intervention-item"><span class="intervention-item__icon" aria-hidden="true">{emoji}</span><p class="intervention-item__text">{text}</p></div>\n'

    content = page_hero_html(root, name, '', og_desc, f'assets/images/programs/{slug}.jpg', img_alt, name, 'Program')
    content += f'''
    <section class="section" aria-labelledby="prog-challenge-heading">
      <div class="container">
        <div class="prog-challenge reveal">
          <div class="prog-challenge__label">The Challenge</div>
          <p class="prog-challenge__text" id="prog-challenge-heading">{challenge}</p>
        </div>

        <div style="margin-bottom:var(--s6);" class="reveal">
          <span class="eyebrow" aria-hidden="true">Program Objectives</span>
          <h2 class="h3" style="margin-bottom:var(--s4);">What this program aims to achieve</h2>
          <div class="prog-objectives" data-stagger>
{objs_html}          </div>
        </div>

        <div class="reveal">
          <span class="eyebrow" aria-hidden="true">Key Interventions</span>
          <h2 class="h3" style="margin-bottom:var(--s3);">Proposed initiatives &amp; activities</h2>
          <p style="font:400 var(--text-sm)/1.4 var(--font-body); color:var(--muted); margin-bottom:var(--s3); font-style:italic;">The following are proposed program interventions. Implementation timelines and specific activities will be confirmed as programs become operational.</p>
          <div class="interventions-grid" data-stagger>
{ints_html}          </div>
        </div>
      </div>
    </section>

    <section class="section section--tinted" aria-labelledby="prog-ownership-heading">
      <div class="container">
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:var(--s7); align-items:start;">
          <div class="reveal">
            <span class="eyebrow" aria-hidden="true">Community Ownership</span>
            <h2 class="h3" id="prog-ownership-heading">Designed to be led by communities.</h2>
            <div class="divider" aria-hidden="true"></div>
            <p style="font:400 var(--text-base)/1.7 var(--font-body); color:var(--muted);">Every intervention in this program is designed with a clear pathway to community ownership. We work to build local capacity, train community leaders, and establish governance structures so that programs can operate independently over time.</p>
          </div>
          <div class="reveal">
            <span class="eyebrow" aria-hidden="true">Measurement</span>
            <h2 class="h3">How we will track progress.</h2>
            <div class="divider" aria-hidden="true"></div>
            <p style="font:400 var(--text-base)/1.7 var(--font-body); color:var(--muted); margin-bottom:var(--s2);">Impact metrics will be defined, tracked and independently verified. Verified figures will be published on the <a href="../impact.html">Impact</a> and <a href="../transparency.html">Transparency</a> pages as programs become operational.</p>
            <p style="font:400 var(--text-sm)/1.5 var(--font-body); color:var(--muted); font-style:italic;">All outcomes described on this page are intended targets — not completed achievements.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--dark" aria-label="Program CTA">
      <div class="container" style="text-align:center; max-width:640px; margin-inline:auto;">
        <h2 class="h3 reveal" style="color:var(--white);">Support the {name} program.</h2>
        <p class="lead reveal" style="margin-block:var(--s3) var(--s5); margin-inline:auto;">Your contribution helps build the foundation's capability to design and launch programs with communities.</p>
        <div class="btn-group reveal" style="justify-content:center;">
          <a href="../donate.html" class="btn btn--primary">Donate to This Program</a>
          <a href="../partner.html" class="btn btn--ghost">Become a Program Partner</a>
        </div>
      </div>
    </section>'''
    return page(name, og_desc, content, 'Our Programs', root, f'programs/{slug}.jpg', f'programs/{slug}.html')


# ── CONTACT ──────────────────────────────────────────────────────────────────
def build_contact():
    content = page_hero_html('', 'Let\'s Build a Better World Together', '', 'Whether you are a donor, volunteer, partner, researcher, community representative or simply curious — we welcome your enquiry.',
        'assets/images/hero/hero-visual.jpg', 'Community collaboration', 'Contact', 'Reach Out')
    content += '''
    <section class="section" aria-labelledby="contact-form-heading">
      <div class="container">
        <div class="contact-grid">
          <div>
            <span class="eyebrow" aria-hidden="true">Send an Enquiry</span>
            <h2 class="h3 reveal" id="contact-form-heading" style="margin-bottom:var(--s4);">We would love to hear from you.</h2>
            <form action="#" method="post" aria-label="Contact form" class="reveal">
              <div class="form-row">
                <div class="form-group">
                  <label for="contact-name">Full Name <span aria-hidden="true">*</span></label>
                  <input type="text" id="contact-name" name="name" class="form-control" placeholder="Your full name" required autocomplete="name">
                </div>
                <div class="form-group">
                  <label for="contact-email">Email Address <span aria-hidden="true">*</span></label>
                  <input type="email" id="contact-email" name="email" class="form-control" placeholder="you@example.com" required autocomplete="email">
                </div>
              </div>
              <div class="form-row">
                <div class="form-group">
                  <label for="contact-phone">Phone Number</label>
                  <input type="tel" id="contact-phone" name="phone" class="form-control" placeholder="+91 00000 00000" autocomplete="tel">
                </div>
                <div class="form-group">
                  <label for="contact-org">Organisation</label>
                  <input type="text" id="contact-org" name="organisation" class="form-control" placeholder="Your organisation (if applicable)">
                </div>
              </div>
              <div class="form-group">
                <label for="contact-purpose">Purpose of Enquiry <span aria-hidden="true">*</span></label>
                <select id="contact-purpose" name="purpose" class="form-control" required>
                  <option value="" disabled selected>Please select…</option>
                  <option value="donor">Potential Donor</option>
                  <option value="csr">Corporate / CSR Partner</option>
                  <option value="volunteer">Volunteer</option>
                  <option value="career">Job Applicant</option>
                  <option value="tech">Technology Collaborator</option>
                  <option value="health">Healthcare Partner</option>
                  <option value="research">Research Institution</option>
                  <option value="media">Media</option>
                  <option value="community">Community Representative</option>
                  <option value="other">Other</option>
                </select>
              </div>
              <div class="form-group">
                <label for="contact-message">Message <span aria-hidden="true">*</span></label>
                <textarea id="contact-message" name="message" class="form-control" placeholder="Please describe how we can help or how you'd like to collaborate…" required></textarea>
              </div>
              <div class="form-group">
                <label style="display:flex; gap:10px; align-items:flex-start; cursor:pointer; font-weight:400;">
                  <input type="checkbox" name="consent" required style="margin-top:3px; flex-shrink:0; accent-color:var(--heritage-blue);">
                  <span style="font:400 var(--text-sm)/1.5 var(--font-body); color:var(--muted);">I consent to Ananth Sarth Seva Foundation contacting me regarding my enquiry. Your information will be handled in accordance with our <a href="privacy.html">Privacy Policy</a>.</span>
                </label>
              </div>
              <button type="submit" class="btn btn--primary" style="min-width:180px;">Send Enquiry</button>
            </form>
          </div>

          <div>
            <div class="contact-info reveal">
              <div class="contact-info__block">
                <h3>Contact Information</h3>
                <div class="contact-info__item"><span aria-hidden="true">📧</span><span>[CLIENT: OFFICIAL EMAIL]</span></div>
                <div class="contact-info__item"><span aria-hidden="true">📞</span><span>[CLIENT: PHONE NUMBER]</span></div>
                <div class="contact-info__item"><span aria-hidden="true">📍</span><span>[CLIENT: REGISTERED OFFICE ADDRESS]</span></div>
                <div class="contact-info__item"><span aria-hidden="true">🕐</span><span>Monday – Friday, 9:00 am – 6:00 pm IST</span></div>
              </div>
              <div class="contact-info__block">
                <h4>Your enquiry is treated confidentially.</h4>
                <p style="font:400 var(--text-sm)/1.6 var(--font-body); color:var(--muted);">We do not share your details with third parties without your consent. All information provided is used solely to respond to your enquiry.</p>
              </div>
              <div class="contact-info__block">
                <h4>Other ways to connect</h4>
                <div class="contact-info__item"><span aria-hidden="true">💼</span><a href="careers.html">Explore career opportunities</a></div>
                <div class="contact-info__item"><span aria-hidden="true">🤝</span><a href="partner.html">Partnership enquiries</a></div>
                <div class="contact-info__item"><span aria-hidden="true">🙏</span><a href="volunteer.html">Join the Seva Network</a></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>'''
    return page('Contact Us', 'Get in touch with Ananth Sarth Seva Foundation. Whether you want to donate, volunteer, partner or collaborate — we welcome your enquiry.', content, 'Contact', '', 'hero/hero-visual.jpg', 'contact.html')


# ── DONATE ───────────────────────────────────────────────────────────────────
def build_donate():
    content = page_hero_html('', 'Support the Mission', '', 'Every contribution helps build programs that create lasting change — not temporary relief.',
        'assets/images/hero/hero-visual.jpg', 'Community impact', 'Donate', 'Contribute')
    content += '''
    <section class="section" aria-labelledby="donate-form-heading">
      <div class="container">
        <div class="donate-grid">
          <div>
            <span class="eyebrow" aria-hidden="true">Make a Contribution</span>
            <h2 class="h3 reveal" id="donate-form-heading" style="margin-bottom:var(--s4);">Choose how you would like to contribute.</h2>
            <form action="#" method="post" aria-label="Donation form" class="reveal">
              <div class="form-group">
                <label>Select an amount</label>
                <div class="amount-selector" role="group" aria-label="Preset amounts">
                  <button type="button" class="amount-btn is-active" data-amount="500">₹500</button>
                  <button type="button" class="amount-btn" data-amount="1000">₹1,000</button>
                  <button type="button" class="amount-btn" data-amount="2500">₹2,500</button>
                  <button type="button" class="amount-btn" data-amount="5000">₹5,000</button>
                </div>
                <label for="custom-amount" style="margin-top:var(--s2); display:block; font-weight:400; color:var(--muted);">Or enter a custom amount</label>
                <input type="number" id="custom-amount" name="custom_amount" class="form-control" placeholder="Enter amount in ₹" min="1" style="max-width:280px;">
              </div>
              <div class="form-group">
                <label>Select a program (optional)</label>
                <div class="pillar-selector" role="group" aria-label="Program selection">
                  <button type="button" class="pillar-btn is-active" data-pillar="where-needed">💛 Where Most Needed</button>
                  <button type="button" class="pillar-btn" data-pillar="learning">📚 Holistic Learning</button>
                  <button type="button" class="pillar-btn" data-pillar="women">🌸 Women\'s Equity</button>
                  <button type="button" class="pillar-btn" data-pillar="communities">🏡 Resilient Communities</button>
                  <button type="button" class="pillar-btn" data-pillar="wellness">🏥 Inclusive Wellness</button>
                  <button type="button" class="pillar-btn" data-pillar="climate">☀️ Climate Resilience</button>
                  <button type="button" class="pillar-btn" data-pillar="eco">🌿 Eco-Conservation</button>
                </div>
              </div>
              <div class="form-row">
                <div class="form-group">
                  <label for="donor-name">Full Name <span aria-hidden="true">*</span></label>
                  <input type="text" id="donor-name" name="name" class="form-control" required autocomplete="name">
                </div>
                <div class="form-group">
                  <label for="donor-email">Email Address <span aria-hidden="true">*</span></label>
                  <input type="email" id="donor-email" name="email" class="form-control" required autocomplete="email">
                </div>
              </div>
              <div class="form-group">
                <label style="display:flex; gap:10px; align-items:flex-start; cursor:pointer; font-weight:400;">
                  <input type="checkbox" name="consent" required style="margin-top:3px; flex-shrink:0; accent-color:var(--heritage-blue);">
                  <span style="font:400 var(--text-sm)/1.5 var(--font-body); color:var(--muted);">I consent to Ananth Sarth Seva Foundation processing my donation and contacting me with a receipt and updates. See our <a href="privacy.html">Privacy Policy</a>.</span>
                </label>
              </div>
              <button type="submit" class="btn btn--primary" style="min-width:200px;">Proceed to Payment</button>
            </form>
          </div>
          <div class="donate-sidebar reveal">
            <h3>Your contribution matters.</h3>
            <p style="font:400 var(--text-sm)/1.6 var(--font-body); color:rgba(255,255,255,.7); margin-bottom:var(--s4);">Your contribution will be allocated according to the selected program and the foundation\'s approved governance process.</p>
            <div class="donate-assurance"><span class="donate-assurance__icon" aria-hidden="true">🔒</span><p class="donate-assurance__text">Secure payment processing. Your financial information is never stored on our servers.</p></div>
            <div class="donate-assurance"><span class="donate-assurance__icon" aria-hidden="true">📊</span><p class="donate-assurance__text">Impact reports will be published on our Transparency page as programs become operational.</p></div>
            <div class="donate-assurance"><span class="donate-assurance__icon" aria-hidden="true">📧</span><p class="donate-assurance__text">You will receive a confirmation email and receipt following your contribution.</p></div>
            <hr style="border:none; border-top:1px solid rgba(255,255,255,.15); margin-block:var(--s4);">
            <p style="font:400 var(--text-xs)/1.5 var(--font-body); color:rgba(255,255,255,.45); font-style:italic;">Tax benefit eligibility will be communicated once the foundation\'s legal and regulatory status is fully established. Please do not assume deductibility at this stage.</p>
          </div>
        </div>
      </div>
    </section>'''
    return page('Donate — Support the Mission', 'Support Ananth Sarth Seva Foundation\'s programs across education, women\'s equity, healthcare, community resilience, climate action and conservation.', content, '', '', 'hero/hero-visual.jpg', 'donate.html')


# ── VOLUNTEER ─────────────────────────────────────────────────────────────────
def build_volunteer():
    categories = [
        ('📚', 'Education Mentor', 'Support learning initiatives, reading rooms, digital labs and vocational training programs.'),
        ('💻', 'Digital Skills Trainer', 'Teach digital literacy, AI tools, e-commerce and technology skills to communities.'),
        ('🏥', 'Healthcare Professional', 'Contribute to mobile health camps, telemedicine support and health awareness programs.'),
        ('🧠', 'Mental Health Professional', 'Support counselling services, addiction recovery and community wellbeing programs.'),
        ('🌿', 'Environmental Volunteer', 'Participate in conservation, plantation, water restoration and eco-monitoring activities.'),
        ('🔬', 'Researcher', 'Contribute to knowledge generation, impact measurement and program evaluation.'),
        ('✍️', 'Content & Communication', 'Help shape the foundation\'s storytelling, reports, social media and community content.'),
        ('⚙️', 'Technology Volunteer', 'Build platforms, apps, data tools and digital infrastructure for foundation programs.'),
        ('⚖️', 'Legal / Governance', 'Contribute legal, compliance or governance expertise to strengthen the foundation\'s operations.'),
        ('📣', 'Fundraising Volunteer', 'Help mobilise support, organise events and build donor relationships.'),
        ('🏢', 'Corporate Volunteering', 'Bring your team for structured volunteering experiences aligned to your CSR goals.'),
        ('🗺️', 'Field Coordinator', 'Support ground-level program implementation and community engagement in target regions.'),
    ]
    cards = ''
    for icon, name, desc in categories:
        cards += f'          <div class="vol-card reveal"><div class="vol-card__icon" aria-hidden="true">{icon}</div><h3 class="vol-card__name">{name}</h3><p class="vol-card__desc">{desc}</p></div>\n'

    content = page_hero_html('', 'Join the Seva Network', '', 'Volunteering with Ananth Sarth Seva Foundation is not limited to fieldwork. We welcome time, expertise, research and passion from every discipline.',
        'assets/images/hero/hero-visual.jpg', 'Volunteers at work', 'Volunteer', 'Seva Network')
    content += f'''
    <section class="section section--tinted" aria-labelledby="vol-categories-heading">
      <div class="container">
        <header class="section-header section-header--center reveal">
          <span class="eyebrow" aria-hidden="true">How to Contribute</span>
          <h2 class="h2" id="vol-categories-heading">The power of selfless service.</h2>
          <div class="divider" aria-hidden="true"></div>
          <p class="lead" style="margin-inline:auto;">Every skill matters. Choose the role that matches your expertise and availability.</p>
        </header>
        <div class="volunteer-categories" data-stagger>
{cards}        </div>
      </div>
    </section>

    <section class="section section--white" aria-labelledby="vol-form-heading">
      <div class="container" style="max-width:780px;">
        <span class="eyebrow reveal" aria-hidden="true">Apply Now</span>
        <h2 class="h3 reveal" id="vol-form-heading" style="margin-bottom:var(--s4);">Express your interest.</h2>
        <form action="#" method="post" aria-label="Volunteer application form" class="reveal">
          <div class="form-row">
            <div class="form-group"><label for="vol-name">Full Name <span aria-hidden="true">*</span></label><input type="text" id="vol-name" name="name" class="form-control" required autocomplete="name"></div>
            <div class="form-group"><label for="vol-email">Email Address <span aria-hidden="true">*</span></label><input type="email" id="vol-email" name="email" class="form-control" required autocomplete="email"></div>
          </div>
          <div class="form-row">
            <div class="form-group"><label for="vol-phone">Phone</label><input type="tel" id="vol-phone" name="phone" class="form-control" autocomplete="tel"></div>
            <div class="form-group"><label for="vol-city">City / Location</label><input type="text" id="vol-city" name="city" class="form-control"></div>
          </div>
          <div class="form-group"><label for="vol-role">Area of Expertise / Preferred Role <span aria-hidden="true">*</span></label><select id="vol-role" name="role" class="form-control" required><option value="" disabled selected>Please select…</option><option>Education Mentor</option><option>Digital Skills Trainer</option><option>Healthcare Professional</option><option>Mental Health Professional</option><option>Environmental Volunteer</option><option>Researcher</option><option>Content &amp; Communication</option><option>Technology Volunteer</option><option>Legal / Governance</option><option>Fundraising Volunteer</option><option>Corporate Volunteering Team</option><option>Field Coordinator</option><option>Other</option></select></div>
          <div class="form-group"><label for="vol-message">Tell us about yourself and your motivation</label><textarea id="vol-message" name="message" class="form-control"></textarea></div>
          <div class="form-group"><label style="display:flex; gap:10px; align-items:flex-start; cursor:pointer; font-weight:400;"><input type="checkbox" name="consent" required style="margin-top:3px; flex-shrink:0; accent-color:var(--heritage-blue);"><span style="font:400 var(--text-sm)/1.5 var(--font-body); color:var(--muted);">I consent to Ananth Sarth Seva Foundation contacting me regarding volunteering opportunities. See our <a href="privacy.html">Privacy Policy</a>. Eligible volunteers may receive recognition based on duration, contribution and the foundation\'s volunteer policy.</span></label></div>
          <button type="submit" class="btn btn--primary">Submit Application</button>
        </form>
      </div>
    </section>'''
    return page('Volunteer — Join the Seva Network', 'Join the Ananth Sarth Seva Foundation Seva Network. Contribute time, expertise or professional skills across education, health, technology, environment and more.', content, '', '', 'hero/hero-visual.jpg', 'volunteer.html')


# ── PARTNER ───────────────────────────────────────────────────────────────────
def build_partner():
    types = [
        ('💼', 'CSR Partnership', 'Align your corporate social responsibility mandate with measurable community programs across education, health, environment and livelihood.'),
        ('💻', 'Technology Partnership', 'Contribute platforms, tools, devices or technical expertise to scale digital programs in underserved communities.'),
        ('🏥', 'Healthcare Partnership', 'Partner with us to expand mobile health, telemedicine, nutrition and mental health programs.'),
        ('🎓', 'Research & Academic', 'Collaborate on knowledge generation, impact measurement, ethnographic research and policy development.'),
        ('🤝', 'Implementation Partnership', 'Work alongside our team to design, deliver and monitor programs on the ground.'),
        ('🏛️', 'Institutional Collaboration', 'Engage with us on policy alignment, government programs and institutional initiatives.'),
        ('📖', 'Knowledge Partnership', 'Share expertise, training resources, curriculum or professional knowledge with our programs.'),
        ('🔧', 'Equipment & Infrastructure', 'Contribute equipment, devices, materials or infrastructure that programs need to operate.'),
        ('⚖️', 'Pro-bono Professional Support', 'Offer legal, financial, governance, communication or strategic advisory services.'),
    ]
    cards = ''
    for icon, name, desc in types:
        cards += f'          <div class="partner-type-card reveal"><div class="partner-type-card__icon" aria-hidden="true">{icon}</div><h3 class="partner-type-card__name">{name}</h3><p class="partner-type-card__desc">{desc}</p></div>\n'

    content = page_hero_html('', 'Partner With Ananth Sarth Seva Foundation', '', 'Build meaningful, measurable partnerships that create lasting impact across education, equity, health, community, climate and conservation.',
        'assets/images/hero/hero-visual.jpg', 'Partners in discussion', 'Partner', 'Partnership')
    content += f'''
    <section class="section section--tinted" aria-labelledby="partner-types-heading">
      <div class="container">
        <header class="section-header section-header--center reveal">
          <span class="eyebrow" aria-hidden="true">Partnership Pathways</span>
          <h2 class="h2" id="partner-types-heading">Multiple ways to collaborate.</h2>
          <div class="divider" aria-hidden="true"></div>
          <p class="lead" style="margin-inline:auto;">We welcome partnerships that bring complementary expertise, resources and reach to our programs.</p>
        </header>
        <div class="partner-types" data-stagger>
{cards}        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="partner-why-heading">
      <div class="container" style="max-width:800px; margin-inline:auto;">
        <span class="eyebrow reveal" aria-hidden="true">Why Partner With Us</span>
        <h2 class="h3 reveal" id="partner-why-heading" style="margin-bottom:var(--s3);">What you can expect from a partnership.</h2>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:var(--s3); margin-bottom:var(--s6);" class="reveal">
          <div class="contact-info__block"><h4>Governance &amp; Reporting</h4><p style="font:400 var(--text-sm)/1.6 var(--font-body); color:var(--muted);">Defined objectives, agreed metrics, documented governance and regular reporting on progress.</p></div>
          <div class="contact-info__block"><h4>Outcome Measurement</h4><p style="font:400 var(--text-sm)/1.6 var(--font-body); color:var(--muted);">Programs designed with measurable intended outcomes and independent verification pathways.</p></div>
          <div class="contact-info__block"><h4>Pilot-First Approach</h4><p style="font:400 var(--text-sm)/1.6 var(--font-body); color:var(--muted);">We are open to scoped pilots that allow both parties to assess fit, impact and partnership potential before scaling.</p></div>
          <div class="contact-info__block"><h4>Community Involvement</h4><p style="font:400 var(--text-sm)/1.6 var(--font-body); color:var(--muted);">All programs involve community participation. Partners are welcome to observe and engage with communities directly.</p></div>
        </div>
        <div style="text-align:center;">
          <a href="contact.html" class="btn btn--primary">Start a Partnership Conversation</a>
        </div>
      </div>
    </section>'''
    return page('Partner With Us', 'Explore partnership pathways with Ananth Sarth Seva Foundation across CSR, technology, healthcare, research, implementation and institutional collaboration.', content, '', '', 'hero/hero-visual.jpg', 'partner.html')


# ── IMPACT ────────────────────────────────────────────────────────────────────
def build_impact():
    categories = [
        ('📚', 'Holistic Learning', [('Learners enrolled in programs', 'planned'), ('Digital skills trainees', 'planned'), ('Vocational training graduates', 'planned'), ('Rural learning hubs established', 'planned')]),
        ('🌸', "Women's Equity", [('Women trained in livelihood skills', 'planned'), ('SHGs and cooperatives supported', 'planned'), ('Micro-enterprises established', 'planned'), ('Women in community leadership roles', 'planned')]),
        ('🏡', 'Resilient Communities', [('Livelihoods created', 'planned'), ('Communities covered', 'planned'), ('Local enterprises supported', 'planned'), ('Cultural heritage initiatives', 'planned')]),
        ('🏥', 'Inclusive Wellness', [('Health consultations completed', 'planned'), ('Mental health sessions provided', 'planned'), ('Health camps organised', 'planned'), ('Local health ambassadors trained', 'planned')]),
        ('☀️', 'Climate Resilience', [('Clean energy capacity deployed', 'planned'), ('Climate-ready communities', 'planned'), ('Environmental volunteers trained', 'planned'), ('Early-warning systems deployed', 'planned')]),
        ('🌿', 'Eco-Conservation', [('Hectares under community protection', 'planned'), ('Trees planted / habitats restored', 'planned'), ('Water bodies restored', 'planned'), ('Youth Green Brigade members', 'planned')]),
    ]
    cats_html = ''
    for icon, name, metrics in categories:
        metric_rows = ''
        for label, status in metrics:
            status_label = {'planned': 'Planned', 'progress': 'In Progress', 'completed': 'Completed'}.get(status, 'Planned')
            metric_rows += f'<div class="impact-metric"><span class="impact-metric__label">{label}</span><span class="impact-metric__status metric-card__status--{status}">{status_label}</span></div>\n'
        cats_html += f'''        <div class="impact-category reveal">
          <div class="impact-category__pillar"><span aria-hidden="true">{icon}</span> {name}</div>
          <div class="impact-category__metrics">{metric_rows}</div>
        </div>\n'''

    content = page_hero_html('', 'Impact Framework', '', 'Because the foundation is newly initiated, we are establishing what we will measure — not fabricating what we have achieved.',
        'assets/images/hero/hero-visual.jpg', 'Impact measurement', 'Impact', 'Our Impact')
    content += f'''
    <section class="section section--tinted" aria-labelledby="impact-categories-heading">
      <div class="container">
        <header class="section-header section-header--center reveal">
          <span class="eyebrow" aria-hidden="true">Measurement Framework</span>
          <h2 class="h2" id="impact-categories-heading">Building impact that can be demonstrated.</h2>
          <div class="divider" aria-hidden="true"></div>
          <p class="lead" style="margin-inline:auto;">All metrics below are planned measurement categories. Verified figures will be published as programs become operational and independently documented.</p>
        </header>
        <div class="impact-categories" data-stagger>
{cats_html}        </div>
        <div class="impact-note reveal">
          <span class="impact-note__icon" aria-hidden="true">📊</span>
          <p class="impact-note__text">Verified impact figures will be published on this page as programs become operational and are independently documented. We are committed to transparent, evidence-based impact reporting.</p>
        </div>
      </div>
    </section>'''
    return page('Impact Framework', 'Ananth Sarth Seva Foundation impact framework — planned measurement categories across education, women\'s equity, healthcare, community, climate and conservation.', content, 'Impact', '', 'hero/hero-visual.jpg', 'impact.html')


# ── TRANSPARENCY ─────────────────────────────────────────────────────────────
def build_transparency():
    doc_sections = [
        ('Registration &amp; Legal', [('🏛️', 'Registration Certificate', 'Document will be published after formal registration is completed.'), ('🏛️', 'Trust Deed / Constitution', 'Document will be published after formal registration is completed.'), ('🏛️', 'PAN Certificate', 'Document will be published after formal registration is completed.')]),
        ('Governance', [('📋', 'Governance Structure', 'Document will be published after formal governance framework is finalised.'), ('📋', 'Board / Trustee Composition', 'Details will be published after formal governance is established.'), ('📋', 'Conflict of Interest Policy', 'Document will be published after policies are formally approved.')]),
        ('Financial Reports', [('📊', 'Annual Report 2026', 'Will be published after the first full financial year of operations.'), ('📊', 'Audited Financial Statements', 'Will be published after formal audit is completed.'), ('📊', 'Donation Utilisation Report', 'Will be published as programs become operational.')]),
        ('Policies', [('📄', 'Donation Policy', 'Document will be published after formal approval.'), ('📄', 'Volunteer Policy', 'Document will be published after formal approval.'), ('📄', 'Safeguarding Policy', 'Document will be published after formal approval.')]),
        ('Impact Reports', [('📈', 'Program Impact Reports', 'Will be published as programs become operational and impact is independently documented.'), ('📈', 'Partner Reports', 'Will be published in accordance with partnership agreements.'), ('📈', 'Community Feedback Reports', 'Will be published as community engagement programs begin.')]),
    ]
    sections_html = ''
    for section_name, docs in doc_sections:
        doc_cards = ''
        for icon, name, status in docs:
            doc_cards += f'<div class="doc-card"><span class="doc-card__icon" aria-hidden="true">{icon}</span><div><div class="doc-card__name">{name}</div><div class="doc-card__status">{status}</div></div></div>\n'
        sections_html += f'''        <div style="margin-bottom:var(--s6);" class="reveal">
          <h3 class="h4" style="margin-bottom:var(--s3);">{section_name}</h3>
          <div class="doc-grid">{doc_cards}</div>
        </div>\n'''

    content = page_hero_html('', 'Transparency &amp; Governance', '', 'We are committed to open, honest and accountable governance. This page will be updated as formal documentation is approved and programs become operational.',
        'assets/images/hero/hero-visual.jpg', 'Governance and transparency', 'Transparency', 'Governance')
    content += f'''
    <section class="section" aria-labelledby="transparency-docs-heading">
      <div class="container">
        <header class="section-header reveal" style="margin-bottom:var(--s7);">
          <span class="eyebrow" aria-hidden="true">Document Library</span>
          <h2 class="h2" id="transparency-docs-heading">Our commitment to openness.</h2>
          <div class="divider" aria-hidden="true"></div>
          <p class="lead">All governance, financial and policy documents will be published on this page as they are formally approved.</p>
        </header>
{sections_html}
        <div class="contact-info__block reveal" style="max-width:640px;">
          <h4>Questions about our governance?</h4>
          <p style="font:400 var(--text-sm)/1.6 var(--font-body); color:var(--muted);">If you have questions about our governance, finances or compliance, please reach out directly through our <a href="contact.html">Contact page</a>. We aim to respond to all governance enquiries within 5 business days.</p>
        </div>
      </div>
    </section>'''
    return page('Transparency & Governance', 'Ananth Sarth Seva Foundation governance, registration, policies and impact reports — committed to open and accountable operations.', content, 'Transparency', '', 'hero/hero-visual.jpg', 'transparency.html')


# ── CAREERS ───────────────────────────────────────────────────────────────────
def build_careers():
    values = [
        ('🌱', 'Purposeful Work', 'Every role contributes directly to community change.'),
        ('🔬', 'Multidisciplinary Environment', 'Work alongside technology, health, environment and social development professionals.'),
        ('🌿', 'Grounded in Seva', 'A culture of selfless service, respect and dignity in everything we do.'),
        ('🚀', 'Growth Opportunity', 'A young organisation where initiative, ideas and leadership are welcomed.'),
    ]
    val_html = ''.join(f'<div class="career-value reveal"><div class="career-value__icon" aria-hidden="true">{icon}</div><div class="career-value__name">{name}</div></div>' for icon, name, _ in values)

    content = page_hero_html('', 'Turn Professional Capability Into Meaningful Impact', '', 'Build a career that combines professional growth with social and environmental impact in a multidisciplinary, purpose-driven organisation.',
        'assets/images/hero/hero-visual.jpg', 'Team at work', 'Careers', 'Work With Us')
    content += f'''
    <section class="section section--tinted" aria-labelledby="careers-values-heading">
      <div class="container">
        <header class="section-header section-header--center reveal">
          <span class="eyebrow" aria-hidden="true">Why Join Us</span>
          <h2 class="h2" id="careers-values-heading">A career with meaning.</h2>
          <div class="divider" aria-hidden="true"></div>
        </header>
        <div class="careers-values" data-stagger>{val_html}</div>
      </div>
    </section>

    <section class="section" aria-labelledby="careers-openings-heading">
      <div class="container">
        <header class="section-header reveal">
          <span class="eyebrow" aria-hidden="true">Opportunities</span>
          <h2 class="h3" id="careers-openings-heading">Current openings, fellowships &amp; internships.</h2>
          <div class="divider" aria-hidden="true"></div>
        </header>
        <div class="contact-info__block reveal" style="margin-bottom:var(--s5);">
          <h4>No specific vacancies are listed at this time.</h4>
          <p style="font:400 var(--text-sm)/1.6 var(--font-body); color:var(--muted);">As a newly initiated foundation, we are building our team carefully. We welcome speculative applications from professionals aligned with our values across technology, social research, environmental science, healthcare, education, communication and operations. Submit an expression of interest below and we will reach out when relevant opportunities arise.</p>
        </div>
        <div style="max-width:780px;" class="reveal">
          <h3 class="h4" style="margin-bottom:var(--s3);">Submit an expression of interest</h3>
          <form action="#" method="post" aria-label="Career expression of interest form">
            <div class="form-row">
              <div class="form-group"><label for="career-name">Full Name <span aria-hidden="true">*</span></label><input type="text" id="career-name" name="name" class="form-control" required autocomplete="name"></div>
              <div class="form-group"><label for="career-email">Email <span aria-hidden="true">*</span></label><input type="email" id="career-email" name="email" class="form-control" required autocomplete="email"></div>
            </div>
            <div class="form-row">
              <div class="form-group"><label for="career-phone">Phone</label><input type="tel" id="career-phone" name="phone" class="form-control" autocomplete="tel"></div>
              <div class="form-group"><label for="career-city">City / Location</label><input type="text" id="career-city" name="city" class="form-control"></div>
            </div>
            <div class="form-group"><label for="career-expertise">Area of Expertise <span aria-hidden="true">*</span></label><input type="text" id="career-expertise" name="expertise" class="form-control" placeholder="e.g. Technology, Healthcare, Education…" required></div>
            <div class="form-group"><label for="career-engage">Preferred Engagement Type</label><select id="career-engage" name="engagement" class="form-control"><option value="">Please select…</option><option>Full-time employment</option><option>Part-time</option><option>Fellowship</option><option>Internship</option><option>Consultant</option><option>Pro-bono</option></select></div>
            <div class="form-group"><label for="career-statement">Short Statement of Purpose</label><textarea id="career-statement" name="statement" class="form-control" placeholder="Why do you want to work with Ananth Sarth Seva Foundation?"></textarea></div>
            <div class="form-group"><label style="display:flex; gap:10px; align-items:flex-start; cursor:pointer; font-weight:400;"><input type="checkbox" name="consent" required style="margin-top:3px; flex-shrink:0; accent-color:var(--heritage-blue);"><span style="font:400 var(--text-sm)/1.5 var(--font-body); color:var(--muted);">I consent to Ananth Sarth Seva Foundation retaining my details and contacting me regarding relevant opportunities. See our <a href="privacy.html">Privacy Policy</a>.</span></label></div>
            <button type="submit" class="btn btn--primary">Submit Expression of Interest</button>
          </form>
        </div>
      </div>
    </section>'''
    return page('Work With Us', 'Explore career, fellowship and internship opportunities with Ananth Sarth Seva Foundation — combining professional growth with social and environmental impact.', content, '', '', 'hero/hero-visual.jpg', 'careers.html')


# ── PRIVACY ───────────────────────────────────────────────────────────────────
def build_privacy():
    content = page_hero_html('', 'Privacy Policy', '', 'How Ananth Sarth Seva Foundation collects, uses and protects personal information.',
        'assets/images/hero/hero-visual.jpg', '', 'Privacy Policy', 'Legal')
    content += '''
    <section class="section" aria-label="Privacy policy content">
      <div class="container" style="max-width:780px;">
        <div class="reveal" style="font:400 var(--text-base)/1.8 var(--font-body); color:var(--muted);">
          <p style="margin-bottom:var(--s3);"><strong>Last updated: 2026</strong></p>
          <h2 class="h4" style="margin-bottom:var(--s2); color:var(--charcoal);">1. Information we collect</h2>
          <p style="margin-bottom:var(--s3);">We collect information you provide voluntarily — such as your name, email address, phone number and enquiry details — when you contact us, volunteer, donate or subscribe to our newsletter. We do not sell or share your personal information with third parties for marketing purposes.</p>
          <h2 class="h4" style="margin-bottom:var(--s2); color:var(--charcoal);">2. How we use your information</h2>
          <p style="margin-bottom:var(--s3);">Information is used to respond to your enquiry, process your contribution, send relevant foundation updates and improve our programs. We use cookieless analytics (Plausible) and do not track individual visitors.</p>
          <h2 class="h4" style="margin-bottom:var(--s2); color:var(--charcoal);">3. Data security</h2>
          <p style="margin-bottom:var(--s3);">We implement appropriate technical and organisational measures to protect your personal information. Our website is served over HTTPS. We do not store payment information on our servers.</p>
          <h2 class="h4" style="margin-bottom:var(--s2); color:var(--charcoal);">4. Your rights</h2>
          <p style="margin-bottom:var(--s3);">Under applicable law, including the Digital Personal Data Protection Act, you have the right to access, correct or request deletion of your personal data. To exercise these rights, contact us at [CLIENT: OFFICIAL EMAIL].</p>
          <h2 class="h4" style="margin-bottom:var(--s2); color:var(--charcoal);">5. Contact</h2>
          <p>For any privacy-related queries, please contact us through our <a href="contact.html">Contact page</a> or at [CLIENT: OFFICIAL EMAIL].</p>
        </div>
      </div>
    </section>'''
    return page('Privacy Policy', 'Ananth Sarth Seva Foundation privacy policy — how we collect, use and protect personal information.', content, '', '', 'hero/hero-visual.jpg', 'privacy.html')


# ── TERMS ─────────────────────────────────────────────────────────────────────
def build_terms():
    content = page_hero_html('', 'Terms of Use', '', 'Terms governing the use of the Ananth Sarth Seva Foundation website.',
        'assets/images/hero/hero-visual.jpg', '', 'Terms of Use', 'Legal')
    content += '''
    <section class="section" aria-label="Terms content">
      <div class="container" style="max-width:780px;">
        <div class="reveal" style="font:400 var(--text-base)/1.8 var(--font-body); color:var(--muted);">
          <p style="margin-bottom:var(--s3);"><strong>Last updated: 2026</strong></p>
          <h2 class="h4" style="margin-bottom:var(--s2); color:var(--charcoal);">1. Use of this website</h2>
          <p style="margin-bottom:var(--s3);">By using this website, you agree to these terms. This website is provided for informational purposes about Ananth Sarth Seva Foundation and its programs. All content is for general information only and should not be relied upon as legal, medical or financial advice.</p>
          <h2 class="h4" style="margin-bottom:var(--s2); color:var(--charcoal);">2. Content accuracy</h2>
          <p style="margin-bottom:var(--s3);">We make reasonable efforts to ensure the accuracy of information on this website. However, programs described as proposed or in development are not guarantees of delivery. Verified impact figures will be published separately.</p>
          <h2 class="h4" style="margin-bottom:var(--s2); color:var(--charcoal);">3. Intellectual property</h2>
          <p style="margin-bottom:var(--s3);">All content — including text, images and design elements — on this website is the property of Ananth Sarth Seva Foundation unless otherwise stated. Reproduction without written permission is prohibited.</p>
          <h2 class="h4" style="margin-bottom:var(--s2); color:var(--charcoal);">4. Third-party links</h2>
          <p style="margin-bottom:var(--s3);">This website may link to external sites. We are not responsible for the content or privacy practices of external websites.</p>
          <h2 class="h4" style="margin-bottom:var(--s2); color:var(--charcoal);">5. Governing law</h2>
          <p>These terms are governed by the laws of India. Any disputes shall be subject to the jurisdiction of courts in [CLIENT: JURISDICTION].</p>
        </div>
      </div>
    </section>'''
    return page('Terms of Use', 'Terms governing the use of the Ananth Sarth Seva Foundation website.', content, '', '', 'hero/hero-visual.jpg', 'terms.html')


# ── Programme data ────────────────────────────────────────────────────────────
PROGRAMS = [
  ('holistic-learning', 'Holistic Learning',
   'Making quality education, digital skills, AI, robotics, vocational training and lifelong learning accessible to underserved communities.',
   'holistic-learning.jpg', 'Learners in an inclusive classroom',
   'Millions of rural and tribal children and young people lack access to quality education, digital skills, vocational pathways and safe learning environments — limiting their ability to participate fully in economic and civic life.',
   ['Establish accessible inclusive classrooms and rural learning hubs for children and young people from economically vulnerable communities.',
    'Provide digital literacy, AI, robotics and innovation training through phygital (physical + digital) learning centres.',
    'Create vocational training and employment pathways that connect rural youth to livelihood opportunities.',
    'Support early childhood to higher education continuums through libraries, reading rooms, literacy camps and coaching centres.'],
   [('📚','Inclusive classrooms for economically vulnerable communities'),('🏠','Safe hostels and support for orphans and street-connected children'),('♿','Accessible education for differently abled learners'),('🌾','Rural learning hubs and reading rooms'),('🤖','AI, robotics and digital innovation labs'),('💼','Vocational training and employment pathways'),('🚀','Youth and rural incubation centres'),('📱','Phygital learning programs'),('🎓','Early childhood to higher education continuum'),('🏛️','Libraries and coaching centre support')],
   '#1A5C9A', '📚', 'Making quality education, digital skills, AI, robotics and vocational training accessible to underserved rural and tribal communities.'),

  ('womens-equity', "Women's Equity",
   'Supporting women through healthcare, safety, financial literacy, livelihood opportunities, digital commerce and community leadership.',
   'womens-equity.jpg', 'Women entrepreneurs reviewing business plans',
   'Women in underserved communities face compounded barriers — limited access to healthcare, economic opportunity, safety networks, digital tools and leadership roles — which compound over generations and constrain entire communities.',
   ['Build financial literacy, livelihood skills and micro-enterprise capabilities among women in underserved communities.',
    'Strengthen health and safety networks through menstrual hygiene education, counselling and support services.',
    'Enable tribal and rural women to preserve, commercialise and own their traditional knowledge and crafts through digital commerce.',
    'Build women-led community governance, SHGs and cooperatives as a pathway to lasting local leadership.'],
   [('💰','Financial literacy and savings programmes'),('🌸','Menstrual health and hygiene awareness'),('🛡️','Safety networks and counselling support'),('🧵','Traditional craft preservation and commercialisation'),('🛒','E-commerce, digital marketing and online brand building'),('🍽️','Food processing and tailoring skill centres'),('🤝','SHGs, cooperatives and micro-enterprises'),('📱','Digital tools training for women entrepreneurs'),('🏛️','Women-led community governance and leadership'),('🏕️','Tribal women\'s development initiatives')],
   '#B56B52', '🌸', 'Supporting women through healthcare, safety, financial literacy, livelihood opportunities, digital commerce and community leadership.'),

  ('resilient-communities', 'Resilient Communities',
   'Combining cultural preservation, smart-village infrastructure, rural innovation, local enterprise and sustainable livelihoods.',
   'resilient-communities.jpg', 'A connected village community',
   'Cultural erosion, distress migration, weak rural infrastructure and lack of sustainable livelihood options continue to fragment communities and reduce their resilience — leaving them dependent on external support.',
   ['Preserve cultural and tribal heritage while creating modern livelihood pathways that respect community identity.',
    'Develop sustainable rural enterprise models through bamboo, forest produce, agriculture and eco-tourism value chains.',
    'Build smart-village infrastructure including digital service centres, skill ATMs and community-owned revenue models.',
    'Prevent distress migration by creating viable, dignified economic opportunity in home communities.'],
   [('🎭','Cultural and tribal heritage preservation'),('🏕️','Tribal hostels and learning spaces'),('🌾','Sustainable agriculture and animal husbandry'),('🌱','Bamboo and minor forest produce value chains'),('🌍','Community-led eco-tourism'),('💻','Smart-village digital services'),('📦','Skill ATMs and learning kiosks'),('🚜','Climate-resilient farming practices'),('🏭','Rural enterprise hubs'),('📊','Community-owned revenue models')],
   '#8B6914', '🏡', 'Combining cultural preservation, smart-village infrastructure, rural innovation, local enterprise and sustainable livelihoods.'),

  ('inclusive-wellness', 'Inclusive Wellness',
   'Bringing mobile healthcare, telemedicine, nutrition, mental health support and integrative wellness to underserved regions.',
   'inclusive-wellness.jpg', 'Healthcare reaching a remote community',
   'Geographical remoteness, infrastructure gaps and limited specialist access leave millions without adequate healthcare, mental health support and nutrition services — compounding across generations with severe consequences for community potential.',
   ['Deploy mobile medical units and last-mile diagnostic services to communities without reliable healthcare access.',
    'Integrate telemedicine platforms to connect remote communities with specialist medical support.',
    'Provide mental health counselling, addiction recovery support and preventive wellness programs.',
    'Combine evidence-based modern medicine with traditional Ayurveda and naturopathy in a respectful, integrated model.'],
   [('🚐','Mobile medical units and last-mile diagnostics'),('💻','Telemedicine and specialist access'),('🧠','Mental health counselling and support'),('🌿','Ayurveda and naturopathy integration'),('🧘','Yoga, meditation and preventive wellness'),('🍎','Nutrition and malnutrition prevention'),('💊','Addiction recovery support'),('🏥','Preventive health camps'),('♻️','Rehabilitation services'),('👩‍⚕️','Local health ambassador training')],
   '#1A7A72', '🏥', 'Bringing mobile healthcare, telemedicine, nutrition, mental health support and integrative wellness to underserved communities.'),

  ('climate-resilience', 'Climate Resilience',
   'Helping communities prepare for climate risks through clean energy, early warning systems, resilient infrastructure and local climate action.',
   'climate-resilience.jpg', 'Community-led clean energy initiative',
   'Rural and tribal communities are disproportionately exposed to climate change impacts — including erratic rainfall, floods, drought and extreme heat — while lacking resources to adapt, access clean energy or implement local climate action.',
   ['Deploy clean energy solutions — solar, wind and bio-energy — to reduce dependence on fossil fuels and provide reliable power.',
    'Establish early-warning systems and disaster-risk reduction protocols adapted to local climate conditions.',
    'Build climate-resilient infrastructure including cool-roof technology and energy-efficient construction.',
    'Train environmental volunteers and youth climate networks to lead local climate action.'],
   [('☀️','Solar, wind and bio-energy deployment'),('⚠️','Early-warning and disaster-risk systems'),('🌲','Urban micro-forests and tree plantation'),('💧','Wetland restoration and soil carbon'),('🏠','Cool-roof and energy-efficient infrastructure'),('🗺️','Local carbon mapping'),('♻️','Waste segregation and circular resource systems'),('🌱','Eco-innovation centres'),('👥','Youth and SHG climate networks'),('🌍','Environmental volunteer programmes')],
   '#1A7A4E', '☀️', 'Helping communities prepare for climate risks through clean energy, early warning systems, resilient infrastructure and local climate action.'),

  ('eco-conservation', 'Eco-Conservation',
   'Empowering communities to protect forests, water, biodiversity, wildlife and natural ecosystems through local participation and technology.',
   'eco-conservation.jpg', 'Community guardians protecting ecosystems',
   'Forests, rivers, wildlife and ecosystems face mounting pressure from deforestation, pollution and unsustainable resource use — without local conservation networks equipped to protect and restore them.',
   ['Empower local communities to become active guardians of forests, water bodies and wildlife through organised conservation networks.',
    'Integrate technology for drone-assisted afforestation, acoustic wildlife monitoring and AI-supported soil mapping (proposed innovations).',
    'Establish zero-waste community models and circular resource systems that reduce environmental pressure.',
    'Build Youth Green Brigades and environmental threat-reporting stations as community-led conservation infrastructure.'],
   [('🌳','Forest protection and community guardians'),('🦋','Wildlife conservation and monitoring'),('💧','River, lake and wetland restoration'),('🚁','Drone-assisted afforestation (proposed)'),('📡','Acoustic and satellite wildlife monitoring (proposed)'),('🌱','Bio-remediation and soil restoration'),('♻️','Zero-waste and circular resource systems'),('🏭','Environmental threat-reporting stations'),('👧','Youth Green Brigades'),('🐾','Wildlife rescue and wetland cleanups')],
   '#1B5E20', '🌿', 'Empowering communities to protect forests, water, biodiversity, wildlife and natural ecosystems through local participation and technology.'),
]


# ── MAIN BUILD ────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    pages = {
        'about.html': build_about(),
        'root-to-rise.html': build_root_to_rise(),
        'programs/index.html': build_programs_index(),
        'contact.html': build_contact(),
        'donate.html': build_donate(),
        'volunteer.html': build_volunteer(),
        'partner.html': build_partner(),
        'impact.html': build_impact(),
        'transparency.html': build_transparency(),
        'careers.html': build_careers(),
        'privacy.html': build_privacy(),
        'terms.html': build_terms(),
    }

    # Add programme pages
    for slug, name, desc, img, img_alt, challenge, objectives, interventions, accent, icon, og_desc in PROGRAMS:
        pages[f'programs/{slug}.html'] = build_program(slug, name, desc, img, img_alt, challenge, objectives, interventions, accent, icon, og_desc)

    built = 0
    for path, content in pages.items():
        os.makedirs(os.path.dirname(path) if os.path.dirname(path) else '.', exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'OK {path}')
        built += 1

    print(f'\nDone. Built {built} pages successfully.')
