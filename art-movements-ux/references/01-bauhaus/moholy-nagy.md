# László Moholy-Nagy — Bauhaus

## Essence
Moholy-Nagy treated light as the material of design, and paint, photo paper, chrome, type and film as ways to modulate it. His work is built from translucent planes that overlap, so you read depth through them. The subject is a surface's change of state (opaque, translucent, transparent, reflective), not the objects. Layout, for him, was montage paced like film.

## Key works examined
- **Light Prop for an Electric Stage (Light-Space Modulator), 1930.** A rotating machine of metal, perforated and glass surfaces. Under a spotlight it throws shadows, translucencies and reflections. It teaches that the interface is the light it throws, not the object.
- **Light Play: Black White Gray, 1930.** A film whose only subject is the Light Prop, shot in close-up with double exposures. It teaches that one component can carry endless states.
- **Photogram Number 1, the Mirror, 1922–23.** A cameraless image made by laying objects on photo paper. It teaches figure and ground as degrees of exposure, not outlines.
- **Composition A.XX, 1924.** A diagonal glass-like plane, with translucent bands that turn more opaque where they cross. It teaches a four-state material system.
- **Painting, Photography, Film, 1925, the "Dynamic of the Metropolis" section.** A film storyboard on paper, with bold rules cutting the pages together. It teaches rules as cuts and pacing as a design variable.
- **Vision in Motion, 1947.** His posthumous Chicago teaching testament, arguing for educating emotion alongside intellect. It teaches that systems should invite play.

## Space & composition
- **Diagonal axis.** The main structural line runs 15–35° off the horizontal and crosses the viewport. Content hangs off the diagonal, not off a centred column.
- **Depth without perspective.** In A.XX, vertical bars recede only by shrinking, and a small distant circle anchors the far plane. In UI terms, that means three tiers at 1×, 0.6× and 0.25× scale, with no drop shadows.
- **Light ground.** About 60% of the field stays pale, with planes spread asymmetrically. The largest plane bleeds 10–20% out of frame.
- **Overlap is information.** The darker shape where two planes cross is the focal point.
- **Rules as cuts.** Thick black bars (6–12px) divide sections the way splices divide film.

## Color
The base is a grey scale, as in Light Play, with a few transparent chromatic planes laid on top. Color acts as a gel, not a fill. Where planes cross, the overlap must get darker (multiply), never lighter.

| Hex | Role |
|---|---|
| `#F1EEE6` | Light-table ground (the highlights of a photogram print) |
| `#121212` | Silver-gelatin black: rules, bars, primary type |
| `#8E9093` | Chrome grey: secondary planes, metallic states |
| `#D9D6CF` | Mid-exposure grey: translucent panels |
| `#E8B624` at 70% opacity | Transparent yellow plane |
| `#3E4FA0` at 60% | Violet-blue plane laid over the yellow so it multiplies to olive-black |
| `#C23B22` | Signal red: one accent circle per screen |

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
1. **Layout:** Rotate the hero image plane 22°, bleed it 15% off the right edge, and seat the headline on that diagonal.
2. **Layout:** Replace shadowed cards with overlapping translucent panels, each 1.5–2× the size of its neighbour, so depth reads from scale alone.
3. **Color:** Build components in greys. Add color only as a semi-transparent multiply overlay, so the overlaps form new, darker tones.
4. **Color:** Use exactly one signal-red circle per screen, marking the primary action or status.
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
Compose this screen like a Moholy-Nagy light table. Use a warm off-white ground, about 60% open, with one large translucent plane rotated about 22° and bleeding off the right edge. Build depth only from overlap and 1×, 0.6× and 0.25× scale tiers, never from shadows. Use grey and chrome planes, with transparent yellow and violet layers that multiply to near-black where they cross, plus one red circle for the main action. Fuse heavy grotesque type with photography, marking emphasis with thick black left rules. Cut hard between sections and dissolve slowly within them. The cursor is a spotlight.

## Sources
- https://www.metmuseum.org/art/collection/search/899299
- https://harvardartmuseums.org/exhibitions/3499/light-display-machines-two-works-by-laszlo-moholy-nagy
- https://harvardartmuseums.org/article/em-light-prop-for-an-electric-stage-em-past-and-present
- https://exhibitions.letterformarchive.org/bauhaus/walkthroughs/typophoto-in-moholy-nagy-s-painting-photography-film
- https://smarthistory.org/laszlo-moholy-nagy-composition-a-xx/
- https://www.getty.edu/art/exhibitions/genius/zoom_moholy.html
- https://www.artic.edu/artworks/29276/untitled
- https://openspace.sfmoma.org/2010/06/moholy-nagy-part-2-form-follows-emotion/
