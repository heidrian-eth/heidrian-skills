# Josef Hoffmann — Vienna Secession / Wiener Werkstätte

## Essence
Hoffmann made the square a whole design system. He used it as a module for windows, a punched pattern in sheet metal, a checkerboard on floors, and the plan behind a palace. He held everything to one consistent logic, from the building down to the spoon. His volumes look weightless because he drew their edges with a thin contrasting line, as if the building were a piece of cut card bound with gilt tape.

## Key works examined
- **Hohe Warte houses, 1899–1902**: windows split into small square panes.
- **Lattice vases and baskets, c. 1906**: white-varnished zinc-plated sheet iron with machine-punched square perforations, 14.4 cm tall. The grid works as both surface and structure, and it is cheap to repeat.
- **Purkersdorf Sanatorium, 1904–05**: a flat-roofed cube of smooth white plaster over reinforced concrete. Only the edges carry blue-and-white ceramic tile borders. Moser's white lobby chairs have checkerboard seats.
- **Sitzmaschine armchair, 1905**: a "sitting machine" with a visible, notched adjustment.
- **Palais Stoclet, Brussels, 1905–11**: white Norwegian marble slabs, with gilded bronze mouldings that trace every edge. Windows sit flush with the wall, so the masonry reads as thin sheets.
- **Cabaret Fledermaus, 1907**: a black-and-white checkerboard floor and custom chairs.
- **Rundes Modell cutlery, c. 1906**: the total-design ethic carried down to the hand.

## Space & composition
- **One module rules every scale.** Derive icon boxes, gutters, cards and section heights as whole multiples (1×, 3×, 9×) of one square unit. Purkersdorf uses symmetrical projections and recesses on its long sides. Stoclet stacks rectangular blocks asymmetrically but on the same module.
- **Edges, not fills, define volume.** On Stoclet the bronze bands make 3D mass read as flat planes. In UI, a card is a pale field with a 1–2px dark or metallic outline, and no shadow.
- **Flush planes.** Windows sit level with the wall. Keep inputs (1px bottom rule, page background), images and buttons on the container's z-plane.
- **Calm field, concentrated pattern.** Purkersdorf is mostly plain white wall, with pattern only at the borders. Use about 85% white or plain ground and limit grid or checker pattern to frames, rails and thresholds.
- **Bilateral calm, local asymmetry.** Use symmetrical page shells, broken only by one "tower" element that rises above the rest.

## Color
The logic is a near-binary of white and black, plus one precious accent used only on edges. Stoclet adds stone tones (honey, dark green) for rooms where people linger.

| Hex | Role |
|---|---|
| `#F7F5EF` | Ground: chalky plaster or marble white |
| `#111111` | Line, type, checker squares |
| `#9C7A3C` | Gilt-bronze edge accent (borders, rules only, never fills) |
| `#2F5D8C` | Purkersdorf tile blue: secondary edge or active state |
| `#C9A66B` | Honey marble: rare warm panel (e.g. a detail view) |
| `#1F3B2D` | Vestibule green-marble: deep "arrival" or modal backdrop |

Use no greys. Make any mid-tone from a 50% black-on-white checker.

## Form, line & typography
The shape language is the square, the cube and the thin parallel rule, with curves reserved for the occasional object (Rundes Modell). Type should be monoline, geometric and squarish, with even strokes like the bronze bands.
- **Josefin Sans**: geometric, with 1920s proportions.
- **Poiret One**: hairline Viennese deco caps for headings, to be used sparingly.
- **Space Mono** or **IBM Plex Mono**: when you want the type itself to sit on the square grid.
Set headings in uppercase, tracked +8–12%, and justify them inside a square or double-square box. Body text stays small and quiet.

## Rhythm, motion & time
Repetition comes before variation. Motion should feel like the Sitzmaschine's notched mechanism: it snaps in discrete steps, one grid unit at a time (`steps()` easing or 120ms linear moves of exactly 8px). Reveal elements as a lattice, with cells filling in a raster sequence (20ms stagger, row-major). Hover lights up an edge (the border shifts from black to gilt), not the fill. There is no spring bounce and no blur.

## UI translations
1. Define `--q: 8px` and enforce `grid-template-columns: repeat(auto-fill, calc(var(--q)*12))`. Every dimension is a multiple of `--q`. Audit for strays.
2. Outline cards with `outline: 2px solid #111; outline-offset: -6px` inside a 1px outer border. The double rule replaces the drop shadow.
3. Run a 1-cell checker band (`conic-gradient` 8×8 black/white) only along the top of the app bar and the bottom of the footer, like the tiled edges of Purkersdorf.
4. Reserve gilt `#9C7A3C` for the border of the single focused or selected element on screen. Never use it as a fill or on text.
5. Render progress, loading and empty states as a perforated lattice: a grid of small squares that turn black in order, instead of a spinner or bar.
6. Build avatar, thumbnail and icon frames as exact squares. Use `border-radius: 0`, with no exceptions except one deliberate round object per screen (the "spoon").
7. Set section titles in Josefin Sans caps, justified inside a square box with a 1px frame, to make a typographic "plaque".
8. Animate drawers and tabs with `transition-timing-function: steps(4)`, so they click open in four grid units like a mechanism.
9. Give one "tower" element (a primary CTA column or sticky summary) 1.5× the height of its row, so it breaks the flat skyline.
10. Theme everything as one set: the toast, date picker, scrollbar, cursor, favicon and email template all use the same module, edges and palette.

## What this artist would reject
- Soft elevation shadows and frosted blur that make planes float. His planes are flush and bound at the edges.
- Large corner radii and pill buttons everywhere.
- Gradient-filled hero areas. Tone should come from pattern density, not airbrushing.
- Stock components (a default date picker) that break the Gesamtkunstwerk.
- Decoration applied all over a surface rather than concentrated at its borders.
- Arbitrary spacing values like 13px or 22px that break the module.

## Signature prompt seed
Design this screen as a Wiener Werkstätte object. Use one 8px square module for every dimension. The ground is chalk white `#F7F5EF`, and all structure is drawn in black hairline edges, double-ruled like the bronze bands on Palais Stoclet. Put no shadows, no radii and no gradients anywhere. Limit checkerboard and punched-lattice patterns to the borders, as with the tiled edges at Purkersdorf. Use gilt only to outline the single active element. Headings are tracked geometric caps justified in square plaques. Motion snaps in stepped grid units like a mechanism. Make every component, down to the scrollbar, part of the same set.

## Sources
- https://en.wikipedia.org/wiki/Josef_Hoffmann
- https://en.wikipedia.org/wiki/Sanatorium_Purkersdorf
- https://vielfaltdermoderne.de/en/sanatorium-purkersdorf-2/
- https://www.klimt-database.com/en/network-vienna-1900/spheres-of-activity/the-purkersdorf-sanatorium/
- https://www.wikiwand.com/en/articles/Stoclet_Palace
- https://whc.unesco.org/en/list/1298/
- https://www.ebsco.com/research-starters/history/hoffmann-designs-palais-stoclet
- https://onlinecollection.leopoldmuseum.org/en/object/4365-lattice-vase/
