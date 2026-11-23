# Dan Flavin — Minimalism

## Essence
Flavin arranged off-the-shelf fluorescent fixtures so the tubes matter less than the colored light they throw onto walls, floors and corners. Each work is a "situation", not a sculpture: the room it lights is part of the piece. With a fixed kit (four lengths, ten colors), all his invention went into placement, orientation and where the light overlaps.

## Key works examined
- **the diagonal of May 25, 1963 (to Constantin Brancusi), 1963.** One yellow tube on the wall at 45°. A single part at an unexpected angle turns the whole wall into a composition.
- **"monument" 1 for V. Tatlin, 1964.** White tubes stepped into an 8-ft form, the first of 39 "monuments", echoing Tatlin's unbuilt tower: a heroic idea from stock parts.
- **greens crossing greens (to Piet Mondrian who lacked green), 1966.** His first full installation. Green fixtures crisscross the room in the one color the grid painter left out.
- **untitled (to you, Heiner, with admiration and affection), 1973.** A barrier of 70 identical 48 × 48 in units. A glowing fence you can see through but not walk through.
- **untitled (Marfa project), 1996–2000.** Six U-shaped buildings whose corridors are closed by full-height barriers of 8-ft fixtures, each holding two colors facing opposite ways (pink/green, yellow/blue, then all four).
- **untitled, Santa Maria Annunciata in Chiesa Rossa, Milan, 1996–97.** His last work: green and blue in the nave, red in the transept, gold-yellow in the apse. Color marks out the zones of the building.

## Space & composition
- **The fixture sits on the edge and the light fills the field.** Tubes hug baselines, corners and doorframes. The middle of the space holds only tinted air.
- **Corners are the stage.** Corner pieces sit in the 90° fold, where the two walls catch light unevenly, which gives a built-in gradient from bright seam to dim edge.
- **A fixed set of parts.** Only 2, 4, 6 and 8 ft lengths (circles from 1972), a 1:2:3:4 ratio. Variety comes from count and orientation, never custom sizes.
- **Barriers and corridors.** Repeated units stop or channel movement (his first corridor dates from 1973), with see-through spacing: a wall made of gaps.
- **Two faces.** At Marfa, space reads differently depending on which side you approach from.

## Color
Flavin's palette was simply the catalog: red, blue, green, pink, yellow, ultraviolet and four whites. These colors are emitted, so they **add up**: overlapping pink and green light on a wall makes a pale, near-white blend no paint could make. Saturation peaks at the source and fades with distance.

| Role | Hex | Note |
|---|---|---|
| Wall / ground (light off) | `#1A1B1E` | dim gallery grey, the surface that receives light |
| Daylight white (primary emitter) | `#F2F7FF` | cool, slightly blue tube |
| Warm white (secondary emitter) | `#FFF1D6` | for calm, resting states |
| Fluorescent green | `#5BFF7A` | the "Mondrian lacked" green; strongest field |
| Pink | `#FF6FB5` | complementary partner to green |
| Gold-yellow | `#FFD23F` | the diagonal and the apse |
| Ultraviolet | `#6B3CFF` | sparse; reads as a deep dark violet |

## Form, line & typography
The basic mark is a uniform rod: constant width, rounded ends, no taper. Type should match: **monoline, narrow, rational** letterforms that look extruded rather than drawn. Flavin titled works in lowercase with a dedication in parentheses ("untitled (to …)"), a quiet, parenthetical way of labeling. Fonts: **Barlow Condensed** (rod-like verticals), **IBM Plex Mono** (catalog/spec tone for metadata), **Archivo Narrow** (body).

## Rhythm, motion & time
Motion should be **ignition, not travel**. Elements don't slide in. They switch on with a short flicker (two or three opacity blips in about 120 ms), and the halo blooms afterward over 400–600 ms. Repeated units light one by one at a 40 ms stagger, like fixtures warming up. On exit, the halo fades before the rod.

## UI translations
1. **Layout:** Draw structure only along edges, with a 3–4 px glowing bar on the left or bottom margin instead of boxed cards.
2. **Layout:** Restrict every divider and bar to four lengths (25/50/75/100%), echoing the 2-4-6-8 ft tubes.
3. **Color:** Make color a source, not a fill: accents get `box-shadow: 0 0 24px 6px` in their own hue at 35% alpha, tinting nearby surfaces. Fills stay `#1A1B1E`.
4. **Color:** Where two zones meet, overlap their glows with `mix-blend-mode: screen` so the seam turns pale.
5. **Color:** Assign one emitted hue per zone of the app (nav green, content blue, alerts red, focal or primary gold), like the nave/transept/apse at Chiesa Rossa.
6. **Corners:** Put a key accent as an L of two bars in a container's inner corner, plus `radial-gradient(at 0 100%, hue 30%, transparent 60%)` so the panel is brightest at the fold.
7. **Type:** Set headings in lowercase Barlow Condensed and put the secondary label in parentheses on the same line, e.g. "settings (to you, admin)".
8. **Motion:** Replace slide/fade entrances with a flicker-on keyframe (opacity 0 → .8 → .2 → 1 over 120 ms), then a 500 ms glow bloom.
9. **Interaction:** Render blocking states (paywalls, permission gates) as see-through barriers: spaced vertical glowing bars over content that stays visible.
10. **Interaction:** Give toggles two faces: pink in one state, green in the other, with the halo spilling toward opposite sides.
11. **Hierarchy:** Mark the single most important element with a 45° bar, the screen's only diagonal.

## What this artist would reject
- Gradients painted *on* objects (glossy buttons, skeuomorphic shading). Light comes out of the element.
- Custom one-off sizes and decorative illustration. Stock kit or nothing.
- Grey drop shadows *below* things, instead of colored light thrown *outward*.
- Centered hero objects floating free of the container's edges and corners.
- Rainbow palettes with many equal hues, instead of one or two emitters per zone.
- Swooping motion, parallax, bouncy easing. Light switches on; it doesn't fly.

## Signature prompt seed
Design the screen as a darkened room lit by a few standard fluorescent fixtures. Use a flat charcoal ground (#1A1B1E) with no cards. Structure comes from 3 px glowing bars on edges and inner corners, in only four lengths (25/50/75/100%). Each zone has one emitted hue (green, pink, gold or cool white) whose halo spills onto neighboring surfaces and turns pale where glows overlap. One bar runs at 45°. Headings are lowercase Barlow Condensed with parenthetical dedications. Elements flicker on, then bloom. Locked areas sit behind see-through barriers of spaced vertical light.

## Sources
- https://www.moma.org/learn/moma_learning/dan-flavin-monument-1-for-v-tatlin-1964/
- https://www.moma.org/collection/works/81337
- https://en.wikipedia.org/wiki/Dan_Flavin
- https://en.wikipedia.org/wiki/Santa_Maria_Annunciata_in_Chiesa_Rossa
- https://www.fondazioneprada.org/project/dan-flavin/?lang=en
- https://diaart.org/collection/collection/flavin-dan-untitled-to-you-heiner-with-admiration-and-affection-1973-2005-007
- https://diaart.org/collection/collection/flavin-dan-the-diagonal-of-may-25-1963-to-constantin-brancusi-1963-1996-001
- https://chinati.org/collection/dan-flavin/
