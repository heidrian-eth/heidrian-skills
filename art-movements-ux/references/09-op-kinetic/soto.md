# Jesús Rafael Soto — Kinetic art (Venezuelan)

## Essence
Soto's images exist in the gap between a foreground of thin lines and a ground of stripes or air, and they only switch on when the viewer moves. Form comes from the density of many identical strokes, never from outlines, so a solid shape seen from far away turns into air up close.

## Key works examined
- **Première vibration, 1957**: wire in front of black-and-white stripes. The moiré comes from layering.
- **Vibration, 1960 (MoMA)**: oil and wire on wood, 99.7 × 99.7 × 2.5 cm. Only 2.5 cm deep, yet it reads as deep.
- **Light Trap, 1965 (Tate)**: wood, nylon and printed paper. Cheap, thin materials turned into shimmer.
- **Volume suspendu, 1968 (Pompidou)**: blue and black volumes of 63 rods each (rows of 11 alternating with 10) in front of a striped panel.
- **Penetrables, 1967 onward**: thousands of single-colour tubes hung like rain. BBL Jaune (1999) fills more than 150 m³.
- **Houston Penetrable, 2004–14**: 24,000 PVC tubes, 28 ft tall. A yellow ellipse inked across clear tubes reads as a floating orb.
- **Sphère Lutétia, 1996**: a Virtual Volume. Coloured beams make a sphere from afar and come apart as you approach.

## Space & composition
- **Two planes, small gap.** Every Vibration stacks a striped ground, a gap of about 1–3 cm, then sparse lines. The effect is parallax between planes, not anything drawn.
- **Volume as density.** A Virtual Volume is a grid of identical strokes, and the coloured ones fill a sphere, ellipse or cube. No outline is ever drawn.
- **Phase shift.** Rows of 11/10/11/10 offset the grid by half a pitch, like brickwork, so it never looks static.
- **Whole field, edge to edge.** Penetrables hang from a full ceiling grid. Composition means picking which region of a uniform field gets saturated.
- **Scale jumps.** The same idea works at 55 cm (the Lutétia model) and at 28 ft (Houston).

## Color
One saturated hue sits in a neutral field of stripes, clear plastic or white. Colour marks where the virtual body is and is never decoration.

| Hex | Role |
|---|---|
| `#F5F3EE` | Ground: off-white wall or gallery air |
| `#111111` | Stripe/rod black: the vibration lines |
| `#F2C200` | Signature yellow: the virtual volume (Houston, BBL Jaune) |
| `#1F4FA8` | Soto blue: a second volume or alternate state |
| `#D8DDE0` | Translucent "clear tube": inactive strands at about 40% opacity |
| `#C8102E` | Rare red accent: one per screen at most |

## Form, line & typography
Soto's whole vocabulary is the thin line repeated: hairline stripes, straight rods, and small T-shaped pieces he called "Tes." For type, that means monolinear, low-contrast geometric letters. Track uppercase labels at +0.08em so they read as evenly spaced rods. Body text should be light and evenly textured, like a striped ground.
- **Space Grotesk** or **Jost**: geometric, monolinear headings.
- **IBM Plex Mono**: even pitch for data, which echoes the rod grid.
- Avoid heavy weights. The heaviest mark on the page should be a coloured field, not a word.

## Rhythm, motion & time
The work changes only when the viewer moves, so motion should come from the user (cursor, scroll, tilt), never from autoplay. Moiré turns a small offset into a large visual change. Penetrables sway when touched, then settle: a damped spring with a slow return over about 800–1200 ms. From far away you see the shape, and up close you see the strands.

## UI translations
1. **Layout:** Put a full-bleed ground of 1px black lines on a 4px pitch (`repeating-linear-gradient`) behind sparse foreground rules, and move the foreground 2–6px with the cursor so moiré shimmers.
2. **Layout:** Build hero shapes from a grid of 2px vertical bars. Colour the bars inside an ellipse and leave the rest at 15% grey, with no outline.
3. **Layout:** Offset alternate rows of repeated items (cards, icons, list markers) by half a column, the way the 11/10 rows do in Volume suspendu.
4. **Color:** Keep 90% of the screen achromatic. Use one saturated hue (`#F2C200`) only for the "virtual volume", meaning the current selection or primary state. Never use it on chrome.
5. **Color:** Show inactive items as translucent strands at 30–40% opacity on the ground, and saturate them when active, the way the Houston yellow sits among clear tubes.
6. **Type:** Set nav and labels in tracked uppercase monolinear type at small size, spaced evenly, so the header reads as a row of rods.
7. **Motion:** Tie the colour field to scroll. As the user scrolls, the coloured bars move across the striped grid with a slight lag (0.9× scroll speed) so the shape seems to float in a separate plane.
8. **Motion:** On hover, push nearby bars aside with a damped spring (stiffness about 120, damping about 8) and let them sway back. This is the curtain of tubes parting around a hand.
9. **Interaction:** Use semantic zoom on approach. At overview zoom a dataset reads as one coloured mass. Zooming or opening it splits the mass into its individual strands (rows or items), the way Sphère Lutétia comes apart as you walk toward it.
10. **Texture:** Swap drop shadows for depth through interference. Separate layers with fine stripes that cross at a 2–5° angle instead of using blur or elevation.

## What this artist would reject
- Elevation shadows and frosted-glass blur as fake depth. Real depth here comes from parallax between planes.
- Shapes defined by outlines and borders. Soto's volumes have no edges.
- Autoplay carousels and looping hero animations that move whether or not anyone is there.
- Rainbow palettes and gradient fills. He uses one hue at a time, placed against black and white.
- Heavy display type that fights the field. The image, not the word, carries the weight.
- A lone object centred in empty space.

## Signature prompt seed
Design the screen as a two-plane vibration field. Behind everything, lay a full-bleed ground of 1px black hairlines on off-white at a 4px pitch. In front, use sparse vertical bars that shift a few pixels with the cursor so moiré shimmers. Imply the main element as a Soto virtual volume: an ellipse made only of coloured bars in saturated yellow among translucent grey ones, with no outline. Tracked monolinear uppercase labels act as rods. Motion only responds to the user, with spring-damped sway. Zooming in breaks the mass into individual strands.

## Sources
- https://mfah.org/press/houstons-interactive-immersion-museum-fine-arts-houston-presents-soto-houston
- https://smarthistory.org/jesus-rafael-soto-houston-penetrable
- https://www.citedelarchitecture.fr/sites/default/files/documents/2026-06/cp_soto_une_traversy_e_ciny_tique.pdf
- https://www.centrepompidou.fr/en/ressources/oeuvre/cajzxGK
- https://jesus-soto.com/biography/
- https://www.moma.org/collection/works/91773
- https://www.tate.org.uk/art/artworks/soto-light-trap-t03770
- https://www.lot-art.com/auction-lots-source-click/51976133
- https://unframed.lacma.org/node/1202
