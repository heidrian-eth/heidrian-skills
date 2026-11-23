---
name: "art-movements-ux"
description: "Use when designing any UI/UX screen, app, page or design system and the user wants non-generic, art-informed design: generate variants in the manner of 10 art/architecture movements (50 artists), then synthesize."
---

# Art Movements UX: diverge through the masters, then synthesize

Left alone, a model designing UI reverts to the statistical median of its training data: Material/Apple-style rounded cards, soft shadows, centered heroes. This skill replaces that default with a studio method: **design the same screen several times, each in the strict manner of a different artist or movement, then splice together the parts the user likes.**

The library below distills 50 artists across 10 movements into rules you can carry out directly (layout, color, type, motion, interaction). Treat every artist entry as a *constraint set to obey*, not a mood to gesture at. Half-applying a manner produces exactly the median look this skill exists to escape.

---

## 0. The Median Detector (purge before you begin)

Nearly every one of the 50 artists rejected these patterns independently. Unless a chosen manner explicitly calls for one, none may appear in a variant:

- Rounded cards (12–16px radius) floating on soft grey drop shadows, plus elevation z-levels
- Centered hero: headline, subhead, two buttons, then a symmetric three-up feature row
- Pure `#FFFFFF` ground with neutral greys and a single "brand blue" accent
- A smooth 1.2–1.25 modular type scale in one sans (Inter/system) with three weights
- Glassmorphism, gradient blobs, decorative stock illustration and mascots
- An even 8pt grid with identical gutters and identical tile sizes
- One `300ms ease-in-out` (or bouncy spring) on every element; fade-and-slide-up-20px entrances
- Color used as decoration, not to carry a meaning

If a draft could be mistaken for a Dribbble template, it has failed. Push harder into the chosen manner.

---

## 1. Workflow

### Phase A: Skeleton (function first, held constant)
Before any styling, write the screen's **functional skeleton**: the user's goal, every piece of content, every action, primary vs secondary actions, states (empty, loading, error, selected), and platform (mobile, desktop). Every variant must deliver the same skeleton so comparisons are fair. Only form changes between variants.

### Phase B: Divergence (the variants)
1. Pick **4–6 movements** (or use the ones the user names). Choose for maximum contrast using the axes map in §3: no two variants from the same corner. A good default spread is one ordered (Swiss / De Stijl), one void (Japanese Ma / Minimalism), one spatial-sequential (Modernist architecture), one ornamental (Secession), one kinetic (Op/Kinetic), and one loud (Postmodern).
2. For each movement, choose a **lead artist** (and optionally one secondary from the same movement). Open the variant with a header card:
   - `Variant B: De Stijl / Rietveld (+ van der Leck)`
   - **The move:** one sentence (the artist's essence)
   - **Rules applied:** the 5–8 specific rules from the entry you are following
   - **Palette:** the exact hexes used, with a role for each
   - **Type:** fonts, sizes, scale ratio
   - **Motion & interaction:** what moves, how, and why
3. Build each variant as a real rendered screen: a self-contained HTML page, or the session's design artifact type if one exists. Same content, real copy, no lorem ipsum. Commit fully: if the manner says "60% empty field", leave 60% empty.
4. Put the variants side by side, or in tabs, in one deliverable so they can be compared.

### Phase C: Gene board (critique)
Break every variant into labeled **genes** so the user can choose à la carte:
- `B-layout` (e.g. slabs overlapping 12px, rules running 16px past joints)
- `B-color` (red reserved for the one content plane, yellow only on ends)
- `B-type`, `B-motion`, `B-interaction`, `B-texture`, `B-navigation`

Then ask the user which genes they like, or propose a combination yourself, with reasons, if they are away.

### Phase D: Synthesis
Combine the chosen genes into one new design. Compatibility rules:
- **One structural system.** Pick one grid logic (Gerstner's 58-unit field, Modulor series, Crouwel's visible cells, Judd's gap = module, and so on). Genes from other variants must re-express themselves inside it.
- **One color logic.** For example, one-accent scarcity (Bayer/Crouwel), value-only relativity (Albers), emitted light (Flavin) or ordered ring (Le Parc). You may layer a second logic only if it governs a different role, e.g. base surfaces vs state signals.
- **One type logic.** Either a scale jump of ≥1:6 (Müller-Brockmann/Scher) or hierarchy by isolation and space (Hara/Sejima/Ruder). Never both.
- **One motion grammar.** Mechanical steps, slow light change, scroll-bound or spring, applied consistently.
- **One rule-break per screen.** Each manner allows a single deliberate violation (one tilted element, one off-grid module, one red). The synthesis keeps exactly one.

Name the hybrid ("Barragán threshold × Crouwel grid × Flavin state light") and document its rules as a mini design system: tokens, the grid, type, motion and component rules.

### Phase E: Guardrails pass (always)
- Body text contrast ≥ WCAG AA 4.5:1. Low-contrast manners (Ando, Agnes Martin, Turrell) still have to pass this.
- Navigation, forms, data, errors and checkout must stay plainly legible and semantic (Carson's own boundary). Expressive distortion goes only on decorative layers, with real text underneath.
- Respect `prefers-reduced-motion`. No flashing more than 3 times a second (WCAG 2.3.1). Avoid high-contrast stripes near 3 cycles/degree with a 50% duty cycle behind content (Riley's pattern-glare zone). Never put text over vibrating fields.
- Tap targets ≥ 44px. Rotate only decorative layers, never controls or text you need to read (van Doesburg's rule).
- Color must never be the only signal: pair it with shape, position or a label (Stepanova's "uniforms").

---

## 2. Cross-cutting lessons (the meta-principles from all 50)

1. **Scarcity of accent.** About 25 of the 50 restrict the saturated color to *one element per screen*, the primary action or the current state. That single constraint does more against genericness than anything else.
2. **Depth without shadows.** Get depth from overlapping flat planes (Rietveld, Popova), value steps (Albers, Sejima, Turrell), translucent multiply (Moholy-Nagy, Kandinsky), scale tiers, emitted glow (Flavin), parallax interference (Soto, Cruz-Diez) or pattern density (Klimt).
3. **Grounds are never pure white.** Use warm papers like `#F4F1EA`, `#EFE9DC` or `#E9DFC7`. White is an active plane, not "nothing".
4. **Show the structure.** Make the grid visible as graph paper (Crouwel), tie-hole dots (Ando), scored joints (Wright), struts (Popova) or bronze mullions (Mies). Structure can be the ornament.
5. **Unequal is alive.** Use irregular tracks (`3.2fr 1fr .45fr 1.6fr`), asymmetric margins and off-center masses. Symmetry is allowed only as a deliberate exception (Klimt's Stoclet bookends, Tanaka's near-symmetry with one offset).
6. **Violent or zero hierarchy.** Either jump scale hard (1:6, 8–12× numerals, 60vh glyphs) or remove size hierarchy entirely and rely on space and position. The mushy middle is the median.
7. **Sequence and threshold.** A screen is a place you arrive at: compression then release (Wright), a dim narrow entry then wide light (Barragán), a void band to cross (Ando), a ramp or promenade (Le Corbusier, Wright's Guggenheim).
8. **System over composition.** Design the rule that generates layouts: Gerstner's morphological box, LeWitt's exhaustive permutations, Vasarely's plastic units, Stepanova's single tile, Le Parc's 14-hue ring. Show the rule to the user.
9. **Motion has a material.** Mechanisms step (`steps()`), light fades slowly (600–1400ms), gravity settles, cuts are hard. Motion either follows content (scroll- or pointer-bound) or makes a point. It never runs as idle decoration on a timer, except in deliberate kinetic idle states.
10. **Interaction changes the medium.** On hover or focus, change value, light, width axis, track size, ring position or transparency instead of lifting and scaling.

---

## 3. Axes map: choose contrasting movements

| Movement | Order ↔ Expression | Void ↔ Density | Flat ↔ Deep | Still ↔ Kinetic | Human/warm ↔ Machine |
|---|---|---|---|---|---|
| Bauhaus | order | balanced | flat→translucent | mid | machine-humanist |
| De Stijl | order | void | flat planes | stepped | machine |
| Constructivism/Suprematism | expressive-order | void + diagonal force | flat, tilted | mechanical | machine |
| Swiss Typographic | strict order | balanced | flat | minimal | machine |
| Modernist architecture | order + sequence | void | spatial | slow procession | human |
| Japanese Ma | quiet order | extreme void | flat / light | very slow | human |
| Art Nouveau / Secession | ornamental order | dense | flat ornament | slow/flowing | human/crafted |
| Minimalism / Light & Space | system | void or serial | light-depth | slow / none | machine/perceptual |
| Op & Kinetic | system | dense field | optical depth | high, user-driven | perceptual |
| Postmodern / New Wave | expression | dense, collision | layered Z | snappy, syncopated | human/irreverent |

---

## 4. The Library

Each entry gives the **move** (essence), the **rules** (do these), the **palette** (approximate hexes, with roles listed in order) and **type/motion**. The hexes are approximations from catalog research, so adjust them to taste and contrast needs.

### 4.1 BAUHAUS: function, primary geometry, color as perception
The movement: form follows role, shape and color carry meaning, and design is a teachable grammar.

**Josef Albers.** *Fix everything except color, and let color do all the work.*
- Nest 3–4 flat regions at 10/8/6/4 units, each step offset 0.5u from the bottom and 1.5u from the top so the core sits low. These rings replace cards.
- Use a single-hue value ladder in 4 steps, with the most important element the *least* saturated. Opaque fills only: no opacity, gradients, borders or shadows.
- Reuse one hex on two grounds so it reads as two colors.
- Hover swaps the value order of adjacent rings, and navigation cross-fades ring colors from the center outward (stagger 120ms). Geometry stays frozen.
- Offer a "theme as series" switch: one layout shown in many tonal variations. Add a mono footer listing the screen's hexes.
- Palette: `#C98A1B #E0A526 #EEC14A #C9C3B3(core) #F4F1EA #2B2A26`. Type: geometric stencil display at ≥8vw, Jost body.

**Herbert Bayer.** *Perception engineering: lowercase, bars, one red, a cone of vision.*
- Set a hard vertical axis at 33.3% width and align all text to it; only one image may cross it. Use 12px black bars instead of cards.
- Everything lowercase. Headlines weight 700–800, ≥4× body, `-0.02em`. Turn one label 90° up the gutter.
- Exactly one red element per screen. Blue and yellow are allowed only inside data. Show small counts as Isotype pictogram rows.
- Keep sticky header and footer to one or two glanceable items at 1.25× size. Rules draw in with `scaleX` over 200ms, then text follows. Hovering a row turns it red and mutes the rest.
- Palette: `#F4F1EA #141414 #D7261E #1D4E9E #F2C200 #B9B3A6`. Type: Jost, lowercase.

**Wassily Kandinsky.** *A field of forces in which shape, color and sound correspond.*
- Use a strict token table: yellow triangle = alert, red square = commitment, blue circle = focus. Never mix the pairs.
- Hang the screen off one dominant blue circle (35–50% of the width) set up and to the left, with content around it as satellites. Run one or two 1px diagonals (8–20°) from dots into empty space. Leave one quadrant silent except for a single 8–12px dot.
- Calm content goes upper-left and urgent content lower-right. Overlaps multiply at 70–85% opacity.
- Yellow CTAs scale outward fast. Blue focus settles inward slowly. Optionally add sound: a cello tone for confirm, a trumpet ping for alert.
- Palette: `#EFE6D2 / #14161C(dark) #F2C230 #C8322B #1F4FA3 #1A1A1A #7A4E9C`. Type: Syne display, with one word 3–4× size rotated −6°, and Jost body.

**Paul Klee.** *Take a line for a walk: a magic square of stepped tones, with polyphony.*
- Make the background a grid of 8–12 tiles with unequal `fr` values, stepping from ochre to twilight blue (`color-mix` in oklch, 0–50%). Tiles are lighter near the content.
- Draw the progress or breadcrumb path as one continuous 1.5px line that walks between the steps and ends in an arrow.
- Stack independent layers (tiles, a 6–8px dot texture, hairline pictograms), each with its own spacing. Allow exactly one red-orange "sun".
- Use arrows as meaning: a heavy black down-arrow for destructive actions, a thin feathered arrow for forward ones. The loader animates point → line → square over 1.2s.
- Palette: `#1E1B24 #4F6D8A #B9A27C #D9C9A8 #E7B9B0 #C8452C #F4EEE2`. Type: Josefin Sans, modest sizes (≤2.5rem).

**László Moholy-Nagy.** *Surfaces are light: opaque, translucent, transparent, reflective.*
- Rotate the hero plane 22° and bleed it 15% off the right edge. Depth comes from overlapping translucent panels at 1×, 0.6× and 0.25× scale, never from shadows.
- Build components in greys and add color only as multiply overlays (transparent yellow over violet makes near-black). Use one red circle.
- Typophoto: run headlines straight into photos. Mark emphasis with a 6px black left bar.
- Modals change material, from transparent to translucent to opaque, over 400ms. Use tempo tokens: hard cuts between sections, 800ms dissolves within them. The cursor acts as a spotlight. Empty states are photograms (white silhouettes on dark).
- Palette: `#F1EEE6 #121212 #8E9093 #D9D6CF #E8B624@70% #3E4FA0@60% #C23B22`. Type: heavy grotesque.

### 4.2 DE STIJL: orthogonal planes, primaries, balance through inequality
The movement: the universal reduced to the rectangle, primary colors plus non-colors, and asymmetric equilibrium.

**Piet Mondrian.** *Balance from inequality.*
- Irregular tracks such as `grid-template-columns: 3.2fr 1fr .45fr 1.6fr`, never `repeat(n,1fr)`. Draw the rules with `gap` over a black background: 14px between regions, 6px within, plus one doubled 4+4px pair.
- Main content is a white near-square (~45%) left of center. Navigation and metadata go in thin edge cells. Stop one rule 24–40px short of the edge.
- One primary goes in an edge-cropped cell (<12% of area), plus two chips of the other primaries (<3%) on opposite sides. Tint each white panel 2–3% differently.
- One 900-weight headline flush in a cell corner, slightly clipped. On select, the tracks resize over 300ms.
- "Boogie mode" for live data: yellow lanes replace the black rules, and colored chips tick inside them. One lozenge card (rotated 45°) per screen at most.
- Palette: `#F2EFE6 #141414 #D0281F #1D3D8F #F2CB1D #BEBDB8`.

**Theo van Doesburg.** *Two grids in friction: the content upright, the color field at 45°.*
- Behind an upright 12-column content grid sits a full-bleed field of 4–8 flat rectangles rotated 45°. Each diagonal bar is exactly one gutter wide, so both grids share a module.
- One vermilion plane covers about 40% of the hero, off-center upper-right. Panels meet edge to edge with no borders.
- Headlines are justified blocks that fill their column. The logo is overprinted on a faint giant monogram.
- Background planes move along a 45° vector at 0.4× scroll speed. Hover slides a color plane in diagonally in 4 steps. Only the decorative layer ever tilts.
- Palette: `#D62E1F #1D3F9B #F2C230 #141414 #F4F1EA #9A9A96 #3E6B4E(once)`.

**Gerrit Rietveld.** *Parts slide past each other and never meet; the room reconfigures.*
- Build the screen from 3–5 absolutely positioned slabs at different z-levels, overlapping 12px so no two share an edge. Every rule extends 16px past its container on both sides.
- One partition toggle slides panels on one-axis tracks over 320ms, turning one open workspace into three without a route change. Animate only `translate`, no fades or scale.
- Red marks the single main content plane, blue the input surfaces, yellow only ends (progress caps, handles, range ends). Structure is drawn as 4–6px black bars.
- Mono labels sit at the crossing joints like bolts (`01 / SEAT`). Leave one corner open. Handles are 6×32px notches. Onboarding runs as a Z-path ribbon.
- Palette: `#F4F2EC #B9B8B3 #151515 #C8261E #1F4E9A #F2C230`. Type: Archivo, Space Mono labels.

**Bart van der Leck.** *A real scene cut into floating bars that never touch.*
- At least 70% of the screen is warm white field. Content sits in 4–6 bars covering under 30% of the area, separated by a uniform 12px gap of white and no borders.
- Work in horizontal density bands: dense vertical slivers on top (nav), staggered blocks in the middle, long thin rules below.
- Each primary has one job: red for action, blue for navigation, yellow for state, black for text. Primaries are never adjacent without white between them. Tilt exactly one element per screen.
- Icons are built from 2–4 disconnected strokes. Headlines use a stencil face with `0.08em` tracking.
- Illustrations are figures made of bars that drift apart into abstraction when a task completes. Hover swaps the fill from blue to red.
- Palette: `#F7F5EF #D52B1E #2456A6 #F3C316 #141414 #7C9BD6`. Type: Big Shoulders Stencil Display, Jost.

**Vilmos Huszár.** *One family of rectangles makes letters, rooms and puppets alike.*
- Build the wordmark from positioned rectangles on an 8px module (1u, 2u, 3u) rather than from a font.
- A dense rectangle cluster fills the top 40%, over a fully justified text slab of the same width.
- Color is its own token layer: a red plane may span two cards or wrap from the header into the sidebar. Translucent green multiply marks intersections such as filter AND selection.
- Transitions use `steps(3)`, and every intermediate frame is a complete composition. Drag moves in whole-module increments. Radius 0, no shadows.
- Palette: `#F4F1E8 #141414 #D7261E #1F4FA3 #F2C200 #2E8B57@65% #9A9A94`.

### 4.3 CONSTRUCTIVISM & SUPREMATISM: forces, diagonals, two inks, apparatus
The movement: design as construction and as a working device. Diagonal energy, red as action, no decoration.

**Kazimir Malevich.** *The background is the subject: weightless planes in endless white.*
- Use a warm field (`#F1ECE0`) with cards in cool white (`#FBFBF8`). The two whites alone separate them, with no borders or shadows.
- Tilt all planes on one shared axis (about −12° to −15°). Bleed the hero off the top-right. Exactly one black plane per screen, and one red 3:1 bar as the only CTA. Ultramarine and ochre 3–6px bars run past the containers.
- Arkhitekton dashboards: one panel at 2/3 width, with 3–5 smaller panels docked at staggered offsets.
- Planes drift in from off-screen, heaviest first, staggered 80ms. Hover rotates 3° and raises the z-order. Empty states show a single off-center black square.
- Palette: `#F1ECE0 #FBFBF8 #141312 #C42A1D #2A3B8F #E2B33A #8C8A84`. Type: Unbounded (rotated with the planes), Jost body kept horizontal.

**El Lissitzky.** *Vectors and counterweights; the reader's hand completes the construction.*
- The main bar runs at −30° off two edges, and content rides along it. The CTA is a red wedge (`clip-path` triangle) aimed at its target.
- Navigation is a fore-edge thumb index: stepped tabs on the right with geometric glyphs (■ ● ▲ ▬). Each destination opens with a full-screen two-color title spread.
- Two inks plus paper. Red only for action and state. Headings jump scale violently (12vw next to 1.2rem), rotating 90° when cramped. 8px black brackets group content.
- Route changes cut along the diagonal with a hard stop. Depth is shown only as axonometric blocks. One slowly rotating 3D primitive serves as the idle state.
- Palette: `#EFE9DC #141414 #D7261E #8C8A84 #C9C3B6 #B8BCC0`. Type: heavy grotesque caps.

**Alexander Rodchenko.** *Every element is a device that hinges, rotates and changes state.*
- Tilt the hero 12–18° and crop the photo from an extreme low angle. The key word comes out of the image as condensed caps inside a red megaphone wedge.
- Nav labels are stacked vertically and rotated 90° in a 48px black bar on the left. Zones are labeled with stencilled capitals instead of icons.
- Cards hinge open in place (`transform-origin:left`) to 2–3× width instead of opening modals. Stats sit on a three-faced prism that turns 120°.
- Page transitions are a 35° red wipe (220ms, linear-in, hard stop). Yellow or blue appear only as one full-bleed state per flow. Black marks the single "opponent" element (the destructive action).
- Palette: `#D7261E #141414 #EEE8DA #8E9196 #F3C318 #1D4C9E`.

**Varvara Stepanova.** *One small unit, two dyes, and repetition makes the variety.*
- Every background is one 24px SVG tile of at most 3 primitives, half-drop repeated. Each screen uses the ground plus two inks, checked in CI.
- Modules overlap 12px with a 2px black rule. Seams, hinges and grid lines are visible. One 35° red bar carries the CTA.
- Users and series wear "uniforms" (an emblem, a stripe and a color), never color alone. Hover inverts the tile: ground becomes ink and ink becomes ground.
- Vertical rhythm alternates 64px pattern bands with 160px plain bands. Hinge transforms use `steps()` and run under 200ms.
- Palette: `#E6D8BA #15130F #C62A1F #7A1E2C #6B5F3B #F5F2EA`. Type: Rubik Mono One labels rotated 90°.

**Lyubov Popova.** *Structure under load: slanted planes, force lines, a visible scaffold.*
- The main plane sits at −14° and bleeds off two edges. 3–5 overlapping planes are ordered by z-index only, and the front plane gets a 3px light edge.
- 1–2px black force lines in an SVG overlay cross card boundaries and meet at an off-grid node. The grid is drawn as visible struts, with one diagonal brace.
- Three inks at most. Headlines are split horizontally, black on top and red on the bottom (hard gradient stop at 50%).
- Controls look like visible mechanisms: a toggle is a wheel turning 90°, progress a spinning segmented disc. A feature list shows one motif in 4–6 permutations.
- Palette: `#EDE6D6 #C8321F #1B1A17 #8C8A84 #D99A93 #B88A55`.

### 4.4 SWISS / INTERNATIONAL TYPOGRAPHIC STYLE: the grid, objectivity, type as structure
The movement: modular grids, flush-left grotesques and meaning through position and interval. The section ends with its two rebels.

**Josef Müller-Brockmann.** *A measured field with one free, musical gesture.*
- A 6×8 grid whose `row-gap` equals the body line-height, with every card sized in whole fields. All text hangs from an axis at column 2.
- Two type sizes at ≥1:6 (e.g. 14 and 96px), lowercase headlines, `-0.03em` tracking, everything flush-left.
- A ghost word at 30vw in grey sits behind the real title (the *der Film* move). One rule-generated SVG (arcs at radius r·2ⁿ, or squares rotated in 15° steps) bleeds off the top-right.
- Offset exactly one block by half a field. Entrances stagger 80/160/320ms along grid axes. The outgoing headline lingers as grey for 300ms.
- Palette: `#F2F0EA #111111 #E2231A #1F5FA8 #8C8C8C #0A0A0A`. Type: Inter or another grotesk.

**Armin Hofmann.** *Two opposing bodies: a hard sign against a soft image.*
- A huge cropped glyph or a perfect dot at 60vh, offset against a coarse halftone photo (`grayscale(1) contrast(1.8)` plus a dot mask).
- Pure value contrast: ink on paper with two greys, and at most one spot red under 3% of the area.
- A fixed "programme slot" (a bordered rectangle at top-right) for live data, so the layout never reflows. The hero spans 4.5 of 6 columns and bleeds.
- Selection is a solid 8–12px dot above the cap height. Loaders are 12 bars stepping from 1px to 8px in a travelling wave. Empty states are a lattice with the missing cells knocked out.
- Palette: `#F3F1EA #0B0B0B #4A4A4A #9A9893 #D9D6CE #C8201A`. Type: condensed grotesque, leading 0.9.

**Emil Ruder.** *White space is the material; one family varied by its axes.*
- 60% empty paper. The headline block is pinned to the lower-left third, with body text 1.5 columns to its right. No section repeats a module footprint (4/2, 2/4, 3/3 offset).
- One variable family for everything. Change width, weight and size, e.g. H1 at `wdth 75 wght 700` and labels at `wdth 112 wght 400 11px`. Metadata is set light and tight so it reads as a grey plane.
- Comparisons use parallel columns of honest, unequal length. 1px grey rules end at the column edges.
- Hover changes `wdth` from 85 to 100 and widens the gap 4px, with no translation. Selection is a step in grey value, not a pill.
- Palette: `#F4F2EC #141414 #6E6E6A #BDBBB4 #E3241B #2B2B29`. Type: Archivo (width axis).

**Karl Gerstner.** *Design the programme, not the layout.*
- `grid-template-columns: repeat(58,1fr)` holds 2-, 3-, 4-, 5- and 6-column divisions at once. A 3-column article sits beside a 4-column data rail, aligned only at shared lines.
- Components are morphological boxes: parameter rows (size, weight, color step, density, orientation), with each variant one selection per row. Never hand-tune a one-off.
- The palette is 5 equal OKLCH steps between two poles. Meaning comes from step index (1 = surface, 5 = action).
- The hero is purely typographic. A visible permutation control reflows the columns or steps the color, so the system shows itself. Add a "specimen" view of all variants.
- Palette: `#1B1430 #4A2F7A #9C7BD4 #F26A1B #F7A35C #F4F1EA #111111`.

**Wim Crouwel.** *Show the grid as graph paper and build everything cell by cell.*
- A permanent hairline grid of 40px squares at 10–15% opacity. Every element snaps to whole cells (lint for it). Columns cluster 3-1-3.
- All UI text in one grotesque at one size (e.g. 15/20). Hierarchy comes from position and weight only. The display headline is a lowercase modular face 6–8 cells tall, cropped at the edge.
- One red element per screen. Numbers use a dot-matrix face. Freeze constants across a series of pages.
- Headings build stroke by stroke with `steps(n)`. Hover fills a whole cell with solid ink, like a pixel switching on.
- Palette: `#F3F1EA #A9BCC4 #111111 #E3241B #FF3D8B #2BD96B`.

**Wolfgang Weingart (Swiss Punk).** *Keep the Swiss grid and push every rule too far from inside.*
- A visible 12-column grid with exactly one module shifted half a column so it overlaps its neighbor. Section intros step like stairs (`indent: calc(3ch*n)`).
- Track one word to 1em or more at body size, so the spacing alone makes it a headline. Labels reverse out of black bars that overshoot unevenly (2ch left, 9ch right).
- Cyan and magenta planes multiply behind the hero. Coarse halftone replaces gradients. Margins are deliberately unequal (6% and 11%).
- Reveals use `steps()`, each line one beat later. Press offsets the layer 2px like a misregistration. Loaders repeat one word with widening tracking.
- Palette: `#F2EFE8 #111111 #8A8A85 #00A0D6 #E4007C #FFE100`. Type: Archivo, two weights.

### 4.5 MODERNIST ARCHITECTURE: the body moving through space
The movement: proportion from the body, free planes, sequence, light and material.

**Le Corbusier.** *A measured promenade, with color that advances or recedes.*
- All spacing and type come from Modulor red (6/10/16/26/42/68) and blue (12/20/32/52/84) series stored as tokens. Ban every other value.
- A 4-column structural grid with panels that float free of it. One panel is curved on one side only. Main content floats above a dark umber base band with a 32–52px gap.
- Navigation is a promenade: one continuous scroll that switches back left, right, left, with ramp-angled reveals. A full-width 1:7 ribbon window frames the imagery.
- Each plane gets one flat Polychromie color: blue and grey recede, a single vermilion plane advances. A "thick wall" sidebar is pierced with unequal tinted openings. Hover adds light, not size. A 4–6px light gap makes the header float.
- Palette: `#FFF1CE #B5B5AF #395A8E #A33A29 #F2B573 #C6D4BD #333230`. Type: stencil caps for stage labels.

**Mies van der Rohe.** *Free planes on a faint grid, with luxury spent on one surface.*
- A faint bronze column grid (1px at 8%), with content hung *between* the lines. At most 3 free-standing panels of different widths (e.g. 5, 3 and 7 columns), offset so the gaps become paths. Never closed boxes.
- Exactly one golden-onyx surface per screen. The rest is travertine, white enamel lines or grey-green glass (blur 12px at 30%).
- The top 40vh is an empty plaza: one wordmark and one action. The dense core sits at 45/55, never 50/50. Bronze mullion rules run every 64px in tables.
- Components get 3 states only (closed, half, open). Navigate by sliding planes sideways. Radius 0, 1px hairlines.
- Palette: `#E9E2D3 #F7F7F4 #C9A25E #2F4A3E #5B4632 #7E8A86 #1C1C1A`. Type: precise grotesk.

**Frank Lloyd Wright.** *Compression, then release; everything grown from one unit.*
- A 2:1 unit (16×8px) for everything, shown as faint scored joints. Key flows start with a dark 56px entry strip, then release into an ochre band ≥60vh.
- Navigation sits off-axis (left or bottom-left). Content anchors to a dark "hearth" column about 1/5 of the width, and panels cantilever 10–15% past the container.
- Horizontal 2px oak rules, no vertical dividers. 90% earth tones and one Cherokee-red mark. Ornament is a leaded-glass SVG with green and gold squares in threes.
- Panels slide in sideways 24–40px, never scaling from the center. Galleries are one descending ramp with a sticky spine. Hover thickens the top border and dims the surroundings.
- Palette: `#E9E1CC #C7A66B #B07E55 #5E4630 #9C3B26 #6F8A4D #C9A23A`. Type: Josefin Sans tracked caps, Alegreya body.

**Alvar Aalto.** *Design for the real posture; a strict grid with one free curve.*
- A strict 12-column grid broken once per screen by a single wave-edged panel where the main task lives.
- Posture first: primary actions in the bottom 40% on mobile. The header is darker green-grey than the canvas, so the eye settles downward. Light falls from above as a soft radial gradient, never glare.
- One yellow line marks the user's path (progress or active step) and appears nowhere else. Hierarchy is terraced: nested levels indent 8–12px with a 2% tone shift.
- Every control shares the same 6px bent corner. Add faint birch grain deeper in, and a tactile 1px inset on press. Vary gutters ±15% so the grid reads as a forest. Motion settles with overdamping.
- Palette: `#F3EEE3 #D9C3A0 #5E7F74 #E8B92F #3E9A9C #D9692B #24221F`. Type: Source Sans 3, a 1.2 scale with emphasis by weight.

**Luis Barragán.** *A walled courtyard: one saturated wall, thresholds, silence.*
- 60–75% of the screen is one flat field. Content sits in a single off-center rectangular "portal" near the 1:3 line.
- Flows start compressed (28ch, dim, small type), then open into full-bleed space. A full-height color plane acts as a threshold, revealing the next section through a vertical slot that widens on scroll.
- One saturated plane per view, edge to edge (pink, yellow or violet), never as pills or chips. Yellow spills onto its neighbor as a faint wash, like light through glass. A freestanding offset plane overlaps the hero by 15%.
- Headings are tiny wide-tracked caps (12–14px, 0.25em) inside huge fields. Transitions are slow (700–900ms). No sticky chrome. Hover recolors a whole plane.
- Palette: `#E7417A #F2B705 #7A5BA6 #2F5FB3 #C46A2B #EFE8DC #3B3632`. Type: Archivo Expanded.

### 4.6 JAPANESE MA & WABI-SABI: the interval, emptiness, light
The movement: *ma* (the meaningful gap), emptiness as invitation, indirect approach, one material.

**Hokusai.** *Invert scale: the huge near form, and the real subject tiny inside its gap.*
- A foreground shape takes 60–70% of the hero, with the CTA or key number small in its negative space. Show the key metric through a `clip-path: circle()` hole.
- The horizon sits at 72%: one flat graded field above, content packed below. A "36 views" component shows one data object in several framings.
- Blue on blue: translucent Prussian blues multiplied over washi, with no black and no shadows. 1.5px outlines with flat fills. One benigara-red accent. One scalloped wave divider.
- Pull to refresh curls into a wave, holds at the crest, then breaks. Empty states are grids of tiny gesture sketches.
- Palette: `#E9DFC7 #003153 #1E2B3A #9DB8C8 #A8432E #E6C7AB`. Type: Shippori Mincho headings.

**Tadao Ando.** *A dark concrete box, one exact cut of light, an indirect path.*
- A 1:2 tatami module drawn as faint tie-hole dots. Split the key view into three equal bands with the middle one empty and lit, so the user must cross it.
- Concrete greys plus deep shadow. One slot of light (a vertical or cruciform `clip-path`) marks the single primary action. The only hue appears inside a masked window. One element sits 15° off-axis.
- Small tracked grey-on-grey text, with one hero word at weight 200 in the void. Concrete noise at 3–4%.
- Reveals take 0.9–1.4s, with light sweeping from one edge. The gradient follows the time of day. No CTA on arrival: a quiet threshold comes first. Hover darkens the surroundings.
- Palette: `#8E8D88 #C9C7C1 #1C1C1B #F4F1E8 #6B5A45 #3E6A7A`.

**Kenya Hara.** *Emptiness as a vessel the user fills.*
- A horizon layout: two warm-white fields at 55/45 split by a hairline, one ≤24px element on the line, nothing else above the fold. The brand sits at 11px in the bottom-left corner.
- Name containers by what they are ("Notes"), not by prescribed use. Empty states are a blank canvas with one hairline and one quiet prompt.
- One weight (400). Hierarchy comes from isolation (48px+ of space), never from boldness, and size jumps stay ≤1.5×. Ban #FFF: layer 2–3 whites a few percent apart. One burgundy point per screen.
- Paper grain at 2–3%, and a 1px inset on press. Fades take 800ms after a 200ms empty pause. Text measure 32–38ch, top margin ≥20vh. Make one ordinary control slightly unfamiliar (exformation).
- Palette: `#F5F2EB #E9E4D8 #EEF1F2 #3A3733 #8C877E #7F0019`. Type: Zen Kaku Gothic New, with Noto Serif JP for one heading.

**Ikko Tanaka.** *A tangram of flat planes on a grid; edges only where colors meet.*
- Hero and empty-state emblems are built from 5–9 CSS primitives (circles, quarter circles, rectangles) on an 8-unit grid, with no outlines.
- One flat field per zone, with hard color changes and no dividers. The image takes the top 70%. Title, meta and CTA sit in a compact bottom band at 12–14px.
- One vermilion "lips" accent per screen, under 5% of the area. A high-contrast Mincho at 48–72px against a 12px sans caption. Near-symmetry with one element offset by half a unit.
- Planes snap in with `clip-path: inset()` at a 70ms stagger, never with fades or blur. Hover recolors a plane.
- Palette: `#C9C2B4 #F3E9D8 #141414 #D8262E #EFA7A4 #7F0019 #2F5D8A`.

**Kazuyo Sejima / SANAA.** *A field, not a hierarchy: equal rooms in one thin outline.*
- One softly rounded container holds 6–12 rooms of different proportions but equal weight. Rows are offset 8–16px on y. No hero and no single primary CTA: offer 3–4 peer entry points.
- Near-white value steps (2–3%) plus 1px hairlines, never shadows. Color comes only from content seen through translucent panels.
- Headings ≤1.25× body at weight 300–400. Structure as thin as it can be (1px borders, 2px progress). Toolbars float without a slab.
- 500ms opacity/blur dissolves. Hover raises transparency, not elevation. Tabs become one continuous pannable canvas. One reflective "canopy" gradient.
- Palette: `#FBFBFA #F1F2F1 #E3E6E5 #B9BEBF #8A8D8C #2B2D2E #9FB8A6(≤3%)`. Type: Inter 300.

### 4.7 ART NOUVEAU & VIENNA SECESSION: ornament as system, the total work of art
The movement: Gesamtkunstwerk (design everything to the spoon), with ornament concentrated by rule rather than sprinkled.

**Alphonse Mucha.** *A vertical shrine: halo, frame, lettering cast as one piece.*
- A tall format (about 1:2.9 for splash screens). An ornamental title band takes ~15%, with lettering stretched to fill the width exactly via `clamp()` and tracking. The subject sits before a 1.2× gold-rimmed halo disc at the 33% mark.
- Rigid zigzag or tile borders around fluid content (never both curvy). One whiplash vine grows out of the logo. Ornament gathers at the focus, and the outer 30% stays flat.
- Variable-width sepia contours instead of shadows. Muted pastels on tan paper, with gold only for frames and selection.
- Ship it as a Documents Décoratifs kit (frame, halo, border, lettering, flora, 4 seasonal palettes). Hover draws a gold contour over 700ms.
- Palette: `#E9DCC3 #B8A4C9 #E3A48A #9FB7C9 #8A8C5A #C49A3A #3E3330`.

**Gustav Klimt.** *92% flat metallic ornament, 8% tender human detail.*
- A 1:1 hero, 90% flat ornamental field, with one photographic "face" zone (~8%) above center that is never overlaid or animated.
- Two pattern tokens: rectangles (black/ivory) for structure, circles and ovals for personal content. Never both on one element.
- Edges come from changes in pattern density, never borders or shadows. Gold is a field, not a button: ink-on-gold CTAs and one coral accent.
- Motion is only light: a cursor- or tilt-tracked shimmer over the gold (overlay blend), with cells glinting one by one. Onboarding is a frieze strip alternating dense and sparse panels.
- Palette: `#C9A13B #7A5A22 #1E1A16 #C8C6BE #EAD1C0 #3E6B4A #B5432F`. Type: tall inscriptional caps.

**Antoni Gaudí.** *Forces find the form; light-shifting broken color over honest structure.*
- Dividers are inverted catenaries (`y = a·cosh(x/a)`). One integer token (6/8/10/12) drives each component's height, radius, color and size. Nesting halves the padding and grows the radius until the deepest chips become pills.
- Hero surfaces use trencadís: a Voronoi mosaic of 40–120 shards in 3–4 neighboring hues with 2px grout, seeded per user.
- Color is saturated low near the thumb and bleaches to prismatic white at the top. Blue in the morning, red-orange in the evening, following the local clock.
- Lists have serpentine edges with bays holding actions. Media frames use tapered, bone-like mullions. Motion is gravity springs, and dismissed sheets fall along a catenary.
- Palette: `#E9DFCB #2F6FA8 #4F9A86 #D99A2B #C2452D #7B5B8C #FDFBF5`.

**Josef Hoffmann.** *The square as the whole system; edges carry the volume.*
- `--q: 8px`, and every dimension is a multiple of it. Cards get a double rule (1px outer plus a 2px outline inset 6px) in place of shadows. Radius 0, except one deliberate round object per screen.
- Checker bands (8×8 conic-gradient) appear only along the top of the app bar and the footer. Gilt marks only the border of the single focused element.
- Progress and loading show as a perforated lattice whose squares turn black in sequence. Section titles are justified caps in square plaques.
- `steps(4)` mechanical motion. One "tower" element at 1.5× row height. Theme everything as a set, down to the scrollbar, favicon and email.
- Palette: `#F7F5EF #111111 #9C7A3C #2F5D8C #C9A66B #1F3B2D`. Type: Josefin Sans caps.

**Charles Rennie Mackintosh.** *A tall frame first, then one small flower inside.*
- Portrait-only cards and panels (1:4 columns). Content is grouped by "high-back" posts: 2px vertical rules 1.5× taller than their content, ending in a 3×3 grid of 4px squares.
- One register per screen: dark oak with a single lit focal card, or white enamel. Never mixed. Pink and purple stay under 5% of pixels, and silver handles secondary emphasis.
- One stylized square rose, varied slightly at each use. Ornament only at nodes (active tab, CTA, title). A 24px silver frieze replaces the nav bar.
- Crossfade between rooms (dark ↔ white) over 500ms. In dark lists, only the hovered row warms. Headings are condensed caps with offset crossbars.
- Palette: `#F3F0E8 #1C1615 #8B7F70 #B8B8B4 #D79FAD #5B3966 #7C9677`.

### 4.8 MINIMALISM / LIGHT & SPACE: the serial, the specific, perception itself
The movement: no composition, only order, interval, material and light. Perception is the medium.

**Donald Judd.** *One thing after another: the gap is the module.*
- The gutter equals the module (64px rows get 64px gaps). Rows of blocks step by Fibonacci widths (1,1,2,3,5,8 × 16px), with gaps shrinking inversely.
- Every card has the same outer size and differs only by internal splits (50/50, a diagonal hairline, a recessed slot). Dashboards are one row of equal units with no hero.
- One accent applied to a whole face only, never to links or icons. Edges stay raw grey metal. Type sizes come from the progression (13/21/34) and stop there.
- Linear 90ms stagger. Hover moves light across the surface without lifting. The item count adapts to the viewport but the module never does.
- Palette: `#F1EEE7 #BFC3C4 #8E9596 #C9A26B #C8261C #4A2C5E #1C1C1B`.

**Agnes Martin.** *A trembling hand-ruled grid floating on pale washes.*
- A centered square panel (72vmin) with contents inset 5%. Rows are 1:6 rectangles, never squares, sized from the container width.
- Rules are 0.5–1px graphite at 65% with a 0.3px `feTurbulence` wobble, and they stop short of every edge. Sections are translucent washes (alpha 0.25–0.4) of equal lightness over gesso with 2–3% grain.
- Jost 300 at 16px, 0.04em, line-height 1.8, with no bold anywhere. Labels in lowercase mono sit on the ruled lines.
- Only opacity fades, ≥1s, row by row. Hover deepens the wash by one step. Distance works as zoom: collapsed bands expand to reveal the ruled detail. One gold hairline action per screen.
- Palette: `#F5F2EB #E9DAD3 #D3DFDC #F2EBC6 #D9CCB6 #9A9893 #C2AB78`.

**Dan Flavin.** *Color is a source, not a fill: light thrown onto edges and corners.*
- A flat charcoal ground with no cards. Structure is 3–4px glowing bars on edges and inner corners, in four lengths only (25/50/75/100%).
- Accents glow outward (`box-shadow: 0 0 24px 6px` in their own hue at 35%), tinting neighboring surfaces. Where two glows meet they blend with `screen` to pale white. One emitted hue per app zone.
- An inner-corner L of two bars plus a radial gradient makes the panel brightest at the fold. One 45° bar marks the single most important element.
- Elements flicker on (opacity 0 → .8 → .2 → 1 over 120ms), then bloom. Paywalls are see-through barriers of vertical light bars. Toggles have a pink face and a green face. Headings are lowercase with parenthetical dedications.
- Palette: `#1A1B1E #F2F7FF #FFF1D6 #5BFF7A #FF6FB5 #FFD23F #6B3CFF`. Type: Barlow Condensed.

**James Turrell.** *One field of light, one knife-edge aperture, slow perception.*
- One flat field covers ≥75% of the viewport. All content sits in one borderless aperture defined only by a 4–8% lightness step. No borders or shadows (focus rings excepted). The canvas edges fade into the field with a radial mask.
- Hero and empty states are 3–5 nested elliptical rings, each ~3% lighter.
- The frame color drifts over 60s (dusk pink → lilac → twilight grey) while content stays fixed. Errors and successes tint the whole field for 2s instead of showing badges.
- Hover is +6% luminance over 400ms. Drill-down grows the aperture from 20% to 100% over 900ms while the field dims. On entry, the bare field shows for 1.2s before content resolves (dark adaptation). Never bold.
- Palette: `#F2EEF3 #8C8A97 #3B4FB8 #E9A3B9 #9B7FD1 #F2A541 #14131C`. Type: Jost 200, Manrope 300.

**Sol LeWitt.** *The screen is an executed instruction; enumerate every valid variant.*
- Write the layout as a rule ("3×4 cells, one variant each, sorted by X") and print it in small mono on the screen.
- Show every valid combination in a matrix instead of a curated top 3, sorted along one labeled axis. The base module is deliberately dull: a hairline square, no radius. Keep a 1:8.5 frame-to-void ratio.
- Color by index (`nth-child(4n+…)` → red, yellow, blue, grey). Overlapping states multiply as washes. Every instance gets a catalogue code ("4/12").
- Generated art and avatars are seeded by user ID. An "instructions" toggle reveals each visualization's rule. Bold mode is full-bleed flat primary bands. Linear sequential reveals.
- Palette: `#F4F2EC #2B2B2B #D2322D #F2C230 #1F4FA3 #8C8C88 #E8742A`. Type: IBM Plex Mono.

### 4.9 OP & KINETIC ART: the eye and the moving viewer complete the work
The movement: color and movement happen in perception and in the user's own motion. Apply the guardrails strictly here.

**Bridget Riley.** *Hold everything constant except one variable, changed at a designed tempo.*
- Lists compress geometrically toward the selected item (row heights 64 → 32px, then reopening). The densest point sits 62–67% across, never at center.
- Saturation ramps from grey at the edges to full vermilion and turquoise in one band under 15% of the screen. Test every color beside its real neighbor.
- Archivo `font-stretch` runs 125% → 70% across the nav, with the active item most compressed. Separators are sine waves whose amplitude rises toward content.
- Curved stagger timing. Loaders are slow ≥2s waves through 1px lines. Scroll shifts the phase of a stripe field. Required: avoid pattern glare, honor reduced motion, keep text on flat panels, offer a "calm surface" toggle.
- Palette: `#F3F0E8 #151413 #8E8D89 #E4472C #23ADA8 #C9B3D6 #E9C46A`.

**Victor Vasarely.** *A plastic-unit alphabet: square ground plus inset form plus numbered color.*
- One square token `--u`, with every element 1u, 2u or 4u. Components are `ground + form + color index` permutations (`<Unit form="disc" ground="blue-3" figure="yellow-1">`).
- A Vega radial lens: the main KPI sits at the bulge peak at 2×, and the surrounding tiles shrink with distance. List rows step along a ramp (blue-1 → blue-7).
- States invert figure and ground. Empty states are 4px Zebra stripes, with shapes made only by a 90° stripe turn. Exactly one inverted unit marks the CTA.
- A "Folklore" mode lets users rearrange their grid, saved as a shareable code. Interactions send scale waves through neighboring cells.
- Palette: `#0E0F1A #2433A6 #6A2C91 #E0402A #F4C21B #15936A #F3F1EA`. Type: tracked Jost caps, Space Mono codes.

**Carlos Cruz-Diez.** *Color is an event between bands, a function of the viewer's position.*
- Full-bleed `repeating-linear-gradient` bands at a 4px pitch, with content on the field and never in cards. Interleave 2px red and 2px green so yellow appears optically. Real yellow is reserved for the one critical action.
- Two band layers parallax at different scroll speeds (1.0× / 0.85×). Pointer x maps to `--phase`, offsetting the bands by up to half a pitch.
- Color animates only through `animation-timeline: scroll()`, never on a timer. Each route floods with one light-primary tint, with 20–30vh blend thresholds.
- Stem-heavy condensed headlines are clipped to the stripes. One circle intrudes per screen. A progress strip along the bottom advances its band sequence.
- Palette: `#E1252B #14A04A #1E4FB8 #0D0D0F #F3F1EC #D8246F #F4C21F`. Type: Big Shoulders Display at 10–14vw.

**Jesús Rafael Soto.** *Form from the density of identical strokes; solid from afar, strands up close.*
- A ground of 1px black lines at a 4px pitch, with sparse foreground bars moving 2–6px with the cursor to make moiré.
- Hero shapes are a grid of 2px bars, colored inside an ellipse and 15% grey outside, with no outline. Alternate rows are offset half a column.
- 90% achromatic. One saturated yellow for the "virtual volume" (the current selection). Inactive items are 30–40% translucent strands.
- Hover parts the bars with a damped spring, like a curtain of tubes around a hand. Semantic zoom: a dataset reads as one mass, then splits into strands as you zoom. Depth comes from stripes crossing at 2–5°.
- Palette: `#F5F3EE #111111 #F2C200 #1F4FA8 #D8DDE0 #C8102E`. Type: tracked monolinear caps.

**Julio Le Parc.** *A running system of a closed set of parts that the user plays, breaks and rebuilds.*
- A near-black chrome frames a small lit window (15–25% of the viewport) holding a 12×12 grid of identical tiles. All content is tile states.
- Colors come from a closed ring of 14 pure, equal-lightness hues, always shown as ordered runs of ≥3, never alone and never tinted. States move position along the ring.
- Number everything as series ("Variation 07/14"). A permute control shows its rule ("shift +3"). Dismantle/reassemble buttons make breaking things safe.
- Idle tiles sway on random phases (static under reduced motion). A cursor light throws reflected squares. Onboarding is a playful itinerary of physical actions.
- Palette: `#0B0B0D #F4F4F0` plus a ring: `#E5222B → #FFB000 → #19A34A → #1F5BD8 → #C2188B`. Type: Archivo Expanded, Space Mono.

### 4.10 POSTMODERN & NEW WAVE: irony, collision, layered depth, type as voice
The movement: against "good taste" functionalism. Personality, density and noise as message. Keep functional UI legible.

**Ettore Sottsass (Memphis).** *An object with a personality: a figure standing on a grid.*
- The lower 60% is a 6-column block grid with every card a different flat hue and no white cards. Above it, one 30° slanted "arm" juts 1.5 columns past the container. Section dividers slant 30° in alternating directions.
- A tiled black squiggle (Bacterio) works as a plinth under cards and footers, never behind text. One red primary action, and one deliberate clash (pink on red).
- Headings in Rubik Mono One at 3–4× on color blocks. Labels in Space Mono uppercase like typewriter keys. Icons are built from 2–3 primitives with 2px black seams.
- Overshoot springs on mount, hover tilts 2–3°, and a toy-like "spool cap" knob rotates on press.
- Palette: `#E2231A #FFD100 #1F4FB4 #F5A3C7 #8ED8C8 #F4F1E8 #111111`.

**April Greiman.** *A deep video composite with the tool's artifacts left visible.*
- Build from ≥4 planes, each with its own `translateZ` and parallax speed (`perspective:1200px`). The hero strip rotates −11° across two layers while body text stays at 0°.
- A violet → magenta → orange gradient field, never flat white. One huge image pixelated 6–10× (`image-rendering: pixelated`) beside razor-sharp vectors.
- Hard-offset shadows (`6px 6px 0 cyan, -3px -3px 0 red`). One DayGlo-orange focal action. Bitmap 10px timecode metadata at the layer edges, plus ghost dot-grid fragments.
- Images load from pixel blocks to sharp as a designed sequence. Hover splits elements into cyan and red copies for 150ms. Horizontal timelines enter at different depths.
- Palette: `#1B1035 #E0457B #FF6A13 #00A6D6 #E3242B #D4F542 #F4F1EA`.

**David Carson.** *Legibility is not communication; the page as painting (expressive surfaces only).*
- The headline sits across the image, covered 15–30%. One column rotates 3° and breaks its column by 1.5× into the gutter. Display leading 0.78, with mixed sizes inside one headline.
- Grayscale high-contrast photos with one spot color multiplied on top at a 4px misregistration. Photocopy noise and torn edges. Micro-captions cluster in one corner while the opposite corner stays empty.
- Hard-cut `steps(3)` transitions with jitter. Hover tears the letterspacing open or briefly swaps in dingbats.
- **Use** it only for heroes, editorial pages, splash screens, 404s and share cards. **Never** for nav, forms, checkout, settings, errors, tables or long body text. At most one illegible element per screen, decorative or with a legible duplicate.
- Palette: `#E8E3D6 #151311 #8D8A84 #C4471C #00A0BE #D6E02A`.

**Paula Scher.** *Type as a loud crowd held by one blunt structure.*
- Mix weights inside one line (300 and 900). Headlines bleed off the edge and crop mid-letter, never shrinking to fit. At most three sizes, with the largest ≥6× body.
- A strict orthogonal grid with one band rotated −12°. Thick 6–10px black rules, some diagonal, replace cards. One accent hue per section, and everything else ink on paper.
- Directories, sitemaps and footers become dense typographic maps: justified all-caps walls with size set by popularity. Headlines wrap around cutout photos (`shape-outside`).
- Syncopated `steps(3)` entrances with irregular delays. Hover pushes variable weight and width. The logo reduces to a two-second gesture.
- Palette: `#111111 #F4F1EA #E2231A #FFD200 #0057B8 #FF3C78`. Type: Anton or another condensed wood-type face.

---

## 5. Fast recipes

- **"Give me options" (default):** run Phases A–C with 5 variants: one Swiss (Crouwel or Gerstner), one Ma (Hara or Ando), one Modernist (Barragán or Wright), one Secession (Klimt or Hoffmann), and one Kinetic or Postmodern (Le Parc or Scher).
- **Calm productivity tool:** Ruder, Sejima, Agnes Martin, Aalto, Mies.
- **Data dashboard:** Gerstner, Judd, LeWitt, Vasarely (lens), Mondrian (Boogie mode for live data).
- **Brand or marketing landing page:** Scher, Lissitzky, Barragán, Klimt, Greiman.
- **Onboarding or flow:** Wright (compression and release), Ando (threshold), Le Corbusier (promenade), Lissitzky (thumb index).
- **Playful consumer app:** Sottsass, Le Parc, Kandinsky, Huszár.
- **Wild card:** ask for two artists from opposite corners of the axes map and force a synthesis ("Agnes Martin × Rodchenko").

## 6. Variant card template

```
VARIANT X: <Movement> / <Lead artist> (+ <secondary>)
The move: <one sentence>
Rules applied: 1… 2… 3… 4… 5…
The one rule-break: <what and where>
Palette: <hex: role, …>
Type: <families, sizes, ratio>
Motion: <grammar + durations>
Interaction: <hover/focus/select behaviour>
Genes offered: X-layout · X-color · X-type · X-motion · X-interaction · X-texture
Guardrail notes: <contrast, legibility, motion-safety checks>
```

## 7. Provenance note
These rules were distilled from museum, foundation and scholarly texts about each artist's works, plus general knowledge. They were not taken from direct image analysis. Hex values are approximations, and a few proportions are commonly cited analyses rather than measured facts. When images of the works are available (user uploads, browser access), look at them and correct an entry before relying on it heavily.