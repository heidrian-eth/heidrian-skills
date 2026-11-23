# Carlos Cruz-Diez — Kinetic / Op art (Venezuelan)

## Essence
Cruz-Diez treated color as an event, not a surface property. It happens between thin parallel bands, in the eye, and changes as the body moves, the light shifts, or the distance closes. His works produce colors that aren't physically there (red + green bands read as yellow), and each is completed only by someone walking past.

## Key works examined
- **Couleur Additive / *Additive Yellow*, 1959**: two lines, red and green, produce a yellow that isn't painted anywhere. Teaches that adjacency generates color.
- ***Physichromie 1*, 1959**: painted edges of red, green and white cardboard strips set in relief inside a frame. Color sits *on the edges* and blooms in the gaps between them.
- ***Physichromie 113*, 1963/1976**: adds reflective lumaline and one circle that cuts across the strips, so the change in color becomes legible. Teaches that one counter-form makes a field readable.
- ***Induction Chromatique n° 54. Bleu + Noir = Jaune*, 1973** (120 × 120 cm, Pompidou): an afterimage made permanent. Complementary "virtual" colors appear instantly instead of after you stare.
- ***Chromosaturation*, 1965/1968**: three walk-through chambers flooded with red, green and blue light that blend at the thresholds. Teaches that color can be architecture you enter.
- ***Ambientación de Color Aditivo*, Maiquetía airport, 1974–78**: about 2,925 m² of thin parallel floor bands whose combinations shift as travelers walk.
- ***Mural de Color Aditivo*, Guri hydroelectric plant, 1977–86**: 17 × 245 m. Shows that a stripe system can scale from 30 cm to 245 m without changing its rules.

## Space & composition
- **The field is the composition.** Works are near-uniform fields of vertical (or floor-parallel) bands that run edge to edge with no focal centerpiece. Hierarchy comes from *modules*: zones where the band sequence changes, not from objects placed on a background.
- **Extreme aspect ratios.** Guri is about 1:14, and Maiquetía is a runway. He designed for traversal, not a frontal viewpoint.
- **One intruder.** A single circle or diagonal across thousands of parallel lines (*Physichromie 113*) is the only "figure" allowed.
- **Depth through thin relief.** Physichromie blades project at right angles from the ground, so the surface has a z-axis only a few centimeters deep. That shallow depth does all the work.
- **Density over void.** There is almost no empty space. The bands are the space.

## Color
Additive, reflective, subtractive: narrow band pairs mix optically, transparent strips filter, reflection spills color onto neighbors. Keep bands at 2–6 px on screen so the eye mixes them. Black is an inducer, not a neutral.

| Hex | Role |
|---|---|
| `#E1252B` | Light-primary red (Chromosaturation chamber; additive partner) |
| `#14A04A` | Light-primary green (red's partner; together they induce yellow) |
| `#1E4FB8` | Light-primary blue (third chamber; inducer for virtual yellow) |
| `#0D0D0F` | Separator/inducer black, used for the thin lines between bands |
| `#F3F1EC` | White blade edge / reflective rest state |
| `#D8246F` | Magenta accent band (Physichromie and Maiquetía register) |
| `#F4C21F` | "Virtual" yellow, used sparingly as a real fill and mostly induced |

## Form, line & typography
The vocabulary is the straight parallel line at a strict pitch, with no curves except the rare intruding circle. Use tall, condensed, vertical-stressed type whose stems read as more stripes. Recommended fonts: **Big Shoulders Display** for headlines (narrow, stem-driven), **Archivo** (variable width; use the condensed axis for UI labels), and **IBM Plex Mono** for data, since its fixed pitch echoes his fixed band spacing.

## Rhythm, motion & time
The work moves only because *you* move. Drive animation by user input (scroll, pointer x, device tilt), not autoplay timers. Color is a continuous function of position, not a transition. Moving parallel to the field shifts hue, and moving toward it changes intensity, as the Tate notes for *Additive Yellow*. Thresholds between sections should blend, as at Chromosaturation's doorways, rather than cut.

## UI translations
1. **Layout:** Build hero and section backgrounds from `repeating-linear-gradient` bands at a fixed 4 px pitch running the full width of the viewport. Content sits on the field and never in a card.
2. **Color/parallax:** Put two band layers at different `translateY` speeds (e.g. 1.0× and 0.85× scroll), so their alignment, and the color that emerges between them, changes as the user scrolls.
3. **Color:** Never fill a large area with the target accent. Interleave 2 px red and 2 px green bands, and let the yellow appear optically. Reserve real `#F4C21F` for one critical action.
4. **Interaction:** Map `pointermove` x to a CSS custom property `--phase` that offsets one band set by up to half a pitch. The hover color of the whole surface drifts with the cursor.
5. **Motion:** Use scroll-driven animations (`animation-timeline: scroll()`) for color, with zero duration-based loops. If the user stops, the color stops.
6. **Navigation:** Treat sections as Chromosaturation chambers. Each route floods the viewport with one light-primary tint, and the boundary is a 20–30 vh gradient blend you scroll *through*.
7. **Type:** Set headlines in Big Shoulders Display at 10–14 vw with `letter-spacing: -0.02em`, so the stems become part of the stripe field. Clip the stripes to the text with `background-clip: text`.
8. **One intruder:** Allow exactly one non-orthogonal element per screen (a circle avatar or a single diagonal CTA) cutting across the band field.
9. **Relief:** Render list rows as "blades": a 1 px light top edge plus a colored right edge that only shows as rows parallax at slightly different rates.
10. **Floor-as-path:** In long flows (checkout, onboarding), run a narrow band strip along the bottom edge whose sequence advances with progress, like the Maiquetía corridor.

## What this artist would reject
- Static flat brand color applied as a 100% fill on large surfaces, which is color as paint rather than event.
- Time-based autoplay carousels and looping ambient gradients that move while the user is still.
- Shadowed cards on neutral gray; hierarchy should come from field modules.
- Gradient "glows" that fake mixing instead of producing it through adjacency.
- A frontal, fold-centered composition that assumes a single fixed viewpoint.
- Color that carries symbolic meaning ("green = success") instead of pure perceptual behavior.

## Signature prompt seed
Design the screen as a full-bleed field of thin vertical color bands at a strict 4 px pitch, with red and green interleaved so yellow appears optically and black hairlines acting as inducers. Two band layers parallax at different scroll speeds, so the field's color is a function of scroll position and pointer x, never a timer. Sections are chromatic chambers flooded with red, green or blue, blending across tall thresholds. Condensed stem-heavy headlines are clipped to the stripes. One circle interrupts the field. No cards, no shadows, no static flat fills.

## Sources
- https://tate.org.uk/research/tate-papers/32/carlos-cruz-diez-physichromies
- https://www.pamm.org/wp-content/uploads/2022/06/ccd-English-1.pdf
- https://www.centrepompidou.fr/en/ressources/oeuvre/cAgjk8M
- https://www.cruz-diez.com/works/physichromie-1959-2019/
- https://cruz-diez.com/works/induction-chromatique
- https://cruz-diez.com/works/monumental-artworks
- https://www.latintimes.com/venezuelas-iconic-airport-floor-became-symbol-migration-carlos-cruz-diezs-family-now-599083
- https://en.wikipedia.org/wiki/Carlos_Cruz-Diez
