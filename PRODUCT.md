# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Two audiences, weighted equally:

- **Game studio hiring managers, recruiters and UI leads** screening Maurice Birchard for a full-time game UI/UX role. They skim fast, judge craft from the first screen, and look for evidence of process as well as polish.
- **Indie teams and studios hiring for contract UI work.** They want proof that he can take a HUD or menu system from wireframe to a working in-engine build without hand-holding.

Both arrive mostly from itch.io, LinkedIn, GitHub or a direct link in an application.

## Product Purpose

A personal portfolio for Maurice Birchard, a systems/SCADA engineer moving into game UI/UX design and development. It exists to win interviews and contract work by showing case studies, a resume and playable work. Success is a visitor reaching a case study, understanding the process behind it, and making contact or opening the resume.

## Positioning

**He designs and ships.** Work goes from Figma wireframes to working builds in Unity (uGUI), Godot and TypeScript, so designs account for how the engine actually behaves (canvas rebuilds, raycast blocking, theme assets for reskins). The industrial HMI background (operator screens for solar plants, Controls/HMI work at Amazon and Microsoft) supports this: readability under pressure and mapping state before drawing screens.

## Operating Context

- Visitors read case studies ("case files") that walk through scope, wireframe directions, findings, engine constraints and outcome.
- Some case studies embed live work: Greywater includes a working title menu (`assets/js/greywater-menu.js`); Shopping List embeds a prebuilt Figma Make React prototype (`work/shopping-list-prototype/`).
- Playable games live on itch.io (moninja.itch.io), linked from the nav and hero.
- Contact runs through email, LinkedIn, GitHub and itch.io, plus a contact page.

## Capabilities and Constraints

- Hand-built static site: HTML, one stylesheet (`assets/css/style.css`), a little vanilla JS. No build step for the site itself.
- Hosted on GitHub Pages (`.nojekyll`, files served as-is). Keep paths relative and URLs stable.
- Pages: home, about, resume (with PDF), contact, 404, and five case studies under `work/`.
- Images are WebP in `assets/img/<project>/`; no image converter is installed locally.
- **`mork-os/` is out of scope.** Its home and privacy pages document a separate personal assistant's read-only Google access. Leave their content, look and URLs alone during portfolio design work.

## Brand Commitments

- Name: Maurice Birchard; handle Moninja / moninja92. "MB" brand mark and existing favicon.
- Voice: plain, direct, first person, practical. Explains decisions and trade-offs without hype.
- Established terminology in case studies, e.g. Project Titan's FOCUS / BEAT design vocabulary and the phase-state matrix.

## Evidence on Hand

- Case studies: Project Titan (UI/UX lead, Unity uGUI, team project), Greywater (Figma UI system, first-person narrative game), Midas: The Accursed King (Godot, GBJam 14, all programming and story), Dreamland Timeline (TypeScript data UI fed from a spreadsheet), UI Explorations / Shopping List (paper sketch to Figma prototype).
- Screens and process images in `assets/img/`; resume at `assets/Maurice-Birchard-Resume.pdf`.
- Background: SCADA engineer in solar energy (Ignition, Wonderware), Controls SME at Microsoft, Controls and HMI systems UI/UX at Amazon; BS in Computer Science (Cybersecurity focus), CSU Global.
- **No testimonials, client logos, shipped commercial game credits or metrics exist.** Do not invent them.

## Product Principles

1. Show the build, not just the picture: prefer live, playable or in-engine evidence over static mockups.
2. Process is the proof: every case study shows how a decision was reached (scope, alternatives, findings, constraints).
3. Respect the skim: a hiring manager should grasp who he is and what he does from the first screen and each card.
4. Truthful scope: state his role on team projects precisely and claim nothing he did not do.
5. The HMI background is a supporting asset, framed as why his game UI reads clearly, not as a career pivot apology.
