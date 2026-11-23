# Ettore Sottsass — Memphis / Postmodern design

## Essence
Sottsass treated an object as a character, not a neutral container for function. He built it from cheap, loud, mass-printed surfaces and stacked primary shapes into figures that look back at you: a bookcase that resembles a robot or a many-armed goddess, a typewriter in a short red skirt. Usefulness stays, pointedly not the whole point. His line against functionalism ran roughly: *"It's not enough. Design should also be sensual and exciting."*

## Key works examined
- **Valentine portable typewriter (with Perry King, 1969)**: red injection-moulded ABS, orange spool caps, and a plastic bucket case that hangs from the machine's own handle. It teaches that an ordinary tool ("like a pencil") can still have a personality.
- **Bacterio laminate (Abet, 1978)**: a field of black squiggles on a pale ground, abstracted from the surface of a temple in Madurai. Pattern as a material you cut panels from, not added decoration.
- **Carlton room divider (Memphis, 1981)**: 196 cm tall, laminated MDF on an equilateral-triangle system, with slanted shelves and two red drawers above a Bacterio base. It teaches that a figure can sit on top of a grid and that one component can do three jobs (divider, bookcase, drawers).
- **Tahiti lamp (1981)**: a bird with yellow neck, pink head, red beak on a black triangle and Bacterio plinth. Every part gets its own colour; joints stay visible.

## Space & composition
- **Figure on top of a grid.** Carlton's lower half is a dense, regular storage body. Above, forms thin into arms reaching outward, topped by a stick figure. Keep the bottom 60% of the screen a strict container and give the top 40% to a silhouette that breaks out of it.
- **Triangulated, not orthogonal.** The diagonals run at 60° and 30°, the angles of an equilateral triangle, not 45°. Slant dividers, shelf lines and section bottoms at 30° from horizontal.
- **Solids and voids alternate.** Alternate filled colour tiles with empty or patterned tiles at about 1:1.
- **Symmetry, then sabotage.** Carlton is near-symmetric in form, not in colour: lay out symmetrically, then break it with colour.

## Color
The logic is one hue per component, never a gradient, and colours meet edge to edge with no neutral gap between them. Cheap printed colour is valued above "noble" materials. Pastels sit next to fire-engine primaries, held together by a black-on-white micro-pattern neutral.

| Role | Hex |
|---|---|
| Hero / "Valentine" red, for primary actions and the key object | `#E2231A` |
| Sun yellow, for structural arms and highlights | `#FFD100` |
| Memphis blue, for secondary panels | `#1F4FB4` |
| Flamingo pink, for surprise accents and the "head" | `#F5A3C7` |
| Mint / aqua, for calm fields | `#8ED8C8` |
| Bacterio ground, the neutral surface | `#F4F1E8` |
| Squiggle black, for pattern, outlines and type | `#111111` |

Rule: no two adjacent panels share a hue. Pair one "wrong" colour combination (pink against red) per screen.

## Form, line & typography
The shape language is primary solids (circle, square, triangle, cylinder) joined by visible seams, plus a hand-drawn squiggle as the one organic gesture. Edges are hard, and flat colour is outlined only where pattern needs to be held in. Type should feel geometric, chunky and toy-like.
- **Rubik Mono One**: blocky display caps for headings that behave like objects.
- **Syne** (Google Fonts): its wide weights have an eccentric, postmodern swing, which suits subheads and body text.
- **Space Mono**: a nod to the Valentine, for labels, metadata and form inputs.

## Rhythm, motion & time
Motion is **playful and mechanical, never liquid**: components pop in with a hard overshoot (`cubic-bezier(.34,1.8,.64,1)`, 180–240 ms), like a plastic part clicking into its socket. Slanted elements can wobble ±3° on hover like a figure balancing on a shelf. Patterns stay still while solid shapes move. Stagger at irregular intervals (40, 90, 60 ms). No fades or soft blurs: things appear, flip and tilt.

## UI translations
1. **Layout:** build the lower part of a screen on a 6-column grid. Above it, let one 30°-slanted "arm" element (a header block or a CTA panel) stick out past the container edge by 1.5× a column width.
2. **Layout:** slant section dividers at 30° (`clip-path: polygon(0 0,100% 0,100% 85%,0 100%)`), alternating direction.
3. **Texture:** use a tiled SVG squiggle pattern (black on `#F4F1E8`) as a "plinth" under cards, footers and empty states. Never use it behind body text.
4. **Color:** give every card in a grid a different solid hue from the palette, with no white cards. Pick the one primary action and make it the only red.
5. **Color:** use exactly one clash per view, such as a pink badge on a red surface or a mint chip on yellow.
6. **Type:** put headings in Rubik Mono One at 3–4× body size, black on a solid colour block, tightly set (`line-height: .9`).
7. **Type:** put form labels and metadata in Space Mono at 12–13px, uppercase with letter-spacing `.08em`, like a typewriter's key legends.
8. **Form:** compose icons and avatars from 2–3 primitives, for example a circle head on a triangle body, each piece in its own hue with 2px black seams.
9. **Motion:** on mount, drop components in with an overshoot spring. On hover, tilt cards by 2–3° around their bottom corner.
10. **Interaction:** give the main tool control a "spool cap", a small round knob in a contrasting orange or pink that physically rotates on press, so the control feels like a toy part.
11. **Interaction:** containers hang from their content's own visible grip tab, like the Valentine's bucket case.

## What this artist would reject
- Grey-on-white "tasteful" neutrality, with a single blue accent standing in for personality.
- Soft shadows and frosted glass faking preciousness or depth; laminate is flat and proud.
- Smooth gradients and colour ramps. He would use hard colour cuts instead.
- Self-effacing tool UI, meaning the idea that a good interface is the one you don't notice.
- Strict orthogonal 12-column grids with every card the same size and colour.

## Signature prompt seed
Design this app screen as a Memphis object with a personality. Use a cream ground tiled with black squiggle texture. Build a dense 6-column block grid in the lower 60%, with each card a different flat primary or pastel and no white cards. Above it, put a 30°-slanted yellow arm that breaks out of the container. Make one red primary action and one deliberate pink-on-red clash. Set headings in chunky Rubik Mono One and labels in Space Mono. Use hard edges, 2px black seams, no shadows and no gradients. Components click in with springy overshoot and tilt on hover. Keep it useful, but make it sensual, ironic and slightly rude.

## Sources
- https://ngv.vic.gov.au/essay/carlton-room-divider
- https://www.metmuseum.org/art/collection/search/486989
- https://www.dezeen.com/2015/08/03/ettore-sottsass-memphis-group-carlton-storage-unit-tahiti-lamp-postmodernism/amp/
- https://www.metmuseum.org/art/collection/search/759731
- https://www.domusweb.it/en/from-the-archive/2011/08/25/red-valentine.html
- https://en.wikipedia.org/wiki/Olivetti_Valentine
- https://www.moma.org/collection/works/4576
