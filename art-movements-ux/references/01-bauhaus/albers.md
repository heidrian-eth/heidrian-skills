# Josef Albers — Bauhaus

## Essence
Albers fixed everything except color, then let color do all the work. A rigid, repeatable format (nested squares, a modular alphabet, a paper exercise) is a laboratory in which the same hue becomes two colors, flat planes advance and recede, and perception is shown to be relative. His art is the system that varies, not the single image: hundreds of panels from one template.

## Key works examined
- **Homage to the Square series, 1950–1976.** One fixed format of three or four nested squares, repeated for 26 years: color is the only variable.
- **Homage to the Square: Light Passage, 1956 (AIC).** Four squares: neutral grey outer, ochre, mottled olive, saturated orange core. *(visually checked: AIC scan; measured)*
- **Homage to the Square: Yellow Signal, 1962 (AIC).** Three squares, 10/8/6, in one yellow family; the core is the most saturated. *(visually checked: AIC scan; measured)*
- **Homage to the Square: Promise, 1967 (AIC).** Three yellow squares, 10/8/6, almost the same tonal theme as Yellow Signal. *(visually checked: AIC scan; measured)*
- **Homage to the Square: New Light, 1967 (AIC).** Three squares, 10/6/4 (the 8 ring omitted), dark teal to light green core. *(visually checked: AIC scan; measured)*
- **Homage to the Square: With Rays, 1959 (Met).** Described as a dull-gray core inside three yellows. *(not visually checked: no image reachable from the allowed sources)*
- **Tenuous, 1962 (MoMA screenprint).** Solid, unmodulated fills, yet depth shifts at every edge. The illusion comes from adjacency, not gradients.
- **Interaction of Color, 1963.** Paper exercises such as "one color appears as two": test colors in context, never as swatches.
- **Kombinationsschrift stencil alphabet, 1926–31.** Letters snapped together from a square, a triangle and a quarter-circle on a 1:3 grid, for posters and signage. A kit-of-parts type system.
- **Bauhaus glass pictures (e.g. *Fugue*, 1925).** Sandblasted bands in strict orthogonal rhythm.

## Process (derived)
*From observation to process (see SKILL.md §1). This is what transfers; the rest of the file is evidence.*

**Josef Albers.** *Freeze the geometry so that colour is the only variable, then tune each colour by its neighbours until one edge dissolves and another jumps.*
Process:
1. Fix one layout of 3–4 regions and use it unchanged on every view. From here on nothing but fill may vary, so every difference the viewer sees is a colour difference.
2. Arrange the regions so each one borders only its neighbours in a single order, outermost to core (nested, or stepped from one side). No region touches a non-neighbour, so every edge is a controlled pair.
3. Offset each inward step unequally: `u` at the sides, 0.5`u` on the heavy side, 1.5`u` on the opposite side (`u` = 1/9–1/10 of the format). The core sits off-centre along one axis and keeps 11–36% of the area.
4. Build one ladder of 3–4 flat, opaque fills that runs monotonically from the outermost region to the core in value, in chroma, or in both. Regions meet at hard edges with no line, gap or shadow between them.
5. Space the ladder unevenly: outer neighbours 3–5 L apart at near-equal chroma; the last step into the core is the big one, and the core is the extreme of the ladder (highest chroma, about 1.4× its neighbour or more, or the lightest or darkest value).
6. Judge every fill in place against its real neighbours, never as a swatch. Before adding a fill, try an existing one on a second ground: one fill on two grounds gives two apparent colours.
7. Make variation serial: the next view or state is the same layout with a new ladder.
Why it works:
- Simultaneous contrast: a fill is pushed away from its surround in value and hue, so a ladder ordered by adjacency controls how every region looks. A region touching a non-neighbour gets an uncontrolled edge and the tuning is lost.
- Edge strength is the hierarchy. Close outer steps fuse into one field and the single large step isolates the core with no outline. Equal steps make a striped target with no focus.
- The unequal offset makes the regions read as stacked planes with weight. Centred, they read as a bullseye or a tunnel, and the eye fixes on the geometry instead of the colour.
Colour relations: one ladder per view, in one hue family or from a near-neutral outer field to one saturated core; outer steps 3–5 L apart; the core the most saturated or the extreme value; area shares run 36 : 28 : 36 (three regions) or 40 : 30 : 20 : 11 (four); no second accent, no transparency, no gradient.
Space and line: no drawn lines; offsets 1 : 0.5 : 1.5 per step; symmetric on one axis and weighted on the other; region sizes 10/8/6, 10/6/4 or 9/7/5/3 units; a step may be skipped.
Type requirement: one plain text voice in few weights, in an ink at the opposite value extreme from the ladder (≥4.5:1 on every region that carries text; text sits on at most two regions); display built from a few modules on the unit `u`.
Motion and interaction: geometry never moves. A state change re-tunes the ladder: the focused region takes the large step (≥3:1 against its neighbour) over 600–900ms, core first; selection also changes a label, mark or weight, because two outer fills 3–5 L apart cannot signal state alone.
Fails when: the content is many peer items (a 20-row table has no 3–4 level order); status hues must appear (they break the ladder); the core holds photographs or video whose colours override the tuning; reading text must sit on mid-value regions.
Signature (do not carry together): concentric squares · the low-set 1 : 3 margin · a single yellow or ochre family in flat unmixed paint.

**Transfer test** (an illustration that the process survives new colours and content; never reuse its hues, layout or wording as a design answer):

Product: dark-mode code-review tool, desktop 1440 × 900, dense monospaced text, cool slate. Shares no palette, content or shape with the source.
1. *Layout, fixed for every pull request.* Three regions stepped from the left edge, not concentric: repository context, changed-file surround, the hunk under review.
2. *Adjacency.* Context touches only the surround; the surround touches only the hunk. The comment rail lives inside the hunk region so it creates no fourth neighbour.
3. *Offset.* `u` = 90px. Each step is 90px in from the right, 45px up from the bottom, 135px down from the top; the left edges step 90px. The hunk keeps 34% of the area and sits low and right.
4. *Ladder.* Slate at L 13, L 17, L 27; chroma 3, 4, 6. Flat fills, no borders, no elevation.
5. *Uneven steps.* Context to surround is 4 L, so that edge almost disappears; surround to hunk is 10 L, so the hunk is the only thing with an edge. The hunk is the lightest and the most chromatic.
6. *In place.* The "commented line" tint is one fill (L 34). On the surround's file list it reads as a clear highlight; inside the hunk it reads as a faint band. Both were checked on their grounds; no second token was made.
7. *Series.* Draft, in review and approved are three ladders on the same geometry (cooler, neutral, slightly warmer); the status is also written as a word beside the title.
- *Type.* One mono family, two weights, ink at L 92 (11:1 on the hunk). Text only on the surround and the hunk.
- *Interaction.* Focusing a file moves the large step: its row goes to L 27 over 700ms and gains a 3px start marker. Nothing translates or scales.
Result: a quiet slate workspace where one panel carries the only strong edge. No squares, no yellow. A viewer would not name the source; what survived is fixed geometry, neighbour-only adjacency and one unequal ladder.

## Space & composition
- **The bottom-heavy nest.** The margin below each inner square is smaller than the margin above, so the stack sinks. Measured on four AIC scans: every inward step is 1u at the sides, 0.5u below and 1.5u above (bottom:top = 1:3), within ±0.07u. Three-square works use a 10u field with squares of 10/8/6 (Yellow Signal, Promise) or 10/6/4 (New Light, one ring skipped, so that step is 2u/1u/3u). The four-square Light Passage measures 9/7/5/3 (u = outer side / 9; outer 807 px, rings 625/446/263 px). The result is symmetric horizontally and weighted vertically: calm, never static.
- **Area shares.** 10/8/6: outer ring 36%, middle ring 28%, core 36%. 9/7/5/3: outer 40%, then 30%, 20%, core 11% (k-means on Light Passage: 37/31/21/11%).
- **Frames, not containers.** Each ring is content. An edge exists only where two flat fields meet.
- **Concentric hierarchy.** Outside = context, center = focus.
- **Serial variation.** Same format on every screen. Vary only the tonal theme.
- **Density:** three or four regions per view, and the void is colored rather than white.
- **Edges:** hard and straight, never softened. Fills are flat but not mechanical: the olive ring of Light Passage is visibly mottled.

## Color
*The hex table below is a reference sample for strict studies and homage only. For design, use the colour relations in "Process (derived)".*

**Color is relative**: Albers called it the most relative medium in art. The ground decides how the figure's color looks. Use (1) a value/chroma ladder that steps monotonically toward the core, either one hue family (Yellow Signal, New Light) or a neutral outer field stepping to one saturated core (Light Passage: grey C\*7 → ochre → olive → orange C\*70), (2) a core that is the extreme of the ladder, the most saturated or the lightest, and (3) one token on two grounds so it reads as two colors. In all four checked works the core is the most saturated field; the outer rings differ from each other by only ~3–5 L\* (Yellow Signal: L\*83 → 86, then core L\*90 with C\*84 against 59–62), so outer edges nearly dissolve and the core jumps. He applied paint unmixed, straight from the tube, so use flat, opaque fills. The palette below is sampled from *Light Passage* (AIC):

| Hex | Role |
|---|---|
| `#99988B` | Outer field / page ground (neutral warm grey, ~37% of the surface) |
| `#B58F43` | Second ring: section surface (ochre, ~31%) |
| `#9C8020` | Third ring: card / active zone (olive, mottled, ~21%) |
| `#CC6A05` | Core: content and focus (saturated orange, ~11%: the most saturated field, not a dull grey) |
| `#CFCABE` | Primer white: the panel's visible white edge, rare text-on-dark |
| `#2B2A26` | Ink: body text, used sparingly (not in the paintings; a UI necessity) |

High-key alternative theme, sampled from *Yellow Signal*: outer `#ECCC5A`, ring `#F4D55F`, core `#FDE631`. Lighting note: AIC scans; Promise samples within 2 levels of Yellow Signal.

## Form, line & typography
The Kombinationsschrift treats a letter as an assembly of a few primitives, with the stencil gaps left visible. In UI, build display headings and icons from a few geometric parts on the layout's unit grid, and keep text type plain so it does not compete with the color.
- **Big Shoulders Stencil Display** (Google Fonts): display only, with visible bridges, in the poster-and-signage spirit.
- **Jost** (Google Fonts): Futura-lineage geometric sans for UI and body text.
- **IBM Plex Mono**: for "label on the back of the panel" metadata such as color names and values.

## Rhythm, motion & time
The paintings move while standing still: edges vibrate and planes swap depth as the eye adapts. Motion should be **chromatic, not spatial**. Transition background tokens while geometry stays put (`transition: background-color 900ms cubic-bezier(.4,0,.2,1)`), so a ring appears to step forward or back. Time unfolds as a series: page 2 is the same nest in a new tonal theme. Nothing bounces, slides or scales.

## UI translations
1. **Layout:** On a square or full-bleed field, nest three regions at 10/8/6 (or 10/6/4) units, or four at 9/7/5/3. Each inward step is 1u in at the sides, 0.5u up from the bottom and 1.5u down from the top, so the content core sits low.
2. **Layout:** Replace cards-with-shadows with concentric color fields. Hierarchy = depth of nesting. Delete every `box-shadow` and `border`.
3. **Color:** Build each screen from a 3–4 step ladder (one hue family, or neutral outside to saturated inside). Keep outer steps close (ΔL\* 3–5) and make the most important element the extreme: the most saturated or the lightest.
4. **Color:** Reuse one hex for the selected state on two different surfaces and let the grounds make it read as two colors, instead of minting a new token.
5. **Color:** Use opaque fills only: no `opacity`, no gradients, no blur. Every perceived blend must come from adjacency.
6. **Type:** Set headings in a modular stencil face at poster size (≥ 8vw), assembled to the same grid unit as the layout. Body text in Jost at a quiet weight.
7. **Type:** Print a "verso label" footer in mono that lists the screen's color tokens, the way Albers listed his paints on the back of each panel.
8. **Motion:** On navigation, keep the geometry frozen and cross-fade only the colors of the rings, inner to outer, staggered by ~120ms. Albers painted from the center outward.
9. **Interaction:** On hover or focus, swap the value order of two adjacent rings so the focused plane appears to advance. No translate or scale.
10. **Interaction:** Offer a "theme as series" control: the user flips through tonal variations of one fixed layout, like a portfolio of ten prints.

## What this artist would reject
- Drop shadows, glassmorphism and elevation as hierarchy, which fake depth that color alone could produce.
- Gradients and translucency that do the color mixing for the viewer instead of letting the eye do it.
- Swatch-picked palettes approved in isolation and never tested on their actual neighbors.
- Vertically centered hero blocks that float with equal margins and no gravity.
- A new layout for every screen when one format with varied color would say more.
- Decorative motion (springy scales, parallax) that moves objects when only perception needs to move.

## Signature prompt seed
Design this app screen as a Josef Albers Homage: a full-bleed field of flat, opaque color with three nested regions on a 10-unit grid (10/8/6). Each inner region sits lower than center, with margins 1u at the sides, 0.5u below and 1.5u above. Use one hue family in close value steps. The core content panel is the most saturated tone so it glows. No borders, shadows, gradients or transparency. Headings use a geometric stencil face at poster scale, body text uses Jost, and a mono footer lists the hex values. State changes only swap ring colors, slowly, from the center outward.

## Sources
- https://en.wikipedia.org/wiki/Homage_to_the_Square
- https://www.metmuseum.org/toah/works-of-art/59.160
- https://www.moma.org/collection/works/90989
- https://archive.bridgesmathart.org/2016/bridges2016-233.html
- https://en.wikipedia.org/wiki/Architype_Albers
- https://exhibitions.letterformarchive.org/bauhaus/walkthroughs/inside-offset-two-experimental-bauhaus-alphabets
- https://www.themarginalian.org/2013/08/16/interaction-of-color-josef-albers-50th-anniversary/
- https://www.albersfoundation.org/learning/workshops/one-color-becomes-two
- Images (visual check): https://www.artic.edu/artworks/5569 (Light Passage, IIIF e81e3afd-69a7-915d-d93d-4b1c2ab91bfe), https://www.artic.edu/artworks/15257 (Yellow Signal, IIIF c696dd0e-3166-f4e3-3159-525bf266249a), https://www.artic.edu/artworks/60281 (Promise, IIIF 76af207b-150d-c328-d8ef-189fc6848ae8), https://www.artic.edu/artworks/66164 (New Light, IIIF 896b2529-fd62-2a2c-80d9-3702d916f90a)
