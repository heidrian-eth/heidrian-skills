# Alexander Rodchenko — Constructivism

## Essence
Rodchenko treated every surface as a device that does a job, and every viewpoint as one he could change. He pushed painting to its end (three flat primaries) and then moved the same geometry into posters, furniture, and the camera. The result is a hard diagonal, a low or high angle, a few stock parts that fold into several uses, and no decoration.

## Key works examined
- **Spatial Construction no. 12, c. 1920**: nested ovals cut from one plywood sheet and rotated into 3D. It hangs with no top, bottom, or base. Lesson: build depth from one flat plane, rotated.
- **Pure Red Color, Pure Yellow Color, Pure Blue Color, 1921**: three monochrome canvases shown at *5x5=25*, which he called the end of painting. Lesson: a full flat field of one color is enough.
- **Lengiz "Books in All Branches of Knowledge" poster, 1924** (text by Mayakovsky): Lilya Brik shouts through a cupped hand, and a megaphone-shaped wedge of type comes out of her mouth. Lesson: the type is the voice, and it projects along a vector.
- **Workers' Club, Paris 1925**: Ripolin enamel in red, white, and grey, with black only on the chess table. It had fold-out tables, a rotating chessboard, and rotating hexagonal display drums. Lesson: components change state, and color marks the zones.
- **Miasnitskaya Street building series, 1925**: shot straight up and straight down at his own apartment block. Lesson: tilting the viewpoint makes ordinary things look strange.
- **Girl with a Leica, 1932–34**: raking bench shadows cut across the figure and the angle confuses depth. Lesson: overlay a diagonal pattern across content.

## Space & composition
- **Diagonals, mostly 30–45°.** He tilted the photo frame, the poster's speech wedge, and the edges of the planes. The page's main axis runs corner to corner, not across and down.
- **Angles from far above or below.** Layout can do the same: an oversized element seen "from below" (huge, cropped at the top) set against tiny UI "seen from above."
- **Zones by color.** In the club, wall color plus a stencilled word ("Library," "Lenin") marked each zone. Sections get a solid ground and a capitalized label, with no icons.
- **Dense and useful.** No empty space for luxury's sake. Any empty area is a flat field doing work, as in the triptych.

## Color
Mostly red, black, and paper. Primaries appear only as full, flat fields, never as tints. Aluminum grey is borrowed from the constructions and the club's walls.

| Hex | Role |
|---|---|
| `#D7261E` | Signal red: main action, wedges, active zone |
| `#141414` | Ink black: type, bars, one "opponent" element |
| `#EEE8DA` | Newsprint off-white: default ground |
| `#8E9196` | Enamel/aluminum grey: secondary zones, disabled |
| `#F3C318` | Pure yellow: one full-bleed field per flow, max |
| `#1D4C9E` | Pure blue: one full-bleed field per flow, max |

Do not use gradients or opacity ramps. Each color fills its whole area or isn't used.

## Form, line & typography
Hand-drawn, condensed, heavy sans capitals, stacked, slanted, and sized to fill whatever bar or wedge holds them. Rules are thick bars, not hairlines. Use circles only as targets or lenses, like the Leica lens or the eye in the Kino-Glaz poster.
Fonts: **Oswald** (condensed headlines), **Russo One** (squared display), **IBM Plex Mono** (labels and data, the "technical drawing" voice).

## Rhythm, motion & time
- Motion is mechanical. Things rotate on a pivot, slide on a track, or unfold along a hinge. They don't float or bounce. Use `cubic-bezier(.7,0,.3,1)` at 180–260 ms with no overshoot.
- Things change state rather than appear. A card opens into a form the way the club table doubles. A display flips through faces like the hexagonal drums (`rotateX` in 120° steps).
- Transitions are diagonal wipes along the composition's axis, like a megaphone blast.

## UI translations
1. **Layout:** rotate the hero container −12° to −18° and let it bleed off two edges. Keep body text horizontal underneath for contrast.
2. **Layout:** crop the main image to an extreme angle seen from below, with the subject cut at the top edge and taking up 70% of the viewport height.
3. **Type:** set the screen's one key word in condensed caps sized to fill a red wedge (`clip-path: polygon(0 40%,100% 0,100% 100%,0 60%)`) coming out of the image toward the CTA.
4. **Type:** stack nav labels vertically, rotated 90°, in a black bar 48px wide on the left.
5. **Color:** give each section a single flat ground (off-white, red, grey). Introduce yellow or blue only as one full-screen state, such as success or empty.
6. **Color:** keep black for one "opponent" element per screen, like the club's chess pieces: the destructive action or the active tab.
7. **Component:** make one base panel and derive the others by rotating it or nesting copies at 0.8× scale, with no new shapes.
8. **Interaction:** cards expand in place along a hinge (`transform-origin: left`) to 2× or 3× width and reveal form fields. Don't use modals.
9. **Interaction:** let stats or features sit on a three-faced prism that turns 120° on click or swipe.
10. **Motion:** do page transitions as a 35° diagonal wipe in red, 220 ms, linear-in / hard-stop.
11. **Labels:** mark zones with stencilled uppercase words ("LIBRARY," "ANNOUNCEMENTS") set at 2× body size instead of icons.

## What this artist would reject
- Ornamental gradients, glassmorphism, and soft drop shadows: they decorate a surface without doing anything.
- Eye-level, centered stock photography: the "navel-height" view he worked against.
- Static furniture-like components with a single use, such as a card that can only link.
- Pastel or tinted brand palettes that dilute the primaries.
- Spring or bounce animations that are playful but not mechanical.

## Signature prompt seed
Design this app screen as Rodchenko's 1925 club furniture in Lengiz-poster colors. Use a newsprint off-white ground, signal red, ink black, and enamel grey. Pure yellow or blue appear only as one full-bleed state. Tilt the hero 15°, cropped from an extreme low angle, and fire the key word out of it as condensed caps inside a red megaphone wedge. Mark zones with stencilled capital labels on flat color. Components are standard modules that hinge, fold, or rotate open in 220 ms mechanical eases. No gradients, no soft shadows, no centered symmetry, nothing purely decorative.

## Sources
- https://www.moma.org/collection/works/81043
- https://www.moma.org/interactives/exhibitions/1998/rodchenko/texts/death_of_painting.html
- https://www.moma.org/interactives/exhibitions/1998/rodchenko/texts/photography.html
- https://www.moma.org/interactives/objectphoto/assets/essays/Lodder.pdf
- https://en.wikipedia.org/wiki/Workers%27_Club_(Alexander_Rodchenko_work)
- https://olk.pushkinmuseum.art/data/graphics/gr_2213_rodchenko_lengiz.php?lang=en
- https://elephant.art/the-memeification-of-rodchenkos-iconic-soviet-portrait-lilya-brik-14102020/
