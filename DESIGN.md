---
name: Maurice Birchard, Instruction Booklet
description: A game UI portfolio set as a 1990s game instruction booklet, with a process-blue cover, chapter thumb tabs and Screen Guide spreads.
colors:
  stock: "#EEF1F4"
  stock-shade: "#E0E5EA"
  rule: "#C4CBD3"
  ink: "#121316"
  ink-soft: "#44474E"
  paper-white: "#FFFFFF"
  cover-blue: "#1450C8"
  cover-blue-deep: "#0E3C9C"
  on-cover-soft: "#D3DEF8"
  chapter-argos-green: "#0E7A45"
  chapter-titan-red: "#C22B22"
  chapter-greywater-magenta: "#A61F60"
  chapter-midas-yellow: "#F2B705"
  chapter-dreamland-blue: "#006AA3"
  chapter-explore-orange: "#B04A0E"
typography:
  display:
    fontFamily: "Schibsted Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(2.6rem, 7.4vw, 5.75rem)"
    fontWeight: 900
    lineHeight: 0.92
    letterSpacing: "-0.02em"
  chapter-numeral:
    fontFamily: "Schibsted Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(4.5rem, 13vw, 10rem)"
    fontWeight: 900
    lineHeight: 0.8
    letterSpacing: "-0.04em"
  headline:
    fontFamily: "Schibsted Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(1.6rem, 3vw, 2.25rem)"
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: "-0.01em"
  title:
    fontFamily: "Schibsted Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.2rem"
    fontWeight: 800
    lineHeight: 1.25
  lede:
    fontFamily: "Schibsted Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(1.1rem, 1.6vw, 1.3rem)"
    fontWeight: 400
    lineHeight: 1.5
  body:
    fontFamily: "Schibsted Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.6
  caption:
    fontFamily: "Schibsted Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.9rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Schibsted Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.82rem"
    fontWeight: 800
    letterSpacing: "0.05em"
rounded:
  none: "0"
  disc: "50%"
spacing:
  gutter: "clamp(16px, 4vw, 48px)"
  section: "clamp(40px, 6vw, 72px)"
  rail: "60px"
  max: "1180px"
  plate-mat: "8px"
  thumb-mat: "5px"
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper-white}"
    rounded: "{rounded.none}"
    padding: "12px 22px"
    height: "48px"
  button-quiet:
    backgroundColor: "{colors.stock}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "12px 22px"
    height: "48px"
  button-on-cover:
    backgroundColor: "{colors.paper-white}"
    textColor: "{colors.cover-blue-deep}"
    rounded: "{rounded.none}"
    padding: "12px 22px"
  button-on-cover-hover:
    backgroundColor: "{colors.chapter-midas-yellow}"
    textColor: "{colors.ink}"
  thumb-tab-rail:
    backgroundColor: "{colors.stock-shade}"
    width: "{spacing.rail}"
  thumb-tab-mobile:
    backgroundColor: "{colors.stock-shade}"
    height: "62px"
  callout-disc:
    textColor: "{colors.paper-white}"
    rounded: "{rounded.disc}"
    size: "30px"
  plate:
    backgroundColor: "{colors.ink}"
    padding: "{spacing.plate-mat}"
    rounded: "{rounded.none}"
  note:
    backgroundColor: "{colors.paper-white}"
    textColor: "{colors.ink}"
    padding: "18px 22px"
    rounded: "{rounded.none}"
  back-cover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper-white}"
  skill-chip:
    textColor: "{colors.ink}"
    padding: "4px 10px"
    rounded: "{rounded.none}"
---

# Design System: Maurice Birchard, Instruction Booklet

## Overview

**Creative North Star: "The Instruction Booklet"**

The site is printed matter from a 1990s game box: a coated, cool-white booklet in black ink, with a process-blue cover, numbered chapters and coloured thumb tabs cut into the right edge. Every project is a chapter. Each chapter opens on a full-bleed band in its own process colour, then a spec strip, then a Screen Guide: the real UI shown large on a black mat, every element pinned, numbered and explained in a legend beside it. The page carries running heads and folios ("Chapter 02 · page 8") the way a manual does.

Density is manual-like, not gallery-like: text sits in tight, ruled lists separated by 2px ink rules and 1px hairlines, and size carries volume instead of extra families or decoration. One family, Schibsted Grotesk, does everything. Black Italic uppercase is the booklet's shout, used for covers, chapter titles and a few labels. Running text stays regular and sentence case.

Colour is flat, opaque process ink. There are no gradients, glass or glow on site surfaces. Depth is printed, made from ink mats, rules and one soft drop shadow under the cover art. The world explicitly refuses the dark thumbnail grid and the cream editorial portfolio.

**Key Characteristics:**
- Cool coated stock (#EEF1F4 family), never cream; black ink type and rules.
- One process colour per chapter, carried by the `--chapter` / `--on-chapter` pair through tabs, openers, discs, list markers, underlines and page-turn links.
- Schibsted Grotesk only; Black Italic for volume, regular for reading.
- Screen Guide spreads: real screens on an ink mat with pins, hairline leader lines and numbered gutter discs linked to a legend.
- Square corners everywhere; the only round shapes are callout discs and pins.
- One motion moment: leader lines draw in once when a Screen Guide enters view.

## Colors

Flat process inks on cool coated stock: one drenched cover blue, six chapter colours, and black.

### Primary
- **Process Cover Blue** (`cover-blue`): drenches the home cover, is the brand `theme-color`, and the text selection colour. It belongs to the cover; inside chapters it appears only as selection.
- **Deep Cover Blue** (`cover-blue-deep`): text colour of the white button on the cover.
- **Cover Mist** (`on-cover-soft`): secondary text on the cover (lede, wordmark subtitle, folio, Contents leaders and page numbers, cover-art captions).

### Secondary: chapter tabs
Each chapter owns one process colour, applied by a chapter class that sets `--chapter` and `--on-chapter`.
- **Argos Green** (`chapter-argos-green`), on white. Chapter 01. Also used for the copy-email success message.
- **Titan Red** (`chapter-titan-red`), on white. Chapter 02.
- **Greywater Magenta** (`chapter-greywater-magenta`), on white. Chapter 03.
- **Midas Yellow** (`chapter-midas-yellow`), on **ink**. Chapter 04, and the only chapter colour that takes dark text. It is also the cover's hover accent (cover button hover, Contents underline, back-cover email underline and link hover).
- **Dreamland Blue** (`chapter-dreamland-blue`), on white. Chapter 05.
- **Explorations Orange** (`chapter-explore-orange`), on white. Chapter 06.
- **Back matter** uses `ink` as its chapter colour, on white: About, Resume, Contact, the home body and the 404.

### Neutral
- **Coated Stock** (`stock`): page background.
- **Stock Shade** (`stock-shade`): the tab rail and mobile tab bar ground, `.term` chips, scrollbar track.
- **Hairline Grey** (`rule`): 1px dividers inside legends, career lists, contact links.
- **Booklet Ink** (`ink`): text, 2px rules and borders, plate and thumbnail mats, primary buttons, and the Contact tab.
- **Soft Ink** (`ink-soft`): secondary text, captions, folios, spec labels, legend descriptions.
- **Paper White** (`paper-white`): note boxes, contact card, on-chapter text, text on ink.

### Named Rules
**The One Chapter Ink Rule.** A page wears exactly one chapter colour, set once on `body` (or a wrapper) through `--chapter` / `--on-chapter`. Components never hard-code a chapter hex; they read the variable. Tabs and page-turn links set their own chapter class because they point to other chapters.

**The Cover Owns The Blue Rule.** Process blue is the cover. It is never a chapter colour and never a section background inside a chapter.

**The Midas Takes Ink Rule.** Yellow is the only chapter fill with dark text. Any new chapter colour must hold at least 4.5:1 against its on-colour.

## Typography

**Display Font:** Schibsted Grotesk (with Helvetica Neue, Arial, sans-serif)
**Body Font:** Schibsted Grotesk (same stack)

**Character:** One grotesk at many weights, like a manual set from one family. Black Italic (900 italic) is the voice of the box art; regular 400 is the voice of the instructions. Loaded weights: 400, 600, 700, 800, 900, italic 800 and 900.

### Hierarchy
- **Display** (900 italic, uppercase): page titles in chapter openers and the cover headline. The cover headline runs slightly smaller (clamp(2.6rem, 5.4vw, 5.25rem)).
- **Chapter numeral** (900 italic, tabular figures): the giant chapter number beside the opener title.
- **Headline** (800 italic): section h2s in prose. Guide titles, section heads, Contents, the back cover and resume headings step up to 900 italic.
- **Title** (800): h3s. Entry titles on the home Chapters list are 900 italic uppercase at clamp(1.4rem, 2.8vw, 2rem); note and fact titles are 900 italic at about 1.1 to 1.2rem.
- **Lede** (400): one paragraph under each display title, max 60ch.
- **Body** (400, 17px, 1.6): prose capped at 68ch; legend descriptions run at 0.97rem in soft ink.
- **Caption** (0.9rem, soft ink): plate and figure captions, max 70ch.
- **Label** (800, 0.82rem, uppercase, 0.05em tracking): spec-strip terms (Role, Engine, Team, Status) only.

### Named Rules
**The Size Carries Volume Rule.** Hierarchy comes from size and the 400 to 900 weight jump within one family. Never add a second family to the site.

**The Black Italic Shout Rule.** Uppercase is allowed only for: display titles, the wordmark name, home Chapters entry titles, page-turn chapter names, pending-plate titles, and spec-strip terms. Everything else, including h2, h3, body, buttons and captions, stays sentence case.

**The Tabular Folio Rule.** Every number that behaves like a page or chapter number (tabs, Contents, chapter numerals, callout discs, dates) uses tabular figures.

Fonts are self-hosted from `assets/fonts/` (woff2, latin and latin-ext subsets, SIL OFL 1.1 with licences alongside), with the upright and italic latin files preloaded. Body text is set in rem so it follows the reader's default font size.

## Layout

A centred column (`max` 1180px) with a fluid `gutter` on each side. On desktop (1000px and wider) the body reserves a 60px right margin for the fixed thumb-tab rail. Below 1000px the rail becomes a fixed bottom bar and the body reserves 64px at the bottom.

Pages follow the booklet order. Home: cover (blue; wordmark, About and Resume links and folio in the top row; headline and cover art in an 11:13 grid with Argos leading and Titan and Greywater following in chapter order; Contents below; on phones the headline comes first and only the Argos screen shows), then a sample Screen Guide, a Chapters index, a one-line aside linking to About, and the back cover. Chapter pages: running head (wordmark left; About and Resume links and folio right; 2px ink rule below), chapter opener band, spec strip, Screen Guide, prose sections, page-turn links, back cover.

Vertical rhythm is the `section` padding at top and bottom; consecutive sections drop their top padding. Screen Guide spreads are a 7:5 grid (plate left), or 5:7 for portrait screens with the plate capped at 420px and pushed to the gutter.

Responsive rules:
- **1000px and wider:** vertical thumb-tab rail of seven tabs, each showing its number and name. Only on screens 700px tall or shorter do tabs drop to the number (or the mail icon) with the name as a flyout label on hover and focus.
- **Below 1000px:** a fixed 60px bottom bar that always fits: the six chapter numbers (names kept for screen readers) and a wider Contact tab with its mail icon and label.
- **860px and below:** the cover stacks with the art first (square collage); Screen Guide spreads stack; gutter discs and leader lines are hidden and the pins grow to 22px numbered discs, so the plate and the legend still match by number.
- **760px and below:** Chapters entries collapse to tab plus text, with the thumbnail full width below; the back cover stacks.
- **640px and below:** the opener numeral sits above the title.
- **560px and below:** folios hide, page-turn links stack, career rows stack.

## Elevation & Depth

The booklet is flat and printed. Depth comes from ink mats (8px on plates, 5px on thumbnails, 6px on cover art), 2px ink rules and borders, and colour fields, not from shadows. There is exactly one ambient shadow on the site, under the tilted cover-art screens, so they read as prints laid on the cover. All other shadows are rings: an inset double ring marks the current tab, a 1px ink ring outlines each pin, and a faint white halo keeps leader lines visible over dark screens.

### Shadow Vocabulary
- **Cover print drop** (`box-shadow: 0 24px 50px -12px rgba(0, 0, 0, 0.5)`): cover-art figures only.
- **Current tab ring** (`box-shadow: inset 0 0 0 3px var(--stock), inset 0 0 0 5px var(--chapter)`): the `aria-current` thumb tab.
- **Pin outline** (`box-shadow: 0 0 0 1px var(--ink)`): plate pins.
- **Leader halo** (`box-shadow: 0 0 0 1px rgba(255,255,255,0.75)`): leader lines.

### Named Rules
**The Printed Depth Rule.** Nothing lifts off the page except the cover prints. Never use hard offset shadows (solid, unblurred, x/y offset); they belong to a different world. Separate with rules, mats and colour fields.

## Shapes

Square corners throughout (`rounded.none`): buttons, tabs, plates, notes, cards, chips, page-turn links and pending plates. The only curves are the callout discs and pins (`rounded.disc`). Borders are 2px ink for structure (rules, notes, buttons, figures, chips) and 1px `rule` hairlines inside lists. On the cover, a 1px white rule at 18% opacity, inset 14px, frames the cover like a print registration border. Cover-art prints sit at slight angles (−1.5°, 1.2°, −0.8°) and straighten on hover.

## Components

### Buttons
Blunt, inked and square.
- **Shape:** square (0), 2px border, at least 48px tall, 800 weight, optional 16px inline SVG arrow.
- **Primary:** ink fill, white text. Hover fills with the page's chapter colour and its on-colour.
- **Quiet:** transparent with ink text and border. Hover inverts to ink.
- **On cover:** white fill, deep cover blue text. Hover turns Midas yellow with ink text.
- **In openers:** on-chapter fill with chapter-colour text. Hover goes transparent; the quiet variant inverts.
- **Focus:** 3px ink outline, 3px offset (global). It turns white on the blue front and back covers, takes the on-chapter colour on chapter openers, and sits 7px inside each thumb tab in the tab's own text colour.

### Navigation: thumb tabs
The site navigation is the booklet's thumb-cut edge. There are seven tabs: chapters 01 to 06, then Contact in ink with a mail icon. About and Resume are back matter: they sit as plain links in the running head and on the back cover, not on the thumb edge. Each tab is a solid block of its chapter colour, 800 weight, with a 900 italic number. On the desktop rail, tabs are vertical text, fill equal heights with 2px gaps, sit 6px off the edge and slide in on hover, focus or current. The current tab also gets the inset double ring. On mobile the tabs form a 62px horizontal bar with a 2px ink top rule, number over name, scrolling sideways.

### Cover
A process-blue field with the registration rule. The top row holds the wordmark (900 italic uppercase name plus "Game UI / UX") and a folio. Below are the Display headline, the lede, one white button, and the cover art: three real screens on ink mats, tilted, captioned "NN Chapter, screen" and linked to their chapters.

### Contents
A booklet contents page on the cover: a 2px white top rule and a grid of entries in a 900 italic number, chapter name, dotted leader and page number layout, with 1px white hairlines at 22% between rows. Page numbers match the folios printed in each chapter's running head.

### Chapter opener and specs
A full-width band in the chapter colour. It holds the giant chapter numeral, the Display title, the lede and optional buttons. Back-matter openers (About, Resume, Contact, 404) are set on the paper stock instead, ink on stock with a 2px ink rule below, and have no numeral. Below it sits the spec strip: a definition list between 2px ink rules, auto-fit columns of uppercase label over a 600-weight value.

### Screen Guide (signature)
- **Title bar:** 900 italic h2 "Screen Guide: …" with a soft-ink note on the right, over a 2px ink rule.
- **Plate:** the real screenshot on an 8px ink mat (pixel art uses `image-rendering: pixelated`).
- **Pin:** a 12px chapter-colour dot with a 2px white border and ink ring, placed with `--x` and `--y` percentages.
- **Leader line:** a 1.5px ink hairline from the pin to the gutter, with a white halo.
- **Gutter disc:** a 30px numbered chapter-colour disc with a 2px ink border, 30px into the gutter, 900 italic tabular number.
- **Legend:** an ordered list of disc, bold name and soft-ink description, separated by hairlines. Rows are plain list items, not tab stops; the text already names each element.
- **Linking:** hovering a legend row, pin or disc lights every part with the same number and fades the rest of that guide to about 20% (legend rows to 45%). The active disc scales up with a ring in the chapter colour, the leader line thickens to 3px, and the legend name gets a 3px chapter-colour underline. The plate takes about two thirds of the spread on landscape guides.
- **Motion:** leader lines start at `scaleX(0)` and draw in once (0.9s, expo-out) when 35% of the guide is visible. With no JS they are drawn from the start. With reduced motion they fade in instead of drawing, and hover movement (tab slide, plate lift, thumbnail zoom, disc scale) is dropped while colour feedback stays.

### Page-turn links
Two blocks with a 2px gap at the end of each chapter. Each is in the colour of the chapter it leads to, with a small "Previous" or "Next" and a 900 italic uppercase "NN Name". Next aligns right. They stack below 560px.

### Notes and terms
A note is a white box with a 2px ink border: a 900 italic title with a 22px inline SVG icon in the chapter colour, then body text. Terms of art (FOCUS, BEAT) are set 900 italic on a stock-shade chip. On screens 1400px and wider, notes inside prose move into the outer margin as a sidebar: no box, a 4px chapter-colour rule on top.

Case-study prose headings carry chapter.section numbers (2.1, 2.2 and so on) in the chapter colour, hanging in their own column so wrapped headings stay aligned. Back matter has no section numbers.

### Facts
A three-column evidence strip under a 2px ink rule: 900 italic title and a short soft-ink paragraph. Plain statements only.

### Chapters index (home)
Ruled rows between 2px ink rules. Each row has a 92px chapter-colour tab with a 900 italic number, an uppercase italic title, a description, an 800-weight meta line (role · engine · context) and a 16:9 thumbnail on a 5px ink mat. On hover the thumbnail zooms to 1.04 and the title gets a 4px chapter-colour underline.

### Back cover
The footer is the booklet's back cover: a process-blue field matching the front cover with a 900 "Contact" heading, the email with a Midas-yellow underline, an availability line, a list of links with arrows separated by 1px translucent white hairlines, and a colophon.

### Pending plates (honest "coming soon")
When a screen has not been captured, its slot is a dark slate panel (#1B1D22) with a 2px dashed inner outline (#5A5E66, inset 10px). It holds a 900 italic uppercase title and "Screenshot coming soon", marked `role="img"` with an honest label. It keeps the aspect ratio of the image it stands in for. It never shows a mock or stand-in image presented as real.

### Exhibit exception: Greywater live menu
`assets/css/greywater-menu.css` styles Greywater's own in-game title menu, rebuilt from its Figma component and loaded only on `work/greywater.html`. It is an exhibit, not part of this system: its IBM Plex Mono and Newsreader type, warm paper panel, glow shadow, side selection bar and tracked uppercase chapter label belong to Greywater's world. Never reuse them on site surfaces, and never treat them as evidence for site rules.

## Do's and Don'ts

### Do:
- **Do** set one chapter class per page and let every accent read `--chapter` / `--on-chapter`.
- **Do** show real screens on ink mats, and annotate signature screens as a Screen Guide with pins, leader lines, gutter discs and a linked legend.
- **Do** use a pending plate ("Screenshot coming soon") when a real capture is missing.
- **Do** keep running heads and folios consistent with the Contents page numbers.
- **Do** separate content with 2px ink rules and 1px hairlines instead of cards and shadows.
- **Do** keep the leader-line draw-in as the only entrance animation, and swap it for a fade under `prefers-reduced-motion`.
- **Do** keep claims truthful: roles, engines and status stated exactly. No invented metrics, logos or testimonials.

### Don't:
- **Don't** use hard offset shadows or black drop boxes.
- **Don't** add eyebrow or kicker labels above headings. The only small uppercase label is the spec-strip term.
- **Don't** introduce a second typeface on site surfaces, or uppercase body, h2/h3 or button text.
- **Don't** use cream or warm paper as a site background, or a dark thumbnail-grid layout.
- **Don't** round corners on anything but discs and pins.
- **Don't** use process blue as a chapter colour or a background inside chapters.
- **Don't** borrow the Greywater exhibit's fonts, glow or selection bar for the site.
