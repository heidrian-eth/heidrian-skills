# Agnes Martin — Minimalism / abstract

## Essence
Martin filled a six-foot square with a grid of slightly *rectangular* cells, ruled by hand in pencil over a pale wash. The work is about near-sameness: a rigid system drawn by a hand that wavers, and a structure that stops short of the edge so it floats. Up close you see trembling graphite. From across the room you see tinted, breathing light that stands for innocence and calm without depicting anything.

## Key works examined
- **Friendship, 1963** (MoMA, 190.5 cm square): gold leaf over oil, scored by hand to reveal the ground. Teaches that a grid can be carved *out* of a surface.
- **The Tree, 1964** (72 × 72 in): planned as a postage-stamp-sized sketch with calculations, then laid out with tape, ruler and pencil. Teaches you to design the system tiny and render it huge.
- **The City, 1966** (Cleveland, acrylic and graphite): thin rectangular cells over a faintly modulated ground. Teaches that the ground should vary while the structure stays fixed.
- **Untitled #4 / Untitled #12, 1977** (NGA Australia / Art Institute of Chicago, ink, graphite and gesso): an uneven ink wash with pencil lines that skip on the canvas tooth. Teaches that imperfection belongs inside the rule.
- **With My Back to the World, 1997** (MoMA, six 60-inch panels): blue, peach and yellow bands that look identical until you look closely. Teaches variation across a series at the threshold of notice.
- **Innocent Love series, 1999–2000** and **Untitled #1, 2003**: the palette warms toward apricot, salmon and buttercup. Teaches you to hold a restrained structure while the colour gets warmer.

## Space & composition
- **The square holds a grid that is not square.** Martin said rectangles "a little bit off the square" lighten the square's weight. In UI: use a square container filled with rows at a 1:3 to 1:8 aspect ratio, never square cells.
- **The grid stops before the edge.** Her pencil lines end short of the canvas edge, so the field floats. Inset every rule by 4–6% of the container width.
- **All-over, no focal point.** No cell outranks another. Hierarchy comes from *distance*: up close it is detail, from far away it is tone.
- **Density as texture.** Cells a few millimetres tall on a 183 cm field read as a surface value, not as information.
- **Late bands.** From the 1990s, horizontal bands of unequal or symmetric heights (for example 1:1:2:1:1) are split by single crisp graphite lines.

## Color
The method is translucent wash over bright white. When a colour felt too heavy she added white wash until it gave off light. Values sit within a few percent of each other, so contrast comes from hue, not value.

| Hex | Role |
|---|---|
| `#F5F2EB` | Gesso ground: the default surface |
| `#E9DAD3` | Pale pink wash: section band |
| `#D3DFDC` | Duck-egg blue wash: alternate band, selected state |
| `#F2EBC6` | Pale lemon: highlight, success |
| `#D9CCB6` | Tan ink wash (1977): secondary panels |
| `#9A9893` | Graphite: rules and text |
| `#C2AB78` | Scored gold (Friendship): one precious action per screen |

Keep every band's L* (lightness) between 86 and 94. Text is graphite, never black.

## Form, line & typography
Her line is a ruled pencil stroke: straight in intent, uneven in pressure, about a hairline at screen scale. Type should be just as thin and even. Use 300 weights, wide tracking and tall leading, and never bold. Her titles are lowercase and plain ("the tree", "friendship").
- **Jost** 300: geometric, quiet, with even stroke width.
- **Cormorant Garamond** 300 italic: rare, gentle titles.
- **IBM Plex Mono** 300: tiny metadata, like her calculations in the margin.

## Rhythm, motion & time
The work changes with viewing distance and time, not with events. Bands fade in over 900–1400 ms (`cubic-bezier(.4,0,.2,1)`), staggered 60–80 ms per row from the top, like a wash spreading. No bounce, scale, or translation over 4 px. An optional ambient cycle moves between two adjacent tints over 20–40 s. Scrolling should feel like crossing an empty beach: long runs of near-identical rows and no parallax.

## UI translations
1. **Layout:** Make the main screen a centred square panel (`aspect-ratio: 1; width: 72vmin`), with contents inset 5% so nothing touches the edge.
2. **Layout:** Make list rows 1:6 rectangles, with height derived from container width rather than from content.
3. **Line:** Draw dividers as 0.5–1 px `#9A9893` rules at 65% opacity, with an SVG `feTurbulence` displacement of 0.3 px so each rule wobbles slightly, like a hand-ruled line.
4. **Color:** Give each section an `rgba` wash at 0.25–0.4 alpha over the gesso ground, with 2–3% grain noise showing through.
5. **Color:** For categories, rotate hue and hold lightness fixed, so bands are indistinguishable in greyscale.
6. **Type:** Use Jost 300 at 16 px, letter-spacing 0.04em, line-height 1.8. Headings get a 1.25× size step and no weight change.
7. **Type:** Set labels in lowercase mono, sitting on the ruled lines like notes written between pencil lines.
8. **Motion:** Make entrances opacity-only, 1 s or longer, row by row.
9. **Interaction:** On hover, deepen a row's wash by one step (alpha +0.1). No shadows, lift or colour inversion.
10. **Interaction:** Use distance as zoom. A collapsed view shows only tinted bands, and expanding a band reveals the fine ruled detail, like walking up to the canvas.
11. **Emphasis:** Allow one gold hairline-outlined action per screen, never a filled button.
12. **Empty states:** Show faint ruled lines, no illustration.

## What this artist would reject
- Elevated cards with drop shadows and 16 px radii.
- Saturated brand accents and pure black text.
- Bold-weight hierarchy and giant hero metrics.
- Hero images and focal-point layouts.
- Springy micro-animations and confetti.
- Pixel-identical, machined repetition with no trace of a hand.

## Signature prompt seed
Design this screen as a pale square field: gesso off-white ground, translucent washes of pink, duck-egg blue and lemon, all at equal lightness. Divide it into thin horizontal rectangles, never squares, ruled with faint wavering graphite hairlines that stop short of every edge so the structure floats. Use Jost Light, lowercase, widely spaced, with no bold anywhere. Remove all shadows, cards and icons. From a distance it should read as breathing light, and up close as trembling pencil. Use only slow opacity fades and one hairline gold action. The mood is innocence and calm.

## Sources
- https://www.moma.org/collection/works/79842
- https://www.moma.org/collection/works/79892
- https://www.phaidon.com/blogs/stories/the-evolution-of-agnes-martin-in-5-pictures
- https://www.artic.edu/artworks/89403/untitled-12
- https://www.clevelandart.org/art/1991.30
- https://diaart.org/program/past-programs/agnes-martin-homage-to-a-life-paintings-1990-2004-exhibition/
- https://www.tate.org.uk/tate-etc/issue-34-summer-2015/square-dance-joy-i
- https://aci-iac.ca/art-books/agnes-martin/significance-and-critical-issues
- https://digital.nga.gov.au/archive/americanmasters/works.cfm%3Fwrkirn=116209.html
