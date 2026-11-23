# Josef Hoffmann — Vienna Secession / Wiener Werkstätte

## Essence
Hoffmann made the square a whole design system. He used it as a module for windows, a punched pattern in sheet metal, a checkerboard on floors, and the plan behind a palace. He held everything to one consistent logic, from the building down to the spoon. His volumes look weightless because he drew their edges with a thin contrasting line, as if the building were a piece of cut card bound with gilt tape.

## Key works examined
- **Hohe Warte houses, 1899–1902**: windows split into small square panes. *(visually checked in the retry pass: MAK KI 8951-50 (Villa Bernatzik, b/w photo, 1902) and KI 13746-30 (Henneberg house hall, b/w photo, 1903). Confirmed: casement windows divided into small near-square panes (each leaf ≈2 across × 3–4 down) punched into a blank white wall under a steep tiled roof, behind a fence of evenly spaced vertical bars. The Henneberg hall repeats the square at every scale: a 3 × 3 square ceiling rose, a cubic lantern, stencilled square motifs in a row along the wall, a checker floor. Colour cannot be judged in b/w.)*
- **Lattice vases and baskets, c. 1906**: white-varnished zinc-plated sheet iron with machine-punched square perforations, 14.4 cm tall. The grid works as both surface and structure, and it is cheap to repeat. *(visually checked on related V&A lattice pieces: a square vase (2007BP4647, silvered, 8 holes across each face, on four ball feet), a round basket (2007BP4613) and a tray (2007BP4644), all painted cream (`#CDC8AC` under grey studio light). The square holes dominate and the bars are about ¼–⅓ of the module (a visual estimate). MAK KI 12032/12031 are design drawings on graph paper.)*
- **Purkersdorf Sanatorium, 1904–05**: a flat-roofed cube of smooth white plaster over reinforced concrete. Only the edges carry blue-and-white ceramic tile borders. Moser's white lobby chairs have checkerboard seats. *(visually checked: MAK LI 10872, b/w lantern slide only. A flat-roofed white block, symmetric, with small square-paned windows in even rows, set into a wall that dominates. Tile colour cannot be judged in b/w: blue unverified.)*
- **Sitzmaschine armchair, 1905**: a "sitting machine" with a visible, notched adjustment. *(visually checked: MAK H 3422 and AIC 37273. The back is a grid of square cut-outs (2 columns × 6 rows on the AIC example) in a flat panel, and the side panels carry vertical slots. The only curves are the hooped arm and a row of round knobs. The finish is dark stained wood (`#302121`–`#493737`), not neutral black.)*
- **Palais Stoclet, Brussels, 1905–11**: white Norwegian marble slabs, with gilded bronze mouldings that trace every edge. Windows sit flush with the wall, so the masonry reads as thin sheets. *(visually checked: MAK LI 10874 / 10875, b/w lantern slides. Dark mouldings trace every edge and corner of the white volumes, and the tower is stepped. Gilt, marble and colour cannot be judged in b/w: unverified.)*
- **Cabaret Fledermaus, 1907**: a black-and-white checkerboard floor and custom chairs. *(visually checked: MAK KI 8951-5, b/w photograph. The checker floor is confirmed, with white-framed chairs and tall white piers.)*
- **Rundes Modell cutlery, c. 1906**: the total-design ethic carried down to the hand. *(visually checked: MAK WWF 130-1-1, b/w catalogue photo. Straight round-section handles with small tips; the bowls and blades are the only free shapes.)*
- **Tall-case clock, c. 1906 (AIC 107300), added.** A white case whose front is a single embossed brass panel, about half the front face, edged by thin dark strips. Gilt as one fill panel per object. *(visually checked: AIC scan)*

## Process (derived)
*From observation to process (see SKILL.md §1). This is what transfers; the rest of the file is evidence.*

**Josef Hoffmann.** *Take one square as the unit of everything, leave the planes blank, and let a thin line on every edge and a cluster of small squares at every opening do all the describing.*
Process:
1. Choose one square module and make every dimension a whole multiple of it. Use the same square at two or three scales at least (the cell, the opening, the plane), down to the smallest object in the set.
2. Keep the plane blank and flush: one flat ground on 80–85% of the surface, with nothing projecting, receding or shaded.
3. Trace every edge and corner of every volume with one thin line in the tone furthest from the ground, one weight throughout (about ¼–⅓ of the module). The line, not a fill, states the form.
4. Open the plane only with clusters of module squares (2 across by 3–4 down for a small opening, up to 8 across for a field), holes wider than the bars between them (bar ¼–⅓ of the pitch). Pattern exists only at an opening, a band or a threshold, never on the plane of step 2.
5. Compose the whole symmetrically; one element may rise above the rest (about 1.5× its neighbours).
6. Allow one exception of each kind per object: one round part (a foot, a knob, a hoop) and one filled panel in the single precious tone (up to half of one face), bounded by the edge line of step 3.
Why it works:
- The same unit at every scale groups parts by likeness, so things of different size and purpose read as one family with no shared ornament. One dimension off the module reads as a mistake.
- An outline is the cheapest sign of a volume. With the fill and the shadow removed, mass is read from its edges alone, so a heavy thing looks like a folded sheet. Fill the planes and it becomes a stack of boxes.
- Pattern is rationed, so texture means "something opens here" (salience by oddness), and one round part among squares is found at once. Spread the lattice everywhere and both signals are lost.
Colour relations: near-binary: light ground ≥80%, the opposite tone ≤15% as lines and small squares, both leaning to the same temperature, with no stepped mid-tones between them; one precious accent, either on edges or as the single fill panel; no gradients.
Space and line: one module; one line weight; hole to bar about 3:1 to 2:1; clusters counted in whole cells; flush planes; right angles except the one round part; symmetry with at most one taller element.
Type requirement: even-stroke, squarish letters with no contrast between thick and thin, in capitals spaced to fill a square or double-square box; a monospaced or tabular cut where figures must sit in cells; small plain reading text on the blank plane, never on a lattice or checker.
Motion and interaction: stepped and counted. Progress is cells filling once, one at a time (≥100ms each, a single pass, no blinking); a filled cell also carries a mark or label, so state is not told by tone alone. A control's hit area is a whole multiple of the module that reaches 44px or more, whatever the size of the visible square.
Fails when: the content has no unit size (photographs, long prose, text of unpredictable length that a square must truncate); small lattice cells are made into targets; a fine checker or lattice lies behind text (it vibrates and breaks reading contrast); the interface needs more than one accent to code categories.
Signature (do not carry together): black-and-white checker and punched square lattice · a white cube bound in dark or gilt edge bands · ball feet.

**Transfer test** (an illustration that the process survives new colours and content; never reuse its hues, layout or wording as a design answer):

Hoffmann's procedure → a plant-care app on a dark moss ground (phone, 390 × 845).
1. *Module.* q = 13px, so the screen is 30 × 65 q. Three scales: q (cell detail), 3q (39px icon box), 9q (117px card side). Controls are 4q = 52px.
2. *Plane.* 84% flat moss (L 18). No shadows, no raised cards, no gradients.
3. *Edges.* The screen frame and every card are traced with one 3px line (about ¼ q) in pale bone (L 88): the light-on-dark inversion of the rule.
4. *Openings.* The watering calendar is the only pattern: 7 cells across × 4 down at a 52px pitch (39px hole, 13px bar, 3:1), 28q wide with 1q margins. Each cell is a 52px target.
5. *Symmetry.* Everything is centred on the vertical axis. Today's plant card rises to 13.5q beside neighbours of 9q.
6. *Exceptions.* One round part: the water button, a 52px circle. One filled panel: the lower half of today's card in a warm clay tone, bounded by the bone line.
- *Set.* The home-screen widget, the notification and the icon use the same q and the same edge line.
- *Type.* Plant names in monoline capitals spaced to fill a 9q or 18q box; care notes at 15px on the plain ground.
- *Motion.* Marking a day watered fills its cell in four steps of 120ms and adds a tick; nothing eases.
Result: a dark green, soft-subject utility. No black and white, no checker, no gilt. What survived is one module at every scale, blank planes with drawn edges, and pattern only where something opens.

## Space & composition
- **One module rules every scale.** Derive icon boxes, gutters, cards and section heights as whole multiples of one square unit (1×, 3×, 9× is a prescription, *unmeasured* on the works; the 3 × 3 ceiling rose is the only triple seen). Purkersdorf uses symmetrical projections and recesses on its long sides. Stoclet stacks rectangular blocks asymmetrically but on the same module.
- **Edges, not fills, define volume.** On Stoclet the bronze bands make 3D mass read as flat planes. In UI, a card is a pale field with a 1–2px dark or metallic outline, and no shadow.
- **Flush planes.** Windows sit level with the wall. Keep inputs (1px bottom rule, page background), images and buttons on the container's z-plane.
- **Calm field, concentrated pattern.** Purkersdorf is mostly plain white wall, with pattern only at the borders. Use about 85% white or plain ground and limit grid or checker pattern to frames, rails and thresholds.
- **Bilateral calm, local asymmetry.** Use symmetrical page shells, broken only by one "tower" element that rises above the rest.

## Color
*The hex table below is a reference sample for strict studies and homage only. For design, use the colour relations in "Process (derived)".*

The logic is a near-binary of white and black, plus one precious accent. Gilt usually traces edges, but it can fill one panel per object (the AIC clock). In the objects checked, the "white" is a warm cream paint and the "black" a dark-stained wood with a red-brown cast. Stoclet adds stone tones (honey, dark green) for rooms where people linger; they are unverified, because only b/w photographs were obtained. Hexes are sampled from V&A/AIC studio photos.

| Hex | Role |
|---|---|
| `#CDC8AC` | Ground: chalky plaster or marble white (cream paint on the lattice tray, grey studio light) |
| `#302121` | Line, type, checker squares (Sitzmaschine stained wood, darkest cluster) |
| `#91774E` | Gilt-bronze edge accent (borders and rules; at most one fill panel per object, as on the AIC clock) |
| `#2F5D8C` | Purkersdorf tile blue: secondary edge or active state (unverified: b/w photos only) |
| `#C9A66B` | Honey marble: rare warm panel (e.g. a detail view) (unverified) |
| `#1F3B2D` | Vestibule green-marble: deep "arrival" or modal backdrop (unverified) |

Prescription *(unverified: not measured on the works, most of which were seen only in b/w photos)*: use no greys and make any mid-tone from a 50% black-on-white checker, never behind text.

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
2. Outline cards with `outline: 2px solid #302121; outline-offset: -6px` inside a 1px outer border. The double rule replaces the drop shadow.
3. Run a 1-cell checker band (`conic-gradient` 8×8 black/white) only along the top of the app bar and the bottom of the footer, like the tiled edges of Purkersdorf.
4. Reserve gilt `#91774E` for the border of the single focused or selected element on screen, or for one inset panel in a hero object. Never use it on text.
5. Render progress, loading and empty states as a perforated lattice: a grid of small squares that turn black in order, instead of a spinner or bar.
6. Build avatar, thumbnail and icon frames as exact squares. Use `border-radius: 0`, with no exceptions except one deliberate round part per component or screen (ball feet, a knob, the "spoon").
7. Set section titles in Josefin Sans caps, justified inside a square box with a 1px frame, to make a typographic "plaque".
8. Animate drawers and tabs with `transition-timing-function: steps(4)`, so they click open in four grid units like a mechanism.
9. Give one "tower" element (a primary CTA column or sticky summary) 1.5× the height of its row, so it breaks the flat skyline.
10. Theme everything as one set: the toast, date picker, scrollbar, cursor, favicon and email template all use the same module, edges and palette.
11. Draw lattices with square holes that dominate: bars about ¼–⅓ of the module, so the surface reads as mostly open.

## What this artist would reject
- Soft elevation shadows and frosted blur that make planes float. His planes are flush and bound at the edges.
- Large corner radii and pill buttons everywhere.
- Gradient-filled hero areas. Tone should come from pattern density, not airbrushing.
- Stock components (a default date picker) that break the Gesamtkunstwerk.
- Decoration applied all over a surface rather than concentrated at its borders.
- Arbitrary spacing values like 13px or 22px that break the module.

## Signature prompt seed
Design this screen as a Wiener Werkstätte object. Use one 8px square module for every dimension. The ground is warm chalk-cream `#CDC8AC`, and all structure is drawn in near-black hairline edges, double-ruled like the bronze bands on Palais Stoclet. Put no shadows, no radii and no gradients anywhere. Limit checkerboard and punched-lattice patterns to the borders, as with the tiled edges at Purkersdorf. Use gilt `#91774E` only to outline the single active element, or as one inset panel. Headings are tracked geometric caps justified in square plaques. Motion snaps in stepped grid units like a mechanism. Make every component, down to the scrollbar, part of the same set.

## Sources
- https://mak-media.azureedge.net/xl/5e3717c45c2b1003f2c4697738a8792c.jpg (MAK KI 8951-50, Villa Bernatzik, Hohe Warte; retry pass)
- https://mak-media.azureedge.net/xl/2d401186f3442d508a69fe80801b3ff6.jpg (MAK KI 13746-30, hall of the Henneberg house, Hohe Warte; retry pass)
- https://api.sammlung.mak.at/web-api/search?q=Sanatorium%20Purkersdorf (MAK collection API: Purkersdorf holdings are b/w photos and drawings only; retry pass)
- https://en.wikipedia.org/wiki/Josef_Hoffmann
- https://en.wikipedia.org/wiki/Sanatorium_Purkersdorf
- https://vielfaltdermoderne.de/en/sanatorium-purkersdorf-2/
- https://www.klimt-database.com/en/network-vienna-1900/spheres-of-activity/the-purkersdorf-sanatorium/
- https://www.wikiwand.com/en/articles/Stoclet_Palace
- https://whc.unesco.org/en/list/1298/
- https://www.ebsco.com/research-starters/history/hoffmann-designs-palais-stoclet
- https://onlinecollection.leopoldmuseum.org/en/object/4365-lattice-vase/
- Image sources (visual check): https://framemark.vam.ac.uk/collections/2007BP4647/full/!1600,1600/0/default.jpg (V&A lattice vase), https://framemark.vam.ac.uk/collections/2007BP4613/full/!1600,1600/0/default.jpg (V&A lattice basket), https://framemark.vam.ac.uk/collections/2007BP4644/full/!1600,1600/0/default.jpg (V&A lattice tray)
- https://www.artic.edu/iiif/2/def17169-a869-24ac-581d-652446cf4609/full/1686,/0/default.jpg (AIC 37273, Sitzmaschine), https://mak-media.azureedge.net/xl/5bc3976092ce79eb15267121d23eb916.jpg (MAK H 3422)
- https://www.artic.edu/iiif/2/988c33a9-ff3f-a1f3-69a8-348074f07d0b/full/1686,/0/default.jpg (AIC 107300, tall-case clock)
- https://mak-media.azureedge.net/xl/5658326617a71c0ebc879029420ac32c.jpg (MAK LI 10872, Purkersdorf), https://mak-media.azureedge.net/xl/afcd2ed5d8d808fcd24ee98ff27222cf.jpg and https://mak-media.azureedge.net/xl/b919245b8366dcf244d3187cb4c07bcc.jpg (MAK LI 10874/10875, Stoclet), https://mak-media.azureedge.net/xl/958481a743e1d1fd7c6f44e440c82346.jpg (MAK KI 8951-5, Fledermaus), https://mak-media.azureedge.net/xl/18eef4fbfcb7ae48e294ebd039c76d03.jpg (MAK WWF 130-1-1, Rundes Modell)
