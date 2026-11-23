# Kazimir Malevich — Suprematism

## Essence
Malevich cut painting back to a "zero point" (he signalled it by putting "0" in the title of the 0,10 exhibition) and then rebuilt it from flat, unshaded planes floating in white space that has no edges. What makes his work recognisable is a few tilted, weightless shapes in a white field read as endless space instead of empty background.

## Key works examined
- **Black Square, 1915** (79.5 × 79.5 cm, Tretyakov). A single black plane inside a white border, hung high across a room corner where a household icon would go. Lesson: one element, placed with total authority, can carry a whole screen.
- **Suprematist Composition: Airplane Flying, 1915** (58.1 × 48.3 cm, MoMA). Stretched, rotated, overlapping bars on white. Lesson: rotation and stacking create a sense of flight and direction without drawing any motion.
- **Red Square, 1915** (Russian Museum). The "square" is a slightly skewed quadrilateral. Lesson: being a little off true is what makes a shape look alive.
- **Suprematist Composition: White on White, 1918** (79.4 × 79.4 cm, MoMA). A tilted, off-centre cool white square on a slightly warmer white ground, with loose edges. Lesson: hierarchy can come from temperature alone.
- **Black Square, later versions (c. 1923–1930s).** Repainted with students. Lesson: the sign is a reusable system mark, like a logo.
- **Arkhitekton Alpha / Gota, 1923** (Gota: plaster, 85.3 × 56 × 52.5 cm). Bare white blocks gathered around one dominant central mass, spreading out horizontally (Alpha) or upward (Gota). Lesson: build a layout by adding smaller volumes to one main block.

## Space & composition
- **Make the ground mean infinity.** White is not padding. It is space that runs past the frame. Let 70–85% of the view stay as one uninterrupted field and keep content away from the edges, so the field reads as endless.
- **Rotate off the grid.** Tilt the main planes between −8° and −30°. Share one tilt axis, with one counter-plane at about +60°.
- **Weight off-centre.** Put the visual centre of mass in the upper-left or upper-right third and let thin bars drift toward the opposite corner.
- **Scale jumps of about 1:8:40.** Use one huge plane, a few medium bars, and hairlines or small dots.
- **Arkhitekton clustering.** Treat a dashboard as one main block with secondary panels stuck to its sides at varying depths and heights, never a uniform card grid.
- **Corner placement.** Like the icon-corner hang, set the key mark where two edges meet.

## Color
Color here is flat, opaque, and has no gradient or modelling. In White on White mode the palette drops to two whites that differ only in temperature.

| Hex | Role |
|---|---|
| `#F1ECE0` | Warm ground: the "infinite" field (the White on White ground) |
| `#FBFBF8` | Cool white: the raised plane that is almost invisible |
| `#141312` | Suprematist black: the main mass, set once per screen |
| `#C42A1D` | Cadmium red: the primary action, the single "energy" plane |
| `#2A3B8F` | Ultramarine: secondary bars, links |
| `#E2B33A` | Ochre-yellow: small accents, hairlines, a few dots |
| `#8C8A84` | Warm grey: a cracked-edge tone for disabled or meta text |

## Form, line & typography
Every shape is a plane, never an outlined box or a stroke-drawn icon. Edges are crisp but slightly off true: rectangles drift a degree out of square, and bars taper or skew. Type should behave like another plane. Set headings in a heavy geometric sans, rotated with the composition and sometimes running vertically along a bar. Body text stays horizontal and small. Faces with Cyrillic support (free on Google Fonts) suit his 1920s print work:
- **Unbounded**: wide and blunt, good for rotated display words.
- **Jost**: a Futura-like geometric sans for body and UI.
- **Russo One**: a single slab-heavy word or a numeral.

## Rhythm, motion & time
Motion should feel like drifting in zero gravity, not bouncing. Planes move slowly (600–1200 ms), with `cubic-bezier(.2,.0,.0,1)` as the default easing, so they glide in from off-screen and settle at their tilt. On scroll, layers can parallax at different rates (heavy black slowest, thin bars fastest) A "zero" state matters: empty states and loading should strip the screen down to one black or red plane on the field.

## UI translations
1. Make the page background `#F1ECE0` and set cards in `#FBFBF8` with no border and no shadow, so the two whites alone separate them.
2. Rotate the hero block with `transform: rotate(-12deg)` and let it bleed off the top-right edge by about 20% of its width.
3. Allow exactly one black plane per screen. If two things want to be black, one of them becomes a bar.
4. Make the primary CTA a red rectangle around 3:1, tilted to match the hero, with a label in heavy uppercase Jost.
5. Replace dividers with thin ultramarine or ochre bars 3–6 px thick, set at the composition's angle and running past the container.
6. Build dashboards arkhitekton-style: one dominant panel spanning 2/3 of the width, with 3–5 smaller panels joined to its edges at staggered offsets (CSS grid with deliberately uneven `grid-row` spans).
7. Run a section label vertically (`writing-mode: vertical-rl`) along the edge of a tall bar.
8. Animate entry so planes drift in from outside the viewport on their own axes, staggered 80 ms, heaviest first.
9. On hover, rotate the plane 3° and shift its z-order above its neighbour. No colour change, no glow.
10. Empty and onboarding states show only one off-centre black square on the field, with one line of small text below and left of it.

## What this artist would reject
- Drop shadows, gradients, and glassmorphism: illusionistic depth instead of overlapping flat planes.
- Uniform card grids with equal gutters, which give density without hierarchy.
- Centred, symmetric hero layouts with a headline, a subhead, and two buttons.
- Outlined icons and skeuomorphic illustration, which bring back the "object" he removed.
- Springy, bouncy micro-interactions: playfulness where there should be weightlessness.

## Signature prompt seed
Design this app screen as a Suprematist field. A warm off-white ground (#F1ECE0) fills most of the viewport and reads as endless space. Content floats on flat, unshaded planes with no borders or shadows, all tilted on one axis around −15°. One dominant black rectangle anchors the upper left. A single red bar is the only call to action. Thin ultramarine and ochre bars cut across and run off the edges. Scale jumps sharply, from hugely heavy to hairline. Headings in Unbounded rotate with the planes, and body copy in small Jost stays horizontal. Planes glide in slowly without bouncing.

## Sources
- https://tate.org.uk/art/artists/kazimir-malevich-1561/five-ways-look-malevichs-black-square
- https://en.wikipedia.org/wiki/Black_Square
- https://www.moma.org/collection/works/80385
- https://www.moma.org/collection/works/79269
- https://socks-studio.com/2015/07/15/kazimir-malevichs-arkhitektons/
- https://thecharnelhouse.org/2014/03/12/suprematism-in-architecture-kazimir-malevich-and-the-arkhitektons/ (Gota caption: 1923, plaster, 85.3 × 56 × 52.5 cm)
