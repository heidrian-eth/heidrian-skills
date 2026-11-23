# James Turrell — Light and Space

## Essence
Turrell treats light as a physical material and perception itself as the medium. His work holds no objects or images. It is a field of color held by an edge so thin it seems to vanish. Over minutes, the viewer finds that the "flat" plane is actually depth, or that the depth is a flat plane. He has said he wants you to "sense yourself sensing" (Smithsonian).

## Key works examined
- **Afrum I (White), 1967**: projected light that reads as a solid cube in a corner. Light at a precise edge becomes an object.
- **Skyspaces, e.g. The Color Inside (UT Austin, 2013, his 84th)**: a sharp ceiling aperture flattens the sky into a plane. At sunrise and sunset, hidden LEDs recolor the room, and that shifts how the sky looks.
- **Breathing Light (LACMA, 2013), a Ganzfeld**: an all-white room with rounded corners, so the eye finds no edge to measure depth by. It teaches that removing edges removes depth.
- **Aten Reign (Guggenheim, 2013)**: five elliptical rings of LED light and daylight stacked inside Wright's rotunda. The space reads as flat at one moment and as a deep funnel the next.
- **Roden Crater (Arizona, since 1977)**: a tunnel nearly three football fields long climbs to an elliptical portal that looks circular from one spot. It teaches reveal by stages.

## Space & composition
- **One field and one aperture.** A Skyspace is a large neutral surface with one cut-out where everything happens. Let roughly 70–85% of the screen be one continuous tone, with a single inset "aperture" at about 38% of the shorter side.
- **The knife edge.** Turrell bevels the aperture until its edge has no thickness, so the sky looks pasted onto the ceiling. In UI, a container should have no border or shadow, only a value step between two flat fills.
- **Edges either cut or dissolved.** Ganzfeld rooms curve corners away, and Skyspaces sharpen one edge to infinity. Pick one per screen: a razor-cut panel, or a field whose edges fade (`mask-image: radial-gradient`).
- **Concentric and centered.** Aten Reign and the Crater portal are nested ellipses. Nest 3–5 rings of slightly different value and put content in the innermost one.

## Color
The logic is simultaneous contrast. The same sky reads as navy against a warm wall and as grey-violet against a cool one, so the frame color controls the content color. Color is emitted, not painted. The Aten Reign sequence ran from moon white and dusk pink through orange, lilac, violet and yellow to grey twilight (Domus).

| Role | Hex |
|---|---|
| Ganzfeld field / base surface | `#F2EEF3` |
| Twilight grey (neutral frame, text-on-light) | `#8C8A97` |
| Aperture sky (primary accent) | `#3B4FB8` |
| Dusk pink (warm frame state) | `#E9A3B9` |
| Lilac-violet (transition midpoint) | `#9B7FD1` |
| Sodium amber (rare alert, the "sunset" hit) | `#F2A541` |
| Crater night (dark mode field) | `#14131C` |

Build states as frame/aperture pairs. Animate the frame and leave the content color fixed; its apparent color will change anyway.

## Form, line & typography
There is no lettering in Turrell's work, so type should behave like the knife edge: thin, quiet, light rather than ink. Use large sizes at weights 200–300, tracked +0.02em, in soft values that still pass contrast. Shapes are rectangles, circles and ellipses with no outline. Fonts: **Jost** at weight 200 for display (its circular geometry echoes the oculus), **Manrope** at 300–400 for body, and optionally **IBM Plex Mono** at 300 for time readouts.

## Rhythm, motion & time
Turrell's time is slow. Skyspace programs last as long as a sunset, and Ganzfeld color changes too slowly to see as it happens. You notice only after it has changed.
- Run ambient color transitions over 30–120 s, linear, below the threshold of noticing.
- Make interaction transitions 600–1200 ms color and opacity fades, with no translate, scale or bounce. Light changes intensity; it does not slide.
- Procession: at Roden, the sky grows from a small disc as you walk. Drill-downs should open the aperture step by step.
- Tie the palette to the real sun (local sunrise and sunset times).

## UI translations
1. Make one flat field fill at least 75% of the viewport and place all primary content in a single borderless inset aperture.
2. Define every container only by a value step of 4–8% lightness. Use no `border`, no `box-shadow` and no `outline` except a focus ring.
3. Give hero and empty states an ellipse of 3–5 nested rings, each about 3% lighter than the one outside it, with content in the core.
4. Slowly animate the frame's `background-color` over 60 s through dusk pink, lilac and twilight grey, and keep the foreground static so contrast does the work.
5. Fade the canvas edges into the field with a radial mask so the screen has no visible edge, Ganzfeld-style.
6. Set headings in Jost 200 at 2.5–4rem and body in Manrope 300. Never use bold. Use size and luminance for hierarchy.
7. Animate hover only through luminance: raise the element's lightness by 6% over 400 ms, with no lift, shadow or scale.
8. Make drill-down navigation a procession: the selected item's aperture grows from 20% to 100% over 900 ms while the surrounding field dims.
9. Use colored light for state. Errors and success tint the whole field for 2 s rather than appearing as small red or green badges.
10. Ship a "dark adaptation" entry: for the first 1.2 s the bare field shows, then content resolves in.

## What this artist would reject
- Drop shadows and elevation layers. They are fake physical depth where perceptual depth should be.
- Card-grid dashboards with no dominant field.
- Snappy 150 ms spring animations and bouncing micro-interactions.
- Hairline borders and dividers. They give the eye the edges Turrell works to remove.
- Glassmorphism with visible highlights. In Turrell's work the light source is always hidden.

## Signature prompt seed
Design this screen as a Turrell Skyspace. One flat, softly lit field (#F2EEF3) fills most of the viewport, with edges dissolving into a radial fade. Cut a single borderless elliptical aperture, defined only by a value step, and put the task inside it. No shadows, borders, bold or icons. Hierarchy comes from luminance and size alone (Jost 200 headings, Manrope 300 body). The frame drifts through dusk pink, lilac and twilight grey over sixty seconds while the content stays fixed. Every interaction is a slow change in light, never a movement.

## Sources
- https://www.architecturalrecord.com/articles/2914-exhibition-review-james-turrell-at-the-guggenheim
- https://domusweb.it/en/art/2013/07/3/james_turrell_ateinreign.html
- https://www.lacma.org/art/exhibition/james-turrell-retrospective
- https://www.dunnedwards.com/?p=4177
- https://landmarks.utexas.edu/artwork/color-inside
- https://www.smithsonianmag.com/arts-culture/james-turrells-light-fantastic-81570846/
