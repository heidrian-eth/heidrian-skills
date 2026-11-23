# El Lissitzky — Constructivism

## Essence
Lissitzky treated a page, a wall or a room as a field of forces. He placed a few charged elements (a wedge, a bar, a block of type) on diagonals, so the viewer has to move: turn the sheet, flip to a tab, walk the room. Every element is either a vector or a counterweight, and the reader's eye or hand finishes the construction.

## Key works examined
- **Beat the Whites with the Red Wedge, 1919** (lithograph): a red triangle drives into a white circle. Meaning comes from collision and direction rather than illustration. Two shapes and one diagonal carry a whole narrative.
- **Prouns, 1919–1923**: "a station" on the way to new form, built to be "surveyed from every direction." Axonometric volumes float with no horizon, so there is no single correct way up.
- **Proun Room, Great Berlin Art Exhibition, 1923**: the Proun goes off the canvas and onto three walls of a small room, with reliefs that lead the visitor around corners. The surface becomes a route.
- **For the Voice (Dlia golosa), 1923**: 13 Mayakovsky poems. A die-cut thumb index marked with geometric signs, not letters, takes you straight to each poem. Every poem opens on a two-colour typographic title page. It is navigation as a designed object, a proto-tab bar.
- **"Topography of Typography," Merz 4, 1923**: eight theses. Printed words are taken in by sight, not sound. Optics should beat phonetics. Pages should run as a continuous, cinematic "bioscopic book." The printed surface itself would be surpassed by the "Electro-Library."
- **Soviet pavilion at Pressa, Cologne, 1928**: a 24 m × 3.5 m photomontage frieze, zig-zag conveyor belts, rotating models, running films, blinking letters. The visitor becomes a player on a stage.

## Space & composition
- **The canvas has no fixed up.** Tilt the main axis between 15° and 45°. Prouns were meant to work from every direction, so build layouts that still read when the dominant block is rotated.
- **Vector plus counterweight.** Each composition has one aggressor (wedge, bar, oversized numeral) and one heavy, static mass (circle, square, black slab). Put them on a shared diagonal running from lower-left to upper-right and leave a narrow gap at the point of contact. The tension sits in that gap.
- **Big flat field, small cluster.** Let one flat colour field take 50–65% of the frame, as the white circle does in Beat the Whites. Scatter 5–9 small fragments (rectangles, short bars, tiny type) as debris along the force line.
- **Floating axonometry.** Show depth with 30°/60° parallel projection, never vanishing-point perspective, and no ground plane.

## Color
Binary opposition with one hot agent: red is always the actor, never decoration; black and white are the stage; grey is the in-between state.

| Role | Hex |
|---|---|
| Agent / primary action | `#D7261E` (signal red) |
| Ground (paper) | `#EFE9DC` (unbleached stock) |
| Mass / counterweight | `#141414` (press black) |
| Secondary plane | `#8C8A84` (zinc grey) |
| Recessive tint / disabled | `#C9C3B6` |
| Rare metallic accent (Pressa nickel) | `#B8BCC0` |

Rule: two inks plus paper per screen, as in For the Voice; red under ~20% of area, only where something happens.

## Form, line & typography
Letters are building material: stacked, rotated 90°, scaled from tiny to giant on one line, boxed in by thick rules. Type carries load like beams. Use heavy grotesque capitals for key words, 4–12 px rules as brackets and arrows, and outsized numerals as section markers. Line is ruler-straight with occasional perfect arcs, never freehand.

Fonts: **Rubik Mono One** (display), **Oswald** (condensed, vertical/stacked labels), **IBM Plex Sans Condensed** (body).

## Rhythm, motion & time
The "bioscopic book" thesis makes each scroll step a film cut. Motion follows vectors: elements slide along the composition's −30° diagonal and stop hard, no bounce, with mechanical easing (`cubic-bezier(.7,0,.2,1)`, 220–320 ms). Pressa's blinking letters and conveyors allow at most one looping element per screen. Hover pushes a block along its own axis rather than lifting it with a shadow.

## UI translations
1. Rotate the hero composition's main bar to −30° and let it run off two viewport edges. Content sits along it, not below it.
2. Make the single primary CTA a red wedge (`clip-path: polygon(0 0,100% 50%,0 100%)`) pointing at the thing it affects.
3. Build section navigation as a fore-edge thumb index: a fixed right rail of stepped tabs that sit at different vertical offsets, each marked with a geometric glyph (■ ● ▲ ▬), with labels only on hover.
4. Give each destination its own title spread, a full-screen two-colour typographic page, before the content starts.
5. Cap every view at two inks plus paper. Use red only for state change, selection and action.
6. Set headings in mixed scale on one baseline: one word at 12vw, the next at 1.2rem, rotated 90° when space runs out.
7. Use thick black rules (8 px) as structural brackets that group content, never hairline dividers or card shadows.
8. Animate route changes as cuts along the diagonal: the outgoing screen leaves on −30° and the incoming one enters on the same vector, with a hard stop and no fade.
9. Draw empty states and illustrations as floating axonometric blocks (30°/60°) with no ground shadow.
10. On dashboards, run a horizontal photomontage strip (Pressa frieze) as a scrolling belt of image and data fragments that crop each other at odd angles.
11. Put one rotating 3D primitive per screen as a loading or idle state, rotating slowly on one axis.

## What this artist would reject
- Centered, symmetrical hero sections with nothing pushing against anything.
- Soft drop shadows and frosted glass that fake depth. Depth should be constructed, not lit.
- Colour used as brand wallpaper, such as gradient backgrounds where red, or any accent, carries no meaning.
- Hamburger menus that hide the structure. Navigation should be visible and physical, like the thumb index.
- Uniform type scales with no jumps, and body-sized headings.
- Decorative illustration that comments on content instead of driving it.

## Signature prompt seed
Design this app screen as a Lissitzky construction. Use an unbleached paper ground (#EFE9DC), press black and one signal red (#D7261E) that appears only where action happens. Tilt the main structure to −30° and let a thick black bar cross the viewport edge to edge. Make the primary action a red wedge aimed at its target. Navigate with a stepped fore-edge thumb index marked by geometric glyphs. Set headings in heavy grotesque capitals with violent scale jumps, some rotated 90°. Draw depth only as floating axonometric blocks. Transitions cut along the diagonal and stop hard. No shadows, no gradients, no centred symmetry.

## Sources
- https://www.moma.org/slideshows/43/793
- https://www.moma.org/interactives/exhibitions/2012/ecstaticalphabets/works/dlia-golosa/index.html
- https://thecharnelhouse.org/2013/09/16/proun/
- https://thecharnelhouse.org/2014/03/01/el-lissitzkys-soviet-pavilion-at-the-pressa-exhibition-in-cologne-1928/
- https://en.wikipedia.org/wiki/Beat_the_Whites_with_the_Red_Wedge
- https://www.dailyartmagazine.com/beat-the-whites-with-the-red-wedge
- https://cca.qc.ca/en/search/details/collection/object/334319
