# Charles Rennie Mackintosh — Glasgow Style / Art Nouveau

## Essence
Mackintosh draws strict, tall frames and lets one small organic thing live inside each: a stencilled rose, a swallow cut through a headrail, a square of pink glass. Every room has one register, either dark oak focused on a single point or white enamel with tiny jewel-coloured insets. Furniture does the job of walls.

## Key works examined
- **Argyle Street Tea Rooms high-back chair, 1897.** Tapering uprights, square at the foot and round at the top, meet in an oversized oval headrail with a swallow cut through it. A crowd of these chairs screens a table and makes a room inside the room.
- **Glasgow School of Art, 1897–99 / 1907–09.** A grid of huge north studio windows on a plain field, with a few sculptural moments set against it.
- **GSA Library, 1907–09.** A dense timber cage with small balusters enamelled in bright colours. Colour appears only in small notches of the structure.
- **Willow Tea Rooms, Salon de Luxe, 1903.** Light, with silver, grey and pink, and a mirrored frieze. Eight silver chairs in purple velvet enclose two tables.
- **Hill House, 1902–04.** A dark hall opens into white rooms stencilled with a geometric rose in pink, green and silver. Colour follows each room's use.
- **78 South Park Avenue dining room, 1905–06.** A dark rose-and-lattice room that sends every glance to the lit table.

## Space & composition
- **Verticality as structure.** Elements run 3:1 to 5:1 tall. Chair backs rise well above head height and window mullions run full height. Treat height as the main axis and width as secondary.
- **Rooms inside rooms.** Tall chair backs and screens, not walls, break open fields into enclosed bays.
- **The square as module.** Small squares (8–12px in UI) appear only at the edges and ends of tall members, like beads at the top of a post.
- **Quiet field, then sculpture.** Most surfaces are plain. Ornament gathers at a few nodes (entrance, oriel window, headrail).
- **Thresholds.** The dark hall gives way to the white room. Movement through the space is designed as a change of register.

## Color
One register per room. Dark rooms: near-black brown, no bright accent, one lit point. White rooms: warm enamel with pastel jewels under 5% coverage. Silver is the neutral highlight in both.

| Role | Hex |
|---|---|
| White-room ground (painted enamel) | `#F3F0E8` |
| Dark-room ground (stained oak) | `#1C1615` |
| Wrapping-paper neutral (stencil ground) | `#8B7F70` |
| Silver (frieze, chair paint, dots) | `#B8B8B4` |
| Rose pink (glass insets, rose heads) | `#D79FAD` |
| Velvet purple (upholstery, rose shadow) | `#5B3966` |
| Stem green (leaf strokes, rare) | `#7C9677` |

## Form, line & typography
His lettering uses tall, condensed capitals with stems as straight as chair posts. Crossbars sit unusually high or low, so letters such as E, H and A read off-centre. Bowls and counters become stretched ovals, and letters often nest into ligatures. The line language mixes long ruled verticals with a single tight curve at the end, like a stem with a closed bud. The rose is the same move on a small scale: concentric arcs closed inside a square. ITC Rennie Mackintosh (1996) has capitals only, plus many ligatures: a display system, not a text face.

Free fonts that fit: **Federo** for condensed Deco-geometric display, **Poiret One** for hairline caps with oval bowls, and **Josefin Sans** for body and labels, since its geometric shapes have a tall, elegant cap height.

## Rhythm, motion & time
- Regular vertical repetition (chair backs, mullions) broken by one event. Motion settles like posts: 8–16px vertical translations, no bounce, `cubic-bezier(.2,.7,.1,1)`.
- Draw the frame first (stroke-dashoffset on lattice lines), then fade in the rose 150ms later.
- Hover lights a small "glass inset" (a 6px square turning from silver to pink) and does not lift the whole card.

## UI translations
1. Build the layout on narrow, tall columns with a 1:4 width-to-height ratio. Hero panels and cards should be portrait, never landscape.
2. Group related content with "high-back" dividers: 2px vertical rules that run 1.5× taller than the content they enclose, ending in a 3×3 grid of 4px squares.
3. Pick one register per screen, either dark (`#1C1615` ground, a single lit focal card) or white (`#F3F0E8` ground). Never mix the two in one view.
4. Keep pink and purple below 5% of pixels: square insets, a selected state, one icon. Use silver for every secondary highlight.
5. Set headings in condensed caps with letter-spacing of 0.08em and a line-height of 0.95, and use a ligature or nested letter in the logotype.
6. Use one stylised rose (concentric arcs in a square) as the only illustrative mark, and vary it slightly at each use, no two identical.
7. Replace the heavy nav bar with a 24px silver frieze strip along the top.
8. Put ornament only at nodes: the active tab, the primary CTA, the page title. Leave everything else plain.
9. On section change, crossfade from the dark register to the white one over 500ms. Each region of the app should feel like a different room.
10. In a dark-register list, dim everything except the hovered row, which gets a warm light, like candlelight on a dinner table.
11. Make cards end in an oval "headrail" cap at the top, with one small negative-space cutout as the brand mark.

## What this artist would reject
- Rounded, low, landscape cards in an even masonry grid that has no single focus.
- Ornament or gradient spread evenly over every surface.
- Mixing dark-mode and light-mode components on one screen.
- Saturated brand colour used across large areas for buttons, headers and backgrounds at once.
- Bouncy, playful spring motion.

## Signature prompt seed
Design the screen as a tall, narrow room in a single register: warm enamel white `#F3F0E8` or stained-oak near-black `#1C1615`, never both. Group content with hairline vertical posts that rise past their content and end in small grids of squares. Put a silver frieze strip along the top. Leave most surfaces plain and gather ornament at one node, a stylised square rose in pink `#D79FAD` with a purple `#5B3966` shadow, covering under 5% of pixels. Headings are condensed caps with offset crossbars. Motion settles vertically, without bounce. Frame first, flower second.

## Sources
- https://www.dezeen.com/2018/06/08/willow-tea-rooms-150-charles-rennie-mackintoshs-interior-design/
- https://www.dezeen.com/2018/06/07/charles-rennie-mackintoshs-argyle-chair-150-anniversary/amp/
- https://www.dezeen.com/2018/06/05/glasgow-school-of-art-charles-rennie-mackintosh-masterwork-150-anniversary/amp/
- https://victorianweb.org/art/design/mackintosh/1.html
- https://madegooddesigns.com/?p=110352
- https://europeana.eu/da/stories/the-hill-house-in-helensburgh
- https://www.thecollector.com/charles-rennie-mackintosh-10-scottish-art-nouveau-designs/
- https://fontsinuse.com/typefaces/3262/itc-rennie-mackintosh
