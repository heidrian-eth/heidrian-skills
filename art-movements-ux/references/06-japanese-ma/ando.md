# Tadao Ando — Japanese Ma / Critical Regionalism

## Essence
Ando builds a dark, closed box out of one material, then cuts a single exact opening to let light, sky or weather in. You arrive by a turned, slightly inconvenient path, so the light reads as an event rather than a feature. He works by subtraction: one material, one module, one aperture, and a void you have to walk through.

## Key works examined
- **Row House in Sumiyoshi (Azuma House), 1976**: a 57 m² plot split into three equal bays (living, open courtyard, sleeping). You cross the open sky in rain to go to bed. The void sits in the middle of the plan, and the inconvenience is intended.
- **Church of the Light, Ibaraki, 1989**: a 5.9 m cube cut by a wall at 15°, with a floor-to-ceiling cross slot behind the altar. It shows that darkness is the medium and light is the content.
- **Chichu Art Museum, Naoshima, 2004**: almost entirely underground. Triangular and square courts are cut into a hill and lit only by daylight, so the works change by hour. It teaches hiding the container and letting the cut-outs be the architecture.
- **Modern Art Museum of Fort Worth, 2002**: form-tie holes "plainly visible" on vast walls. The grid shows up as surface texture rather than drawn lines.
- **Ando's concrete method**: watertight timber shuttering in tatami-sized 3×6 ft (0.91×1.83 m) panels, so construction becomes a visible module.

## Space & composition
- **Module first.** Everything is built in a 1:2 panel (910×1820) with evenly spaced tie holes, typically 2 across × 3 down. Seams and holes form a faint grid that every opening and edge lands on.
- **Thirds with a hollow middle.** Sumiyoshi gives exactly one third of the plan to nothing. Use that as a layout law: a three-band layout whose center band is an empty, lit void the user has to traverse.
- **Orthogonal box + one diagonal intruder.** Plans are rectangular systems cut by a single angled or curved wall. The Church of the Light's 15° wall is the only non-orthogonal line, and it governs the entire entry.
- **Blank street face.** Sumiyoshi shows the street a windowless wall with one door.
- **Low density, high mass.** Walls 38 cm thick read as weight, and content clusters where the light reaches.
- **Processional, not hub-and-spoke.** You slip between volumes and turn before you arrive.

## Color
Color comes from material and light only. The palette is concrete under changing daylight plus one natural intrusion.
- `#8E8D88` concrete in shade (primary surface)
- `#C9C7C1` concrete in direct light (raised/lit surfaces)
- `#1C1C1B` interior darkness (the dominant ground in key moments)
- `#F4F1E8` the slot of daylight (used only at the aperture, never as a fill)
- `#6B5A45` aged scaffold-plank wood (floors, touch surfaces, a quiet warm accent)
- `#3E6A7A` framed sky/water (the one hue allowed, seen only through a cut)

Rule: 90% grey, at most 3% light, and blue appears only *inside* an opening.

## Form, line & typography
Ando's line is the precise cut: an untrimmed edge, a slot, a seam. Type should behave like that: small, restrained grotesk with generous tracking, placed on the module grid. Display type is rare, and when it appears it's thin and large. The angled wall maps to one rotated or obliquely aligned element per screen at most. Fonts: **Zen Kaku Gothic New** (Japanese-rooted, calm), **Inter Tight** (precise UI text), **Shippori Mincho** for a single quiet heading where serif warmth is wanted.

## Rhythm, motion & time
Time here is daylight moving slowly across a fixed wall, so motion should be slow, directional and ambient. Transitions follow a compression-release logic (dim, narrow, then open), like the dark corridor at Chichu ending in a line of light. A reveal holds briefly in shadow before the content brightens. Nothing bounces.

## UI translations
1. **Layout:** Build on a 1:2 module (e.g., 56×112 px cells) and draw it faintly as tie-hole dots (2 per cell width, 3 per height, `radial-gradient` at 6% opacity) instead of lines.
2. **Layout:** Split the key screen into three equal bands. Leave the middle band empty except for a lit gradient, and make users scroll or swipe *through* it to reach the second content block.
3. **Layout:** Allow exactly one element per screen to sit at 15° off-axis (a divider, card edge or clip-path). Everything else is orthogonal.
4. **Color:** Default to `#8E8D88`/`#1C1C1B` surfaces. Reserve `#F4F1E8` for one aperture: a thin vertical or cruciform slot of light (`clip-path` cut-out over a dark panel) that marks the primary action.
5. **Color:** Show the only saturated color (`#3E6A7A`) inside a masked window, never on buttons or text.
6. **Type:** Keep UI text at 13–15 px with +0.04em tracking, grey on grey (contrast passing AA but low-chroma). Put one hero word at 64–96 px weight 200 on the void band.
7. **Texture:** Apply a subtle concrete noise (SVG `feTurbulence`, 3–4% opacity) to large fields.
8. **Motion:** Use 900–1400 ms ease-in-out for page reveals: the screen opens dark, then a light gradient sweeps across from one edge, as if sunlight is entering.
9. **Motion:** Tie a very slow background gradient angle to the local time of day (morning light from the left, evening from the right).
10. **Interaction (indirect approach):** The landing screen offers no immediate CTA. The user passes one quiet threshold (scroll past a blank wall, or a turn into a side panel) before the primary content appears.
11. **Interaction:** Hover states darken the surround instead of lightening the target, so the focus is carved out of shadow.

## What this artist would reject
- Equal-weight card grids with drop shadows and 12 px rounded corners.
- A hero that announces everything on arrival, with no threshold.
- Multi-hue palettes and gradient buttons. Color enters only through an opening.
- Decorative illustration in place of material texture.
- Snappy 150 ms springs and confetti.
- Plastered-over structure that hides the grid instead of showing it.

## Signature prompt seed
Design this screen as a poured-concrete room in Ando's manner. Lay out on a 1:2 tatami module with faint tie-hole dots, in mid-grey `#8E8D88` with deep shadow `#1C1C1B`. Split the view into three equal bands and leave the center one empty except for drifting light, so the user must cross it. Cut one precise slot of `#F4F1E8` light to mark the single primary action. Allow one 15° wall. Show blue only through a masked window. Use small tracked grotesk type and slow 1 s reveals from darkness. Arrival should be indirect.

## Sources
- https://en.wikipedia.org/wiki/Church_of_the_Light
- https://en.wikipedia.org/wiki/Row_House_in_Sumiyoshi
- https://archeyes.com/row-house-by-tadao-ando-azuma-house-light-space-concrete/
- https://www.witoldrybczynski.com/?p=3797
- https://dimensions.com/element/concrete-wall-site-cast-panels-3x6
- https://en.wikipedia.org/wiki/Chichu_Art_Museum
- https://benesse-artsite.jp/en/art/chichu.html
- https://artsandculture.google.com/story/kgUBINjNbw6Nfg
- https://www.pritzkerprize.com/biography-tadao-ando
