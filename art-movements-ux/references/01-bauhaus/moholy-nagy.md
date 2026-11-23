# László Moholy-Nagy — Bauhaus

## Essence
Moholy-Nagy treated light as the material of design, and paint, photo paper, chrome, type and film as ways to modulate it. His work is built from translucent planes that overlap, so you read depth through them. The subject is a surface's change of state (opaque, translucent, transparent, reflective), not the objects. Layout, for him, was montage paced like film.

## Key works examined
- **Light Prop for an Electric Stage (Light-Space Modulator), 1930.** A rotating machine of metal, perforated and glass surfaces. Under a spotlight it throws shadows, translucencies and reflections. It teaches that the interface is the light it throws, not the object. *(not visually checked: no image of the object reachable)*
- **Light Play: Black White Gray, 1930.** A film whose only subject is the Light Prop, shot in close-up with double exposures. It teaches that one component can carry endless states. *(visually checked: Centre Pompidou film-strip image; high-contrast black/white frames with the perforated disc's grid and double-exposed planes)*
- **Photogram Number 1, the Mirror, 1922–23.** A cameraless image made by laying objects on photo paper. It teaches figure and ground as degrees of exposure, not outlines. *("the Mirror" itself not obtained; three AIC photograms checked instead: Untitled 1922, Untitled c.1923/25 (a profile in soft-edged white on black), Untitled c.1940)*
- **Composition A.XX, 1924.** A diagonal glass-like plane, with translucent bands that change tone where they cross. It teaches a four-state material system. *(visually checked: Centre Pompidou image. Entirely neutral: raw beige canvas, two greys, black. A large circle (48% of the width, lower right) and a small one (16%, upper left); a tilted translucent quadrilateral; two crossing bands that turn black quadrants grey and grey quadrants ground-coloured, i.e. lighter; a hairline at 27° running to the left edge; faint vertical hairlines across the full height. Nothing bleeds off the canvas except hairlines)*
- **The Mavericks II (Die Eigenbrötler II), 1927 (AIC)** *(added; visually checked)*: photomontage (fotoplastik) of cut-out figures, animals and a gridded façade on a pale photographic ground; the façade runs off the right edge.
- **Painting, Photography, Film, 1925, the "Dynamic of the Metropolis" section.** *(not visually checked)* A film storyboard on paper, with bold rules cutting the pages together. It teaches rules as cuts and pacing as a design variable.
- **Vision in Motion, 1947.** His posthumous Chicago teaching testament, arguing for educating emotion alongside intellect. It teaches that systems should invite play.

## Process (derived)
*From observation to process (see SKILL.md §1). This is what transfers; the rest of the file is evidence.*

**László Moholy-Nagy.** *Treat every surface as a filter of light with a declared state, and let overlap carry depth: wherever two planes cross, a third value must appear.*
Process:
1. Build a value ladder of 4–5 steps, at least 8–10 L apart, and give hue no structural job. The ground takes one end of the ladder and, in the open mode, about 80% of the area.
2. Declare a state for every surface from a short list: opaque (a ladder value), translucent (shifts whatever is beneath by exactly one step), transparent (an outline or hairline only). Three or four states for the whole system.
3. Set one oblique axis, 15–35° off the horizontal, and hang the planes along it asymmetrically. Nothing is centred on the format.
4. Repeat one simple form at two or three sizes along the axis, 1 : 0.33 (optionally 0.6 between). The smaller reads as farther.
5. Make every crossing visible. Where planes overlap, shift one ladder step, always in the direction the upper plane's state dictates (it may lighten what is under it). An overlap that changes nothing is not allowed: separate the planes or change a state.
6. Run a few hairlines the full extent of the format. They are the only elements that reach the frame, and they tie the floating planes to it.
Why it works:
- Perceived transparency: when an overlap takes a value consistent with one surface filtering another, the eye infers which is in front without shadow or outline. If the shift is inconsistent or absent, the layers collapse into a flat mosaic.
- Size gradient: the same form repeated at a third of the size is read as the same thing farther away. Different forms at different sizes are read only as big and small.
- With hue out of the structure, value is free to mean one thing, the passage of light. Add structural hue and each overlap needs a colour mixture the eye must also believe.
Colour relations: a neutral or single-hue ladder; ground at one extreme, ≈80% in the open mode; mid values ≈9%, the opposite extreme ≈5%; translucent planes sit one step from the ground; any hue acts as a tint over the ladder, never as a role.
Space and line: one oblique axis at 15–35°; forms at 1 : 0.33; open, asymmetric distribution; hairlines edge to edge in two directions; planes otherwise stay inside the frame (running a plane off the edge is an option, not a rule); no shadows.
Type requirement: one heavy weight that reads as a solid plane on the ladder; text stays on an area of a single value with ≥4.5:1 and crosses a plane boundary only if that holds on both sides; emphasis is a solid bar at the ladder's far end, not a hue.
Motion and interaction: a state change is a change of material state. A layer goes transparent → translucent → opaque (about 400ms) and what lies under it shifts one step; hard cuts between sections, slow dissolves (600–900ms) within one, never repeated fast enough to flicker; a pointer may brighten its neighbourhood by one step, but nothing is revealed by hover alone.
Fails when: status or brand hue must carry meaning; the content is tables or forms (overlap hides data and the oblique axis fights rows); copy has to sit on crossings; displays or contrast modes erase single-step shifts.
Signature (do not carry together): a circle cut by translucent bands on bare canvas · white camera-less silhouettes on black · a tilted glass-like plane with hairlines.

**Transfer test** (an illustration that the process survives new colours and content; never reuse its hues, layout or wording as a design answer):

Product: cooking-timer and recipe-step app, phone 390 × 844, one saturated warm hue family, friendly. The source is hue-less, sparse and austere.
1. *Ladder.* Five values of one terracotta hue: L 92, 80, 66, 48, 24. Ground is L 92 and covers 78% of the screen. Hue is constant, so it carries no structure.
2. *States.* Opaque: the active timer (L 24). Translucent: the "next step" sheet, which darkens anything under it by one step. Transparent: finished steps, drawn as 1px outlines.
3. *Axis.* 24° rising left to right. The active timer sits low right, the next-step sheet crosses it, finished steps trail up left along the axis.
4. *Tiers.* Timers are one rounded-bar form at 220px, 132px and 72px long (1 : 0.6 : 0.33): running, queued, later.
5. *Crossings.* Where the sheet covers the running timer, L 24 becomes L 48, and where it covers ground, L 92 becomes L 80: one step each, same direction. A queued timer that touched the sheet without changing was moved 16px clear.
6. *Hairlines.* Two 1px lines at L 66 run the full height at x = 96 and x = 294, and one runs along the axis to the left edge.
- *Type.* One heavy rounded sans. The countdown is L 92 on L 24 (12:1) and is placed wholly inside the uncovered part of the timer; no text sits on a crossing.
- *Interaction.* Starting a step turns its outline translucent, then opaque over 400ms while the previous timer drops to outline. Tapping, not hovering, opens the sheet. Section changes cut; nothing strobes.
Result: a warm, single-hue screen in which depth comes only from consistent one-step overlaps and three sizes. No grey, no circle, no photogram.

## Space & composition
- **Diagonal axis.** The main structural line runs 15–35° off the horizontal and crosses the viewport. Content hangs off the diagonal, not off a centred column.
- **Depth without perspective.** In A.XX a small circle (one third the diameter of the large one: 16% vs 48% of the width) anchors the far plane. In UI terms, that means scale tiers such as 1×, 0.6× and 0.33×, with no drop shadows.
- **Light ground.** About 80% of the field stays open ground in A.XX (ground plus translucent plane 85%, grey 9%, black 5%), with planes spread asymmetrically. In A.XX nothing bleeds off except hairlines; in the photograms and The Mavericks II bands and façades do run off the edge, so a bleed is optional.
- **Overlap is information.** Where two planes cross, the tone shifts by one step; in A.XX it is usually *lighter* (black becomes grey, grey becomes ground), like light passing through glass.
- **Rules as cuts.** Thick black bars (6–12px) divide sections the way splices divide film.

## Color
*The hex table below is a reference sample for strict studies and homage only. For design, use the colour relations in "Process (derived)".*

The base is a grey scale, as in Light Play. Every checked work (A.XX, three photograms, The Mavericks II, the Light Play film strip) is neutral or sepia, with no chromatic colour at all, so the earlier yellow, violet and red roles are replaced by the nearest real tones below. Colour acts as a gel, not a fill. Where planes cross, the overlap shifts one step of value, darker or lighter (lighter over black in A.XX); never assume multiply. Samples are from the Pompidou A.XX image (raw canvas, so warm) and the AIC photograms.

| Hex | Role |
|---|---|
| `#C6B8A1` | Light-table ground (A.XX raw canvas, ≈80%; photogram highlights sample `#E4DBD4`) |
| `#1E1E1E` | Silver-gelatin black: rules, bars, primary type (A.XX black quadrants, 5%) |
| `#878787` | Chrome grey: secondary planes, metallic states (A.XX grey quadrants, 9%) |
| `#A7957C` | Mid-exposure tone: translucent panels (Photogram 1922 sepia mid-tone, 31%) |
| `#BEAD93` | Translucent plane, replaces the transparent yellow (A.XX quadrilateral: one step darker than the ground; no yellow seen) |
| `#9D9A95` | Light-grey band laid across other planes, replaces the violet-blue (A.XX bands; no violet seen) |
| `#1E1E1E` | The one accent circle, replaces signal red (A.XX's circles are black and grey; no red seen) |

## Form, line & typography
Moholy-Nagy coined "typophoto" for "the visually most exact rendering of communication": type and photograph fused into one composition. His books used bold type freely for emphasis. A heavy left-margin rule indented passages that needed attention. Bold circles marked section breaks and small circles marked footnotes. The shape vocabulary is the circle, the bar, the long thin plane and the grid of perforations. Type is a grotesque, sometimes run vertically or along the diagonal.
- **Fonts:** *Archivo Black* for heavy display, *Space Grotesk* for engineered mid-weights, *IBM Plex Mono* for captions.
- Set headlines large and tight (-0.02em). Set body in one weight. Mark emphasis with rules and bold, never with color.

## Rhythm, motion & time
His operative word was **tempo**: reading pace changes the way film cuts do. Motion means changing light, not objects sliding.
- Animate state changes between the four material states: opaque, translucent (12px backdrop blur at 60%), transparent (20%) and reflective (a sweeping gradient sheen).
- Rotate one element slowly, one revolution every 20–40 seconds. A perforated disc whose `mask-image` casts a moving shadow over the content works as a small Light Prop.
- Use hard 0ms cuts between sections and slow 600–900ms dissolves within them. For double exposures, crossfade two images at 50% with `mix-blend-mode: multiply`.

## UI translations
1. **Layout:** Rotate the hero image plane 20–30° (A.XX's main hairline runs at 27°), optionally bleed it off the right edge, and seat the headline on that diagonal.
2. **Layout:** Replace shadowed cards with overlapping translucent panels, each 1.5–2× the size of its neighbour, so depth reads from scale alone.
3. **Color:** Build components in a 5-step neutral ladder (`#C6B8A1 #BEAD93 #9D9A95 #878787 #1E1E1E`). Where panels overlap, step the overlap one value up or down (often lighter over dark), as a change of material, not a multiply.
4. **Color:** Use exactly one dominant circle per screen (black or black/grey quartered, as in A.XX), marking the primary action or status. A chromatic accent is a UI choice, not something seen in the checked works.
5. **Type:** Mark key passages with a 6px black left bar and a 1.5em indent. Use ● markers instead of numbered headers.
6. **Typophoto:** Run headlines straight into photographs, knocked out of the image or overlapping it, so letters and photo share one plane.
7. **Motion:** Open modals by changing material, transparent to translucent to opaque over 400ms, instead of sliding them in.
8. **Motion:** Make tempo a token: `--tempo-cut: 0ms`, `--tempo-dissolve: 800ms`.
9. **Interaction:** Make the cursor a light source. A radial highlight follows the pointer and turns the surfaces it passes reflective.
10. **Interaction:** Draw empty states as photograms: white silhouettes of the missing objects on a dark field.
11. **Texture:** Lay a perforated dot-grid mask over one panel and offset it on scroll so it casts a parallax shadow.

## What this artist would reject
- Opaque white cards with drop shadows faking elevation.
- Brand color poured flat into every fill.
- Centred, symmetrical heroes with text on the left and an image on the right.
- One uniform 300ms ease on every transition, which kills tempo.
- Photography and type quarantined in separate boxes.
- Decorative illustration unrelated to light, material or mechanism.

## Signature prompt seed
Compose this screen like a Moholy-Nagy light table. Use a warm raw-canvas ground, about 80% open, with one large translucent plane on a 20–30° diagonal. Build depth only from overlap and 1×, 0.6× and 0.33× scale tiers, never from shadows. Use grey and chrome planes, with translucent beige and light-grey bands that shift one value step where they cross, plus one black circle for the main action. Fuse heavy grotesque type with photography, marking emphasis with thick black left rules. Cut hard between sections and dissolve slowly within them. The cursor is a spotlight.

## Sources
- https://www.metmuseum.org/art/collection/search/899299
- https://harvardartmuseums.org/exhibitions/3499/light-display-machines-two-works-by-laszlo-moholy-nagy
- https://harvardartmuseums.org/article/em-light-prop-for-an-electric-stage-em-past-and-present
- https://exhibitions.letterformarchive.org/bauhaus/walkthroughs/typophoto-in-moholy-nagy-s-painting-photography-film
- https://smarthistory.org/laszlo-moholy-nagy-composition-a-xx/
- https://www.getty.edu/art/exhibitions/genius/zoom_moholy.html
- https://www.artic.edu/artworks/29276/untitled
- https://openspace.sfmoma.org/2010/06/moholy-nagy-part-2-form-follows-emotion/
- Images (visual check): https://www.centrepompidou.fr/fr/ressources/oeuvre/cAzEjq (Composition A.XX, https://www.centrepompidou.fr/media/picture/00/73/00735a6f90ce75d3a5a383f2003ad395/thumb_large.jpg), https://www.centrepompidou.fr/fr/ressources/oeuvre/crgdGrB (Ein Lichtspiel schwarz-weiss-grau, film strip), https://www.artic.edu/artworks/55465 (Untitled photogram 1922), https://www.artic.edu/artworks/132717 (Untitled photogram c.1923/25), https://www.artic.edu/artworks/29276 (Untitled c.1940), https://www.artic.edu/artworks/212399 (The Mavericks II)
