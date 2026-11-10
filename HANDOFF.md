# Handoff: portfolio redesign ("Instruction Booklet")

Last updated 2026-11-10. Branch `redesign/new-visual-world`, 7 commits ahead of `main`. Nothing is merged or pushed.

## Where things stand

The portfolio has been rebuilt as a 1990s game instruction booklet:
- a blue cover with real screens and a Contents page;
- process-colour chapter tabs as the navigation (right-edge rail on desktop, bottom bar on phones);
- a "Screen Guide" (screenshot with numbered pins linked to a legend) opening every chapter.

Chapters:

| # | Page | Notes |
|---|---|---|
| 01 | `work/argos.html` | River Menu guide, Watch Pause and Journal captures (supplied by Maurice) |
| 02 | `work/project-titan.html` | HUD guide; the three grayscale directions and the state matrix (from Figma "Beginning Stage Design"); the Kaiju Cold War mockups as an "earlier pitch" block (from Figma "Project Titan Vertical Slice") |
| 03 | `work/greywater.html` | Live title menu plus HUD guide |
| 04 | `work/midas.html` | Dialogue guide |
| 05 | `work/dreamland.html` | Archive guide (the Timeline web tool) |
| 06 | `work/shopping-list.html` | Paper-prototype guide plus the embedded prototype |
| 07 | `work/dreamland-concept.html` | New: Dreamland game UI concept pass (from Figma "Dreamland") |

Back matter (`about.html`, `resume.html`, `contact.html`, `404.html`) sits on paper stock. The back cover (footer) is cover blue.

Commits on the branch, oldest first:
1. `36edd2c` the redesign;
2. `ae45c68` Argos screenshots;
3. `c95e5ac` audit fixes;
4. `f5b9d59` polish;
5. `d8d4a6e` critique fixes;
6. `6629b92` Kaiju Cold War frames;
7. `8ad3110` Titan's real directions and chapter 07.

Latest scores:
- **Audit:** 18/20, before the critique fixes and the Figma additions.
- **Critique:** 22/32 on 2026-11-10, before the critique fixes. The snapshots are in `.impeccable/critique/`. A fresh critique was started and interrupted, so the current score is unknown.

## How to work on it

- **The pages are generated.** Edit `tools/build_pages.py`, then run `python tools/build_pages.py .` from the repo root. The script overwrites every portfolio page (not `mork-os/` or the prototype). A hand edit to a page's HTML will be undone by the next run unless it is copied into the script.
- **Styles** live in `assets/css/style.css`. Greywater's in-game menu has its own `assets/css/greywater-menu.css`.
- **The design system** is described in `DESIGN.md` (with its sidecar `.impeccable/design.json`). Product facts are in `PRODUCT.md`. The direction contract is in `.impeccable/surfaces/index-html.md`.
- **Image origins:** every image has a `.webp.json` note saying where it came from. When you add an image, add one with `sh .claude/skills/impeccable/scripts/impeccable embed-prompt <file> --prompt-file <origin.txt>`. `embed-prompt --scan assets/img` must report 0 missing.
- **Fonts** are self-hosted in `assets/fonts/`, with their OFL licences.
- **Checks:** serve the site with `python -m http.server 8790 --bind 127.0.0.1`, then:
  - run `sh .claude/skills/impeccable/scripts/impeccable detect --json index.html about.html resume.html contact.html 404.html work/*.html`;
  - look at desktop (1440), a short laptop (1280×700) and a phone (390).
  - The remaining `cramped-padding` findings are known false positives: the inner `.wrap` supplies the inset.

## Open items

1. **Push and open a PR** to `main` when Maurice is happy with the branch.
2. **Re-run `/impeccable critique`** to score the redesign after the critique fixes and the Figma additions.
3. **Resume PDF:** `assets/Maurice-Birchard-Resume.pdf` still says "Bachelor of Science (Cybersecurity)". The site says Computer Science with a Cybersecurity focus, as Maurice confirmed. Maurice needs to update the PDF.
4. **Chapter 07 labels:** the specs strip says Role "UI/UX concept design" and Status "Concept". These were inferred, not stated in the Figma file. Confirm them with Maurice.
5. **Titan phase-state matrix:** Maurice chose to keep it as text only. The state-matrix board shown on the page covers component states, not the seven round phases.
6. **Argos "Figma vs Unity":** the Argos Figma work is in Make files (`Argos-Pause-Menu-and-Journal`, `River-Menu-Prototype`), which the Figma connector cannot export. Showing it needs screenshots from Maurice.
7. **Unused Figma links:** "UI-UX Presentation for Kaiju Cold War (Copy)" and "Integrate Markdown Support" are Make files and were not used.
8. **Small known items:**
   - Screen Guide highlighting works on mouse hover only; legend rows are no longer keyboard stops.
   - The contact page's YouTube handle is @MorkusGaming, which differs from the Moninja brand. Maurice's call.

## Gotchas

- **Port 8765 is taken** on this machine by another local server (it serves `ollama-guide.html`). Use 8790.
- **Full-page screenshots via CDP** (`captureBeyondViewport`) draw `position: fixed` elements (the tab rail and phone bar) only once, at the first viewport. They also show the rail's hidden flyout labels faintly. The live page is correct.
- **Short laptop screens:** the tab rail switches to numbers only with a flyout name at 700px tall or less. Long tab names are shortened on the rail ("Explore", "Concept") so all eight tabs fit at 900px tall.
- **The Figma "Project Titan Vertical Slice" file is actually the Kaiju Cold War pitch.** Titan's real three directions are in "Beginning Stage Design".
