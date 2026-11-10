"""Rebuild the portfolio pages from one source.

The site is plain static HTML with no build step: the pages in the repo are
what GitHub Pages serves. This script only exists so the shared parts (chapter
tabs, running header, back cover, Screen Guides) stay identical across pages.
Edit the page content below, then run from the repo root:

    python tools/build_pages.py .

It overwrites index.html, about.html, resume.html, contact.html, 404.html and
work/*.html (not mork-os/ or the shopping-list prototype). If you edit a page
by hand instead, copy the change here too, or the next run will undo it.
"""
import pathlib, sys
ROOT = pathlib.Path(sys.argv[1])

FONTS = '<link rel="preload" href="{p}assets/fonts/schibsted-grotesk-normal-400-900-latin.woff2" as="font" type="font/woff2" crossorigin>\n<link rel="preload" href="{p}assets/fonts/schibsted-grotesk-italic-800-900-latin.woff2" as="font" type="font/woff2" crossorigin>'
GW_FONTS = ''

EXT = '<svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 11 11 5M6 5h5v5"/></svg>'
ARR = '<svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'
MAIL = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4"><rect x="3" y="5" width="18" height="14"/><path d="m3 6 9 7 9-7"/></svg>'
NOTE = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4"><circle cx="12" cy="12" r="10"/><path d="M12 7v6M12 16.5v.5"/></svg>'

TABS = [
    ("argos", "01", "Argos", "work/argos.html", "4"),
    ("titan", "02", "Titan", "work/project-titan.html", "8"),
    ("greywater", "03", "Greywater", "work/greywater.html", "12"),
    ("midas", "04", "Midas", "work/midas.html", "16"),
    ("dreamland", "05", "Dreamland", "work/dreamland.html", "20"),
    ("explore", "06", "Explorations", "work/shopping-list.html", "24"),
    ("back", "", "About", "about.html", "28"),
    ("back", "", "Resume", "resume.html", "30"),
    ("back", "", "Contact", "contact.html", "32"),
]

def pending(label, note='Screenshot coming soon'):
    return f'<div class="pending" role="img" aria-label="{label}: {note.lower()}"><span>{label}</span><small>{note}</small></div>'

def argos(name, w, h, alt, label, p='', extra=''):
    """Real capture when it exists, an honest 'capture pending' plate otherwise."""
    f = ROOT / 'assets' / 'img' / 'argos' / f'{name}.webp'
    if f.exists():
        return f'<img src="{p}assets/img/argos/{name}.webp" width="{w}" height="{h}" alt="{alt}"{extra}>'
    return f'<div class="pending" role="img" aria-label="{label}: screenshot coming soon"><span>{label}</span><small>Screenshot coming soon</small></div>'

RAIL = TABS[:6] + [("back", "", "Contact", "contact.html", "32")]

def tabs(p, current):
    items = []
    for ch, num, name, href, _ in RAIL:
        cur = ' aria-current="page"' if href == current else ''
        n = f'<span class="num">{num}</span>' if num else f'<span class="num icon">{MAIL}</span>'
        label = f'<span class="visually-hidden">Chapter {num}: </span>' if num else ''
        cls = f'ch-{ch}' + ('' if num else ' tab-contact')
        items.append(f'    <li class="{cls}"><a href="{p}{href}"{cur}>{n}{label}<span class="name">{name}</span></a></li>')
    return '<nav class="tabs" aria-label="Chapters">\n  <ol>\n' + '\n'.join(items) + '\n  </ol>\n</nav>'

def backcover(p, minimal=False):
    if minimal:
        return '<footer class="backcover"><div class="wrap"><div class="colophon"><span>&copy; <span id="year">2026</span> Maurice Birchard</span><span>Hand-built in HTML and CSS. Set in Schibsted Grotesk.</span></div></div></footer>'
    return f'''<footer class="backcover">
  <div class="wrap">
    <div>
      <h2>Contact</h2>
      <a class="mail" href="mailto:mauricebirchard@gmail.com">mauricebirchard@gmail.com</a>
      <p>Open to game UI/UX, game design and software roles, full-time or contract. Based in Chandler, AZ, open to remote.</p>
    </div>
    <ul>
      <li><a href="{p}contact.html">All contact options {ARR}</a></li>
      <li><a href="{p}about.html">About {ARR}</a></li>
      <li><a href="{p}resume.html">Resume {ARR}</a></li>
      <li><a href="https://www.linkedin.com/in/mauricebirchard/" rel="noopener">LinkedIn {EXT}</a></li>
      <li><a href="https://github.com/moninja92" rel="noopener">GitHub {EXT}</a></li>
      <li><a href="https://moninja.itch.io/" rel="noopener">itch.io {EXT}</a></li>
    </ul>
    <div class="colophon"><span>&copy; <span id="year">2026</span> Maurice Birchard</span><span>Hand-built in HTML and CSS. Set in Schibsted Grotesk.</span></div>
  </div>
</footer>'''

def runhead(p, folio):
    return f'''<header class="runhead">
  <div class="wrap">
    <a class="wordmark" href="{p}index.html"><b>Maurice Birchard</b><span>Game UI / UX</span></a>
    <div class="runhead-end"><nav class="backlinks" aria-label="Back matter"><a href="{p}about.html">About</a><a href="{p}resume.html">Resume</a></nav><span class="folio">{folio}</span></div>
  </div>
</header>'''

def page(path, title, desc, body, current, chapter_class, folio=None, extra_head='', scripts='', extra_css=''):
    depth = path.count('/')
    p = '../' * depth
    head_runner = runhead(p, folio) if folio else ''
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta name="theme-color" content="#1450C8">
<link rel="icon" href="{p}assets/img/favicon.svg" type="image/svg+xml">
{FONTS.replace('{p}', p)}{extra_head}
<link rel="stylesheet" href="{p}assets/css/style.css">{extra_css}
</head>
<body class="{chapter_class}">
<a class="skip-link" href="#main">Skip to content</a>
{tabs(p, current)}
{head_runner}
<main id="main">
{body.replace('{P}', p)}
</main>
{backcover(p, minimal=(path=='contact.html'))}
<script src="{p}assets/js/main.js"></script>{scripts}
</body>
</html>
'''
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding='utf-8', newline='\n')

def guide(title, sub, img, w, h, alt, cap, points, portrait=False, pixel=False):
    cos = '\n'.join(f'      <span class="lead-line" data-n="{i+1}" style="--x:{x}%;--y:{y}%"></span><span class="pin" data-n="{i+1}" style="--x:{x}%;--y:{y}%" aria-hidden="true">{i+1}</span><span class="co" data-n="{i+1}" style="--x:{x}%;--y:{y}%" aria-hidden="true">{i+1}</span>' for i, (x, y, _, _) in enumerate(points))
    leg = '\n'.join(f'      <li data-n="{i+1}"><span class="co" aria-hidden="true">{i+1}</span><div><b><span class="visually-hidden">{i+1}. </span>{t}</b><p>{d}</p></div></li>' for i, (_, _, t, d) in enumerate(points))
    return f'''<section class="guide" aria-labelledby="guide-h">
  <div class="wrap">
    <div class="guide-title"><h2 id="guide-h">{title}</h2><p>{sub}</p></div>
    <div class="spread{' portrait' if portrait else ''}">
      <figure class="plate{' pixel' if pixel else ''}">
        <img src="{img}" width="{w}" height="{h}" alt="{alt}">
{cos}
      </figure>
      <ol class="legend" aria-label="Screen elements">
{leg}
      </ol>
    </div>
    <p class="plate-cap">{cap}</p>
  </div>
</section>'''

def opener(num, title, lede, buttons=''):
    chap = f'<span class="chap" aria-hidden="true">{num}</span>' if num else ''
    pre = f'<span class="visually-hidden">Chapter {num}: </span>' if num else ''
    return f'''<section class="opener">
  <div class="wrap{'' if num else ' solo'}">
    {chap}
    <div>
      <h1 class="display">{pre}{title}</h1>
      <p class="lede">{lede}</p>{buttons}
    </div>
  </div>
</section>'''

def specs(rows):
    inner = ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in rows)
    return f'<div class="wrap specs-wrap"><dl class="specs">{inner}</dl></div>'

def turn(prev, nxt):
    def a(t, cls, label):
        if not t: return '<span></span>'
        ch, num, name, href = t
        return f'<a class="{cls} ch-{ch}" href="{{P}}{href}"><small>{label}</small><b>{num + " " if num else ""}{name}</b></a>'
    return f'<nav class="turn" aria-label="Turn the page">{a(prev, "prev", "Previous")}{a(nxt, "next", "Next")}</nav>'

TITAN_POINTS = [
    (96, 3.0, "Commander portrait", "Shows whose turn it is, so the meter always has a face attached."),
    (36, 8.0, "Kaiju threat meter", "Every kill feeds this shared meter, with a countdown to the Kaiju's arrival. It makes the risk readable at a glance."),
    (80, 15.7, "Unit Inspector", "Explains the next step in plain words: select an ally, then click a reachable tile."),
    (84, 43.4, "Orders", "Attack, Hold, Defend and Retreat for the selected unit. They stay greyed until a unit is selected."),
    (84, 81, "Command seal", "Stamped with the faction's emblem. Translucent on hover, full opacity when pressed, lit once every unit has orders."),
]

GW_POINTS = [
    (3.8, 12.2, "Objective", "Top left, then fades to 40% after eight seconds. It returns when the objective changes or the player taps Q."),
    (50, 75.6, "Hold prompt", "The only element allowed to animate, which is what makes it readable at the edge of vision."),
    (77.5, 82.8, "Equipped item", "The oil lamp, with Tab to cycle and I for the satchel."),
    (6, 96.5, "Movement hint", "A keycap and a short verb. Shift to move quietly."),
]

MIDAS_POINTS = [
    (40, 30, "Scene", "The play area keeps the full four-tone palette, so the box below always reads as UI."),
    (34, 60.4, "Speaker", "The speaker's name sits on its own line above the text."),
    (73, 71.8, "Line", "Short lines in capitals, sized to stay legible at 160&times;144."),
    (81, 89, "Continue marker", "A small arrow says there is more to read."),
]
DL_POINTS = [
    (20, 13.9, "Records request", "Search across events, characters and years, with a keyboard shortcut to jump to it."),
    (10, 25, "Category filters", "Colour-coded, with live counts."),
    (34, 35, "Decade histogram", "Shows where history clusters at a glance."),
    (12.6, 49.7, "Entries by decade", "Each entry opens its own numbered case file."),
]
SL_POINTS = [
    (45, 12.6, "Home", "The only starting point."),
    (44.7, 52, "Numbered routes", "Seven numbered arrows connect five screens, so a reviewer can walk them step by step."),
    (23, 61.5, "Navigation flow", "A legend listing every route."),
    (40, 87, "Checked items", "Ticked items sink to the bottom of the list."),
]

# ---------------- Home ----------------
CONTENTS = '\n'.join(
    f'        <li><a href="{href}"><span class="n">{num}</span><span><b>{name}</b> <span class="lead" aria-hidden="true"></span></span><span class="pg"><span class="visually-hidden">page </span>{pg}</span></a></li>'
    for ch, num, name, href, pg in TABS[:6])

home = f'''<section class="cover" aria-labelledby="cover-h">
  <header class="wrap cover-top">
    <a class="wordmark" href="index.html" aria-label="Maurice Birchard, home"><b>Maurice Birchard</b><span>Game UI / UX</span></a>
    <div class="runhead-end"><nav class="backlinks" aria-label="Back matter"><a href="about.html">About</a><a href="resume.html">Resume</a></nav><span class="folio">Instruction booklet, 2026</span></div>
  </header>
  <div class="wrap cover-grid">
    <div>
      <h1 id="cover-h" class="display">Game UI, designed in Figma, shipped in engine.</h1>
      <p class="lede">I design and build menus, HUDs and game systems in Unity, Godot and TypeScript. By day I build the screens operators use to run solar plants and industrial systems.</p>
      <div class="btn-row"><a class="btn" href="work/argos.html">Start with chapter 01 {ARR}</a></div>
    </div>
    <div>
    <div class="cover-art">
      <figure class="art-a">{argos("river-menu", 2000, 953, "Argos River Menu: a river seen from above, with leaves floating on it as the menu buttons", "Argos River Menu")}<figcaption><b>01 Argos</b>, River Menu</figcaption><a href="work/argos.html" aria-label="Chapter 01, Argos"></a></figure>
      <figure class="art-b"><img src="assets/img/titan/hud-panel.webp" width="528" height="1248" alt="Project Titan Skirmish HUD: Kaiju threat meter, Unit Inspector and orders"><figcaption><b>02 Titan</b>, Skirmish HUD</figcaption><a href="work/project-titan.html" aria-label="Chapter 02, Project Titan"></a></figure>
      <figure class="art-c"><img src="assets/img/greywater/menu-panel.webp" width="520" height="721" alt="Greywater title menu: a paper panel with Continue selected"><figcaption><b>03 Greywater</b>, title menu</figcaption><a href="work/greywater.html" aria-label="Chapter 03, Greywater"></a></figure>
    </div>
    </div>
  </div>
  <div class="wrap">
      <nav class="contents" aria-labelledby="contents-h">
        <h2 id="contents-h">Contents</h2>
        <ol>
{CONTENTS}
        </ol>
      </nav>
  </div>
</section>

<div class="ch-titan">
{guide("Screen Guide: Project Titan", "Skirmish HUD, built in Unity uGUI", "assets/img/titan/hud-panel.webp", 528, 1248, "Project Titan Skirmish HUD in Unity: Kaiju threat meter with commander portrait, Unit Inspector with Attack, Hold, Defend and Retreat orders, and the command seal", "Hover a numbered entry to find it on the screen.", TITAN_POINTS, portrait=True)}
</div>

<section class="section" id="chapters" aria-labelledby="chapters-h">
  <div class="wrap">
    <div class="section-head"><h2 id="chapters-h">Chapters</h2><p>Six projects, each from first sketch to working build.</p></div>
    <ol class="index-list">
      <li class="ch-argos"><a class="entry" href="work/argos.html"><span class="tab" aria-hidden="true">01</span><div><h3>Argos</h3><p>A river seen from above as the title menu, and a stopped pocket watch with a field journal as the pause, for a story-led Unity adventure.</p><span class="meta">Menus and pause &middot; Unity uGUI &middot; design and build</span></div><span class="thumb">{argos("river-menu", 2000, 953, "", "Argos River Menu", extra=' loading="lazy"')}</span></a></li>
      <li class="ch-titan"><a class="entry" href="work/project-titan.html"><span class="tab" aria-hidden="true">02</span><div><h3>Project Titan</h3><p>Skirmish HUD for an isometric tactical auto battler, from grayscale wireframes to Unity.</p><span class="meta">UI/UX lead &middot; Unity uGUI &middot; team project</span></div><span class="thumb"><img src="assets/img/titan/hud-panel.webp" width="528" height="1248" alt="" loading="lazy"></span></a></li>
      <li class="ch-greywater"><a class="entry" href="work/greywater.html"><span class="tab" aria-hidden="true">03</span><div><h3>Greywater</h3><p>Menus, HUD and dialogue for a first-person narrative game, with a live title menu you can try.</p><span class="meta">UI system &middot; Figma, rebuilt in HTML</span></div><span class="thumb"><img src="assets/img/greywater/title-menu.webp" width="1282" height="726" alt="" loading="lazy"></span></a></li>
      <li class="ch-midas"><a class="entry" href="work/midas.html"><span class="tab" aria-hidden="true">04</span><div><h3>Midas: The Accursed King</h3><p>A narrative top-down RPG built inside Game Boy constraints for GBJam 14.</p><span class="meta">Programming and story &middot; Godot &middot; game jam</span></div><span class="thumb pixel"><img src="assets/img/midas/village.webp" width="312" height="264" alt="" loading="lazy"></span></a></li>
      <li class="ch-dreamland"><a class="entry" href="work/dreamland.html"><span class="tab" aria-hidden="true">05</span><div><h3>Dreamland Timeline</h3><p>A searchable, declassified-archive timeline for a fictional world, fed live from a spreadsheet.</p><span class="meta">Design and development &middot; TypeScript</span></div><span class="thumb"><img src="assets/img/dreamland/archive.webp" width="1600" height="876" alt="" loading="lazy"></span></a></li>
      <li class="ch-explore"><a class="entry" href="work/shopping-list.html"><span class="tab" aria-hidden="true">06</span><div><h3>UI Explorations</h3><p>A five-screen mobile app taken from paper sketch to clickable prototype.</p><span class="meta">Prototyping &middot; Figma</span></div><span class="thumb"><img src="assets/img/shopping/sketch.webp" width="904" height="832" alt="" loading="lazy"></span></a></li>
    </ol>
  </div>
</section>

<section class="section flush-top">
  <div class="wrap">
    <p class="aside-line">The habits come from operator screens: SCADA and HMI work for solar sites, and controls roles at Microsoft and Amazon, where a cluttered screen costs something. <a href="about.html">More about me</a></p>
  </div>
</section>'''

page('index.html', 'Maurice Birchard | Game UI/UX Designer',
     'Game UI/UX designer who designs menus and HUDs in Figma and ships them in Unity, Godot and TypeScript.',
     home, 'index.html', 'ch-back')

ARGOS_POINTS = [
    (25.8, 24, "Wake", "Begins the game. It sends three pulses out from the leaf, one for each of Cerberus's barks."),
    (42.2, 42, "Settings", "Subtitles, vibration, motion level, music and effects. The same pages open from the pause."),
    (58.3, 57, "Controls", "Rebinding leaves for keyboard and controller; each leaf's small word is the current key."),
    (74.2, 70.5, "Credits", "Every leaf is a button: it bobs on the current, lifts when focused and flips when pressed."),
    (90, 83.5, "Sleep", "Quits. Wake and Sleep frame the start and end of the game."),
]

# ---------------- Argos ----------------
ar = opener("01", "Argos", "Lead UI/UX on a contemplative 3D narrative adventure. Two diegetic menus, designed in Figma and built in Unity: a title menu that looks down into a river, with fallen leaves as buttons, and a pause that stops a pocket watch.") + '\n' + specs([
    ("Role", "Lead UI/UX: design and Unity build"), ("Engine", "Unity 6, uGUI + TextMeshPro, FMOD"), ("Input", "Keyboard and mouse, Xbox and PlayStation controllers"), ("Status", "Vertical slice in development, 2026")]) + '\n' + guide("Screen Guide: River Menu", "Day theme, built in Unity uGUI", "{P}assets/img/argos/river-menu.webp", 2000, 953,
    "Argos River Menu: fallen autumn leaves floating on a blue-grey river as the buttons Wake, Settings, Controls, Credits and Sleep, with a man reflected in the water", "The River Menu, Day theme. Hover an entry to find it on the screen.", ARGOS_POINTS) + f'''
<section class="section flush-top">
  <div class="wrap prose">
    <h2>A title menu you look down into</h2>
    <p>The title menu is a river seen from above. Fallen autumn leaves are the buttons and toggles: they bob on the current, lift when focused, and flip when pressed. Sliders are skipping stones, and Back is a rock. It is built to the Figma prototype's spec, on the same 1920&times;1080 stage with the same formulas and tokens.</p>
    <ul>
      <li><strong>Three rivers, one per stage of the game.</strong> Day is an autumn river with a willow and the man reflected in it. Soul is dark water lit by the hound's collar light and fireflies. Night holds stars, a faint aurora and a fractured moon.</li>
      <li><strong>Story in the menu.</strong> Wake and Sleep frame the start and end of the game. Wake sends three pulses out from the leaf, one for each of Cerberus's barks. After the first full loop, the hound's reflection slowly surfaces beside the man's.</li>
      <li><strong>Every input is first class.</strong> Mouse, keyboard and controller all focus and press the same leaves, and every control except Pause can be rebound from leaves on the Controls pages.</li>
    </ul>
  </div>
  <div class="wrap pair">
    <figure class="figure">{argos("watch-pause", 1109, 704, "Argos Watch Pause: a gold pocket watch over the dimmed village, its minute hand pointing at Resume, with Journal at 3, Leave river at 6 and Settings at 9", "Watch Pause", p="{P}", extra=' loading="lazy"')}<figcaption>The Watch Pause: the minute hand points at the focused option.</figcaption></figure>
    <figure class="figure">{argos("journal", 1235, 869, "Argos Field Journal, Letters page: entries grouped by act on the left page, the letter being read on the right, with three empty photograph fragment slots", "Field Journal", p="{P}", extra=' loading="lazy"')}<figcaption>The Field Journal, Letters: entries on the left page, the one being read on the right.</figcaption></figure>
  </div>
  <div class="wrap prose">
    <h2>A pause that stops time</h2>
    <p>Esc or Start stops time, the world dims to 55%, and the protagonist's father's pocket watch slides up. The minute hand points at the focused option: Resume at 12, Journal at 3, Leave river at 6, Settings at 9. Resume plays one tick, the second hand steps six degrees, and the world moves again 240&nbsp;ms later.</p>
    <p>Settings fades into the River Menu, so one settings system serves the title and the pause. The Field Journal is a notebook spread with Letters, Keepsakes and Photos tabs.</p>
    <div class="note"><h3>{NOTE}Design tone</h3><p>Minimal and diegetic, in the vein of Gris and Spiritfarer. No gradients, glows or glass, except the Soul act's collar light.</p></div>
    <h2>From Figma to Unity, number for number</h2>
    <ul>
      <li>Colours, geometry, type sizes and motion timings live in one tokens file taken from the Figma source, so a change happens in one place.</li>
      <li>Layout is written in Figma frame pixels, with the same cubic-bezier easing curves as the prototype.</li>
      <li>Menus run on unscaled time, so the same river can sit over a paused game.</li>
      <li>UI sounds are FMOD events shared between the River Menu and the pause, so a sound designer owns them without touching code.</li>
    </ul>
    <h2>Accessibility</h2>
    <ul>
      <li>Three motion levels: full, gentle (the default) and still.</li>
      <li>A Text Size setting (100, 125 and 150%) for dialogue and prompt words.</li>
      <li>Subtitles, vibration, and music and effects volume, all saved between sessions.</li>
      <li>Full rebinding for keyboard and controller.</li>
    </ul>
  </div>
  <div class="wrap">''' + turn(None, ("titan", "02", "Project Titan", "work/project-titan.html")) + '''</div>
</section>'''
page('work/argos.html', 'Argos | Maurice Birchard',
     'Diegetic menus for a narrative Unity adventure: a river title menu with leaves as buttons, and a stopped-watch pause with a field journal.',
     ar, 'work/argos.html', 'ch-argos', folio='Chapter 01 &middot; page 4')

# ---------------- Titan ----------------
titan = opener("02", "Project Titan", "Lead designer for the UI and HUD of a tactical skirmish auto battler with a twist.") + '\n' + specs([
    ("Role", "UI/UX lead and programmer"), ("Engine", "Unity, uGUI + TextMeshPro"), ("Team", "Small team, working in Notion and Discord"), ("Status", "In development, 2026")]) + '\n' + guide(
    "Screen Guide: Skirmish HUD", "Built in Unity uGUI", "{P}assets/img/titan/hud-panel.webp", 528, 1248,
    "Skirmish HUD in Unity: Kaiju threat meter with commander portrait, Unit Inspector with four order buttons, and a riveted command seal", "The Skirmish HUD in engine. Hover an entry to find it on the screen.", TITAN_POINTS, portrait=True) + '''
<section class="section">
  <div class="wrap prose">
    <h2>A HUD that narrates</h2>
    <p>Titan's hook is risk: every kill feeds a shared meter that can summon a Kaiju neither player fully controls. The HUD has to make that tension readable at a glance, keep the board clear, and reskin cleanly for three factions.</p>
    <p>Visual direction landed on cream panels with heavy dark outlines and riveted metal borders, so it is cartoony, easy to read and easy to swap.</p>
    <figure class="figure"><img src="{P}assets/img/titan/meter-detail.webp" width="494" height="128" alt="Detail of the Kaiju threat meter: IN 2 TURNS on the left, KAIJU THREAT on the right, an empty meter bar, and the commander portrait" loading="lazy"><figcaption>Detail, in engine: the threat meter and its countdown, with the commander portrait.</figcaption></figure>

    <h2>Scope first</h2>
    <p>The first pass covered the Skirmish HUD only. The War Room and formation builder are later passes. Keeping scope tight meant the team could react to something concrete instead of a sprawling system.</p>

    <h2>Three distinct directions</h2>
    <p>I wireframed three structurally different layouts in grayscale before any colour decisions:</p>
    <ul>
      <li><strong>Command Table:</strong> a diegetic, holographic table the player leans over.</li>
      <li><strong>Clean Tactical:</strong> a readability-first baseline.</li>
      <li><strong>Card-Forward:</strong> the hand dominates the screen.</li>
    </ul>
    <p>Grayscale kept the conversation on hierarchy and layout. Colour came later, built on a neutral dead-world base with faction colours layered on top.</p>

    <h2>The finding that shaped everything</h2>
    <p>I mapped every HUD element against every phase of a round in a phase-state matrix. Four of the seven phases have no player input at all. That led to two terms the team now uses:</p>
    <div class="note">
      <h3>''' + NOTE + '''Design vocabulary</h3>
      <p><span class="term">FOCUS</span> is where the hands go: interactive and dominant. <span class="term">BEAT</span> is where the eyes go: dominant but not interactive. Titan spends most of its round in BEAT, so the HUD's job is often to tell the story of what just happened.</p>
    </div>

    <h2>Readability risks, called early</h2>
    <p>Blue-for-you, red-for-them collides with a faction whose identity colour is red, and it breaks for red-green colourblind players. I flagged friend-or-foe as the sharpest open risk and proposed non-colour carriers: base rings, silhouettes and outline weight.</p>

    <h2>Designing for the engine</h2>
    <p>Moving to Unity's uGUI changed what was cheap and what was expensive, so the designs account for it:</p>
    <ul>
      <li>Live elements like the threat meter and health bars sit on their own dynamic canvas, since any change rebuilds the whole canvas mesh.</li>
      <li>A click-through policy for the HUD, because every graphic blocks raycasts by default and the HUD floats over a clickable board.</li>
      <li>Faction reskins through a theme asset rather than a prefab per faction, decided before component specs were drawn.</li>
    </ul>

    <h2>The command seal</h2>
    <p>The team replaced a plain Resolve Orders button with a modular command seal stamped with the current faction's emblem. It sits translucent on hover, goes full opacity when pressed, and lights up once every unit has orders, so readiness is visible without reading a word.</p>
    <figure class="figure w-sm"><img src="{P}assets/img/titan/seal-detail.webp" width="268" height="323" alt="Detail of the command seal: a riveted round button above the Resolve Orders label" loading="lazy"><figcaption>Detail, in engine: the command seal above its Resolve Orders label.</figcaption></figure>

    <h2>What I took from it</h2>
    <p>Mapping state before drawing screens saved the team from designing controls for phases where the player cannot act. It is the same habit that keeps an operator screen honest, applied to a game.</p>
  </div>
  <div class="wrap">''' + turn(("argos", "01", "Argos", "work/argos.html"), ("greywater", "03", "Greywater", "work/greywater.html")) + '''</div>
</section>'''
page('work/project-titan.html', 'Project Titan | Maurice Birchard',
     'Skirmish HUD for a tactical auto battler, from grayscale wireframes to Unity uGUI.',
     titan, 'work/project-titan.html', 'ch-titan', folio='Chapter 02 &middot; page 8')

# ---------------- Greywater ----------------
gw = opener("03", "Greywater", "UI/UX for a first-person narrative exploration game set in an abandoned town that fell off the map in the 1970s. A complete interface system: title menu, exploration HUD, dialogue and a style guide built to keep the town, not the UI, at the centre of the screen.") + '\n' + specs([
    ("Role", "UI/UX design"), ("Tools", "Figma"), ("Platform", "PC, keyboard and mouse"), ("Scope", "Menus, HUD, dialogue, style guide")]) + '''
<section class="section" aria-labelledby="try-h">
  <div class="wrap">
    <div class="guide-title"><h2 id="try-h">Try the title menu</h2><p>Hover, or use &uarr; &darr; and Enter</p></div>
    <div class="gw-scene">
      <div class="gw-panel">
        <div class="gw-chapter">Chapter one</div>
        <div class="gw-title">Greywater</div>
        <div class="gw-sub">More Silent than the Grave</div>
        <div class="gw-rule"></div>
        <ul class="gw-menu" role="menu" aria-label="Greywater main menu">
          <li role="none"><button role="menuitem" class="gw-row is-selected" tabindex="0">Continue <span class="gw-meta">Ferry Road &middot; 42 min</span></button></li>
          <li role="none"><button role="menuitem" class="gw-row" tabindex="-1">New game</button></li>
          <li role="none"><button role="menuitem" class="gw-row" tabindex="-1">Settings</button></li>
          <li role="none"><button role="menuitem" class="gw-row" tabindex="-1">Credits</button></li>
          <li role="none"><button role="menuitem" class="gw-row gw-quiet" tabindex="-1">Quit</button></li>
        </ul>
        <div class="gw-hints" aria-hidden="true"><span>&uarr;&darr; Navigate</span><span>Enter Select</span><span>Esc Back</span></div>
        <p class="gw-status" aria-live="polite"></p>
      </div>
    </div>
    <p class="plate-cap">Rebuilt in HTML and CSS from the Figma component, so hover and keyboard both resolve to the same selected state.</p>
  </div>
</section>
''' + guide("Screen Guide: Exploration HUD", "Everything inside a 48px safe margin", "{P}assets/img/greywater/hud.webp", 1280, 720,
    "Greywater exploration HUD: objective top left reading Find another way into the chapel, a hold E prompt to pry the shutter at centre, a Shift keycap hint for moving quietly, and the equipped oil lamp bottom right",
    "The exploration HUD over a placeholder scene. Hover an entry to find it on the screen.", GW_POINTS) + '''
<section class="section">
  <div class="wrap prose">
    <h2>Three rules for the whole interface</h2>
    <ul>
      <li><strong>Darker while playing, lighter at rest.</strong> Gameplay overlays are near black and translucent so the town stays the brightest thing on screen. Menus, inventory and pause are opaque paper panels that slide over a dimmed scene, a clear signal that the world has stopped.</li>
      <li><strong>Blue means "this is what your next key affects."</strong> Slate blue marks the current selection and nothing decorative uses it, so the eye never has to search.</li>
      <li><strong>Few keys, simple controls.</strong> Arrows or WS to navigate, Enter to select, E to interact, I for the satchel, Esc to back out, 1 through 6 for quick select.</li>
    </ul>
    <h2>A HUD that gets out of the way</h2>
    <p>The objective sits top left and fades to 40% opacity after eight seconds, returning when the objective changes or the player taps Q. The interaction prompt is the only element allowed to animate, which is exactly what makes it readable at the edge of vision.</p>
    <p>Hold prompts fill over 450ms, cancel on release, and can be switched to a single press for players who need it.</p>
  </div>
  <div class="wrap">
    <figure class="figure">
      <img src="{P}assets/img/greywater/dialogue.webp" width="1600" height="882" alt="Greywater dialogue: Margaret Hollis, caretaker, says the ferry stopped running on the Sunday and nobody asked why. Three numbered reply choices, the second tagged Ledger page" loading="lazy">
      <figcaption>Dialogue: spoken lines in serif, numbered choices, and a tag showing which reply an item unlocks.</figcaption>
    </figure>
  </div>
  <div class="wrap prose">
    <h2>Dialogue with consequences you can see</h2>
    <p>Spoken lines are set in Newsreader, a serif, so voice always reads differently from interface text. Choices are numbered for one-key answers, and a choice unlocked by something in the satchel carries a small tag, here "Ledger page," so the player knows why it is available.</p>
    <h2>Player flow</h2>
    <p>Every state is reachable in one or two keys, and Esc always takes the player one step back toward exploration.</p>
  </div>
  <div class="wrap">
    <figure class="figure">
      <img src="{P}assets/img/greywater/player-flow.webp" width="1504" height="185" alt="Player flow: Main menu, Continue or New game, Exploration HUD, Esc to Pause, then Settings. From exploration: Hold E to interact, Dialogue choice, back to HUD, or I for Satchel and Esc back to HUD" loading="lazy">
    </figure>
    <figure class="figure">
      <img src="{P}assets/img/greywater/style-guide.webp" width="1504" height="1205" alt="Greywater style guide: IBM Plex Mono and Newsreader type scale, eight-colour palette, 4px spacing scale, menu row states, keycaps, hold prompt, item slots, and accessibility notes" loading="lazy">
      <figcaption>Style guide: type, palette, spacing, menu row states and in-game components.</figcaption>
    </figure>
  </div>
  <div class="wrap prose">
    <h2>Accessibility built in</h2>
    <ul>
      <li>Interface text scales to 175% without pushing panels off screen.</li>
      <li>Selection is never colour alone: the 3px bar and the fill always travel together.</li>
      <li>Nothing in the HUD depends on telling hues apart.</li>
      <li>Hold-to-interact can become a single press.</li>
    </ul>
  </div>
  <div class="wrap">''' + turn(("titan", "02", "Project Titan", "work/project-titan.html"), ("midas", "04", "Midas", "work/midas.html")) + '''</div>
</section>'''
page('work/greywater.html', 'Greywater | Maurice Birchard',
     'Menus, HUD and dialogue for a first-person narrative game, with a live title menu rebuilt from Figma.',
     gw, 'work/greywater.html', 'ch-greywater', folio='Chapter 03 &middot; page 12', extra_head=GW_FONTS,
     scripts='\n<script src="../assets/js/greywater-menu.js"></script>',
     extra_css='\n<link rel="stylesheet" href="../assets/css/greywater-menu.css">')

# ---------------- Midas ----------------
midas = opener("04", "Midas: The Accursed King", "A narrative-driven top-down RPG made for GBJAM 14. Midas, a disgraced king, works to restore his form and memories while chasing wealth and power, with two endings to uncover.",
    f'\n      <div class="btn-row"><a class="btn" href="https://moninja.itch.io/midas-the-accursed-king" rel="noopener">Play in your browser on itch.io {EXT}</a></div>') + '\n' + specs([
    ("My role", "Programming and story"), ("Engine", "Godot, HTML5"), ("Jam", "GBJAM 14, Sept 2026"), ("Constraints", "160&times;144, four colours, Game Boy inputs")]) + '''
''' + guide("Screen Guide: Dialogue", "160&times;144, four colours", "{P}assets/img/midas/dialogue.webp", 312, 255,
    "Forest path with a ghost NPC and a dialogue box reading Ghosty: Oh... good morning!", "Dialogue UI built to fit the Game Boy screen. Hover an entry to find it on the screen.", MIDAS_POINTS, pixel=True) + '''
<section class="section flush-top">
  <div class="wrap">
    <figure class="figure pixel narrow"><img src="{P}assets/img/midas/village.webp" width="312" height="264" alt="Village with houses, ghosts and a skeleton enemy in a muted four-tone palette" loading="lazy"><figcaption>Village hub in the four-tone palette.</figcaption></figure>
  </div>
</section>
<section class="section">
  <div class="wrap prose">
    <h2>Designing inside a tiny box</h2>
    <p>GBJam's rules are the point: a 160&times;144 screen, four colours per frame, and only the Game Boy's buttons. Every piece of UI, from dialogue boxes to menus, has to earn its pixels and stay legible with almost no colour to separate information.</p>
    <h2>Systems over content</h2>
    <p>With a jam timeline, I leaned on systems that generate variety instead of hand-authoring everything:</p>
    <ul>
      <li><strong>Two power tracks:</strong> slaying unique enemies grows LEAD powers, while gold grows GOLD powers, so how you play shapes how Midas grows.</li>
      <li><strong>Gold as a resource:</strong> healing costs gold from the SELECT menu, which turns wealth into a running decision.</li>
      <li><strong>Branching endings:</strong> after finishing, players can continue and choose differently to see another ending.</li>
    </ul>
    <h2>Controls</h2>
    <p>Keyboard maps to the Game Boy layout (Z for A, X for B, arrows to move, Shift for SELECT, Enter for START), and gamepads work out of the box.</p>
    <div class="note"><h3>''' + NOTE + '''Credits</h3><p>Programming and story: Maurice Birchard (Moninja). Art: Lexiianna. Music and SFX: PhantomAxis Studios and Haphaeu.</p></div>
    <h2>What I took from it</h2>
    <p>Hard constraints make UI decisions faster and sharper. With four colours, hierarchy has to come from shape, spacing and placement, which is good practice for any HUD.</p>
  </div>
  <div class="wrap">''' + turn(("greywater", "03", "Greywater", "work/greywater.html"), ("dreamland", "05", "Dreamland", "work/dreamland.html")) + '''</div>
</section>'''
page('work/midas.html', 'Midas: The Accursed King | Maurice Birchard',
     'A narrative top-down RPG built in Godot inside Game Boy constraints for GBJam 14.',
     midas, 'work/midas.html', 'ch-midas', folio='Chapter 04 &middot; page 16')

# ---------------- Dreamland ----------------
dl = opener("05", "Dreamland Timeline", "An interactive archive covering 160 years of a fictional world's history, styled as a declassified records system. Built so a writing team can update the lore in a spreadsheet and see it live on the site.",
    f'\n      <div class="btn-row"><a class="btn" href="https://moninja92.github.io/dreamland-timeline/" rel="noopener">Open the live site {EXT}</a><a class="btn btn-quiet" href="https://github.com/moninja92/dreamland-timeline" rel="noopener">View source {EXT}</a></div>') + '\n' + specs([
    ("Role", "Design and development"), ("Stack", "TypeScript, Vite"), ("Data", "Google Sheet via CSV, local fallback"), ("Deploy", "GitHub Actions to Pages")]) + '\n' + guide("Screen Guide: The archive", "Live site, TypeScript and Vite", "{P}assets/img/dreamland/archive.webp", 1600, 876,
    "Dreamland archive overview with records search, category filters and decade histogram", "The archive overview. Hover an entry to find it on the screen.", DL_POINTS) + '''
<section class="section tight-top">
  <div class="wrap">
    <figure class="figure"><img src="{P}assets/img/dreamland/file-panel.webp" width="1600" height="997" alt="Dreamland archive with an entry selected, showing a File No. 001 detail panel with start and end dates, length and concurrent events" loading="lazy"><figcaption>Selecting an entry opens its case file: dates, duration, who was alive, what overlapped.</figcaption></figure>
  </div>
  <div class="wrap prose">
    <h2>The problem</h2>
    <p>A fictional world with a long history gets hard to keep straight. Writers need to check what happened when, who was alive at the time and what overlapped, without digging through a spreadsheet.</p>
    <h2>An archive, not a table</h2>
    <p>The interface leans into the setting. Searching is a "records request," entries open as numbered case files, and monospace labels and stamped headers make it feel like declassified documents. The theme does real work: it makes a dense data tool feel like part of the world.</p>
    <h2>Features</h2>
    <ul>
      <li>Search across events, characters and years, with a keyboard shortcut to jump to search.</li>
      <li>Colour-coded category filters with live counts.</li>
      <li>A decade histogram that shows where history clusters at a glance.</li>
      <li>Case file panels with computed duration, characters alive at the start, and events happening at the same time.</li>
      <li>A spoiler toggle so the archive is safe for readers who are not caught up.</li>
      <li>A custom calendar with 28-day months and 336-day years, with all date maths built around it.</li>
      <li>Light and dark modes, plus shareable links to individual entries.</li>
    </ul>
    <h2>Built for the people maintaining it</h2>
    <p>The data lives in a Google Sheet. Edit the sheet, refresh the page, and everyone sees the change. If the sheet is unreachable, the site falls back to a bundled CSV snapshot so it never shows an empty archive.</p>
  </div>
  <div class="wrap">
    ''' + turn(("midas", "04", "Midas", "work/midas.html"), ("explore", "06", "UI Explorations", "work/shopping-list.html")) + '''
  </div>
</section>'''
page('work/dreamland.html', 'Dreamland Timeline | Maurice Birchard',
     'A searchable, declassified-archive timeline for a fictional world, built in TypeScript and fed live from a spreadsheet.',
     dl, 'work/dreamland.html', 'ch-dreamland', folio='Chapter 05 &middot; page 20')

# ---------------- Shopping list ----------------
sl = opener("06", "UI Explorations: Shopping List", "A five-screen mobile flow taken from a paper-style prototype, drawn in Figma, to a working, clickable prototype. Every screen, and every path between them, mapped and testable.",
    f'\n      <div class="btn-row"><a class="btn" href="shopping-list-prototype/index.html">Open the prototype full screen {ARR}</a></div>') + '\n' + specs([
    ("Context", "Coursework, CSU Global"), ("Tools", "Figma, React"), ("Screens", "Home, Add, View, Edit, Settings"), ("Deliverable", "Navigation-mapped prototype")]) + '''
''' + guide("Screen Guide: Paper prototype", "Five screens, seven routes", "{P}assets/img/shopping/sketch.webp", 904, 832,
    "Sketched paper prototype: Settings, Home, Add Item, View List and Edit Item screens joined by seven numbered arrows", "Step 1: the paper prototype. Hover an entry to find it on the screen.", SL_POINTS) + '''
<section class="section flush-top">
  <div class="wrap">
    <figure class="figure w-md"><img src="{P}assets/img/shopping/home-hifi.webp" width="900" height="1150" alt="Refined Home screen titled My Lists with Groceries, Hardware Store and Party Supplies cards and an Add Item button" loading="lazy"><figcaption>Refined Home screen.</figcaption></figure>
  </div>
</section>
<section class="section">
  <div class="wrap prose">
    <h2>The brief</h2>
    <p>Design a paper prototype for a shopping list app covering Home, Add Item, View List, Edit/Delete and Settings/About, with the navigation between them clearly shown.</p>
    <h2>Navigation first</h2>
    <p>Before styling anything I mapped every path a user can take. Seven numbered routes connect five screens, and Home is the only starting point. Numbering the arrows turned the sketch into something a reviewer could walk through step by step.</p>
    <h2>From sketch to something you can click</h2>
    <p>I rebuilt the sketch in Figma as a working prototype. Lists, items and settings hold real state, so checking off milk updates the "left" count on Home, and a saved item shows up in View List. Below is the full board in its starting state.</p>
  </div>
  <div class="wrap">
    <div class="proto-frame" role="region" aria-label="Interactive prototype, scrolls sideways on small screens" tabindex="0">
      <iframe src="shopping-list-prototype/index.html" title="Shopping List interactive paper prototype" loading="lazy"></iframe>
    </div>
    <figure class="figure"><img src="{P}assets/img/shopping/beginning-state.webp" width="1800" height="2167" alt="Full prototype board in its beginning state: Settings, Home with Groceries selected, Add Item, View List, Edit Item and the navigation flow legend" loading="lazy"><figcaption>The prototype board at its beginning state, Groceries selected.</figcaption></figure>
  </div>
  <div class="wrap prose">
    <h2>Refining the screens</h2>
    <p>A higher-fidelity pass added item categories under each name, a dedicated Preferences group in Settings, and a softer, rounded device frame.</p>
  </div>
  <div class="wrap">
    <figure class="figure narrow"><img src="{P}assets/img/shopping/hifi-screens.webp" width="1600" height="1930" alt="Refined View List, Edit Item, Add Item and Settings screens on a gray canvas" loading="lazy"><figcaption>Refined View List, Edit Item, Add Item and Settings.</figcaption></figure>
  </div>
  <div class="wrap prose">
    <h2>Design decisions</h2>
    <ul>
      <li>Checked items drop below a divider and fade, so what is left to buy is always on top.</li>
      <li>Delete asks for confirmation inline instead of a modal, keeping the user on the same screen.</li>
      <li>Save stays disabled until an item has a name, which prevents empty entries without an error message.</li>
      <li>One accent colour carries every primary action, so the next step is always obvious.</li>
    </ul>
  </div>
  <div class="wrap">''' + turn(("dreamland", "05", "Dreamland", "work/dreamland.html"), ("back", "", "About the designer", "about.html")) + '''</div>
</section>'''
page('work/shopping-list.html', 'UI Explorations | Maurice Birchard',
     'A five-screen mobile app taken from paper sketch to a clickable Figma prototype.',
     sl, 'work/shopping-list.html', 'ch-explore', folio='Chapter 06 &middot; page 24')

# ---------------- About ----------------
about = opener("", "About the designer", "I'm Maurice Birchard, a systems engineer moving into the UI and UX side of game design. I've spent years on the screens operators use to run solar plants and industrial systems in real time. That work taught me how to put the right information in front of someone at the exact moment they need it, and how much a cluttered screen can cost.") + '''
<section class="section">
  <div class="wrap two-col">
    <div class="prose">
      <h2>What I do</h2>
      <ul>
        <li><strong>Interface design:</strong> dense information made easy to read and act on.</li>
        <li><strong>Design that ships:</strong> I prototype in Figma, then build in Unity, Godot or TypeScript, so designs account for how the engine actually works.</li>
        <li><strong>Team process:</strong> wireframes first, so the team spots risks early and prototypes quickly.</li>
      </ul>
      <h2>Tools</h2>
      <p>Figma, Unity (uGUI, TextMeshPro), Godot, TypeScript and Vite, Ignition Perspective and Vision, Wonderware System Platform, Miro and Notion.</p>
      <div class="btn-row after-prose"><a class="btn" href="resume.html">Read the resume ''' + ARR + '''</a><a class="btn btn-quiet" href="contact.html">Get in touch</a></div>
    </div>
    <div>
      <h2 class="col-head">Service record</h2>
      <ol class="career">
        <li><span class="when">Apr 2026 &ndash; now</span><div><b>SCADA Engineer, QE Solar</b><span>Custom SCADA platform in Ignition, with dashboards operators can track and update.</span></div></li>
        <li><span class="when">Jul 2025 &ndash; now</span><div><b>Control Systems SME, Microsoft</b><span>OT and ICS systems for datacenters: BMS, EPMS, SCADA and PLCs.</span></div></li>
        <li><span class="when">Nov 2023 &ndash; Apr 2026</span><div><b>Intelligence Analyst, US Army</b><span>Served alongside the civilian roles listed here. Turned large, messy datasets into clear briefings for leadership.</span></div></li>
        <li><span class="when">Oct 2024 &ndash; Jul 2025</span><div><b>Control Systems Specialist, HelloFresh</b><span>PLCs for automation and robotics.</span></div></li>
        <li><span class="when">Jun 2023 &ndash; Oct 2024</span><div><b>Controls and robotics, Amazon</b><span>Control Systems Specialist and Maintenance and Robotics Engineer II.</span></div></li>
        <li><span class="when">Jan 2026</span><div><b>BS, Computer Science</b><span>Cybersecurity focus, Colorado State University Global. Master's in AI and Machine Learning in progress.</span></div></li>
      </ol>
    </div>
  </div>
</section>'''
page('about.html', 'About | Maurice Birchard',
     'Game UI/UX designer with a background in industrial HMI and SCADA design and military service.',
     about, 'about.html', 'ch-back', folio='Back matter &middot; page 28')

# ---------------- Resume ----------------
resume = opener("", "Resume", "The full resume, readable here. Download the PDF for your files.",
    f'\n      <div class="btn-row"><a class="btn" href="assets/Maurice-Birchard-Resume.pdf" download="Maurice-Birchard-Resume.pdf">Download PDF</a><a class="btn btn-quiet" href="assets/Maurice-Birchard-Resume.pdf" target="_blank" rel="noopener">Open PDF in a new tab {EXT}</a></div>') + '''
<section class="section">
  <div class="wrap prose resume">
    <h2>Career objective</h2>
    <p>Experienced and highly adaptive military veteran with a secret clearance and 14 years of experience developing and troubleshooting mechanical, electrical and computer systems. Scheduled to finish a Master's in AI and Machine Learning in November 2026.</p>
    <h2>Skills</h2>
    <ul class="skills">
      <li>Robotics and automation</li><li>Industrial cybersecurity</li><li>SCADA/HMI</li><li>Communication protocols</li><li>Data analysis</li><li>Electrical systems</li><li>Python</li><li>Project management</li><li>Reporting and briefing</li>
    </ul>
    <h2>Experience</h2>
    <div class="job"><h3>SCADA Engineer, QE Solar, Scottsdale</h3><span class="when">April 2026 &ndash; current</span><ul>
      <li>Building a custom SCADA platform with Ignition and Chariot MQTT services to monitor and track multiple sites, with a dashboard operators can easily track and update.</li>
      <li>Program manager of SCADA operations: reported gap analysis and used Jira and Confluence for ticketing, reporting and agile development.</li>
      <li>Used C#, Java and Python to build the back-end dev environment for SCADA development; managed and instructed other users on the systems.</li></ul></div>
    <div class="job"><h3>Control Systems SME, Microsoft, Phoenix</h3><span class="when">July 2025 &ndash; current</span><ul>
      <li>Controls SME ensuring secure and reliable operation of OT/ICS systems, including BMS/BAS, EPMS, SCADA, PLCs, HVAC controls and electrical monitoring.</li>
      <li>Troubleshoot complex automation, controls and network issues supporting datacenter uptime and security baselines.</li>
      <li>Collaborate with OT Security, Networking and CE leadership to harden controls networks and align with Zero Trust OT principles.</li>
      <li>Conduct RCAs and implement design improvements that improve resiliency and reduce recurrence.</li>
      <li>Support incident response for control-related alarms, communication failures and cybersecurity issues.</li></ul></div>
    <div class="job"><h3>Intelligence Analyst, United States Army</h3><span class="when">November 2023 &ndash; April 2026</span><ul>
      <li>Conducted complex intelligence analysis to identify patterns, anomalies and emerging threats across large, multi-source datasets, supporting risk-informed decision-making.</li>
      <li>Performed detailed investigative assessments and root cause analysis to evaluate adversary behaviour, vulnerabilities and systemic risk factors.</li>
      <li>Synthesized ambiguous and incomplete information into clear, actionable intelligence products for senior leadership and cross-functional stakeholders.</li>
      <li>Applied structured analytic techniques to assess likelihood, impact and mitigation options for operational and strategic risks.</li>
      <li>Collaborated with multidisciplinary teams to develop mitigation strategies, improve controls and reduce recurrence of identified risks.</li>
      <li>Produced concise written reports and briefings translating technical findings into business-relevant insights under time-sensitive conditions.</li></ul></div>
    <div class="job"><h3>Control Systems Specialist, HelloFresh AZ01, Phoenix</h3><span class="when">October 2024 &ndash; July 2025</span><ul>
      <li>Configured and tested PLCs to control automation and robotics systems.</li>
      <li>Analyzed network traffic with Wireshark to identify latency issues, improving connectivity and reducing downtime to under 1 percent.</li>
      <li>Performed preventative maintenance and led root cause analyses; assisted with system and network integration.</li></ul></div>
    <div class="job"><h3>Control Systems Specialist, Amazon GYR3, Phoenix</h3><span class="when">January 2024 &ndash; October 2024</span><ul>
      <li>Programmed servomotors and variable frequency drives; performed advanced electrical troubleshooting.</li>
      <li>Used structured text and ladder logic to optimize product flow, increasing throughput and reducing invalid transport.</li>
      <li>Maintained Profibus and Profinet communication protocols controlling facility inputs.</li></ul></div>
    <div class="job"><h3>Maintenance and Robotics Engineer II, Amazon GYR3, Phoenix</h3><span class="when">June 2023 &ndash; January 2024</span><ul>
      <li>Diagnosed and troubleshot robotic, electrical and mechanical systems through remote software platforms.</li>
      <li>Programmed and troubleshot programmable logic controllers across thousands of assets.</li>
      <li>Performed cloud network analysis and maintained server systems monitored through SCADA and SNMP.</li></ul></div>
    <h2>Education</h2>
    <div class="job"><h3>Master of AI and Machine Learning, Colorado State University Global</h3><span class="when">In progress, finishing November 2026</span></div>
    <div class="job"><h3>Bachelor of Science, Computer Science (Cybersecurity focus), Colorado State University Global</h3><span class="when">January 2026</span></div>
  </div>
</section>'''
page('resume.html', 'Resume | Maurice Birchard',
     'Resume of Maurice Birchard: SCADA, controls and HMI engineering, intelligence analysis, and game UI/UX.',
     resume, 'resume.html', 'ch-back', folio='Back matter &middot; page 30')

# ---------------- Contact ----------------
contact = opener("", "Contact", "Open to game UI/UX, game design and software roles, full-time or contract. Email is the fastest way to reach me.") + f'''
<section class="section">
  <div class="wrap two-col">
    <div class="contact-card">
      <h2>Email</h2>
      <a class="mail" href="mailto:mauricebirchard@gmail.com">mauricebirchard@gmail.com</a>
      <div class="btn-row">
        <a class="btn" href="mailto:mauricebirchard@gmail.com">Send an email {ARR}</a>
        <button class="btn btn-quiet" type="button" data-copy="mauricebirchard@gmail.com" aria-describedby="copy-status">Copy address</button>
      </div>
      <p class="copy-status" id="copy-status" role="status"></p>
      <p class="where">Based in Chandler, AZ. Open to remote.</p>
    </div>
    <div>
      <h2 class="col-head">Elsewhere</h2>
      <ul class="links">
        <li><a href="https://www.linkedin.com/in/mauricebirchard/" rel="noopener"><div><b>LinkedIn</b><span>linkedin.com/in/mauricebirchard</span></div>{EXT}</a></li>
        <li><a href="https://github.com/moninja92" rel="noopener"><div><b>GitHub</b><span>github.com/moninja92</span></div>{EXT}</a></li>
        <li><a href="https://moninja.itch.io/" rel="noopener"><div><b>itch.io</b><span>moninja.itch.io</span></div>{EXT}</a></li>
        <li><a href="https://www.youtube.com/@MorkusGaming" rel="noopener"><div><b>YouTube</b><span>youtube.com/@MorkusGaming</span></div>{EXT}</a></li>
        <li><a href="resume.html"><div><b>Resume</b><span>Read it here or download the PDF</span></div>{ARR}</a></li>
      </ul>
    </div>
  </div>
</section>'''
page('contact.html', 'Contact | Maurice Birchard',
     'Contact Maurice Birchard about game UI/UX, game design and software roles.',
     contact, 'contact.html', 'ch-back', folio='Back page &middot; page 32')

# ---------------- 404 ----------------
nf = opener("", "Page not found", "That page isn't in this booklet. It may have moved, or the link has a typo.",
    f'\n      <div class="btn-row"><a class="btn" href="/index.html">Back to the cover {ARR}</a></div>')
page('404.html', 'Page not found | Maurice Birchard', 'This page is not in the booklet.', nf, '', 'ch-back', folio='Missing page')
# 404 is served from any depth: make its links absolute.
p404 = ROOT / '404.html'
t = p404.read_text(encoding='utf-8')
t = t.replace('href="assets/', 'href="/assets/').replace('src="assets/', 'src="/assets/')
for _, _, _, href, _ in TABS:
    t = t.replace(f'href="{href}"', f'href="/{href}"')
t = t.replace('href="index.html"', 'href="/index.html"').replace('href="contact.html"', 'href="/contact.html"').replace('href="resume.html"', 'href="/resume.html"')
p404.write_text(t, encoding='utf-8', newline='\n')
print('ok')
