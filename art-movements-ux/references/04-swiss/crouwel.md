# Wim Crouwel — International Typographic Style (Dutch)

## Essence
Crouwel treated the grid as something to show off, not hide: a coordinate system that letters, images and even the alphabet itself are built from, cell by cell. His work starts from the limits of the machine (phototypesetting, the CRT, dot-matrix output) and makes those limits the style. The result is impersonal, serial and exact, yet tense, because the system is always pushed right up to the edge of legibility.

## Key works examined
- **Vormgevers poster, Stedelijk Museum, 1968** (offset, 95 × 64 cm): drawn on pre-printed 1 cm graph paper, with square lowercase letters 4.5 × 4.5 cm (subtext 1.3 cm). The grid stays visible in the finished piece and *is* the image.
- **New Alphabet, 1967**: a parametric face built for low-resolution CRTs. Mostly a 5 × 7 unit grid, horizontal and vertical strokes only, 45° corners, M/W shown as N/V with a bar under them. It adapts the letter to the machine rather than the reverse.
- **Stedelijk catalogue series, 1964–84**: one typeface (Univers), always at the same size, at a constant catalogue height. Each issue is legible as one part of a run.
- **Stedelijk identity and posters, 1963–85**: one system flexible enough for hundreds of exhibitions while keeping a recognisable voice.
- **Total Design, founded 1963**: the first multidisciplinary Dutch studio. Standard paper formats, a narrow set of sans serifs, grid sheets as templates for everything.

## Space & composition
- **Show the scaffold.** The Vormgevers poster keeps its graph-paper lines printed. In UI, the column and baseline grid can be a real visible layer (1px hairlines at about 12% opacity) and not only a dev overlay.
- **Square cells, not columns alone.** Crouwel worked in square modules. Use a square module (e.g. 8px base, 40px cell) for both axes so that type, images and gaps all snap to the same lattice.
- **Tension through uneven intervals.** The poster's grey bars run in a 3-1-3 spacing rhythm, and Crouwel held that a page needs tension. Group columns in uneven clusters (3 wide, 1 gap, 3 wide) instead of a uniform 12-up spread.
- **Fixed constants across a series.** The catalogues kept the same height and type size issue after issue. Keep a few constants frozen across every screen (header height, title size, margin) so that only content varies.
- **Flush-left, ragged-right, top-anchored.** Content hangs from a strong top-left origin. Empty cells are part of the system and are not filled to balance the page.

## Color
The logic is mostly achromatic structure plus one or two loud signals. Paper and grid carry the system, and a single saturated colour (often red, sometimes fluorescent) carries the event.

| Role | Hex |
|---|---|
| Paper / background | `#F3F1EA` |
| Grid hairline (graph-paper blue-grey) | `#A9BCC4` |
| Ink / primary type | `#111111` |
| Stedelijk signal red (one per screen) | `#E3241B` |
| Fluorescent accent (sparingly) | `#FF3D8B` |
| Phosphor green (CRT / New Alphabet nod) | `#2BD96B` |

Use solid flat fills only, with no gradients. The grid colour should be cool and quiet so it reads as "measuring device".

## Form, line & typography
- Letters are *constructed*, not drawn: only orthogonal strokes on a unit grid, corners cut at 45°, uniform stroke weight, counters as squares. Display type can be modular and borderline unreadable because body text stays strictly legible (Univers, one size).
- All-lowercase display was a Crouwel habit (Vormgevers is entirely lowercase).
- Tight, regular word spacing, with no optical fudging into "friendliness".
- **Fonts (free):** *Archivo* (neutral grotesque stand-in for Univers, for body and UI); *Major Mono Display* (geometric, monospaced and modular, for headlines); *Doto* (dot-matrix, for numerals, status and data, echoing early computer typesetting).

## Rhythm, motion & time
- Motion should feel like a **plotter or CRT refresh**: elements step cell by cell (`steps()` timing) and never glide with springy easing.
- Headline reveals build stroke by stroke, horizontals then verticals, in 30–40ms ticks, as if drawn on a raster.
- Transitions keep the grid fixed while content swaps in place. The grid never moves, and only what sits in it changes.

## UI translations
1. Render the layout grid as a permanent background layer: `background-image: linear-gradient` hairlines on a 40px square module at 10–15% opacity.
2. Snap every element's x, y, width and height to whole cells, and lint for anything off-module.
3. Build columns in an uneven 3-1-3 cluster (content, gutter-cell, content), not equal 12-column spans.
4. Set all body, labels and UI chrome in one grotesque at one size (e.g. 15px/20px). Create hierarchy with position and weight, never with five font sizes.
5. Give each screen exactly one red element (the current state, the primary action, or the live item) and keep everything else ink on paper.
6. Make the hero headline a modular, lowercase display face at 6–8 grid cells tall, cropped by the viewport edge if needed.
7. Animate headings with `steps(n)` timing: a stroke-by-stroke build, no ease-out.
8. On hover, fill the hovered cell solid ink with inverted type. The state is a whole cell switching, like a pixel turning on.
9. Freeze series constants: every detail page shares the same header height, title position and image box ratio, and only the content changes, the way the catalogues did.
10. Use a dot-matrix face for numbers (prices, counts, timestamps) so that data visibly comes "from the machine".

## What this artist would reject
- Illustrated mascots, blobby shapes and hand-drawn "warmth" layered over a system.
- Rounded-corner cards floating on soft drop shadows, which hide the grid instead of declaring it.
- Ten type sizes and three typefaces per screen, with hierarchy by inflation.
- Gradients and glassmorphism. Colour should be a flat signal, not an atmosphere.
- Springy, bouncy physics animation that treats elements as rubber rather than raster.
- Centred, symmetrical hero layouts that balance the page instead of charging it with tension.

## Signature prompt seed
Design this app screen as a Wim Crouwel Stedelijk poster for a CRT: a visible 40px square graph-paper grid in pale blue-grey hairlines on off-white, with every element snapped to whole cells in an uneven 3-1-3 column rhythm, top-left anchored. Set a lowercase, modular display headline built from orthogonal strokes with 45° cuts, 7 cells tall and cropped at the edge. All other text is one neutral grotesque at one size. Use black ink, one red signal element, and dot-matrix numerals. Motion steps cell by cell, and hover inverts whole cells. No shadows, no gradients, no rounded softness.

## Sources
- https://en.wikipedia.org/wiki/New_Alphabet
- https://www.sfmoma.org/artwork/2015.658/
- https://www.cooperhewitt.org/2013/11/26/gridnik/
- https://eyemagazine.com/feature/article/electrifying-the-alphabet
- https://eyemagazine.com/blog/post/crouwels-institutional-intuition
- https://www.stedelijk.nl/en/news/wim-crouwel-mr-gridnik-2
- https://beta.designmuseum.org/designers/wim-crouwel
- https://designobserver.com/the-debate-part-3/
