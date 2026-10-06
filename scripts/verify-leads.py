#!/usr/bin/env python3
"""Verify all 13 essay lead paragraphs."""

essays = [
    'hodgin-hall', 'laguna-devargas-hall', 'lobo-statues', 'marron-hall',
    'mesa-vista-hall', 'modern-art', 'duck-pond', 'la-posada', 'mckinnon-center',
    'ortega-hall', 'center-of-the-universe', 'mitchell-hall', 'womens-resource-center'
]

for name in essays:
    path = f'essays/{name}/index.md'
    c = open(path).read()
    fm_end = c.find('---', 3) + 3
    body = c[fm_end:].lstrip('\n')
    first_char = body[:1]
    starts_bad = first_char in ('#', '{', '`', '>')
    status = 'FAIL' if starts_bad else 'OK'
    print(f'[{status}] {name}: {body[:80]!r}')
