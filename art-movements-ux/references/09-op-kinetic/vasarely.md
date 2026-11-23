# Victor Vasarely — Op Art

## Essence
Vasarely turned painting into a combinatorial system: a colored square with a contrasting form cut into it (the "plastic unit") is one letter of an alphabet that assistants, factories and the public could all use. Depth and movement aren't drawn in. They come from programmatic variation across a grid, where small shifts in each cell's size, hue or tone make the flat surface swell, sink or vibrate.

## Key works examined
- **Zebra (1937):** two interlocked zebras made only of black and white stripes on black, with no outlines. Contour can come entirely from where a pattern changes.
- **Vega III (1957–59) → Vega-Nor (1969, 200×200 cm):** a checkerboard that swells into a sphere. Distorting the grid creates volume without any shading.
- **Unités plastiques (patented 2 March 1959):** forms are cut from a colored square and recombined. This is the first design token system, in all but name.
- **Folklore Planétaire (presented 1963):** the alphabet is published as a numbered palette of about 16 colors and 17 forms, meant to be a universal, industrial visual language.
- **Planetary Folklore Participants No. 1 (1969):** a magnetic relief kit (edition of 3,000) with 390 coded elements in 19 colors and "programmation" sheets for recording layouts. A design system shipped to users.
- **Renault losange (1972, with Yvaral):** a diamond made of parallel stripes, with opposite corners offset so it reads as 3D. Renault used it for about 20 years. Op Art compressed into a brand mark.

## Space & composition
- **The square cell is the only container.** Use a strict square module, such as 8×8 or 12×12 cells, filling a square or near-square field. Avoid 12-column gutters. Cells touch edge to edge with no gaps, and any spacing comes from the inner form shrinking inside its cell.
- **Each cell has two layers:** a ground square and one inner figure (circle, square, rotated square, ellipse, half-disc), inset at 60–85% of the cell size. Figure and ground swap colors across the field.
- **Use a field-wide displacement function rather than local layout.** The Vega bulge is a radial lens: cells near a focal point grow to about 1.6× and cells at the edges compress to about 0.7×. The composition has one focal point, often off-center, and the eye drifts toward its peak.
- **No empty space.** Calm areas come from cutting contrast between neighboring tones, not from leaving blanks.

## Color
Vasarely's numbered palette had three reds, three greens, three blues, two violets, two yellows, black, white and grey. The logic is **tonal ramps across the grid**: hue fixed along one axis, value stepping along the other. Figure and ground contrast strongly within a cell, but neighboring cells differ by one step, so the field shimmers instead of clashing.

| Role | Hex |
|---|---|
| Deep ground / night field | `#0E0F1A` |
| Ultramarine (primary ramp anchor) | `#2433A6` |
| Violet (ramp midpoint) | `#6A2C91` |
| Vermilion (warm accent / focal) | `#E0402A` |
| Chrome yellow (highest-energy figure) | `#F4C21B` |
| Emerald (counter-ramp) | `#15936A` |
| Paper white | `#F3F1EA` |

Use these as endpoints; interpolate 6–9 OKLCH lightness steps per hue.

## Form, line & typography
The shapes are a short list of hard-edged, strokeless primitives: circle, square, lozenge, ellipse, split disc. Line appears only as **stripe fields** (Zebra, Renault), where a contour is just a change in stripe direction or phase. Type should be geometric sans in caps, tracked 0.2em or more so letters read as units in a row.
- **Jost** (Futura-like) for headings and UI.
- **Rubik Mono One** for blocky display numerals.
- **Space Mono** for unit codes like "C-12 / R3," echoing the codes on the Folklore tiles.

## Rhythm, motion & time
Motion is a **wave of value or scale passing through the grid**, never an object moving across it. On hover or focus the lens moves to that element, and neighbors scale by distance (CSS `scale` from a `--d` custom property, 300–500ms, ease-in-out). Load-in sweeps tones diagonally, 15–25ms per cell. Stripe fields shift phase a few pixels on scroll, echoing his Kinetic-period layered Plexiglas. Under `prefers-reduced-motion`, freeze the bulge; the illusion works when still.

## UI translations
1. Build every surface from one square token, `--u` (e.g. 56px): cards, avatars, buttons are 1u, 2u or 4u, never off-multiple rectangles.
2. Define components as **ground + inner form + color index**, e.g. `<Unit form="disc" ground="blue-3" figure="yellow-1">`. Style variants are permutations, not new designs.
3. Place a Vega-style radial lens on the dashboard: the main KPI tile sits at the bulge peak at 2×, and surrounding tiles scale down with distance.
4. Color each list row one step further along a ramp (`blue-1` → `blue-7`) to show order or time, so the sequence is visible before anyone reads it.
5. For states, swap figure and ground instead of adding a border or shadow: a selected tile inverts its two colors.
6. Draw empty/loading states as 4px Zebra stripe fields, with shapes defined only by a 90° stripe turn.
7. Build the logo or hero mark from offset parallel stripes, with opposite corners shifted in opposite directions, to get depth with no gradients.
8. Ship a "Folklore" mode where users rearrange their home grid, saved as a shareable code (`D3-B5-Y1…`).
9. Set headings in widely tracked Jost caps; label swatches and forms with catalogue codes in Space Mono.
10. Break the system exactly once per screen: one inverted unit marks the main call to action.

## What this artist would reject
- Drop shadows and blur as depth; depth comes from distortion.
- One-off hero illustrations outside the component grammar.
- Beige-and-grey neutrals with a single brand accent.
- Rounded rectangles with arbitrary padding and radii.
- Outlined icons and hairline borders; edges are meetings of flat color.
- Layouts users can't recombine.

## Signature prompt seed
Design this app screen as a Vasarely plastic-unit field. The whole canvas is a seamless grid of square cells, each a flat colored ground holding one inset geometric form (disc, square, lozenge, ellipse). Components are permutations of form and numbered color, never one-offs. Run ultramarine-to-violet tonal ramps across rows, with chrome yellow and vermilion figures. Bulge the grid radially around the primary content so its tiles swell to 2× and the edges compress. Show states by inverting figure and ground, and use Zebra stripes for emptiness. Set the type in tracked geometric caps. Interactions send scale waves through neighboring cells.

## Sources
- https://www.theartstory.org/artist/vasarely-victor/
- https://en.wikipedia.org/wiki/Victor_Vasarely
- https://www.fondationvasarely.org/planetary-folklore-period/
- https://sainsburymuseum.com/art-and-objects/31237-planetary-folklore-participants-no-1/
- https://vertufineart.com/news/24
- https://www.artchive.com/?p=249205
- https://www.autosphere.fr/blog/renault-le-logo-vasarely/
- https://www.renaultgroup.com/en/magazine/our-group-news/sharing-the-diamond-at-the-vasarely-foundation/
- https://www.lacma.org/lab/project/metavasarely
