# Piet Mondrian — De Stijl

## Essence
Mondrian builds balance from inequality. Black orthogonal bars split an off-white field into cells that are never equal, and a few flat primaries sit at the edges, so a small, heavy color area offsets a large, quiet void. In New York he removed the black and turned the grid into syncopated traffic. The system was about rhythm, not boxes.

## Key works examined
- **Tableau I, 1921**: off-white grounds and small primary blocks, with lines that stop short of the edges. Teaches: a rule can end.
- **Tableau No. IV; Lozenge Composition, c. 1924/25** (142.8 × 142.3 cm, NGA): an upright grid in a canvas turned 45°. The edge cuts the colored cells into triangles, and the lines were thickened in a repaint. Teaches: let the container crop the system.
- **Composition C (No. III) with Red, Yellow and Blue, 1935** (Tate): the mature grid, with doubled lines and color at the margins. Teaches: put weight at the edges and keep the center empty.
- **Composition with Yellow, Blue and Red, 1937–42** (Tate): a dense mesh of bars, with thin ones bunched close together. Teaches: the gaps between lines carry rhythm.
- **Broadway Boogie Woogie, 1942–43** (127 × 127 cm, MoMA): no black. Yellow lanes are broken up by red, blue and gray blocks. Teaches: turn borders into signals.
- **Victory Boogie Woogie, 1942–44** (Kunstmuseum Den Haag): his last work, an unfinished lozenge still carrying taped paper strips. Teaches: a composition can stay open to change.

## Space & composition
- **Unequal cells.** No two neighboring cells are the same size. Neighbor ratios run from about 1:1.6 to 1:4, and one near-square cell takes 35–50% of the area, placed off-center.
- **Edge-loaded color.** Primaries sit in cells that touch the frame, often cut off by it. The biggest cell stays white.
- **Lines of different weights.** At screen scale, mix bars of about 6, 10 and 16 px. A heavy bar marks a major division and a thin one a minor division. Two thin lines 8–12 px apart read as one "chord."
- **Lines that stop.** Some rules end short of the edge, so the grid never reads as a spreadsheet.
- **Lozenge.** Rotate the frame, not the grid. The 45° crop activates the edges and suggests space beyond the canvas.

## Color
He used primaries sparingly against what he called non-colors. Red, yellow and blue together rarely exceed 15–20% of the surface: one primary is large and the others are chips. The whites differ slightly from cell to cell; NGA notes hints of blue and gray. In Broadway Boogie Woogie, yellow takes over from black as the structural color.

| Role | Hex |
|---|---|
| Ground white (warm) | `#F2EFE6` |
| Ground white (cool variant) | `#E9EBEA` |
| Structure black | `#141414` |
| Red (dominant accent) | `#D0281F` |
| Blue (counterweight) | `#1D3D8F` |
| Yellow (chip / Boogie lane) | `#F2CB1D` |
| Gray (quiet cell) | `#BEBDB8` |

## Form, line & typography
No letterforms, but the line language maps directly: right angles only, with weight contrast doing all the expressive work. Use one geometric grotesk at two very different weights, 900 for a single corner-flush headline and 400 for everything else. Seat text against a rule the way color sits against a bar, and never center it. Fonts: **Archivo** (variable width, good for fitting text to a cell), **Space Grotesk**, and **Inter Tight** for dense data.

## Rhythm, motion & time
The Boogie Woogies pulse: MoMA describes blinking blocks moving from intersection to intersection like street traffic. Motion should run along the lines and never float. Show loading as chips moving down a yellow rule in an uneven 3-against-2 beat. In transitions, the bars slide and cells resize. Use `steps(6)` or `cubic-bezier(.7,0,.3,1)`, and never bounce. On hover, fill the cell with its primary in 120 ms, with no shadow and no scale change.

## UI translations
1. **Layout:** Use irregular grid tracks, such as `grid-template-columns: 3.2fr 1fr .45fr 1.6fr`. Never use `repeat(n, 1fr)`.
2. **Layout:** Make the main content a white near-square of about 45% of the viewport, left of center. Put navigation and metadata in thin cells along the right and bottom edges.
3. **Line:** Draw the rules with `gap` over a black background, not borders. Use a 14 px gap between regions and 6 px within them, plus one doubled 4 px + 4 px accent pair.
4. **Color:** Put the brand primary in one edge-touching cell only, at under 12% of the area. Add two chips of the other primaries, each under 3%, on opposite sides.
5. **Color:** Tint each white panel 2–3% differently so the field reads as painted, not `#FFF`.
6. **Type:** Set one 900-weight headline flush in the top-left corner of its cell, with line-height .95, sized so the cell edge clips it slightly.
7. **Type:** Align body text to cell edges with padding of 0.75× the adjacent gap.
8. **Motion:** Animate state changes by moving the `grid-template-columns` tracks over 300 ms. The selected panel grows and its neighbors yield.
9. **Interaction:** In a "Broadway mode" for live dashboards, drop the black rules and use yellow lanes as dividers. Red, blue and gray chips inside the lanes tick in place as real events.
10. **Interaction:** Make one feature card a lozenge: rotate the wrapper 45°, counter-rotate the inner grid, and let the edge clip the colored cells into triangles.
11. **Layout:** Stop one internal rule 24–40 px short of the edge so the system stays open.

## What this artist would reject
- Uniform card grids with equal gutters and identical tiles.
- Rounded corners, drop shadows, glassmorphism and gradients, which all bring back illusion.
- Centered, symmetrical hero sections with a single middle CTA.
- Color spread evenly as decoration, like tinted sections or rainbow tags.
- Curves or diagonals inside the grid. Only the lozenge's frame may be diagonal.
- Springy easing and floating particles.

## Signature prompt seed
Design this app screen as a Neoplastic composition. Use an off-white field split by black bars of three widths (about 4, 8 and 14 px) into strictly unequal rectangles, with no two neighbors the same size. Make one large white near-square, off-center, hold the main content. Confine red to a single edge-cropped cell under 12% of the area and add tiny chips of blue and yellow on opposite margins. Set one ultra-bold grotesk headline flush in a corner. Use no shadows, curves or rounded corners. On interaction, the bars slide and cells resize. In live states, yellow lanes carry blinking color blocks like traffic.

## Sources
- https://www.moma.org/collection/works/78682
- https://en.wikipedia.org/wiki/Broadway_Boogie_Woogie
- https://www.nga.gov/collection/art-object-page.52614.html
- https://piet-mondrian.org/tableau-i.jsp
- https://www.tate.org.uk/art/artworks/mondrian-composition-with-yellow-blue-and-red-t00648/
- https://www.tate.org.uk/art/artworks/mondrian-composition-c-no-iii-with-red-yellow-and-blue-l00097
- https://www.museum.nl/en/kunstmuseum-den-haag/showpiece/victory-boogie-woogie
