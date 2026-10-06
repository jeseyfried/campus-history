#!/usr/bin/env python3
"""Debug mckinnon-center."""
path = "/Users/fwgibbs/Dropbox/projects/campus-history/essays/mckinnon-center/index.md"
content = open(path).read()

# Find the figure include
idx = content.find('{% include images/figure.html class="img-center" width="100%"')
if idx >= 0:
    chunk = content[idx:idx+350]
    print("CHUNK:")
    print(repr(chunk))
    print()
    
    # Try to match parts
    part1 = '{% include images/figure.html class="img-center" width="100%"'
    part2 = 'The McKinnon Center for Management is the staple'
    print("part1 found:", part1 in content)
    print("part2 found:", part2 in content)
    
    # Find part1 end
    end1 = content.find(' %}\n', idx)
    print(f"\nFigure ends at: {end1}")
    print(repr(content[end1:end1+30]))
