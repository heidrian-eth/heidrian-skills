# Alphonse Mucha — Art Nouveau

## Essence
Mucha builds every image as a vertical shrine: one figure, a circular "halo" disc behind the head, a frame around her, and lettering locked into that frame as if cast from one piece. A single flowing outline governs everything (hair, smoke, drapery, tendrils), set against still geometric borders and filled with muted, chalky color. He treated ornament as a reusable, mass-printable system.

## Key works examined
- **Gismonda (Sarah Bernhardt), 1894–95**: 214 × 74 cm, almost 3:1, on two joined sheets. Extreme portrait format plus one halo anchors everything.
- **Job (cigarette papers), 1896**: hair and smoke curl into the logo while a gold Byzantine zigzag border stays rigid. Curves are set against hard geometry, and the brand mark sits inside the illustration.
- **The Seasons, 1896**: four 103 × 54 cm panels (~1.9:1) with no text, Mucha's first series for the printer Champenois. One template, four variants.
- **Rêverie, 1897–98**: a figure framed by a halo of pink flowers, turning the pages of a design book. The frame is the card.
- **The Arts (1898) / The Precious Stones (1900)**: figures sit on or inside large gold discs, each set above its own plant. A component library with theme slots.
- **Documents Décoratifs, 1902**: 72 plates covering posters, wallpaper, friezes, stained glass, jewelry, furniture and lettering. In effect, a design-system handbook.

## Space & composition
- **Tall column.** Gismonda's width-to-height ratio is about 1:2.9, the Seasons about 1:1.9: roughly a phone viewport made ceremonial.
- **Three-tier stack.** An ornamented title band sits at the top, the figure and halo in the middle ~65%, and a thin, quiet footer at the bottom (Gismonda's footer gives only the theater's name). The top is heavy and the bottom light.
- **The halo as the visual anchor.** A circle or arch behind the head, centered on the vertical axis at about the upper third, pulls the eye to the face before anything else.
- **Uneven density.** Under deadline, Gismonda's background was left mostly blank, with mosaic tiles only behind the head. Ornament collects only where attention should go.
- **The frame is the layout.** Borders, arches and friezes enclose the content, and the lettering is built into them rather than floating on top.

## Color
The logic is low-chroma pastels on a warm paper ground, held together by a dark contour line rather than by value contrast. One metallic accent, gold, marks the sacred zone: halo and borders. Gismonda was printed in lavender, salmon, cobalt, light blue and olive on tan paper. Job's gold-on-purple suggests a deeper "night" variant.

| Hex | Role |
|---|---|
| `#E9DCC3` | Tan paper ground (page background, never pure white) |
| `#B8A4C9` | Lavender: large fields, drapery, secondary surfaces |
| `#E3A48A` | Salmon: skin and flowers, warm highlight and active state |
| `#9FB7C9` | Light blue: halo interior, quiet panels |
| `#8A8C5A` | Olive: foliage, borders, secondary text |
| `#C49A3A` | Muted gold: halo rim and frame, the one sacred accent |
| `#3E3330` | Sepia-black contour: all lines and body text |

## Form, line & typography
Mucha's line changes weight as it moves. It thickens on the outer contour and thins inside, and it ends in loops and coils. His lettering is hand-drawn: rounded, closed counters, flared or uncial-like strokes. The letters are stretched or squeezed to fill a band exactly, the way type fills a stone tablet,.

Fonts (Google Fonts): **Macondo Swash Caps** (display titles only, sparingly), **Marcellus** (flared caps for labels and nav), **Cormorant Garamond** (body).

## Rhythm, motion & time
Motion should feel like hair in water: slow, continuous, organic, never springy. Use easing like `cubic-bezier(.45,.05,.25,1)` and durations of 600–900 ms. Halos can rotate or "bloom" very slowly (a radial mask from 0 to 100% over about 800 ms) on load. Line ornaments should draw themselves with SVG `stroke-dashoffset`. Borders stay still; contents move. Theme by season or time of day, as in his series: fixed structure, swapped palette and flora.

## UI translations
1. Build hero screens as a vertical shrine: an ornamental title band (about 15% of height), a central subject with a circular halo disc behind it at the 33% mark, and a 1-line footer at most 6% of height.
2. Put a 1.2× oversized circle (`border-radius:50%`, gold 2px rim, light-blue fill, faint mosaic pattern) behind avatars, product shots or the main stat, so the focal object reads as haloed.
3. Make the title fill its band exactly: use `font-size` from `clamp()` plus letter-spacing so the word spans 100% of the container width, set on a tinted cartouche with a 1.5px sepia outline.
4. Set the page on `#E9DCC3` paper, not white. Use no more than one saturated-feeling accent (gold) and keep it for frames and the selected state.
5. Outline cards and images with a variable-width contour (an SVG path or doubled border, 2px outside and 0.75px inside) instead of drop shadows.
6. Put rigid geometry (zigzag or tile borders made with `repeating-linear-gradient`) around fluid content. Never make both the frame and the content curvy.
7. Let one SVG "whiplash" vine grow out of the brand mark and wrap the section header, the way Job's smoke runs into the logo.
8. Concentrate ornament at the focal point and let it fade toward the edges. Leave the outer 30% of the layout flat.
9. Ship a token system like Documents Décoratifs. A small set of frame, halo, border, lettering and flora components plus 4 seasonal palette sets should let you assemble any screen.
10. On hover, draw a fine gold contour around the card (`stroke-dashoffset` over 700 ms) and very slightly widen the halo behind its thumbnail (scale 1 to 1.04).
11. On mobile, treat the 1:2.9 Gismonda ratio as the full-screen splash or onboarding format, one figure per screen.

## What this artist would reject
- Flat, borderless cards floating on white with generic drop shadows.
- Lettering placed on top of imagery without a container. In Mucha, type and frame are one object.
- Even, uniform ornament or icon sprinkles spread across the whole screen.
- High-chroma primary brand colors (pure #0000FF, neon CTAs).
- Bouncy, springy micro-interactions. He would prefer slow, flowing motion.

## Signature prompt seed
Design this app screen as a tall Mucha shrine on warm tan paper (#E9DCC3). An ornamented title cartouche spans the top band, its hand-lettered display type stretched to fill the width exactly. The central subject sits before a large gold-rimmed circular halo with faint mosaic tiles at the upper-third mark. Hold everything with variable-weight sepia contours, not shadows. Use lavender, salmon, light blue and olive pastels, with gold only on frames and selection. Rigid zigzag borders enclose fluid whiplash vines that grow out of the logo. Keep ornament near the focus and plain at the edges.

## Sources
- https://www.artic.edu/artworks/10429/la-gismonda-sarah-bernhardt
- https://artmajeur.com/en/magazine/5-art-history/gismonda-by-alfons-maria-mucha/333445
- https://theartstory.org/artist/mucha-alphonse/
- https://productiontype.com/article/mucha-documents-decoratifs
- https://muchafoundation.org/gallery/themes/theme/art-posters
- https://en.wikipedia.org/wiki/The_Seasons_(Mucha)
- https://kettererkunst.com/dict/le-style-mucha.php
