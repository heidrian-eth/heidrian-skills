# Armin Hofmann — Swiss International Typographic Style

## Essence
Hofmann made graphic design out of two forces set against each other: a hard, still geometric sign (a dot, a bar, a sans-serif letter) placed next to something soft and moving (a blurred halftone body, a gestural line), almost always in black and white. Unlike Müller-Brockmann's mathematical grids, his grid flexes. The tension between opposites does the communicating.

## Key works examined
- **Graphic Design Manual: Principles and Practice, 1965** (Niggli, black and white throughout; revised 1988). Chapters run Dot, Line, Confrontation, Letters and Signs, and each moves from abstract exercise to applied work. It teaches that a whole visual language can be built up from the smallest units.
- **Giselle, Basler Freilichtspiele, 1959** (offset litho, 127.6 × 90.2 cm). A near-abstract halftone dancer against rigid type. The dot of the "i" rises above the letter height to echo her knee. It teaches the organic-versus-geometric pairing.
- **Junge Holländische Bildhauer, Kunsthalle Basel, 1960.** A huge hand-cut linoleum "h" over condensed wood type. It teaches a single glyph scaled until it becomes architecture.
- **Stadttheater Basel season posters, 1960s** (the 1968 sheet is a 128 × 90.4 cm lithograph). They carried a fixed blank box, upper right, where the weekly programme was pasted, so the poster lived all season. It teaches the permanent frame with a swappable data slot.
- **Stadt Theater Basel 1965, the "feets" poster.** A ballet slipper against a cowboy boot. It teaches that meaning comes from putting two cropped fragments side by side, without illustration.
- **Wilhelm Tell, 1963.** Univers 57 condensed in perspective, with the numeral "1" replaced by a capital "I". It teaches glyphs bent to fit the system.
- **Dot/line studies** (Manual): Thérèse Moll's lattice of black bars with sections knocked out, and graded lines suggesting a passing train. They teach rhythm through interruption and gradation.

## Space & composition
- **Two-body compositions.** One soft mass (photo, blur, gesture) against one hard type cluster. Neither is centred, and they meet at a tense, near-touching edge.
- **Flexible grid.** Columns exist but give way when clarity demands it.
- **Extreme scale jumps.** A single letter or dot can take 50–70% of the sheet height while the text sits at roughly 1/40 of that.
- **Bare paper is a material.** The whites in *Giselle* are unprinted paper: an active field the black pushes against.
- **The fixed data slot.** A permanent frame with one window for changing information, placed as part of the design.

## Color
Hofmann reacted against the "trivialization of colour" in postwar advertising and said colour photography was too simple and too brilliant to be used correctly. His colour was precise, rare and treated as a language. The default is value contrast: black against paper, with halftone greys between.

| Hex | Role |
|---|---|
| `#F3F1EA` | Paper: the dominant field and page background |
| `#0B0B0B` | Ink: type, solid dots and bars |
| `#4A4A4A` | Dense halftone: photographic shadows, secondary masses |
| `#9A9893` | Light halftone: disabled, meta, motion-blur trails |
| `#D9D6CE` | Ghost: rules, knocked-out lattice cells |
| `#C8201A` | Optional single spot: one signal per screen, at most |

## Form, line & typography
The vocabulary is point, line and plane: perfect circles, and uniform bars that are graded or interrupted. Type is a condensed grotesque, set flush-left and ragged, and sometimes rotated. Letters are shapes first, so a counter, a dot or a stem can be enlarged until it reads as an image.
Fonts: **Archivo** (variable width axis; condensed widths stand in for Univers 57), **Anton** (for the Schmalfette wood-type punch), and **Inter Tight** for small text.

## Rhythm, motion & time
The Manual's line studies are motion diagrams: bars that thicken, thin or space out to suggest speed. In UI, motion should look like gradation, not easing flourishes. On fast transitions, leave a trail of 2–3 grey ghost copies at falling opacity. Keep the geometric frame still while the "soft" layer moves, the way the type in *Giselle* holds still as the dancer spins. Swap the data slot with a hard cut, never a fade.

## UI translations
1. Build every key screen as two bodies: one large soft element (a blurred or high-contrast photo, a gradient-free grey mass) offset against one tight block of type. Never centre either.
2. Default to pure value contrast: ship the whole UI in `#0B0B0B` on `#F3F1EA` plus two greys, and earn any hue with a single spot accent no larger than 3% of the screen.
3. Turn one glyph into the hero: set a single initial or numeral at `font-size: 60vh`, cropped by the viewport edge with `overflow: hidden`.
4. Design a permanent shell with a fixed "programme slot", a bordered rectangle top-right where live data swaps in, so the composition never reflows.
5. Run a 6-column grid but let the hero span 4.5 columns and bleed off the opposite edge, and allow text to hang outside the grid when that reads better.
6. Render photos as coarse halftones (`filter: grayscale(1) contrast(1.8)` plus a dot `mask-image`), with highlights left as bare background.
7. Make loading and progress states into graded line rhythms: 12 bars whose weights step from 1px to 8px, animated as a travelling wave.
8. Mark selection with a solid black dot (8–12px) set slightly above the cap height, Giselle's oversized i-dot, instead of a filled pill or background tint.
9. For empty states, show Moll's lattice: a grid of black bars with the missing cells knocked out to `#D9D6CE`, so the absence of data is drawn.
10. Set headings in a condensed grotesque, flush-left with tight tracking (`-0.02em`) and leading at 0.9, and rotate one per view 90° along an edge.

## What this artist would reject
- Cheerful multi-hue palettes with no meaning behind them.
- Centred, symmetrical heroes on soft gradients.
- Rounded cards and drop shadows standing in for figure/ground contrast.
- Decorative illustration and literal stock imagery.
- Timid type scales where nothing is enormous and nothing is tiny.
- Choices justified by taste rather than correctness.

## Signature prompt seed
Design this screen as a Basel poster by Armin Hofmann: warm paper-white field, black ink, two halftone greys, and no hue except one tiny red signal. Compose with two opposing bodies: a huge cropped geometric sign (a single letter or perfect dot at 60% of viewport height) against a coarse, near-abstract halftone photo, offset asymmetrically on a flexible six-column grid. Use condensed grotesque type, flush-left, set tight and small, and keep one fixed rectangular slot for live data. Show motion only through graded line rhythms and ghost trails, with no rounded cards and no shadows.

## Sources
- https://www.eyemagazine.com/blog/post/at-your-service
- https://www.slanted.de/?p=792679
- https://www.cooperhewitt.org/2018/08/05/aharmonyofcontrasts/
- https://posterhouse.org/blog/armin-hofmann-1920-2020/
- https://www.sfmoma.org/artwork/2014.667/
- https://fontsinuse.com/uses/14968/wilhem-tell-basler-freilichtspiele-1963
- https://vonbartha.com/stories/what-is-right-is-automatically-beautiful
- https://www.printmag.com/daily-heller/the-daily-heller-armin-hofmann-s-100-years/
- https://en.wikipedia.org/wiki/Armin_Hofmann
