# Emil Ruder — Swiss International Typographic Style

## Essence
Ruder treated the unprinted part of the page as the real material. The white inside an "o", the gap between words and the field around a block are all shapes to compose. Drawing on the Tao Te Ching and the Japanese tea aesthetic, he made asymmetry calm rather than aggressive. He worked with one sans family, mostly in black and grey, and got his contrast from rhythm, texture and interval, not decoration.

## Key works examined
- **Typographie (Niggli, 1967)**: a near-square, three-language manual that teaches counterform, contrast, texture, rhythm and the grid through exercises.
- **"Wesentliches", TM (1957–59)**: Plane, Line, Word, Rhythm. Typography reduced to primitives you can combine.
- **"The Typography of Order", Graphis 85 (1959)**: non-inked areas have their own optical value, and narrow intervals read as more intensely white.
- **TM 1952, tea and typography**: asymmetry as simple, plain and natural. This is the Zen root.
- **TM covers (1961, e.g. No. 10 in Univers 48)**: a year of covers in one family, lowercase, black and white, varying only size, weight, width and slant.
- **Ruder-Schrift and the *glas* poster (1956)**: a condensed sans built with students for high-impact word shapes.
- **Nine-square grid**: one 3×3 field yields 24 image positions and shapes.

## Space & composition
- **Counterform first.** Enclosed white (counters, tight gutters) reads muted, while open white reads bright. Compose with both temperatures.
- **Grid as a source of variety.** Use a 3×3 field and choose among its 24 module combinations, so no two sections share a footprint. The grid gives formal unity while every page differs.
- **Calm asymmetry.** Like the stones at Ryoanji, place 3–5 masses off-centre at unequal intervals. Never mirror.
- **Density versus void.** Set tight, dark blocks on narrow measures and float them in fields that are 50–65% empty.
- **Parallel columns.** Typographie runs three languages side by side, so equal-width columns of unequal length become texture.

## Color
Black is the primary colour, grey values do most of the work, and red is the single accent. A small red against a large black mass gains intensity. Ruder warned against pushing any contrast to the extreme.

| Role | Hex |
|---|---|
| Paper (warm uncoated) | `#F4F2EC` |
| Ink (body, display) | `#141414` |
| Grey value 1 (secondary text, rules) | `#6E6E6A` |
| Grey value 2 (tints, disabled, texture fields) | `#BDBBB4` |
| Signal red (one element per view) | `#E3241B` |
| Deep grey field (inverted panels) | `#2B2B29` |

The greys are warm steps of the ink, and light, small, tight type *becomes* a grey.

## Form, line & typography
- **One family, many voices.** Univers (Frutiger, 1957) gave Ruder a numbered matrix of weights and widths plus a steep oblique. Get hierarchy from width, weight, slant and size within one family, never from a second typeface.
- **Typographic texture.** Judge each text block by its grey value, and compose the page as a pattern of greys.
- **Optical over geometric.** A true circle looks too wide, so trust the eye. Kern by counter area, not sidebearings.
- **Lowercase, flush-left, ragged-right.** A run of words reads as a line and a paragraph as a plane.
- **Free fonts:** **Archivo** (variable width 62–125 and weight 100–900, the closest Univers-style matrix), **Instrument Sans** (has a width axis), **Hanken Grotesk** (neutral grotesque text).

## Rhythm, motion & time
Ruder's rhythm is interval-based, like music. Repeat one element at sizes that grow and shrink (the 1961 covers), or change the gaps between equal elements.
- Animate **intervals** (gap, leading, tracking), not position. Rows breathe from 1.1 to 1.5 line-height over 400ms.
- Shift hierarchy by interpolating `font-variation-settings` (`wdth` 75→100, `wght` 300→600).
- Stagger entrances in irregular, fixed steps (0, 60, 150, 270ms). Never bounce: ease out for about 300ms, then stillness.

## UI translations
1. **Layout:** Build on a 6-column grid. Each section takes a different module footprint (4/2, 2/4, 3/3 offset by one), and none repeats on a screen.
2. **Void:** Make the hero 60% empty paper, with the headline block pinned to the lower-left third and the body text 1.5 columns to its right, top-aligned to the headline's x-height.
3. **Counter-aware spacing:** Space display text optically (`font-kerning: normal` plus manual tracking of -1 to -2% on bold widths). Check that the gaps between letters match the area of the letters' counters.
4. **Type:** Use one variable family everywhere, varying only axes and size: H1 at `wdth 75, wght 700, 64px`, labels at `wdth 112, wght 400, 11px`.
5. **Texture:** Set metadata at 11px weight 300 with tight leading, so it reads as a grey plane balancing one black headline.
6. **Color:** Allow one red per view, for the most important state (unread, live, error), never for decoration.
7. **Parallel columns:** Show comparisons as equal-width columns of honest, unequal length. Don't equalise card heights.
8. **Rules:** Separate with 1px Grey 1 rules that end at column edges. No boxes or shadows.
9. **Motion:** On hover, a row's `wdth` goes from 85 to 100 and its gap grows by 4px. Nothing translates.
10. **Interaction:** Show selection as a change of grey value (Grey 1 → Ink, weight 400 → 500), not a filled pill.
11. **Scale jump:** Pair one numeral 8–12× body size with tiny text in the same family. No imagery.

## What this artist would reject
- Centred hero stacks, which put symmetry where tension should be.
- Pairing two or three typefaces for "personality" when one family's widths and weights can do it.
- Equal-height card grids with uniform padding: a monotone rhythm and dead counterforms.
- Colour as decoration: gradients, brand-tinted backgrounds, multicoloured icons.
- Letterspaced uppercase labels everywhere, and geometric spacing that ignores optics.
- Bouncy, scale-pop motion that moves objects instead of adjusting intervals.

## Signature prompt seed
Design the screen as ink on warm paper. Use one variable grotesque and build all hierarchy from width, weight, slant and size. Treat white as material: compact, tight-leaded blocks float in fields that are 60% empty, set asymmetrically on a 6-column grid where no section repeats a module footprint. Compose text blocks as grey values, so a light, dense caption balances one black, condensed headline. Use only black and tonal greys plus a single red accent for the one critical state. Separate with thin rules, not boxes. Motion only adjusts intervals and axes, then stops.

## Sources
- https://en.wikipedia.org/wiki/Emil_Ruder
- https://lineto.com/articles/ruder1
- https://neugraphic.com/ruder/ruder-text2.html
- https://neugraphic.com/ruder/ruder-text5.html
- https://mail.neugraphic.com/ruder/ruder-text4.html
- https://fontsinuse.com/uses/18507/typographische-monatsblaetter-1961-no-10
- https://skillbox.ru/media/design/ruder-book/
- https://www.niggli.ch/en/produkt/typography/
- https://alistapart.com/article/whitespace
- https://www.lars-mueller-publishers.com/ruder-typographyruder-philosophy
