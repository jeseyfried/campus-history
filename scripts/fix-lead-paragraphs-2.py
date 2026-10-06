#!/usr/bin/env python3
"""Fix remaining lead paragraph issues."""
import os

base = "/Users/fwgibbs/Dropbox/projects/campus-history/essays"

def fix(path, old, new):
    full = os.path.join(base, path)
    content = open(full).read()
    if old in content:
        content = content.replace(old, new, 1)
        open(full, 'w').write(content)
        print(f"  FIXED: {path}")
    else:
        print(f"  SKIP (not found): {path}")
        # Debug
        # print(repr(old[:80]))

# --- la-posada: remove duplicate paragraph from under ### A Reflection ---
fix("la-posada/index.md",
    '  %}'\
    '\n\nIn an architectural sense, UNM has furiously sought to reflect itself within the space in which it surrounds. La Posada Dining Hall, Laguna and De Vargas Dormitory, and all other building that came before and after all have displayed that UNM wants to represent its unique modern South Western culture in its architecture. La Posadas, architecturally being built in an adobe style, reflecting UNMs latter 20th century culture, similar to other building built at the time like the Laguna Dormitory, De Vargas Dormitory, Kiva Lecture Hall, and the Farris Engineering Center. \t',
    '  %}'
)

# --- mckinnon-center: fix with straight apostrophes ---
fix("mckinnon-center/index.md",
    '{% include images/figure.html class="img-center" width="100%" caption="The McKinnon Center for Management, UNM\'s most modern development and the latest addition to The School of Management. [_Source_](https://www.mgt.unm.edu/building/construction-photos.asp)" image-path="images/mcm.jpg" %}\n\n## Background\n\nThe McKinnon Center for Management is the staple of UNM\'s northern edge of campus.  The multi-story building was constructed as a replacement for the deteriorating Anderson School of Management building, and $5 million of the total $25.4 million funds were donated to UNM by Ian and Sonnet McKinnon.  The building became accessible to students in the summer of 2018',
    'The McKinnon Center for Management is the staple of UNM\'s northern edge of campus.  The multi-story building was constructed as a replacement for the deteriorating Anderson School of Management building, and $5 million of the total $25.4 million funds were donated to UNM by Ian and Sonnet McKinnon.\n\n{% include images/figure.html class="img-center" width="100%" caption="The McKinnon Center for Management, UNM\'s most modern development and the latest addition to The School of Management. [_Source_](https://www.mgt.unm.edu/building/construction-photos.asp)" image-path="images/mcm.jpg" %}\n\n## Background\n\nThe building became accessible to students in the summer of 2018'
)

# --- ortega-hall: add lead paragraph before opening image ---
# The text was already removed from ### The Exterior Design; now add it as the lead
fix("ortega-hall/index.md",
    '{% include images/figure.html class="img-center" width="75%" caption="March, 9 1998; Looking Southeast towards Smith plaza on this gloomy winter day. The artwork of Bruce Nauman\'s Center of the Universe pictured on the rightside.[Source](https://econtent.unm.edu/digital/collection/ULPhotoImag/id/3352/rec/83)" image-path="images/ortega-hall-exterior-gloomy.jpg" %}\n\n### Location',
    'This 50,000 square foot classroom and faculty office building at the University of New Mexico also contains clusters of language labratories and audiovisual rooms as well as a large student lounge and library. Completed in 1977 for a cost of $1,440,000, this first increment in the main academic area of the central campus established the upper pedestrian walkway system which connects the major academic buildings south of the central plaza.\n\n{% include images/figure.html class="img-center" width="75%" caption="March, 9 1998; Looking Southeast towards Smith plaza on this gloomy winter day. The artwork of Bruce Nauman\'s Center of the Universe pictured on the rightside.[Source](https://econtent.unm.edu/digital/collection/ULPhotoImag/id/3352/rec/83)" image-path="images/ortega-hall-exterior-gloomy.jpg" %}\n\n### Location'
)

# --- womens-resource-center: insert ## The Climb heading back after lead paragraph ---
fix("womens-resource-center/index.md",
    "shape the institution that stands before us today. \n{% include images/figure.html\n  class=\"img-right\"\n  width=\"66%\"\n  caption=\"Women at UNM 1972-73\"\nimage-path=\"images/KIC Document 0001.jpg\"\n%}\nFor women, the start of revolutionary change began in the early 1970",
    "shape the institution that stands before us today.\n\n## The Climb for Women at UNM\n\n{% include images/figure.html\n  class=\"img-right\"\n  width=\"66%\"\n  caption=\"Women at UNM 1972-73\"\nimage-path=\"images/KIC Document 0001.jpg\"\n%}\nFor women, the start of revolutionary change began in the early 1970"
)

print("\nAll done.")
