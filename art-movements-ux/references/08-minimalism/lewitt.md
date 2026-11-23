# Sol LeWitt — Minimalism / Conceptual

## Essence
LeWitt treated art as a specification rather than an artifact: he wrote the rule, and other people or circumstances produced the output. A deliberately dull unit (a line, a square, an open cube) is run through a system until every option is used up, and the beauty comes from that complete coverage, not from taste. He is art history's parametric component library.

## Key works examined
- **Wall Drawing 47 (1970)**: a wall split into fifteen equal parts, each with a different line direction. A grid of cells, each holding one variant of a single parameter.
- **Wall Drawing 46**: "vertical lines, not straight, not touching, covering the wall evenly." The drafter supplies the jitter.
- **Serial Project #1 (ABCD), 1966 / Open Modular Cubes**: white open lattices built on a fixed ratio of beam to space (roughly 1:8.5). The module is the grammar.
- **Incomplete Open Cubes, 1974**: 122 cube frames, each with 3–11 edges, always three-dimensional and connected, with no rotational duplicates. Shown on a matrix beside diagrams and photos: a complete enumeration.
- **"Paragraphs on Conceptual Art," 1967**: "The idea becomes a machine that makes the art." All decisions are made beforehand, and execution is perfunctory.
- **Wall Drawing 1136 / 1144 "Broken Bands of Color in Four Directions" (2000s)** and **#729 Irregular Color Bands (1993)**: the same systematic logic in flat, saturated acrylic bands that meet edge to edge.
- **Wall Drawing 1152 "Whirls and twirls" (2005)**: late curvilinear bands. Playful, still flat and unmodeled.

## Space & composition
- **Divide, then fill.** Every surface is first cut into equal cells (2×2, 3×5, 4×4), and each cell gets one value of one variable: line direction, color, or which edges are missing.
- **Show the whole set.** In *Incomplete Open Cubes* the 122 units sit in regimented rows, sorted by edge count (3 edges at one end, 11 at the other). The ordering key is visible, and density increases along one axis.
- **Fixed ratio module.** The open cubes keep beam to void at about 1:8.5, so the structure is mostly air and the frame reads as a drawing in space. The ratio is the brand.
- **Coverage over focal point.** "Covering the wall evenly" means no hero. Visual weight is distributed uniformly, and hierarchy comes from sequence, not size.
- **Scale for comprehension.** Size the grid so the whole system fits in one viewport.

## Color
The early work uses graphite and black on white, and the logic is in the line. Later the palette moves to LeWitt's basic set of red, yellow, blue, and grey. These were first layered as translucent ink washes, so overlaps mix, and later laid as opaque, flat acrylic bands that meet edge to edge. Color is assigned by rule (band n gets color n mod 4), never chosen per element.

| Role | Hex |
|---|---|
| Wall / ground | `#F4F2EC` |
| Graphite line, text | `#2B2B2B` |
| Primary red | `#D2322D` |
| Primary yellow | `#F2C230` |
| Primary blue | `#1F4FA3` |
| Grey (fourth primary) | `#8C8C88` |
| Late saturated accent (orange/green mix) | `#E8742A` |

For layered states, use `mix-blend-mode: multiply` on 60%-opacity washes of the primaries, so overlap regions produce derived colors (red+yellow, blue+grey) instead of new swatches.

## Form, line & typography
LeWitt's line is uniform, unmodulated, and drawn to a ruler: one stroke weight across the whole wall. Shapes come only from a basic geometric vocabulary (square, circle, triangle, trapezoid, parallelogram, isometric cube). Typographically that calls for a monoline, mechanically regular face with tabular figures, because every element is labelled with a code like the cube variants ("7/29").
- **IBM Plex Mono**: instructions, captions, variant codes.
- **Space Grotesk** or **Archivo**: headings in one weight, set like stencilled labels.
One weight per role, never italic.

## Rhythm, motion & time
Time belongs to execution (a team drawing 10,000 lines). Motion should show the system running.
- Reveal a grid cell by cell in reading order with a constant 30–40ms stagger and linear easing. A machine has no ease-out.
- Draw lines with `stroke-dashoffset` at the same speed for every line, so long lines take proportionally longer.
- Changing a parameter regenerates the whole set, and every cell updates in sequence, so the user sees the rule apply to everything.

## UI translations
1. **Write the screen as a rule first.** Define the layout as a written spec ("3×4 cells, each showing one variant, sorted by X") and render the spec text in small mono at the top or bottom of the view.
2. **Enumerate, don't curate.** For any option space (themes, plans, filter combos), show every valid combination in a matrix rather than three "featured" picks. Exclude only true duplicates.
3. **Sort along one visible axis.** Order the matrix by a single increasing variable (edge count, price, density), and label row headers with the value.
4. **Make the base component deliberately boring.** It should be a bordered square with one label, no shadow, no radius. All interest comes from how instances vary.
5. **Use 1px rules on 8–9× cell spacing** (a 1:8.5 frame-to-void ratio).
6. **Assign color by index.** `nth-child(4n+1..4)` maps to red/yellow/blue/grey. No per-component color picking.
7. **Do overlaps with multiply washes.** Selected or hovered states lay a translucent primary over the cell, and multi-select overlaps mix into new hues.
8. **Seed the variation.** Generated art, avatars, and empty states take a deterministic seed (user ID) and a rule like "lines not straight, not touching."
9. **Label every instance with its code** ("4/12", "B-3") in tabular mono, as a catalogue number.
10. **Give an "instructions" toggle.** Let users flip any visualization to see the rule that produced it.
11. **For bold modes, go flat and edge to edge.** Full-bleed bands of saturated primary color with no gutter, no gradient, and no shadow. Use crisp boundaries only.

## What this artist would reject
- One-off "hero" layouts with no generating rule behind them.
- Gradients, glassmorphism, drop shadows, and texture: surface effects that distract from the idea.
- Curated "top 3" choices that hide the rest of the option space.
- Ease-in-out bounce and spring physics on systematic reveals.
- Per-component color decisions made for "vibe" instead of from a mapping.

## Signature prompt seed
Design the screen as an executed instruction, not a composition. Start from a deliberately plain module, a hairline-bordered square with a mono catalogue code, and tile it in an equal grid that shows every valid permutation of one variable, sorted along a single labelled axis. Keep frames thin and cells airy (about 1:8.5). Assign color strictly by index from red, yellow, blue, and grey, flat or as multiply washes where states overlap. Reveal cells in linear sequence. Print the generating rule in small IBM Plex Mono beneath the grid.

## Sources
- https://massmoca.org/sol-lewitt/
- https://massmoca.org/event/sol-lewitt-a-wall-drawing-retrospective/
- https://www.sfmoma.org/artwork/97.516.A-KKKKKKKKKK/
- https://socks-studio.com/?p=40341
- https://www.britannica.com/topic/Variations-of-Incomplete-Cubes
- https://mma.pages.tufts.edu/fah188/sol_lewitt/paragraphs%20on%20conceptual%20art.htm
- https://www.pbs.org/newshour/arts/sol-lewitt-paint-and-share-alike
- https://high.org/collection/wall-drawing-729-irregular-color-bands-2/
