import os
import re

STYLE_MAP = {
    'border-top: 4px solid var(--color-royal-blue);': 'border-top-royal',
    'padding: 24px; border: 1px solid #eee;': 'card--light',
    'width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 6px;': 'input--default',
    'background-color: var(--ivory); padding: 180px 0 80px;': 'inner-hero',
    'font-size: 20px; font-style: italic; color: var(--gray); line-height: 1.6; margin-bottom: 24px;': 'quote-text',
    'max-width: 800px; margin: 24px auto 0;': 'container-narrow mt-24',
    'display: grid; grid-template-columns: 1fr 1fr; gap: 40px;': 'grid-2 gap-40',
    'color: var(--gold);': 'text-gold',
    'font-size: 14px; color: var(--gray);': 'text-sm text-muted',
    'margin-top: 16px; line-height: 2;': 'mt-16 lh-2',
    'display: grid; grid-template-columns: 1fr 1fr; gap: 32px; margin-top: 48px;': 'grid-2 gap-32 mt-48',
    'margin-top: 16px;': 'mt-16',
    'margin-top: 12px; font-weight: 500;': 'mt-12 fw-500',
    'max-width: 800px; margin: 24px auto;': 'container-narrow my-24',
    'margin-bottom: 24px;': 'mb-24',
    'display: grid; grid-template-columns: 1fr 1fr; gap: 64px;': 'grid-2 gap-64',
    'display: flex; flex-wrap: wrap; gap: 24px; justify-content: space-between; font-size: 13px; opacity: 0.8;': 'footer__bottom',
    'margin-top: 32px;': 'mt-32',
    'background-color: var(--royal-blue); color: white; padding: 160px 0 60px;': 'inner-hero inner-hero--blue',
    'margin-top: 48px; background: white; padding: 32px; border-radius: 12px; box-shadow: var(--shadow-sm); text-align: center;': 'card--elevated mt-48 text-center',
    'font-weight: 600; color: var(--royal-blue);': 'fw-600 text-blue',
    'margin-top: 56px;': 'mt-56',
    'background-color: rgba(255,255,255,0.05); padding: 16px 0; margin-top: 32px; border-top: 1px solid rgba(255,255,255,0.1); border-bottom: 1px solid rgba(255,255,255,0.1);': 'footer__transparency',
    'margin-top: 8px;': 'mt-8',
    'background-color: #E8F4F8; padding: 132px 0 72px;': 'inner-hero',
    'text-align: center; margin-top: 64px;': 'text-center mt-64',
    'margin-top: 24px;': 'mt-24',
    'margin-top: 12px; color: var(--gray);': 'mt-12 text-muted',
    'max-width: 800px; margin: 24px auto 40px;': 'container-narrow my-24-40',
    'background: var(--royal-blue); color: white; margin-bottom: 16px; display: inline-block;': 'badge--blue',
    'border-color: var(--color-gold); color: var(--color-gold);': 'btn--outline-gold',
    'max-width: 800px; font-size: 16px; line-height: 1.8;': 'container-narrow text-lead',
    'background-color: #F1F8E8; padding: 132px 0 72px;': 'inner-hero',
    'background-color: var(--white);': 'bg-white',
    'margin-left: 16px;': 'ml-16',
    'background-color: var(--ivory);': 'bg-ivory',
    'width: 120px; height: 120px; border-radius: 50%; object-fit: cover; margin: 0 auto 24px; border: 2px solid var(--gold);': 'avatar--lg',
    'margin-top: 64px;': 'mt-64',
    'max-width: 800px; margin: 24px auto 48px;': 'container-narrow my-24-48',
    'color: inherit; text-decoration: underline;': 'link--inherit',
    'background: linear-gradient(135deg, var(--color-royal-blue) 0%, #060640 100%); color: white;': 'bg-gradient-blue text-white',
    'background-color: #E8EDF8; padding: 132px 0 72px;': 'inner-hero',
    'margin: 2rem 0; font-size: 0.9rem; color: var(--color-muted);': 'my-32 text-sm text-muted',
    'max-width: 640px; margin: 20px auto 0;': 'hero__sub',
    'background-color: #FDF4E3; padding: 132px 0 72px;': 'inner-hero',
    'border-top: 4px solid var(--color-green);': 'border-top-green',
    'max-width: 800px;': 'max-w-800',
    'margin-top: 2rem;': 'mt-32',
    'background-color: #050538; color: white;': 'bg-navy-deep text-white',
    'max-width: 800px; margin: 0 auto; text-align: center;': 'container-narrow text-center',
    'max-width: 800px; margin: 0 auto;': 'container-narrow',
    'background: white; padding: 40px; border-radius: 24px; box-shadow: 0 10px 40px rgba(10,10,112,0.05);': 'card--white-lg',
    'margin-top: 16px; font-size: 14px; opacity: 0.8; line-height: 1.6;': 'mt-16 text-sm opacity-80 lh-16',
    'background: white; padding: 40px; border-radius: 16px; box-shadow: var(--shadow-md);': 'card--white-md',
    'background-color: #E6F7F1; padding: 132px 0 72px;': 'inner-hero',
    'margin-top: 48px;': 'mt-48',
    'border-top: 4px solid var(--color-gold);': 'border-top-gold',
    'background-color: #F8E8F4; padding: 132px 0 72px;': 'inner-hero',
    'background-color: var(--white); text-align: center;': 'bg-white text-center',
    'margin: 0 auto 16px;': 'mx-auto mb-16',
    'display: flex; flex-direction: column; gap: 16px;': 'flex-col gap-16',
    'display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 40px; text-align: center;': 'grid-auto-fit gap-40 text-center',
    'max-width: 800px; margin: 24px auto 0; opacity: 0.9;': 'container-narrow mt-24 opacity-90',
    'background-color: var(--royal-blue); color: white; padding: 180px 0 80px;': 'inner-hero inner-hero--blue',
    'display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-top: 3rem;': 'flex-center gap-16 mt-48',
}

NEW_CSS = """
/* ===========================
   AUTO-GENERATED SEMANTIC CLASSES
   =========================== */
.border-top-royal { border-top: 4px solid var(--navy); }
.card--light { padding: 24px; border: 1px solid #eee; }
.input--default { width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 6px; }
.quote-text { font-size: 20px; font-style: italic; color: var(--muted); line-height: 1.6; margin-bottom: 24px; }
.container-narrow { max-width: 800px; margin: 0 auto; }
.grid-2 { display: grid; grid-template-columns: 1fr; }
@media (min-width: 768px) { .grid-2 { grid-template-columns: 1fr 1fr; } }
.gap-40 { gap: 40px; }
.gap-32 { gap: 32px; }
.gap-64 { gap: 64px; }
.mt-48 { margin-top: 48px; }
.mt-64 { margin-top: 64px; }
.lh-2 { line-height: 2; }
.fw-500 { font-weight: 500; }
.my-24 { margin-top: 24px; margin-bottom: 24px; }
.footer__bottom { display: flex; flex-wrap: wrap; gap: 24px; justify-content: space-between; font-size: 13px; opacity: 0.8; }
.mt-32 { margin-top: 32px; }
.inner-hero--blue { background: var(--navy); color: white; }
.card--elevated { background: var(--surface); padding: 32px; border-radius: var(--r-md); box-shadow: var(--e1); }
.fw-600 { font-weight: 600; }
.mt-56 { margin-top: 56px; }
.footer__transparency { background-color: rgba(255,255,255,0.05); padding: 16px 0; margin-top: 32px; border-top: 1px solid rgba(255,255,255,0.1); border-bottom: 1px solid rgba(255,255,255,0.1); }
.my-24-40 { margin: 24px auto 40px; }
.my-24-48 { margin: 24px auto 48px; }
.badge--blue { background: var(--navy); color: white; margin-bottom: 16px; display: inline-block; }
.btn--outline-gold { border-color: var(--gold); color: var(--gold-dk); }
.text-lead { font-size: 16px; line-height: 1.8; }
.ml-16 { margin-left: 16px; }
.avatar--lg { width: 120px; height: 120px; border-radius: 50%; object-fit: cover; margin: 0 auto 24px; border: 2px solid var(--gold); }
.link--inherit { color: inherit; text-decoration: underline; }
.bg-gradient-blue { background: linear-gradient(135deg, var(--navy) 0%, var(--navy-deep) 100%); color: white; }
.my-32 { margin: 32px 0; }
.hero__sub { max-width: 640px; margin: 20px auto 0; }
.border-top-green { border-top: 4px solid var(--green); }
.max-w-800 { max-width: 800px; }
.bg-navy-deep { background-color: var(--navy-deep); color: white; }
.card--white-lg { background: var(--surface); padding: 40px; border-radius: var(--r-lg); box-shadow: var(--e2); }
.opacity-80 { opacity: 0.8; }
.lh-16 { line-height: 1.6; }
.card--white-md { background: var(--surface); padding: 40px; border-radius: var(--r-md); box-shadow: var(--e1); }
.border-top-gold { border-top: 4px solid var(--gold); }
.mx-auto { margin-left: auto; margin-right: auto; }
.flex-col { display: flex; flex-direction: column; }
.gap-16 { gap: 16px; }
.grid-auto-fit { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); }
.opacity-90 { opacity: 0.9; }
.flex-center { display: flex; justify-content: center; }
"""

with open('assets/css/design-system.css', 'a', encoding='utf-8') as css_file:
    css_file.write(NEW_CSS)

files = [f for f in os.listdir('.') if f.endswith('.html') or f.endswith('.py')]
files += ['programs/' + f for f in os.listdir('programs') if f.endswith('.html')]

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Update font link
    content = re.sub(
        r'<link href="https://fonts\.googleapis\.com/css2\?[^"]+" rel="stylesheet">',
        '<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">',
        content
    )
    
    # 2. Remove class
    content = content.replace('', '')
    content = content.replace('', '')
    content = content.replace('class=""', 'class=""')
    
    # 3. Replace styles
    def style_replacer(match):
        style_str = match.group(1).strip()
        # Find exact match
        if style_str in STYLE_MAP:
            mapped_class = STYLE_MAP[style_str]
            return f' class="{mapped_class}"'
        else:
            print(f"UNMAPPED STYLE in {f}: {style_str}")
            return match.group(0)
    
    content = re.sub(r'\s*style="([^"]+)"', style_replacer, content)
    
    # 4. Merge data-refactor-class into class
    def merge_classes(match):
        existing_class = match.group(1)
        new_class = match.group(2)
        return f'class="{existing_class} {new_class}"'
    
    content = re.sub(r'class="([^"]*)"\s+class="([^"]+)"', merge_classes, content)
    
    # In case there was no class attribute:
    content = re.sub(r'class="([^"]+)"', r'class="\1"', content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Refactor complete.")
