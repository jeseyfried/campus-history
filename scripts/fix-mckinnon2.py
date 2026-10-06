#!/usr/bin/env python3
"""Fix mckinnon-center by index-based replacement."""
path = "/Users/fwgibbs/Dropbox/projects/campus-history/essays/mckinnon-center/index.md"
content = open(path).read()

# Find exact boundaries
fig_start = content.find('{% include images/figure.html class="img-center" width="100%"')
fig_end = content.find(' %}\n', fig_start) + len(' %}\n')

bg_start = content.find('## Background\n\n', fig_end)
bg_para_start = bg_start + len('## Background\n\n')

# Find end of first two sentences (ending with McKinnon.)
# Sentences: "The McKinnon Center...campus." and "The multi-story...McKinnon."
para_text = content[bg_para_start:]
# Find second period after "McKinnon"
s1_end = para_text.find('McKinnon.') + len('McKinnon.')
# But check it's the Ian and Sonnet McKinnon sentence
if 'Ian and Sonnet McKinnon.' in para_text[:s1_end+50]:
    split_at = bg_para_start + para_text.find('Ian and Sonnet McKinnon.') + len('Ian and Sonnet McKinnon.')
    print(f"Split at index: {split_at}")
    print(repr(content[split_at:split_at+30]))
    
    # The new content:
    lead = content[bg_para_start:split_at]
    print(f"\nLead paragraph:\n{lead}\n")
    
    # New structure: lead + blank + figure + blank + ## Background + blank + rest of para
    rest_start = split_at
    while rest_start < len(content) and content[rest_start] in ' ':
        rest_start += 1
    if content[rest_start] == '\n':
        rest_start += 1
    if rest_start < len(content) and content[rest_start] == '\n':
        rest_start += 1
        
    figure_block = content[fig_start:fig_end]
    rest_of_para = content[rest_start:]
    
    new_content = (content[:fig_start]
                   + lead + '\n\n'
                   + figure_block + '\n'
                   + '## Background\n\n'
                   + rest_of_para)
    
    open(path, 'w').write(new_content)
    print("FIXED: mckinnon-center")
else:
    print("Could not find split point")
    print(repr(para_text[:200]))
