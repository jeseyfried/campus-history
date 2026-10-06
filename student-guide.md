---
title: Student Publishing Guide
layout: wide
date: 2026-08-04
permalink: /student-guide/
---

# Student Publishing Guide

This page explains how to turn a course assignment into a working page on the Campus History site. Your course syllabus explains the assignment, grading, due dates, and reflection requirements. This guide only covers the site workflow: making a page, adding images, checking metadata, and submitting your work for publication.

## Before You Start

- Create or sign in to a [GitHub](https://github.com/) account.
- Choose a topic according to your course assignment.
- Check with your instructor before duplicating a topic already claimed by another student.
- Open the [Campus History repository](https://github.com/amaranth-unm/campus-history).
- Keep the [code samples page](../code/) open for image, carousel, pullquote, and bibliography snippets.

## Fork the Repository

In GitHub, a fork is your own copy of the Campus History repository. You can edit your fork without changing the public site until you are ready.

1. Go to the [Campus History repository](https://github.com/amaranth-unm/campus-history).
2. Click `Fork` in the upper-right corner.
3. Keep the default settings and click `Create fork`.
4. After GitHub creates the fork, make sure the URL includes your GitHub username.

Bookmark two pages:

- Your repository: `https://github.com/YOUR-USERNAME/campus-history`
- Your preview site, once GitHub Pages is enabled: `https://YOUR-USERNAME.github.io/campus-history`

## Preview Your Work

Your fork can generate its own preview version of the website. Use that preview to check page content, links, images, and formatting before submitting. Fork previews can behave a little differently from the public Campus History site because they live under your GitHub username, so do not change `_config.yml` or site-wide settings unless your instructor specifically tells you to.

1. In your fork, click `Settings`.
2. Click `Pages` in the left sidebar.
3. Under `Build and deployment`, choose `Deploy from a branch`.
4. Select the `master` branch and the `/root` folder.
5. Click `Save`.
6. Wait a minute or two, then return to `Settings` > `Pages` and open the published site link.

GitHub Pages takes about a minute to rebuild your site and show your latest changes. 


## Start From a Starter Essay

All essays live in the `essays` folder. Each essay has its own folder and an `index.md` file inside that folder. The easiest way to begin is to copy one of the starter essay folders and rename it for your topic.

Use one of these:

- `starter-essay-simple` — best for most essays. Includes a basic structure, one image, captions, an AI-archive comparison section, and a bibliography.
- `starter-essay-advanced` — use this if you want optional components like a pullquote, image grid, and before/after image slider.

Do not edit the starter folder directly. Copy it first, then rename the copy.

If you are using GitHub's web code editor, open your fork and press `.` to launch the editor. Then copy the starter folder inside `essays`, paste it in the same `essays` folder, and rename the copied folder with your topic name.

Your copied folder should be named like this:

```text
essays/mesa-vista-hall
```

Folder names must be:

- all lowercase
- hyphenated instead of spaced
- short but recognizable
- exactly the same wherever you refer to them

Good folder names look like `mesa-vista-hall`, `maxwell-museum`, or `duck-pond`.

Inside your copied folder, keep the file named `index.md`. Your folder should now look something like this:

```text
essays/mesa-vista-hall/index.md
essays/mesa-vista-hall/images/sample-archive-photo.jpg
```

## Customize the Metadata

Every essay begins with metadata between two lines of three hyphens. The directory, homepage cards, and page header use this metadata, so fill it out carefully.

```markdown
---
title: Mesa Vista Hall
author: Your Name
layout: essay
date: 2026-11-12
header-title: Mesa Vista Hall
category: Dormitory
popup-teaser: A one-sentence teaser for the map or directory.
card-description: A two-sentence description that helps readers decide to open your essay.
card-image: /essays/mesa-vista-hall/images/example.jpg
header-image: images/example.jpg
---
```

When you copy a starter essay, replace the starter metadata with your own information. Pay especially close attention to:

- `title`
- `author`
- `header-title`
- `category`
- `popup-teaser`
- `card-description`
- `card-image`
- `header-image`
- `start`

The `card-image` path starts from the root of the site, so it should include your essay folder name: `/essays/mesa-vista-hall/images/example.jpg`.

The `header-image` path starts from inside your essay folder, so it usually looks shorter: `images/example.jpg`.

Use one of these preferred categories when possible:

- `Academic Building`
- `Administration`
- `Arts Venue`
- `Athletics`
- `Campus Services`
- `Classroom Building`
- `Dining`
- `Dormitory`
- `Historic Building`
- `Landscape`
- `Museum`
- `Office`
- `Public Art`
- `Student Resource`

The current Campus History directory is generated from essay metadata. You do not need to update a separate spreadsheet for the public directory unless your instructor gives you a separate course-specific sheet.


## Add Images

The starter essay already includes an `images` folder with sample images. Replace those sample images with your own images from the archive, or upload additional images to the same folder.

Your folder should look like this:

```text
essays/mesa-vista-hall/index.md
essays/mesa-vista-hall/images/mvh-construction.jpg
essays/mesa-vista-hall/images/mvh-today.jpg
```

Image paths must match exactly, including capitalization, spaces, punctuation, and file extension. `mvh.jpg`, `MVH.jpg`, and `mvh.jpeg` are three different filenames.

### How big should images be?

Save images **at least 768 pixels wide**, and closer to **1500 pixels** if the archive gives you the option. The text column is 768 pixels, so anything narrower gets stretched to fit and looks blurry on the page. Downloading the largest version a digital collection offers is almost always the right move — the site will scale it down cleanly, but it cannot invent detail that is not in the file.

Before/after sliders are stricter. Both images should be at least 768 pixels wide **and roughly the same shape**, because the slider is sized from the first image and crops the second one to match. Two landscape photographs work well; a tall document paired with a wide photograph will get its top and bottom cut off.

If the only scan you can find is small, use it and say so in your pull request rather than stretching it — a note about a low-resolution source is more useful than a blurry image.

Use the Campus History image include instead of regular Markdown image syntax:

{% raw %}
```markdown
{% include images/figure.html
  class="img-center"
  width="100%"
  caption="Construction of Mesa Vista Hall in 1950. This image shows how the building was originally framed as a residential solution for postwar enrollment growth. Source: Center for Southwest Research, collection and box information."
  image-path="images/mvh-construction.jpg"
%}
```
{% endraw %}

Captions should explain why the image matters, not just identify what is in the picture. Include a source, box number, collection name, or link whenever possible.

## Use Site Components

The [code samples page](../code/) shows the current snippets for:

- headings
- figures
- image grids
- carousels
- before/after image sliders
- pullquotes
- footnotes
- bibliography drawers

Copy snippets from that page rather than inventing your own HTML. The site is built to keep student essays visually consistent, and the snippets do most of that work for you.

## Check Your Page

Before submitting, open your preview site and check:

- Your essay page loads at `/essays/your-folder-name/`.
- The page title, author, card description, and category are correct.
- Your header image and card image appear.
- Every image in the essay appears.
- Captions are informative and include source information.
- Links go where you expect.
- The bibliography is readable.
- The essay has subheadings and is easy to skim.
- The first paragraph gives readers a clear entry point into the story.

## Submit a Pull Request

When your page is ready, send your work back to the main Campus History repository with a pull request.

1. Go to your fork on GitHub.
2. Click `Contribute` or `Pull requests`.
3. Click `Open pull request` or `New pull request`.
4. Review the list of changed files.
5. Make sure you are only submitting your essay folder and related images unless your instructor told you otherwise.
6. Click `Create pull request`.
7. Add a short note with your name, course, and topic.

After that, your instructor can review the page and merge it into the public Campus History site.
