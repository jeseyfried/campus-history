#!/usr/bin/env python3
"""Fix mckinnon-center lead paragraph."""
import os

path = "/Users/fwgibbs/Dropbox/projects/campus-history/essays/mckinnon-center/index.md"
content = open(path).read()

old = ('{% include images/figure.html class="img-center" width="100%" caption="The McKinnon Center for Management, UNM\'s most modern development and the latest addition to The School of Management. [_Source_](https://www.mgt.unm.edu/building/construction-photos.asp)" image-path="images/mcm.jpg" %}'
       '\n\n## Background\n\n'
       'The McKinnon Center for Management is the staple of UNM\'s northern edge of campus.  The multi-story building was constructed as a replacement for the deteriorating Anderson School of Management building, and $5 million of the total $25.4 million funds were donated to UNM by Ian and Sonnet McKinnon.  The building became accessible to students in the summer of 2018')

new = ('The McKinnon Center for Management is the staple of UNM\'s northern edge of campus.  The multi-story building was constructed as a replacement for the deteriorating Anderson School of Management building, and $5 million of the total $25.4 million funds were donated to UNM by Ian and Sonnet McKinnon.'
       '\n\n{% include images/figure.html class="img-center" width="100%" caption="The McKinnon Center for Management, UNM\'s most modern development and the latest addition to The School of Management. [_Source_](https://www.mgt.unm.edu/building/construction-photos.asp)" image-path="images/mcm.jpg" %}'
       '\n\n## Background\n\n'
       'The building became accessible to students in the summer of 2018')

if old in content:
    content = content.replace(old, new, 1)
    open(path, 'w').write(content)
    print("FIXED: mckinnon-center")
else:
    print("NOT FOUND")
    # Try to find the figure
    idx = content.find('construction-photos.asp')
    if idx >= 0:
        print(repr(content[idx:idx+200]))
    else:
        print("Figure not found at all")
