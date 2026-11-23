# Luis Barragán — Modernist architecture (Mexican)

## Essence
Barragán builds emotion from a few plain things: a high blank wall, one saturated colour, a slot of light, the sound of water. His spaces shut the world out and then ration what gets back in, so moving through them becomes a slow sequence of thresholds (dark, then coloured light, then open sky). Modernist abstraction is pushed toward ritual, and what you feel is serenity: in his words, "in my fountains, silence sings."

## Key works examined
- **Casa Luis Barragán, Mexico City (1947–48; UNESCO 2004)**: entry by compression. A bare, dim foyer leads to a high vestibule with yellow light and one fuchsia wall, then past a low threshold to a double-height white living room. The roof terrace walls (blood red, brownish grey, white) frame only the sky.
- **Capuchin Convent Chapel, Tlalpan (1954–c.1963)**: light you never see the source of. Yellow glass turns orange walls hotter, and an orange cross painted the colour of the wall seems to dissolve.
- **Cuadra San Cristóbal, with Andrés Casillas (1966–68)**: one long pink wall splits the site roughly 1:3. Portals are sized to a horse and rider, and a purple wall, a pink granary and a water spout make a composition of planes at landscape scale.
- **Casa Gilardi (1975–77)**: a 10 × 35 m lot organised around an existing jacaranda. The corridor has yellow walls, ceiling and glass and opens onto an indoor pool with a blue back wall and a magenta freestanding plane lit from a hidden skylight.
- **Pritzker acceptance speech (1980)**: a vocabulary of beauty, silence, solitude, serenity, joy, myth and the garden "poetic and mysterious."

## Space & composition
- **The wall is the subject.** Façades show almost nothing to the street. Each room is a box of 4–6 planes, and usually only one of them carries colour.
- **Compress, then release.** Low, dark and narrow first, then tall, bright and open. The ratio between the two is extreme: Casa Barragán goes from a squat foyer to a double-height room.
- **Asymmetric division.** A wall cuts the field off-centre (San Cristóbal is about 1:3). Openings are rectangles cut into large planes, never grids of windows.
- **Freestanding planes.** At Gilardi a magenta wall stands in the pool without touching the ceiling, which hides the light source and creates depth through overlapping layers.
- **Void as programme.** The courtyard, the pool and the sky framed by walls are the main rooms. Density sits in tiny pockets: a chair, a gold panel, a spout.
- **Human or animal scale tied to monumental scale.** One opening sized exactly to the body (horse plus rider) sits next to planes much larger than the body.

## Color
Colour is applied as a flat field across a whole plane, never as a highlight or a gradient. Adjacent planes clash (fuchsia beside ochre, magenta beside blue) instead of harmonising. Coloured light, such as yellow glass or a yellow corridor, tints the surfaces next to it, so the colour seems to come from the air.

| Hex | Role |
|---|---|
| `#E7417A` | Mexican pink / fuchsia: the one shouting plane per view |
| `#F2B705` | Gilardi yellow: corridors, transitions, light |
| `#7A5BA6` | Lavender-violet: secondary boundary wall |
| `#2F5FB3` | Pool blue: terminus, depth |
| `#C46A2B` | Ochre-orange: earth, warm ground |
| `#EFE8DC` | Lime-plaster white: the dominant quiet field |
| `#3B3632` | Volcanic stone / dark timber: floors, text |

Rules: about 70% plaster white, one saturated plane per screen, and at most two saturated hues meeting at a hard edge.

## Form, line & typography
The forms are orthogonal blocks with sharp arrises and rough stucco texture. There are no curves, mouldings or visible joints. The few lines are thresholds and shadow edges. The type should echo that: wide, sturdy, calm grotesques with almost no detail, set large with very generous tracking, plus a humanist serif for the rare poetic phrase. Suggested fonts: **Archivo** (wide or expanded widths for display, like a monumental inscription), **Work Sans** (body, plain and warm), **Cormorant Garamond** italic (one quiet line, used sparingly). Headings sit in the field like a portal in a wall: uppercase, small, widely letterspaced. Avoid stacked hierarchies.

## Rhythm, motion & time
Time is sunlight moving across a wall. Motion should be slow, ambient and indirect. A colour field can drift through a few lightness steps over minutes. A soft "light shaft" gradient can move across a plane as you scroll. Transitions work like doorways: the screen dims and narrows for about 200 ms, then opens to the next view over 700–900 ms with `cubic-bezier(.2,.7,.1,1)`. There should be no bounce, no stagger cascades and no parallax confetti. Water appears only as a slow, faint, low-amplitude ripple or reflection at the base of a coloured plane.

## UI translations
1. **Layout:** Make 60–75% of each screen a single flat, uninterrupted colour or plaster field, and put content in one rectangular "portal" cut off-centre, around the 1:3 line.
2. **Layout:** Start every flow with a compressed screen (narrow max-width of about 28ch, dim background, small type), then release into a full-bleed spacious view. Enforce the contrast between the two.
3. **Color:** Allow exactly one saturated plane per viewport (pink, yellow or violet) as a full panel edge to edge. Never use a saturated pill, chip or underline.
4. **Color:** Tint neighbours with light. Give the panel next to a yellow block a `#F2B70514` wash so the colour seems to spill like light through glass.
5. **Layering:** Use a freestanding plane, an offset card with no border, radius or shadow, that overlaps the hero by about 15% and hides the image's edge, the way Gilardi's magenta wall hides the skylight.
6. **Type:** Set headings in Archivo Expanded, uppercase, `letter-spacing: .25em`, at 12–14 px inside huge fields. Let quiet type in a vast plane do the monumental work.
7. **Light:** Light a key panel from an unseen source: an off-canvas `radial-gradient` that brightens one edge, with no visible icon or glow object.
8. **Motion:** Slow down navigation by default: a 700–900 ms crossfade-and-widen between sections, and an ambient lightness drift of no more than 3% on the hero over 60 s.
9. **Interaction:** Hide the next section behind a threshold, a full-height colour plane the user has to cross, with the next content revealed only through a narrow vertical slot that widens on scroll.
10. **Interaction:** Hover and focus states change the colour of a whole plane (such as a row's full background) instead of adding borders or icons.
11. **Seclusion:** Keep the chrome walled off. No sticky header, no visible nav until the user asks for it. The screen is a courtyard, not a street.
12. **Scale:** Size one control exactly to the body, such as a 56 px tap portal, and place it in a field more than 10× larger.

## What this artist would reject
- Dashboard walls of equal cards, the opposite of a single framed void.
- Gradients, drop shadows and glassmorphism that blur the edge where two planes meet.
- Rainbow accent systems and colour as decoration on small elements.
- Everything visible at once: mega-menus, sticky banners, "open-plan" pages with no thresholds.
- Snappy, bouncy, attention-seeking motion and notification noise.
- Curved, bubbly, rounded-everything forms.

## Signature prompt seed
Design this screen as a walled Mexican courtyard. Make about 70% of it a single flat plaster-white or fuchsia field with rough, unshadowed edges. Cut one off-centre rectangular portal into it, around the 1:3 line, to hold the content. Allow only one saturated plane per view (pink #E7417A, yellow #F2B705 or violet #7A5BA6) meeting a second at a hard edge, with yellow spilling onto its neighbour like light through glass. Use small, widely tracked Archivo Expanded capitals. Enter through a narrow, dim screen before opening wide. Make transitions slow and doorway-like, and keep everything silent and secluded.

## Sources
- https://www.pritzkerprize.com/sites/default/files/inline-files/1980_Acceptance_Speech.pdf
- https://barragan-foundation.org/works/list/gilardi-house
- https://barragan-foundation.org/works/list/cuadra-san-cristobal
- https://barragan-foundation.org/works/list/capuchin-convent-chapel
- https://en.wikipedia.org/wiki/Luis_Barrag%C3%A1n_House_and_Studio
- https://www.archdaily.com/958804/why-did-luis-barragan-win-the-pritzker-prize
- https://www.domusweb.it/en/from-the-archive/2013/03/23/luis-barragan-seclusion-and-serenity.html
