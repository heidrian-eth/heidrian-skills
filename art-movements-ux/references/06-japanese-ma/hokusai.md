# Katsushika Hokusai — Japanese aesthetics (ukiyo-e, read through Ma)

## Essence
Hokusai holds one subject constant (Fuji) and varies everything around it: vantage, scale, weather, foreground. The famous subject is often tiny and the near thing huge, so meaning lives in the interval (*ma*) between them. He builds everything from a few flat colour fields held by one confident outline, printed in blue rather than black.

## Key works examined
- **Under the Wave off Kanagawa (The Great Wave), c. 1830–32**: scale inversion. The foreground wave dwarfs Fuji, and its trough frames the mountain. *(visually checked: AIC 24645 scan)*
- **Thirty-six Views of Mount Fuji, c. 1830–32**: one subject as a design system, extended from 36 prints to 46. *(four sheets visually checked: Great Wave, Red Fuji, Shower Below the Summit, Fujimigahara)*
- **Fine Wind, Clear Morning ("Red Fuji")**: one mass on the right, balanced by rows of paper-reserved clouds on the left. The cone's apex sits at ~74% of the width and its slope rises from the bottom-left corner, so the red plane spans the right ~60% and covers ~21% of the sheet. *(visually checked: CMA 1930.189, "South Wind, Clear Sky")*
- **Thunderstorm Beneath the Summit (Shower Below the Summit)**: the same silhouette, re-weathered. Theming without changing layout. The lower ~40% is a warm sumi-black (#393631, 32% of the sheet) cut by pale-pink lightning. *(visually checked: AIC 87008)*
- **Fujimigahara in Owari Province**: Fuji, about 4% of the sheet width, seen through a barrel ring whose diameter is ~0.65× the sheet height; horizon at ~53%. *(added work, visually checked: AIC 24573)*
- **Hokusai Manga, 1814 onward (15 vols.)**: thousands of studies in only black, grey and pale flesh, a component library of gestures. Studies float loosely inside a ruled single-line frame on each page; the flesh tint has faded to within ~5 L of the paper. *(visually checked: AIC 192276, open volume)*
- **Ryakuga hayaoshie, 1812–14**: finished figures paired with versions reduced to geometry, including compass-drawn circles. Primitives first. *(visually checked: AIC 231629 and AIC 231162, open volumes. Confirmed: in 231629 each page holds two stacked ruled panels of about equal height; one builds a figure from compass circles, a triangle and squares (a monkey), the other shows the finished figure in the same pose. The line is one thin, even outline (≈0.2% of the page width) with no fill, ink ≈10–20% of the page (#767167 on #E8E4D6). In 231162 about 45 small figures float unframed across one spread, each tagged with a short kana or kanji caption.)*

## Process (derived)
*From observation to process (see SKILL.md §1). This is what transfers; the rest of the file is evidence.*

**Katsushika Hokusai.** *Keep one small subject constant and make each view by changing what stands in front of it: the largest, busiest form is context, and its hollow points at the subject.*
Process:
1. Fix the constant: one subject whose silhouette is still recognisable at 0.5–2% of the area (4–11% of the width), and one label slot (≈4% of the width × 20% of the height, in a corner) that never moves between views. Everything else may change.
2. Stack the view in three flat planes (near, middle, far), each one value with no gradual recession. Put the dividing line anywhere from 50% to 75% down; it is a parameter, set per view.
3. Give the near plane the largest and most detailed form (40–65% of the area), and shape it so that it encloses a hollow of the ground value, 15–35% of the area.
4. Seat the subject whole inside the hollow, low and off its centre, at 1/4 to 1/15 of the hollow's width, with clear ground on every side. The hollow frames and never clips: no figure, word or number is cut by the near form. Aim the near form's strongest contour at the subject.
5. Draw every form in one thin even line (0.15–0.2% of the width) and fill it flat. Take line and fills from one colour family in 2–3 depths; the darkest depth replaces neutral black. Allow one gradient per view: a fall-off from an edge of the far plane.
6. Change state by re-tinting one whole plane (20–35% of the area) and leaving the layout untouched; never by sprinkling small marks.
7. Mode for teaching: build each form from 3 primitives and show the pair, construction and finished form in the same pose, in two stacked panels of equal height, same line weight.
Why it works:
- Salience by oddness, plus a scale reference: a small, calm, closed shape among large active detail is the odd one, and the near form tells the eye that the small thing is far and large, not minor. Enlarge the subject and it is an ordinary hero; remove the near form and it is a small thing in a bare field.
- Figure and ground: an enclosed region of ground reads as a shape in its own right, so what sits inside it is found without size or colour. If the hollow clips the subject, the subject joins the near form's texture and cannot be read.
- Constancy across a series: with subject and label slot fixed, every difference between views is information about the vantage. Change both and each view has to be learned from nothing.
Colour relations: bare ground and its tints 60–80%; one colour family in 2–3 depths ≈15–20%, carrying outline, near form and text (darkest depth on ground ≥4.5:1); an optional second, warmer family only as a whole state plane of 20–35%; the subject is defined by silhouette and position, not by a special colour.
Space and line: three flat planes; near form 40–65% with a hollow 15–35%; subject 0.5–2% of the area and whole; hollow 4–15× the subject's width; dividing line 50–75% down; one line weight; mass on one side and open ground on the other, never mirrored.
Type requirement: a compact label that survives small, stacked or vertical setting inside a ruled box; short captions that tag forms one to one; all text in the darkest depth of the colour family; the subject, if it is a number, keeps a readable absolute size (it is small relative to the near form, not small in pixels).
Motion and interaction: the subject and the label stay pinned while the near plane is replaced or moves; a state change re-tints a plane over 300–400ms; reveals are separated by rests of 200–300ms; under reduced motion all of it is a cut. If the subject is a control, its hit area is ≥44px whatever its drawn size.
Fails when: there is no single constant subject (mixed dashboards, feeds); the subject is a table or long text that cannot be small; the screen is so small that a hollow of 15–35% cannot hold the subject at reading size; the subject must be read at a glance from a distance (alerts).
Signature (do not carry together): a curling wave with claw-shaped foam · deep blue on buff paper · a snow-capped cone · a vertical title cartouche.

**Transfer test** (an illustration that the process survives new colours and content; never reuse its hues, layout or wording as a design answer):

Delivery tracker, phone 390 × 844, dark charcoal with one lime family. Nothing shared with a blue-and-buff landscape print.
1. *Constant.* The arrival time ("12 min") in a rounded tag, 86 × 40px = 1% of the area, 22% of the width; the tag keeps its shape on all four views (placed, cooking, on the road, arriving). The order number sits in a fixed 16 × 170px slot top-left, set vertically.
2. *Planes.* Far: charcoal L 12, top 58% of the screen. Middle: L 17 band. Near: L 24. Dividing line at 58%.
3. *Near form.* The route, drawn as one thick looping ribbon with street names and stops along it, 52% of the area, entering from the left and bottom edges. Its loop encloses a hollow of far-plane charcoal, 300 × 210px = 19% of the area.
4. *Subject.* The time tag sits in the hollow, 3.5× narrower than it, 24px above the hollow's floor and right of its centre, with at least 40px of clear charcoal all round. The ribbon's last bend points at it. The whole hollow (300 × 210) is the tap target.
5. *Line and colour.* Every form has a 1px line in the darkest lime depth and a flat fill in one of three lime depths (17% of the area in all). Text is the lightest depth on charcoal, 9:1. One gradient: the far plane falls 4 L darker toward the top edge.
6. *State.* "Delayed" re-tints the middle band (22% of the area) to a warm ochre and changes the tag's text to "Delayed · 25 min"; nothing moves and no icon is sprinkled.
7. *Views.* Swiping changes only the near form (kitchen counter, street, door); the tag and the order slot do not move.
Result: a dark utility screen whose biggest element is a route and whose point is one small whole number. No wave, no blue, no paper.

## Space & composition
- **Scale inversion as hierarchy.** The biggest thing is context, the smallest is the subject. In the Great Wave, Fuji takes only ≈0.5% of the sheet (about 11% of its width) yet anchors it, and the crest's diagonal leads the eye to the peak.
- **Framing through the gap.** Fuji sits *inside* a negative shape: the wave's hollow, a barrel's ring (Fujimigahara), the underside of a bridge.
- **Low horizon** (a Dutch-print borrowing): the Great Wave's sea horizon is at 73% from the top (bottom 27%), so the sky reads as one flat field. It is not fixed: Fujimigahara's is at ~53%.
- **Title cartouche.** Every checked sheet carries a small vertical title label in the top-left corner (~4% of the width, ~20% of the height) with the signature beside it: a fixed metadata slot that never moves between views.
- **Weight against emptiness.** Red Fuji puts mass on one side and air on the other, with no mirroring.
- **Stacked planes.** In a roughly 2:3 landscape sheet (25.7 × 37.9 cm), near, middle and far are separate flat layers, not a smooth perspective gradient.

## Color
*The hex table below is a reference sample for strict studies and homage only. For design, use the colour relations in "Process (derived)".*

Blue-led, but not monochrome. In the Great Wave, blues cover ~19% of the sheet (dark Prussian ~16%); the rest is buff paper and a buff-grey sky that darkens to a grey band at the horizon. In Red Fuji and Shower Below the Summit a warm plane takes 20–35% of the sheet, and the sky *bokashi* is darkest along the top edge. The early prints were *aizuri-e* (blue-printed), even the outlines. Printers mixed indigo with the new Prussian blue for outlines and overprinted pure Prussian blue, so two transparent blues build depth without black.

| Hex | Role |
|---|---|
| `#DECCAE` | Washi ground: the default surface, never pure white (Great Wave paper, 27%) |
| `#304C67` | Prussian blue: primary ink, outlines, headings (Great Wave mid blue, 8%) |
| `#1C2E47` | Gunmetal (indigo+Prussian overprint): deepest tone, replaces black (Great Wave, 8%) |
| `#A7B1AD` | Pale sky/wave wash: large fields (faded light indigo, 10% of the Great Wave; Red Fuji's faded sky reads `#82989F`) |
| `#C19884` | Benigara red: a whole weather plane, not a dot (Red Fuji cone, 21%, faded; Shower's deeper red-brown `#795044`) |
| `#E2D1B6` | Pale flesh (the Manga tint, now faded): secondary fills, highlighted states |
| `#C6B599` | Buff sky: the Great Wave's sky is this, not blue (32% of the sheet) |
| `#393631` | Sumi storm: warm brown-black for the "storm" theme (Shower Below the Summit, 32%) |

## Form, line & typography
One closed contour, no modelling, flat fill. The wave's foam breaks into claw-like fractal tips: one expressive edge inside a calm system. The Manga method is to reduce to circles and strokes, then add character.
- Fonts: **Shippori Mincho** (display, large, slightly open tracking), **Zen Kaku Gothic New** (UI/body), **Klee One** (sketchbook captions).
- Headings in Prussian blue, never black. Dividers are 1.5px blue rules, not grey hairlines. (Outlines in the scans are ~0.15% of the sheet width, i.e. ~1.5px on a 1000px frame.)

## Rhythm, motion & time
The Great Wave is the instant before the break: hold at the peak, then release.
- Easing `cubic-bezier(.7,0,.2,1)` with a 120ms hold at the apex.
- Series as navigation: swipe between views of one object, with the foreground plane moving 3× faster than the far plane.
- Weather as state: loading, error and success keep the layout and only re-tint the field.
- Ma in time: 200–300ms rests between staggered reveals, not a continuous cascade.

## UI translations
1. **Invert the hierarchy**: a foreground shape (an illustration or curved SVG mask) takes 60–70% of the hero. The primary CTA sits small in its negative space.
2. **Frame through a hole**: show the key metric small (≈4–11% of the width, as Fuji is) inside a negative shape: a `clip-path: circle()` ring about 0.65× the frame height cut in a large surface (the barrel in Fujimigahara) or the hollow of the foreground form (the wave).
3. **Put the horizon low, but not at a fixed line**: 73% in the Great Wave, ~53% in Fujimigahara. One flat field above, with content clustered in the band below.
4. **Build a 36-views component**: one data object rendered in several framings (crop, zoom, seasonal tint). Keep the object and change the vantage.
5. **Go blue-on-blue**: overlap translucent blues with `mix-blend-mode: multiply`. Text is `#304C67` on `#DECCAE`.
6. **Red as weather**: benigara is a theme that floods one whole plane (~20% of the screen) for a special state, never a sprinkle of red buttons.
7. **Outline plus flat fill**: give cards and icons a 1.5px Prussian stroke and a flat tint. The only gradient is a single horizon wash (*bokashi*).
8. **Claw edge**: make one section divider a scalloped, fractal SVG crest and keep everything else straight.
9. **Tonal planes, not shadows**: show depth as three z-planes with distinct flat tints, with no `box-shadow`.
10. **Crest-hold refresh**: on pull-to-refresh, the indicator curls into a wave, holds, then breaks into the new content.
11. **Manga empty states**: grids of tiny single-colour gesture sketches in flesh and grey, a different one per context.
12. **Cartouche slot**: a small vertical title label pinned top-left on every view of the series; it never moves.
13. **Construction pairs** (Ryakuga hayaoshie): in onboarding or a style guide, show each icon twice in two stacked panels of equal height, once as its circle/triangle/square construction in a thin even line with no fill, and once finished.

## What this artist would reject
- The centred hero where the product shot is biggest.
- Pure `#000` text and neutral grey chrome.
- Drop shadows and glass blur standing in for depth.
- A rainbow of semantic colours where one hue at several densities would do.
- Endless looping micro-animation with no pause: motion without *ma*.
- Inventing every screen from scratch instead of varying one subject.

## Signature prompt seed
Design this screen as one view in a series of thirty-six. Ground it on washi `#DECCAE`, with a low horizon (between ~53% and 73% from the top, set per view): one flat graded field above and content clustered below it. Let a huge curling foreground form take most of the frame, and place the real subject (the key number or CTA) tiny inside its negative space. Draw with 1.5px Prussian-blue `#304C67` outlines and flat fills, build depth from overlapping blues, and use no neutral black or shadows. Pin a small vertical title cartouche top-left. Use Shippori Mincho headings. Motion rises, holds at the crest, then breaks.

## Sources
- https://www.metmuseum.org/essays/hokusai-great-wave
- https://smarthistory.org/?p=1953
- https://en.wikipedia.org/wiki/36_Views_of_Mount_Fuji
- https://en.wikipedia.org/wiki/Fine_Wind,_Clear_Morning
- https://www.metmuseum.org/art/collection/search/57804
- https://en.wikipedia.org/wiki/Hokusai_Manga
- https://pulverer.si.edu/node/314/title/1
- https://en.wikipedia.org/wiki/Ma_(negative_space)
- https://www.artic.edu/artworks/24645 (Great Wave scan, IIIF b3974542-b9b4-7568-fc4b-966738f61d78, CC0)
- https://www.clevelandart.org/art/1930.189 (South Wind, Clear Sky, CC0)
- https://www.artic.edu/artworks/87008 (Shower Below the Summit, CC0)
- https://www.artic.edu/artworks/24573 (Fujimigahara in Owari Province, CC0)
- https://www.artic.edu/artworks/192276 (Hokusai manga volumes, CC0)
- https://www.artic.edu/artworks/231629 (Ryakuga haya oshie, IIIF 003fc80b-e17e-4016-e4e8-acf7216e712d; retry pass)
- https://www.artic.edu/artworks/231162 (Ryakuga Haya-oshie, IIIF 6923e80a-5e78-d686-1e59-4220cbfc1985; retry pass)
