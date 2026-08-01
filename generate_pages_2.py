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
