# Le Corbusier — Modernist architecture

## Essence
Le Corbusier treated a building as a measured system you move through: a body-based proportion scale (the Modulor), a structural grid that frees walls from loads, and a choreographed path (the *promenade architecturale*) turn white volumes into a timed sequence of views. Color and light are spatial tools that push planes forward, pull them back, or open a wall into a lantern.

## Key works examined
- **Villa Savoye, Poissy (1928–31).** White box on pilotis; a ramp rises from the hall to the salon, the roof terrace and a curved solarium. Teaches: one continuous path as the main structure.
- **Five Points (1926).** Pilotis, roof garden, free plan, ribbon windows, free facade. Teaches: once structure is separate from skin, every partition is optional.
- **Le Modulor (1948; Modulor 2, 1955).** A 1.83 m figure, 2.26 m with raised arm, 1.13 m navel; two golden-ratio series, red (navel) and blue (double the navel). Teaches: two linked scales instead of one linear scale.
- **Notre-Dame du Haut, Ronchamp (1953–55).** A south wall tapering from a point to about 3 m thick, pierced by irregular splayed openings with clear and red, green and yellow glass; a few-centimeter light slot under the heavy roof. Teaches: light as the event, mass as the frame.
- **Polychromie Architecturale (1931, 1959).** 43 "purist" shades in 14 series, plus 20 stronger ones in 1959 (63 total), grouped into keyboards (*claviers*) to be played in combination. Teaches: a palette is a set of permitted chords.

## Space & composition
- **Grid as structure, not as walls.** Villa Savoye sits on a regular column grid (cut from 5 m to 4.75 m to save money), while the walls move freely around the columns. A strict 4-column grid carries the content, and panels ignore column edges. One curved partition, like the solarium, meets the orthogonal frame.
- **The piloti lift.** The main volume floats above a recessed ground: a visible gap plus a darker, set-back base band, never a drop shadow.
- **Ribbon over punch.** Openings are long horizontal strips (roughly 1:6 to 1:8), not portrait holes.
- **Dual-scale spacing.** Red series in px (rounded): 6, 10, 16, 26, 42, 68, 110. Blue series: 12, 20, 32, 52, 84, 136. Red sets tight internal spacing and blue sets structural gaps. Never use a value outside these two scales.

## Color
Polychromy is spatial: light tones widen, dark tones deepen and focus. One flat color per surface, white dominant. Hex values approximate the Les Couleurs codes.

| Role | Name (code) | Hex |
|---|---|---|
| Ground (about 60%) | blanc (32001) | `#FFF1CE` |
| Receding plane / secondary panels | gris clair 31 (32013) | `#B5B5AF` |
| Deep receding wall | bleu outremer 59 (4320K) | `#395A8E` |
| Advancing accent (one per view) | rouge vermillon 59 (4320A) | `#A33A29` |
| Warm mid-plane | ocre jaune clair (4320L) | `#F2B573` |
| Calm field | vert anglais pâle (32042) | `#C6D4BD` |
| Text / pilotis base | ombre naturelle 59 (4320R) | `#333230` |

Logic: blue and gray recede (back panels); red and ochre advance (the one nearest plane). Each screen plays one chord: at most 3 colors plus white.

## Form, line & typography
Orthogonal volumes cut by one free curve; thin columns against thick slabs. Le Corbusier's drawings and signage used stencil capitals (engineer lettering with broken strokes). Map it to a geometric sans for body and stencil caps for labels and numbers, tracked about +8%.
- **Jost** (Futura-like geometric sans) for body and UI.
- **Big Shoulders Stencil Display** or **Stardos Stencil** for section numbers and wayfinding labels.
Set type sizes from the red series (10/16/26/42/68), so the type scale and the spacing scale are the same scale.

## Rhythm, motion & time
Motion follows a ramp, not an elevator: translate on a 6–8° diagonal with near-linear easing (`cubic-bezier(.3,.1,.3,1)`), 500–700 ms. Each stage reveals a framed view, as the Savoye ramp turns back on itself to reframe the landscape. Light moves slowly. On Ronchamp-style screens, colored glints drift over 10–20 s as ambient motion, never as a reaction to clicks.

## UI translations
1. Build all spacing and type from two Modulor-derived px series (red and blue), stored as CSS custom properties. Ban all other values.
2. Run a fixed 4-column structural grid, but let panels sit off the column lines. Make exactly one panel a curved shape (a large `border-radius` on one side only).
3. Raise the primary content block on a recessed base band in ombre `#333230`, with a blue-series gap of 32–52 px between them. No shadows.
4. Replace hero images with one full-width ribbon at about 1:7 that frames a horizontal view.
5. Make navigation a promenade: one continuous scroll path whose sections switch back (left, right, left), each revealed by a ramp-angle transition.
6. Give each surface exactly one flat Polychromie color. Use blue or gray for anything meant to recede and a single vermillion plane for the nearest element.
7. Build a "thick wall" sidebar (about 30% width) pierced by 5–9 openings of unequal size (thumbnails or CTAs) with bevelled inner borders and red, green or yellow tints at 15–25% opacity.
8. Separate the header from the body with a light gap only 4–6 px high in `#FFF1CE`, so the top bar seems to float the way Ronchamp's roof does.
9. Hover: increase light, not size. Brighten the tint of the hovered opening and leave its dimensions alone.
10. Use a free facade: each breakpoint gets its own composition based on orientation, not a stacked copy of the desktop layout.

## What this artist would reject
- 8-pt spacing systems with no relation to the human body.
- Gradients and glassy blur that leave a plane with no one color.
- Equal-weight card grids where nothing advances or recedes.
- Elevator UX: hard page cuts and modals that teleport the user with no path.
- Decorative drop shadows imitating mass, instead of real lift and void.
- Portrait-punched images scattered without a structural grid.

## Signature prompt seed
Design this screen as a promenade architecturale. A warm-white `#FFF1CE` field sits on a 4-column structural grid, and panels drift free of the columns, with one curved like a solarium. All spacing and type come from Modulor red (6/10/16/26/42/68) and blue (12/20/32/52/84) series. The main volume floats above a dark umber base band. One full-width ribbon window frames imagery. Each plane gets one flat Polychromie color: ultramarine and gray recede, a single vermillion plane advances. Stencil caps label each stage. Sections switch back left and right and reveal through a slow, ramp-angled transition.

## Sources
- https://en.wikipedia.org/wiki/Modulor
- https://en.wikipedia.org/wiki/Villa_Savoye
- https://smarthistory.org/?p=1954
- https://en.wikipedia.org/wiki/Notre-Dame_du_Haut
- https://en.wikipedia.org/wiki/Le_Corbusier%27s_Architectural_Polychromy
- https://www.lescouleurs.ch/en/the-colours/colour-system
- https://gist.github.com/oelna/743be12076895e2c2d662c631f34ec97
