# Varvara Stepanova — Constructivism

## Essence
Stepanova designed systems, not pictures. She worked out one small unit (a chevron, a belted tunic, a slatted stool) under a budget of one or two dyes and four shapes, then let repetition and use produce the variety. Construction stays visible, and decoration has to earn its place by working.

## Key works examined
- **Gaust chaba, 1919**: a book of zaum (invented-language) poems, watercolor lettering painted over found newspaper pages, edition of 54. Teaches you to treat the substrate as a layer: a new, louder system printed straight over the old grid.
- **Set for *The Death of Tarelkin* (Meyerhold), 1922**: separate wooden "apparatuses" (treadle and cage, stools, chairs, high and low tables, a folding screen) that actors could combine or use alone. Teaches modular components with mechanical, sometimes misbehaving, states.
- **Sportswear designs for *LEF*, 1923**: boxy unisex tunics where emblems and contrasting color mark the team, not rank or gender. Differentiation must be functional.
- **Fabric designs, First State Textile Printing Factory, 1924**: more than 150 designs in about a year, built only from triangles, circles, squares and lines in one or two dyes. Teaches a constrained token set with very large output.
- **Chevron flannel, Tsindel factory, 1924 (V&A)**: wine-red and olive-brown chevrons on natural fawn. The unbleached ground counts as a color.

## Space & composition
- **The tile is the composition.** Design a unit on a 24×24 or 24×48 px cell and repeat it with half-drop or mirror offsets. A page is an area filled by a rule, not a hero-and-sections scene.
- **Overprinting creates depth, not shadow.** Her textiles stack flat layers so they read in several dimensions with no gradients. Overlap cards with hard edges and a visible z-order, never blur.
- **Discrete apparatuses.** As on the Tarelkin stage, each component sits alone on an empty floor and can link to its neighbors. Lay out a dashboard as 4–6 free-standing modules on a bare field, joined by visible hinges (shared edges, connector bars), not a grid of identical cards.
- **Density alternates.** Tight pattern strips run against wide plain bands, about 30% pattern to 70% flat ground.
- **Diagonals carry action.** The key path runs on a 30–45° bar across an orthogonal grid.

## Color
Few inks, maximum contrast, and the ground counts as an ink: red, black and white for sportswear, and one or two dyes on natural cloth for textiles.

| Role | Hex |
|---|---|
| Ground (unbleached calico/fawn) | `#E6D8BA` |
| Ink 1, structure and text | `#15130F` |
| Ink 2, signal and team red | `#C62A1F` |
| Wine (textile alternate red) | `#7A1E2C` |
| Olive-brown (second dye) | `#6B5F3B` |
| Paper white (knock-out) | `#F5F2EA` |

Use at most **two inks plus the ground** per screen. Assign hues as she did for teams: one per actor or state, never as decoration.

## Form, line & typography
- The shape vocabulary is circle, square, triangle and the ruled bar. Edges are compass and ruler only: no freehand curves, and no corner radius except a full circle.
- Gaust chaba adds a second register: hand-painted, uneven capitals over printed columns. Use it for one expressive word per screen, as a rough SVG over a low-contrast "newsprint" text layer.
- Fonts (all Google Fonts): **Unbounded** for headings, **Rubik Mono One** for labels and numerals, **IBM Plex Mono** for the newsprint underlayer and data. Set type large, uppercase and tightly tracked.

## Rhythm, motion & time
- Things should move like the Tarelkin furniture, a mechanism doing a job: hinge, fold, drop and spring, with linear or `steps(4)` easing.
- Pattern fields scroll like a conveyor belt, moving exactly one tile width per scroll unit.
- Let some states misbehave on purpose, as stage furniture does in a circus-style farce. A destructive-action button can "fold" flat (`scaleY: 0` from the bottom edge over 120 ms) before it confirms.
- Team logic: switching user or context recolors the whole uniform (accent token) in one hard cut. Do not crossfade.

## UI translations
1. Build every background from one 24 px SVG tile of no more than 3 primitives, repeated with `background-repeat` and a half-drop offset.
2. Limit each screen to ground `#E6D8BA` plus two inks. Validate in CI that no third hue appears.
3. Overlap adjacent modules by 12 px with hard edges and a 2 px black rule. Express hierarchy through stacking order, not shadows.
4. Run the primary CTA on a single 35° red bar that crosses the grid and bleeds off one edge.
5. Expose construction: show grid lines and connector "seams" as visible hairlines. Treat structure as ornament.
6. Let users dock free-standing modules into larger assemblies by dragging one flush to another.
7. Assign each user, team or data series a full "uniform": an emblem glyph, a stripe and a color. Never tell series apart by color alone.
8. Put one hand-painted zaum headline per screen over a 10%-opacity monospaced newsprint underlayer.
9. Animate with `steps()` or linear easing on hinge transforms (`rotate`, `scaleY` from an edge). Keep every duration under 200 ms.
10. Set section labels in uppercase Rubik Mono One, rotated 90° and running up the left edge of each module.
11. Show a hover state by inverting the tile: the ground becomes ink and the ink becomes ground.
12. Alternate dense pattern bands (about 64 px) with wide plain bands (about 160 px) as the vertical rhythm.

## What this artist would reject
- Floral or "lifestyle" decoration (blob art, stock-photo heroes) used to soften a product.
- Borderless cards, frosted glass and drop shadows that hide how things are built.
- Uniform rounded corners and pill shapes that are neither a true circle nor a true square.
- Gradients and big palettes. More inks than the process needs.
- Gold "premium" badges: differentiate by role, not rank.
- One-off bespoke layouts that cannot be repeated as a system.

## Signature prompt seed
Design this app screen as a printed calico and a working stage set. Use an unbleached fawn ground, black, and one signal red, with no third hue. Build every surface from a single 24 px tile of circle, bar and triangle, repeated with half-drop offsets. Components are free-standing wooden apparatuses with visible seams and hinges, overlapping with hard edges and no shadows. One 35° red bar carries the main action. Use one hand-painted zaum headline over faint monospace newsprint. Motion hinges and folds with stepped, mechanical timing. Users are told apart by team uniforms: emblem, stripe and color.

## Sources
- https://garagemca.org/en/exhibition/i-the-fabric-of-felicity-2018-i/tour/from-picture-to-calico
- https://garagemca.org/en/exhibition/i-the-fabric-of-felicity-2018-i/tour/varvara-stepanova
- https://www.moma.org/collection/works/13332
- https://collections.vam.ac.uk/item/O1371413
- https://smarthistory.org/?p=44236
- https://en.wikipedia.org/wiki/Varvara_Stepanova
- https://max.mmlc.northwestern.edu/mdenner/Drama/plays/constructivist/constructivist.html
- https://sainsburymuseum.com/art-and-objects/31253o-the-death-of-tarelkin-folding-screen-from-set-maquette-reconstruction-1970/
- https://www.sainsburycentre.ac.uk/?p=33245
- https://collectiononline.gctm.ru/en/entity/OBJECT/38126
