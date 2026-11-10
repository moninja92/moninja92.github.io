# Maurice Birchard: Game UI/UX Portfolio

Hand-built static site (HTML, CSS, a little JavaScript). No build step: the files in the repo are what GitHub Pages serves.

## Structure

```
index.html                 Home: the booklet cover, Contents and chapter index
about.html                 About and service record
resume.html                Resume (HTML, with the PDF to download)
contact.html               Contact
work/argos.html            Chapter 01
work/project-titan.html    Chapter 02
work/greywater.html        Chapter 03 (includes a live title menu)
work/midas.html            Chapter 04
work/dreamland.html        Chapter 05
work/shopping-list.html    Chapter 06 (embeds the prototype below)
work/shopping-list-prototype/   Built Figma Make prototype (React, prebuilt)
assets/css/style.css       Theme ("Instruction Booklet"; see DESIGN.md)
assets/css/greywater-menu.css   The Greywater game's own menu styles, used only on its page
assets/js/                 Screen Guide callouts, tab bar, copy email, Greywater menu
assets/fonts/              Self-hosted fonts (SIL Open Font License, licences included)
assets/img/                Project images (WebP); each .webp.json notes where the image came from
tools/build_pages.py       Optional: rebuilds the pages so shared parts stay identical
404.html                   Not found page
.nojekyll                  Tells GitHub Pages to serve files as-is
mork-os/                   Separate project pages (not part of the portfolio design)
```

## Editing pages

The pages share their chapter tabs, header, back cover and Screen Guide markup. To change those everywhere at once, edit `tools/build_pages.py` and run:

```
python tools/build_pages.py .
```

It rewrites the portfolio pages (not `mork-os/` or the prototype). Small edits straight to a page's HTML are fine too, but copy them into the script as well, or the next run will undo them.
