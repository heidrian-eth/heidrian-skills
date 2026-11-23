# Exploration mode: two worked fusions (seed 7)

See SKILL.md §1, Stage 2, "Exploration mode: ten fused triads". Specimens are specified with numbers, not built.

### The brief, held constant (Stage 1, as in `WORKED-EXAMPLE-rail.md`)

- **Case.** Adults, several checks a day, one thumb, in public, 5 to 10 seconds. No brand.
- **Content truth.** Money moves through a month: a past you cannot change, a now, and a short future you can still affect.
- **Problems.** P1 (crux) urgent without alarm · P2 one figure wins the glance · P3 trust: exact and still, nothing jumps · P4 dense records stay scannable, in and out told apart without red and green · P5 position in time · P6 actions under the thumb.
- **Specimen constants.** Home at 390 × 844. Balance €2,481.36 (worst case €12,480.00). Budget: Groceries, €372 of €400, 8 days left. Send, Receive. Eight transactions, newest first: Lidl −€41.87 · NS Reizigers −€12.60 · Zahnarztpraxis Dr. Hoffmann-Lindqvist −€85.00 · M. de Vries +€40.00 · Spotify −€10.99 · Albert Heijn −€23.40 · Bol.com −€64.95 · R. Jansen +€18.50. Neutrals plus one attention hue, case-derived and *unconfirmed* (an ochre; red stays reserved for faults). A board shows as many of the eight rows as its own rule allows, and that count is a finding.
- **Draw.** `python3 scripts/triads.py --seed 7`, level artists. No re-draws (reasons below).

---

### T01 "Open Ends": Josef Hoffmann × Gerrit Rietveld × Donald Judd

This one fuses plainly. Its risk is the opposite of a clash: two members are nearly the same.

**Profile, in the case's nouns**

| | Unit | Exception | Change | Mechanism | Fails here |
|---|---|---|---|---|---|
| Hoffmann | one square at 2–3 scales; blank planes; a line on every edge | pattern only where something opens: a cluster of small squares; one filled panel | cells fill one at a time, counted | likeness of one unit; oddness of the one texture | a payee name has no unit size; small cells cannot be targets |
| Rietveld | parts named by kind; parts pass, never merge | colour only on what ends or moves; fixed is neutral; the most saturated is the smallest | a part persists and slides on one track | depth by overlap; bright ends tick off the parts | eight equal rows turn overshoot into noise; 390px is near his limit |
| Judd | one envelope; the gap is derived from the unit; no rank | every difference sits inside the envelope | constant stagger; press changes light, never size | figure and ground in balance; total likeness | the warning and the primary action must outrank; gap = unit halves capacity |

**Bridge: lock and key, twice.** Judd fails where one item must outrank the rest. Rietveld and Hoffmann each hold a way to mark one unit without changing its envelope: colour on its end, and a counted cluster where it opens. Rietveld in turn fails on many equal items, which is the one thing Judd is for. There is also a shared mechanism, grouping by likeness of one unit (Hoffmann, Judd). That is the warning sign of a duo: both cannot own structure.

**Cast**

| | Skeleton | Charge | Behaviour |
|---|---|---|---|
| Hoffmann | 2 | 1 | 2 |
| Rietveld | 0 (equal rows) | 2 | 2 |
| Judd | 2 | 0 (20–40% of every unit saturated floods a calm money screen and cannot single one out) | 1 |

Best: **Judd Skeleton · Rietveld Charge · Hoffmann Behaviour** = 6. Runner-up: Hoffmann Skeleton · Rietveld Charge · Judd Behaviour = 5.
Layer owners: structure Judd · colour Rietveld · type Judd · line and texture Hoffmann · motion Hoffmann · interaction Rietveld. Two layers each, nobody holds structure and colour.

**Run on the content**
- *Skeleton on "money through a month".* Every record is the same unit. Judd's second mode (constant units, gaps stepped by a fixed decrement) is run from now into the past: each gap is 0.75 of the one before. The open present has air around it and the settled past closes up into a block. The interval carries recency.
- *Charge on the crux.* "Fixed is neutral, what moves is coloured" becomes: settled money is neutral, money that is still open carries the hue, on its end. The budget is a unit like any other. It does not grow, turn red or jump the queue. It sits where the content truth puts it, between now and the past.
- *Behaviour on state.* "Pattern only where something opens" becomes the count: a unit that is running towards a limit shows a small cluster of cells, and the same cluster says "this one opens". Cells fill in counted steps.

**Collisions**
1. Hoffmann's square module vs Judd's envelope → **parameter**: the envelope is 26 × 4 cells of 14px, and the unit's leading end is a 4 × 4 square.
2. Hoffmann's line on every edge vs Judd's "every edge is two planes meeting" and Rietveld's "no closed boxes" → **dropped** from units (structure owner). It survives inside Hoffmann's own layer: the cells of the cluster.
3. Hoffmann's symmetry → **dropped**: the structure owner centres nothing.
4. Judd's colour on a whole face vs Rietveld's 1–3% on ends → the colour owner wins. Judd's "same face in every unit" becomes a **parameter**: the mark is always on the leading end.
5. Rietveld's overshoot vs Judd's "outer size never signals" → **dropped** from the run (it is also Rietveld's own failure case). Kept once, where kinds differ: the action bar is a different kind of part, runs past the run by 13px on both sides, and the run passes beneath it.
6. Judd's gap = unit vs the case (dense records) → the case wins, and Judd's own decrement mode is used.
7. No rank vs P2 → this is the **one tension kept**, by role: the screen's one key figure is Judd's "constant element beside the series" and takes the only scale jump; everything else is flat. The 1:4 ratio comes from the case (a 5-second glance).
8. Hoffmann's counted fill vs the guardrail on money figures → cells animate only when the count changes. The figure beside them never moves.

Why no re-draw: each member's failure applies in one role only, and each was cast away from it.

**Thesis.** A month of money is one run of equal units that closes up as it recedes into the settled past; nothing grows to be noticed, and only what is still open carries a mark on its end and a count of what is left.

**Specimen (390 × 844; module 14px; unit 364 × 56; side margin 13)**
- y 61–173, the constant element: label "Balance" at 14px, then €2,481.36 at 56px, tabular, on the bare ground. Two type sizes in all, 14 and 56 (1:4). The worst case €12,480.00 is about 325px wide and fits.
- Gap 56, the largest in the run.
- y 229–285, the budget unit, same envelope as every row. Leading end: a 14 × 56 cap in the attention hue. Text: "Groceries" in semibold, then "€372 of €400 · 8 days left". Trailing: a cluster of 10 cells, 5 across by 2 down, 10px squares on a 14px pitch (bar to pitch 0.29), €40 each. Nine are solid ink; the tenth, part-used, is in the hue and carries the label "€28 left".
- Gaps then run 42, 32, 24, 18, 13, 10, with a floor of 7.
- Rows at y 327, 415, 495, 569 and 638, each 56 high and one value step (4 L) off the ground, with no outline. Inside: a 56 × 56 date square at the leading end, the payee (truncated, never the amount), the amount right-aligned and tabular. An incoming amount sits on an inner face one step lighter, 98px wide, with a plus sign.
- y 732–788, the action bar: full width (390), the darkest value, split 50:50 into Send and Receive. Row six (y 704–760) passes beneath it. Five rows are clear above the bar.
- Budgets: hue 884px² = 0.27% of the screen, on one unit only; dark bar 6.6%; ground and units about 90%.
- Motion caption: a new row enters at the top and every unit slides one slot down the single axis, 90ms apart. A count changes cell by cell, 100ms each, one pass. Press changes a unit's face by one value step.

**Tests**
- *Hinge.* Without Hoffmann the warning is told by colour alone (a guardrail break) and gives no sense of how close. Without Rietveld there is no rule for where colour goes; the default left is a coloured face on every unit. Without Judd it becomes a symmetric set of outlined boxes with a taller hero: the median, drawn in line.
- *Thesis.* Passes; "settled" and "still open" tie it to money in a month.
- *Case-fit.* P1 solved (Rietveld, Hoffmann; Judd keeps it from being an alarm) · P2 solved, by the tension · P3 solved (no envelope ever rescales) · P4 **worsened in capacity**: five rows above the bar where a plain list shows seven; in and out are told by the inner face and the sign · P5 solved (the interval is recency) · P6 solved.
- *Name.* The cluster is one Hoffmann signature trait, carried alone, on 0.3% of the screen. One watch-point: the hue must never sit on the ends of the dark bar, because a dark rail with a bright cut end is a Rietveld signature. A stack of neutral text rows does not read as a wall piece.
- *Patch.* A crop of settled rows still shows the interval rule, the square end, and neutrality as the mark of "settled".
- *Handles.* `.S` a run whose gaps close into the past · `.C` the hue marks only the end of what is still open · `.B` limits are counted in cells.

---

### T02 "Close Ranks": Wim Crouwel × Charles Rennie Mackintosh × Frei Otto  (the hard one)

Two members fail this case as structure, and the third has its best-known step forbidden by a guardrail. The patchwork answer is obvious and wrong: a cell grid for the list, an ornamented head for the balance, a tensioned curve for the warning card. That is three artists in three parts. The procedure gives something else.

**Profile, in the case's nouns**

| | Unit | Exception | Change | Mechanism | Fails here |
|---|---|---|---|---|---|
| Crouwel | one square cell, drawn quietly, everything in whole cells from the top-left; one hard split, 50:50 to 90:10; all text at one size | one hue on a whole region or on the whole display figure; the display built from cells | the grid never moves; content changes in place, in whole cells | a visible measure makes size and emptiness countable | a cell-built balance is a stylised money figure (guardrail); a saturated region spends the colour on the wrong thing |
| Mackintosh | long plain members in strict repeat | every mark on one line, at the head of each member; all irregularity in one narrow bay (about 1/8), off the axis, which holds the way in; notes under 5% | only the node responds, the members hold still | alignment joins the marks into a band; oddness finds the one bay | the phone is a single tall bay; a transaction table is wide content |
| Otto | 3–7 anchors that may not move; everything else is free and placed by relaxing one net of constant mesh | one opening at the highest anchor, the lightest point | every change is shared across the field, and travel decays with distance | small moves keep each neighbour, so the map of the screen survives | rows must align to be compared; the layout may not differ per data set (P3) |

**Bridge.** Shared mechanism between Crouwel and Otto: a mesh of constant size is the scale reference, so change shows as displacement and never as resizing. Shared between Crouwel and Mackintosh: a frozen repeat with the whole difference in one place. And one **tension**, Mackintosh against Otto: "only the node responds" against "every change is shared". It is split by role using Otto's own first step: **anchored** things (the key figure, the edge, the actions) never move and answer only at their node; **free** things (the records) are placed by relaxation.

**Cast**

| | Skeleton | Charge | Behaviour |
|---|---|---|---|
| Crouwel | 2 | 1 | 1 |
| Mackintosh | 1 (only if turned on its side) | 2 | 1 |
| Otto | 0 (rows must align; layout identical for all data) | 1 | 2 |

Best: **Crouwel Skeleton · Mackintosh Charge · Otto Behaviour** = 6. Runner-up: Mackintosh Skeleton · Crouwel Charge · Otto Behaviour = 4.
Layer owners: structure Crouwel · colour Mackintosh · type Crouwel · motion Otto · interaction Mackintosh.

Why no re-draw: Otto's *Fails when* matches twice, but only as Skeleton. As Behaviour his process is a direct answer to P3. A failure in one role is a casting constraint.

**Device, stated: time split, plus a narrow-format re-solve.** Otto rules only what happens when the data changes; the resting layout is not his. Mackintosh's tall bays are turned through 90° for the phone: the long plain members are the rows, the "one height" becomes one vertical line, the narrow bay stays vertical. The invariants (strict repeat, marks joined by alignment, one odd bay) do not depend on the axis.

**Run on the content**
- *Skeleton.* A 13px cell, 30 across, drawn as hairlines 2 L off the ground. Everything sits in whole cells from the top-left.
- *Charge on the crux.* Everything that needs you or lets you act is on one edge. Each row ends at that edge with a one-cell mark. The warning is the same mark, larger and in the hue.
- *Behaviour on state.* When the warning arrives it is not inserted with a push. The anchors hold, and the nearest free rows give up their gaps: the closer to the load, the tighter. The measure makes the squeeze countable.

**Collisions**
1. Crouwel's one split (50:50 to 90:10) vs Mackintosh's narrow bay (about 1/8) → **parameter**: the one split *is* the bay, 25:5 cells (83:17), inside both ranges.
2. Crouwel's two regions of opposite value vs Mackintosh's one register → the colour owner wins: one light register. The bay is the second neutral, 10 L below the ground, with a hard edge on a cell line.
3. Crouwel's saturated region vs Mackintosh's notes at nodes → the colour owner wins; the region hue is **dropped** (the Rail example cut it for the same reason).
4. Crouwel's cell-built display → **dropped** (guardrail on money figures). Parameter kept: the figure is set plainly and stands exactly 4 cells high.
5. Otto's continuous solver vs whole cells → **parameter**: slack is given up in whole cells, and every end state lies on the grid.
6. Crouwel's "changes in place, in whole-cell steps" vs Otto's damped travel → the motion owner wins: 400ms, critically damped, no overshoot.
7. Otto's sag, sheared mesh and peaked anchors → **dropped**: they need a continuous surface, and the structure owner's cells do not shear. His "mesh never rescales" and "hairlines at 6–10% contrast" agree with Crouwel's grid and set its contrast.
8. Otto's "a pressed anchor rises and the field follows" vs Mackintosh's "only the node responds" → the interaction owner wins: press changes the node's shape and fill.
9. Otto's opening → **parameter**: the key figure's block is the lightest value on the screen.

**Thesis.** The month's records lie on one fixed measure with a single edge where everything that needs you or lets you act is found; when spending presses on a limit the nearest records close ranks, and the rest of the field does not move.

**Specimen (390 × 844; cell 13px; 30 × 64 cells)**
- The one split: a vertical hard edge at x = 325. Main region 25 cells; bay 5 cells (65px, 16.7%), full height, second neutral.
- Rows 5–10: label "Balance", then €2,481.36 at 52px on a 4-cell block, the lightest value (ground + 4 L). All other text is 13px (1:4); rank comes from weight and position.
- Resting state (no warning): transaction rows 4 cells high (52px), 2-cell gaps, starting at cell-row 14.
- Crux state, as drawn: the budget row takes cell-rows 14–17 (y 182–234). Its node is a 2 × 2 cell square (26 × 26) in the hue, set across the edge, half in the bay. The rows below sit at y 234, 286, 351, 416, 494, 572, 650 and 728. The gaps read **0, 0, 1, 1, 2, 2, 2, 2** cells. The first three rows have moved 52, 26 and 13px; from the fourth row down nothing has moved. All eight transactions are visible.
- The line: every row ends in a one-cell ink square at the edge. An outgoing row's square is on the list side (x 312–325); an incoming row's has crossed into the bay (x 325–338) and its amount has a plus sign and a weight step.
- The bay holds the way in: Send at y 650–715 and Receive at y 728–793, each 65 × 65, labels at 13px semibold. The bay mirrors for left-handed use and for right-to-left scripts.
- Budgets: hue 676px² = 0.21%; bay 16.7%; row-end squares 0.4%; light ground about 80%.
- Motion caption: the warning arrives, the anchors hold, three rows travel 4, 2 and 1 cells in 400ms without overshoot. With reduced motion: a cut and a short cross-fade.

**Tests**
- *Hinge.* Without Crouwel there is no measure: the squeeze cannot be read and the split has no cell line to sit on. Without Mackintosh there is no rule for where signals and actions live, and no reason for the split to be at 83:17. Without Otto the warning either owns a slot that is empty most of the month or shoves the whole list down, and nothing separates what may move from what may not. All three hold, and Otto's part is visible in a still image as the gradient of gaps.
- *Thesis.* Passes.
- *Case-fit.* P1 solved (all three: the node on the line, the squeeze, the measure that makes it countable) · P2 solved · P3 **solved with a stated cost**: three rows move, by at most 4 cells; nothing below y 416 ever moves · P4 solved (eight rows; in and out by the side of the line) · P5 **untouched**: nothing shows where you are in the month · P6 solved for one hand, with a risk: a side bay is unfamiliar and needs the mirror setting.
- *Name.* No built letters, no colour field, no curve, no ornament. Residual risk: it can read as a generic Swiss grid if the hairlines are drawn above 2 L.
- *Patch.* Any crop of rows holds the grid, a mark on the line and a gap state.
- *Flag on the card.* `FUSED BY DEVICE: time split`. Otto's steps 4–7 are not carried.
- *Handles.* `.S` a fixed measure with one off-axis edge · `.C` everything that needs you is a mark on that edge · `.B` a change is absorbed by the nearest free rows, never by the anchors.

**Difference, T01 against T02.** T01: a receding run · the hue on the end of what is open, with a count · jump for the key figure against equality for the rest. T02: a measured field with one edge · a mark crossing a line, with a squeeze · anchored against free. They differ in all three. A mix such as `T01.S + T02.C` would have to be re-fused: the run has no edge for T02's marks to sit on, so the person would get either marks on the leading ends (which is T01.C again) or a conflict to decide.
