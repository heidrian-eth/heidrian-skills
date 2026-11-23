# Theo van Doesburg — De Stijl

## Essence
Van Doesburg kept Mondrian's vocabulary of flat primaries, black bars and white ground, then rotated it 45° against the architecture it sat on. The result, a "new polarity," is always two systems in friction, never one at rest. Elementarism treats tension, time and the moving viewer as material in their own right.

## Key works examined
- **Geometric alphabet, 1919**: monoline capitals on a 5×5 square grid, stretched or condensed to justify. It teaches type as building blocks.
- **De Stijl magazine (1917 Huszár masthead; 1921 redesign)**: woodcut rectangles spelling the title over a fully justified bold block. In 1921 a horizontal bold sans was overprinted on "NB". It teaches layered, justified, rectangular lockups.
- **Counter-Composition V, 1924**: nine colored rectangles tilted 45° that touch edge to edge with no black lines between them, plus one small grey patch. It teaches adjacency without dividers.
- **Contra-compositie VII, 1924**: a large off-center plane ringed by smaller ones, built on a rhombus. Its black bars are so thick they read as planes. It teaches that line weight can turn a line into a plane.
- **Counter-Composition VI, 1925**: three thick black diagonals laid over an orthogonal background grid, each as wide as the grid's squares. It teaches two grids sharing one module.
- **Café Aubette ciné-dancing, Strasbourg, 1926–28**: colored relief panels tilted 45°, clashing with the orthogonal doors, windows and booths. It teaches that a rotated layer can sit over a functional layer that stays upright.
- **Simultaneous Counter-Composition, 1929–30**: 50 × 50 cm, with orthogonal and diagonal systems superimposed in one square. It teaches simultaneity: two readings at once.

## Space & composition
- **Two grids, one module.** Keep a strict upright column grid for content. Put a second grid rotated 45° behind it, built on the same unit, so a diagonal bar is exactly one cell wide.
- **The diagonal belongs to the field, not to the content.** At the Aubette the doors, seats and windows stayed upright and only the color planes tilted. Text, inputs and buttons never rotate.
- **Planes run off the edge.** Cropped tilted rectangles imply an endless field; bleed them off two viewport edges.
- **Square formats.** Most counter-compositions are square; a 1:1 field turned 45° becomes the hidden rhombus scaffold.
- **Off-center dominance.** One large plane takes about 35–45% of the field and sits off-center. Four to eight smaller planes cluster around it at falling sizes.
- **Bars as planes.** Black dividers are 12–24px, as wide as a gutter, not 1px hairlines.

## Color
The base is primaries plus non-colors, with one or two extras to break Mondrian's purity: a grey patch in Counter-Composition V, and greys and greens at the Aubette. Colors sit edge to edge with no stroke between them.
- `#D62E1F` vermilion red: the dominant tilted plane and the primary action
- `#1D3F9B` ultramarine blue: the secondary plane and links
- `#F2C230` cadmium yellow: small accent and focus state
- `#141414` near-black: bars and type
- `#F4F1EA` warm off-white: ground (the paintings' whites are never pure)
- `#9A9A96` mid grey: the "impure" Elementarist plane for disabled or muted UI
- `#3E6B4E` muted green: a rare extra drawn from the Aubette, used once at most

## Form, line & typography
The letters are capitals made only of right-angle, even-weight strokes on a 5×5 cell grid. Counters are square and there are no curves or diagonals. Width varies so lines justify into rectangles; set display type as solid justified blocks. Body text stays plain and readable. **Fonts:** *Archivo* or *Archivo Black* (Google, has a width axis for justifying blocks), *Space Grotesk* for squarish UI text, and *Silkscreen* or a custom 5×5 grid face for one display word only. (Architype Van Doesburg, The Foundry 1997, is the commercial revival.)

## Rhythm, motion & time
Elementarism admitted the "fourth dimension," time, and Van Doesburg designed the Aubette to be experienced by moving through it. Motion should feel like a plane snapping into its slot, not like floating.
- Background planes move by translating along the 45° axis only, at a different scroll speed from the upright content. The two systems slide past each other.
- Transitions are stepped (`steps(4)`) or a sharp `cubic-bezier(.7,0,.2,1)` at 180–260ms. Never use bounce.
- Shared-element moves take an L-path: x, then y.

## UI translations
1. Render a full-bleed background of 4–8 rectangles rotated 45°, cropped by the viewport, behind an upright 12-column content grid.
2. Size every diagonal bar to exactly one gutter, for example 24px, so both grids share one module.
3. Give 40% of the hero to a single tilted red plane anchored off-center to the upper right. Huddle content in the remaining upright quadrant.
4. Separate adjacent color panels by touching edges with no borders. Use 16px black bars only where a real structural division exists.
5. Set the page title as a justified block that spans its column exactly, in bold sans with variable width or tracking tuned to fill it.
6. Overprint the logo or section label on a large faint glyph or monogram behind it, as the 1921 masthead did.
7. Reserve yellow for one element per screen: the current focus or selection.
8. On scroll, move background planes along a 45° vector at 0.4× content speed (`transform: translate(x, x)`).
9. On hover, have a card's color plane slide in from one corner along its diagonal in 4 steps, without fading.
10. Use square cards (1:1) and square avatars. Rotate only the decorative layer, never the tap target.

## What this artist would reject
- 1px hairlines and drop shadows. Depth comes from overlapping planes.
- Gradients, glassmorphism and soft blurs. Color is a flat, bounded plane.
- Pure symmetry and a centered hero. Balance is reached through tension, not mirroring.
- Rotating text or controls for effect. The functional layer stays orthogonal.
- Floaty spring animations. Motion is direct and stepped.

## Signature prompt seed
Design the screen as two colliding systems. An upright 12-column grid holds all text and controls, and behind it a field of flat rectangles rotated exactly 45° bleeds off two edges. One vermilion plane takes about 40% of the field, off-center, with smaller blue, yellow, grey and black planes touching it edge to edge and no outlines. Dividers are thick black bars, one gutter wide. Headlines are bold justified blocks filling their column. Square cards, no radii, no shadows, no gradients. Background planes slide diagonally at a different scroll speed, and transitions snap in steps.

## Sources
- https://www.moma.org/collection/works/80028
- https://lakenhal.nl/en/collection/s-5794
- https://ideelart.com/magazine/theo-van-doesburg-counter-composition
- https://en.wikipedia.org/wiki/Elementarism
- https://www.archdaily.com/791507/ad-classics-cafe-laubette-strasbourg-theo-van-doesburg
- https://www.dailyartmagazine.com/aubette-1928-a-neoplasticist-gesamtkunstwerk-in-strasbourg/
- https://www.strasbourg.eu/web/musees-en/aubette-1928
- https://en.wikipedia.org/wiki/Architype_Van_Doesburg
- https://medium.com/fgd1-the-archive/100-years-of-de-stijl-e532e0a83160
