# Vilmos Huszár — De Stijl

## Essence
Huszár treated a composition as a field of separate rectangles that can be shuffled: letters, rooms, a puppet's limbs and a cigarette girl's face are all assembled from the same flat, interchangeable planes. Where Mondrian held still, Huszár made the planes move (the dancing figure), wrap round space (the interiors) and sell things (Miss Blanche).

## Key works examined
- **De Stijl masthead/cover, 1917 (used until 1921)**: a woodcut in which black rectangles of varied size spell "De Stijl" on white, above a block of justified text. Lettering is built from the same units as the image.
- **Bruynzeel boys' bedroom, Voorburg, 1918–c.1920**: Huszár did the color and Klaarhamer the furniture. One color scheme runs across cupboard, beds, carpets, cushions and four stained-glass windows, so color is the system holding the room together.
- **Mechanical Dancing Figure, 1920**: a key-and-string marionette about 1 m tall with transparent red and green planes, projected as a silhouette on a lit screen at Dutch Dada soirées. Each pose makes a new composition.
- **Space-Color-Composition, Juryfreie Kunstschau Berlin, 1923**: the wall reads "color by Huszár / form by Rietveld". Color and structure are credited as separate layers.
- **Miss Blanche Virginia cigarettes, 1926–28**: a full identity covering packaging, press ads, display cards, coupons, a mirror case and an ad cart. It shows the "New Woman" through flat geometric planes, with variant labels (Yellow, Green) coded by color.

## Space & composition
- **Rectangles as tiles, not lines.** Unlike Mondrian's black grid, Huszár's early work leaves out the dividing bars. Blocks float on white and touch only at corners or across narrow gutters. The white between them is part of the figure.
- **Multiple sizes from one module.** The masthead uses a small family of rectangle sizes, roughly 1×, 2× and 3× a base unit, packed into a dense, uneven cluster. Density is high in the cluster and zero around it, with no middle tones.
- **Image block over text block.** The cover stacks a charged, irregular mosaic over a calm, fully justified slab of type. Wild and still share one column width.
- **Color can be detached from form.** In the Berlin room, color planes were laid across walls, floor and ceiling regardless of where the architecture breaks. A blue plane may turn a corner. Color is its own layer over the structure.

## Color
The logic is primaries used as **separable planes**, each a solid field with hard edges and no gradients. In the projected figure, transparent red and green overlap to make a third tone, so color is added up by stacking layers. In the Miss Blanche range, a hue marks a product variant (yellow label, green label). That is color as data, not decoration.

| Hex | Role |
|---|---|
| `#F4F1E8` | Ground: warm paper white, the dominant field |
| `#141414` | Woodcut black: structural blocks, letterforms |
| `#D7261E` | Signal red: one active plane per view |
| `#1F4FA3` | Primary blue: secondary plane, links/selected |
| `#F2C200` | Yellow: highlight / variant code A |
| `#2E8B57` | Transparent green (use at 60–70% opacity): overlay/variant code B |
| `#9A9A94` | Interior grey: neutral surfaces, disabled |

## Form, line & typography
The 1917 masthead letters are pixel glyphs: every stroke is a rectangle, and counters are leftover white. That maps straight onto a bitmap/grid face for display, set beside a sturdy grotesque in justified blocks for body text. Corners are square (radius 0), and line weight is replaced by **block weight**. Fonts that fit (Google Fonts): **Silkscreen** (constructed block letters, display only), **Space Grotesk** (body, square-shouldered), **Archivo Black** (heavy titling for justified slabs).

## Rhythm, motion & time
Motion is **pose-to-pose**, not fluid. Like the marionette's key mechanism, elements jump between a few discrete states (steps(), not ease-in-out). Each state should be a complete, balanced composition. Color planes can slide over one another with opacity, so new tones appear where they cross. Hover and press move a plane by a whole grid unit, never by a few nudging pixels. A loading state can be the logo's rectangles rearranging between two or three fixed configurations.

## UI translations
1. Build the wordmark/hero title from absolutely positioned rectangles on an 8px module (sizes 1u/2u/3u). No font for the signature element.
2. Remove the visible grid lines between panels. Separate cards with 8–12px gutters of the ground color, so white does the dividing.
3. Stack a dense, irregular rectangle cluster (top 40% of the screen) over a fully justified text slab (`text-align: justify; hyphens: auto`) of exactly the same width.
4. Put color on a separate token layer from components. Let a single colored plane span two unrelated cards or wrap from header into sidebar, ignoring component boundaries.
5. Code product tiers or categories with one flat primary each (yellow tier, green tier) and apply it to the whole card surface, not a little badge.
6. Animate between states with `animation-timing-function: steps(3)`. Every intermediate frame must look like a deliberate composition.
7. On drag or hover, translate panels by whole module units (`transform: translate(calc(var(--u)*2))`), never by fractional pixels.
8. Overlap two translucent color planes (`mix-blend-mode: multiply`, 65% opacity) to mark an intersection, e.g. a filter AND a selection.
9. Allow exactly one red plane per viewport, used for the primary action or current state.
10. Use radius 0 and no shadows. Depth comes only from overlap order and opacity.

## What this artist would reject
- Gradients, glassmorphism blur, soft shadows: planes must stay flat and hard-edged.
- Color stuck to component edges, like a tinted card border or an accent stripe on a button.
- Smooth, springy easing everywhere. He wanted deliberate, readable poses.
- Visible hairline grids and dividers. The ground should separate things.
- A logo that is just a font in a weight.

## Signature prompt seed
Design the screen as a field of warm off-white in which flat, hard-edged rectangles float, separated by gutters of ground color rather than lines. Build the title from the same 8px block module as the imagery, then set body text in a fully justified slab matching the cluster's width. Treat color as an independent layer: a single red plane, plus blue and yellow fields that cross card boundaries, with translucent green overlapping to make new tones. Zero radius, no shadows. Transitions snap through two or three complete poses using stepped timing, like a marionette changing position.

## Sources
- https://en.wikipedia.org/wiki/Vilmos_Husz%C3%A1r
- https://sammlung-online.berlinischegalerie.de/en/collection/item/208503
- https://www.centraalmuseum.nl/en/explore/collection/modern-and-contemporary-art/27425-vignet-voor-de-stijl-vilmos-huszr
- https://www.centraalmuseum.nl/en/explore/collection/modern-and-contemporary-art/28600-maquette-ruimte-kleur-compositie-voor-de-juryfreie-kunstschau-in-berlijn-vilmos-huszr
- https://www.stedelijk.nl/en/collection/88175-vilmos-huszar-de-stijl.-maandblad-voor-de-beeldende-vakken
- https://stedelijk.nl/en/collection/17158-vilmos-huszar-miss-blanche-virginia-cigarettes
- https://static1.squarespace.com/static/5e68e6f8d34bcf00a52fd5a6/t/60883236b0fda25665468381/1619538492971/Miss+Blanche.pdf
- https://www.european-traveler.com/?p=29945
- https://medium.com/fgd1-the-archive/100-years-of-de-stijl-e532e0a83160
- https://bulletin.rijksmuseum.nl/article/view/9783
