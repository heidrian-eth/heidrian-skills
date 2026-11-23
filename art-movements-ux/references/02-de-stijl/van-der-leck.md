# Bart van der Leck — De Stijl

## Essence
Van der Leck never let go of the figure. He cuts a real scene (workers leaving a factory, passengers on a deck) into short flat bars of red, yellow, blue and black that float apart, never touching, on an open white field. The scene stays legible, held together only by where each bar sits and which way it leans.

## Key works examined
- **Batavier Line poster, 1915–16** (lithograph, 77.7 × 114.6 cm, Kröller-Müller). A commission for Wm H. Müller & Co.'s Rotterdam–London line. Passengers become flat colour planes; the version usually reproduced today is a 1920 alteration he disowned.
- **Composition 1917 No. 4 (Leaving the Factory)** (oil, 95.5 × 102.2 cm). Tight verticals at the top read as factory and chimney, staggered small blocks in the middle are the crowd, and horizontal stripes below are the street.
- **The "Leaving the Factory" series, 1916–17.** The same scene moves from realistic to nearly abstract over several versions. A model for progressive disclosure.
- **Delft Salad Oil poster, 1919 (unprinted).** Lettering too radical for the client; type becomes image.
- **Metz & Co. identity, from 1930.** Branding plus a rectilinear geometric alphabet; fabrics in his vermillion, cornflower and canary, first used in the Sonneveld House.
- **H.C. Andersen, *Het Vlas*, 1941.** About a dozen pages, called a "small masterpiece" of Dutch book design. Type is cut from discrete bars and the illustrations are fragments floating on white.

## Space & composition
- **White is the medium, not the background.** Usually 70–85% of the surface stays untouched, read as one shape with the bars as events inside it.
- **Separation is the rule.** Elements almost never touch or overlap. There is a constant gap of white between neighbours, roughly 0.5–1× the bar's thickness. Think `gap`, never `border`.
- **Banded semantics.** In *Leaving the Factory* the canvas splits into three horizontal zones: dense verticals at the top, scattered mid-size blocks in the middle, long thin horizontals at the bottom.
- **The diagonal is allowed.** Unlike Mondrian, van der Leck kept diagonals after 1918. A minority of bars, maybe 10–20%, tilt (often 45° or close to it), and that tilt carries the motion.
- **Near-square formats.** 95.5 × 102.2 is almost 1:1, and the poster is roughly 2:3. Calm frames; tension lives in the fragments.

## Color
The logic: from 1916 on, pure primaries plus black, laid flat with no gradient, each colour used in small amounts so the white stays in charge. Colour tells you what something is, not how important it is.

| Hex | Role |
|---|---|
| `#F7F5EF` | Field: the warm white ground, at least 70% of every screen |
| `#D52B1E` | Vermillion: action and focal fragments |
| `#2456A6` | Blue: structure and navigation bars |
| `#F3C316` | Canary yellow: highlights and state change |
| `#141414` | Black: thin bars, type strokes, never fills |
| `#7C9BD6` | Cornflower (Metz textile variant): secondary or quiet surfaces |

## Form, line & typography
His letters follow the same rules as his pictures: built from straight bars with a few diagonals, strokes that stop short of each other, and counters that open into the surrounding white. The Metz alphabet started out as stencil lettering, which is why the strokes break. In *Het Vlas* the type and the illustrations are clearly cut from the same pieces. The 1994 revival, Architype van der Leck, isn't free. Alternatives:
- **Big Shoulders Stencil Display** (Google Fonts): condensed and stencil-broken, for headlines.
- **Major Mono Display** (Google Fonts): geometric, built from unusual constructions, for labels and numerals.
- **Jost** (Google Fonts): plain geometric sans for body text, so the display type stays special.

## Rhythm, motion & time
The figure-to-abstraction series is itself a motion idea: interfaces can *assemble* and *disassemble*. On load, bars slide 8–16px into place one after another, staggered 40–60ms apart, with no fades and nothing bouncing. On hover, a fragment shifts or rotates a few degrees. Use short ease-out tweens (120–200ms), clipped like stencil cuts, never springy.

## UI translations
1. **Layout:** Build every screen from a 12-column grid, but put content in at most 4–6 rectangular "bars" whose total area stays under 30% of the viewport. Leave the rest as `#F7F5EF`.
2. **Layout:** Keep a uniform gap (`gap: 0.75em` or `12px`) between all blocks and never use borders or dividers. Separation comes from white alone.
3. **Layout:** Split long pages into horizontal bands, each with its own density: a header band of tightly packed vertical slivers (nav), a middle band of scattered cards in staggered positions, and a footer of long thin horizontal rules.
4. **Color:** Give every primary one semantic job: red for actions, blue for navigation, yellow for state, black for text. Never put two primaries next to each other without white between them.
5. **Color:** Use solid fills only. No gradients, no shadows, no tints below 100% except the single cornflower secondary.
6. **Type:** Set headlines in a stencil face at large size with wide tracking (`letter-spacing: 0.08em`), so the breaks in each letter echo the gaps between blocks.
7. **Type:** Build icons from 2–4 disconnected strokes (CSS bars or SVG `<line>`s with gaps) instead of closed outlines.
8. **Composition:** Tilt exactly one element per screen (badge, primary CTA or progress marker) by `rotate(-12deg)` to `rotate(45deg)`.
9. **Motion:** On first load, bring blocks in on a stagger from the edge they point toward, as if the composition is assembling.
10. **Interaction:** Progressive abstraction for illustration and empty states. Show a recognisable figure built from bars; on task completion the bars drift apart into pure abstraction.
11. **Interaction:** Use colour instead of hover outlines. A hovered card changes fill from blue to red; nothing else moves.

## What this artist would reject
- Rounded cards with drop shadows sitting on a grey canvas. Volume and elevation make a lie of the flat plane.
- Containers that touch or nest: boxes inside boxes inside a bordered panel.
- Gradients, glassmorphism, blurred backdrops.
- Full-bleed hero photography that crowds the white field out.
- Subjectless decoration: he insisted on staying tied to ordinary life.
- Colour used as a brand wash, like a blue header bar running across the whole width.

## Signature prompt seed
Design this app screen on a warm white field (#F7F5EF) covering at least 70% of the viewport. Build content from four to six flat rectangular bars in vermillion, blue, canary and black. The bars never touch, have a uniform 12px white gap between them, and use no borders, shadows or gradients. Arrange them in horizontal bands: dense vertical slivers on top, scattered staggered blocks in the middle, long thin rules below. Tilt exactly one element diagonally. Set headlines in condensed stencil type with wide tracking. Build icons from disconnected strokes. Animate blocks assembling one after another on load, with crisp 150ms motion and no bounce.

## Sources
- https://www.krollermuller.nl/en/collection/bart-van-der-leck-poster-batavier-line-km-121-068
- https://www.krollermuller.nl/en/collection/bart-van-der-leck-composition-1917-no-4-leaving-the-factory-km-100-312
- https://designmuseumdedel.nl/en/tentoonstelling/bart-van-der-leck-designs-for-posters/
- https://www.sonneveldhouse.com/node/118
- https://en.wikipedia.org/wiki/Bart_van_der_Leck
- https://luc.devroye.org/fonts-50285.html
- https://designersandbooks.com/blog/dutch-book-design-1914-1945
- https://risdmuseum.org/art-design/collection/flax-het-vlas-20037/print
