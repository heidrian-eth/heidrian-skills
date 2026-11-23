# Katsushika Hokusai — Japanese aesthetics (ukiyo-e, read through Ma)

## Essence
Hokusai holds one subject constant (Fuji) and varies everything around it: vantage, scale, weather, foreground. The famous subject is often tiny and the near thing huge, so meaning lives in the interval (*ma*) between them. He builds everything from a few flat colour fields held by one confident outline, printed in blue rather than black.

## Key works examined
- **Under the Wave off Kanagawa (The Great Wave), c. 1830–32**: scale inversion. The foreground wave dwarfs Fuji, and its trough frames the mountain.
- **Thirty-six Views of Mount Fuji, c. 1830–32**: one subject as a design system, extended from 36 prints to 46.
- **Fine Wind, Clear Morning ("Red Fuji")**: one symmetrical mass fills the right half, balanced by light clouds on the left.
- **Thunderstorm Beneath the Summit**: the same silhouette, re-weathered. Theming without changing layout.
- **Hokusai Manga, 1814 onward (15 vols.)**: thousands of studies in only black, grey and pale flesh, a component library of gestures.
- **Ryakuga hayaoshie, 1812–14**: finished figures paired with versions reduced to geometry, including compass-drawn circles. Primitives first.

## Space & composition
- **Scale inversion as hierarchy.** The biggest thing is context, the smallest is the subject. In the Great Wave, Fuji takes roughly 5% of the sheet yet anchors it, and the crest's diagonal leads the eye to the peak.
- **Framing through the gap.** Fuji sits *inside* a negative shape: the wave's hollow, a barrel's ring (Fujimigahara), the underside of a bridge.
- **Low horizon** (a Dutch-print borrowing) at about the bottom 25–30%, so sky or sea reads as one flat field.
- **Weight against emptiness.** Red Fuji puts mass on one side and air on the other, with no mirroring.
- **Stacked planes.** In a roughly 2:3 landscape sheet (25.7 × 37.9 cm), near, middle and far are separate flat layers, not a smooth perspective gradient.

## Color
Monochrome blue with rare warm accents. The early prints were *aizuri-e* (blue-printed), even the outlines. Printers mixed indigo with the new Prussian blue for outlines and overprinted pure Prussian blue, so two transparent blues build depth without black.

| Hex | Role |
|---|---|
| `#E9DFC7` | Washi ground: the default surface, never pure white |
| `#003153` | Prussian blue: primary ink, outlines, headings |
| `#1E2B3A` | Gunmetal (indigo+Prussian overprint): deepest tone, replaces black |
| `#9DB8C8` | Pale sky wash: large fields, graded toward the horizon |
| `#A8432E` | Benigara red: one accent per screen |
| `#E6C7AB` | Pale flesh (the Manga tint): secondary fills, highlighted states |

## Form, line & typography
One closed contour, no modelling, flat fill. The wave's foam breaks into claw-like fractal tips: one expressive edge inside a calm system. The Manga method is to reduce to circles and strokes, then add character.
- Fonts: **Shippori Mincho** (display, large, slightly open tracking), **Zen Kaku Gothic New** (UI/body), **Klee One** (sketchbook captions).
- Headings in Prussian blue, never black. Dividers are 1.5px blue rules, not grey hairlines.

## Rhythm, motion & time
The Great Wave is the instant before the break: hold at the peak, then release.
- Easing `cubic-bezier(.7,0,.2,1)` with a 120ms hold at the apex.
- Series as navigation: swipe between views of one object, with the foreground plane moving 3× faster than the far plane.
- Weather as state: loading, error and success keep the layout and only re-tint the field.
- Ma in time: 200–300ms rests between staggered reveals, not a continuous cascade.

## UI translations
1. **Invert the hierarchy**: a foreground shape (an illustration or curved SVG mask) takes 60–70% of the hero. The primary CTA sits small in its negative space.
2. **Frame through a hole**: show the key metric through a `clip-path: circle()` cut-out in a large surface, like Fuji seen inside the barrel.
3. **Put the horizon at 72%**: one flat field above, with all content packed into the bottom band.
4. **Build a 36-views component**: one data object rendered in several framings (crop, zoom, seasonal tint). Keep the object and change the vantage.
5. **Go blue-on-blue**: overlap translucent blues with `mix-blend-mode: multiply`. Text is `#003153` on `#E9DFC7`.
6. **One red per screen**: only the most consequential action gets benigara red.
7. **Outline plus flat fill**: give cards and icons a 1.5px Prussian stroke and a flat tint. The only gradient is a single horizon wash (*bokashi*).
8. **Claw edge**: make one section divider a scalloped, fractal SVG crest and keep everything else straight.
9. **Tonal planes, not shadows**: show depth as three z-planes with distinct flat tints, with no `box-shadow`.
10. **Crest-hold refresh**: on pull-to-refresh, the indicator curls into a wave, holds, then breaks into the new content.
11. **Manga empty states**: grids of tiny single-colour gesture sketches in flesh and grey, a different one per context.

## What this artist would reject
- The centred hero where the product shot is biggest.
- Pure `#000` text and neutral grey chrome.
- Drop shadows and glass blur standing in for depth.
- A rainbow of semantic colours where one hue at several densities would do.
- Endless looping micro-animation with no pause: motion without *ma*.
- Inventing every screen from scratch instead of varying one subject.

## Signature prompt seed
Design this screen as one view in a series of thirty-six. Ground it on washi `#E9DFC7`, with the horizon at 72%: one flat graded field above and content clustered low. Let a huge curling foreground form take most of the frame, and place the real subject (the key number or CTA) tiny inside its negative space. Draw with 1.5px Prussian-blue `#003153` outlines and flat fills, build depth from overlapping blues, and use no black or shadows. Allow one benigara-red accent. Use Shippori Mincho headings. Motion rises, holds at the crest, then breaks.

## Sources
- https://www.metmuseum.org/essays/hokusai-great-wave
- https://smarthistory.org/?p=1953
- https://en.wikipedia.org/wiki/36_Views_of_Mount_Fuji
- https://en.wikipedia.org/wiki/Fine_Wind,_Clear_Morning
- https://www.metmuseum.org/art/collection/search/57804
- https://en.wikipedia.org/wiki/Hokusai_Manga
- https://pulverer.si.edu/node/314/title/1
- https://en.wikipedia.org/wiki/Ma_(negative_space)
