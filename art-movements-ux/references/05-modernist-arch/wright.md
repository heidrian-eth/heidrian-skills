# Frank Lloyd Wright — Modernist / Organic architecture

## Essence
Wright choreographs the body through space: you are squeezed through a low, dim, hidden passage and then let out into a long, horizontal, light-filled room that seems to slide out toward the landscape. Everything from floor joints to window leading to chair backs comes from one geometric unit, so the building reads as a single grown organism, not a set of parts.

## Key works examined
- **Darwin D. Martin House "Tree of Life" window, 1904**: a stylized wheat form in clear, green and golden glass, repeated three times in a 105 × 67 cm panel. Nature reduced to orthogonal line, used as a repeating module.
- **Robie House, Chicago, 1908–10**: Roman brick with raked horizontal joints and flush vertical ones, a steel-cantilevered roof, and a hidden entrance into a low hall. Teaches horizontality and the entry sequence.
- **Fallingwater, 1935–37**: ochre concrete terraces cantilevered from a central stone chimney over the falls. Mass anchored at one core, then thrown outward into space.
- **Jacobs House I, 1937**: a 2 × 4 ft grid scored into a red concrete slab, a 13-inch vertical module that sets the shelves, windows and eaves, and ceilings from 7′3″ in the bedrooms to 11′7″. The unit system and height as a hierarchy.
- **Hanna–Honeycomb House, 1937**: a hexagonal unit with 120° angles and no right angles anywhere in the plan. Changing the module changes the whole feel.
- **Guggenheim Museum, 1943–59**: a quarter-mile continuous ramp around a skylit atrium. Visitors take a lift to the top and walk down, and the bands widen as they rise. A path replaces the set of rooms.

## Space & composition
- **Compression → release.** The entrance is never on the main axis. At Robie it sits at the end of a long side walk and opens into a low hall with a stair turning up. Treat height as something you spend: about 0.6× at thresholds, about 1.6× in the gathering room.
- **Horizontal dominance.** Bands run at roughly 1:6 to 1:10. Horizontal joints are emphasized and vertical ones suppressed, with deep overhangs.
- **Anchor + cantilever.** One heavy off-center core with floating planes reaching out from it in opposite directions.
- **Sliding volumes.** Robie is two offset rectangles, not a centered symmetry.
- **One unit governs everything.** Gutters, cards, icons and line height all come from one module. Break it only for circulation, as when Jacobs widens halls to 3 ft.
- **Path as structure.** At the Guggenheim, scroll is a ramp, not a stack of pages.

## Color
Site earth tones plus one red. Wright's Cherokee Red was a family of faded iron-oxide reds, kept at Fallingwater to sashes and railings.

| Hex | Role |
|---|---|
| `#E9E1CC` | Limestone/plaster ground (main background) |
| `#C7A66B` | Fallingwater ochre (large planes, cards) |
| `#B07E55` | Roman brick tawny (secondary surfaces, borders) |
| `#5E4630` | Stained oak (text, structural lines, battens) |
| `#9C3B26` | Cherokee red (one accent: active state, signature square) |
| `#6F8A4D` | Art-glass green (data highlights, focus) |
| `#C9A23A` | Art-glass gold (tiny glints only, ≤2% of area) |

Warm, low-chroma, tonal. The red is a stamp, never a field.

## Form, line & typography
Line is thin, straight and leaded: orthogonal strokes (or 120° in hexagonal work) with small squares of color set at the intersections. Wright signed his drawings with a red square. Type should feel drawn on a grid: geometric, wide and slightly archaic, with tracked caps for labels. Fonts: **Josefin Sans** (headings and labels), **Alegreya** (Arts-and-Crafts warmth for body text), **Poiret One** (thin-line display only).

## Rhythm, motion & time
Motion is horizontal and slow: elements glide along the x-axis like Robie's roof, with long eases (`cubic-bezier(.2,.7,.1,1)`, 500–800 ms). Section headers start compressed (short and dark) and expand in height and light once scrolled past a threshold. Lists unspool as one descending ramp instead of paginating. Rhythm is a repeated module with one variation per band, like the wheat motif repeated three times.

## UI translations
1. **Layout:** Build on a 2:1 unit (16 × 8 px). Cards, gutters, icons and line-height are multiples of it. Show it as faint hairline joints on the background, like the scored slab.
2. **Compression/release:** Open key flows with a short, dark 56px entry strip, then release into an ochre band ≥60vh. Users pass through the narrow part first.
3. **Off-axis entry:** Put navigation at the left edge or bottom-left, never centered at the top.
4. **Cantilever:** Anchor content to a dark, off-center "hearth" column about 1/5 of the width. Let panels overshoot the container by 10–15% with no visible support and a deep shadow beneath.
5. **Horizontality:** Use 2px oak horizontal rules and no vertical dividers. Band tables by tone.
6. **Color:** Keep 90% of the surface earth tones. Use Cherokee red on exactly one element per screen.
7. **Type:** Labels in Josefin Sans caps, `letter-spacing: .18em`, 11–12px. Body in Alegreya, line-height snapped to the unit.
8. **Art-glass ornament:** Dividers and empty states are SVG leaded-glass patterns: 1px oak lines with green and gold squares at intersections, repeated in threes.
9. **Motion:** Panels slide in 24–40px horizontally. Never scale up from the center, and never bounce.
10. **Ramp navigation:** Galleries and timelines are one descending path with a sticky progress spine. Start at the summary and walk down into the details.
11. **Interaction:** On hover, thicken the card's top border and dim its surroundings, compressing attention onto the chosen item.
12. **Module swap:** For a radical variant, switch to hexagons (120° clip-paths on avatars, chips and tiles) everywhere.

## What this artist would reject
- Centered, symmetric heroes with the CTA dead center.
- Uniform "ceiling height": the same padding and elevation everywhere.
- Cool grays and pure #FFF/#000.
- Decoration unrelated to the grid: stock illustrations, blobs, gradients.
- Grids of identical boxes. He "broke the box."
- Several bright accent colors competing.

## Signature prompt seed
Design this app screen as a Wright Prairie house. Enter through a low, dim, 56px oak-brown strip with navigation tucked bottom-left, then release into a tall limestone-and-ochre band that stretches horizontally. Derive every dimension from a 2:1 rectangular unit shown as faint scored joints. Anchor content to one offset dark "hearth" column and cantilever panels out beyond the container. Use horizontal 2px rules, Josefin Sans tracked caps, and Alegreya body text. Ornament only with leaded-glass SVG lines with green and gold squares in threes. Allow one Cherokee-red mark per screen. Panels glide in sideways, slowly.

## Sources
- https://www.artic.edu/artworks/38836/darwin-d-martin-house-tree-of-life-window
- https://sah-archipedia.org/node/12854
- https://www.britannica.com/place/Fallingwater
- https://en.wikipedia.org/wiki/Herbert_and_Katherine_Jacobs_First_House
- https://en.wikipedia.org/wiki/Hanna%E2%80%93Honeycomb_House
- https://franklloydwright.org/site/hanna-house/
- https://www.dezeen.com/2017/06/09/solomon-r-guggenheim-museum-frank-lloyd-wright-new-york-city/
- https://franklloydwright.org/willey-house-stories-part-11-origins-of-wrights-cherokee-red/
- https://www.housedigest.com/2230036/frank-lloyd-wright-home-design-technique-entryways/
