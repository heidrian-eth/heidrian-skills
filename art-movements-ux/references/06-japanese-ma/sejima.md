# Kazuyo Sejima / SANAA — Japanese contemporary architecture (Ma, lightness)

## Essence
Sejima builds a field, not a hierarchy. Rooms of equal standing float inside one thin, continuous outline. Structure is pared down until it nearly disappears, and glass, white and mirror let the surroundings and the people inside become the content. Nothing is the "front" and nothing is the "hero". Ma here is the gap between equal things, and that gap is used for moving through and seeing across.

## Key works examined
- **21st Century Museum of Contemporary Art, Kanazawa (2004)**: a glass circle 112.5 m across with several entrances. Box-shaped galleries 4–12 m tall are scattered inside, and corridors double as gallery space. Lesson: a container with no front, and content that is placed rather than ranked.
- **Glass Pavilion, Toledo Museum of Art (2006)**: a field of curved glass rooms inside a double-glazed skin, with an air cavity between. Few corners, no mullions. Lesson: borders shown as layered transparency, not as lines.
- **Serpentine Pavilion, London (2009)**: a 26 mm roof of birch panels clad on both sides in mirrored aluminium, set on 50 mm columns in a random mesh. Lesson: the thinnest possible plane, whose surface is a reflection of its context.
- **Rolex Learning Center, EPFL Lausanne (2010)**: one undulating floor of about 20,000 m² with no interior walls, pierced by roughly a dozen patios. Slopes separate uses. Lesson: zoning by topography, not by partitions.
- **New Museum, New York (2007)**: offset stacked boxes. Lesson: misalignment as the only emphasis.

## Space & composition
- **Equivalence of spaces.** The Pritzker jury praised a non-hierarchical "equivalence of spaces". Kanazawa's galleries differ in size and light but have equal status. In UI, cards differ in proportion (1:1, 2:3, 3:1), not in visual weight.
- **Round or soft outer boundary, orthogonal inside.** A loose, rounded container (large radius, or an ellipse that is almost a circle) holds crisp rectangles. Use 28–40 px radius on the outer frame and 0–2 px on inner tiles.
- **Scatter with even gaps.** The boxes are not on a strict grid, but the space between them stays roughly even. Use a masonry or offset layout with a fixed gutter (24–32 px), and nudge items off-axis by 8–16 px.
- **Gaps as circulation.** Kanazawa's corridors are galleries too, so gutters carry captions and metadata.
- **One continuous floor.** Rolex splits programs with slopes. Separate sections with tonal steps and vertical offsets, never dividers.

## Color
The palette is material: white plaster, glass, mirror aluminium, grey carpet. Real colour is reflected: trees, sky, people. Use near-whites 2–4% L apart.

| Hex | Role |
|---|---|
| `#FBFBFA` | Field / ceiling white (base background) |
| `#F1F2F1` | Room plane (cards, 1 step down) |
| `#E3E6E5` | Glass edge: hairline borders, translucent overlays at 60% |
| `#B9BEBF` | Mirror aluminium (selected states, reflective gradients) |
| `#8A8D8C` | Carpet grey (secondary text, the "floor") |
| `#2B2D2E` | Thin black steel (primary text, 1 px column lines) |
| `#9FB8A6` | Reflected park green (the only accent; ≤3% of pixels) |

## Form, line & typography
The line language is very thin and very even: 50 mm columns under a vast roof, and slabs that read as drawings. Use a light grotesk with no display weights. Headings stay barely 1.25× body, in sentence case, and labels get +0.04em tracking.
- **Inter** (300/400) for UI text.
- **Zen Kaku Gothic New** (300) for labels and bilingual text.
- **IBM Plex Mono** (300) for tiny captions, like dimension notes on a plan.
Use 1 px rules only, `#2B2D2E` at 40%, and 1.25 px icon strokes.

## Rhythm, motion & time
Motion should feel like walking a gentle slope, or light shifting on mirror. Nothing snaps or bounces.
- Transitions run 400–700 ms with `cubic-bezier(0.25, 0.1, 0.25, 1)`: opacity plus at most 12 px of travel.
- Panels arrive translucent (`backdrop-filter: blur(12px)`, 70% white) before they turn opaque.
- A slow specular gradient on selected surfaces follows the pointer, the way the Serpentine canopy takes on the weather.

## UI translations
1. **Layout:** Put the main view in one large rounded container. Inside it, float 6–12 rectangles of different proportions at equal visual weight, with no hero card.
2. **Layout:** Give the screen several equal entry points. Don't use a single primary CTA; offer 3–4 calm, peer-level actions placed around the field.
3. **Layout:** Offset the items in each row by 8–16 px on the y-axis so the grid reads as "placed", not machined.
4. **Color:** Use only value steps of near-white. Separate surfaces with a 2–3% lightness difference plus a 1 px `#E3E6E5` hairline, never with shadows.
5. **Color:** Let any colour on screen come from user content (photos, avatars) shown through translucent panels. Chrome stays colourless.
6. **Type:** Cap the heading scale at 1.25× body in weight 300–400. Mark hierarchy with position and spacing only.
7. **Structure:** Make every structural element as thin as it can be: 1 px borders, 2 px progress bars, 0.5 px separators on retina. Toolbars float with no visible background slab.
8. **Motion:** Animate state changes as opacity and blur dissolves (500 ms) rather than slides or scale pops.
9. **Interaction:** On hover, raise transparency instead of elevation. The hovered card turns 85% translucent and you see faintly through it to the layer below.
10. **Interaction:** Replace tabs with a continuous canvas. Moving between sections is a smooth pan across one field, like walking the Rolex floor, and the zoom level hints at the "slope".
11. **Texture:** Add a subtle reflective gradient (`#FBFBFA` to `#E3E6E5` at 160°) to one surface only, the "canopy", so it mirrors scroll position.

## What this artist would reject
- A hero banner with one huge headline and one big button. That is a front door, and her buildings have none.
- Drop-shadow elevation stacks (Material z-levels), which add hierarchy and mass instead of transparency.
- Heavy dividers, thick nav bars and tab strips that act as walls between programs.
- Saturated brand-colour chrome; colour should be borrowed from context.
- Bold display type at 3–5× body size.

## Signature prompt seed
Design this screen as a SANAA plan. Use one softly rounded, near-white field (#FBFBFA) holding a scatter of orthogonal rooms of different proportions but equal weight, separated by even 28 px gaps that carry quiet captions. There is no hero, no front and no primary button; offer several peer entry points. Make all structure as thin as possible: 1 px hairlines, light Inter at 300, and headings barely larger than body. Separate surfaces by 2% value steps and translucency, never shadows. Colour comes only from content seen through glass-like panels. Motion is slow opacity and blur, like light shifting on mirror.

## Sources
- https://en.wikipedia.org/wiki/21st_Century_Museum_of_Contemporary_Art,_Kanazawa
- https://epfl.ch/campus/visitors/buildings/rolex-learning-center/building
- https://architecturalrecord.com/articles/8237-rolex-learning-center-by-sanaa
- https://www.serpentinegalleries.org/whats-on/serpentine-gallery-pavilion-2009-kazuyo-sejima-ryue-nishizawa-sanaa-0/
- https://beatricegalilee.com/case-study/sanaa-serpentine
- https://www.e-architect.com/awards/pritzker-prize-citation-2010
- https://archeyes.com/toledo-museum-glass-pavilion-by-sanaa-in-toledo-ohio/
- https://www.pmq.org.hk/designfeature/architecture-like-a-park/
