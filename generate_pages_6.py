PAGES["impact.html"] = {
    "title": "Our Impact",
    "root_path": "",
    "about_active": "",
    "programs_active": "",
    "involved_active": "",
    "impact_active": "header__nav-link--active",
    "contact_active": "",
    "content": """
    <section class="inner-hero inner-hero inner-hero--blue">
      <div class="container text-center reveal">
        <h1 class="heading-display text-white">Our Impact</h1>
        <p class="text-lg container-narrow mt-24 opacity-90">Measurable, community-led change driven by the Root-to-Rise model.</p>
      </div>
    </section>
    
    <section class="section bg-navy-deep text-white">
      <div class="container reveal">
        <div class="stats-grid grid-auto-fit gap-40 text-center">
          <div class="stat-card">
            <h3 class="heading-display text-gold">[CLIENT: NUMBER OF COMMUNITIES REACHED]</h3>
            <p class="text-md">Communities Reached</p>
          </div>
          <div class="stat-card">
            <h3 class="heading-display text-gold">[CLIENT: NUMBER OF LEARNERS SUPPORTED]</h3>
            <p class="text-md">Learners Supported</p>
          </div>
          <div class="stat-card">
            <h3 class="heading-display text-gold">[CLIENT: NUMBER OF WOMEN ENTREPRENEURS]</h3>
            <p class="text-md">Women Entrepreneurs Enabled</p>
          </div>
          <div class="stat-card">
            <h3 class="heading-display text-gold">[CLIENT: HECTARES RESTORED]</h3>
            <p class="text-md">Hectares Restored</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
        <div class="container reveal">
            <h2 class="heading-lg text-center">How We Measure</h2>
            <p class="text-md text-center container-narrow my-24-40">Our impact tracking is tied directly to our Root-to-Rise model, using data-driven metrics to ensure sustained growth and ultimate community independence.</p>
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

    <section class="section bg-ivory">
      <div class="container reveal text-center max-w-800">
        <div class="story-block card--white-lg">
            <img src="assets/images/hero/hero-visual.jpg" alt="Beneficiary story" class="avatar--lg">
            <blockquote class="quote-text">"Since the incubator opened, our cooperative has doubled its production. We are now exporting our crafts and my daughters can go to a good school without us leaving the village."</blockquote>
            <p class="fw-600 text-blue">Priya M.</p>
            <p class="text-sm text-muted">Maharashtra</p>
        </div>
        <div class="mt-56">
            <a href="donate.html" class="btn btn--primary">Donate Now</a>
            <a href="partner.html" class="btn btn--secondary ml-16">Partner With Us</a>
        </div>
      </div>
    </section>
    
    <section class="section bg-white text-center">
      <div class="container reveal">
        <h2 class="heading-md">Transparency & Financials</h2>
        <p class="mt-16">We are committed to absolute financial transparency. View our latest annual reports and audited financials.</p>
        <a href="[CLIENT: LINK TO FINANCIALS]" class="btn btn--outline mt-24">Download Financial Report</a>
      </div>
    </section>
"""
}
