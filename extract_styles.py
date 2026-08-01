import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html') or f.endswith('.py')]
files += ['programs/' + f for f in os.listdir('programs') if f.endswith('.html')]

styles = set()
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        styles.update(re.findall(r'style="([^"]+)"', file.read()))

for i, style in enumerate(styles):
    print(repr(style) + ',')
