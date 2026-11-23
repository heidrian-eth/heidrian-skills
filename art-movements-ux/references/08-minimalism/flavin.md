# Dan Flavin — Minimalism

## Essence
Flavin arranged off-the-shelf fluorescent fixtures so the tubes matter less than the colored light they throw onto walls, floors and corners. Each work is a "situation", not a sculpture: the room it lights is part of the piece. With a fixed kit (four lengths, ten colors), all his invention went into placement, orientation and where the light overlaps.

## Key works examined
- **the diagonal of May 25, 1963 (to Constantin Brancusi), 1963.** One yellow tube on the wall at 45°. A single part at an unexpected angle turns the whole wall into a composition. *(not obtained: diaart.org 403)*
- **"monument" 1 for V. Tatlin, 1964.** White tubes stepped into an 8-ft form, the first of 39 "monuments", echoing Tatlin's unbuilt tower: a heroic idea from stock parts. *(visually checked: AIC "monument" for V. Tatlin, 1964. Seven cool-white tubes side by side, lengths 155/318/480/640/485/322/160 px = 1:2:3:4:3:2:1, i.e. 2-4-6-8-6-4-2 ft, bottoms aligned on the left half and tops aligned on the right, so the silhouette is a stepped diagonal. The halo on the grey wall falls to half within ≈3 tube widths and fades out by ≈8–10)*
- **greens crossing greens (to Piet Mondrian who lacked green), 1966.** His first full installation. Green fixtures crisscross the room in the one color the grid painter left out. *(not obtained)*
- **untitled (to you, Heiner, with admiration and affection), 1973.** A barrier of 70 identical 48 × 48 in units. A glowing fence you can see through but not walk through. *(not obtained: diaart.org 403)*
- **untitled (Marfa project), 1996–2000.** Six U-shaped buildings whose corridors are closed by full-height barriers of 8-ft fixtures, each holding two colors facing opposite ways (pink/green, yellow/blue, then all four). *(visually checked: five Chinati photos. Each barrier is a parallelogram of 10–12 fixtures leaning ≈10–15° off vertical (photo perspective), the two hues alternate tube by tube at 1:1 with gaps no wider than a tube, and the white room around them is flooded with the mixed light: the wall between a pink/green and a yellow/blue barrier reads near-white `#D0BFC7`)*
- **untitled, 1969 (AIC).** Two 8-ft pink tubes leaning in a corner of a white room, one facing the viewer, one turned to the wall so only its wash shows. The "pink" reads coral (`#F08C6E`). *(visually checked: AIC image)*
- **untitled, Santa Maria Annunciata in Chiesa Rossa, Milan, 1996–97.** His last work: green and blue in the nave, red in the transept, gold-yellow in the apse. Color marks out the zones of the building. *(visually checked: secondary source, divisare.com, 5 photos)* Seen: the tubes are thin continuous lines tucked along the cornice where wall meets vault, so the source is a line but the colour arrives as whole fields: the nave vault and entrance wall wash deep blue, the side chapels and transept walls glow pink-red, and the apse at the end of the axis is gold-yellow, with the warm zone framed by the blue nave in the long view. Green was not visible in these photos. Wooden pews and doors keep their own dark brown, so the light tints only the white plaster.

## Process and relations (observed)
- **Space** (Chiesa Rossa): the building's zones (nave, transept, apse) each get one hue; the hues follow the main axis from cool at the entrance to warm at the goal.
- **Colour relations:** 3 emitted hues seen (blue, pink-red, gold); each fills a whole architectural zone; the warmest and brightest (gold) is the smallest and sits at the end of the axis, framed by the cool largest field.
- **Line and edge:** the source is a thin line at an architectural edge (cornice); the light edges on the walls are soft gradients.
- **The procedure:** hide one line of light along each zone's edge; give each zone one hue; order hues cool → warm along the route; make the goal the smallest, warmest, brightest field.

## Process (derived)
*From observation to process (see SKILL.md §1). This is what transfers; the rest of the file is evidence.*

**Dan Flavin.** *Colour is thrown, not applied: thin sources on the edges light an empty field, and zones are made by whose light reaches them.*
Process:
1. Fix a kit before designing: one source shape of constant thickness in at most four lengths at 1:2:3:4. Nothing custom; all invention goes into count, placement and orientation.
2. Empty the field and give it a neutral value with headroom (at least 30 L away from the source's value). No panels inside it. Place sources only on structure: boundaries, folds, thresholds, the seam between two zones.
3. Split colour into two roles. The source is the thinnest thing present, at the value extreme and nearly without chroma. The wash it throws carries the peak chroma and the area: half strength within about 3 source widths, gone by 8–10.
4. Give each zone one hue. Order the hues along the main route from cool at the entry to warm at the goal, and make the goal the smallest, warmest and brightest zone, seen framed by the largest cool one.
5. Where two washes meet, let them overlap and mix toward a paler, more neutral blend. Never draw a divider there.
6. Barrier mode (to stop movement while showing what lies beyond): repeat the source side by side with gaps no wider than one source, two hues alternating 1:1, covering the passage.
7. Switch on in one direction only: the source rises in a single monotone fade, then its wash spreads. Never blink, pulse or flicker.
Why it works:
- A large soft gradient is read as illumination and discounted, so content keeps its own colours while the zone is still felt. A hard-edged filled panel in the same hue would read as an object competing with the content.
- A thin pale source avoids a glare point, and sitting on the edge it leaves the centre free. Saturate the source instead and it becomes a neon sign: the eye goes to the line and the field goes dark.
- A seam that is paler than both of its sides reads as a join, not as a wall, so zones stay one space. With a fixed kit, every difference is read as arrangement, which is the only variable left.
Colour relations: neutral field 70–85%, mid value; sources under 3% at the value extreme, lowest chroma; washes 15–30% carrying peak chroma, at most four hues, one per zone, ranked cool and large to warm and small; overlaps paler than either parent; text only where the wash has fallen low enough to keep 4.5:1, or the wash is capped under text.
Space and line: sources 0.3–0.5% of the short side, four lengths at 1:2:3:4 (stepped 1:2:3:4:3:2:1 when grouped); all on edges; centre empty; the visible source is never the hit area (control targets 44px or more around it).
Type requirement: monoline and narrow, of even stroke like the source; set on the neutral field, not on the peak of a wash; every zone carries a text label, since hue alone may not name it.
Motion and interaction: on = one fade of the source (about 150ms, opacity 0 → 1, monotone), then the wash spreading over 400–600ms; repeated units follow at about 40ms each; off reverses (wash first). Reduced motion: the final state appears with no transition.
Fails when: the ground sits at the source's own value extreme (no headroom for a wash); long text or data colours must sit inside a wash; more than about four zones; meaning (status, category) would rest on hue alone.
Signature (do not carry together): bare fluorescent tubes · pink, green, yellow and blue catalogue light · a glowing corner or leaning barrier in a white room.

**Transfer test** (an illustration that the process survives new colours and content; never reuse its hues, layout or wording as a design answer):

Flavin's procedure → a tax-filing wizard in warm paper greys (desktop, 1440 × 900).
1. *Kit.* One 4px line (0.44% of the short side) in four lengths: 225, 450, 675, 900px. Nothing else draws structure.
2. *Field.* One warm grey at L 66 covering the screen, no cards. Lines at L 97 (31 L of headroom). Forms sit directly on the field in dark ink.
3. *Roles.* Each line is near-white with a trace of its zone hue. Its wash is the saturated part: a tint that is half strength at 12px and gone by 36px, capped so ink on it stays above 4.5:1.
4. *Zones.* Four steps along the left-to-right route: Income, a slate-blue wash from a 900px line on the left edge (40% of the width); Deductions, a grey-green wash from a 675px line (30%); Review, a dusty violet from a 450px line (20%); Submit, a warm ochre from a 225px line on the right edge (10%), the smallest, warmest, lightest field. Each zone is headed by its name and step number in text.
5. *Seams.* Between steps the two washes overlap for 36px and blend 4 L lighter than either; no rule is drawn.
6. *Barrier.* A locked step is covered by 11 lines at 4px with 4px gaps, alternating its own hue and its neighbour's, with the form readable but inert behind them and the text "Complete Income first" plus a lock icon on top.
7. *On.* Entering a step: its line fades in over 150ms, its wash spreads over 500ms. With reduced motion both simply appear.
- *Type.* A narrow monoline sans, 15px body on the grey field; the submit control is a 48px-high target around the 225px line.
Result: a pale, papery form flow. No tubes, no dark room, no neon hues. What survived: a fixed kit, structure only at the edges, pale source with coloured throw, cool-to-warm zoning toward the goal, seams made by mixture.

## Space & composition
- **The fixture sits on the edge and the light fills the field.** Tubes hug baselines, corners and doorframes. The middle of the space holds only tinted air.
- **Corners are the stage.** Corner pieces sit in the 90° fold, where the two walls catch light unevenly, which gives a built-in gradient from bright seam to dim edge. (No corner piece obtained; the AIC 1969 tubes lean near a corner and do light the two walls unevenly.)
- **A fixed set of parts.** Only 2, 4, 6 and 8 ft lengths (circles from 1972), a 1:2:3:4 ratio, confirmed on the AIC "monument" (1:2:3:4:3:2:1). Variety comes from count and orientation, never custom sizes.
- **Barriers and corridors.** Repeated units stop or channel movement (his first corridor dates from 1973), with see-through spacing: a wall made of gaps. At Marfa the barriers are slanted parallelograms, not upright fences, and two hues alternate 1:1 inside one barrier.
- **Two faces.** At Marfa, space reads differently depending on which side you approach from.

## Color
*The hex table below is a reference sample for strict studies and homage only. For design, use the colour relations in "Process (derived)".*

Flavin's palette was simply the catalog: red, blue, green, pink, yellow, ultraviolet and four whites. These colors are emitted, so they **add up**: overlapping pink and green light on a wall makes a pale, near-white blend no paint could make (seen at Marfa: `#D0BFC7` between the barriers). In the photographs the **tube itself reads pale**, its core clipped to near-white and its flank pastel (green tube `#98C38A`, C*35), while the **strongest colour sits on the lit wall and floor** a little way off (green wall `#60A75E`, C*48; blue-lit side walls `#6868A9`, C*38). Saturation peaks in the wash, not at the source. The receiving walls are white surfaces turned mid-tone by the light (L*33–66), never near-black.

| Role | Hex | Note |
|---|---|---|
| Wall / ground (light off) | `#6F6E5D` | grey wall beside the "monument" (AIC); photographed walls are L*41–52, not charcoal, so a darker UI ground is a screen choice |
| Daylight white (primary emitter) | `#ECEDEA` | cool-white tube core ("monument", AIC) |
| Warm white (secondary emitter) | `#D0BFC7` | nearest real: pale near-white blend where pink/green and yellow/blue light overlap (Marfa); no warm-white tube photographed |
| Fluorescent green | `#98C38A` | green tube as seen (Marfa); pastel at the source |
| Pink | `#F08C6E` | pink tube (AIC 1969); reads coral, not magenta |
| Gold-yellow | `#EDC274` | yellow tube flank (Marfa); core clips to `#F9E69C` |
| Ultraviolet | `#797EB9` | nearest real: "blue" tube, reads lavender (Marfa); no ultraviolet work obtained |
| Green wash on wall | `#60A75E` | the most saturated colour in the set is on the wall, not the tube (Marfa) |

## Form, line & typography
The basic mark is a uniform rod: constant width, rounded ends, no taper. Type should match: **monoline, narrow, rational** letterforms that look extruded rather than drawn. Flavin titled works in lowercase with a dedication in parentheses ("untitled (to …)"), a quiet, parenthetical way of labeling. Fonts: **Barlow Condensed** (rod-like verticals), **IBM Plex Mono** (catalog/spec tone for metadata), **Archivo Narrow** (body).

## Rhythm, motion & time
Motion should be **ignition, not travel**. Elements don't slide in. They switch on in one monotone fade (opacity 0 → 1 over about 150 ms, never blinking or pulsing), and the halo blooms afterward over 400–600 ms. Repeated units light one by one at a 40 ms stagger, like fixtures warming up. On exit, the halo fades before the rod.

## UI translations
1. **Layout:** Draw structure only along edges, with a 3–4 px glowing bar on the left or bottom margin instead of boxed cards.
2. **Layout:** Restrict every divider and bar to four lengths (25/50/75/100%), echoing the 2-4-6-8 ft tubes.
3. **Color:** Make color a source, not a fill: accents get `box-shadow: 0 0 24px 6px` in their own hue at 35% alpha, tinting nearby surfaces (measured halo: half-strength at ≈3 bar widths, gone by ≈10). Keep the bar's own fill pale (near-white with a tint) and let the glow carry the saturation. Fills stay a dim ground.
4. **Color:** Where two zones meet, overlap their glows with `mix-blend-mode: screen` so the seam turns pale.
5. **Color:** Assign one emitted hue per zone of the app (nav green, content blue, alerts red, focal or primary gold), like the nave/transept/apse at Chiesa Rossa.
6. **Corners:** Put a key accent as an L of two bars in a container's inner corner, plus `radial-gradient(at 0 100%, hue 30%, transparent 60%)` so the panel is brightest at the fold.
7. **Type:** Set headings in lowercase Barlow Condensed and put the secondary label in parentheses on the same line, e.g. "settings (to you, admin)".
8. **Motion:** Replace slide entrances with a switch-on: one monotone fade (opacity 0 → 1 over 150 ms, no flicker or blips), then a 500 ms glow bloom; under reduced motion, show the lit state at once.
9. **Interaction:** Render blocking states (paywalls, permission gates) as see-through barriers: 10–12 glowing bars, two hues alternating 1:1, gaps no wider than a bar, the block leaning 10–15° as a parallelogram, over content that stays visible.
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
Design the screen as a darkened room lit by a few standard fluorescent fixtures. Use a flat dim ground (the photographed walls are mid-grey, #6F6E5D; go darker only as a screen choice) with no cards. Structure comes from 3 px glowing bars on edges and inner corners, in only four lengths (25/50/75/100%). Each zone has one emitted hue (green, pink, gold or cool white) whose bar stays pale while its halo carries the saturation onto neighboring surfaces, turning near-white where glows overlap. One bar runs at 45°. Headings are lowercase Barlow Condensed with parenthetical dedications. Elements switch on in one monotone fade, then bloom. Locked areas sit behind see-through, slightly leaning barriers of bars in two alternating hues.

## Sources
- Retry pass 2 (secondary source, divisare.com): Santa Maria Annunciata in Chiesa Rossa, 5 photos, https://images.divisare.com//images/…/v1518007431/a2qjb4luhr6n5jv0suqc/… and 4 others (page https://divisare.com/projects/379048-giovanni-muzio-alba-deangelis-dan-flavin-at-santa-maria-annunciata-in-chiesa-rossa)
- https://www.moma.org/learn/moma_learning/dan-flavin-monument-1-for-v-tatlin-1964/
- https://www.moma.org/collection/works/81337
- https://en.wikipedia.org/wiki/Dan_Flavin
- https://en.wikipedia.org/wiki/Santa_Maria_Annunciata_in_Chiesa_Rossa
- https://www.fondazioneprada.org/project/dan-flavin/?lang=en
- https://diaart.org/collection/collection/flavin-dan-untitled-to-you-heiner-with-admiration-and-affection-1973-2005-007
- https://diaart.org/collection/collection/flavin-dan-the-diagonal-of-may-25-1963-to-constantin-brancusi-1963-1996-001
- https://chinati.org/collection/dan-flavin/
- Images checked: https://www.artic.edu/artworks/52310 , https://www.artic.edu/artworks/184115 (AIC IIIF)
- https://chinati.org/wp-content/uploads/2019/06/9330_Chinati_IN_166_flavin.jpg , ..._IN_169_flavin-e1575557310997-768x1152.jpg , ..._IN_156_flavin2.jpg , ..._IN_171_flavin2.jpg , ..._IN_172_Flavin2.jpg
