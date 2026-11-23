# Worked example: mobile bank, board "Rail" → kit → Home → Send money

This is the method of SKILL.md §1 run end to end. A build of it, with the same content as the five strict studies (balance €2,481.36, groceries €372 of €400, 8 days left), is in `references/worked-example/`: `brand-book.html`, `kit.css` (v1.1, which adds a Nav component through a recorded kit change), `home.html` and `send.html`. The figures below are the original worked numbers; plate claims were checked against the corrected entries.

The request is one screen (home: balance, recent transactions, send/receive, a budget warning). The method still produces board → kit → screen, and a second screen (Send money) is then derived from the same kit to show the lock holding.

### Stage 1: Brief
- **Case.** Adults checking several times a day, one-handed, often in public, for 5–10 seconds. No brand given, so the ink is case-derived (a dark green-black: calm, legible, not the domain's default blue), marked *assumed, unconfirmed*. iOS/Android system navigation untouched. AA contrast, tabular figures, nothing that makes a figure ambiguous.
- **Inventory.** Home, Send money, Receive, Transaction detail, Budgets, Cards, Settings. Components: key figure, list row, form field, forecast, action bar, sheet, fault notice, empty, loading.
- **Content truth.** Money moves through a month: a past you cannot change, a now, and a short future you can still affect.
- **Problems (product-wide).**
  1. **(crux) Urgent without alarm.** Forecasts (budget running out, a payment not covered) must be noticed in a glance and must never look like fraud, an error or a nag. *Home, Send, Budgets, Cards.*
  2. **One figure wins the glance** without the shouting that makes a bank feel like a game. *Every screen has one: balance, amount, limit.*
  3. **Trust.** Exact and still. Nothing jumps or reflows. *Everywhere.*
  4. **Dense records** stay scannable; in vs out clear without leaning on red and green. *Home, detail, Budgets.*
  5. **Position in time.** Where am I in the month, and in a flow. *Home, Budgets, Send.*
  6. **Actions under the thumb** that compete with neither the figure nor the forecast. *Every screen with an action.*

### Stage 2: Mood board "Rail"

| # | Plate | Answers | Principle | Take (with calibration) | Leave | Layer |
|---|---|---|---|---|---|---|
| 1 | **Aalto, Paimio Sanatorium** (yellow floor from lobby to top floor; rooms designed from the patient's posture) | 1, 5, 6 | Put the signal on the route the person is already on; design from the body's real position | A marked path through the screen that carries position and signal; actions where the thumb is | The yellow, the curve, the wood | structure |
| 2 | **Müller-Brockmann, *der Film*** | 2, 4 | Two sizes far apart, everything hung from one axis; labels against the axis, values from it | One hang line; two type sizes with nothing between (poster 1:13 → phone 1:4) | The 28% axis position, lowercase, overlapping words | type (and fits inside plate 1's structure) |
| 3 | **Klee, *Sunset* 1930** | 1 | Scarcity makes the signal: one small mark in a quiet field | A point signal held under 1% of area (the disc measures 0.7%) | The red, the dot lattice, the arrow | colour: signals |
| 4 | **Barragán, Casa Gilardi corridor** | 1, 5 | A signal is calmer as light that spills than as paint on an object; a small opening at the end shows what comes next | A small strong dose plus a large faint one; a fixed place that previews the future; slow tempo (700–900ms) for the system's news | Every hue, the walls, the slots | motion (system news); supports colour |
| 5 | **Sejima/SANAA, 21st Century Museum, Kanazawa** | 3, 4 | Surfaces part by small value steps and hairlines, not borders and shadows | Grounds ~4–5 L apart with a cool cast; 1px structure; tint always low-chroma | The circle, the glass, the no-hero plan | colour: surfaces; interaction (value step on press) |
| 6 | **Judd, *Untitled (Stack)* 1967 and the 1969 progression** | 3, 4 | The module never changes, only the count; rhythm from interval and a stated series | Fixed row and slot heights; marker sizes in a stated series (5, 8, 13); linear 80–90ms stagger | Boxes, metal, the single lacquer colour | structure (module); motion (user actions) |
| 7 | **Le Corbusier, Villa Savoye** (visually checked: dark green #657E5E recessed ground floor under the white volume) | 3, 6 | The darkest plane sits lowest and carries the load | A dark full-width base that holds the actions | The green, the pilotis, the Modulor | structure (fits inside plate 1) |
| C1 | **Case: the content at its worst** — "+€12,480.00", "Zahnarztpraxis Dr. Hoffmann-Lindqvist", a month with 2 transactions, a month with 140 | all | — | Tabular figures, truncation on the payee never on the amount, fixed slots | — | — |
| C2 | **Case: use in public, 5 seconds, one thumb** | 2, 6 | — | Figure can be covered; nothing important in the top corners | — | — |

**Thesis.** The month is one rail. What is still open sits above today, what is settled sits below, and the one thing that needs you appears on the rail ahead of you.

**Layer owners.** Structure: plate 1 (with 6 and 7 inside it). Colour: plate 5 for surfaces, plate 3 for signals (different roles). Type: plate 2. Motion: plate 6 for the user's actions, plate 4 for the system's news. Interaction: plate 5.
**Bundle limit.** No artist owns more than two layers; none owns both structure and colour. The crux has three sources (1, 3, 4).
**Tension kept, by role.** Hard jump for the one key figure on a screen ↔ flat equality, one size, for everything else (plate 2 ↔ plates 5 and 6).
**Scouted and cut.** Hokusai's scale inversion (a tiny balance fails a 5-second glance). Turrell's whole-field tint for 2s (a flashing bank screen reads as a fault). Mondrian's Boogie lanes (answers problem 1, but plate 1 already does and its primaries-in-lanes device is too signed). Crouwel's figure-inside-the-colour-field (spends the only colour on the wrong thing). LeWitt/Gaudí per-user seeded art (decoration on a money screen; no problem asks for it).
**Rejected board, "Level":** every screen split by a waterline whose height shows what is left. Vivid, but layouts would move with the data, which fails problem 3.

### Stage 3: Kit "Rail" v1.0 (condensed brand book)

**Principles.** **K1** One rail per screen; everything hangs from it. **K2** One key figure per screen. **K3** Open above, settled below. **K4** One signal, and only for the future. **K5** The base carries the actions.

**Structure** (390pt reference width; scales by margin, never by module)
- **S1 Rail.** A 1px ink hairline at x = 64, the only vertical on any screen. Left of it a 36px label column (x 16–52), text flush right. Right of it everything hangs flush left at x = 80. Values that are amounts sit flush right at x = 374.
- **S2 Module.** Row 52. Forecast slot 120. Base bar 56 + safe area. Spacing tokens 4, 8, 12, 16, 28. Heights never change with data; only counts do.
- **S3 Archetype** (every screen): **Head** (the key figure) → optional **Fields** → **Ahead** (forecast slot) → **Edge** → **Settled** (records) → **Base** (actions). Zones may be absent; their order never changes.
- **S4 Edge.** The change from open to settled is a ground step, full width, no rule.

**Colour** (roles, tokens, budgets per screen)
- **C1** `--ground-open #E9ECEA`, `--ground-settled #DFE3E0` (≈4 L apart). Together ≥75% of the screen.
- **C2** `--ink #10201C` (case-derived): text, rail, markers, base. `--ink-2 #4E5B56`: secondary text (≈6.0:1 and ≈5.5:1 on the two grounds). Ink planes ≤20%.
- **C3** `--signal #B06A00`: forecasts that need the user. **At most one signal element per screen, ≤1% of area**, never text, always paired with thickness, a ring and words. Its spill `--signal-cast #EFE7D6` fades from the rail to the ground within the Ahead slot only.
- **C4** `--fault #B3261E`: failures and fraud only, as a 4px top edge on an ink notice block, or on the rail segment of an invalid field. Never in the Ahead slot. Signal and fault never share a form.
- **C5** No other hue exists. No success green: a settled thing is shown by moving below the edge (K3).
- Dark mode: values invert, the 4 L step, the single signal and the heavy base remain.

**Type**
- **T1** One variable grotesque with tabular figures and a width axis, chosen from the brand. No second family.
- **T2** Two sizes: `--t-text 14/20` and `--t-figure 56/56`. Controls in the base bar use 16/20, the same step set for a control. Nothing else.
- **T3** Hierarchy otherwise by weight (400, 600; 300 for the decimals of the figure) and by position against the rail.

**Line and shape**
- **F1** Two weights: 1px (rail, dividers inside the base) and 4px (signal or fault segment). **F2** No cards, boxes or shadows; nothing has a corner to round. Focus ring: 2px ink, 2px offset. **F3** Markers on the rail: filled = in or done, hollow = out or pending; diameters 5, 8, 13 by amount band.

**Motion**
- **M1** *The user's actions are ink:* the rail draws (360ms linear), items appear as it passes (opacity only, 80ms stagger, 600ms cap), press is a 120ms value step. **M2** *The system's news is light:* the signal and its cast fade in over 800ms, last. **M3** Nothing translates, scales, bounces or counts up, except platform sheets. Reduced motion: everything present at once.

**Interaction**
- **I1** Press, select: one value step (settled ↔ open; ink → `#22332E`). **I2** A row is one target, ≥52px. **I3** The one unfamiliar control in the product: press and hold the key figure to cover it with an ink bar of the same footprint (no reflow); a visible "Hide balance" toggle in the account menu and the keyboard shortcut H do the same.

**Components** Rail · Marker · Key figure · Row (label column | text | amount) · Field (a Row whose text is editable; label in the label column) · Ahead slot (states: clear, watch, over; never collapses) · Edge · Base bar (one cell, or two equal cells split by a hairline; docks above the keyboard) · Notice (fault) · Empty (the rail with open ticks and one sentence) · Loading (rail draws, hollow markers).

**Voice** **V1** Forecasts are dated and quantified, in the future tense: "runs out Sat 22", "would be €102.80 short". **V2** Records are past tense and bare. **V3** No exclamation marks, no "Warning", no praise. Amounts always carry currency and two decimals.

**Exception** **X1** The signal segment is the only thick, coloured, slow thing in a hairline, achromatic, quick system. One per screen.

**Do / Don't** Do hang every text from x = 80. Do keep the Ahead slot when it has nothing to say. Don't add a card, a shadow, a merchant logo or an avatar ring. Don't use a third type size. Don't colour an amount. Don't use the signal for promotion or praise. Don't use primaries with black rules, cream paper, or a rotated label. Don't animate a figure.

**Provenance appendix** (the only place sources are named)

| Rule | Problem | Principle | Plate | Left behind |
|---|---|---|---|---|
| K1, S1, S3 | 1, 5 | The route carries position and signal | 1 (2 for the hang line) | Yellow floor, curves, 28% axis |
| K2, T2 | 2 | Two sizes, one axis, nothing between | 2 | Lowercase, overlap |
| K3, S4, C1 | 3, 5 | A value step is an edge and can carry meaning | 5 | Glass, circle |
| K4, C3, X1 | 1 | Scarcity makes the signal; point signal ≤1% | 3 | Red disc, arrow |
| C3 cast, M2, Ahead slot | 1, 5 | Strong small dose plus faint large one; a fixed opening onto what is next; news arrives slowly | 4 | All hues, walls |
| S2, F3, M1 | 3, 4 | Fixed module, variable count; stated series | 6 | Boxes, lacquer |
| K5, Base bar | 3, 6 | Darkest plane lowest; actions at the thumb | 7, 1 | Green band, pilotis |
| I1 | 3 | Change the value, not the elevation | 5 | Transparency effects |

**Kit checks on the specimen** (Home, Send, an empty Budgets). *Name:* a hairline, dots, one large figure, grey-green fields, a dark base; "Swiss-ish" at most for the alignment, no artist nameable; the signature bundles (primaries + black bars, cream + red, a saturated wall, a visible square grid) are absent. *Caption:* each rule above reads as a reason about glancing, forecasting or trust once the plate column is removed. *Swap:* a navy ink and a humanist sans leave the rail, the edge and the single signal intact. *Elsewhere:* needs a quantity, a period and a forecast; it would suit an energy or data-allowance product (same content truth) and not a messenger or a shop. *Three medians:* no cards, shadows, radius, gradient hero card, logo circles, round action buttons, donut, brand blue; no cream, vermilion, rotated label or `steps()`. *Reach:* every principle K1–K5 appears on all three. One honest residue: a line with dots is a known tracking-timeline pattern; what is new is the half that lies in the future and a warning expressed as a gap. If Home reads as parcel tracking in the build, shrink the markers (a kit change, so everywhere).

### Stage 4a: Home, built from Rail v1.0

Skeleton: balance €2,847.20; 7 recent transactions; Send, Receive; Groceries €344 of €400 on day 19 of 30. Archetype S3 without Fields. Reference frame 390 × 844, safe areas 47 and 34.

- **Head, y 47–212, `--ground-open`.** Account name at 14px on the hang line. "Available", then the key figure `€2,847.20` at 56px, weight 600, decimals weight 300 (K2, T2, T3). 28px of empty ground below. Nothing else (Don't list).
- **Ahead slot, y 212–332.** Today at the bottom edge, day 30 at the top, 11 days at ~10.9px each. At the present pace (€18.1 a day, €56 left) Groceries runs out on day 22. The rail is ink from today to day 22 (y ≈ 299), then a 4px `--signal` segment from there to month end, 87px: the eight uncovered days. A 9px signal ring sits at the run-out point; `--signal-cast` spreads right of the rail (C3, X1). Hung at x = 80: "Groceries runs out Sat 22" (600) and "8 days short at this pace · €56.00 left" (`--ink-2`) (V1). The row is one 64px target. Label column: "30" at the top, "19 today" at the bottom.
- **Edge, y 332.** `--ground-open` → `--ground-settled` (S4, K3).
- **Settled, y 332–754.** Rows of 52. One marker per row on the rail, filled for money in, hollow for money out, 5/8/13 by amount (F3), so the rail reads as a rhythm of spending before any text is read. Day number in the label column on the first row of each day, 12px extra between days, no dividers. Payee at x = 80; amount flush right, outgoing 400, incoming 600 with "+" (T3, C5: no coloured amounts).
- **Base, y 754–844.** Ink bar, two equal cells: Send, Receive (K5). The list scrolls beneath it.
- **Motion.** Rail draws from the figure downward, rows appear as it passes; the signal fades in last (M1, M2). The balance is present from the first frame.
- **States.** No forecast: the slot stays, plain ink rail, "On pace · 11 days left". Already over: the signal segment starts at today, "Groceries is €12.00 over · 11 days left". Empty: Empty component, "Nothing has moved this month."

Budgets: grounds ≈78%; ink ≈14% (base 11% plus text and marks); signal ≈0.15%, one element. Coherence: all values are tokens; components all from the kit; citations as marked; no artist named.

### Stage 4b: Send money, from the same kit (no library opened)

Skeleton: amount, recipient, source account, note; consequence of sending; history with this person; one action. Same archetype, this time with Fields.

- **Head.** "Send", then the key figure: the amount being typed, `€120.00`, at 56px. It is the screen's one figure (K2), so the balance does not appear at 56px here; it appears as a 14px line beneath, "of €2,847.20 available".
- **Fields.** Three Rows of 52 hung on the rail: label column "To", "From", "Note"; values at x = 80 ("Ana Ruiz", "Everyday ··42", "Dinner"). A filled marker appears on the rail beside each field as it is completed (F3: filled = done). An invalid field turns its rail segment `--fault` with a sentence beneath (C4). No boxes around inputs (F2).
- **Ahead slot, 120, same component.** It answers "what will this do to my month?". Clear state: "After this: €2,727.20. Rent €950.00 on Fri 28 is covered." in ink, plain rail. Watch state, if the amount were €2,000.00: a signal ring on the rail at day 28, the 4px signal segment from day 28 to month end, the cast, and "Rent €950.00 on Fri 28 would be €102.80 short" (K4, C3, V1). The same form means the same thing as on Home (L4).
- **Edge**, then **Settled:** "Earlier with Ana Ruiz", Rows with hollow and filled markers.
- **Base.** One cell: "Send €120.00" (K5). It docks above the keypad.
- **After sending.** No green tick, no confetti (C5, V3). The amount row gains a hollow marker and drops below the edge into Settled, by the M1 draw; the Head returns to the new balance. Settled is where done things live (K3).

**What the lock did here.** A flow screen invites a different idea: a stepper, a celebratory success state, a colour for "sent". Each would be a second style. The parking list for this screen has one entry ("a progress device for multi-step flows such as adding a payee: could the rail carry step ticks?"), to be answered at v1.1 from the existing board (plate 1 already covers it) and then applied to every flow at once.

**Sibling and crop tests.** Home and Send share the rail at x = 64, one 56px figure, the 120px slot in the same order, the edge, the ink base. A 200px crop of either shows a hairline with hung text on grey-green, which is the product.

**Guardrails.** Text ≥5.5:1; signal graphic ≈3.6:1 and never alone; targets 52–64px; no timer-driven motion; reduced motion honoured; figures never animated or cropped. Contrast values are computed estimates and must be re-measured in the build.
