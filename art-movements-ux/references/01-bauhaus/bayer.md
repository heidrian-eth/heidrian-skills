# Herbert Bayer — Bauhaus

## Essence
Bayer treated design as an engineering problem of perception. Letters become a circle and a bar, a page becomes bars and fields of red and black, a room becomes sightlines around one eye. He cut whatever did not carry information (capitals, serifs, centered symmetry, the straight-ahead gaze) and ordered the rest so it reached the eye in sequence.

## Key works examined
- **universal alphabet, 1925 (published in *Offset* no. 7, 1926)**: one case only, built from a circle and a horizontal bar so it could be drawn with ruler and compass. The lesson is to build a type system from 2–3 primitives and drop redundant variants. *(visually checked: V&A proof sheet, c.1926. Single-storey a, round counters, flat terminals, a giant textured "d" as a sign beside the alphabet; the block's left edge sits at 34% of the sheet width; the small captions are set in tiny bold caps)*
- **Kandinsky 60th-birthday exhibition poster, 1926** (47.7 × 63 cm, red and black on white): one accent color plus black, with heavy rules used as structure rather than ornament. *(not visually checked: no image reachable from the allowed sources)*
- **Thuringian emergency banknotes, 1 and 2 million mark, 1923 (V&A)** *(added; visually checked)*: a solid colour bar (red, or grey on the 2-million note) holding huge bold black numerals, a striped multi-line rule under it, a micro-texture of repeated numerals, and two text columns rotated 90° at the right edge (≈70–90% of the width). The red block plus its stripes cover ≈20% of the note.
- **Breuer Metallmöbel catalogue, 1927 (V&A)** *(added; visually checked)*: a negative (inverted) photograph on a black panel, an ALL-CAPS geometric-sans headline, and hairline leader lines with arrowheads running from tiny caps labels to the parts of the chair.
- **50 Jahre Bauhaus poster, 1968 (AIC)** *(added; visually checked)*: lowercase universal-style wordmark across the top, flush-left text at 8% of the width, and circle/square/triangle in blue, red and yellow on a blue ground (blue 49%, red 8.5%, yellow 5.8%). Late work; it breaks the "one red, blue and yellow only for data" rule.
- **Diagram of the field of vision, 1930 (Werkbund, Paris), revised 1935** *(not visually checked)*: an eye at the center with panels set above, below and around it. The lesson is that the viewport is a cone, not a rectangle.
- **Section Allemande, Grand Palais, 1930**: chairs mounted on a wall, plus a bridge that lifted visitors so they could see from above. Change the viewer's position to change what reads first.
- **Road to Victory, MoMA, 1942**: over half the route ran along a ramp, so large and small photographs were seen from both far and near. Pacing is designed.
- **World Geo-Graphic Atlas, 1953** *(retry pass, visually checked: Cooper Hewitt scan of the spread "World Annual Rainfall and Ocean Currents", object 68776127)* (368 pp., 56 × 40 cm, all Futura): pictograms in the manner of Neurath, thematic maps, cross-sections and charts set on one grid as a visual narrative. Seen on the spread: one world map in an interrupted equal-area projection fills the double page (≈90%), text reduced to a small legend column at the left edge and a red running head ("world geo-graphic atlas container corporation of america", tracked caps) top right. Data is encoded in muted tints, not primaries: rainfall as a sequential ramp pale yellow `#D0C580` → green `#B1AE81` → blue `#588CA0` on land, ocean currents as hundreds of fine lines, warm currents red-pink, cold ones blue. So in a data view red and blue become a paired encoding drawn as hairlines, while the single-red rule holds for the page furniture (the running head). Colours are from a scan of a 1953 offset print and read faded.

## Process (derived)
*From observation to process (see SKILL.md §1). This is what transfers; the rest of the file is evidence.*

**Herbert Bayer.** *Decide the order in which things must reach the eye, then give each rank a channel of its own (size, the one colour, orientation, attachment) and delete every variant that carries no information.*
Process:
1. Rank the content into at most four reading ranks: seen at a glance, read, consulted, kept for reference. Everything that follows assigns channels to ranks, so an unranked item cannot be placed.
2. Cut redundant variants before composing: one letter case per rank, one family, marks and glyphs built from 2–3 primitives. A distinction that does not change the meaning is removed.
3. Give rank 1 a single dominant figure. If it is a number or word it takes about 20% of the surface; if it is an image, map or chart it takes 70–90% and text shrinks to an edge column. Never two.
4. Hang all text from one hard edge on the reading side, 5–8% in from the frame (about 1/3 across only when the figure occupies the near side). Mark zones with solid bars, not boxes; one bar may thicken into the field that holds the rank-1 item.
5. Spend the single saturated colour on rank 1 or on the furniture that names the page, never on both. It may be large (up to 20%). Inside data, other hues appear only as low-chroma ramps, plus at most one opposed pair of hairline colours for a paired quantity.
6. Demote by orientation and distance: rank-4 text goes to the far edge (70–90% across) in a narrow column turned 90° (decorative or secondary text only; never a control), at the smallest size that still meets the 12px floor. It is found only by someone who looks for it.
7. Attach every label to the thing it names with a hairline leader ending at the part. No detached legend where a leader will do.
Why it works:
- Size, colour and orientation are separate preattentive channels. With one channel per rank, the order is read before any word is. Two ranks sharing a channel (two sizes that are close, two accents) make the eye arbitrate, and the sequence is lost.
- Salience is oddness: one saturated element among neutrals wins at any size. A second one halves it; a saturated data palette under it drowns it, which is why data colour is kept low in chroma.
- A leader replaces a look-up. A detached legend makes the reader hold a code in memory and travel back and forth; connection does the same work in one fixation.
Colour relations: neutral ground and one ink carry everything but rank 1; one saturated colour, ≤20%, in one place; data ramps of low chroma in 3 steps; one opposed pair as hairlines only; a neutral bar may stand in for the saturated one in a variant.
Space and line: one hard text edge at 5–8% (or ≈1/3); one dominant figure; bars of two kinds (a solid bar, and a band of thin rules under it); hairline leaders; a rotated edge column at 70–90% across; no boxes.
Type requirement: one family with a heavy and a regular weight, simple round forms and no redundant alternates; one case for display, small spaced capitals only for technical labels; numerals strong enough to be the rank-1 figure; rotated text limited to short reference labels, never instructions.
Motion and interaction: a state change is a change of rank. The promoted item takes the rank-1 channel (its bar extends along the text edge and fills, 240–320ms, no overshoot) and the previous holder gives it up; the dominant figure stays pinned while lower ranks pass it; hover and selection always add a bar or weight change, not colour alone.
Fails when: the content has no ranks (a feed or gallery of equal items); several items need the alarm colour at once (an incident board); categories in the chrome need more than one saturated hue; rank-4 text is long or legally required to be legible, so it cannot be rotated or shrunk.
Signature (do not carry together): lowercase geometric sans · heavy black bars with one red block · a text column turned 90° at the right edge.

**Transfer test** (an illustration that the process survives new colours and content; never reuse its hues, layout or wording as a design answer):

Product: a poetry-reading and sleep wind-down app, phone 390 × 844, dusk violets, soft and lyrical. The source is utilitarian print in neutral, ink and one hot colour.
1. *Ranks.* 1: the line being read now. 2: the stanza around it. 3: title and poet. 4: source, translator, licence.
2. *Variants cut.* One serif family, sentence case only, two weights. No italics, no second face, no icons beyond a bar and a dot.
3. *Dominant.* The current line at 34px takes about 20% of the screen (a band 170px high). Nothing else exceeds 16px.
4. *Edge and bars.* All text hangs from x = 24px (6%). A 6px bar in a violet 12 L above the ground sits under the title; it thickens to the 170px band that holds the current line.
5. *The one colour.* The band is the only saturated field: a deep rose at about 18% of the area, the single warm note on a violet ground. Reading-progress ticks are a three-step low-chroma violet ramp.
6. *Demotion.* Source and translator run up the right edge at x = 85%, turned 90°, 11px, two short labels only. The licence text is a normal upright sheet behind a control, because it must be readable.
7. *Attachment.* A footnote mark in a line has a hairline leader to its gloss in the margin; there is no glossary screen.
- *Interaction.* Advancing a line moves the band: the next line's bar extends from the text edge and fills over 280ms while the previous band thins back to 6px. The band also sets heavy weight, so rank is not carried by colour alone.
- *Check.* Hide the rose band: the screen has no first read. Add a second rose element (a "favourite" dot): the band stops winning, so the dot is drawn in the ground ramp.
Result: a dim violet page with one warm band and a quiet turned label. No lowercase sans, no black bars, no red-on-paper. What survived is one channel per rank and a single dominant.

## Space & composition
- **Asymmetric, weighted to the left.** Text blocks hang flush-left off one strong vertical axis. Its position varies: 34% of the width on the universal-alphabet sheet, 5–8% on the 1923 banknotes and the 1968 poster. The rest stays open or holds one large image or block.
- **Rules as architecture.** Thick bars (8–16 px at screen scale) mark zones, underline headings, or run fully off-canvas. Use them in place of boxes and cards. Bayer framed with bars, never with containers. On the 1923 notes the bar grows into a solid field that holds the main number, with a striped band of thin rules beneath it.
- **Rotated columns.** Whole text columns, not just one label, run at 90° along the right edge (1923 notes).
- **Leader lines.** Hairline callouts with arrowheads tie small labels to parts of an image (Breuer catalogue, 1927).
- **Peripheral planning.** The field-of-vision diagram tilts panels toward the eye at the top and bottom edges of vision. In UI, content at the viewport margins (sticky headers, footers, side rails) should be shaped for glancing: shorter, larger and higher in contrast than content in the center.
- **Atlas density.** Pair a dense grid of small multiples with one dominant figure. Never put two hero elements on one screen.

## Color
*The hex table below is a reference sample for strict studies and homage only. For design, use the colour relations in "Process (derived)".*

The base is black plus one primary on paper white. Blue and yellow, the other Kandinsky primaries, appear only for coding, as in maps or the 1923 stairwell murals with one color per level. Color means something before it sets a mood. The single red is not necessarily small: on the 1923 note it is a block of ≈20% of the surface that carries the key number. Samples: paper and ink from the V&A sheets (aged paper, so the ground reads warmer than it was printed), red, blue and yellow from the 1968 AIC poster (the 1923 red has faded to `#9D4B3C`).

| Role | Hex |
|---|---|
| Ground (warm offset paper) | `#F1EBD8` |
| Ink (text, rules) | `#2D2B2D` |
| Signal red (one accent per view) | `#E20A14` |
| Data blue (secondary category) | `#01378F` |
| Data yellow (tertiary, highlight) | `#FDBD1F` |
| Map neutral (inactive regions, gridlines) | `#B7B5AB` |
| Map tint ramp (added; atlas rainfall, low → high) | `#D0C580` → `#B1AE81` → `#588CA0` |

## Form, line & typography
Use a geometric sans with a single-story "a", lowercase by default (one alphabet is enough). In practice Bayer kept caps for small technical text: the captions on the alphabet sheet, the leader labels and the headline of the 1927 Breuer catalogue, and all text on the 1923 notes are capitals. Lowercase is the rule for display and wordmarks; tiny tracked caps are allowed for labels. Set headlines heavy and tightly tracked, and body text in the same family at regular weight. Letters are a circle plus a stem: round counters, flat terminals, no humanist quirks.

Fonts: **Jost** (the closest free Futura analogue, with a geometric "a" option), **Josefin Sans** (thinner, closer to the universal drawings), and **League Spartan** for heavy display.

## Rhythm, motion & time
Bayer's exhibitions were choreographed paths: ramps, bridges, footprints on the floor (1938). Motion should feel like guided travel, not bounce.
- Elements enter along the reading axis with ease-out timing of 240–320 ms. No springs, no scale-pop.
- Scroll like the ramp: a large figure stays pinned (`position: sticky`) while small captions pass, which gives the near/far rhythm of *Road to Victory*.

## UI translations
1. **Layout:** Put one hard vertical axis at 33.3% of the width (this figure comes from the universal-alphabet specimen sheet only, ≈34%) or flush-left near the margin (5–8%, as on the banknotes and posters). Every text block aligns its left edge to it, and only one image may cross it.
2. **Layout:** Replace cards with 12 px black bars. A section is defined by a bar above it and empty space below it, with no borders or shadows.
3. **Color:** Allow exactly one red element per screen (the primary action or the key number). Blue and yellow appear only inside data visualizations.
4. **Type:** Set nav and headings in lowercase with `text-transform: lowercase` (keep the source text accessible). Tiny technical labels and annotations may be tracked caps, as in his catalogues.
5. **Type:** Give display headlines a weight of 700–800 with `letter-spacing: -0.02em`, sized at least 4× body. Bayer used a few dramatic sizes, not gentle steps.
6. **Composition:** Turn one section label, or a whole narrow text column, 90° and pin it to the gutter as a running spine.
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
Design this screen like a Herbert Bayer Bauhaus print. Use warm off-white paper, black ink and one signal-red element. Set everything in lowercase geometric sans (Jost), with huge heavy headlines and small precise body text. Hang all text off one strong vertical axis (one-third from the left as on the alphabet specimen sheet, or near the left margin as on the posters), and divide zones with thick black bars instead of cards. Turn one label 90° along the gutter. Show data as Isotype pictogram rows and atlas-style small multiples next to one dominant figure. Keep the edges of the viewport short and glanceable. Motion should travel along one axis like a guided ramp: rules draw in first, then content follows.

## Sources
- https://letterformarchive.org/news/bauhaus-typefaces-part-two/
- https://theartstory.org/amp/artist/bayer-herbert/
- https://eyeondesign.aiga.org/herbert-bayers-world-geo-graphic-atlas-anticipated-the-age-of-infographics/
- https://exhibitions.letterformarchive.org/bauhaus/walkthroughs/bayer-s-world-geographic-atlas
- https://peoplesgdarchive.org/item/14390/poster-for-kandinsky-exhibition-honoring-the-artists-60th-birthday
- https://www.designboom.com/art/peripheral-vision-artwork-exceeds-eye/
- https://monoskop.org/images/1/1f/Bayer_Herbert_1961_Aspects_of_Design_of_Exhibitions_and_Museums.pdf
- Images (visual check): https://collections.vam.ac.uk/item/O1348589 (universal alphabet proof, framemark 2006AM9802), https://collections.vam.ac.uk/item/O1035784 and https://collections.vam.ac.uk/item/O1035743 (1923 notes, framemark 2015HJ9709, 2015HK0008), https://collections.vam.ac.uk/item/O113441 (Breuer Metallmöbel, framemark 2006AB5930), https://www.artic.edu/artworks/229987 (50 Jahre Bauhaus, IIIF 68dd42d0-540b-ae57-8365-bd3476a655f7)
- Retry pass: Cooper Hewitt, Smithsonian Design Museum, object 68776127 (World Geo-Graphic Atlas, rainfall and ocean currents spread): https://images.collection.cooperhewitt.org/93886_894724f679ab5e05_b.jpg
