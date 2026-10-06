import re

base = '/Users/fwgibbs/Dropbox/projects/campus-history/essays'

files = [
    ('sara-raynolds-hall', 'Sources'),
    ('popejoy-hall', 'Sources'),
    ('la-posada', 'Bibliography'),
    ('laguna-devargas-hall', 'Bibliography'),
    ('mesa-vista-hall', 'Bibliography'),
    ('ortega-hall', 'Bibliography'),
    ('university-police', 'Bibliography'),
    ('womens-resource-center', 'Bibliography'),
    ('maxwell-museum', 'Bibliography'),
    ('communication-journalism', 'Bibliography'),
    ('hodgin-hall', 'Bibliography'),
    ('humanities-building', 'Bibliography'),
    ('dane-smith-hall', 'Bibliography'),
    ('modern-art', 'Bibliography'),
    ('unm-press', 'Bibliography'),
    ('duck-pond', 'Bibliography'),
    ('lobo-statues', 'Bibliography'),
]

for essay, title in files:
    filepath = f'{base}/{essay}/index.md'
    with open(filepath, 'r') as f:
        content = f.read()

    # Find the heading (modern-art has trailing space)
    heading_re = re.compile(r'## ' + re.escape(title) + r' *\n')
    match = heading_re.search(content)
    if not match:
        print(f'WARNING: heading not found in {essay}')
        continue

    bib_content_start = match.end()

    # For essays with footnotes after bib, find the start of footnote block
    fn_match = re.search(r'\n(\[\^)', content[bib_content_start:])
    if fn_match and essay in ('lobo-statues', 'unm-press'):
        bib_end = bib_content_start + fn_match.start()
        bib_content = content[bib_content_start:bib_end].strip()
        after_bib = content[bib_end:]
    else:
        bib_content = content[bib_content_start:].rstrip('\n')
        after_bib = ''

    before_bib = content[:match.start()]

    new_section = (
        f'{{% capture bibliography %}}\n'
        f'{bib_content}\n'
        f'{{% endcapture %}}\n'
        f'{{% include typography/bibliography.html title="{title}" content=bibliography %}}\n'
    )

    if after_bib:
        new_content = before_bib + new_section + after_bib
    else:
        new_content = before_bib + new_section

    with open(filepath, 'w') as f:
        f.write(new_content)

    print(f'OK: {essay}')
