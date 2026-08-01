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
