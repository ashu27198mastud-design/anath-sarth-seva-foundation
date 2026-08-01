import os
import re

# --- TEMPLATES ---
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
            </ul>
          </li>
          <li class="header__nav-item"><a href="{root_path}impact.html" class="header__nav-link">Impact</a></li>
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
        <p class="footer__tagline">Serving Humanity, Creating Hope.</p>
      </div>
      <div class="footer__col">
        <h4 class="footer__heading">About Us</h4>
        <ul class="footer__list">
          <li><a href="{root_path}about.html" class="footer__link">Our Story</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h4 class="footer__heading">Programs</h4>
        <ul class="footer__list">
          <li><a href="{root_path}programs/holistic-learning.html" class="footer__link">Holistic Learning</a></li>
          <li><a href="{root_path}programs/womens-equity.html" class="footer__link">Women's Equity</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h4 class="footer__heading">Connect</h4>
        <div class="footer__contact">
          <a href="mailto:contact@anathsarthsevafoundation.org" class="footer__link">contact@anathsarthsevafoundation.org</a>
        </div>
      </div>
    </div>
    <div class="footer__bottom">
      <div class="footer__bottom-inner container">
        <span class="footer__copyright">&copy; 2026 Ananth Sarth Seva Foundation. All rights reserved.</span>
      </div>
    </div>
  </footer>

  <script src="{root_path}assets/js/main.js"></script>
</body>
</html>
"""

# Helper to generate 3D cards
def build_3d_card(title, desc):
    return f'''
    <div class="feature-card-3d">
        <div class="feature-icon-wrapper">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
        </div>
        <h3 class="heading-md">{title}</h3>
        <p class="text-md" style="margin-top: 12px; color: var(--gray);">{desc}</p>
    </div>
    '''

# --- PAGE CONTENT DATA ---
PAGES = {
    "about.html": {
        "title": "About Us",
        "root_path": "",
        "about_active": "header__nav-link--active",
        "programs_active": "",
        "involved_active": "",
        "contact_active": "",
        "content": """
    <section class="inner-hero watermark-bg" style="background-color: var(--ivory); padding: 180px 0 80px;">
      <div class="container text-center">
        <h1 class="heading-display">About Us</h1>
        <p class="text-lg" style="max-width: 800px; margin: 24px auto 0;">Ananth Sarth Seva Foundation was newly initiated in 2026 and our journey began with a conversation among close friends who came together with the intention of giving back to society.</p>
      </div>
    </section>

    <section id="our-story" class="section watermark-bg">
      <div class="container">
        <h2 class="heading-lg text-center">Our Story</h2>
        <p class="text-md text-center" style="max-width: 800px; margin: 24px auto;">We felt a shared responsibility to give back to the world. Guided by spiritual values of selfless service and interconnectedness, we realized that creating real change requires a complete plan for human dignity and environmental care. What started as a passionate discussion evolved into a lifelong mission. We saw talented people held back by a lack of opportunities, rich traditions fading due to poverty, and ecosystems threatened by climate change. To break this cycle, we decided to combine ancient wisdom with modern innovation.</p>
      </div>
    </section>

    <section id="vision-mission" class="section" style="background-color: var(--white);">
      <div class="container" style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">
        <div id="vision" class="feature-card-3d">
          <div class="feature-icon-wrapper"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg></div>
          <h2 class="heading-lg">Vision</h2>
          <p class="text-md" style="margin-top: 16px;">To build a sustainable global future by transforming vulnerable regions into thriving hubs of innovation and conservation.</p>
        </div>
        <div id="mission" class="feature-card-3d">
          <div class="feature-icon-wrapper"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg></div>
          <h2 class="heading-lg">Mission</h2>
          <p class="text-md" style="margin-top: 16px;">To empower rural and tribal communities across six core pillars: education, women's equity, self-reliance, holistic healthcare, climate action, and conservation.</p>
        </div>
      </div>
    </section>
    
    <section id="objective" class="section watermark-bg">
      <div class="container">
        <h2 class="heading-lg text-center">Our Objectives</h2>
        <div class="features-grid">
            """ + build_3d_card("Bridging the Knowledge Gap", "Democratising holistic education and tech-driven skills.") + """
            """ + build_3d_card("Digitising Tradition", "Empowering tribal and marginalized women through digital-commerce.") + """
            """ + build_3d_card("Future-Proofing Villages", "Blending indigenous culture with smart technology.") + """
            """ + build_3d_card("Tech-Driven Healthcare", "Merging traditional Indian sciences with digital health tech.") + """
            """ + build_3d_card("Localized Climate Action", "Deploying community-led clean energy models.") + """
            """ + build_3d_card("Community-Led Conservation", "Activating local populations as technology-enabled guardians.") + """
        </div>
      </div>
    </section>

    <section id="how-we-work" class="section" style="background-color: var(--ivory);">
      <div class="container">
        <h2 class="heading-lg text-center">How We Work: The Root-to-Rise Model</h2>
        <p class="text-md text-center" style="max-width: 800px; margin: 24px auto;">We don't believe in temporary fixes. Real, lasting change happens when you look at an ecosystem as a whole. Our 4-Step Operational Framework:</p>
        
        <div class="features-grid">
            """ + build_3d_card("1. Listen & Learn", "We deeply immerse ourselves in rural and tribal communities to map their unique cultural traditions and natural resources.") + """
            """ + build_3d_card("2. Bridge & Blend", "We merge ancient traditions and sciences with digital-age skills, modern medical technology, and localized clean energy.") + """
            """ + build_3d_card("3. Digitalize & Scale", "We connect local craftsmanship directly to global markets via digital commerce and smart technology.") + """
            """ + build_3d_card("4. Transfer Ownership", "We set up local leadership councils to completely manage the initiatives. Our ultimate goal is our own exit.") + """
        </div>
      </div>
    </section>
"""
    },
    
    "programs/holistic-learning.html": {
        "title": "Holistic Learning",
        "root_path": "../",
        "about_active": "",
        "programs_active": "header__nav-link--active",
        "involved_active": "",
        "contact_active": "",
        "content": """
    <section class="inner-hero" style="background-color: #E8F4F8; padding: 180px 0 80px;">
      <div class="container text-center">
        <span class="badge" style="background: var(--royal-blue); color: white; margin-bottom: 16px; display: inline-block;">Education</span>
        <h1 class="heading-display">Holistic Learning</h1>
        <p class="text-lg" style="max-width: 800px; margin: 24px auto 0;">Bridging the educational divide by ensuring high-quality, subsidized, or free institutional access for marginalized communities.</p>
      </div>
    </section>
    <section class="section watermark-bg">
        <div class="container">
            <div class="features-grid">
                """ + build_3d_card("Inclusive Classrooms", "Ensuring high-quality access for minorities, tribes, and economically weaker sections.") + """
                """ + build_3d_card("Targeted Child Welfare", "Establishing safe residential environments and hostels.") + """
                """ + build_3d_card("Dignity for Differently-Abled", "Building completely accessible learning infrastructure.") + """
                """ + build_3d_card("Rural & Agrarian Empowerment", "Decentralized learning hubs and reading rooms.") + """
                """ + build_3d_card("Next-Gen Tech Access", "AI, robotics, and digital innovation hubs for underprivileged youth.") + """
                """ + build_3d_card("Phygital Learning Ecosystems", "Merging physical schools with e-learning platforms.") + """
            </div>
        </div>
    </section>
"""
    },
    
    "programs/womens-equity.html": {
        "title": "Women's Equity",
        "root_path": "../",
        "about_active": "",
        "programs_active": "header__nav-link--active",
        "involved_active": "",
        "contact_active": "",
        "content": """
    <section class="inner-hero" style="background-color: #F8E8F4; padding: 180px 0 80px;">
      <div class="container text-center">
        <span class="badge" style="background: var(--royal-blue); color: white; margin-bottom: 16px; display: inline-block;">Women Empowerment</span>
        <h1 class="heading-display">Women's Equity</h1>
        <p class="text-lg" style="max-width: 800px; margin: 24px auto 0;">Breaking gender-based economic barriers by providing marginalized women with financial literacy, livelihood tools, and sustainable opportunities.</p>
      </div>
    </section>
    <section class="section watermark-bg">
        <div class="container">
            <div class="features-grid">
                """ + build_3d_card("Socio-Economic Upliftment", "Providing financial literacy and sustainable income-generating opportunities.") + """
                """ + build_3d_card("Health & Hygiene Security", "Comprehensive menstrual hygiene management to eliminate stigma.") + """
                """ + build_3d_card("Safety & Crisis Networks", "Emergency crisis support services to protect women in distress.") + """
                """ + build_3d_card("Digital Commerce Integration", "Training women in e-commerce to connect rural creators to global marketplaces.") + """
                """ + build_3d_card("Micro-Entrepreneurship", "Transforming home-based skills into scalable, women-led enterprises.") + """
            </div>
        </div>
    </section>
"""
    },
    
    "programs/resilient-communities.html": {
        "title": "Resilient Communities",
        "root_path": "../",
        "about_active": "",
        "programs_active": "header__nav-link--active",
        "involved_active": "",
        "contact_active": "",
        "content": """
    <section class="inner-hero" style="background-color: #FDF4E3; padding: 180px 0 80px;">
      <div class="container text-center">
        <span class="badge" style="background: var(--royal-blue); color: white; margin-bottom: 16px; display: inline-block;">Rural & Urban Development</span>
        <h1 class="heading-display">Resilient Communities</h1>
        <p class="text-lg" style="max-width: 800px; margin: 24px auto 0;">Eliminating rural poverty by creating sustainable, local livelihood models that stop forced distress migration to cities.</p>
      </div>
    </section>
    <section class="section watermark-bg">
        <div class="container">
            <div class="features-grid">
                """ + build_3d_card("Cultural & Heritage Preservation", "Documenting and protecting tribal arts and indigenous heritage.") + """
                """ + build_3d_card("Smart Village Infrastructure", "Transforming traditional villages into tech-enabled hubs.") + """
                """ + build_3d_card("Skill ATMs", "Deploying localized training kiosks for automated, on-demand vocational learning.") + """
                """ + build_3d_card("Forest Economy Value Chains", "Advanced processing hubs for minor forest produce to maximize local revenue.") + """
            </div>
        </div>
    </section>
"""
    },
    
    "programs/inclusive-wellness.html": {
        "title": "Inclusive Wellness",
        "root_path": "../",
        "about_active": "",
        "programs_active": "header__nav-link--active",
        "involved_active": "",
        "contact_active": "",
        "content": """
    <section class="inner-hero" style="background-color: #E6F7F1; padding: 180px 0 80px;">
      <div class="container text-center">
        <span class="badge" style="background: var(--royal-blue); color: white; margin-bottom: 16px; display: inline-block;">Healthcare</span>
        <h1 class="heading-display">Inclusive Wellness</h1>
        <p class="text-lg" style="max-width: 800px; margin: 24px auto 0;">Bridging the rural-urban medical divide by deploying mobile medical units to provide doorstep diagnostic and healthcare services.</p>
      </div>
    </section>
    <section class="section watermark-bg">
        <div class="container">
            <div class="features-grid">
                """ + build_3d_card("Last-Mile Healthcare Access", "Mobile medical units for remote communities.") + """
                """ + build_3d_card("Destigmatising Mental Health", "Accessible counseling and addiction recovery centers.") + """
                """ + build_3d_card("Telemedicine & Digital Health", "Connecting world-class doctors to patients in remote areas.") + """
                """ + build_3d_card("Integrative Medical Clinics", "Synthesizing Ayurveda and Naturopathy with modern evidence-based medicine.") + """
            </div>
        </div>
    </section>
"""
    },
    
    "programs/climate-resilience.html": {
        "title": "Climate Resilience",
        "root_path": "../",
        "about_active": "",
        "programs_active": "header__nav-link--active",
        "involved_active": "",
        "contact_active": "",
        "content": """
    <section class="inner-hero" style="background-color: #E8EDF8; padding: 180px 0 80px;">
      <div class="container text-center">
        <span class="badge" style="background: var(--royal-blue); color: white; margin-bottom: 16px; display: inline-block;">Environmental</span>
        <h1 class="heading-display">Climate Resilience</h1>
        <p class="text-lg" style="max-width: 800px; margin: 24px auto 0;">Building the capacity of vulnerable communities to anticipate, endure, and recover from localized climate-induced shocks.</p>
      </div>
    </section>
    <section class="section watermark-bg">
        <div class="container">
            <div class="features-grid">
                """ + build_3d_card("Disaster-Resilient Communities", "Implementing village-level early warning systems and risk reduction programs.") + """
                """ + build_3d_card("Decentralized Clean Energy Grids", "Smart solar, wind, or bio-energy installations for remote community spaces.") + """
                """ + build_3d_card("Nature-Based Solution Hubs", "Urban micro-forests, wetland restoration, and soil carbon sinks.") + """
                """ + build_3d_card("Hyper-Local Carbon Mapping", "Data-tracking tools to help rural localities reduce carbon footprints.") + """
            </div>
        </div>
    </section>
"""
    },
    
    "programs/eco-conservation.html": {
        "title": "Eco-Conservation",
        "root_path": "../",
        "about_active": "",
        "programs_active": "header__nav-link--active",
        "involved_active": "",
        "contact_active": "",
        "content": """
    <section class="inner-hero" style="background-color: #F1F8E8; padding: 180px 0 80px;">
      <div class="container text-center">
        <span class="badge" style="background: var(--royal-blue); color: white; margin-bottom: 16px; display: inline-block;">Ecosystem & Natural Resources</span>
        <h1 class="heading-display">Eco-Conservation</h1>
        <p class="text-lg" style="max-width: 800px; margin: 24px auto 0;">Engaging local populations in protecting native forests, trees, and endangered wildlife, fostering a harmonious coexistence.</p>
      </div>
    </section>
    <section class="section watermark-bg">
        <div class="container">
            <div class="features-grid">
                """ + build_3d_card("Community-Led Conservation", "Protecting native forests, trees, and endangered wildlife.") + """
                """ + build_3d_card("Revitalising Shared Waters", "Mobilizing citizens for the cleanup and protection of rivers, lakes, and wetlands.") + """
                """ + build_3d_card("Tech-Driven Eco-Restoration", "Drone-assisted afforestation and AI-mapped soil health tracking.") + """
                """ + build_3d_card("Blue & Green Carbon Vaults", "Utilizing wetlands, oceans, and forests as natural carbon sinks.") + """
            </div>
        </div>
    </section>
"""
    },
}

# Ensure programs directory exists
if not os.path.exists("programs"):
    os.makedirs("programs")

# Only generate About and Programs pages (Contact, Donate, Volunteer, Careers remain unchanged from before unless requested)
for file_path, data in PAGES.items():
    html = HEADER_TEMPLATE.format(
        title=data["title"],
        root_path=data["root_path"],
        about_active=data["about_active"],
        programs_active=data["programs_active"],
        involved_active=data["involved_active"],
        contact_active=data["contact_active"]
    )
    html += data["content"]
    html += FOOTER_TEMPLATE.format(root_path=data["root_path"])
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
        print(f"Generated {file_path}")

print("3D Cards and Watermarks applied to About & Programs successfully!")
