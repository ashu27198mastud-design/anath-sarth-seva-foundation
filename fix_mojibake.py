import os

def fix_mojibake(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            text = f.read()
    except Exception as e:
        return

    mapping = {
        'ðŸ“š': '📚',
        'ðŸŒ¸': '🌸',
        'ðŸ ¡': '🏡',
        'ðŸ ¥': '🏥',
        'ðŸŒŽ': '🌎',
        'ðŸŒ±': '🌱',
        'ðŸŒ³': '🌳',
        'â•': '═',
        'Ã¢â‚¬â€œ': '–',
        'Ã¢â‚¬â€': '—',
        'Ã¢â‚¬â„¢': "'",
        'Ã¢â‚¬Å“': '"',
        'Ã¢â‚¬Â': '"',
        'Â·': '·',
        'δŸCE±': '🌱'
    }

    count = 0
    for bad, good in mapping.items():
        if bad in text:
            text = text.replace(bad, good)
            count += 1

    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'Fixed {count} instances in {filepath}')

fix_mojibake('build_site.py')

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            fix_mojibake(os.path.join(root, file))
