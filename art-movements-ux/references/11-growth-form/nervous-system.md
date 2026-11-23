# Nervous System (Jessica Rosenkrantz & Jesse Louis-Rosenberg) — Growth & Form

## Essence
Nervous System write simulations of biological growth (leaf venation, differential growth of petals and sea slugs, crystal dendrites, reaction–diffusion), then let each run grow one unique object. The design is the system: a seed, an environment and a few growth parameters. Every output is different, and all are recognisably one family. They publish the algorithms, so the process is the work.

## Key works examined
- **Hyphae lamps (2011).** 3D-printed nylon lamps whose veins grow from a set of root points into an "auxin-filled" volume, after Adam Runions's venation model (Algorithmic Botany, Calgary). They teach space-colonising branching with merging loops. *(visually checked: n-e-r-v-o-u-s.com press kit image "Hyphae, an infinite series" and the lamp pair photo)*
- **Floraform (2014–15).** A simulated elastic surface that grows faster at its edge, after the biomechanics of leaves, flowers and lettuce sea slugs. It teaches edge growth producing a cascade of ruffles. *(visually checked: n-e-r-v-o-u-s.com blog, "Floraform – an exploration of differential growth": growth-sequence render and sculpture photo)*
- **Floraform, uniform-growth control.** A hemisphere growing uniformly wrinkles chaotically. It teaches that differential growth, not growth, makes order. *(visually checked: same blog post, figure "a hemisphere growing uniformly")*
- **Kinematics (2013–14; Kinematics Dress acquired by MoMA).** Thousands of rigid triangles linked by printed hinges, folded by simulation to fit the printer. It teaches rigid units plus joints making a flexible whole. *(visually checked: n-e-r-v-o-u-s.com blog image "Kinematics")*
- **Generative jigsaw puzzles (2012 onward).** Piece cuts grown by a dendritic-solidification (snowflake) simulation, with art by Jonathan McCabe layering reaction–diffusion at several scales; figural "whimsy" pieces are set into the field. They teach a grown tessellation with a few legible exceptions. *(visually checked: n-e-r-v-o-u-s.com blog, "Generative jigsaw puzzles", McCabism puzzle photo)*
- **Reaction–diffusion puzzle and textile pieces.** *(not obtained: the studio's own reaction–diffusion algorithm post was not found; the puzzle post states the cuts are dendritic and the reaction–diffusion is in McCabe's artwork)*

## Process and relations (observed)
- **Grow from roots toward a field of sources** (Hyphae). Thick trunks rise from the base and branch upward; between them a finer mesh of closed loops fills the surface, because veins merge where they meet (anastomosis) instead of only forking. Material covers ≈16–21% of each lamp's silhouette in the press drawing, slightly denser at the rim (≈0.20–0.21 in the top third against ≈0.16–0.17 lower). Eight lamps from one system differ in outline and vein path but share the density and the hierarchy.
- **Edge grows faster than area, so ruffles cascade** (Floraform growth sequence, 24 frames). A disc first buckles into 5 lobes, each lobe tip then splits, and later frames carry waves on waves with no flat area left. The blog's control figure (uniform growth) wrinkles without hierarchy. The rule is in the gradient, not in the rate.
- **Holes graded with growth** (Floraform sculpture). The perforation lattice starts small and sparse near the stem and grows larger and denser toward the ruffled rim, propagated outward from the growing edge (the blog cites lacy bryozoans).
- **Rigid units, flexible whole** (Kinematics). Every tile is a rounded triangle with its own triangular hole; hinges sit at every shared edge; voids (the black field) cover ≈26% of the image. Tile size varies across the piece (smaller where more drape is needed, per MoMA's record).
- **Grown tessellation with legible exceptions** (puzzle). Hundreds of pieces with dendritic, interlocking edges of similar size fill the board; roughly 15 figural pieces (animals, cells, leaves; 16 shown lifted out around the board) sit scattered inside the field, each surrounded by ordinary pieces.
- **The generative rule:** define a seed (roots, an edge, a point), an environment (sources to reach, a body to fit, a boundary) and one gradient (growth faster at the edge, or toward the sources); iterate small local steps with collision avoidance until the space is filled; let branches merge into loops; vary density along the gradient; output a family, not a single object. This works in any palette, material or medium.

## Process (derived)
*From observation to process (see SKILL.md §1). This is what transfers; the rest of the file is evidence.*

**Nervous System.** *Design the rule and not the object: a seed, an environment and one gradient, stepped locally until the space is full, and shown as a family of outcomes.*
Process:
1. Declare three inputs and nothing else. A seed (start points, taken from the item's ID). An environment (the boundary, the targets to reach, and keep-out zones for text and controls). ONE gradient: the direction along which growth runs faster or density rises.
2. Grow in small local steps, each 1–2% of the width, toward the nearest unreached targets. A branch stops one step short of the boundary, a keep-out zone or another branch. Nothing crosses.
3. Where two branches meet, merge them, so the result has closed loops and every region is reachable by two routes. Halve the width at each branching level (4 : 2 : 1).
4. Stop on coverage, not on time: structure fills 16–21% of its area (voids about a quarter in the tiled mode), and density at the far end of the gradient is about 25% above the near end.
5. Grade one secondary variable along the same gradient and no other: opening size from small to large, unit size from large to small, or a second wave at 1/3–1/5 of the first wavelength and 1/3 of its amplitude.
6. Set the exceptions inside the field: about 3–5% of the units take a recognisable outline plus a label, each wholly surrounded by ordinary units.
7. Run the rule on 4–8 seeds and show the outcomes side by side, each with its seed printed. Publish the parameters.
Why it works:
- A local rule with collision produces gaps that are even without being regular. The field fuses into one tone at a distance, as a texture, yet no region repeats, so the eye finds neither a grid nor noise. Hand placement cannot hold the gaps even over hundreds of units.
- The gradient is the only source of hierarchy. Growth at the same rate everywhere wrinkles without order (the studio's own control case); a faster edge gives large lobes, then lobes on lobes, and a direction to read in with no hero.
- Several kin side by side let the viewer subtract what varies and see what holds (density, hierarchy of widths), so the identity is carried by the rule. A single output reads as an illustration somebody drew.
Colour relations: the grown structure is ONE value; the ground is the opposite end of the value scale; emphasis comes from density, not hue; if colour is needed it is one ordered ramp mapped to growth age or depth (never categories), with the same information in a label or in width.
Space and line: fill by growth to a coverage target; lines taper from trunk to tip, branch, merge and never cross; widths halve per level; density up 25% along the gradient; exceptions 3–5% and embedded; families of 4–8.
Type requirement: a neutral voice that stays out of the structure's way, plus a fixed-width voice for seeds and parameters; all text on plain ground in keep-out zones declared in step 1, never on the grown field; an indented list of the same structure for keyboard and screen-reader users.
Motion and interaction: growth is the animation and it runs once. The structure extends from its seed in the rule's own steps over 1–3s and stops at the stable state; new content extends from its parent along a path (300–600ms); "regrow" takes a new seed. Never loop growth behind text. Reduced motion: the final state at once, with a replay control.
Fails when: there are too few items to make a texture (under ~30 units the result is a doodle); exact position must carry meaning (rank, time, geography); the content is one fixed object with no family; users must find the same item in the same place on every visit (pin the seed, or do not use it for navigation).
Signature (do not carry together): white 3D-printed vein and coral forms · ruffled laser-cut or printed surfaces · a grid of numbered variants on black.

**Transfer test** (an illustration that the process survives new colours and content; never reuse its hues, layout or wording as a design answer):

Course and prerequisite map for a university catalogue, desktop 1440 × 900, saturated cobalt on warm white, text-heavy and administrative (the studio's work is white, wordless and ornamental).
1. *Inputs.* Seed: the student's programme code (`BIO-2291`) sets three root positions on the bottom edge. Environment: the canvas (1040 × 760px), 140 course nodes as targets, a keep-out rectangle behind every course label. Gradient: bottom (first year) to top (final year).
2. *Growth.* Paths extend 18px per step (1.25% of the width) toward the nearest unreached course, stopping one step short of labels and of each other. No path crosses another.
3. *Merge.* A course with two prerequisites is where two branches meet, so they join there into a loop. Widths are 8, 4 and 2px by level, so the core sequence reads as trunks.
4. *Coverage.* Growth stops at 18% ink. The top third comes out at 21% and the bottom third at 17%, because electives multiply late.
5. *Secondary variable.* Node size grades the other way: 20px discs in first year down to 10px in final year, each inside a 44px hit area.
6. *Exceptions.* Six capstone courses (4%) take a hexagonal outline and a text tag, each ringed by ordinary nodes, not parked in a margin.
7. *Family.* A strip of four thumbnails shows the same rule run for four neighbouring specialisations, each with its seed in a fixed-width caption. Clicking one regrows the map.
- *Colour.* All paths are one cobalt on warm white. Completed courses are marked by a tick glyph and a doubled stroke, not by a second hue.
- *Access.* A "List" toggle gives the same graph as an indented outline. Growth plays once over 2s on first load; reduced motion shows the finished map.

Result: a blue administrative diagram, not a lamp or a coral. What survived is seed plus environment plus one gradient, merge into loops, stop on coverage, embedded exceptions, and the family.

## Space & composition
- **Fill by growth, not by grid.** Space is occupied by a process that stops when it meets itself or the boundary, so the gaps are even without being regular.
- **Hierarchy of widths.** Trunks, branches and veinlets step down in width, roughly halving at each branching level (Hyphae: few thick, many thin).
- **Density follows a gradient.** Material or holes get denser along one direction (toward the rim, toward the sources).
- **One family, many instances.** A screen may show several outputs of one rule side by side (eight lamps in the press image) to prove the rule.
- **Exceptions inside the field.** Special items sit inside the grown field, surrounded by ordinary units, not set apart in a margin.

## Color
*The hex table below is a reference sample for strict studies and homage only. For design, use the colour relations in "Process (derived)".*

The studio mostly lets the material carry the colour: white nylon, white porcelain, natural wood, black-on-white process drawings. The relation is a single value or material for the grown structure, a contrasting plain ground (white on black, black on white), and light passing through the voids as the second tone. In the puzzle the ground is one wood tone, and the cut lines (darker) are the only drawing. Translate as: the generated structure is one value; the ground is the opposite end of the value scale; density gradients, not hue changes, make emphasis; if colour is used, map it to the growth parameter (age, depth or generation) as a single ordered ramp, never as categories.

**Reference sample (studies and homage only)**

| Hex | Role |
|---|---|
| `#FFFFFF` | ground (Floraform photography) |
| `#E6E6E4` | grown structure in light |
| `#000000` | void field (Kinematics) |
| `#C9A06A` | single material (puzzle wood) |

## Form, line & typography
Lines are grown: they taper from trunk to tip, branch, merge and never cross. Surfaces ruffle at more than one scale. Type requirement: a clean, neutral, slightly technical sans in one or two weights that stays out of the way of complex generated forms (letters must not compete with veins), plus a monospaced voice for parameters and seeds; text sits on plain ground beside the generated field, never on top of it. For example, Space Grotesk with IBM Plex Mono.

## Rhythm, motion & time
Growth is the animation, and it is optional. A structure grows from its seed in small local steps (roots extend, edges ruffle) over 1–3 s, ending at a stable state; it can then be replayed or regrown with a new seed. Reduced motion: show the final grown state immediately, with a "replay growth" control. Never loop growth continuously behind text.

## UI translations
1. **Space-colonising navigation.** Generate a sitemap or dependency view by growing branches from root items toward leaf items (attraction points), step length 1–2% of the width, with branches merging when they meet, so the result is a vein network with loops, not a strict tree. Provide the same structure as an indented list for keyboard and screen-reader users.
2. **Edge-weighted density.** In a dense dashboard put the finest detail at the rim and keep the centre calmer, like the lamps' denser top (≈+25% density at the edge).
3. **Ruffle at two scales.** Give long dividers or progress edges a two-level wave (one primary wavelength, one secondary at 1/3–1/5 of it, amplitude 1/3) instead of a single sine; keep text clear of them by at least one line-height.
4. **Graded perforation.** In empty states, use a pattern of holes whose size grows from small near the anchor (the CTA) to large at the far edge; keep the CTA on plain ground.
5. **Rigid tiles, flexible layout.** Build a responsive grid of rigid identical tiles joined at hinges: as the viewport changes, tiles rotate and fold around their joints rather than resizing; tiles get smaller where the layout must bend more.
6. **Seeded variety.** Generate per-user or per-item visuals (avatars, covers, empty states) from one growth rule with a seed derived from the item ID, so each is unique and all are kin. Print the seed in a small monospaced caption.
7. **Exceptions inside the field.** Put featured items inside a grid of ordinary items, each surrounded by normal neighbours, and mark them by shape (figural outline) plus a label, not by colour alone.
8. **Map colour to generation.** If the structure needs colour, run one ordered ramp by growth age or depth (root dark → tip light), never categorical hues.
9. **Grow, don't fade.** New content enters by extending from its parent along a path (300–600 ms), then stops. Reduced motion: appear in place.
10. **Families, not singletons.** When presenting options, show 4–8 instances of one rule side by side so the rule is legible.

## What this artist would reject
- One hand-drawn hero object presented as final.
- Strict trees with no merging, or regular grids pretending to be organic.
- Decorative noise textures with no generative rule.
- Colour used as random categories on generated forms.
- Closed tools: algorithms hidden instead of explained.

## Signature prompt seed
Define a seed, an environment and one gradient, and let the screen's structure grow from them. Branches extend from root items toward targets, merge into loops where they meet and taper from trunk to tip. Density rises toward the rim, holes grade from small to large away from the anchor, and edges ruffle at two scales. Use one value for the grown structure against an opposite plain ground. Generate each item's visual from the same rule with its own seed, and show several kin side by side. Growth animates once and settles; reduced motion shows the final state.

## Sources
- Nervous System blog, "Floraform – an exploration of differential growth" (2015): https://n-e-r-v-o-u-s.com/blog/?p=6721
- Nervous System, Hyphae press kit (auxin flux canalization; base volume and root points; after Adam Runions): https://n-e-r-v-o-u-s.com/pressKit/hyphaeLamp.html
- Nervous System blog, "Generative jigsaw puzzles" (dendritic solidification cuts; Jonathan McCabe reaction–diffusion art): https://n-e-r-v-o-u-s.com/blog/?p=2368
- MoMA, Kinematics Dress (2013): https://www.moma.org/collection/works/185294
- Scientific American, "An Intricate 3D-Printed Dress, No Assembly Required" (Kinematics Fold compression): https://www.scientificamerican.com/blog/symbiartic/an-intricate-3d-printed-dress-no-assembly-required/
- Architect Magazine, "Natural Wonder" (Hyphae origins in leaf-venation research): https://www.architectmagazine.com/?p=96003
- Cross-reference: Neri Oxman (material ecology) and D'Arcy Thompson, *On Growth and Form* (1917).
