# Ludwig Mies van der Rohe — Modernist architecture

## Essence
Mies drew a strict, regular structural grid and then placed a few free-standing planes inside it, so that space flows around them and is never boxed into rooms. The minimal form doesn't come from being cheap. It comes from extreme precision, and from saving the luxury for a few large, perfectly finished surfaces: onyx, travertine, bronze, primavera wood. In his work the frame is the ornament and the material is the color.

## Key works examined
- **Barcelona Pavilion, 1929 (rebuilt 1983–86):** a regular grid of chrome-clad cruciform columns with freely placed planes between them. Content can float off the grid.
- **Golden onyx wall, Barcelona Pavilion:** the single book-matched slab of Atlas Mountains onyx that the plan turns around. One precious surface anchors the whole composition.
- **Farnsworth House, 1951:** a white steel floor slab and roof slab raised 5'3" above the floodplain, with an off-center wood core. The base is the hero, and the one opaque block sits off-center.
- **Seagram Building and plaza, 1958:** a 515 ft tower set 100 ft back from Park Avenue behind a granite plaza. Spending space on emptiness is how prestige reads.
- **Seagram bronze I-beams:** non-structural, purely expressive mullions that stand in for the hidden frame. Structure is used as rhythm and ornament.

## Space & composition
- **The grid is a grid of supports, not of walls.** At Farnsworth, eight columns at 22 ft centers make three bays; the roof cantilevers about 5.5 ft (a quarter bay) past the end columns. Let the outer edges overhang the grid by a quarter column.
- **Offset planes, not enclosures.** At Barcelona the walls slide past each other, so the circulation path narrows and widens. Panels never close into four-sided boxes.
- **One opaque core, off-center.** The Farnsworth core (13 × 25 ft) sits slightly north of center in a 55 × 28 ft room. Put the dense element (nav, editor, data table) at about 45/55, never dead center.
- **The plinth.** Both houses sit on a raised travertine base, reached by a few steps. Give the page a distinct base band that the content "stands on."
- **Setback as luxury.** The Seagram plaza gives up ground-floor value for an empty forecourt. Give the first 30–40vh to a quiet surface with a single name and one entry point.
- **Measured void.** Every gap is a multiple of the module, never leftover.

## Color
Mies used no applied color. Color comes from materials, and each material has one job.

| Hex | Role |
|---|---|
| `#E9E2D3` | Travertine. Base canvas and plinth |
| `#F7F7F4` | Farnsworth white enamel. Structural lines and frames |
| `#C9A25E` | Golden onyx. The single feature surface (one per screen) |
| `#2F4A3E` | Tinos verde antico. Deep secondary panel or the selected state |
| `#5B4632` | Seagram bronze. Mullions, rules, active text |
| `#7E8A86` | Grey-green tinted glass. Translucent overlays (with backdrop-blur) |
| `#1C1C1A` | Black. Text only |

Logic: about 80% stone, 15% frame and glass, one veined onyx hit (subtle SVG noise). Two onyx surfaces read as decoration.

## Form, line & typography
Mies's line language is the steel profile: thin, constant-width, perfectly straight, with crisp right-angle crossings like the cruciform column and no visible joints. The type should feel engineered, with even strokes, open apertures, and no flourish. Use a strict scale (14/18/28/56) and all-caps labels tracked +0.08em.
- **Inter Tight** or **Archivo** for UI and headings (neutral, grotesk, steel-like).
- **IBM Plex Mono** for numerals and data, where the grid needs to show.

## Rhythm, motion & time
The experience is a walk past planes, not a series of screens. Motion should feel like your viewpoint shifting while the architecture stays put: panels translate slowly in parallax (0.3–0.5× scroll), and nothing scales or bounces. Easing: cubic-bezier(0.4,0,0.2,1), 400–600ms. Reveal content by sliding a plane aside, as though a wall moved, never by fading in from nothing. On hover, a rule warms from bronze to onyx and does not grow.

## UI translations
1. Lay the page on a visible but faint column grid (1px `#5B4632` at 8% opacity). Hang content between the lines, not on them.
2. Build at most three free-standing panels per view. Give each a different width (for example 5, 3, and 7 columns) and offset them vertically so the gaps between them become paths.
3. Make exactly one surface per screen onyx-textured (a hero card, primary CTA field, or featured record). Everything else is stone or glass.
4. Run thin vertical bronze rules every 64px in headers and tables as non-structural "mullions." Do the same for rhythm in lists.
5. Raise the main content on a plinth: a 1px top border plus a 24px-taller travertine band below.
6. Put the dense functional core (sidebar, editor) off-center at 45/55. Never split the screen in two equal halves.
7. Limit component states the way the Seagram blinds were limited: a toggle, an accordion, or a drawer gets only three positions (closed, half, open) so the composition always holds.
8. Use translucent grey-green glass (`backdrop-filter: blur(12px)`, `#7E8A86` at 30%) for overlays, so the plane behind stays legible.
9. Navigate by sliding planes horizontally, not by modal pop-ups. Space should flow from one area to the next.
10. Treat the empty hero as the plaza: one wordmark, one entry action, and 40vh of quiet stone. Don't put cards there.
11. Give corners `border-radius: 0` and hairline borders of 1px. Use a 2px rule only on the single structural element.

## What this artist would reject
- Rounded, shadowed cards stacked into equal boxes. These are enclosures, not planes.
- Gradients and accent colors used for "brand energy" instead of real material differences.
- Ornament that hides the system: illustrations, decorative blobs, icon confetti.
- Centered, symmetrical hero blocks with three equal feature tiles underneath.
- Components with unlimited visual states that break the facade's uniformity.

## Signature prompt seed
Design this app screen as a Miesian pavilion. Lay a faint bronze column grid over a warm travertine field (#E9E2D3). Set three free-standing panels of different widths, offset so the gaps between them read as paths, with no closed boxes. Make one surface golden onyx (#C9A25E) with fine veining; everything else is stone, white enamel lines, or blurred grey-green glass. Leave the top 40vh as an empty plaza with one wordmark and one action. Put the dense core off-center at 45/55. Use 1px hairlines, square corners, and a precise grotesk. Motion slides planes slowly, as if you were walking past walls.

## Sources
- https://wikiwand.com/en/articles/Barcelona_Pavilion
- https://en.wikipedia.org/wiki/Farnsworth_House
- https://www.archdaily.com/59412/ad-classics-seagram-building-mies-van-der-rohe
- https://www.wttw.com/node/740
- https://www.macba.cat/en/node/100337
- https://hyperallergic.com/548225/looking-back-at-one-of-mies-van-der-rohes-most-famous-buildings/ (paywalled; only the teaser was readable)
