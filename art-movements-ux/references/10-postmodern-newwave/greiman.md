# April Greiman — New Wave / early digital design

## Essence
Greiman treats the screen as a deep space and not a flat sheet. Type, video stills, bitmaps and color planes float at different depths, overlap, and cast shadows. She leaves each tool's artifact visible on purpose (pixel, scan line, DayGlo ink), and she broke open her Basel training using the early Macintosh as a "co-creator." What results is a hybrid surface where low-res and high-res, typeset and captured, all sit in one frame.

## Key works examined
- **CalArts poster (with Jayme Odgers), 1978.** Photography, diagonal type and drop-shadowed planes in one perspective space. Teaches that the page has depth.
- **Douglas W. Schmidt poster, 1981.** Offset litho plus screenprint, with fluorescent fruit and buildings. Teaches that a fluorescent spot color can be the structure, not decoration.
- **Your Turn, My Turn, 1983.** Red and blue layers printed out of register, giving a proto-glitch double image. Teaches that misregistration can be a deliberate depth cue.
- **Design Quarterly #133, "Does It Make Sense?", 1986.** The issue's usual 32 pages became one double-sided fold-out of about 25.5 x 76.5 in. The front is a pixelated, life-size nude double self-portrait. It was made with MacPaint (sketching), MacVision (video digitizing) and MacDraw (layering and stretching), tiled out as letter-size LaserWriter sheets. Teaches that pixels can be a material and that big scale can sit next to tiny data.
- **AIGA Communication Graphics poster, 1993.** Brain scans and a flow chart linked by green and red lines. Teaches that diagram lines can tie unrelated layers together.
- **Hand Holding a Bowl of Rice, Wilshire/Vermont, 2007.** An 8,200 sq ft oil mural painted from a video still she shot in Koreatown. Teaches that low-res source material can scale up to architecture and keep its blur as atmosphere.

## Space & composition
- **Z-space over X/Y.** Plan every screen as 4–6 overlapping depth planes: far gradient field, large pixelated image, type, small "data" text, floating chips (triangles, grid fragments, thin rules). Nothing sits in its own clean box.
- **Diagonal axes.** Tilt one main element 8–15°, usually a headline or a photo strip. Keep the small text horizontal so the page still reads.
- **The grid is a ghost.** Show a dot-matrix grid fragment in one corner as texture, and let content ignore it.
- **Scale jumps of 20x or more.** In DQ133 a life-size body shares the sheet with tiny bitmap captions. Pair a full-bleed figure or glyph with 9–10px annotations.
- **Long format.** The 3:1 fold-out reads as a timeline, so map it to horizontal scroll.
- **Uneven density.** Dense clusters around one hot spot, open gradient fields elsewhere. The void is colored, not white.

## Color
She thinks in light: fluorescent spot inks over soft video-style gradients, with red/blue offsets for depth. Gradients run between near-complements (violet to orange) through a luminous middle, never gray.

| Role | Hex |
|---|---|
| Deep field / gradient start (video violet-black) | `#1B1035` |
| Gradient end / ambient glow (sunset magenta) | `#E0457B` |
| Signal accent (DayGlo orange) | `#FF6A13` |
| Depth offset A (process cyan) | `#00A6D6` |
| Depth offset B (register red) | `#E3242B` |
| Electric chip (acid yellow-green) | `#D4F542` |
| Paper / bitmap white | `#F4F1EA` |

Logic: one gradient field carries the mood, one fluorescent accent marks the focal point, and the cyan/red pair only appears as offset shadows or doubled images.

## Form, line & typography
Her type starts Swiss (Helvetica, Univers) and gets knocked off its axis. Words get stretched, set at angles, given drop shadows, letterspaced, or rendered as 1-bit bitmaps beside crisp vector type. Thin rules, small triangles, squiggles and dotted grids act like punctuation floating between layers. Fonts: **Inter Tight** or **Archivo** (neo-grotesk base, Archivo's width axis allows stretching), **Silkscreen** or **VT323** for bitmap labels, and **Space Mono** for timecode-like metadata.

## Rhythm, motion & time
Motion should feel like broadcast compositing (she made Paintbox idents for Esprit and Lifetime). Layers parallax at different rates as you scroll, with the far gradient slowest and the floating chips fastest. Images resolve from chunky pixels to sharp, moving from about 8px blocks to full resolution over 400–600ms. Hover splits an element into red/cyan offsets that settle back. Gradients drift in hue on a 30s loop. Transitions are wipes and dissolves, not springs.

## UI translations
1. Build each view from at least four `position:absolute` or `z-index` planes. Give each plane its own `translateZ` and its own scroll speed (`perspective: 1200px` on the container).
2. Rotate the hero headline or image strip 11° (`rotate: -11deg`) and let it cross at least two other layers. Keep body copy at 0°.
3. Fill the background with a two-hue `linear-gradient` or `conic-gradient` (violet to magenta to orange). Never use a flat #FFF canvas.
4. Render one key image as visible pixels: downsample it, then upscale with `image-rendering: pixelated` at 6–10x. Put it next to a razor-sharp vector element.
5. Put drop shadows on type and chips as hard offsets, not blurs: `text-shadow: 6px 6px 0 #00A6D6, -3px -3px 0 #E3242B`.
6. Use exactly one DayGlo `#FF6A13` element per screen, the primary action or the current state.
7. Set metadata (dates, IDs, timestamps) in a bitmap font at 10px, scattered at layer edges like video timecode.
8. Lay a partial dot-grid or crosshair lattice over one quadrant at 20% opacity as texture, with content deliberately off it.
9. For long content, use a horizontal scrolling timeline (`scroll-snap-type: x`) where items enter at different depths.
10. On hover or focus, split the element into cyan and red copies offset by 4px for 150ms, then recombine.
11. Load images progressively from pixel blocks to full resolution and make that sequence part of the design, not a skeleton loader.

## What this artist would reject
- A single flat z-plane of identical rounded cards with soft gray shadows.
- Hiding the medium: skeleton shimmers and pretending pixels aren't there.
- Neutral gray-and-blue palettes where "accent" means one muted brand blue.
- Everything orthogonal: every text block, image and divider locked to 0°.
- A house style applied to every screen. She said she doesn't have a style, and each piece follows its own logic.

## Signature prompt seed
Design this screen as a deep, layered video composite, not a flat page. Start with a violet-to-magenta-to-orange gradient field, then stack four or five depth planes that parallax at different speeds. Place one huge pixelated image (upscaled 8x, hard edges) beside crisp neo-grotesk type tilted about 11°. Give type hard-offset cyan and red shadows. Scatter 10px bitmap timecode-style metadata at layer edges, plus small floating triangles and a ghost dot-grid fragment. Use exactly one DayGlo-orange focal action. Images resolve from pixels to sharp, hover splits elements into red/cyan offsets, and overlap is welcome everywhere.

## Sources
- https://www.moma.org/collection/works/172729
- https://aprilgreiman.com/does-it-make-sense
- https://eyeondesign.aiga.org/april-greiman-is-still-ahead-of-the-curve/
- https://www.cooperhewitt.org/design-topics/women-in-design/april-greiman
- https://www.moma.org/audio/playlist/298/4850
- https://aprilgreiman.com/public-art/hand-holding-a-bowl-of-rice
- https://readymag.com/designstories/april-greiman/design-quarterly-133
