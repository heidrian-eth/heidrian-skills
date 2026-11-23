# David Carson — Grunge / Postmodern typography

## Essence
Carson treats a page as something you look at all at once, like a painting, before you read it in lines. Type works as image and texture, and the layout responds to how a piece *feels*, not to a grid. He rejects the idea that legibility and communication are the same thing: a page can be hard to read and still say a lot, or very easy to read and say nothing. Each layout is built by eye from cropping, collision and found scraps.

## Key works examined
- **Beach Culture (1989–91, six issues)**: the first full run of his experimental layouts. Shows that low-stakes products are where to push hardest.
- **Ray Gun (1992–c.1995)**: no page numbers, headings and pull-quotes left out, crops that cover text, typos left in. Shows that the navigation scaffolding itself is something you can design.
- **Bryan Ferry interview, Ray Gun (1994)**: he found the interview boring and set the whole spread in Zapf Dingbats, with readable text printed elsewhere as a supplement. Shows that an editorial verdict can be expressed through the typeface, as long as a legible fallback exists.
- **The End of Print (1995, with Lewis Blackwell)**: the book of the work, about 35,000 copies sold before the 2000 revision. Shows that the pages hold together through their attitude, not a house style.
- **nucollage.001**: a 360-page collage book built from torn posters, street debris and his own old work. Shows intuitive, additive composition from found material.

## Space & composition
- **No grid, but a decision on every spread.** He has never used grids. In UI, keep a hidden 12-column grid and break it only on hero and editorial surfaces.
- **Collision instead of separation.** Body text runs into the gutter, and photos cover copy. Overlap at least one pair of elements by 10–25% of the smaller one's width.
- **Uneven density.** One corner packed with 6–9px-leading micro text, the opposite corner almost empty. Aim for roughly 70/30 crowded to empty rather than even padding.
- **Crop past comfort.** Cut faces at the eyes and headlines halfway through the cap height. Let `overflow: hidden` cut a word in two at the viewport edge.
- **Rotated columns.** Columns tilted 2–90°, sometimes running vertically up the margin.

## Color
Color in Carson's work comes from print: newsprint, photocopy grey, misregistered spot inks, and photos pushed until the contrast breaks up. It is dirty and comes from the process, never a tidy brand set.
- `#E8E3D6` newsprint ground (background)
- `#151311` toner black (type, heavy rules)
- `#8D8A84` photocopy grey (secondary text, degraded images)
- `#C4471C` rust/spot orange (single accent, used in slabs)
- `#00A0BE` misregistered cyan (offset ghost layer, hover)
- `#D6E02A` acid yellow-green (one shout per screen at most)

Logic: images are monochrome or duotone, with one spot ink allowed to bleed off its shape. Use `mix-blend-mode: multiply` so layers darken where they overlap, the way overprinted ink does.

## Form, line & typography
Several faces per spread; sizes changed mid-word; reverse leading so ascenders and descenders collide; extreme letterspacing beside type squeezed to nothing; dingbats used as text. Scale jumps are huge: a 9px caption sitting against a 400px fragment of a letter.
Fonts: **Anton** (condensed, compressible, for jammed display type), **Special Elite** (typewriter-and-photocopy texture for captions), **Bodoni Moda** (high-contrast serif to set against the grunge, set huge and cropped).

## Rhythm, motion & time
The pace is jumpy, like flicking through TV channels, never smooth. Use hard cuts (`steps()` easing, 0ms crossfades) rather than 300ms ease-out slides. Have elements arrive slightly late and slightly off their final position (2–6px jitter, then snap). On scroll, let layers slide past each other at different speeds so overlaps re-form as you read. Each section gets its own entrance.

## UI translations
1. **Layout:** On editorial and landing screens, place the headline across the image so the image covers 15–30% of the letters; set the body column at a 3° rotation.
2. **Layout:** Make one text block break its column by 1.5× and run into the gutter or off-canvas, with `overflow-x: clip` on the section.
3. **Type:** Set display type at `line-height: 0.78` with mixed sizes inside one headline (for example, 180px / 48px / 220px words).
4. **Type:** Put two to three faces on a hero, all sharing one weight-contrast idea (heavy condensed, typewriter, hairline serif).
5. **Color:** Run photos through `filter: grayscale(1) contrast(1.6)` with one spot-colour block multiplied on top, offset 4px for misregistration.
6. **Texture:** Lay a photocopy-noise SVG over the newsprint background at 6–10% opacity; torn-paper `clip-path` edges on images.
7. **Motion:** Use hard-cut transitions between sections (`animation-timing-function: steps(3)`) with a brief offset jitter before elements settle.
8. **Interaction:** On hover, pull a headline apart by letterspacing (`letter-spacing` 0 to 0.4em) or swap it briefly to a dingbat or glitch version, then restore it.
9. **Interaction ("Ferry move"):** Let an editorial "verdict" scramble a teaser into symbols, with a clear "read plainly" toggle that shows clean, accessible text.
10. **Usable in UI:** marketing heroes, editorial features, music/fashion/event sites, 404 and empty states, splash screens, share cards.
11. **Not usable in UI:** forms, navigation, checkout, settings, error messages, data tables, body copy longer than a paragraph. Leaving out headings, covering text or keeping typos there breaks wayfinding and WCAG. Keep real semantic text in the DOM and apply the distortion through CSS or `aria-hidden` decorative layers.
12. **Rule of thumb:** At most one fully illegible element per screen, and it must be decorative or have a legible duplicate.

## What this artist would reject
- Identical card grids in which every story gets the same template, no matter what it says.
- Letting the software decide: default type scales, auto-layout spacing, layouts produced from presets.
- One tasteful sans-serif in three weights as the whole personality of the site.
- Smooth, generic ease-in-out fades on everything.

## Signature prompt seed
Design this screen as a Ray Gun spread, not a template. Newsprint ground (#E8E3D6), toner-black type, a single rust spot ink multiplied over a high-contrast grayscale photo with 4px misregistration. Crop the photo aggressively so it covers part of a giant condensed headline set with negative leading and mixed sizes within the line. Rotate one text column a few degrees and let it run into the gutter. Cluster micro captions densely in one corner; leave the opposite corner empty. Use hard-cut transitions and hover that tears letterspacing open. Keep navigation and controls plainly legible and semantic underneath.

## Sources
- https://web.mit.edu/comm-forum/legacy/papers/kirsch.html
- https://eyemagazine.com/review/article/who-cares-if-you-read
- https://eyeondesign.aiga.org/anti-grid-icon-david-carson-on-why-computers-make-you-lazy-and-indie-mag-design-needs-to-liven-up/
- https://medium.com/@yopaulmiranda/david-carson-surfing-the-unconventional-waves-of-zapfs-dingbats-52a520186c64
- https://en.wikipedia.org/wiki/David_Carson_(graphic_designer)
- https://www.printmag.com/design-books/the-end-of-print-again-why-david-carson-still-matters/
- https://www.kinokuniya.co.jp/f/dsg-02-9780811830249
