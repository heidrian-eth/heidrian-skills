# Josef Müller-Brockmann — Swiss International Typographic Style

## Essence
Müller-Brockmann treated a page as a measured field. Every element snaps to a modular grid, so meaning comes from position, interval and scale, not from decoration. Inside that rigid system he allowed one large, almost musical gesture: arcs, rotated squares or giant overlapping letters that move against fixed, flush-left Akzidenz-Grotesk type. The structure is strict and the main move is free.

## Key works examined
- **Beethoven, Tonhalle Zürich (1955)**: 127.6 × 91 cm lithograph. Black arc segments whose spacing follows a doubling rule turn a mathematical progression into a visual crescendo. Lesson: derive spacing from a ratio, not by eye.
- **musica viva series (1957–1971)**: Constructivist bars and squares stand in for harmonic structure without imitating musical notation. One poster uses a grid 4.5 fields wide by 4 deep, and its small program text aligns to the letters of the headline.
- **der Film, Kunstgewerbemuseum Zürich (1959–60)**: 128 × 90.6 cm offset print. Giant grey "Film" sits behind white "der Film", which turns cinematic montage into type layers that read as earlier and later in time.
- **Schützt das Kind! (1953)**: photography by Ernst Heiniger, 127.5 × 90.5 cm. A car too big for the frame charges at a small fleeing child. Lesson: let the cropping carry the threat.
- **Grid Systems in Graphic Design (1981)**: a manual for grids of 8 to 32 fields, including three-dimensional grids. It argues that working to a grid means submitting to universal laws.

## Space & composition
- **The field is the unit, not the pixel.** Divide the format into n×m fields, with the gutter equal to one line of body leading, so text lines and module edges share a single vertical rhythm.
- **Asymmetry anchored to one strong axis.** Text hangs flush-left from a single vertical line, usually the second or third column, and nothing is centred. Half or more of the format is often empty or holds only the one geometric gesture.
- **Half-field offsets.** The 4.5-field-wide musica viva grid shows he used fractional modules to create tension. Shift one block by exactly half a field and leave everything else locked.
- **Scale jumps of 1:8 or more.** In der Film the headline letters are many times larger than the information text. Pair a huge element with tiny, precise detail and drop the middle sizes.
- **Bleed as meaning.** In Schützt das Kind the car runs off the frame because its scale is the message.

## Color
Color is functional and flat: one ground, one or two signals, no gradients. Hue codes structure, never mood.

| Role | Hex |
|---|---|
| Ground (print paper) | `#F2F0EA` |
| Ink / primary text | `#111111` |
| Signal red (Swiss / Tonhalle accent) | `#E2231A` |
| Cool secondary (musica viva blue) | `#1F5FA8` |
| Ghost layer (der Film grey) | `#8C8C8C` |
| Night ground (der Film black) | `#0A0A0A` |

Use at most three colors per screen. The grey is for depth, as a layer behind, never as a disabled state.

## Form, line & typography
His typeface of choice was Akzidenz-Grotesk: lowercase where possible, flush-left, ragged-right, never justified, and never more than two weights. His geometry is pure circles, arcs, bars and squares, built mechanically and shown without illustration. Size and position create hierarchy, not color or ornament.

Free fonts: **Inter** (closest neutral grotesk, use the tight display optical size), **Work Sans**, or **Archivo** for condensed headline weights.

## Rhythm, motion & time
The arcs in the Beethoven poster are a crescendo frozen on paper. In der Film the grey layer is "before" and the white layer is "now". So motion should **reveal the system rather than decorate it**. Elements enter along grid lines on a geometric timing series (80, 160, 320 ms, doubling each step), the way the arcs double. Use linear or strong ease-out curves, no bounce, no springs. A view change works like a montage cut: the old headline drops to 40% grey and stays visible behind the new white one for a beat before it clears.

## UI translations
1. **Layout:** Build a 6-column by 8-row CSS grid in which `row-gap` equals the body `line-height` (e.g. 24px), and size every card in whole fields.
2. **Layout:** Hang all text from one vertical axis at column 2. Columns 1 and 5–6 stay empty except for one geometric figure.
3. **Layout:** Offset exactly one block by half a field (`translateX(calc(var(--field)/2))`) to break the symmetry on purpose. Never offset two.
4. **Type:** Use two sizes per screen at a ratio of at least 1:6 (e.g. 14px and 96px), lowercase headlines, `letter-spacing:-0.03em` on display text, and `text-align:left` everywhere.
5. **Type:** Set the hero as a ghost word at 30vw in `#8C8C8C`, with the real title overlapping it in white at a quarter of that size, as in der Film.
6. **Color:** Use one flat ground, black ink and a single red signal reserved for the primary action and the current state. No tints, shadows or gradients.
7. **Graphic:** Generate one decorative SVG from a rule (concentric arcs at radius `r·2ⁿ`, or squares rotated in 15° steps), place it bleeding off the top-right edge, and let it behave as part of the grid.
8. **Motion:** Stagger entrances along columns at 80/160/320 ms with `cubic-bezier(.2,0,0,1)` and translate only along grid axes.
9. **Interaction:** On navigation, keep the previous screen's headline as a grey layer behind the incoming one for 300 ms (a montage cut), then fade it out.
10. **Imagery:** Crop photos so the subject overflows the frame (`object-fit:cover` with an off-centre `object-position`), with scale doing the talking.

## What this artist would reject
- Centred hero blocks with a centred CTA and a symmetric three-up feature row.
- Rounded "friendly" cards, soft drop shadows and glassmorphism, which simulate material where his work only measures.
- Spacing tokens chosen arbitrarily (13px here, 18px there) and not derived from the leading.
- Justified text, title case and more than two weights in a view.
- Gradient buttons and decorative color with no structural meaning.

## Signature prompt seed
Design this screen in the manner of Josef Müller-Brockmann. Lay a 6×8 modular grid whose gutters equal the body leading, and snap everything to it. Hang all lowercase Inter text flush-left from one axis in column two, using only two sizes at least 1:6 apart. Use an off-white ground, black ink and one signal red for the single primary action. Fill the empty half with one rule-generated figure, arcs doubling in radius, bleeding off the edge. Ghost the section word huge in grey behind the title. Animate on a doubling timing series along grid lines, with no shadows, rounding or ornament.

## Sources
- https://collection.cooperhewitt.org/objects/2318803418 (Beethoven, 1955)
- https://medium.com/fgd1-the-archive/beethoven-poster-by-josef-muller-brockmann-ce06940edf74
- https://www-4.collection.cooperhewitt.org/objects/18673705 (der Film, 1959–60)
- https://collection.cooperhewitt.org/objects/18673645 (Schützt das Kind!, 1953)
- https://openlab.citytech.cuny.edu/langecomd3504fa2019/files/2018/10/MullerBrockmann_Grid_Des-Phil.pdf
- https://www.slanted.de/?p=792761 (Grid Systems in Graphic Design)
- https://socks-studio.com/2016/11/30/joseph-muller-brockmann-musica-viva-posters-for-the-zurich-tonhalle/
- https://wikiwand.com/en/articles/Josef_Muller-Brockmann
