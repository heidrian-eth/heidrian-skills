# Frei Otto — Growth & Form

## Essence
Otto did not design shapes. He set boundary conditions (high points, low points, edges, a mesh) and let a physical process find the form: a soap film stretched to its least area, or a hanging chain net settled under gravity and was then turned upside down. The result is everywhere in equilibrium, double-curved, and as light as the load allows. His design act is choosing the supports; the surface between them is computed by nature.

## Key works examined
- **German Pavilion, Expo 67, Montreal (1967, with Rolf Gutbrod).** A cable-net tent over masts of different heights, with an "eye" loop at each peak. It teaches unequal high points joined by one continuous net. *(visually checked: secondary source (pritzkerprize.com, photo © Frei Otto))*
- **Roofs of the Olympic Park, Munich (1968–72, with Behnisch & Partner).** A chain of saddle-shaped acrylic cable-net bays over the stadium, hall and pool. It teaches a field of alternating high and low points. *(visually checked: secondary source (pritzkerprize.com, photo © Christine Kanstinger))*
- **Multihalle, Mannheim (1970–75, with Carlfried Mutschler and Ove Arup).** A timber gridshell of 50 × 50 mm hemlock laths on a 500 mm two-way grid, its form taken from an inverted hanging-chain model. It teaches a constant mesh that bends to any surface. *(visually checked: secondary source (pritzkerprize.com, photo © Frei Otto))*
- **Institute for Lightweight Structures (IL), Stuttgart-Vaihingen (1967).** A cable-net tent around one mast, with a glazed eye at the high point. It teaches the prototype as a building. *(visually checked: secondary source (pritzkerprize.com, photo © Atelier Frei Otto Warmbronn))*
- **Soap-film form-finding models (1960s onward).** Films spanning thin wire masts and edge threads. It teaches that every free edge becomes a concave arc and every field a saddle. *(visually checked: secondary source (metalocus.es, IL photo, "soap film model as a minimal surface within a defined boundary geometry"))*
- **IL 18 (1987), minimal surfaces between three rigid rings.** Photograms of films spanning rings of different sizes (IL-Bach/Klenk). It teaches that the boundary alone decides the surface. *(visually checked: secondary source (metalocus.es, reproduction of IL 18 p.122))*
- **Multihalle hanging-chain model.** *(not obtained: no open image found; mechanism confirmed in text sources)*

## Process and relations (observed)
- **Supports first, surface second** (soap-film model, Expo 67, IL). Each model is a few rigid points (mast tips, anchors, rings) plus free edges. The film is never drawn: it is what spans them. At Expo 67 the three visible peaks differ visibly in height, yet one net joins them without seams.
- **Every free edge sags inward** (soap-film model). Between two supports the film's edge is a concave arc, never a straight line, so the outline of every bay is scalloped. In the photo every edge between mast tip and ground anchor curves toward the film's interior.
- **Alternation of high and low** (Munich aerial). Peaks (mast points) and pulled-down low points (funnels, visible as dark dimples) alternate across the roof field, so every bay is a saddle curving up one way and down the other. No part is flat, and no part is far from a support.
- **Constant mesh, variable curvature** (Multihalle, Munich). The grid cell is one size everywhere (500 mm laths; equal square panels in Munich). Where the surface curves strongly the square cells shear into rhombi instead of changing size: in the Multihalle photo, near-square cells at the crown elongate toward the springing.
- **Opening at the peak** (Expo 67, IL Stuttgart). Each high point carries a loop or glazed eye, the place where the net is gathered and the light comes in.
- **No frame behind the skin** (all works): the surface is the structure. Masts are few and slender.
- **The generative rule:** fix a small set of anchor points with heights, and the edges between them; let a surface relax to minimal area (or an inverted hanging net settle under uniform load); every free edge becomes a concave arc and every bay a saddle; tile the result with a constant-size mesh whose cells shear rather than resize. This works in any medium: layout boxes, charts, motion curves.

## Process (derived)
*From observation to process (see SKILL.md §1). This is what transfers; the rest of the file is evidence.*

**Frei Otto.** *Place only the supports and say which edges are free; everything between them is found by relaxing one continuous surface to equilibrium, so every change is shared by the whole field.*
Process:
1. Fix 3–7 anchors: the elements that may not move. Give each a height (its importance); no two equal, the most important highest.
2. Declare each boundary between neighbouring anchors pinned (to the frame or to a rigid edge) or free. Nothing else is positioned by hand, now or later.
3. Relax. Treat all remaining items as nodes of one net with a single rest length `m`, and solve for equilibrium (springs or force density, iterated until the largest move is under 0.5px). The solved positions are the layout.
4. Every free edge sags toward the interior as a concave arc, sag ≈ span ÷ 10 (1/12–1/8). Never straight, never convex. More load on an edge means more sag.
5. Alternate high and low: between two raised anchors put one pulled-down point, so each bay curves up one way and down the other. No bay is flat and no node lies more than one bay from a support.
6. Keep one mesh size `m` across the whole field. Where the surface curves the cells shear into rhombi; they never scale. Show the mesh as hairlines.
7. Cut one opening only, at the highest anchor. It is the lightest point of the field and holds the one live view.
Why it works:
- A boundary that curves inward between two points is what a pulled sheet does, so the eye reads the corners as holding the region. Anchors gain weight without gaining size, and regions need no border. A straight edge reads as a box that was drawn; a convex one as a blob that was inflated.
- A mesh of constant size is a scale reference: shear reads as slope, as any regular texture does on a curved surface. If the cells resize instead, size reads as rank and the slope is lost.
- When a change is spread over every node, each moves a little and keeps its neighbours, so the viewer's map of the screen survives. One box jumping a long way destroys the map and draws the eye to the wrong thing.
Colour relations: the continuous surface is ONE value of one neutral or one material hue, unchanged across bays (near-neutrals ≈90% of the view); supports are darker and thinner than the field; the opening is the lightest point; all chroma (≤10%) belongs to content seen through or under the surface, never to the structure.
Space and line: 3–7 supports and large spans; bays run into each other with no seams or gutters, told apart by rise and fall (a value gradient); only two kinds of line, straight thin supports and tensioned curves; mesh hairlines at 6–10% contrast.
Type requirement: one light, even weight with open counters and a wide rhythm; reading text sits only where the field is calm (near anchors, low curvature), on plain surface and never across the mesh at more than 10% contrast or along a steep bay.
Motion and interaction: relaxation. Any change re-solves the net and every node travels to the new equilibrium, critically damped, 300–500ms, no overshoot; moving one anchor shifts neighbours by an amount that decays with distance; a pressed anchor rises and the surface follows. Supports stay thin with ≥44px invisible hit areas. Reduced motion: cut to the new state with a short cross-fade.
Fails when: content must align in rows and columns to be compared (tables, forms, code); there are dozens of equal anchors (no spans left, the field becomes a quilt); long text has to follow a curved boundary; the layout must be identical for every user and data set (the solver gives a different answer per content).
Signature (do not carry together): peaked tent roofs on masts · translucent panels on a cable net · soap-film models on wire frames.

**Transfer test** (an illustration that the process survives new colours and content; never reuse its hues, layout or wording as a design answer):

Weekly meal planner, phone 390 × 844, saturated tomato and leaf-green on cream, domestic and small-scale (the works are neutral, vast and engineered).
1. *Anchors (5).* Today's dinner (height 1.0), the shopping-list action (0.7), the week's cost (0.5), and the top-left and bottom-right screen corners (0, pinned). Nothing else is placed by hand.
2. *Edges.* Top and bottom are pinned to the frame. The left and right boundaries of the meal field are free.
3. *Relax.* Twenty other meals (3 a day minus today's dinner) are nodes of one net, `m` = 56px. The solver settles in about 40 iterations. Meals near today sit higher and so render larger (64px) than meals on Sunday (48px); every node remains a ≥44px target.
4. *Sag.* The free left edge between the top corner and the shopping action spans 520px and sags inward 52px. It carries 12 list items; at 24 items it sags to 65px (span ÷ 8).
5. *High and low.* Between "today" and "shopping list" the field is pulled down at Wednesday's leftovers, a darker and smaller dimple, so the week reads as two rises and a dip.
6. *Mesh.* 56px cells as cream hairlines at 8% contrast. Around today's peak they shear to roughly 70° rhombi; none changes size.
7. *Opening.* Only today's dinner has a window: a 120px oval, the lightest point on screen, showing the live cook timer and a photo. The colours stay in the content (food photos, the green "bought" ticks with their check glyph), about 9% of the area; the surface itself is one cream value.
- *Motion.* Dragging Thursday's lunch to Saturday re-solves the net: every node moves 2–14px over 400ms, critically damped. Reduced motion cuts to the solved state.
- *Type.* One light weight; meal names sit on the calm surface beside each node, never across the hairlines near the peak.

Result: a warm, small, domestic planner with no tent, mast or membrane in it. What survived is supports before surface, the inward sag, the constant shearing mesh and the shared reflow.

## Space & composition
- **Few supports, large spans.** A screen is a handful of anchored points (3–7) holding a continuous field, not many boxes.
- **Anchors at unequal heights.** Peaks differ in height; the most important anchor is the highest and carries the opening.
- **Scalloped outlines.** Every outer edge between two anchors curves inward (≈1/10 of its span is a hint from typical cable-edge sag, *unmeasured* here).
- **Field, not cells.** Bays flow into each other without seams or gutters; regions are told apart by where the surface rises and falls.
- **Visible mesh.** The construction grid is shown, constant in size, distorted only by the surface's curvature.

## Color
*The hex table below is a reference sample for strict studies and homage only. For design, use the colour relations in "Process (derived)".*

Colour is the material's own and light does the rest. In the Munich aerial the roof field is grey translucent acrylic over a grey and green landscape: four near-neutral values (L≈13–78, C≤6) cover ≈92% of the frame, and the only chroma is the vegetation (≈8%, C≈18). Inside the IL and the Multihalle, warm wood or translucent white membrane spans as a single surface; colour does not change across a bay. Translate as: the continuous surface is one value of one neutral or one material hue; the anchors are darker and thinner than the field; the openings at the peaks are the lightest points; any chroma belongs to the content seen through or under the surface, not to the structure.

**Reference sample (studies and homage only)**

| Hex | Role |
|---|---|
| `#778381` | translucent roof field (Munich, ~28%) |
| `#BEBCB8` | lit membrane / opening |
| `#1C2629` | shadow under the net |
| `#495438` | life under the roof (vegetation, ~8%) |

## Form, line & typography
Every line is a catenary or a geodesic: curves under tension, concave between supports, never arbitrary béziers. Masts are straight and thin. The mesh is a regular net of hairlines. Type requirement: a light, even, open face with no ornament, in which the letter skeleton reads like a net (a single weight, generous counters, a wide rhythm), and text set in the calm parts of the field, never across steep curvature. For example, a geometric or technical sans such as Inter Light or Barlow.

## Rhythm, motion & time
Motion is relaxation to equilibrium. When content changes, the layout springs to its new minimal configuration with damping and no overshoot (a critically damped spring, about 300–500 ms). When one anchor moves, the whole field adjusts a little rather than one box jumping a lot. Hover lifts an anchor slightly and the surface follows. Reduced motion: jump to the new equilibrium with a short cross-fade.

## UI translations
1. **Anchor, then relax.** Place 3–7 anchor elements (title, primary action, key figures) first, then compute the remaining layout as a relaxed spring system (for example force-directed with edge springs), not by hand.
2. **Scalloped containers.** Draw region boundaries between anchors as concave arcs (sag ≈span/10 is a starting hint only, *unmeasured* on the works), so containers read as tensioned between their corners.
3. **High–low alternation for sections.** Give sections alternating raised (lighter, larger) and lowered (darker, smaller) states along the scroll, so the page reads as a series of saddles rather than a stack of equal bands.
4. **Highest anchor carries the opening.** The most important element is the highest point and holds the only "window" (a live preview, a video, a map); no other element gets one.
5. **Constant-mesh grid.** Use one cell size everywhere. Where a layout must curve (a radial chart, a wrapped carousel) shear the cells rather than scaling them.
6. **Show the net.** Draw the construction grid as hairlines at 6–10% contrast in empty states and loading, so the structure is visible before content arrives. Never place reading text over a high-contrast mesh.
7. **One material per surface.** Each continuous region is one value; colour belongs only to the content seen through it.
8. **Equilibrium motion.** Use critically damped springs (no overshoot, 300–500 ms) for every reflow; when one item resizes, distribute the change to all neighbours.
9. **Load paths visible.** Connectors between dependent items are catenaries that sag under the "weight" (count) of what they carry: more items, more sag.
10. **Thin supports.** Controls that hold up a region (handles, dividers) are thin and few; targets stay ≥44 px through invisible hit areas.

## What this artist would reject
- Rectangles drawn first and filled afterwards.
- Heavy frames and borders behind a decorative skin.
- Flat regions with no rise or fall.
- Hand-placed curves that no force would produce.
- Linear or bouncy easing that ignores equilibrium.

## Signature prompt seed
Fix a few anchor points at different heights, the highest holding the screen's only window, and let everything between them be one continuous field relaxed to equilibrium. Every edge between two anchors sags inward as a tensioned arc. Sections alternate raised and lowered like saddles. A constant-size hairline mesh shows the structure and shears where the field bends. Each surface is one material value; colour belongs only to the content beneath. Every change springs to a new balance with damped motion and no overshoot.

## Sources
- The Pritzker Architecture Prize, Frei Otto 2015 laureate page and works gallery: https://www.pritzkerprize.com/laureates/2015
- Metalocus, "Frei Otto, video modeling soap films" (soap-film model photos; IL 18 page): https://www.metalocus.es/en/news/frei-otto-video-modeling-soap-films
- ArchDaily, video of Frei Otto experimenting with soap bubbles (from Juan María Songel's interview): https://www.archdaily.com/609541/video-frei-otto-experimenting-with-soap-bubbles
- proHolz Austria, Multihalle Mannheim (hanging models, 50 × 50 mm hemlock, double-layer grid): https://www.proholz.at/en/holzbauten/architektur/multihalle-mannheim
- Mannheim Multihalle gridshell case study (500 mm grid; chain lines representing every third mesh line; stereophotogrammetry): https://www.fastepp.com/wp-content/uploads/Mannheim-Multihalle-Gridshell.pdf
- Boller & D'Acunto, "Modelling the form: Heinz Isler, Frei Otto and their approaches to form-finding": https://researchgate.net/publication/342003907
