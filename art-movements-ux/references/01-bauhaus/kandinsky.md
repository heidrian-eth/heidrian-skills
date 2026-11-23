# Wassily Kandinsky — Bauhaus

## Essence
Kandinsky treated the picture plane as a field of forces in which every point, line and colour has a temperature, a direction and a sound. At the Bauhaus he made this a teachable grammar: point, line, plane; triangle-yellow, square-red, circle-blue. Composition becomes orchestration: tuned dissonances held around one dominant circle.

## Key works examined
- **Composition VII, 1913** (Tretyakov): pre-Bauhaus maximal density, still readable because one centre-left vortex organises it.
- **Composition VIII, 1923** (Guggenheim): his first methodical colour–form painting, made at Weimar. A large black circle sits upper-left as an anchor, with sharp lines and triangles scattered across a cool, light ground.
- **Bauhaus questionnaire, 1923**: students matched three shapes to three primaries; a design system can start as a mapping table.
- **Yellow-Red-Blue, 1925** (Pompidou): warm angular yellow left, cool round blue right; one screen, two opposed temperatures.
- **Several Circles, 1926** (Guggenheim, 140.7 × 140.3 cm): about 30 overlapping translucent circles on a near-black square. It teaches layered transparency and hierarchy carried by size alone.
- **Point and Line to Plane, 1926** (Bauhaus Book 9): the "Basic Plane" (BP), whose edges and orientations carry weight and temperature. It shows that a layout canvas is never neutral.
- **Concerning the Spiritual in Art, 1911**: colour as instrument (yellow = trumpet, light blue = flute, dark blue = cello, white = pause). It supplies a ready vocabulary for sound and motion design.

## Space & composition
- **The canvas has a weather.** In *Point and Line to Plane*, horizontal reads as "cold rest" and vertical as "warm rest". Top is light and loose, bottom heavy; left is "airier", right compressed. A light element floats top-left and feels trapped bottom-right, so place content by urgency.
- **One dominant circle, many satellites.** Composition VIII and Several Circles both hang everything off a single large disc, offset from centre (roughly the upper-left third). Smaller elements orbit it at 1/3 to 1/12 its diameter.
- **Diagonals carry the drama.** The structure is a lattice of crossing diagonals, not a column grid. Lines start at a point and end in empty space.
- **Density is uneven, never uniform.** Clusters sit beside open fields, with roughly 40% of the plane left as breathing ground. The ground is a tinted field, cream or near-black, not white.

## Color
Temperature plus movement. Yellow pushes outward (eccentric, sharp, acute angles); blue pulls inward (concentric, calm, the circle); red is the steady, earthbound square. White is a silence before sound, black a final silence. Gray is soundless, so avoid it as a working neutral.

| Role | Hex | Note |
|---|---|---|
| Ground (light mode) | `#EFE6D2` | warm parchment, not white |
| Ground (dark mode) | `#14161C` | Several Circles near-black |
| Primary action / alert | `#F2C230` | trumpet yellow, triangle |
| Structure / commit | `#C8322B` | earth red, square |
| Focus / calm / selected | `#1F4FA3` | cello blue, circle |
| Accent line | `#1A1A1A` | thin black linework |
| Secondary harmony | `#7A4E9C` | violet, bassoon, rare |

Keep yellow rare (under 5% of area). Let blue take the largest coloured mass.

## Form, line & typography
A line is the track of a moving point: straight lines are tense, curves lyrical, zigzags high-pitched. In type, a geometric sans with a true-circle "o" is the circle; a sharp display face is the triangle. Dividers are hairlines (0.75–1px) that stop short and never close a box.

Fonts: **Jost** (Futura-like Bauhaus geometric, for body and UI), **Syne** (angular, eccentric display for headlines), **Space Mono** (for "point"-like numerals and data labels).

## Rhythm, motion & time
Treat motion as instrumentation:
- **Yellow/triangle elements** move fast and outward: 120–160ms, `cubic-bezier(.2,.9,.3,1.4)` with a slight overshoot, scaling up.
- **Blue/circle elements** move slowly and inward: 400–600ms, ease-in-out, scaling down and settling toward the centre.
- **Red/square elements** don't bounce. They translate on a single axis and stop dead.

Pace interactions with rests: a white "pause" of 200ms or more after each burst. Stagger lists in a musical meter (3+2 beats), not an even 50ms cascade.

## UI translations
1. Build a shape–colour token table: `--alert: triangle/yellow`, `--commit: square/red`, `--focus: circle/blue`. Never mix pairs.
2. Anchor each screen with one large circle (avatar, progress ring, hero disc) at 35–50% of viewport width, centred about 30% from top and left. Arrange content as satellites around it.
3. Run one key divider or progress path as a 1px diagonal (8–20°) across the layout, not horizontal.
4. Set light-mode grounds to `#EFE6D2` and dark-mode grounds to `#14161C`. Forbid pure `#FFFFFF` and neutral grays as surfaces.
5. Make overlapping cards translucent (`mix-blend-mode: multiply`, 70–85% opacity) so the overlaps produce new colours, as in Several Circles.
6. Put calm, reading content top-left and urgent, compressed content (CTAs, warnings) bottom-right, where the plane is heaviest.
7. Animate primary CTAs with a fast eccentric scale-out; animate selection and focus with a slow concentric scale-in ring.
8. Pair Syne headlines with Jost body. Set one headline word at 3–4× body size and rotate it −6°.
9. Map sound to colour: confirmation is a low soft "cello" tone, an alert is a short bright "trumpet" ping, a disabled tap is silent.
10. Leave at least one quadrant nearly empty except for a single 8–12px dot. That is the "point", silence with speech.
11. On hover, let lines extend from points (draw with `stroke-dashoffset`) toward the cursor, so the user's movement turns points into lines.

## What this artist would reject
- Neutral gray UI chrome. Gray is "soundless immobility".
- Centred, symmetrical hero sections with a uniform 12-column rhythm.
- Colour used only as brand decoration, with no meaning attached to form.
- Rounded rectangles for everything. Shape should signal a role (circle, square or triangle), not be a default radius.
- Even, metronomic stagger animations and identical easing on every element.
- Pure white backgrounds treated as "nothing". White is an active pause.

## Signature prompt seed
Design this screen as a Kandinsky Bauhaus composition. Start from a warm parchment (or near-black) basic plane, then hang everything off one dominant blue circle offset to the upper-left. Map role to shape and colour strictly: yellow triangles for alerts, red squares for commitments, blue circles for focus. Cross the layout with one or two hairline diagonals that start at dots and end in empty space. Leave one quadrant silent. Overlaps are translucent. Typography is Jost with angular Syne accents. Motion is orchestral: yellow snaps outward fast, blue settles inward slowly, and rests sit between phrases.

## Sources
- https://www.britannica.com/topic/Composition-VIII
- https://artsandculture.google.com/story/OwURAJwcVUkTow
- https://www.getty.edu/research/exhibitions_events/exhibitions/bauhaus/new_artist/form_color/form/
- https://bauhaus-bookshelf.org/bauhaus-book-9-vassily-kandinsky-point-and-line-to-plane_pdf.html
- https://artincontext.org/several-circles-by-wassily-kandinsky/
- https://artsandculture.google.com/story/a-life-imbued-with-music-the-centre-pompidou/iAWhbiSy_2YBig?hl=en
- https://www.mat.ucsb.edu/g.legrady/academic/courses/12w259/Kandinsky_ Color Theory.pdf
