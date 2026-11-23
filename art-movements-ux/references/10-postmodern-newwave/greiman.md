# April Greiman — New Wave / early digital design

## Essence
Greiman treats the screen as a deep space and not a flat sheet. Type, video stills, bitmaps and color planes float at different depths, overlap, and cast shadows. She leaves each tool's artifact visible on purpose (pixel, scan line, halftone dot, offset copy), and she broke open her Basel training using the early Macintosh as a "co-creator." What results is a hybrid surface where low-res and high-res, typeset and captured, all sit in one frame.

## Key works examined
- **CalArts poster (with Jayme Odgers), 1978.** Photography, diagonal type and drop-shadowed planes in one perspective space. Teaches that the page has depth. *(visually checked: Cooper Hewitt 18617589. A 3.8:1 panoramic strip, one photographic atrium in perspective with objects floating in it. The ground is grey-white architecture; colour arrives only as small flat bars (red, yellow, black, blue) at the edges.)*
- **Douglas W. Schmidt poster, 1980 (dated 1980 by Cooper Hewitt).** Offset litho plus screenprint, with fruit and buildings. Teaches that a flat spot colour can be the structure, not decoration. *(visually checked: Cooper Hewitt 18617835 and 18637165. A vermilion base plane #DA5939 (≈9% of the sheet) rises at ≈9° under tilted postcards, a halftone field, acid-green triangles, holographic foil and airbrushed splatter, all inside a white margin. Whether the ink is fluorescent cannot be judged from the scan.)*
- **Your Turn, My Turn, 1983.** Brown type with a pale-cyan copy offset down-left by ≈1% of the sheet width, so every word reads as doubled (not red and blue, as written before). Teaches that misregistration can be a deliberate depth cue. *(visually checked: Cooper Hewitt 18650849. Black wedges at the top and bottom cut in at ≈21°, coarse halftone dots fill the planes, and an acid-yellow block #ECF783 holds the credits.)*
- **Design Quarterly #133, "Does It Make Sense?", 1986.** The issue's usual 32 pages became one double-sided fold-out of about 25.5 x 76.5 in. The front is a pixelated, life-size nude double self-portrait. It was made with MacPaint (sketching), MacVision (video digitizing) and MacDraw (layering and stretching), tiled out as letter-size LaserWriter sheets. Teaches that pixels can be a material and that big scale can sit next to tiny data. *(visually checked: aprilgreiman.com front and back. The front prints in one colour, dithered violet-black #282342 on cream #FDF6E5, at 3.04:1, with a typewriter caption line along the bottom. The back is the colour side: deep violet-black #241B32 video fields (30%), process yellow #F8DA24 (19%) and a halftone yellow-orange glow.)*
- **AIGA Communication Graphics poster, 1993.** Brain scans and a flow chart linked by green and red lines. Teaches that diagram lines can tie unrelated layers together. *(visually checked: Cooper Hewitt 18647569. White ground (≈61%), a figure built from extruded bitmap dots, inset brain scans, thin black leader lines and red/green crossing lines. Names run vertically in pale yellow and pink, and captions reverse out of black bars.)*
- **Hand Holding a Bowl of Rice, Wilshire/Vermont, 2007.** An 8,200 sq ft oil mural painted from a video still she shot in Koreatown. Teaches that low-res source material can scale up to architecture and keep its blur as atmosphere. *(visually checked: aprilgreiman.com photo. Soft gradient bands of yellow #F2C55D, orange #D8813D and green #9BE094 with horizontal scan lines across a wedge-shaped facade.)*

## Process (derived)
*From observation to process (see SKILL.md §1). This is what transfers; the rest of the file is evidence.*

**April Greiman.** *Compose in depth, not on the sheet: stack planes that each keep the grain of the tool that made them, tilt the planes, and keep the words level.*
Process:
1. Start from an open ground at one extreme of value. 25–60% of the surface stays ground.
2. Sort the content by source, not by importance: captured (photo, video, scan), drawn (flat shapes), set (text), measured (data and metadata). Each source gets its own plane and keeps its own grain: one plane coarse (cells 6–10× the fine grain), the rest sharp. 4–6 planes.
3. Stack by overlap. Each plane crosses at least two others and at least one edge of the frame. Tilt the large planes 9–21°, no two at the same angle. Depth comes from overlap, size and hard offset only; nothing is blurred.
4. Keep every line that must be read at 0°, whatever plane it lies on. Text sits on a tilted plane and does not tilt with it.
5. Double the main text with a hard copy in the palest tint that is not the ground, displaced ≈1% of the width along one diagonal, the same direction everywhere. The copy is decorative and hidden from assistive technology; the main text carries the content and meets 4.5:1.
6. Load one hot flat plane, 9–13% of the area, the only fully saturated flat. It enters from an edge and carries the thing to act on.
7. Cluster density beside the hot plane, and run the measured text level along plane edges, at least 20× smaller than the largest element.
Why it works:
- Overlap is the strongest depth cue a flat surface has. With planes that are not parallel to the frame and are cut by it, the sheet stops reading as boxes on a page and reads as a volume seen through a window. Tilt without overlap is only a crooked layout.
- Grain is scale information. A coarse-celled image beside sharp type reads as a different origin and a different distance, so sources stay apart with no boxes round them (grouping by texture). Equalise the resolution and the planes collapse into one flat collage.
- Level text gives the eye one stable frame while everything else leans, so the disorder is felt and not paid for in reading. Tilt the text too and the page is simply hard to read.
Colour relations: ground 25–60% at one extreme of value; one hot flat 9–13% at peak chroma; two or three smaller flat planes at mid value; captured imagery reduced to one or two inks so it never out-saturates the hot plane; the offset tint is used only as a double, never as text colour; one deep full field (≤30%) is allowed for a single immersive panel, not as the default; reading text sits on ground or on a flat (≥4.5:1), never on the coarse grain.
Space and line: planes enter from the edges; a long format (3:1 to 3.8:1) reads as a sequence; thin leader lines in one weight may tie items across planes; a fragment of a regular dot lattice in one quadrant gives scale; scale jump ≥20×.
Type requirement: one neutral sans with a wide width range for the level headings; one fixed-pitch or coarse-celled voice for measured text, never under 12px. Smallness is a ratio: reach the 20× jump by enlarging the largest element, not by shrinking the smallest.
Motion and interaction: depth is the thing that moves. Planes shift at different rates on scroll (far ≈0.3×, near 1×; fixed under reduced motion). An image resolves from coarse cells to sharp once, in one monotone pass of 400–600ms, with no flicker. Focus widens the offset from 1% to 2% for as long as it lasts and adds a level rule; a selected item moves onto the hot plane. Controls sit level on flat planes, ≥44px.
Fails when: the content needs aligned columns (tables, forms), because overlap hides cells; reading runs long, because planes cut the measure; the screen is too small to keep 25% ground under four planes (drop to two); everything comes from one source (all text), so layers would have to be invented.
Signature (do not carry together): pixelated video stills and halftone dots · tilted wedges with airbrushed splatter · type doubled by a pale offset copy.

**Transfer test** (an illustration that the process survives new colours and content; never reuse its hues, layout or wording as a design answer):

Greiman's procedure → a dark-mode weather app in muted earth tones (phone, 390 × 844).
1. *Ground.* The deepest value, a brown-black at L 9; 42% of the screen stays bare.
2. *Sources.* Captured: the radar frame, one ochre ink, kept at 8px cells. Drawn: pressure fronts as flat shapes. Set: the forecast sentence. Measured: temperatures, wind, station and timestamps in a fixed-pitch face at 12px. Four planes.
3. *Stack.* Radar plane 120% of the width, tilted −12°, cut by the top and right edges. A flat slate plane tilted +9° crosses the radar and the bottom edge. The fronts cross both at 18°. Hard edges, no shadows.
4. *Level text.* "Rain by four." at 44px and 0°, on the slate plane; the hourly row at 0° below it.
5. *Offset.* The sentence is doubled by a pale sand copy 4px (1%) down and left.
6. *Hot plane.* One saturated terracotta wedge, 11% of the area, entering from the bottom-left edge. It holds the next-hour alert and the only button (48px high, level).
7. *Density.* Station and update time run level along the wedge's upper edge. The current temperature is a 240px numeral cropped by the left edge: 20× the metadata.
- *Motion.* On scroll the radar moves at 0.3×, the slate at 0.6×, text at 1×. On load the radar resolves from 24px to 8px cells in 500ms, once. Reduced motion: static.
- *State.* The focused hour's offset widens from 4 to 8px and a 2px level rule appears under it.
Result: a dark, earthy forecast with real depth. No pastel paper, no splatter, no video stills of people. What survived is the stack by source, mixed grain, tilted planes under level text, and one hot plane.

## Space & composition
- **Z-space over X/Y.** Plan every screen as 4–6 overlapping depth planes: far gradient field, large pixelated image, type, small "data" text, floating chips (triangles, grid fragments, thin rules). Nothing sits in its own clean box.
- **Diagonal axes.** Tilt the big planes 9–21° (Schmidt base plane ≈9°, Your Turn black wedges ≈21°), with several angles on one sheet. Headlines mostly stay horizontal on tilted planes, and small text stays horizontal so the page still reads. Exception: in Your Turn, My Turn the big headline rises a few degrees and some small display words are set upside down or mirrored; only the reading text (credits, dates) is strictly 0°.
- **The grid is a ghost.** Show a dot-matrix grid fragment in one corner as texture, and let content ignore it.
- **Scale jumps of 20x or more.** In DQ133 a life-size body shares the sheet with tiny bitmap captions. Pair a full-bleed figure or glyph with 9–10px annotations.
- **Long format.** The 3:1 fold-out reads as a timeline, so map it to horizontal scroll.
- **Uneven density.** Dense clusters around one hot spot, open fields elsewhere. In the 1978–93 posters the open field is white or pale grey (26–61% of the sheet; CalArts, Schmidt, Your Turn, AIGA). A coloured void (violet-black, gradient) appears only in DQ133's back and the 2007 mural.

## Color
*The hex table below is a reference sample for strict studies and homage only. For design, use the colour relations in "Process (derived)".*

She thinks in light, but on paper she starts from white. The checked posters are white or pale grounds with flat spot planes (vermilion, acid yellow-green, cobalt, brown), airbrushed glows at the edges and offset copies for depth. Saturated full fields (violet-black, process yellow) come with the video and Mac work (DQ133 back). No magenta field appears in any checked work.

| Role | Hex |
|---|---|
| Deep field / gradient start (video violet-black; DQ133 back, 30%) | `#241B32` |
| Gradient end / ambient glow (halftone yellow-orange glow, DQ133 back; no magenta seen) | `#E5BB69` |
| Signal accent (vermilion base plane, Schmidt ≈9%) | `#DA5939` |
| Depth offset A (pale cyan offset copy, Your Turn) | `#ADD4DB` |
| Depth offset B (brown type the cyan doubles, Your Turn ≈21%; no register red seen) | `#866250` |
| Electric chip (acid yellow-green, Your Turn 12.5%) | `#ECF783` |
| Paper / bitmap white (poster white; DQ133 cream `#FDF6E5`) | `#E7ECED` |
| Cobalt band (Your Turn top band) | `#4870A9` |
| Process yellow field (DQ133 back, 19%) | `#F8DA24` |

Logic: a pale ground carries the page, one hot flat plane (vermilion or acid yellow-green, 9–13% of the surface) anchors it, and the pale-cyan copy appears only as an offset shadow behind darker type. Keep the deep violet field for one immersive surface (a video/hero panel), not as the default canvas.

## Form, line & typography
Her type starts Swiss (Helvetica, Univers) and gets knocked off its axis. Words get stretched, set at angles, given drop shadows, letterspaced, or rendered as 1-bit bitmaps beside crisp vector type. Thin rules, small triangles, squiggles and dotted grids act like punctuation floating between layers. Fonts: **Inter Tight** or **Archivo** (neo-grotesk base, Archivo's width axis allows stretching), **Silkscreen** or **VT323** for bitmap labels, and **Space Mono** for timecode-like metadata.

## Rhythm, motion & time
Motion should feel like broadcast compositing (she made Paintbox idents for Esprit and Lifetime). Layers parallax at different rates as you scroll, with the far gradient slowest and the floating chips fastest. Images resolve from chunky pixels to sharp, moving from about 8px blocks to full resolution over 400–600ms. Hover slides a pale-cyan copy out from behind an element and settles back. Where a gradient glow is used, it drifts in hue on a 30s loop. Transitions are wipes and dissolves, not springs.

## UI translations
1. Build each view from at least four `position:absolute` or `z-index` planes. Give each plane its own `translateZ` and its own scroll speed (`perspective: 1200px` on the container).
2. Tilt the big planes 9–21° at different angles (`rotate: -9deg`, `rotate: 21deg`) and let them cross at least two other layers. Keep body copy and every line that must be read at 0°; a display headline may tilt a few degrees, as in Your Turn, My Turn (the one exception seen).
3. Use a pale ground (`#E7ECED`) for most views and let colour come from tilted flat planes and one airbrushed edge glow. Reserve a full deep field (`#241B32` with a yellow `#F8DA24` band) for one immersive panel, as on the back of DQ133.
4. Render one key image as visible pixels: downsample it, then upscale with `image-rendering: pixelated` at 6–10x. Put it next to a razor-sharp vector element.
5. Put drop shadows on type and chips as hard offsets, not blurs: one pale copy behind darker type, offset down-left by ≈1% of the frame width (`text-shadow: -6px 6px 0 #ADD4DB` on `#866250` type).
6. Use exactly one hot flat plane per screen (`#DA5939` or `#ECF783`, ≤13% of the area), the primary action or the current state.
7. Set metadata (dates, IDs, timestamps) in a bitmap font at 10px, scattered at layer edges like video timecode.
8. Lay a partial dot-grid or crosshair lattice over one quadrant at 20% opacity as texture, with content deliberately off it.
9. For long content, use a horizontal scrolling timeline (`scroll-snap-type: x`) where items enter at different depths.
10. On hover or focus, slide a pale-cyan copy out behind the element by 4px for 150ms, then recombine.
11. Load images progressively from pixel blocks to full resolution and make that sequence part of the design, not a skeleton loader.

## What this artist would reject
- A single flat z-plane of identical rounded cards with soft gray shadows.
- Hiding the medium: skeleton shimmers and pretending pixels aren't there.
- Neutral gray-and-blue palettes where "accent" means one muted brand blue.
- Everything orthogonal: every text block, image and divider locked to 0°.
- A house style applied to every screen. She said she doesn't have a style, and each piece follows its own logic.

## Signature prompt seed
Design this screen as a deep, layered video composite, not a flat page. Start from a pale ground with one deep violet-black video panel, then stack four or five depth planes, tilted 9–21°, that parallax at different speeds. Place one huge pixelated image (upscaled 8x, hard edges) beside crisp neo-grotesk type set level on a tilted plane. Give dark type a hard-offset pale-cyan copy. Scatter 10px bitmap timecode-style metadata at layer edges, plus small floating triangles and a ghost dot-grid fragment. Use exactly one vermilion or acid yellow-green plane as the focal action. Images resolve from pixels to sharp, hover slides out a pale-cyan copy, and overlap is welcome everywhere.

## Sources
- https://www.moma.org/collection/works/172729
- https://aprilgreiman.com/does-it-make-sense
- https://eyeondesign.aiga.org/april-greiman-is-still-ahead-of-the-curve/
- https://www.cooperhewitt.org/design-topics/women-in-design/april-greiman
- https://www.moma.org/audio/playlist/298/4850
- https://aprilgreiman.com/public-art/hand-holding-a-bowl-of-rice
- https://readymag.com/designstories/april-greiman/design-quarterly-133

- Images examined (visual check):
  - CalArts, Cooper Hewitt 18617589: https://images.collection.cooperhewitt.org/89746_69f0902346ccadc6_b.jpg
  - Douglas W. Schmidt, Cooper Hewitt 18617835 / 18637165: https://images.collection.cooperhewitt.org/88923_c6ef53891e01da3f_b.jpg, https://images.collection.cooperhewitt.org/81474_717dfa8a6651f2c4_b.jpg
  - Your Turn, My Turn, Cooper Hewitt 18650849: https://images.collection.cooperhewitt.org/81536_b482daf4310b5261_b.jpg
  - AIGA Communication Graphics 1993, Cooper Hewitt 18647569: https://images.collection.cooperhewitt.org/81476_5b401d4fec5f39a8_b.jpg
  - DQ133 front/back, aprilgreiman.com: https://cdn.prod.website-files.com/65eb84ca7db7cc5a9a9de38d/65f4f9cd0a019f1d78724176_DQ-133%20for%20Web-p-1600.jpg, https://cdn.prod.website-files.com/65eb84ca7db7cc5a9a9de38d/65f8f135769b4705860d3e05_DQ_133%20back%201200-p-1600.jpg
  - Hand Holding a Bowl of Rice, aprilgreiman.com: https://cdn.prod.website-files.com/65ef80eea4fd490fbb7746e8/65ef9e966efb730b954317bb_WV_Mural.jpg
