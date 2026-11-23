# Wolfgang Weingart — Swiss Punk / New Wave typography

## Essence
Weingart took the Basel School's own tools (Akzidenz-Grotesk, the grid, the rule, black and white) and pushed each one past its tolerance: letterspacing until words became pictures, text blocks stepped down like stairs, films stacked until halftone dots turned into texture. It is rebellion from inside the system, not outside it; he held that you could only break typographic rules after mastering them. The result looks chaotic, but every piece was set, measured and spaced deliberately by hand.

## Key works examined
- **Round Compositions, 1962** — a dropped case of 6pt Akzidenz-Grotesk tied in a ring and printed, faces and feet: accident turned into method.
- **Typografische Monatsblätter covers, 1972–73** — fifteen covers with stepped text blocks cut through by heavy black rectangles; Tschichold called him the "anti-typographer."
- **"How Can One Make Swiss Typography?", 1972** — lecture manuscript treating Swiss style as principles to question, not a style to copy.
- **Nine Collages series, 1974–75** — hand-cut films, barely legible type, overlapping halftones and moiré.
- **TM supplement, December 1976** — seven years of work: spaced-out letters, thick black text boxes, a broken grid over a desert photo, text fragments that come back on later pages.
- **Kunsthalle Basel Kunstkredit 76/77, 1977** — world-format (128×90 cm) silkscreen film collage, black and white; won a Swiss Poster Award. The B/W series ran 1976–79.
- **Kunstkredit color posters, 1980–83 (e.g. 1981, offset)** — layered dot screens in process colors held together by an irregular, wide border.

## Space & composition
- **The grid is visible so it can be violated.** Keep a strict 12-col Swiss grid, then offset one block by half a column and let a black bar cross two others. The break only reads because the structure is obvious.
- **Staircase blocks.** Text is set as a run of short lines, each indented one fixed step (e.g. 2–4ch) further than the last, so the block's edge becomes a diagonal. Stack 2–3 of these at different step sizes for counter-rhythm.
- **Heavy rectangles as structure.** Solid black bars and boxes (often 20–40% of a block's area) are compositional weights, not decoration. They hide, divide and underline.
- **Collage density inside a calm frame.** The Kunstkredit posters pack fragmented images into the center, held by a wide, uneven margin (around 8–12% of width, deliberately unequal on each side). Dense core, quiet edge.
- **Layer, don't place.** Elements overlap by design. Assume a z-axis of 3–5 translucent planes rather than a flat flow.

## Color
The logic is reprographic: black, paper, and the halftone in between. When color arrives (1980s), it is process ink overprinted, so overlaps make a third color. Use `mix-blend-mode: multiply`.

| Hex | Role |
|---|---|
| `#F2EFE8` | Paper ground, slightly warm newsprint |
| `#111111` | Ink: type, bars, solid blocks |
| `#8A8A85` | Halftone grey: dot-screen fields, secondary type |
| `#00A0D6` | Process cyan, overprint layer 1 |
| `#E4007C` | Process magenta, overprint layer 2 |
| `#FFE100` | Process yellow, small highlight plane only |

Rule: most screens stay in black and grey. Use at most two process colors per view, always overlapping each other.

## Form, line & typography
One grotesque in a few weights, fully exploited: extreme tracking (`letter-spacing: 0.5em–1.2em`) on a single word so it reads as a shape; tight negative tracking (−0.04em) on the block next to it; mixed sizes within one line; heavy horizontal rules; type reversed out of black bars; words split across lines or across the page. Lines are type-high rules: horizontal, thick, sometimes cut off sharply.
Fonts: **Archivo** (grotesque with variable width, so it can do Akzidenz-like stretching and condensing), **Inter Tight** for dense small text, **Archivo Black** for knockout bars.

## Rhythm, motion & time
Weingart compared typographic unity to musical composition, so motion should feel syncopated rather than eased. Blocks enter in steps (`steps(4)` timing, 60–80ms per step) so a staircase builds one tread at a time. Letterspacing animates: on hover, tracking opens from 0 to 0.6em and the word dissolves into a pattern. Layers slip against each other on scroll at different rates (parallax of 0.9/1/1.15), and grain or halftone fields shift 1–2px, like misregistered film. A text fragment seen earlier comes back later in the flow, a callback.

## UI translations
1. **Layout:** Build on a visible 12-col grid, then shift exactly one module per screen by 0.5 column and let it overlap its neighbor.
2. **Layout:** Set section intros as staircase blocks, with each line indented `calc(var(--step) * n)`, where `--step: 3ch`.
3. **Type:** Track one display word to 1em+ and set it at the same size as body text. Readability shouldn't depend on size; the spacing alone makes it a headline.
4. **Type:** Reverse key labels out of solid black bars that run past the text by an uneven amount on one side, e.g. 2ch left and 9ch right.
5. **Color:** Overlap cyan and magenta planes with `mix-blend-mode: multiply` behind a hero image; never use either color as a flat button fill.
6. **Texture:** Replace gradients with a coarse halftone (`radial-gradient` dot pattern, 4–6px pitch) masked onto images and empty fields.
7. **Composition:** Frame dense dashboards with a wide margin whose sides are deliberately unequal, e.g. 6% left and 11% right.
8. **Motion:** Reveal content in `steps()` jumps, not smooth easing. Each line of a staircase lands one beat after the previous one.
9. **Interaction:** On hover, open a word's letterspacing and slide a black bar under it; on press, offset the layer 2px like a registration error.
10. **Repetition:** For loading or empty states, repeat one word 3–5 times down a column, widening the tracking each time.

## What this artist would reject
- Center-aligned hero text sitting in symmetrical padding.
- One uniform tracking value across the whole design system.
- Soft drop shadows and rounded cards that fake depth instead of literally layering planes.
- Decorative gradients and pastel tints with no reprographic logic.
- Rule-breaking without a visible grid to break: random "brutalism" with no system underneath.
- Icons standing in for words when typography alone could carry the message.

## Signature prompt seed
Design this screen in the manner of Wolfgang Weingart. Use a strict, visible 12-column Swiss grid on warm newsprint (#F2EFE8), and break it once: one module offset half a column, crossed by a solid black bar. Set Archivo in two weights only. Track one word to 1em so it becomes an image; set intros as staircase blocks stepping 3ch per line; reverse labels out of black bars. Add a coarse halftone field and overprint cyan and magenta with multiply. Reveal in stepped jumps, never smooth eases. Keep a dense core inside an uneven wide margin.

## Sources
- https://www.aiga.org/membership-community/aiga-awards/2013-aiga-medalist-wolfgang-weingart
- https://eyeondesign.aiga.org/museum-of-design-zurich-unveils-the-weingart-archive/
- https://letterformarchive.org/news/from-the-collection-legacies-of-swiss-style-part-2-wolfgang-weingart/
- https://www.neugraphic.com/weingart/weingart-text3.html
- https://www2.palomar.edu/users/gkelley/Weingart.html
- https://www.galerie123.com/en/original-vintage-poster/34174/kunstkredit-197677-kunsthalle-basel
- https://www.galerie123.com/en/original-vintage-poster/34249/basel-1981-kunstkredit