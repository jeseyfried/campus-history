#!/usr/bin/env python3
"""Fix lead paragraph violations in campus-history essays."""
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

# --- hodgin-hall ---
fix("hodgin-hall/index.md",
    '{% include images/figure.html class="img-left" width="60%" caption="Hodgin Hall previously known as the University Building was built in 1892 and is the oldest building on the UNM campus." image-path="images/hodgin-hall-main-pic.PNG" %}\n---\nIf you aren\u2019t familiar with the University Building and do not know where it is located, you are not alone. This University Building has had four name changes and is currently called Hodgin Hall, Alumni Center. This building is located off the corner of Central and University, previously railyard road, and is the heart and backbone of UNM. Some would say it is the unexplored heart, but we will get into that later. Hodgin Hall is where it all started. That\u2019s correct, it is the very first building that was constructed on UNM\u2019s campus and was the only building for almost a decade.\n---\n{% include images/figure.html class="img-right" width="50%"',
    'If you aren\u2019t familiar with the University Building and do not know where it is located, you are not alone. This University Building has had four name changes and is currently called Hodgin Hall, Alumni Center. This building is located off the corner of Central and University, previously railyard road, and is the heart and backbone of UNM. Some would say it is the unexplored heart, but we will get into that later. Hodgin Hall is where it all started. That\u2019s correct, it is the very first building that was constructed on UNM\u2019s campus and was the only building for almost a decade.\n\n{% include images/figure.html class="img-left" width="60%" caption="Hodgin Hall previously known as the University Building was built in 1892 and is the oldest building on the UNM campus." image-path="images/hodgin-hall-main-pic.PNG" %}\n\n---\n{% include images/figure.html class="img-right" width="50%"'
)

# --- center-of-the-universe ---
fix("center-of-the-universe/index.md",
    '## Controversy in Concrete\nSome may call it an eyesore.',
    'Some may call it an eyesore.'
)
# Also need to remove the heading and ensure paragraph ends before ## The Big Bang
fix("center-of-the-universe/index.md",
    'stand tall between Mitchell and Ortega hall.\n\n## The Big Bang',
    'stand tall between Mitchell and Ortega hall.\n\n## Controversy in Concrete\n\n## The Big Bang'
)

# --- duck-pond ---
fix("duck-pond/index.md",
    '{% include images/figure.html class="img-left" width="75%" caption="A photo of the Pond taken shortly after completion. shows a distinct lack of foliage on the peninsula and surrounding area." image-path="images/duck-pond-0002.png" %}\n\n## Yatoka Hall & Y-1\n[Yatoka Hall]',
    'Built in 1975, the Duck Pond was met with hesitation and heavy criticism from the campus community. It was eventually embraced and named by students, who have adored it ever since.\n\n## Yatoka Hall & Y-1\n\n{% include images/figure.html class="img-left" width="75%" caption="A photo of the Pond taken shortly after completion. shows a distinct lack of foliage on the peninsula and surrounding area." image-path="images/duck-pond-0002.png" %}\n\n[Yatoka Hall]'
)

# --- la-posada ---
fix("la-posada/index.md",
    '{% include images/juxtapose.html\nid="juxtapose-exterior"\nimage1="images/la-posada-building-sign2.jpg"\nimage2="images/lp-outside-comparison.jpg"\ncaption="La Posada circa 1970s',
    'In an architectural sense, UNM has furiously sought to reflect itself within the space in which it surrounds. La Posada Dining Hall, Laguna and De Vargas Dormitory, and all other building that came before and after all have displayed that UNM wants to represent its unique modern South Western culture in its architecture. La Posadas, architecturally being built in an adobe style, reflecting UNMs latter 20th century culture, similar to other building built at the time like the Laguna Dormitory, De Vargas Dormitory, Kiva Lecture Hall, and the Farris Engineering Center.\n\n{% include images/juxtapose.html\nid="juxtapose-exterior"\nimage1="images/la-posada-building-sign2.jpg"\nimage2="images/lp-outside-comparison.jpg"\ncaption="La Posada circa 1970s'
)

# Remove the paragraph from under ### A Reflection of Ourselves
fix("la-posada/index.md",
    '  %}In an architectural sense, UNM has furiously sought to reflect itself within the space in which it surrounds. La Posada Dining Hall, Laguna and De Vargas Dormitory, and all other building that came before and after all have displayed that UNM wants to represent its unique modern South Western culture in its architecture. La Posadas, architecturally being built in an adobe style, reflecting UNMs latter 20th century culture, similar to other building built at the time like the Laguna Dormitory, De Vargas Dormitory, Kiva Lecture Hall, and the Farris Engineering Center.',
    '  %}'
)

# --- mckinnon-center ---
fix("mckinnon-center/index.md",
    '{% include images/figure.html class="img-center" width="100%" caption="The McKinnon Center for Management, UNM\u2019s most modern development and the latest addition to The School of Management. [_Source_](https://www.mgt.unm.edu/building/construction-photos.asp)" image-path="images/mcm.jpg" %}\n\n## Background\n\nThe McKinnon Center for Management is the staple of UNM\u2019s northern edge of campus.  The multi-story building was constructed as a replacement for the deteriorating Anderson School of Management building, and $5 million of the total $25.4 million funds were donated to UNM by Ian and Sonnet McKinnon.  The building became accessible to students in the summer of 2018',
    'The McKinnon Center for Management is the staple of UNM\u2019s northern edge of campus.  The multi-story building was constructed as a replacement for the deteriorating Anderson School of Management building, and $5 million of the total $25.4 million funds were donated to UNM by Ian and Sonnet McKinnon.\n\n{% include images/figure.html class="img-center" width="100%" caption="The McKinnon Center for Management, UNM\u2019s most modern development and the latest addition to The School of Management. [_Source_](https://www.mgt.unm.edu/building/construction-photos.asp)" image-path="images/mcm.jpg" %}\n\n## Background\n\nThe building became accessible to students in the summer of 2018'
)

# --- ortega-hall (2 changes) ---
fix("ortega-hall/index.md",
    '{% include images/figure.html class="img-center" width="75%" caption="March, 9 1998; Looking Southeast towards Smith plaza on this gloomy winter day. The artwork of Bruce Nauman\u2019s Center of the Universe pictured on the rightside.[Source](https://econtent.unm.edu/digital/collection/ULPhotoImag/id/3352/rec/83)" image-path="images/ortega-hall-exterior-gloomy.jpg" %}\n\n### Location\nOrtega Hall is located southwest of Zimmermann Library and east of the Smith Plaza.',
    'This 50,000 square foot classroom and faculty office building at the University of New Mexico also contains clusters of language labratories and audiovisual rooms as well as a large student lounge and library. Completed in 1977 for a cost of $1,440,000, this first increment in the main academic area of the central campus established the upper pedestrian walkway system which connects the major academic buildings south of the central plaza.\n\n{% include images/figure.html class="img-center" width="75%" caption="March, 9 1998; Looking Southeast towards Smith plaza on this gloomy winter day. The artwork of Bruce Nauman\u2019s Center of the Universe pictured on the rightside.[Source](https://econtent.unm.edu/digital/collection/ULPhotoImag/id/3352/rec/83)" image-path="images/ortega-hall-exterior-gloomy.jpg" %}\n\n### Location\nOrtega Hall is located southwest of Zimmermann Library and east of the Smith Plaza.'
)
# Remove duplicate text from ### The Exterior Design
fix("ortega-hall/index.md",
    '### The Exterior Design\nThis 50,000 square foot classroom and faculty office building at the University of New Mexico also contains clusters of language labratories and audiovisual rooms as well as a large student lounge and library. Completed in 1977 for a cost of $1,440,000, this first increment in the main academic area of the central campus established the upper pedestrian walkway system which connects the major academic buildings south of the central plaza.',
    '### The Exterior Design'
)

# --- mitchell-hall ---
fix("mitchell-hall/index.md",
    '## Location\nMitchell hall is located just south of Dane Smith Hall in-between the Duck Pond and Carlisle Gym.',
    'Mitchell Hall is located just south of Dane Smith Hall, between the Duck Pond and Carlisle Gym.'
)

# --- womens-resource-center ---
fix("womens-resource-center/index.md",
    '## Womens Resource Center\n{% include images/figure.html class="img-center" width="100%" caption="Womens resource center at UNM has evolved meraculously over the past 50 years into a home and inclusive space for many students and survivors. [Source](https://rmoa.unm.edu/docviewer.php?docId=nmu1unma028.xml)" image-path="images/wrc-building.jpeg" %}\n\n## The Climb for Women at UNM\nFor centuries, women were told to be silent',
    'For centuries, women were told to be silent'
)
# Move the first paragraph out as lead, leaving ## The Climb section starting at the figure
fix("womens-resource-center/index.md",
    'For centuries, women were told to be silent, that their words meant nothing and an education for a woman was out of the ordinary. Today women\u2019s voices, create movements, win elections and rewrite laws. It was not long ago when women fought for a place in the classroom. Women at UNM made up less than 50% of total students in the 1970\u2019s. The climb for women at UNM has been a fight for equal opportunity, that continues to shape the institution that stands before us today. \n{% include images/figure.html\n  class="img-right"\n  width="66%"\n  caption="Women at UNM 1972-73"\nimage-path="images/KIC Document 0001.jpg"\n%}\nFor women, the start of revolutionary change began in the early 1970\u2019s',
    'For centuries, women were told to be silent, that their words meant nothing and an education for a woman was out of the ordinary. Today women\u2019s voices, create movements, win elections and rewrite laws. It was not long ago when women fought for a place in the classroom. Women at UNM made up less than 50% of total students in the 1970\u2019s. The climb for women at UNM has been a fight for equal opportunity, that continues to shape the institution that stands before us today.\n\n## The Climb for Women at UNM\n\n{% include images/figure.html\n  class="img-right"\n  width="66%"\n  caption="Women at UNM 1972-73"\nimage-path="images/KIC Document 0001.jpg"\n%}\nFor women, the start of revolutionary change began in the early 1970\u2019s'
)

print("\nAll done.")
