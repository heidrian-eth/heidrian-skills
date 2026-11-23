# Gustav Klimt — Vienna Secession

## Essence
Klimt sets a small, softly modeled human zone (face, hands) inside a huge, flat field of metallic ornament. The pattern is not background but a second body that dresses and nearly swallows the figure. What makes it unmistakable is extreme flatness everywhere except one tender patch of naturalistic detail.

## Key works examined
- **Adele Bloch-Bauer I, 1903–07 (Neue Galerie, 140 × 140 cm).** Face, hair and hands are under 1/12 of the surface, and the rest is gold and silver leaf with gesso relief. A ratio of roughly 92% ornament to 8% human.
- **The Kiss, 1908–09 (Belvedere, 180 × 180 cm).** Gold, silver and platinum leaf on a glazed brass-leaf ground flecked with metal. His robe is rectilinear and hers is circles. Pattern tells the two figures apart.
- **Beethoven Frieze, 1902 (Secession, about 2.15 × 34.14 m).** Casein, gilt stucco, mirror shards and mother-of-pearl buttons. A narrative that runs around a room, with quiet stretches between climaxes.
- **Stoclet Frieze, 1905–11 (Palais Stoclet, with the Wiener Werkstätte).** Marble, enamel, gilded tiles and stones. Two facing Tree of Life panels bookend a geometric Knight panel.
- **Square landscapes from 1899 on (e.g. Schloss Kammer on the Attersee).** Framed through a cardboard viewfinder with a square hole, then compressed into a skyless tapestry.
- **San Vitale mosaics, Ravenna (visited Dec 1903).** The source of the icon-like gold ground.

## Space & composition
- **The square is the default canvas.** Adele, The Kiss and the landscapes are all 1:1. The square removes the left-to-right pull, so the eye spirals inward.
- **Figures fill the field.** In The Kiss the couple is a single vertical bell shape that almost touches the top, above a flowered strip that ends abruptly like a cliff.
- **Merge, don't separate.** Adele's dress dissolves into the background. The edge between figure and ground shows only as a shift in pattern density.
- **Telescope cropping.** The landscapes have little or no horizon. Foliage runs off all four sides, giving even density and no focal point.
- **Frieze rhythm.** The Beethoven Frieze puts dense clusters of figures between long, nearly empty stretches of wall, so density pulses with the story.

## Color
One dominant metallic field, a near-black for outlines and a few "jewel" accents packed into pattern cells. Flesh is the only modeled colour.

| Role | Hex |
|---|---|
| Leaf gold (primary field) | `#C9A13B` |
| Glazed bronze ground (recessed areas) | `#7A5A22` |
| Ink black (outlines, rectangles) | `#1E1A16` |
| Silver/platinum (secondary metallic) | `#C8C6BE` |
| Pale flesh (the one naturalistic zone) | `#EAD1C0` |
| Meadow green (accent) | `#3E6B4A` |
| Enamel red/coral (spot accent) | `#B5432F` |

## Form, line & typography
There are two line languages and they never mix. One is structural: upright rectangles, black-and-white checks and columns. The other is organic: circles, ovals, eye shapes and spirals. The Kiss assigns one to each figure. Adele adds Egyptian eyes, Mycenaean whorls and her own initials worked into the motifs, so letters are ornament too. For type, use narrow inscriptional capitals for display, a soft serif for body and a circle-built geometric sans for labels. Suggested free fonts: **Marcellus SC** (inscriptional display), **Cormorant Garamond** (body), **Josefin Sans** (geometric labels and data).

## Rhythm, motion & time
The surface should shimmer, not slide. Gold leaf changes as the viewer moves, so the motion is light passing over a static pattern. Gesso-relief circles catch the light separately, which suggests a cell-by-cell glint. Pace long pages like the frieze: quiet stretches broken by dense, decorated climaxes. The human detail (a face, a hand) never animates.

## UI translations
1. **Make the hero a 1:1 square** that is 90% flat ornamental field. Put the one photographic "face" element in about 8% of the area, above centre.
2. **Build two pattern tokens:** `--ornament-rect` (black/ivory rectangles) for structural surfaces and `--ornament-round` (radial-gradient circles and ovals) for personal content. Never use both on one element.
3. **Make edges out of density instead of borders.** A card repeats its parent's pattern at a tighter `background-size`, with no stroke and no shadow.
4. **Gold is a field, not a button.** Use `#C9A13B` for large surfaces only, with calls to action in ink black on gold. Coral goes on at most one element per screen.
5. **Shimmer on pointer.** Bind a gradient highlight to cursor or device-tilt position over the gold, with `mix-blend-mode: overlay`.
6. **Stagger the glint.** On load, brighten pattern circles one at a time (120ms each, with 15–30ms random delays), like light over gesso.
7. **Viewfinder crop for imagery.** Show galleries as tight square tiles with no horizon, texture running off all edges and no centred subject.
8. **Frieze scroll.** For onboarding, use a horizontal scroll-snap strip that alternates dense ornamented panels with sparse ones.
9. **Bookend symmetry.** Lay out dashboards Stoclet-style: two mirrored organic panels with a compact geometric panel between them for the key metric.
10. **Keep the human zone untouched.** No overlays or animation on avatars or faces.

## What this artist would reject
- Neutral grey surfaces and empty white canvas as the default "calm."
- Drop shadows and elevation to separate layers, instead of shifts in pattern density.
- Wide 16:9 hero banners with a centred headline floating over a stock photo.
- Ornament scattered evenly as decoration instead of packed into one dense field.
- One generic icon set for everything, when structure and intimacy deserve different shape languages.
- Animating content itself (bouncing, sliding) instead of animating light on a still surface.

## Signature prompt seed
Design this screen as a 1:1 Klimt icon. Fill about nine-tenths of it with a flat field of leaf gold (#C9A13B) made of packed ornament cells. Use stacked black-and-ivory rectangles for structural UI and gold circles, ovals and eye shapes for anything personal. Let containers dissolve into the background through density, never through borders or shadows. Set one small, still, naturalistic human zone (a face or a pair of hands) slightly above centre. Use a single coral accent. Use tall inscriptional capitals for headings. Motion is only light: a cursor-tracked shimmer and cells that glint one at a time.

## Sources
- https://sammlungtest.belvedere.at/objects/6678/der-kuss-liebespaar
- https://smarthistory.org/gustav-klimt-the-kiss
- https://www.neuegalerie.org/content/adele-bloch-bauer-i
- https://en.wikipedia.org/wiki/Adele_Bloch-Bauer_I
- https://secession.at/en/beethovenfrieze
- https://en.wikipedia.org/wiki/Beethoven_Frieze
- https://en.wikipedia.org/wiki/Stoclet_Frieze
- https://onlinecollection.leopoldmuseum.org/en/object/9690-viewfinder-from-the-estate-of-gustav-klimt
