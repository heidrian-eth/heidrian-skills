# Wim Crouwel — International Typographic Style (Dutch)

## Essence
Crouwel treated the grid as something to show off, not hide: a coordinate system that letters, images and even the alphabet itself are built from, cell by cell. His work starts from the limits of the machine (phototypesetting, the CRT, dot-matrix output) and makes those limits the style. The result is impersonal, serial and exact, yet tense, because the system is always pushed right up to the edge of legibility.

## Key works examined
- **Vormgevers poster, Stedelijk Museum, 1968** (offset, 95 × 64 cm): the grid stays visible in the finished piece and *is* the image. *(visually checked: Stedelijk scan, 665 × 999 px)* Measured: a uniform lattice of **square modules, period 23.3 px ≈ 1/28.5 of the sheet width**, each drawn as a cell (≈80%) plus a narrow gutter channel (≈20%) outlined by **double hairlines**; the "1 cm graph paper / 4.5 cm letters" figures could not be confirmed at this scale (the module reads ≈2.2 cm on a 64 cm sheet). The top **49% is a solid dark warm-grey field** with the grid continuing in lighter lines; the headline sits in the paper half. Letters are **5 modules tall with a 1-module stroke**, corners **rounded (radius ≈ ¼ stroke)**, diagonals built as **1-module stair-steps** (v, r), not 45° cuts. The header line is the same modular face, small, reversed white out of the dark field.
- **New Alphabet, 1967**: a parametric face built for low-resolution CRTs. Mostly a 5 × 7 unit grid, horizontal and vertical strokes only, M/W shown as N/V with a bar under them. It adapts the letter to the machine rather than the reverse. *(visually checked: Stedelijk, the Kwadraatblad booklet cover and a letter drawing sheet)* The drawing sheet shows uniform strokes with **rounded terminals**, orthogonal except for **45° diagonals in k, v, x**. The booklet cover is a **full-bleed red field (89% of the surface)** with the black headline, four parallel language columns in tiny New Alphabet, two white full-width hairline rules, and a **white dot-matrix** text block.
- **Stedelijk catalogue series, 1964–84**: one typeface (Univers), always at the same size, at a constant catalogue height. Each issue is legible as one part of a run. *(visually checked: Stedelijk, covers for Hockney 1966, Larry Bell, Lichtenstein, Oldenburg 1970, Rauschenberg)* The constant is a **huge "SM" monogram in a bold grotesque, cropped by the top and left edges**, plus one tiny information line; the field colour changes per issue and is **full-bleed and saturated** (mint, violet-magenta, blue, or the artist's image).
- **Stedelijk identity and posters, 1963–85**: one system flexible enough for hundreds of exhibitions while keeping a recognisable voice. *(visually checked: Visuele Communicatie Nederland 1969 and Lucht Kunst 1971, Stedelijk scans)* *Visuele Communicatie*: about 39 grey, round-ended vertical bars fill the sheet (bar ≈ 2.2% of the width, light gaps ≈ 17% of the area), with modular round-dotted type whose title runs in a **fluorescent orange→magenta gradient**. *Lucht Kunst*: a **blue→cyan gradient ground**, a speech-bubble panel with **large rounded corners (radius ≈ 10% of the width)** filled cream→lime, an outlined modular headline, and a plain lowercase grotesque info block set **flush-right** at the foot.
- **Total Design, founded 1963**: the first multidisciplinary Dutch studio. Standard paper formats, a narrow set of sans serifs, grid sheets as templates for everything.

## Process (derived)
*From observation to process (see SKILL.md §1). This is what transfers; the rest of the file is evidence.*

**Wim Crouwel.** *Declare one square cell and build everything from whole cells, the big word included; freeze the constants of the series, so the only free choices left are one whole-region colour and what the cells spell.*
Process:
1. Fix one square module for both axes: period ≈1/28 of the short side, of which ≈80% is cell and ≈20% is gutter. Draw it, quietly, as a continuous layer over every ground, light or dark; it never moves or stops at a region edge.
2. Snap every position and size to whole cells and hang content from the top-left origin. Empty cells stay empty; nothing is centred or stretched to balance.
3. Divide the format once with a hard edge on a cell line into two regions of opposite value, between 50:50 and 90:10. No other large division.
4. Construct the single display element from the module itself: stroke exactly 1 cell, height a small whole number (5 cells), corners rounded by ≈1/4 of the stroke, diagonals as one-cell steps. It may be cropped by the format edge and may sit near the limit of legibility, because step 5 holds.
5. Set all other text in one neutral face at ONE size; rank comes from position and weight only. Every word in the constructed display is repeated or labelled in this plain text.
6. Give the piece one saturated hue and spend it on a whole region of step 3 or on the whole display element, never as scattered small marks. One two-stop ramp across that single element is allowed.
7. Freeze the series: choose 3–4 constants that never change between items (a cropped mark and its position, the text size, the format, the origin) and one variable (the region hue).
Why it works:
- A visible measure makes every size readable as a count: the eye compares things in cells, so the empty cells are as exact as the full ones and a 5-cell element looks deliberate. Hide the grid and the same layout reads as sparse.
- When the unit of the letter equals the unit of the layout, type and structure are the same object (grouping by likeness), which is why one constructed word can hold a format with nothing else in it. A drawn display face on the same grid sits on it instead of in it.
- Colour over a whole region is read as the state of the piece, not as a signal inside it, so a series can be told apart at a glance while everything else is identical. Sprinkle the same hue and it becomes a set of alerts.
Colour relations: three neutrals (ground, a dark that is not the darkest possible, a grid line 1–2 steps from its ground) plus one saturated hue at 45–90% as a region, or ≤10% as the whole display element; the hue changes per item in a series; text on the hue must still reach 4.5:1, so choose its value for the text, not the reverse.
Space and line: module ≈1/28 of the short side; gutter 20% of the module, drawn as a pair of hairlines; one hard division on a cell line; display 5 cells high with a 1-cell stroke; a mark cropped by two edges as the series constant.
Type requirement: a neutral face with enough weights to rank at one size, and figures that stay clear in a coarse matrix; the display is not a font choice but a construction rule (cells, stroke, step), applied to at most one or two words per view.
Motion and interaction: the grid is fixed and content changes in place, in whole-cell steps. The display builds stroke by stroke once on entry (≤320ms in total; with reduced motion it appears complete); nothing blinks or repeats. Hover and selection fill whole cells with the dark value and invert the text, with a weight step as the non-colour partner; a target is at least 44px, so two or more cells.
Fails when: the content is long reading text or free-form imagery that cannot be cropped to cells; the display has to carry a critical instruction (it is slow to read); the screen is too small for 5-cell elements (below about 20 cells across); items in a series need different structures.
Signature (do not carry together): visible graph-paper grid · stroke-built lowercase letters with stepped diagonals · a full-bleed red or fluorescent field.

**Transfer test** (an illustration that the process survives new colours and content; never reuse its hues, layout or wording as a design answer):

Habit tracker in sage and sand (phone, 390 × 844; humanist serif for text, soft photography in the journal).
1. *Module.* 14px (390 / 28 ≈ 13.9): 11px cell + 3px gutter, drawn as paired hairlines one step darker than the sand and one step lighter than the sage. It runs under everything, journal photos included.
2. *Snap.* All cards, photos and rows are whole cells; content hangs from (1,1). The lower right of the screen is 9 × 14 empty cells and stays empty.
3. *Division.* A hard edge at row 30 of 60: deep sage above, sand below.
4. *Display.* The current streak as a bar figure, not lettering: 30 day-columns each 1 cell wide, up to 5 cells high, corners rounded 3px, with rising weeks drawn as one-cell steps. It sits on the division and is cropped by the right edge.
5. *Text.* Everything in the serif at 16/22: habit names in bold, counts in regular. "Streak: 23 days" is printed in plain text under the figure.
6. *Hue.* One clay orange for the whole sage region on a day when the streak is at risk; otherwise no hue at all. Text on the clay is the darkest sage, 5.2:1.
7. *Series.* Constants on every habit's page: a cropped leaf mark at top-left, the division at row 30, the 16px text. Variable: the upper region's hue per habit.
- *Interaction.* Marking a day fills its 3 × 4-cell target (42 × 56px, padded to 44) with deep sage and sets the date bold.
- *Motion.* The bar figure builds column by column in 300ms once.
Result: a soft, serif habit journal. No grotesque, no red, no pixel lettering. What survived is the drawn cell, whole-cell construction of the one big element, a single hard division and frozen series constants.

## Space & composition
- **Show the scaffold.** The Vormgevers poster keeps its grid printed over both the paper and the dark field. In UI, the grid can be a real visible layer, not only a dev overlay: a cell plus a narrow gutter channel drawn as two hairlines (gutter ≈ 20% of the module), in warm grey on light grounds and a lighter grey on dark ones.
- **Square cells, not columns alone.** Crouwel worked in square modules (Vormgevers: identical 23.3 px period on both axes). Use one square module (e.g. 40px = 32px cell + 8px gutter) for both axes so that type, images and gaps all snap to the same lattice, and make the display stroke exactly one module.
- **Tension through blocks, not uneven columns.** Crouwel held that a page needs tension. In the works checked it comes from a **hard half/half split** (Vormgevers: 49% dark field over 51% paper) and from big type sitting against empty cells, while the lattice itself stays uniform. The "3-1-3" bar rhythm claimed earlier was **not seen** in any checked work (*unverified*).
- **Fixed constants across a series.** The catalogues kept the same height and type size issue after issue. Keep a few constants frozen across every screen (header height, title size, margin) so that only content varies.
- **Flush-left, ragged-right, top-anchored.** Content hangs from a strong top-left origin. Empty cells are part of the system and are not filled to balance the page.

## Color
*The hex table below is a reference sample for strict studies and homage only. For design, use the colour relations in "Process (derived)".*

The logic is achromatic structure plus one loud field. Paper, dark warm grey and grid carry the system, and each piece takes **one saturated hue, usually as a full-bleed field or the whole headline**, not as a small signal: red at 89% of the New Alphabet cover, violet-magenta on the Larry Bell catalogue, mint behind Hockney, fluorescent orange→magenta on Visuele Communicatie. Crouwel's "black" in Vormgevers is a **dark warm grey** (`#454140`), not black.

| Role | Hex |
|---|---|
| Paper / background | `#F5F2E9` (Vormgevers paper) |
| Grid hairline (warm grey, not blue: scan softens it, the printed line is a little darker) | `#C7C5BD`; on the dark field `#5A5755` |
| Ink / primary type | `#181416` (New Alphabet drawing ink) |
| Stedelijk red (a whole field, up to ~90% of a cover) | `#C21006` |
| Fluorescent accent (Visuele Communicatie title, magenta end) | `#ED258C` |
| Lime (replaces the phosphor green, which appears in no checked work; Lucht Kunst) | `#AACC2E` |
| Dark warm-grey field and poster ink (Vormgevers top 49%) | `#454140` |
| Fluorescent orange (Visuele Communicatie title, orange end) | `#EF8052` |
| Bar grey (Visuele Communicatie stripes, ~46% of that sheet) | `#635F5E` |
| Stedelijk blue (Oldenburg catalogue; Lucht Kunst ground `#467AB7`) | `#035B9F` |

Fills are flat in the 1960s pieces, but the 1969–71 posters use **vertical gradients** (orange→magenta type, blue→cyan ground), so a single gradient on one element is in character; atmospheric multi-stop gradients are not. The grid colour stays neutral and quiet so it reads as a measuring device.

## Form, line & typography
- Letters are *constructed*, not drawn: orthogonal strokes on a unit grid, uniform stroke weight, counters as squares. Vormgevers rounds every corner slightly (radius ≈ ¼ stroke) and builds diagonals as 1-module steps; the New Alphabet uses rounded terminals and 45° strokes only in k, v, x. Display type can be modular and borderline unreadable because body text stays strictly legible (Univers, one size).
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
3. Keep the lattice uniform and get tension from blocks: one hard horizontal split (dark field over paper, near 50/50) and large type against empty cells. (The earlier "3-1-3 column cluster" is *unverified*: not seen in the checked works.)
4. Set all body, labels and UI chrome in one grotesque at one size (e.g. 15px/20px). Create hierarchy with position and weight, never with five font sizes.
5. Give each screen one saturated hue and let it own a whole region (a full-bleed header field, the hero headline, or the active panel), keeping everything else warm grey, ink and paper. Do not scatter it as small accents.
6. Make the hero headline a modular, lowercase display face 5 cells tall with a 1-cell stroke and slightly rounded corners, cropped by the viewport edge if needed. Split the hero into a dark-grey half and a paper half, with the grid running through both.
7. Animate headings with `steps(n)` timing: a stroke-by-stroke build, no ease-out.
8. On hover, fill the hovered cell solid ink with inverted type. The state is a whole cell switching, like a pixel turning on.
9. Freeze series constants: every detail page shares the same header height, title position and image box ratio, and only the content changes, the way the catalogues did.
10. Use a dot-matrix face for numbers (prices, counts, timestamps) so that data visibly comes "from the machine".

## What this artist would reject
- Illustrated mascots, blobby shapes and hand-drawn "warmth" layered over a system.
- Rounded-corner cards floating on soft drop shadows, which hide the grid instead of declaring it.
- Ten type sizes and three typefaces per screen, with hierarchy by inflation.
- Glassmorphism and multi-stop atmospheric gradients. Colour should be a flat field or one clean two-stop ramp, not an atmosphere.
- Springy, bouncy physics animation that treats elements as rubber rather than raster.
- Centred, symmetrical hero layouts that balance the page instead of charging it with tension.

## Signature prompt seed
Design this app screen as a Wim Crouwel Stedelijk poster for a CRT: a visible 40px square grid (cell plus narrow gutter, double warm-grey hairlines) running across a dark warm-grey top half and an off-white bottom half, with every element snapped to whole cells, top-left anchored. Set a lowercase, modular display headline built from 1-cell orthogonal strokes with slightly rounded corners and stepped diagonals, 5 cells tall and cropped at the edge. All other text is one neutral grotesque at one size. Use warm-grey ink, one saturated hue as a full region (Stedelijk red or a fluorescent magenta), and dot-matrix numerals. Motion steps cell by cell, and hover inverts whole cells. No shadows, no gradients, no rounded softness.

## Sources
- Images checked (Stedelijk Museum Amsterdam collection, original files behind https://www.stedelijk.nl/en/search?query=crouwel&filter[]=collection_work):
  - Vormgevers 1968: https://s3-eu-west-1.amazonaws.com/production-static-stedelijk/images/adlib/affiches/hiresafgeleiden/196871-1748059317349.jpg
  - New Alphabet booklet 1967: https://s3-eu-west-1.amazonaws.com/production-static-stedelijk/images/adlib/kna-11624-1774670439683.jpg
  - New Alphabet drawing: https://s3-eu-west-1.amazonaws.com/production-static-stedelijk/images/adlib/2023/2008.204671-8a-1773806438914.jpg
  - Visuele Communicatie Nederland 1969: https://s3-eu-west-1.amazonaws.com/production-static-stedelijk/images/adlib/affiches/hiresafgeleiden/196921-1748059315966.jpg
  - Lucht Kunst 1971: https://s3-eu-west-1.amazonaws.com/production-static-stedelijk/images/adlib/affiches/hiresafgeleiden/197110-1748059316651.jpg
  - Catalogues (Hockney, Larry Bell, Lichtenstein, Oldenburg, Rauschenberg): https://s3-eu-west-1.amazonaws.com/production-static-stedelijk/images/adlib/2020/kna-8572-1596686527606.jpg, …/2020/kna-8631-1629777637965.jpg, …/grafische-vormgeving/kna-8627.jpg, …/grafische-vormgeving/kna-8697-1629777637333.jpg, …/kna-8641-1629777637149.jpg
- https://en.wikipedia.org/wiki/New_Alphabet
- https://www.sfmoma.org/artwork/2015.658/
- https://www.cooperhewitt.org/2013/11/26/gridnik/
- https://eyemagazine.com/feature/article/electrifying-the-alphabet
- https://eyemagazine.com/blog/post/crouwels-institutional-intuition
- https://www.stedelijk.nl/en/news/wim-crouwel-mr-gridnik-2
- https://beta.designmuseum.org/designers/wim-crouwel
- https://designobserver.com/the-debate-part-3/
