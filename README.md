# UNM Campus Histories

**Spaces have histories, too.**

A student-driven digital history collaboration. UNM Campus Histories collects
student-built essays about the buildings, landscapes, public art, and everyday
places that shape university life at the University of New Mexico, turning
explorations of UNM's official archive into a shared public record.

Live site: <https://amaranth.unm.edu/campus-history/>

The project treats coursework as something that can outlast the semester.
Instead of Word documents discarded when the course ends, students publish
research that keeps circulating — and in the process learn version control,
collaborative editing, and scholarly publishing on open-source tools. The site
doubles as a model for how digital humanities projects can be public,
collaborative, and sustainable without servers, licences, or hosting costs.

## For students

Start here, in this order:

1. **[student-guide.md](student-guide.md)** — forking the repo, previewing your
   work, starting from a starter essay, adding images, opening a pull request.
2. **[code/](code/)** — copy-paste snippets for every site component: figures,
   image grids, carousels, before/after sliders, pull quotes, footnotes,
   bibliography drawers.

You do not need to be a programmer. If you can work with folders and files and copy and paste, you can do everything you need. Copy `essays/starter-essay-simple/` (or
`starter-essay-advanced/` if you want the fuller set of components), rename the
folder, and replace the contents.



## How the site is put together

```
essays/<folder>/index.md      one essay per folder, plus its own images/
essays/starter-essay-*/       templates students copy
_layouts/essay.html           essay pages: hero, prev/next arrows, content
_layouts/wide.html            full-bleed pages: homepage, directory, map
_includes/images/             figure, image-grid, carousel, juxtapose
_includes/nav/                directory, compact list, essay pagination
_includes/layout/             the shared page header
_data/homepage.yml            which essays appear in the homepage blocks
_data/home_quotes.yml         the rotating pull quotes on the homepage
assets/css/                   base, typography, page-header, home, map
scripts/                      one-off maintenance scripts, not part of the build
```

Top-level pages are `index.md` (homepage), `about.md`, `directory.md` (browse by
category), `all-essays.md` (browse by name), and `map.md` (essays plotted on a
campus map, driven by the KML files in `assets/kml/`).

### Essay front matter

An essay's front matter drives more than its own page. `card-description` and
`card-image` are what let it appear as a card in the directory, the map popups,
and the homepage; `category` places it in the browse-by-category strip and
supplies the eyebrow above the hero title; `header-image` and `header-caption`
build the hero. See `student-guide.md` for the full list.

Two conventions worth knowing:

- **`published: false`** removes an essay from the build entirely — no page, and
  it disappears from every listing, the map, and the prev/next chain. Used for
  drafts and for the Mesa Vista Hall demo essay.
- **`category: Starter Essay`** keeps the starter templates out of the
  prev/next navigation.

### Homepage curation

The Featured and Recommended blocks are curated in
[`_data/homepage.yml`](_data/homepage.yml) by essay folder name, in the order
they should appear. Adding an essay to the site does **not** put it on the
homepage — list it there. Entries that don't resolve, or that lack a
`card-description` or `card-image`, are skipped silently rather than rendered
broken.

## Deployment

GitHub Pages builds `master` automatically; there is no CI workflow in the repo.
`_config.yml` sets `permalink: pretty`, so pages build as directories
(`/directory/`, not `/directory.html`) and trailing-slash links work.

If a change doesn't appear on the live site, check that the Pages build actually
succeeded — a failed build leaves the previous version served with no visible
error:

```bash
gh api repos/amaranth-unm/campus-history/pages/builds/latest
```

## Credits

Essays are written by students at the
[University of New Mexico](https://www.unm.edu) and are credited by author on
each page. The project is produced in collaboration with the
[Amaranth Digital Humanities Studio](https://amaranth.unm.edu), whose domain
the site is published under.

The site is built on the
[Xanthan web framework](https://xanthan-web.github.io/), which supplies the
page-header system, the carousel and figure includes, and the layout
conventions essays are written against — the "Xanthan patterns" the style guide
asks you to use instead of ad hoc HTML.

Built with [Jekyll](https://jekyllrb.com) and hosted on GitHub Pages; the image
comparison sliders use [JuxtaposeJS](https://juxtapose.knightlab.com) and the
map uses [Leaflet](https://leafletjs.com).
