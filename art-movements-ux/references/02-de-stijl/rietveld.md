# Gerrit Rietveld — De Stijl

## Essence
Rietveld was a cabinetmaker who built space out of separate parts that slide past each other and never quite meet. He made rooms that rearrange themselves over the day and chairs whose rails run past every joint. Each part keeps its own colour, and the space is the gap between parts.

## Key works examined
- **Red Blue Chair, 1918 (painted c.1923)**: square beech rails pegged where they cross. The frame is black, the cut ends yellow, the back a red plane and the seat a blue one, tilted against the frame. Lesson: a structure can be legible as layers that never touch at their edges.
- **Rietveld Schröder House, Utrecht, 1924**: the upper floor is one open room by day. In the evening, sliding walls split it into three rooms (two children's rooms and a living room). Lesson: the layout is a state, not a fixed fact.
- **Schröder House corner window**: two casements open at right angles and the corner post disappears. Lesson: remove the corner and the edge turns into a threshold.
- **Schröder House façade**: wall planes and linear bars in white, grey, black and the primaries, sticking out past the volume. Lesson: colour identifies parts; it doesn't set mood.
- **Zig-Zag Chair, 1934**: four beech planks with mitred joints, bolts and triangular blocks. No legs, a Z shape about 66 × 78 × 76 cm, and a slot in the back to lift it by. Lesson: one continuous folded path, with its fasteners left on show as the only ornament.

## Space & composition
- **Planes overshoot their joints.** At every crossing, each element runs 8–16px past the edge of the one it meets, like the chair's rails. Containers are overlapping slabs on different z-levels, not boxes with shared borders.
- **Plan as state machine.** Each screen has at least two named layouts, "day" (open) and "night" (divided), built from the same panels. Panels slide on tracks to switch between them, with no navigation to a new page.
- **Asymmetric 3-track grid** in roughly 1 : 1.6 : 0.6 proportions. The narrow track holds controls. Columns are never equal.
- **Dissolved corners.** At least one corner of the main panel has no border and no radius. That edge opens straight into the next region, like the corner window.
- **Density:** about 55% white or grey ground, colour on under 15% of surfaces. Content sits on planes, never on bare background.

## Color
Colour marks what kind of part something is, and each colour does one job only.
- `#F4F2EC` white plane (main ground)
- `#B9B8B3` grey plane (recessed or inactive panels, the night state)
- `#151515` black (structure: rails, rules, dividers, frames)
- `#C8261E` red (the backrest: the one surface that holds the user's main thing)
- `#1F4E9A` blue (the seat: the surface where you put input)
- `#F2C230` yellow (only on ends: cut edges, handles, endpoints of the active selection)

The rule: black lines carry the structure and coloured planes carry meaning. Yellow appears only where an element ends.

## Form, line & typography
The form language is square-section rails plus flat rectangles. There are no curves, no gradients, and only 0–2px radii. In type, that means a straight-sided grotesque with square terminals for the body, condensed vertical labels running up the rails, and mono labels at the joints as visible bolts. Fonts: **Archivo** (variable width, good both expanded and condensed), **Space Mono** (labels and bolts), and optionally **Big Shoulders Display** for tall section numerals.

## Rhythm, motion & time
- Motion is **translation along tracks only**. Panels slide in x or y over 280–360ms with `cubic-bezier(.6,0,.2,1)`, like a heavy door on a runner.
- Reconfiguring is shown in steps: one partition moves, then the next, staggered 60ms apart, so the user can see the room being divided.
- Time of day is a real input: "divided" closes partitions for focus, "open" gives overview.

## UI translations
1. **Layout:** Build the main screen from 3–5 absolutely positioned slabs with different `z-index` values. Each overlaps its neighbour by 12px, so no two share an edge.
2. **Layout:** Extend every horizontal rule 16px beyond the container it divides, both left and right (`margin-inline: -16px`).
3. **Interaction:** Add a single "partition" toggle that slides 2–3 panels into place over 320ms, turning one open dashboard into three separate workspaces without leaving the page.
4. **Interaction:** Make panels draggable along a fixed track only (one axis each), with snap stops at grid lines.
5. **Color:** Use red for exactly one surface per screen, the primary content plane. Blue goes on input surfaces only, yellow only on ends: the leading cap of a progress bar, a drag handle, the end of a selected range.
6. **Color:** Draw structure as 4–6px black bars, never grey hairlines or shadows.
7. **Type:** Put mono labels like `01 / SEAT` exactly at the points where rails cross, as visible bolts.
8. **Motion:** Animate only `transform: translate`. Drop opacity and scale transitions entirely.
9. **Layout:** Leave one corner of the main card with no border, so it opens into the next panel or the page edge.
10. **Interaction:** Give movable panels a cutout handle (a 6 × 32px notch in the edge) instead of an icon button, like the slot in the Zig-Zag back.
11. **Flow:** Build onboarding as a single Z-path ribbon: right, down, right. Each fold is a step and fasteners (step numbers) show at each fold.

## What this artist would reject
- Rounded cards on soft shadows: elevation faked with blur, not real overlap.
- Modals and route changes for what should be a rearrangement of the same room.
- Decorative colour, gradients, or brand tints used for mood instead of to name a role.
- Hidden structure: borderless layouts where alignment is implied but never drawn.
- Springy, scaling, or fading motion that hides how a part actually moves.

## Signature prompt seed
Design this app screen as a Rietveld interior. Build it from flat slabs and 5px black rails that cross and run 16px past every joint, so nothing shares an edge or a corner. Use an off-white ground and grey recessed panels. Put red on the single main content plane, blue on input surfaces, and yellow only where elements end. Give the layout two states, open and divided, toggled by panels sliding on one-axis tracks over 320ms with no fades. Use Archivo, with Space Mono labels placed at the joints like visible bolts. Leave one corner open to the next region.

## Sources
- https://www.moma.org/collection/works/4044
- https://collections.vam.ac.uk/item/O142927/the-red-blue-chair-armchair-rietveld-gerrit
- https://en.wikipedia.org/wiki/Red_and_Blue_Chair
- https://rietveldschroderhuis.nl/en
- https://www.architecturelab.net/rietveld-schroder-house-gerrit-rietveld/
- https://collections.vam.ac.uk/item/O142934/zig-zag-chair-chair-rietveld-gerrit/
