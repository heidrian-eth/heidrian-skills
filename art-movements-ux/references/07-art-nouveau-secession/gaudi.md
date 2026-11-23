# Antoni Gaudí — Catalan Modernisme / Art Nouveau

## Essence
Gaudí didn't draw his forms first. He let forces find them. He hung weighted strings and turned the result upside down, so every curve is the shape a load wants to take. Over that honest structure he laid a skin of broken, glittering colour that shifts with the sun. Structure is ornament, nature is the grid, and there are almost no straight lines.

## Key works examined
- **Colònia Güell hanging model (c.1898–1908)**: a 1:10 model of strings and weights, with cloth cutouts to show the inverted building. It teaches you to derive form from constraints rather than impose it.
- **Park Güell (1900–1914)**: 86 Neo-Doric columns that collect rainwater, inclined viaduct columns, and the modular trencadís serpentine bench (1909–14, with Jujol). Infrastructure doubles as delight.
- **Casa Batlló facade (1904–06)**: bone-like columns, cast-iron mask balconies, a wavy ceramic-and-glass skin and a scaled roof whose colours shift end to end. A single surface can tell a story.
- **Sagrada Família nave columns (designed 1910s–20s)**: star-section shafts that double-twist into circles and branch like trees. A strict generative rule yields organic results.
- **Sagrada Família stained glass (with Joan Vila-Grau)**: cool blues on the east (Nativity), warm reds and oranges on the west (Passion). Colour is assigned by orientation and time of day.

## Space & composition
- **Form follows the load path.** Gaudí's columns lean because the thrust leans. Let alignment follow a curve set by the user's reading path, not the 12-column grid.
- **Rule-generated hierarchy.** At the Sagrada Família, a column's height in metres is twice its star points, and its base height in decimetres equals them: 12 points gives 24 m in porphyry, 6 points gives 12 m in sandstone. One integer drives size, material and position.
- **Progressive subdivision.** Each section of a column halves in height and rotation while its points double, so the star resolves into a circle.
- **Forest, not hall.** Columns branch into vaults that filter light like a canopy. Gaudí's emptiness is dappled, never blank.
- **The edge is the room.** The serpentine bench is both the guardrail and the place to sit. Its concave bays make small social pockets along a long edge. Treat page edges as habitable, wavy zones, not hard frames.

## Color
Colour runs on direction and height. Cool belongs to dawn and beginnings, warm to dusk and endings. The most saturated glass sits low, at reading height. Higher up it bleaches to clear textured glass that splits the light, the reverse of Gothic practice. Gaudí wanted the sun to do the colouring ("sunshine is a great painter"). Trencadís adds a second rule: small, broken, glossy fragments of related hues, separated by pale grout.

| Hex | Role |
|---|---|
| `#E9DFCB` | Sandstone/grout ground: base surface and the gaps between tiles |
| `#2F6FA8` | Nativity blue: onboarding, start states, morning |
| `#4F9A86` | Batlló sea-green: secondary surfaces, the scaled roof |
| `#D99A2B` | Ochre trencadís: highlights, selection |
| `#C2452D` | Passion red-orange: completion, destructive, evening states |
| `#7B5B8C` | Mauve glaze: rare accent, visited/archived |
| `#FDFBF5` | Clear-glass white: upper zones, top-of-page light |

## Form, line & typography
Line is catenary and parabolic: curves under tension, never compass circles or arbitrary béziers. Corners are tangent parabolic arcs, like the rounded points of the column stars. Gaudí's own lettering is hand-cut into tile and ironwork, fused with the material. Type should be soft-shouldered but structured:
- **Fraunces** (Google Fonts) with SOFT at 100 and WONK on, for display. Its bulbous terminals echo carved stone.
- **Young Serif** for warm headings, if Fraunces is too playful.
- **Commissioner** (variable flare) for body text, quiet under heavy ornament.

## Rhythm, motion & time
Motion behaves like gravity. Elements hang from anchors and settle like a chain, with a damped spring and no overshoot. Animate the light rather than the layout: hues drift cool at morning and warm at evening, and glossy fragments glint under the pointer or when the device tilts. Repetition works like the bench modules, with the same module in different colours and no identical neighbours.

## UI translations
1. **Hang the layout.** Draw section dividers as flipped catenaries (`y = a·cosh(x/a)`) in SVG, not generic waves.
2. **Drive components from one integer.** A `--points: 6|8|10|12` token sets height, radius, material colour and font size, like the column specifications.
3. **Nest by halving.** Each level down halves the padding, doubles the grid divisions and increases the corner radius until the deepest chips are pills, star to circle.
4. **Assign colour by orientation.** Start panels and morning states use `#2F6FA8`; end panels and evening states use `#C2452D`, keyed to the local clock.
5. **Saturate low, bleach high.** Put the strongest colour in the bottom third of the screen (tab bar, CTAs). Let the top fade to `#FDFBF5` with a faint spectral fringe.
6. **Trencadís surfaces.** For hero areas, use a Voronoi mosaic of 40–120 irregular shards in 3–4 neighbouring hues with 2px `#E9DFCB` grout. Generate it once per user, so no two people see the same pattern.
7. **Habitable edges.** Give long lists a serpentine edge, concave bays every 4–6 items that hold contextual actions, like the seats along the bench.
8. **Skeletal frames.** Give media containers bone-like mullions: tapered supports thicker at the joints, not uniform 1px borders.
9. **Gravity motion.** Use `spring(stiffness 120, damping 18)` for drop-ins. Dismissed sheets fall along a catenary arc instead of a straight line.
10. **Infrastructure as ornament.** Make functional affordances (scroll progress, loading, dividers) the decorative elements, like the columns that carry rainwater.
11. **Light that moves.** Let the hero gradient's hue angle drift 1° per minute of local time, and add a pointer-driven specular highlight on glossy tiles.

## What this artist would reject
- Rectangular cards on a rigid 12-column grid with the same radius everywhere.
- Flat single-hue fills that don't respond to light.
- Decoration pasted on top of structure, like a hero illustration with no function.
- Linear or `ease-in-out` motion with no weight.
- Dead 1px borders and identical, repeated list items.

## Signature prompt seed
Design this screen as if its forces shaped it. Section dividers are inverted catenary arches, and containers have tapered, bone-like frames. Clad the hero in irregular trencadís shards of ochre, sea-green and blue with pale sandstone grout. Put saturated colour low near the thumb and let the top bleach to prismatic white. Theme cool blue at morning and red-orange at evening. Lists run along a serpentine edge with bays for actions. Motion settles under gravity, like a hanging chain. No straight lines, no flat fills, no ornament that doesn't do structural work.

## Sources
- https://en.wikipedia.org/wiki/Funicular_curve
- https://blog.sagradafamilia.org/en/vitralls-llum-colors-creacio/
- https://blog.sagradafamilia.org/en/columnes-sagrada-familia-geometria-mecanica-materials-bosc-pedra/
- https://www.casabatllo.es/en/antoni-gaudi/casa-batllo/facade/
- https://www.lapedrera.com/en/work-antoni-gaudi/park-guell/
- https://www.barcelona.com/barcelona-attractions/park-guell/serpentine-bench
