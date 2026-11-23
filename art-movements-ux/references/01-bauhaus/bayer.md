# Herbert Bayer — Bauhaus

## Essence
Bayer treated design as an engineering problem of perception. Letters become a circle and a bar, a page becomes bars and fields of red and black, a room becomes sightlines around one eye. He cut whatever did not carry information (capitals, serifs, centered symmetry, the straight-ahead gaze) and ordered the rest so it reached the eye in sequence.

## Key works examined
- **universal alphabet, 1925 (published in *Offset* no. 7, 1926)**: one case only, built from a circle and a horizontal bar so it could be drawn with ruler and compass. The lesson is to build a type system from 2–3 primitives and drop redundant variants.
- **Kandinsky 60th-birthday exhibition poster, 1926** (47.7 × 63 cm, red and black on white): one accent color plus black, with heavy rules used as structure rather than ornament.
- **Diagram of the field of vision, 1930 (Werkbund, Paris), revised 1935**: an eye at the center with panels set above, below and around it. The lesson is that the viewport is a cone, not a rectangle.
- **Section Allemande, Grand Palais, 1930**: chairs mounted on a wall, plus a bridge that lifted visitors so they could see from above. Change the viewer's position to change what reads first.
- **Road to Victory, MoMA, 1942**: over half the route ran along a ramp, so large and small photographs were seen from both far and near. Pacing is designed.
- **World Geo-Graphic Atlas, 1953** (368 pp., 56 × 40 cm, all Futura): pictograms in the manner of Neurath, thematic maps, cross-sections and charts set on one grid as a visual narrative.

## Space & composition
- **Asymmetric, weighted to the left.** Text blocks hang off a strong vertical axis that sits at about 1/3 of the width. The right two-thirds stay open or hold one large image.
- **Rules as architecture.** Thick bars (8–16 px at screen scale) mark zones, underline headings, or run fully off-canvas. Use them in place of boxes and cards. Bayer framed with bars, never with containers.
- **Peripheral planning.** The field-of-vision diagram tilts panels toward the eye at the top and bottom edges of vision. In UI, content at the viewport margins (sticky headers, footers, side rails) should be shaped for glancing: shorter, larger and higher in contrast than content in the center.
- **Atlas density.** Pair a dense grid of small multiples with one dominant figure. Never put two hero elements on one screen.

## Color
The base is black plus one primary on paper white. Blue and yellow, the other Kandinsky primaries, appear only for coding, as in maps or the 1923 stairwell murals with one color per level. Color means something before it sets a mood.

| Role | Hex |
|---|---|
| Ground (warm offset paper) | `#F4F1EA` |
| Ink (text, rules) | `#141414` |
| Signal red (one accent per view) | `#D7261E` |
| Data blue (secondary category) | `#1D4E9E` |
| Data yellow (tertiary, highlight) | `#F2C200` |
| Map neutral (inactive regions, gridlines) | `#B9B3A6` |

## Form, line & typography
Use a geometric sans with a single-story "a", lowercase by default (one alphabet is enough). Set headlines heavy and tightly tracked, and body text in the same family at regular weight. Letters are a circle plus a stem: round counters, flat terminals, no humanist quirks.

Fonts: **Jost** (the closest free Futura analogue, with a geometric "a" option), **Josefin Sans** (thinner, closer to the universal drawings), and **League Spartan** for heavy display.

## Rhythm, motion & time
Bayer's exhibitions were choreographed paths: ramps, bridges, footprints on the floor (1938). Motion should feel like guided travel, not bounce.
- Elements enter along the reading axis with ease-out timing of 240–320 ms. No springs, no scale-pop.
- Scroll like the ramp: a large figure stays pinned (`position: sticky`) while small captions pass, which gives the near/far rhythm of *Road to Victory*.

## UI translations
1. **Layout:** Put a hard vertical axis at 33.3% of the width. Every text block aligns its left edge to it, and only one image may cross it.
2. **Layout:** Replace cards with 12 px black bars. A section is defined by a bar above it and empty space below it, with no borders or shadows.
3. **Color:** Allow exactly one red element per screen (the primary action or the key number). Blue and yellow appear only inside data visualizations.
4. **Type:** Set all UI labels, nav and headings in lowercase with `text-transform: lowercase` (keep the source text accessible). Use capitals only for acronyms in body copy.
5. **Type:** Give display headlines a weight of 700–800 with `letter-spacing: -0.02em`, sized at least 4× body. Bayer used a few dramatic sizes, not gentle steps.
6. **Composition:** Turn one section label 90° and pin it to the left gutter as a running spine.
7. **Peripheral design:** Reduce sticky header and footer content to one or two glanceable items at 1.25× normal size, treating them as panels tilted toward the eye.
8. **Data:** Show quantities with repeated pictograms (Isotype rows) rather than bars where counts are small, with one icon equal to one fixed unit.
9. **Motion:** Draw rules in from the left (`scaleX` from 0) over 200 ms, then fade text in 80 ms later along the same axis, so structure comes before content.
10. **Interaction:** On hover, turn the data row signal red and every other row map-neutral, so focus comes from muting everything else.

## What this artist would reject
- Title Case and ALL-CAPS buttons, which add a second alphabet for nothing.
- Centered hero stacks with symmetric padding.
- Rounded cards with drop shadows, which hold content in boxes when bars would structure it.
- Gradients and multi-hue "brand palettes" where color carries no meaning.
- Decorative illustrations that encode no data.
- Bouncy spring animations that draw attention to the motion instead of guiding the eye.

## Signature prompt seed
Design this screen like a Herbert Bayer Bauhaus print. Use warm off-white paper, black ink and one signal-red element. Set everything in lowercase geometric sans (Jost), with huge heavy headlines and small precise body text. Hang all text off a vertical axis one-third from the left, and divide zones with thick black bars instead of cards. Turn one label 90° along the gutter. Show data as Isotype pictogram rows and atlas-style small multiples next to one dominant figure. Keep the edges of the viewport short and glanceable. Motion should travel along one axis like a guided ramp: rules draw in first, then content follows.

## Sources
- https://letterformarchive.org/news/bauhaus-typefaces-part-two/
- https://theartstory.org/amp/artist/bayer-herbert/
- https://eyeondesign.aiga.org/herbert-bayers-world-geo-graphic-atlas-anticipated-the-age-of-infographics/
- https://exhibitions.letterformarchive.org/bauhaus/walkthroughs/bayer-s-world-geographic-atlas
- https://peoplesgdarchive.org/item/14390/poster-for-kandinsky-exhibition-honoring-the-artists-60th-birthday
- https://www.designboom.com/art/peripheral-vision-artwork-exceeds-eye/
- https://monoskop.org/images/1/1f/Bayer_Herbert_1961_Aspects_of_Design_of_Exhibitions_and_Museums.pdf
