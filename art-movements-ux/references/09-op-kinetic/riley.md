# Bridget Riley — Op Art

## Essence
Riley builds motion from a repeated unit with one variable changed at a steady rate: the width of a square, the curve of a line, the step of a grey. The surface is flat, still and made without visible touch, yet the eye produces the movement. Her subject is perception, set off by a strict system of tempo.

## Key works examined
- **Movement in Squares, 1961**: a checkerboard whose columns squeeze into thin slivers right of centre. It shows that progressive compression of one axis reads as a fold in space.
- **Fall, 1963** (Tate, 141 × 140 cm, PVA emulsion on hardboard): black waves over white primer at a roughly constant 5–6 mm pitch while the radius tightens. Keep the spacing fixed and vary the curvature.
- **Hesitate, 1964**: circles flatten to ellipses, narrowest about one third from the top. The grey sequence steps 0→24 in twos, speeds up, then slows. Tempo is a designed curve.
- **Cataract 3, 1967** (222 × 223 cm): vermilion and turquoise twisted along curves. Grey at the edges cools the hues and saturation peaks in the centre. Color pairs change wherever lines meet.
- **Late Morning, 1967–68 / Rise I, 1968**: vertical stripe sequences. A narrow stripe changes the color of its neighbours, so you design the adjacencies, not the swatches.
- **Evoë 3, 2003, and Arcadia (wall painting, 2008)**: later curves placed freely, with large planes of soft color locked together. They borrow the "processional rhythms" of Mantegna and Raphael.

## Space & composition
- **One unit, one variable.** In *Fall* only the curvature changes, never the pitch. That is why the motion reads as smooth, not noisy.
- **Off-centre climax.** The crush in *Movement in Squares* falls to the right of centre and the tightest ellipse in *Hesitate* sits a third from the top. Put the peak density at roughly a 1:2 split, never in the middle.
- **Edge-to-edge field, tiny margin.** A thin primer border is the only frame. In UI: full bleed with a 4–8px quiet gutter, not a card floating in padding.
- **Density gradient instead of hierarchy boxes.** Things get closer together as they approach what matters.
- **Square formats.** *Fall* and *Cataract 3* are about 1:1, so all direction comes from the pattern.

## Color
Color arrived in 1967 as relationships: complementary pairs in a regular beat, grey to quiet the edges, and saturation pushed to a central peak ("a sudden flood of bright colour"). Later stripes drop the black and white separators so hues touch directly.

| Hex | Role |
|---|---|
| `#F3F0E8` | Primer white: ground and negative stripe |
| `#151413` | Mars-black: line and positive stripe |
| `#8E8D89` | Mid grey: edge damper, inactive state |
| `#E4472C` | Vermilion: climax accent, used only at the peak |
| `#23ADA8` | Turquoise: vermilion's partner, in alternate bands |
| `#C9B3D6` | Later-curve lilac: large calm plane |
| `#E9C46A` | Later-curve ochre: warm plane next to lilac |


## Form, line & typography
Riley's line is impersonal: compass, T-square and template, painted by assistants "unchecked by any kind of touch." Type should feel as mechanical and be able to *compress progressively*, like her squares.
- **Archivo** (variable width axis 62–125): animate or step `font-stretch` across a line or list so letters narrow toward a focal point.
- **Instrument Sans** or **Inter Tight**: neutral, even-stroke text faces that won't add "touch."
Use one weight. Make rhythm with tracking and width, not bold.

## Rhythm, motion & time
Grey let her tempo be "accelerated … or delayed": *Hesitate* speeds up, then slows. In UI, that is easing written into layout. Stagger on a curve (0, 40, 70, 90, 100, 105ms), not in equal steps. Motion is slow and periodic (8–20s cycles). Interaction shifts a pattern's *phase*, not its objects. The flicker belongs to the eye, so the animation itself stays calm.

## UI translations
1. **Layout:** Build lists as a compression gradient: row height falls geometrically from 64px to 32px toward the selected item, then reopens.
2. **Layout:** Place the hero's densest point at 62–67% across the viewport, never at 50%.
3. **Color:** Ramp saturation: grey (`#8E8D89`) at the edges, full vermilion/turquoise only in one band under 15% of the screen.
4. **Color:** Choose colors as adjacent pairs. Test each swatch beside its real neighbour; a 2px turquoise rule changes a vermilion block.
5. **Type:** Use Archivo with `font-stretch` going from 125% to 70% across a nav row, so the active item is the most compressed one.
6. **Motion:** Use curved stagger timing (fast then slow, or slow-fast-slow) for entrances. Never use linear 50ms steps.
7. **Motion:** Loading states: a slow wave through 1px vertical lines (≥2s per cycle), not a spinner.
8. **Interaction:** Scroll or pointer shifts the phase of a `repeating-linear-gradient` field, so the page seems to bend as you move.
9. **Texture:** Draw separators as SVG sine waves with constant pitch and amplitude rising toward content.
10. **Accessibility:** High-contrast stripes near 3 cycles/degree with a 50% duty cycle are the peak pattern-glare zone. On a laptop at about 50cm, keep black/white stripes about 3–8px wide off large areas. Use unequal widths, lower contrast or color instead.
11. **Accessibility:** Put pattern motion behind `prefers-reduced-motion`. Never exceed 3 light/dark changes per second over 25% of a 10° field (WCAG 2.3.1). Offer a "calm surface" toggle.
12. **Accessibility:** Never put body text on a vibrating field. Give it a flat primer-white panel.

## What this artist would reject
- Decorative gradients with no system: her every change is stepped and measured.
- Drop shadows and glassmorphism: her space comes from pattern, not faked light.
- Handmade quirk (brush textures, wobbly illustration) posing as personality.
- Even, centred spacing with no build-up or climax.
- Saturated accents scattered everywhere instead of peaking once.
- Moving objects around when surface rhythm could do the work.

## Signature prompt seed
Design the screen as one full-bleed square field with a single repeated unit (stripe, square or wave) where only one property changes at a time. Compress the spacing in a geometric progression toward a focal point about two-thirds across. Neutral grey edges on primer white (#F3F0E8); complementary vermilion and turquoise touch only in the focal band. Set type in Archivo, narrowing its width toward the active item. Use curved stagger timing and slow phase-shifting waves. Keep text panels flat. Avoid high-contrast stripes at about 3 cycles/degree, and respect reduced motion.

## Sources
- https://www.tate.org.uk/research/tate-papers/39/a-technical-study-into-bridget-rileys-paintings-fall-and-hesitate
- https://artscouncilcollection.org.uk/explore/blog/conservators-view-movement-squares-bridget-riley
- https://www.artchive.com/artwork/movement-in-squares-bridget-riley-1961/
- https://bridget-riley.publications.britishart.yale.edu/catalogue/32/
- https://artuk.org/discover/stories/bridget-riley-top-of-the-ops
- https://www.tate.org.uk/art/artworks/riley-late-morning-t01032
- https://www.nationalgallery.org.uk/about-us/press-and-media/press-releases-archive/bridget-riley-paintings-and-related-work
- https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2015.01651/full
- https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html
