import os

def update_logos(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    text = text.replace('class="header__logo-img" width="160" height="48"', 'class="header__logo-img" width="210" height="64"')
    text = text.replace('class="footer__brand-logo" width="160" height="48"', 'class="footer__brand-logo" width="210" height="64"')
    text = text.replace('class="mobile-nav__logo-img" width="140" height="42"', 'class="mobile-nav__logo-img" width="178" height="54"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

update_logos('index.html')
update_logos('build_site.py')
print('Updated logos safely')
