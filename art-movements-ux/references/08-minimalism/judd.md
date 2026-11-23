# Donald Judd — Minimalism

## Essence
Judd made boxes that are neither painting nor sculpture: factory-made units, identical or sized by a stated number series, set out in real space as "one thing after another" (*Specific Objects*). Nothing balances anything else. The order comes from interval, material and the whole run of units, never from a focal point.

## Key works examined
- **Untitled (Stack), 1967 (MoMA)**: twelve galvanized-iron boxes, each 9" high with 9" gaps. Solid and void are equal, and the unit count is cut down to fit the ceiling. It teaches gap = element, and that the count may change while the module stays fixed.
- **Untitled (progression), 1967 (Indianapolis)**: red boxes grow geometrically from right to left while the voids shrink. The last box is 16× the length of the first. It teaches one rule that drives both the solids and the spaces between them.
- **Untitled, 1969 (Van Abbe)**: polished aluminum blocks sized 1, 1, 2, 3, 5, 8, 13, 21. It teaches a spacing scale you can see, not one hidden in tokens.
- **Untitled, 1973 (Tate)**: copper. Each protrusion is 1.5" wider than the one before. It teaches arithmetic steps as an alternative to Fibonacci.
- **100 untitled works in mill aluminum, 1982–86 (Chinati, Marfa)**: every box is 41 × 51 × 72", set in a strict three-row grid. Each interior is different: halved vertically, horizontally or diagonally, with single or double walls 100 mm apart. It teaches a fixed outer shell with a different inside every time.
- **Furniture and "It's Hard to Find a Good Lamp," 1993**: rectangular volumes in pine, plywood and sheet metal. Judd held that a chair is judged as a chair, and that proportion is how its reasonableness shows. It teaches that function comes first and art is not added on top.

## Space & composition
- **Non-relational.** No hero balanced by a sidebar. Every unit gets the same weight, and the series makes the order.
- **Gap equals module.** In the Stack the 9" box and the 9" void are equal. A 72px card gets a 72px gutter.
- **Stated progressions.** Size elements 1:1:2:3:5:8 or in +24px steps, and keep the series visible (stats bar, timeline, pricing ladder). As solids grow, voids shrink by the same rule.
- **Fixed envelope, variable interior.** As at Marfa, all tiles share outer proportions (about 4:5 or 5:7). They differ only in how they are split inside.
- **The wall is the ground.** Units hang in rows off a bare pale field. Density is low and even, with no clusters.

## Color
Colour is treated as material: it simply exists and depicts nothing. It goes on whole faces, never in gradients: one saturated industrial lacquer against bare metal or wood, with unpainted tops and edges showing what the object is made of.

| Hex | Role |
|---|---|
| `#F1EEE7` | Whitewashed wall: page background |
| `#BFC3C4` | Mill aluminum: surfaces, cards |
| `#8E9596` | Galvanized iron: borders, secondary text |
| `#C9A26B` | Douglas fir plywood: warm alternate surface |
| `#C8261C` | Cadmium red light: the single accent, used on whole faces only |
| `#4A2C5E` | "Hi-Fi Purple" lacquer: alternate accent, one per product |
| `#1C1C1B` | Black anodized: text |

## Form, line & typography
Right angles only. Edges are crisp because one plane meets another, not because a line is drawn. Type should feel fabricated: a neutral grotesk in sizes taken from the layout's progression, with tracked uppercase labels like a stencil on a crate. No italics, at most two weights. Fonts: **Inter Tight** or **Archivo** for UI and headings, **IBM Plex Mono** for numbers and measurements, which Judd would have listed plainly.

## Rhythm, motion & time
Meaning builds up in sequence as you walk past. Motion is serial and mechanical: a constant stagger (about 90ms), near-linear easing (`cubic-bezier(.2,0,.2,1)`), no bounce or overshoot. Hover changes the *light*, not the form. At Marfa the mill aluminum picks up sky and sunset, so let a faint sheen follow the cursor while the geometry stays still. Scrolling shows repetition with difference, never a narrative build-up.

## UI translations
1. Set the gutter equal to the module height. If list rows are 64px, the gaps between them are 64px.
2. Size a horizontal row of blocks by Fibonacci widths (1,1,2,3,5,8 × 16px) and shrink the gaps by the inverse.
3. Make every card the same outer size. Show the difference through internal splits only: a 50/50 divide, a diagonal hairline, or a recessed slot.
4. Use one accent colour, applied to a whole surface (a full card face or a full button fill), never as text links, icons or gradients.
5. Leave edges and dividers in raw material grey (`#8E9596`). The colour goes on the face, the metal shows at the edges.
6. Take type sizes from the layout's progression (13/21/34) and stop there. No in-between sizes.
7. Build a dashboard as a single row or column of equal units. No hero metric, no featured tile.
8. Stagger list entry at a fixed 90ms with linear easing. Every item behaves identically.
9. On hover, move a faint reflective gradient across the surface. Never scale or lift with a shadow.
10. Let the item count change to fit the viewport, as the Stack drops units for a low ceiling, but never change the module size.
11. Build forms like Judd furniture: square-cornered fields, stencilled labels, no ornament.

## What this artist would reject
- Rounded corners, pill buttons and soft drop shadows that fake depth.
- A big hero with balancing side elements (relational composition).
- Gradients and illustrative colour. Colour should be flat and factual.
- Decorative icons and skeuomorphic texture added on top of function.
- Bento grids with mixed tile sizes and no stated rule.
- Bouncy, playful spring animations.

## Signature prompt seed
Design this app screen as a run of identical rectangular units on a whitewashed field (#F1EEE7), one thing after another. Fix a module and make every gap equal to it. Where sizes must vary, step them by a visible rule (Fibonacci or +24px) and shrink the voids inversely. Cards share one outer size and differ only by internal splits: halves, diagonals, a recessed slot. Use mill-aluminum greys, square corners, a single flat cadmium red on one whole face, a plain grotesk at three sizes, linear staggered entry, and hover that shifts light rather than form.

## Sources
- https://chinati.org/collection/donald-judd/
- https://www.archdaily.com/777737/how-donald-judds-100-shimmering-aluminum-boxes-light-up-the-chinati-foundation
- https://www.moma.org/learn/moma_learning/donald-judd-untitled-stack-1967/
- https://en.wikipedia.org/wiki/Donald_Judd_(progression_sculptures)
- https://juddfoundation.org/wp-content/uploads/2021/11/Its_Hard_To_Find_A_Good_Lamp_1993.pdf
- https://juddfoundation.org/?p=108
- https://www.nybooks.com/articles/2017/10/26/donald-judd-visionary-real/
- https://www.britannica.com/topic/Specific-Objects
