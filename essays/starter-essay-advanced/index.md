---
title: Starter Essay Advanced
author: Your Name
layout: essay
date: 2026-11-12
header-title: Your Campus Topic
header-subtitle: Replace this with a short phrase if your essay needs one
category: Starter Essay
popup-teaser: Replace this with one clear sentence that makes readers want to know more.
card-description: Replace this with two sentences that summarize the story your essay tells and why it matters.
card-image: /essays/starter-essay-advanced/images/sample-archive-photo.jpg
header-image: images/sample-archive-photo.jpg
header-caption: Replace this with a short source note for your header image.
header-position: center center
start: 1950
---

This advanced starter includes a few optional components: a pullquote, an image grid, a before/after style image slider, and a bibliography drawer. Delete any component you do not need. A clean simple essay is better than a cluttered essay with every possible feature.

## Opening Historical Problem

Use this section to set up the historical problem your essay investigates. What seems obvious about your topic today? What does the archive reveal that complicates that first impression?

{% include typography/aside.html
  class="right"
  text="Replace this pullquote with one vivid sentence from your essay or from a primary source."
%}

Your prose should still carry the main argument. Pullquotes are highlights, not substitutes for explanation. Use them sparingly when a phrase or source deserves extra attention.

## Archival Evidence

Use this section to show readers the evidence behind your interpretation. Explain what you found, where you found it, and how it changed what you thought you knew.

{% assign images =
"images/sample-archive-photo.jpg,
images/sample-primary-source.jpg" | split: ','
%}

{% assign captions =
"Replace this with a caption for the first image, including source information.|
Replace this with a caption for the second image, including source information." | split: '|'
%}

{% include images/image-grid.html
  images=images
  captions=captions
  columns=2
%}

## Change Over Time

Use this section to explain chronology. What changed, when, and why? What stayed the same? Which people or institutions had the power to shape what happened?

If you have two images that show a meaningful comparison, use a slider. This works best when the images show the same place, object, or document from comparable angles.

{% include images/juxtapose.html
  image1="images/sample-archive-photo.jpg"
  image2="images/sample-second-photo.jpg"
  caption="Replace this with a caption that explains what readers should notice in the comparison."
%}

## AI-Archive Comparison

Use this section if your course assignment asks you to compare an AI-generated history with archival evidence. Be specific:

- Quote one AI claim that the archive confirmed.
- Quote one AI claim that was wrong, vague, or impossible to verify.
- Name one thing the AI missed because it was not in digitized public sources.
- Explain what this taught you about AI as a historical research tool.

## Why This History Matters

End by returning to the present. How should readers see this campus place, person, organization, object, or event differently after reading your essay?

{% capture bibliography %}
- Replace this with a book, article, archival collection, or digital source.
- Replace this with another source.
- Replace this with another source.
{% endcapture %}

{% include typography/bibliography.html
  title="Bibliography"
  content=bibliography
%}
