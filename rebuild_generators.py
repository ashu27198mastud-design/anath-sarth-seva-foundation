import re

PAGE_DATA = {
    "programs/holistic-learning.html": {
        "slug": "holistic-learning",
        "rail_count": "01",
        "badge_text": "Education",
        "title": "Holistic Learning",
        "subline": "Bridging the educational divide by ensuring high-quality, subsidized, or free institutional access for marginalized communities.",
        "alt": "Learners in an inclusive classroom setting",
        "section_h2": "Ten ways we open a classroom"
    },
    "programs/womens-equity.html": {
        "slug": "womens-equity",
        "rail_count": "02",
        "badge_text": "Women's Empowerment",
        "title": "Women's Equity",
        "subline": "Dismantling socio-economic barriers for rural and tribal women through skill-building, self-help groups, and micro-entrepreneurship.",
        "alt": "Women entrepreneurs reviewing business plans",
        "section_h2": "Ten routes to independence"
    },
    "programs/resilient-communities.html": {
        "slug": "resilient-communities",
        "rail_count": "03",
        "badge_text": "Rural & Urban Development",
        "title": "Resilient Communities",
        "subline": "Eliminating rural poverty by creating sustainable, local livelihood models that stop forced distress migration to cities.",
        "alt": "A connected village community and its households",
        "section_h2": "Ten ways a village stands on its own"
    },
    "programs/inclusive-wellness.html": {
        "slug": "inclusive-wellness",
        "rail_count": "04",
        "badge_text": "Healthcare",
        "title": "Inclusive Wellness",
        "subline": "Bridging the rural-urban medical divide by deploying mobile medical units to provide doorstep diagnostic and healthcare services.",
        "alt": "Healthcare reaching a remote community",
        "section_h2": "Ten ways care reaches further"
    },
    "programs/climate-resilience.html": {
        "slug": "climate-resilience",
        "rail_count": "05",
        "badge_text": "Environmental",
        "title": "Climate Resilience",
        "subline": "Building the capacity of vulnerable communities to anticipate, endure, and recover from localized climate-induced shocks.",
        "alt": "Community-led clean energy and climate resilience",
        "section_h2": "Ten defences against a changing climate"
    },
    "programs/eco-conservation.html": {
        "slug": "eco-conservation",
        "rail_count": "06",
        "badge_text": "Ecosystem & Natural Resources",
        "title": "Eco-Conservation",
        "subline": "Engaging local populations in protecting native forests, trees, and endangered wildlife, fostering a harmonious coexistence.",
        "alt": "Community guardians protecting local ecosystems",
        "section_h2": "Ten ways we guard what remains"
    }
}

HERO_TEMPLATE = """
    <section class="inner-hero">
      <div class="container text-center reveal">
        <nav class="rail" aria-label="Programme pillars">
          <span class="rail__label">Pillar</span>
          <span class="rail__ticks">
            <a href="holistic-learning.html" class="tick{active_1}" title="Education"></a>
            <a href="womens-equity.html" class="tick{active_2}" title="Women's Empowerment"></a>
            <a href="resilient-communities.html" class="tick{active_3}" title="Rural &amp; Urban Development"></a>
            <a href="inclusive-wellness.html" class="tick{active_4}" title="Healthcare"></a>
            <a href="climate-resilience.html" class="tick{active_5}" title="Environmental"></a>
            <a href="eco-conservation.html" class="tick{active_6}" title="Ecosystem &amp; Natural Resources"></a>
          </span>
          <span class="rail__count">{rail_count} / 06</span>
        </nav>
        
        <span class="badge badge--blue mb-16">{badge_text}</span>
        <h1 class="t-display">{title}</h1>
        <p class="hero__sub">{subline}</p>
        
        <div class="hero__actions">
            <a href="../donate.html" class="btn btn--primary">Support this pillar</a>
            <a href="#initiatives" class="btn btn--ghost">See all 10 initiatives</a>
        </div>

        <div class="hero__proof">
            <div><span class="hero__proof-n">10</span><span class="hero__proof-l">INITIATIVES</span></div>
            <div><span class="hero__proof-n">100%</span><span class="hero__proof-l">COMMUNITY-LED</span></div>
            <div><span class="hero__proof-n">3–5 yrs</span><span class="hero__proof-l">TO SELF-RELIANCE</span></div>
        </div>
        
        <div class="hero-image-block">
          <img src="../assets/images/programs/{slug}.jpg" alt="{alt}">
        </div>
        <a href="#initiatives" class="hero-scroll-cue">Explore the initiatives ↓</a>
      </div>
    </section>
    
    <section class="section" id="initiatives">
        <div class="container reveal">
            <h2 class="t-eyebrow text-center mt-8">What we do</h2>
            <h3 class="t-h2 text-center mb-s7">{section_h2}</h3>
            <p class="t-micro text-center mb-24">01 — 10</p>
            <div class="features-grid">
"""

def process_file(target_file):
    with open(target_file, "r", encoding="utf-8") as f:
        content = f.read()

    blocks = content.split('PAGES["')
    new_blocks = [blocks[0]]

    for block in blocks[1:]:
        page_key = block.split('"]')[0]
        if page_key in PAGE_DATA:
            pd = PAGE_DATA[page_key]
            active = {f"active_{i}": "" for i in range(1, 7)}
            active[f"active_{int(pd['rail_count'])}"] = " is-active"
            
            hero_html = HERO_TEMPLATE.replace("{active_1}", active["active_1"]) \
                                     .replace("{active_2}", active["active_2"]) \
                                     .replace("{active_3}", active["active_3"]) \
                                     .replace("{active_4}", active["active_4"]) \
                                     .replace("{active_5}", active["active_5"]) \
                                     .replace("{active_6}", active["active_6"]) \
                                     .replace("{rail_count}", pd["rail_count"]) \
                                     .replace("{badge_text}", pd["badge_text"]) \
                                     .replace("{title}", pd["title"]) \
                                     .replace("{subline}", pd["subline"]) \
                                     .replace("{slug}", pd["slug"]) \
                                     .replace("{alt}", pd["alt"]) \
                                     .replace('{section_h2}', pd['section_h2'])
            
            pattern = r'<section class="inner-hero.*?(?:<div class="features-grid">|<div class="features-grid.*?>)'
            block = re.sub(pattern, hero_html.strip(), block, count=1, flags=re.DOTALL)
            
            # Reset card count for this specific block
            card_count = 0
            def card_replacer(match):
                nonlocal card_count
                card_count += 1
                idx = ((card_count - 1) % 10) + 1
                return f'build_3d_card({match.group(1)}, idx="{idx:02d}")'
            
            block = re.sub(r'build_3d_card\((.*?)\)', card_replacer, block)
            
        new_blocks.append(block)

    with open(target_file, "w", encoding="utf-8") as f:
        f.write('PAGES["'.join(new_blocks))

for target_file in ["generate_pages_3.py", "generate_pages_4.py", "generate_pages_5.py"]:
    process_file(target_file)

print("Rebuilt python generators!")
