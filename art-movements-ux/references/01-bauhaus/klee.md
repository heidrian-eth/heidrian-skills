# Paul Klee — Bauhaus

## Essence
Klee treated a picture as a small machine for growing form: a dot moves and becomes a line, the line closes into a plane, planes are tiled into a grid of slightly-off squares, and colour is stepped across that grid like notes on a stave. Everything rests on a strict, teachable system, yet the result is small, wry and handmade, with a pictographic wit (arrows, suns, stick birds) laid over it.

## Key works examined
- **Pedagogical Sketchbook (Bauhausbuch 2), 1925.** Distilled from about 3,900 pages of lecture notes, it runs point, line, plane, balance, gravity, then colour and motion. It teaches growth as a sequence of operations.
- **Twittering Machine, 1922 (MoMA).** Oil transfer, watercolour and ink, 64.1 × 48.3 cm. Wire-thin birds on a sine-wave branch ending in a crank, over a blue-to-pink wash: hairline over gradient.
- **Static-Dynamic Gradation, 1923 (Met).** Oil and gouache, 43.5 × 29.2 cm. Rectangles step from dark edges to a light core: gradation as structure.
- **Ancient Sound, Abstract on Black, 1925.** Oil on cardboard, about 15 in. square. Muted squares on black, bright cells pulsing: the magic square as colour score.
- **Castle and Sun, 1928.** Stacked rectangles, triangles and one red disc: modules read as a city.
- **Ad Parnassum, 1932 (Kunstmuseum Bern).** Oil, 100 × 126 cm. Muted squares, then stamped small white and tinted squares, then stamped lines tracing a pyramid and orange sun: polyphony as layers at different scales.

## Space & composition
- **The grid wobbles.** Klee's "magic squares" are a near-regular grid of roughly 8–12 columns. The cells vary by ±10–20% in width and none are perfectly square. Tracks should look hand-ruled, not snapped to a framework.
- **Structure first, then figure.** The ground is a full tiling, with no empty margin. The figure (a pyramid, a sun, an arrow) is drawn *over* the tiling as a hairline, so it never knocks cells out.
- **Polyphonic layering.** Ad Parnassum uses three strata. Large blocks, about 1/8 of the width, make the bass. Small stamped squares, about 1/60, are the melody. Linework is the voice.
- **Framed small.** Painted borders (about 4–8% of the short side) make works read as cards, not full-bleed spreads.
- **Balance by counterweight, not symmetry.** The tightrope walker and the black arrow of gravity are the model. One heavy accent (a red disc, a single arrow) balances a whole field.

## Color
The logic is gradation plus one outlier. Hues step through 5–9 near-neighbour values across the grid, from dark at the edges to light at the core, or warm to cool. Then a single saturated note breaks the series. Colour is also motion: Klee pictured it travelling between pure black and pure white.

| Hex | Role |
|---|---|
| `#1E1B24` | Night ground (Ancient Sound black, slightly violet) |
| `#4F6D8A` | Cool mid-field / twilight blue |
| `#B9A27C` | Ochre base cell, the dominant "bass" tone |
| `#D9C9A8` | Pale sand step / surface |
| `#E7B9B0` | Dawn pink gradient end (Twittering Machine) |
| `#C8452C` | The single sun: accent, CTA, active state |
| `#F4EEE2` | Stamped white dots / text on dark |

Generate tile steps with `color-mix(in oklch, #B9A27C, #4F6D8A N%)` at N = 0, 12, 25, 37, 50.

## Form, line & typography
Klee's line is a single unbroken monoline stroke that wanders. It loops, zigzags and ends in arrows or tiny pictograms, and its thickness never changes. Type should feel drawn with the same pen: slightly naive, geometric, not engineered. Use **Josefin Sans** for headings (its 1920s geometric vintage fits), **Gaegu** or **Patrick Hand** sparingly for annotations, and **Karla** for body text. He painted letters as image elements, so a display character can sit in a grid cell like a tile.

## Rhythm, motion & time
His motion models are the pendulum, the spinning top, darting aquarium fish and the line "on a walk."
- **Lines draw on.** Animate SVG paths with `stroke-dashoffset` at a slow, slightly irregular pace (900–1400 ms, `cubic-bezier(.3,.1,.3,1)`), as if being drawn.
- **Grid cells step tone in sequence**, staggered 30–40 ms in reading order like an arpeggio, never all at once.
- **Pendulum ease.** Settle interactive feedback with one damped overshoot, not a spring wobble.
- **Counterpoint.** Dots drift slowly while blocks stay still.

## UI translations
1. Build the page background as a CSS grid of 8–12 tinted tiles whose `grid-template-columns` use unequal `fr` values (`1.1fr .9fr 1fr 1.2fr…`), not a flat colour.
2. Draw the primary navigation path (onboarding progress, a breadcrumb, a step flow) as one continuous 1.5px SVG line that "walks" between steps and ends in an arrowhead.
3. Tint cards from a 5-step `oklch` ramp. The card nearest the user's focus is lightest and the rest darken toward the edges.
4. Allow exactly one saturated element per screen (`#C8452C`, ideally a circle). Everything else stays in the muted gradient.
5. Use arrows as semantic glyphs. A heavy black downward arrow marks destructive or "sink" actions. A thin feathered arrow marks forward or creative actions.
6. Layer polyphonically. Put a dot texture (`radial-gradient` at 6–8px pitch) over the tile layer, then hairline icons on top, with deliberately different spacing on each layer.
7. Frame key panels with a 6% inset painted border (`outline` plus a contrasting `padding` band) so they read as small framed works.
8. Set headings in Josefin Sans at modest sizes (no larger than 2.5rem) and put hand-drawn annotations in the margins.
9. On hover, let a cell step one tone lighter and grow a pictogram (sun, eye, bird) in a hairline stroke.
10. Animate loaders as a dot that becomes a line that closes into a square. Point, line, plane in about 1.2s.

## What this artist would reject
- Perfectly uniform 12-column grids with identical card sizes.
- Flat single-hue surfaces with no tonal steps.
- Multiple competing accent colours and a gradient on every button.
- Heavy, filled, rounded-blob icon sets (he drew with a thin, inquisitive line).
- Bouncy spring physics and decorative motion with no growth logic.

## Signature prompt seed
Design this app screen as a Klee "magic square." Lay a hand-ruled grid of 8–12 unequal tiles stepping in muted ochre-to-twilight-blue gradation across the whole background, darker at the edges and lighter toward the content. Over it, run independent layers: a fine stamped dot texture, then hairline monoline icons and one continuous wandering line that links the steps of the task and ends in an arrow. Allow a single red-orange sun as the primary action. Use modest geometric type in a framed, intimate card. Paths draw themselves on, and tiles brighten in staggered arpeggios.

## Sources
- https://www.thecollector.com/what-was-paul-klee-pedagogical-sketchbook/
- https://en.wikipedia.org/wiki/Pedagogical_Sketchbook
- https://metmuseum.org/art/collection/search/484862
- https://www.moma.org/collection/works/37347
- https://en.wikipedia.org/wiki/Twittering_Machine
- https://en.wikipedia.org/wiki/Ad_Parnassum
- https://www.artchive.com/artwork/ancient-sound-abstract-on-black-paul-klee-1925/
- https://mymodernmet.com/paul-klee-art-and-music
