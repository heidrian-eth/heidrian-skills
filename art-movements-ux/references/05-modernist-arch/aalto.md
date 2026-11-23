# Alvar Aalto — Modernist / humanist architecture

## Essence
Aalto bent the functionalist grid around the body. He designed rooms, lights and chairs from the user's actual posture and line of sight (a patient on their back, a reader at a desk), not from the façade. A strict orthogonal frame lets one free curve run loose, in warm, touchable materials.

## Key works examined
- **Viipuri Library, 1927–35.** Deep cylindrical roof-lights give even, glare-free light. A stepped hall puts supervision at the top. A timber wave ceiling shapes the room's sound.
- **Paimio Sanatorium, 1929–33.** Ceilings are darker than walls, chosen for a patient lying down. Lights are placed out of the patient's view. A yellow floor marks the route from the lobby to the top floor.
- **Paimio armchair, 1931–32.** A plywood scroll angled to ease breathing: the form itself does the ergonomic work.
- **Stool 60, L-leg patented 1933.** One bent "knee" joint, made with Otto Korhonen, grew into a whole furniture system.
- **Savoy Vase, 1936.** First blown among wooden sticks. Its irregular wavy outline looks different from every side.
- **Villa Mairea, 1938–39.** Wavy pool and balconies set against right angles. Every column differs, to avoid "artificial architectural rhythms". Floors move from stone to timber as rooms get more private.

## Space & composition
- **Orthogonal frame, one free curve.** Plans are mostly rectilinear. The curve (the ceiling, the pool, the vase) appears once, where human activity is densest.
- **L-plans.** Wings wrap a courtyard. In UI, a top rail plus a left rail wraps the content, which becomes the courtyard.
- **Terraces, not cards.** Viipuri's hall drops in levels, with the control desk at the peak. Show hierarchy through changes of plane, not shadowed boxes.
- **Diffuse light from above.** Use many even sources, never one spotlight.
- **Planned irregularity.** Spacing varies by about ±15% inside a consistent system, like Mairea's mix of paired and wrapped posts.

## Color
Paimio's color logic is vertical: light walls, calmer darker ceilings, and a saturated yellow floor marking the route. Turquoise rails and orange accents appear in shared spaces. Strong color goes only where hands and feet go. The rest is birch and linen.

| Hex | Role |
|---|---|
| `#F3EEE3` | Wall: main surface |
| `#D9C3A0` | Birch: controls, wood-toned surfaces |
| `#5E7F74` | Paimio "ceiling" green-grey: top bars |
| `#E8B92F` | Floor yellow: the single route or progress line |
| `#3E9A9C` | Rail turquoise: affordances, focus rings |
| `#D9692B` | Café orange: rare accent |
| `#24221F` | Black lacquer: text, rules |

## Form, line & typography
Aalto's line is a long, taut straight run ending in a tight laminated bend: the L-leg knee, the scroll of the Paimio chair. There are no sharp 90° corners and no blobs either. Bend the joints and keep the runs straight. For type, use humanist sans faces with open apertures: **Source Sans 3** (UI and body), **Alegreya Sans** (more handmade), and **Literata** for warm display text. Use sentence-case headings and a gentle type scale.

## Rhythm, motion & time
- Motion should settle like bending plywood: overdamped, no bounce, `cubic-bezier(.3,.7,.2,1)`, 280–420ms.
- Let the overhead gradient shift with local time, cooler in the morning and warmer at dusk, like light through the skylights over a day.
- Repeat with variation, so scrolling never feels like a metronome.
- The wave ceiling sends sound toward listeners. In UI, feedback should travel from the touched control toward the content it changed.

## UI translations
1. **Layout:** Keep a strict 12-column grid and break it with exactly one free-form element per screen: a wavy, SVG-clipped panel edge where the main task lives.
2. **Layout:** Show hierarchy as terraces: indent nested levels 8–12px and shift tone by 2%, with no shadows. Put the overview at the top terrace.
3. **Posture-first:** Design for how the device is actually held. On mobile, put primary actions in the bottom 40% and keep the top bar quiet.
4. **Color:** Make the header darker (`#5E7F74`) than the light canvas, so the eye settles downward.
5. **Color:** Reserve one saturated yellow line (`#E8B92F`) for the user's path, such as a progress rail or active step, and use it nowhere else.
6. **Light:** Replace hard white cards with `radial-gradient(at 50% -20%, #fff, #F3EEE3 60%)`: glare-free light from above.
7. **Type:** Set body text in Source Sans 3 at 17px/1.55. Use a 1.2 type scale and build emphasis through weight, not size.
8. **Form:** Give every control the same 6px bent "knee" corner, one joint reused everywhere like the L-leg.
9. **Material:** Make surfaces warmer as users go deeper: flat linen for lists, a 2–3% birch-grain noise in detail views.
10. **Motion:** Use overdamped settling. Let a confirmation ripple outward from the control that was touched.
11. **Interaction:** Give frequently touched controls a tactile press state (1px inset plus a warmer tint), the way Aalto wrapped door handles in leather.
12. **Rhythm:** In grids of more than 6 items, vary gutters by about ±15% or pair items, so the grid reads as a forest, not a parking lot.

## What this artist would reject
- Glaring pure-white surfaces and spotlight heroes.
- Uniform card grids on a metronomic 24px gap.
- Organic curves everywhere, which makes them meaningless.
- Cold glassmorphism and chrome with no grain or warmth.
- Layouts made for the designer's upright monitor, ignoring the user's real posture.
- Decorative color unrelated to wayfinding or touch.

## Signature prompt seed
Design this screen as an Aalto room for a reclining user: a warm limewash canvas (#F3EEE3) under a darker green-grey header (#5E7F74), with soft light falling from above as a gradient, never glare. Hold a strict 12-column grid, then break it once with a single wave-edged panel where the main task lives. Mark the user's path with one Paimio-yellow line. Set Source Sans 3 on a gentle scale, give every control the same bent 6px corner, add faint birch grain deeper in, vary the rhythm slightly, and let motion settle like bending plywood.

## Sources
- https://finnishdesignshop.com/architecture/alvar-aalto-and-the-colors-of-the-paimio-sanatorium
- https://en.wikipedia.org/wiki/Vyborg_Library
- https://en.wikipedia.org/wiki/Aalto_Vase
- https://www.archdaily.com/85390/ad-classics-villa-mairea-alvar-aalto
- https://www.designboom.com/design/artek-vitra-the-making-of-the-patented-l-shaped-stool-60-by-alvar-aalto-01-31-2014/
