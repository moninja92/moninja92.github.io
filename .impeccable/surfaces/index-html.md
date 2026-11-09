---
version: 1
slug: "index-html"
primary_target: "index.html"
related_targets: ["about.html","resume.html","contact.html","404.html","work/project-titan.html","work/greywater.html","work/midas.html","work/dreamland.html","work/shopping-list.html"]
---

# Portfolio site (home + case studies + about/resume/contact)

Scope: whole portfolio redesign, replacing the "Briefing" theme. Mode: Experience (the work leads from the first viewport). mork-os/ is out of scope. URLs stay as they are; Argos gets a new page at work/argos.html.

Audience: studio UI leads/recruiters and contract clients, skimming. Job: grasp "game UI designer who ships in engine" in one screen, open a case study, then make contact.
Proof: real UI screens (Argos River Menu + Watch Pause, Titan HUD, Greywater live menu, Midas, Dreamland, Shopping List prototype). No invented metrics, logos or testimonials.
Constraints: static HTML/CSS/vanilla JS on GitHub Pages, no build step. Copy changes to facts get confirmed with Maurice.

## Direction contract

THESIS: The site is a 1990s game instruction booklet. Every project is a chapter whose opening is a Screen Guide: the UI shown large, each element numbered and explained. Refuses the dark thumbnail grid and the cream editorial portfolio.

OWN-WORLD: Cool coated booklet stock (not cream), black ink, process-colour chapter tabs (blue, red, green, yellow, magenta), one per project. Home cover drenched in process blue. Schibsted Grotesk only: Black Italic headers, regular body, size carries volume. Numbered callout discs with hairline leader lines. Page folios. No hard offset shadows, no black boxes.

STORY: The visitor opens the booklet, sees the best screens on the cover, reads a Contents with page numbers, and flips to a chapter. They come away believing Maurice designs UI and builds it in engine, and they find Contact on the back page.

FIRST VIEWPORT: Home is the booklet cover: blue field, title "Game UI, designed in Figma, shipped in engine." top left, a collage of three real screens (Argos, Titan, Greywater) as the cover art filling the right two-thirds, and a Contents block with page numbers linking to each chapter. Chapter thumb tabs run down the right edge as navigation; Contact is the last tab.

FORM: Instruction Booklet, my top-ranked grounded candidate (position 1), chosen over the assigned Show Floor. seed:234f9c04104f329c
Signature interaction: legend rows and image callouts are linked; hovering or focusing either one highlights its partner and draws the leader line.
Motion grammar: leader lines draw in once when a Screen Guide enters view; reduced motion shows them static.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
