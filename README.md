# Maurice Birchard: Game UI/UX Portfolio

Hand-built static site (HTML, CSS, a little JavaScript). No build step for the site itself.

## Structure

```
index.html                 Home
about.html                 About and service record
work/project-titan.html    Case file 01
work/greywater.html        Case file 02 (includes a live title menu)
work/midas.html            Case file 03
work/dreamland.html        Case file 04
work/shopping-list.html    Case file 05 (embeds the prototype below)
work/shopping-list-prototype/   Built Figma Make prototype (React, prebuilt)
assets/css/style.css       Theme ("Briefing")
assets/js/                 Nav toggle, Greywater menu
assets/img/                Project images (WebP)
404.html                   Not found page
.nojekyll                  Tells GitHub Pages to serve files as-is
```

## Before publishing

1. Add your resume as `assets/Maurice-Birchard-Resume.pdf`.
2. Replace `[YOUR-EMAIL]` and `[YOUR-LINKEDIN-URL]` in every page footer and on `about.html` (search the project for `[YOUR-`).

## Deploy to GitHub Pages

1. Create a public repo named `moninja92.github.io`.
2. Upload the contents of this folder to the repo root (not the folder itself).
3. In the repo: Settings > Pages > Source: Deploy from a branch, Branch: `main`, folder `/ (root)`.
4. The site goes live at https://moninja92.github.io/ within a minute or two.

Your existing Dreamland site at https://moninja92.github.io/dreamland-timeline/ keeps working; project sites live under the user site's address.

## Editing

Pages are plain HTML. To add a project, copy an existing file in `work/`, change the content, and add a card to the grid in `index.html`.
