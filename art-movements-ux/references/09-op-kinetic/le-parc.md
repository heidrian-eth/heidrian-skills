# Julio Le Parc — Kinetic art (Argentine; GRAV)

## Essence
Le Parc picks a small, closed set of parts (14 pure hues, a few hundred mirrored squares, one light source) and lets a rule, a breath of air, or the visitor's body produce endless variations of them. The work is never a fixed image. It is a system that is running, and the viewer is expected to set it off, rearrange it, or even break it. His game works rest on one idea: taking part matters more than finishing.

## Key works examined
- **Fourteen Colors – Sequence, 1959** (Met; gouache, 49.7 cm square). A grid of squares and circles where shifting color steps make a still image look like it moves.
- **Projet Couleur / Feuilles du Dossier Couleur, 1959–70.** Colors are written down as numbers, and arrangements are worked out like permutations. He reckoned that painting every combination of one method would take 150 years.
- **Double Concurrence—Continuous Light, 2, 1961** (MoMA). A black box with a 20 × 20 cm lit opening. Inside, 54 plastic squares of 3.6 cm hang on 18 threads in front of a mirror, with screens and filters you can swap. It is a tiny stage for light.
- **Continuel-Lumière Mobile, 1960 onward.** Curtains of small steel discs or squares on nylon, lit by projectors. The real artwork is the moving spatter of reflections they throw on the room.
- **Une journée dans la rue (GRAV), 19 April 1966.** A day-long schedule across Paris: gifts handed out at the Châtelet metro at 8 a.m., buildable structures on the Champs-Élysées, a giant kaleidoscope, and paving slabs at Montparnasse that moved underfoot.
- **Miroir en vibration and 3 jeux avec balles de ping-pong, 1965.** Press a button, and something shivers or a ball rolls through a course. The museum piece becomes a toy.
- **La Longue Marche, 1974.** Ten 200 × 200 cm canvases. A ribbon in the 14 colors winds across all of them with no center and no hierarchy.

## Space & composition
- **Modular square cells.** The canvases are square, the openings are square, and the units are square. Build on a strict square module (for example 8 px × n) and never use a golden-ratio layout.
- **No focal point.** In La Longue Marche nothing sits at the center and nothing dominates. Spread visual weight evenly across the field and let the *sequence* lead the eye, not a hero element.
- **A dark frame around a small bright opening.** The 1961 box puts a 20 cm lit window in a black case of about 53 × 50 cm, so the light takes up roughly 15% of the face. Copy that in UI: a near-black chrome with a small, intensely active panel.
- **Panels as frames of a film.** Series like Séquences progressives and the ten-panel Longue Marche read like stills from one movie. Lay out carousels and dashboards as numbered panels where each one moves the rule forward a single step.
- **Density from repeating one unit.** Fifty-four identical squares, never mixed shapes. Use one tile component and let the variety come from position and state.

## Color
His rule was strict: 14 pure hues, never mixed with black or white, no colors outside the set, and no color used alone. They always come as a run or scale. He got there by starting with 7, then going to 10, then 12. Treat the 14 as a closed hue ring and spend all your contrast on *order*, not on tints.

| Role | Hex | Note |
|---|---|---|
| Ground / chrome | `#0B0B0D` | the black box, the darkened room |
| Light / reflections | `#F4F4F0` | the projector, steel glints |
| Ring step 1 | `#E5222B` | red, the start of every sequence |
| Ring step 4 | `#FFB000` | orange-yellow |
| Ring step 7 | `#19A34A` | green |
| Ring step 10 | `#1F5BD8` | ultramarine |
| Ring step 13 | `#C2188B` | magenta, the ring closes back to red |

A full ring is about 14 hues spaced roughly 25.7° apart on an OKLCH wheel at nearly the same lightness and chroma, for example `oklch(68% .19 calc(29deg + n*25.7deg))`. Show colors only as adjacent runs of 3 or more. A single colored badge breaks the system.

## Form, line & typography
The shapes are the square, the circle, the thin vertical thread, and the band that cuts a circle into slices. The type should feel equally modular and engineered, like a lab notebook more than editorial design. Write labels the way he titled his works, as series codes: "Série 14-2 · n°3".
- **Space Mono** for codes, counts, and step numbers.
- **Archivo** (wide/expanded) for display, like the flat, even letters of 1960s exhibition posters.
- **IBM Plex Sans** for body text.
Keep the type monochrome on the dark ground. Color lives in the system, not in the words.

## Rhythm, motion & time
- **Continuous, low-amplitude drift.** Continuel means always running. Idle states should never freeze. Give tiles a slow, out-of-sync sway (rotateY ±12°, 6–11 s periods with randomized phase), like squares on nylon in moving air.
- **Light that slides across a surface.** Reflections crawl over walls. Animate a soft radial highlight across cards with `background-position`, tied to the cursor or to device tilt.
- **Stepping, not easing.** The color sequences move forward in discrete steps. Use `steps(14)` timing for hue cycles, the way a gouache series moves one frame at a time.
- **Pulse and jolt.** Lumière saccadée and the "surprise movement" boxes jerk around. Add one deliberate `steps()` jitter on activation, then return to calm drift.

## UI translations
1. Build the main surface as a square grid of identical tiles (for example 12 × 12). Every piece of content is a tile state, never a different component.
2. Give every colored sequence its hues in ring order, at least 3 adjacent steps. Never use a lone accent color.
3. Use no tints or shades of the accent hues. Hover and disabled states change *position in the sequence* or opacity, not lightness.
4. Frame the active workspace as a small lit window (about 15–25% of the viewport) set in near-black chrome.
5. Number everything like a series: "Variation 07 / 14". Show progress as moving along the ring.
6. Add a "permute" control that reshuffles the layout or palette order by a rule. Show the rule (for example "shift +3") so the variations are legible.
7. Let a cursor-following light source throw reflected squares (CSS `box-shadow` or canvas) onto the background, like a Continuel-Lumière mobile.
8. Animate idle tiles with independent sway on random phases. Respect `prefers-reduced-motion` by swapping sway for a static staggered offset.
9. Make onboarding a timed itinerary like Une journée dans la rue: small gifts (a reward or a preset) at fixed points, each asking the user to *do* something physical, such as drag, tilt, or rearrange.
10. Make it safe to break things. Give users a one-tap "dismantle" that scatters the layout and a "reassemble" that puts it back. Messing it up is part of the work.
11. Lay type flat on dark: Archivo Expanded headings in off-white, Space Mono series codes, and no colored text.
12. Hand over agency: buttons should trigger visible mechanical results (a vibration, a rolling marker), not just change a route.

## What this artist would reject
- The single brand accent color sprinkled across badges. Colors only appear as an ordered scale.
- Hero-centric layouts that point the eye at one star element.
- Frozen, finished screens. A UI with no idle life is a picture, not a system.
- Gradient blends and tinted pastels. He kept his hues pure and stepped.
- Mystified "magic" interactions that hide their rules. GRAV's manifesto, Assez de mystifications, demanded a conscious participant.
- Precious, untouchable interfaces where nothing can be rearranged or undone.

## Signature prompt seed
Design this screen as a running kinetic system in the manner of Julio Le Parc. Use a near-black chrome around a small lit square window holding a 12 × 12 grid of identical tiles. Colors come only from a closed ring of 14 pure, equal-lightness hues, always shown as adjacent ordered runs, never alone, never tinted. Tiles sway on independent slow phases, and a cursor-driven light throws reflected squares across the background. Label everything as series codes in Space Mono ("Série 14-2 · n°5"). Add permute, dismantle, and reassemble controls with visible rules, so the user plays, breaks, and rebuilds it.

## Sources
- https://metmuseum.org/art/collection/search/815316
- https://www.moma.org/collection/works/81125
- https://en.wikipedia.org/wiki/Groupe_de_Recherche_d%27Art_Visuel
- https://ocula.com/art-galleries/perrotin/exhibitions/julio-le-parc-color-and-colors/
- https://www.studiointernational.com/index.php/julio-le-parc-light-and-movement
- https://www.artbasel.com/catalog/artwork/55449/Julio-Le-Parc-La-Longue-Marche?lang=zh_CN
- https://www.fondationdentreprisehermes.org/sites/default/files/programmes/lescouleursenjeu_guidebook.pdf
- https://www.tate.org.uk/kids/artists/who-julio-le-parc
- https://ocula.com/magazine/reports/julio-le-parc-nostalgia-for-optimism/
