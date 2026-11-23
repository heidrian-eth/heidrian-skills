# Josef Albers — Bauhaus

## Essence
Albers fixed everything except color, then let color do all the work. A rigid, repeatable format (nested squares, a modular alphabet, a paper exercise) is a laboratory in which the same hue becomes two colors, flat planes advance and recede, and perception is shown to be relative. His art is the system that varies, not the single image: hundreds of panels from one template.

## Key works examined
- **Homage to the Square series, 1950–1976.** One fixed format of three or four nested squares, repeated for 26 years: color is the only variable.
- **Homage to the Square: With Rays, 1959 (Met).** A dull-gray core inside three yellows. The least saturated field reads as the most luminous.
- **Tenuous, 1962 (MoMA screenprint).** Solid, unmodulated fills, yet depth shifts at every edge. The illusion comes from adjacency, not gradients.
- **Interaction of Color, 1963.** Paper exercises such as "one color appears as two": test colors in context, never as swatches.
- **Kombinationsschrift stencil alphabet, 1926–31.** Letters snapped together from a square, a triangle and a quarter-circle on a 1:3 grid, for posters and signage. A kit-of-parts type system.
- **Bauhaus glass pictures (e.g. *Fugue*, 1925).** Sandblasted bands in strict orthogonal rhythm.

## Space & composition
- **The bottom-heavy nest.** The margin below each inner square is smaller than the margin above, so the stack sinks. The common analysis uses a 10-unit field: squares of 10/8/6/4, per-step margins of 1u at the sides, about 0.5u below and 1.5u above (≈ 1:3). The result is symmetric horizontally and weighted vertically: calm, never static.
- **Frames, not containers.** Each ring is content. An edge exists only where two flat fields meet.
- **Concentric hierarchy.** Outside = context, center = focus.
- **Serial variation.** Same format on every screen. Vary only the tonal theme.
- **Density:** three or four regions per view, and the void is colored rather than white.

## Color
**Color is relative**: Albers called it the most relative medium in art. The ground decides how the figure's color looks. Use (1) one-hue value ladders with small steps, (2) a desaturated core that glows against saturated surrounds, and (3) one token on two grounds so it reads as two colors. He applied paint unmixed, straight from the tube, so use flat, opaque fills. The palette below approximates the tonal theme of *With Rays*:

| Hex | Role |
|---|---|
| `#C98A1B` | Outer field / page ground (deep ochre) |
| `#E0A526` | Second ring: section surface |
| `#EEC14A` | Third ring: card / active zone |
| `#C9C3B3` | Core: content and focus (dull gray that reads as light) |
| `#F4F1EA` | Primer white: outer frame, rare text-on-dark |
| `#2B2A26` | Ink: body text, used sparingly |

## Form, line & typography
The Kombinationsschrift treats a letter as an assembly of a few primitives, with the stencil gaps left visible. In UI, build display headings and icons from a few geometric parts on the layout's unit grid, and keep text type plain so it does not compete with the color.
- **Big Shoulders Stencil Display** (Google Fonts): display only, with visible bridges, in the poster-and-signage spirit.
- **Jost** (Google Fonts): Futura-lineage geometric sans for UI and body text.
- **IBM Plex Mono**: for "label on the back of the panel" metadata such as color names and values.

## Rhythm, motion & time
The paintings move while standing still: edges vibrate and planes swap depth as the eye adapts. Motion should be **chromatic, not spatial**. Transition background tokens while geometry stays put (`transition: background-color 900ms cubic-bezier(.4,0,.2,1)`), so a ring appears to step forward or back. Time unfolds as a series: page 2 is the same nest in a new tonal theme. Nothing bounces, slides or scales.

## UI translations
1. **Layout:** On a 10-unit square or full-bleed field, nest three or four flat regions at 10/8/6/4 units. Offset each inward step 0.5u from the bottom and 1.5u from the top, so the content core sits low.
2. **Layout:** Replace cards-with-shadows with concentric color fields. Hierarchy = depth of nesting. Delete every `box-shadow` and `border`.
3. **Color:** Build each screen from a single-hue value ladder of 4 steps, and make the most important element the *least* saturated one.
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
Design this app screen as a Josef Albers Homage: a full-bleed field of flat, opaque color with three nested regions on a 10-unit grid (10/8/6/4). Each inner region sits lower than center, with margins 1u at the sides, 0.5u below and 1.5u above. Use one hue family in four value steps. The core content panel is the least saturated tone so it glows. No borders, shadows, gradients or transparency. Headings use a geometric stencil face at poster scale, body text uses Jost, and a mono footer lists the hex values. State changes only swap ring colors, slowly, from the center outward.

## Sources
- https://en.wikipedia.org/wiki/Homage_to_the_Square
- https://www.metmuseum.org/toah/works-of-art/59.160
- https://www.moma.org/collection/works/90989
- https://archive.bridgesmathart.org/2016/bridges2016-233.html
- https://en.wikipedia.org/wiki/Architype_Albers
- https://exhibitions.letterformarchive.org/bauhaus/walkthroughs/inside-offset-two-experimental-bauhaus-alphabets
- https://www.themarginalian.org/2013/08/16/interaction-of-color-josef-albers-50th-anniversary/
- https://www.albersfoundation.org/learning/workshops/one-color-becomes-two
