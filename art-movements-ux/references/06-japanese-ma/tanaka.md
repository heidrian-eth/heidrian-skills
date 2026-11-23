# Ikko Tanaka — Japanese graphic design (Ma meets modernism)

## Essence
Tanaka took the flat, opaque color fields and stylized natural motifs of Rinpa and Edo woodblock prints and put them on a Bauhaus/Swiss construction grid. The result is images built from the fewest possible geometric planes that still carry a full cultural identity. Simplicity, as Cooper Hewitt puts it, means "maximizing a visual message with minimum components." That is different from stripping things out. The poster is assembled like a tangram, and the empty field is an active plane rather than background.

## Key works examined
- **Nihon Buyo poster (1981)**, screenprint and rotogravure, 75.5 x 49.2 cm, for UCLA's Asian Performing Arts Institute. A geisha made from a few grid-snapped planes: a pale face block, black hair masses, small red lips and pink cheeks. It teaches that identity survives extreme reduction as long as the *signature* features stay intact.
- **The 8th Sankei Kanze Noh (1961)**, screenprint, 103 x 73 cm. Multicolored kanji on a black ground. Type is the image, and a dark field makes saturated color vibrate.
- **MUJI identity (1980 onward)**, with Kazuko Koike and Takashi Sugimoto. Kraft and recycled paper, a maroon four-kanji logo, one illustration plus one witty headline ("low price for a reason"). The brand is defined by what it leaves out.
- **Seibu target pattern (1975 onward)**, concentric green and blue. One geometric motif carries a whole environment.
- **Kōchō typeface**: a Bodoni-inspired Mincho with strong thick-thin contrast, bringing Didone drama to Japanese text.

## Space & composition
- **Construction grid first, figure second.** In the Nihon Buyo poster the face is not drawn. It is *tiled*: squares, rectangles and quarter circles snapped to a modular grid (think 6 x 8 or 8 x 10 units on a roughly 2:3 sheet).
- **Figure high, text low and tiny.** The image occupies the top ~70–75%. Typography sits in a thin band at the foot, set small, in a disciplined left- or center-aligned block. The type never competes with the figure.
- **Void as a plane.** Ground is one unmodulated color field, never "white space". The edges of the figure are defined by where planes stop (negative space expressing form), with no outlines.
- **Low part-count.** Most Tanaka posters resolve to 5–9 shapes. Count your components.
- **Symmetry, then one deviation.** The face is near-frontal and symmetric, and a single offset keeps it alive.

## Color
Opaque, flat, screenprint-pure. No gradients, no tints within a shape. Pastels (pink, cream) sit directly against black and saturated red, and that contrast does all the work. MUJI is the same system turned down to near-zero: kraft brown plus one maroon.

| Role | Hex | Note |
|---|---|---|
| Ground field | `#C9C2B4` | warm grey/kraft-adjacent plane |
| Face / light plane | `#F3E9D8` | ivory, never pure white |
| Ink mass | `#141414` | hair, kanji, the heavy anchor |
| Accent (lips, seal) | `#D8262E` | vermilion, tiny area only |
| Soft accent | `#EFA7A4` | cheek pink, sits against black |
| Brand mark | `#7F0019` | MUJI-style maroon |
| Cool counter-field | `#2F5D8A` | Seibu-like blue for a second zone |

Keep the area ratio roughly ground 55%, light plane 25%, ink 15%, accents ≤5%.

## Form, line & typography
Form is made of geometric primitives: square, circle, half-circle, quarter-circle, bar. Line exists only as the edge between two fields. Kanji strokes are treated as rectangles and dots that can be recolored one stroke at a time. For type, pair a high-contrast serif Mincho (the Kōchō instinct) with a quiet, rational sans set small.
- **Shippori Mincho** or **Zen Old Mincho** (Google Fonts) for display, giving Kōchō-like thick-thin contrast
- **Noto Sans JP** for tiny, grid-locked captions and metadata
- **Jost** as a Latin geometric companion with Bauhaus genes

## Rhythm, motion & time
Motion should feel like a screen-printing pass: each color plane lands separately, as a hard-edged cut with no blur. Stagger the arrival of planes by ~60–90 ms with a short `steps()` or crisp `cubic-bezier(.2,0,0,1)` over 180–240 ms, so the figure *assembles* rather than fades in. Interaction recolors a plane rather than moving it: stillness with one decisive event.

## UI translations
1. Build hero illustrations and empty states from 5–9 CSS primitives (`border-radius: 50%`, `0 0 100% 0` quarter circles, rectangles) snapped to an 8-unit grid. No SVG detail, no outlines.
2. Give the screen one flat `background` field per zone. Separate zones by a hard color change with no border, shadow or divider.
3. Put the image or key metric in the top 70% of the viewport and push the title, meta and CTA into a compact band in the bottom 25%, set at 12–14px.
4. Use `#D8262E` on at most one element per screen, under 5% of the area: the "lips" of the layout. Typically this is the primary action or the live status dot.
5. Set display headings in a high-contrast Mincho at 48–72px against a 12px sans caption. The 5:1 scale jump stands in for decoration.
6. Recolor individual strokes or letters of a short CJK or Latin wordmark in separate flat colors on a black field for splash and section headers (the Kanze Noh move).
7. On load, animate planes in one at a time with hard edges (`clip-path: inset()` reveals, 70 ms stagger). Never use opacity fades or blur.
8. Make hover and selection swap a plane's fill (ivory to pink, ground to blue). Don't scale, lift or shadow anything.
9. For brand or commerce screens, use the MUJI register: kraft ground `#C9C2B4`, one maroon mark, one plain line illustration, one sentence of copy that explains *why*.
10. Make the layout near-symmetric, then offset exactly one element by half a grid unit.

## What this artist would reject
- Gradients, glassmorphism, and soft drop shadows that blur plane edges
- Outlined icons and 1px divider lines. Edges should come from color meeting color.
- Big headlines fighting a big hero image, or stock photos standing in for a constructed emblem
- Accent color sprinkled on every button, tag and link
- Busy "brand patterns" that don't come from a single geometric idea

## Signature prompt seed
Design the screen as a screenprinted poster: one flat warm-grey field, with a central emblem assembled from no more than eight geometric planes (squares, half and quarter circles) locked to an 8-unit grid and placed in the upper 70%. Edges come only from colors meeting, with no outlines, shadows or gradients. Use ivory, black ink, and a single tiny vermilion accent for the primary action. Pair a high-contrast Mincho display with a whisper-small sans caption block at the foot. Planes snap in one by one with hard clip reveals, and hover recolors instead of moving.

## Sources
- https://www.cooperhewitt.org/2015/12/05/do-i-look-simple/
- https://collections.vam.ac.uk/item/O1161237/nihon-buyo-poster-tanaka-ikko/
- https://www-4.collection.cooperhewitt.org/objects/18645853
- https://umma.umich.edu/objects/the-8th-sankei-kanze-noh-performance-2017-2-8
- https://yokogaomag.com/editorial/ikko-tanaka-muji
- https://www.dandad.org/insights/features/how-build-iconic-brand-muji-founding-board-member-features-opinions
- https://en.wikipedia.org/wiki/Ikko_Tanaka
- https://www.moma.org/collection/works/7848 (attempted, failed to load)
