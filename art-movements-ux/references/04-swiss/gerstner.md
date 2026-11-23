# Karl Gerstner — Swiss International Typographic Style

## Essence
Gerstner designed the rule set, not the layout. He held that "the formula creates the form." A design is one selection from a space of possibilities that he defined explicitly: a grid that holds several column counts at once, a morphological box of typographic parameters, a color sequence. Each piece looks like one frame from a system you could keep running.

## Key works examined
- **Designing Programmes (1963/64)** *(retry pass, visually checked: 10 spreads of the Lars Müller Publishers edition)*: a two-column book with wide white heads, black and white throughout. Spreads seen: Pro-Programmatic essay; the Ostwald grid of 18 line patterns from one square (3×6); 16 car photos in a 4×4 grid from one viewpoint programme; Bech Electronic Centre permutations (one word set vertically/horizontally in 6 variants, black squares); a 4×4 matrix of the letter "n" stepping width and weight, and a 4-angle roman-to-italic series; *The Tangential Eccentric* 1956/57 (black circle cut by grey bands). It argues that the designer should "create structures from which single solutions can be derived." Describing the problem is already half of solving it.
- **Mobile grid for *Capital* (1962–63)** *(not obtained; the 58-unit arithmetic is unverified against an image)*: one 58-module field that contains the 1-, 2-, 3-, 4-, 5- and 6-column grids together. The grid is responsive in print, decades before the term existed.
- **Morphological box of the typogram (in *Designing Programmes*)** *(retry pass, visually checked: LMP spread)*: a ruled table of 13 parameters in 4 groups: Basic (components, typeface, technique), Colour (shade, value), Appearance (size, proportion, boldness, inclination), Expression (reading direction, spacing, form, design). Each row has 3–5 numbered values (11, 12, 13…) and ends in "Combined", so every row allows a mix. A mark is made by choosing one value per row. It is a design-token matrix in all but name.
- ***Schiff nach Europa* (1957)** *(not obtained)*: grotesque type only, on a complex grid, where the typography itself builds the image. This is "integral typography."
- **Color Sound series (1968–73; *Lavender on Orange*, 1972, serigraph, 31½ in square)**: square fields where nested bands step through a scientifically ordered hue or value scale. The color is produced by a rule. *(Lavender on Orange not obtained; visually checked instead: **Color Sound 15**, 1973, book illustration, Cooper Hewitt.)* On a **neutral near-black ground (64% of the surface)** a T of nested tiers steps through **equal increments of hue and lightness**: the wings go grey → green-grey → teal → blue (L 23 → 29 → 33 → 36 → 40), and the centre column continues blue → violet in five steps (L 42 → 47, constant chroma ≈50). Each tier is inset a few pixels inside the last, so the edges read as thin concentric stair-steps. The sequence is one cool ramp, not two complementary poles.
- ***Aperspektive 0* (1952/53)** *(not obtained)*: the right edge continues into the left and the top into the bottom. The picture is a tile, so it can extend without end.
- **Linsenbild (1964) and alterable multiples** *(not obtained)*: viewers move parts to produce variants.
- **Holzäpfel Büromöbel poster (GGK, 1950s/60s)** *(added; visually checked: Stedelijk)*: the programme made visible on one sheet. A single photo module (three men at a desk) is repeated **four times at descending scales (≈1, 0.7, 0.45, 0.3, estimated from the scan) and rotated in 90° steps**, with the wordmark in one orange-brown riding each copy. The desk front is three flat greys. No layout decision is made by eye: every copy is the same unit under a different transform.
- ***Kompendium für Alphabeten* (1972)** *(not obtained)*: a taxonomy of every way type can be treated. It reads like a parameter catalog.

## Process (derived)
*From observation to process (see SKILL.md §1). This is what transfers; the rest of the file is evidence.*

**Karl Gerstner.** *Do not compose: list the parameters of the problem, give each a short ordered row of values, and treat every design as one selection, so the set of selections is the work.*
Process:
1. Write the problem as a table before drawing anything: 10–15 parameters in 3–4 groups (what it is made of, its colour, its appearance, its expression), each with 3–5 numbered values and one "combined" value. A parameter with one value is a constant; move it out of the table.
2. Order every row as equal steps between two poles, so a value is an index, not a name. Size, proportion, weight, slant, direction and colour all step this way (seen: width × weight as a 4 × 4 matrix; scale ≈1, 0.7, 0.45, 0.3; turns of 90°).
3. Fix ONE unit (a word, an image, a component) and allow only the transforms in the table. A variant is one value per row; a value outside the table means the table must be changed for every variant, not this one adjusted.
4. Give the field the same treatment: one module, every width, height and void a whole number of modules, and only the divisions that the module arithmetic admits (see Space and line).
5. Build colour as a ramp by the rule of step 2: between two poles, hue and lightness move together in equal steps (≈3–5 L per step, chroma constant) on a neutral ground that keeps the majority (≈64%). Neighbouring steps touch, each nested or inset in the last, so the edges themselves show the increment.
6. Show the programme at least once: several selections of the same unit side by side (4–16 of them), so the viewer can read the rule from the differences.
Why it works:
- Variation of one thing under visible constraints is read by comparison: with the unit constant, every difference is attributable to one parameter, so the system explains itself. Hand-tune one variant and the differences stop being readable.
- Equal steps make a scale perceptually even, so position in the row can carry meaning (first to last, low to high) without a legend of names. Unequal steps turn a scale into a set of unrelated swatches or sizes.
- Deciding in the table moves judgement to where it is cheap and shared: a wrong value is fixed once for all cases. Deciding per layout hides the rule and multiplies exceptions.
Colour relations: neutral ground ≥60%; one ramp of 5–9 steps between two poles; adjacent steps differ by 3–5 L, which separates regions but cannot carry text, so text is set only on a step far enough along the ramp to reach 4.5:1, and step meaning is always doubled by position or a printed index; a second, complementary pole is unverified.
Space and line: one module. Correct arithmetic for a field that holds several column counts: pick a period `P` divisible by every count wanted and a gutter `g` in the same units; the field is `P − g` units; a `k`-column division has columns `P/k − g` wide starting every `P/k` units. With `P` = 60 and `g` = 2 the field is 58 and the columns are 28, 18, 13, 10 and 8 for 2–6. In CSS this is 58 gapless tracks with each gutter as two empty tracks (`column-gap: 0`); `repeat(58,1fr)` with a gap, or without reserved gutter tracks, does not hold the divisions. The attribution of this field to the "Capital" grid is unverified (no image obtained); treat it as a hint.
Type requirement: one family whose widths, weights and slants form a full matrix, so each axis can be a row of the table; sizes on a scale tied to the module; ranged left.
Motion and interaction: motion is permutation: a change of selection snaps to the next value in its row (150–200ms, or stepped), never through values that are not in the table. One visible control lets the user turn a parameter; that control has a 44px target and a text label of the current value.
Fails when: there will only ever be one or two instances (the table costs more than it returns); the content is a single authored narrative that needs one exception; a parameter cannot be ordered (brand names, legal categories), so index carries no meaning.
Signature (do not carry together): nested bands stepping through a cool colour ramp · one photograph repeated at descending scales and turns · a ruled parameter table set in grotesque.

**Transfer test** (an illustration that the process survives new colours and content; never reuse its hues, layout or wording as a design answer):

Recipe app in warm cream and terracotta (phone and tablet; serif titles, food photography, soft corners).
1. *Table.* 12 parameters in 4 groups. Made of: photo / title / time badge. Colour: ramp step (1–6), photo treatment (3). Appearance: card size (4), proportion (3), title weight (3), slant (2). Expression: reading direction (2), spacing (3), crop (4), density (3).
2. *Rows.* Card sizes step 1, 0.7, 0.5, 0.35 of the column; title weights 400, 550, 700; crops step from whole dish to detail in four equal zooms.
3. *Unit.* One recipe card. "Tonight's pick" is selection 4-1-3-2…, not a special component. A request for a wider badge added value 4 to the badge row, for all cards.
4. *Field.* Module 12px. The tablet content field is 58 modules = 696px, as 58 gapless tracks: 2 columns of 28 for features, 3 of 18 for the index, 6 of 8 for ingredient chips, with 2-module gutters as empty tracks. All voids are whole modules (the hero void is 13).
5. *Ramp.* Cream ground 66%. Six steps from cream toward terracotta, 4 L darker and a fixed hue shift per step. Step index = cooking time band; the band is also printed as "≤15", "≤30"… on the card, and text uses step 1 on step 6 only.
6. *Specimen.* The "variations" tab shows one recipe as 12 cards, three rows of four, each differing from its neighbour in one parameter.
- *Motion.* Switching the index from 3 to 6 columns snaps in 180ms. The density control is a 48px segmented switch labelled "comfortable / regular / dense".
Result: a warm, photographic cooking app with a serif. No grotesque, no cool ramp, no black ground. What survived is the parameter table, equal-step rows, one unit under transforms, and a view that shows the set.

## Space & composition
- **Use a common multiple, not a fixed column count.** The *Capital* math: 58 units with 2-unit gutters gives 2×28, 3×18, 4×13, 5×10 or 6×8, and each one adds back up to 58. Every module boundary is shared by several grids, so a 3-column story can sit beside a 4-column caption block and still align.
- **Mix column counts on the same page.** Asymmetry comes from combining grids, not from nudging by eye. Dense ragged-right blocks (he brought flush-left setting to Geigy in 1954) sit next to voids that are exact module multiples.
- **Treat edges as continuations** (Aperspective): pattern bands tile seamlessly, never "ending."
- **Size voids in units.** Empty space is always 4, 9 or 13 modules wide. It is never just "some padding."

## Color
*The hex table below is a reference sample for strict studies and homage only. For design, use the colour relations in "Process (derived)".*

Color is a **sequence generated by a rule**, never a picked palette. Color Sound works step a hue through measured intervals, so the chord works because the steps are equal. Use two poles and interpolate between them. In Color Sound 15 the poles are a neutral near-black and a blue-violet, and the ramp moves hue and lightness together (≈+3–5 L per step); the orange pole of *Lavender on Orange* is *unverified* (not obtained).

| Role | Hex |
|---|---|
| Ground (dark pole: neutral near-black in Color Sound 15, not violet) | `#353533` |
| Step 2 (teal-grey) | `#365360` |
| Step 3 (lavender: violet end of the centre column) | `#6469B9` |
| Complementary pole (no orange in checked works; nearest real: Holzäpfel wordmark orange-brown, muted in the scan) | `#93745C` |
| Mid warm step (nearest real: Holzäpfel warm grey) | `#B3ADA1` |
| Paper / text ground (Holzäpfel) | `#F0E8D6` |
| Text ink (Holzäpfel photo dark) | `#4B4846` |
| Blue step (Color Sound 15 centre top) | `#3163B6` |
| Green-grey step (Color Sound 15 wing) | `#394945` |

Build steps with `color-mix(in oklch, …)` at fixed 20% increments, or generate them in OKLCH with constant ΔL.

## Form, line & typography
Grotesque only. The type is the image, and words are set so their shape carries the meaning. Ranged left, tight leading on headlines, and one weight jump per hierarchy level. Type sizes come from a modular scale tied to the grid module, so cap heights and baselines land on module lines. Treat the logo or wordmark as one cell of a morphological box: weight × case × width × rotation × colour step.
Fonts: **Inter Tight** (closest free stand-in for Akzidenz), **Archivo** (has width axes, good for parametric variants), **Space Grotesk** (for systematic playfulness).

## Rhythm, motion & time
Motion is **permutation**. Elements reflow between the 2-, 3-, 4- and 6-column states on the shared 58-unit field, snapping to module lines with a short, linear-ish ease (150–200ms). Color transitions step through the defined scale (`steps(5)`) rather than blending smoothly. Patterns tile and scroll endlessly. Let the user turn a parameter and watch the system answer, as his multiples did.

## UI translations
1. Define the layout as `grid-template-columns: repeat(58, 1fr)` with spans of 28/18/13/10/8 plus 2-unit gutters. Let components choose their own column count on the same field.
2. Put two incompatible column rhythms side by side on every screen, for example a 3-col article beside a 4-col data rail. They align only at shared module lines.
3. Model components as a morphological box: list the parameters (size, weight, color step, density, orientation) as tokens and render each variant as one row selection. Never hand-tune a one-off.
4. Generate the palette from two poles in OKLCH at equal steps, moving hue and lightness together (Color Sound 15: ≈+4 L and a fixed hue increment per step). Assign meaning by step index (step 1 = surface, 5 = action), never by "brand blue."
5. Set all text in one grotesque, flush-left/ragged-right, with sizes snapped so baselines fall on a 4px multiple of the module.
6. Make the hero typographic: compose the headline so its letterforms *are* the illustration, through cropping, scale and line breaks that carry meaning.
7. Size empty regions in whole modules (e.g. 13 units of void), and expose them in dev overlays.
8. Animate layout changes as snaps between grid states. Animate color with `steps()` through the scale, not continuous gradients.
9. Give one interactive control (a dial or segmented slider) that permutes a visible parameter of the page, such as column count, color step or type width, so the system shows itself.
10. Ship a "specimen" view: a matrix of all valid variants of a component, laid out like the *Kompendium*, or, as on the Holzäpfel poster, the same component shown at several scales and 90° rotations on one canvas.

## What this artist would reject
- One-off components designed by eye with arbitrary padding (`13px`, `margin: auto` "because it looked right").
- A single fixed 12-column grid with every element spanning 4/8/12, monotonous and unrelated to the content.
- Palettes picked from a mood board with no ordering logic between swatches.
- Decorative stock illustration where typography could carry the message.
- Centered, justified body text and mixed type families used for "personality."
- Soft, continuous easing applied to everything with no link to the structure.

## Signature prompt seed
Design this screen as one output of a programme, not as a composition. Lay it on a 58-unit grid holding 2-, 3-, 4-, 5- and 6-column divisions at once, and place a 3-column text block against a 4-column data rail that aligns only at shared module lines. Set everything in one grotesque, flush-left, with a typographic hero whose cropped letterforms are the image. Derive the colors as equal OKLCH steps from a neutral near-black through teal and blue to violet, moving hue and lightness together. Show a small permutation control that reflows columns and steps color, so the user sees the rule generating the form.

## Sources
- Images checked: Color Sound 15 (Cooper Hewitt 68766123) https://images.collection.cooperhewitt.org/96112_3e209dc6ce99ffed_b.jpg ; Holzäpfel Büromöbel (Stedelijk 56418) https://s3-eu-west-1.amazonaws.com/production-static-stedelijk/images/adlib/affiches/hiresafgeleiden/cz308-1748664413101.jpg
- https://ms-studio.net/notes/karl-gerstners-layout-grid/
- https://www.eyemagazine.com/review/article/the-designer-as-programmer
- https://artequalswork.com/posts/designing-programmes/
- https://medium.com/svilenk/what-i-learned-from-the-2-000-elusive-design-book-designing-programmes-f518faefcf4b
- https://jonathanzong.com/assets/jzong-gerstner.pdf
- https://davidgibsonwriting.substack.com/p/the-sound-of-vision
- https://high.org/collection/lavender-on-orange/
- https://www.hauskonstruktiv.ch/en/artists/karl-gerstner
- https://www.moma.org/calendar/exhibitions/2545
- Retry-pass images (publisher reproductions, analysis only): https://www.lars-mueller-publishers.com/designing-programmes-0 (sites/default/files/styles/large_uncropped/public/2026-02/Gerstner_Designing_Programmes_01 … _10.png)
