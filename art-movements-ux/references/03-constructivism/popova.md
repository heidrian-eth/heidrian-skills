# Lyubov Popova — Constructivism

## Essence
Popova treats a picture as a structure under load. Colored planes overlap, slant and push past the frame, and later thin lines of force cut through them, so the picture reads as energy held in balance. From 1922 she took the same grammar into working objects: a stage set built for actors to use, and cheap two-color prints repeated across cloth by the bale.

## Key works examined
- **Painterly Architectonic, 1917** (MoMA, oil, 80 × 98 cm). Red, black, gray, pink and white planes lie over a pale ground. They avoid right angles and seem to continue past the frame. It teaches layered planes and diagonal tension.
- **Spatial-Force Construction, 1921** (MOMus Costakis Collection, oil and wood sand on plywood, 112.5 × 112.3 cm). A near-square board with a gritty surface. Crossed thin lines run over interpenetrating planes. It teaches vectors laid over fields, texture as information, and a square format.
- **The Magnanimous Cuckold, 1922** (Meyerhold). A free-standing bare-wood frame on an empty stage, with platforms, crossing struts, turning wheels and windmill blades. It teaches that the interface is an apparatus that actors perform by using.
- **Textile designs for the First State Textile Printing Works (formerly Zindel), 1923–24**. Circles, stripes, grids turned 45°, and stars, mostly in one color plus black and/or the bare white cloth. It teaches permutation of one motif in an endless repeat.
- **LEF no. 2 cover textile design, 1924**. Red and black only. The ЛЕФ letters are sliced horizontally in alternating colors, inside a frame of diagonals and red circles.

## Space & composition
- **Tilt the dominant axis.** Her planes avoid true horizontals. The main slant sits around 12–25° off orthogonal, and one opposing slant answers it at a different angle, never a mirror.
- **Stack, don't shadow.** Depth comes from overlap order (3–5 planes), and the front plane gets a light edge.
- **Overflow the frame.** At least one major plane is cropped by the edge on two sides.
- **Force lines over fields.** In the 1921 works, thin lines cross the planes, meet off center and run off the edge, following a different geometry from the planes.
- **Scaffold layouts (Cuckold).** An exposed, load-bearing frame with empty stage around it.
- **Square modules.** The 112 × 112 cm board and the textile repeats suggest a square base tile, for example 96 px.

## Color
Flat colors with hard edges, and the ground counts as a working color, like the bare cloth in the textiles. She used three colors or fewer in 1920–21 and two in the textiles, for economy. Red does the work, black does the structure, and gray and the ground mediate.

| Role | Hex |
|---|---|
| Ground / raw cloth | `#EDE6D6` |
| Action red (primary plane, CTA) | `#C8321F` |
| Structure black (lines, text, struts) | `#1B1A17` |
| Mediating gray (secondary planes) | `#8C8A84` |
| Icon pink (accent plane) | `#D99A93` |
| Bare-wood ochre (surfaces, panels) | `#B88A55` |

Use at most three of these per screen.

## Form, line & typography
Shapes are trapezoids, sheared rectangles, arcs and circles. Lines are taut, with square ends. Type should feel constructed, as on the LEF cover: condensed geometric caps, sliced into two colors, set on a slant. Use a plain grotesk for working text.
- **Big Shoulders Display**: condensed, strutted headlines.
- **Oswald**: compact uppercase labels.
- **Rubik** or **Archivo**: body and UI text with slightly squared curves.

## Rhythm, motion & time
- **Mechanical, not organic.** Like the Cuckold wheels: constant `linear` rotation (8–20 s) for ambient elements, and decisive `cubic-bezier(.7,0,.3,1)` moves (180–260 ms) for state changes.
- **Planes slide along their own slant.** On entry, a plane travels along its tilt axis, not straight up. Layers arrive in overlap order, back to front, 60 ms apart.
- **Textile time.** Backgrounds can drift as a slow seamless repeat, like cloth running off a roller.

## UI translations
1. Rotate the hero container's main color plane by −14° and let it bleed off the top and right edges (`overflow: clip` on the parent).
2. Build depth from 3–5 overlapping flat planes with `z-index` order only, with no `box-shadow`. Give the front plane a 3 px `#EDE6D6` edge.
3. Draw 1–2 px black "force lines" in an absolutely positioned SVG. They cross card boundaries and meet at a node off the grid.
4. Show the scaffold: render the layout grid as visible 1 px struts. Put content on platforms between them, and add a diagonal brace in one bay.
5. Limit each screen to three colors from the palette. Red marks only the one actionable thing.
6. Split display headlines horizontally: top half black, bottom half red, using `background-clip: text` with a hard `linear-gradient` stop at 50%.
7. Fill empty and loading states with a two-color CSS `background-image` repeat (circles on a 45° grid).
8. Use a square base tile for cards and thumbnails. Break the rhythm once per screen with a tile twice as wide on a slant.
9. Treat controls as visible mechanisms. A toggle is a wheel that turns 90°, and a progress indicator is a constantly spinning segmented disc.
10. Add a faint grain (SVG `feTurbulence`, 4–6% opacity) to the largest plane only, like the wood-sand surface.
11. In each section, say a feature list, show one motif in 4–6 permutations (circle, half circle, ring, circle with a bar), not a different icon for each item.

## What this artist would reject
- Soft drop shadows and frosted glass that fake depth.
- Gradients and 12-color "brand palettes" instead of two or three flat inks.
- Perfectly centered, symmetrical heroes with everything inside the safe area.
- Decorative illustration that does no work.
- Bouncy springs. Her motion is mechanical.
- Hiding the layout grid. She left the frame bare.

## Signature prompt seed
Design this screen as a Popova construction: a raw-cloth ground (#EDE6D6) with at most three flat inks, structure black, action red and one gray. Tilt the dominant plane about 14° and let it run off two edges. Stack 3–5 planes for depth without any shadow. Draw thin black force lines that cross card borders and meet off center. Show the grid as struts with one diagonal brace. Set headlines in condensed caps split black over red. Every element must work like apparatus. Motion is mechanical: constant rotation, crisp linear slides along each plane's own slant, and a two-color geometric repeat in the empty areas.

## Sources
- https://www.moma.org/collection/works/78444
- https://www.tate.org.uk/research/tate-papers/14/liubov-popova-from-painting-to-textile-design
- https://artsandculture.google.com/story/VQUxAkR4CHhRMw
- https://www.studiointernational.com/rodchenko-and-popova-defining-constructivism
- https://max.mmlc.northwestern.edu/mdenner/Drama/plays/constructivist/constructivist.html
- https://theartstory.org/amp/artist/popova-lyubov/
