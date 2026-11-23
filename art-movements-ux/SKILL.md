---
name: "art-movements-ux"
description: "Use when designing any UI/UX screen, app, site or design system and the user wants non-generic, art-informed design: build one mood board from artworks chosen for the product's real design problems (55 artists, 11 movements, checked against the actual works), distil it into a locked brand book / UI kit, then generate every screen from that kit only. For explorations, draw ten random triads of artists, fuse each into one board, and let the person pick or mix. One coherent new system, not a pastiche and not a patchwork."
---

# Art Movements UX: one mood board, one kit, every screen

Left alone, a model designing UI reverts to the statistical median of its training data: Material/Apple-style rounded cards, soft shadows, centered heroes. This skill replaces that default with a studio method in four design stages, plus guardrails and reporting: **(1) read the brief for the product's design problems, (2) assemble a mood board of artworks that solved those problems, (3) distil the board into a brand book and UI kit and lock it, (4) build every screen and component from the kit alone.**

The library (`references/library.md`) holds 55 artists as processes, measured relations and the reasons they work. It is a body of solved problems, not a wardrobe: you take an artist's process, never their look, and you open it in Stages 2 and 3 only.

Two failures are equally bad. **Pastiche:** a product that can be captioned "the Mondrian one". **Patchwork:** a product whose parts answer to different artists. Do not pick a different artist for a different screen, section or component, however well it would suit that part. Once the kit is approved the style does not change in one place because a new artist resonated there.

---

## 0. The Median Detector (purge before you begin)

Most of the library's artists reject these patterns. None may appear in a kit or a screen unless a Stage 3 kit rule adopts it with a reason from the case:

- Rounded cards (12–16px radius) floating on soft grey drop shadows, plus elevation z-levels
- Centered hero: headline, subhead, two buttons, then a symmetric three-up feature row
- Pure `#FFFFFF` ground with neutral greys and a single "brand blue" accent
- A smooth 1.2–1.25 modular type scale in one sans (Inter/system) with three weights
- Glassmorphism, gradient blobs, decorative stock illustration and mascots
- An even 8pt grid with identical gutters and identical tile sizes
- One `300ms ease-in-out` (or bouncy spring) on every element; fade-and-slide-up-20px entrances
- Color used as decoration, not to carry a meaning

If a draft could be mistaken for a Dribbble template, it has failed: go back to the board's principles, not to an artist's look.

**The library's own median.** The entries share habits that become a house style if you pool them: warm cream paper (`#F4F1EA` and cousins), one vermilion accent, the same few fonts (Archivo, Jost, Space Mono, Inter, Josefin Sans), a label rotated 90°, `steps()` motion, radius 0. None of these may enter a kit by default. Each needs a reason from this case.

---

## 1. Workflow

**Before anything: is there already a kit?** If the project has a kit from this skill (a `kit.css`, a brand book page, a kit version in the conversation) or the user's own design system, do not start a new board. Go to Stage 4, or to "Changing the kit" if the request cannot be met from it. A single-screen request with no kit still runs all four stages on the **light path**, so the next screen has something to obey:
- Stage 1: 3–4 problems, no inventory beyond the 2–3 likely next screens.
- Stage 2: 4–6 plates; open at most 8 reference files in total (start from §P in `references/principles.md`, then the one-line index at the top of `references/library.md`, then only the entries and files you will cite).
- Stage 3: a compact kit = a token table (colour roles with budgets, type, space, motion), the components this screen needs, 5 Do/Don't pairs, the provenance table. Specimen = this screen plus one likely next screen. Name, swap and three-medians tests only.
- Stage 4: the screen, with citations and the token lint.
Use the full path when the user asks for a product, a design system or several screens.

### The ladder (used in Stages 2 and 3)
Every move in the library can be read at four rungs.

| Rung | Example (Barragán, Casa Gilardi) | Transfers? |
|---|---|---|
| **Surface** | magenta `#E74889` plane before a cyan wall | Only in the cases listed below |
| **Device** | the most saturated plane is the smallest (5–10%) and stands free in front of a larger, cooler one | As a hint, rebuilt in the case's material |
| **Principle** | saturation and area trade off; the eye goes to the small intense thing only if the big thing is calm | **Yes. This is what you carry.** |
| **Problem** | make one place in a quiet room feel like the destination | This is how you *find* the move |

Carry the principle. Take surface from the case: brand colours, platform type, the content's own shapes. Keep the artist's *numbers* (area shares, ratios, value steps) as calibration, because they describe perception, not style.

**When surface may travel.** (a) The user asks for a homage or a named manner; then the whole kit is that manner, everywhere. (b) Stage 2 single-artist studies (never triad boards, which carry processes only). (c) The brand already lives there (a museum, a furniture maker). (d) A single surface detail with no signature of its own (a 4 L value step, a hairline). Never two bundled surface traits from one artist (their geometry *and* their palette) outside (a)–(c).

### From observation to process (how to read a work or an entry)

A measurement says what is on the surface. A kit needs what the artist did: decisions, in order,
with reasons (the Principle rung, made executable). Convert an entry before it enters a kit.

**1. Turn every value into a relation.** Ask of each observation: compared to what?
- Colour: its role (ground, mass, counterweight, signal, light); share of the area; rank in
  saturation; value step to each neighbour; warmer or cooler than its neighbour; form (point,
  band, field or light).
- Size and position: fraction of the format; ratio to the neighbour; distance from the centre
  and from the edge.
- Line: thickness as a fraction of the short side; how many weights exist; what a line does when
  it meets another line or the frame.
Once the relation is written, delete the hex, the hue name, the material and the motif.

**2. Separate the invariant from the instance.** Compare the works. What holds in all of them is
a rule. What moves between them is a parameter, and its spread is the range. What appears in one
work is a mode or a signature. In CHANGELOG.md, every "corrected", "contradicted", "softened" or
"not universal" marks a rule that was really one instance; the wording that survived is the
invariant ("exactly one saturated plane" died, "the most saturated plane is the smallest" lived).

**3. Break it to find the reason.** For each invariant, run five counterfactuals: centre it,
enlarge it, equalise it, multiply it, remove it. Say what the eye would do differently, and name
the mechanism: visual weight and leverage; figure and ground; simultaneous contrast; adaptation
to the previous state; grouping by likeness or texture; depth from overlap, temperature or value;
salience by oddness; fusion of fine detail into tone; scale reference. If no counterfactual
breaks anything, the observation is surface: discard it. If you cannot name a mechanism, do not
promote it to a step.

**4. Recover the order.** Ask of each decision: what had to be fixed before this could be
chosen? Sort by dependency, usually: format and enclosure, the largest thing, the division,
where intensity goes, detail and texture, time. Step 1 is the decision that, if changed, forces
every other to be redone. Write each step as an imperative with a parameter, a range, and a
constraint tying it to an earlier step ("the smallest", "opposite the dominant", "one value only").

**5. Derive what the artist never made.** Type, motion and interaction come from the process,
not from the look. Ask: what is the repeated unit, and what texture must text have to be one?
What changes when the viewer or the light moves? What would the artist adjust if the content
changed? Illustrating the surface (a shimmer because the painting is gold) derives nothing.

**6. Test, in this order.**
- *Blind test.* Every step must be executable by someone who has never seen the work. Remove
  every noun that belongs to the artist.
- *Substitution test.* Rotate the hue, invert light and dark, swap the content. Each step must
  still force a decision. A step that only works in the original palette is surface.
- *Transfer test.* Apply the procedure, with numbers, to a product that shares nothing with the
  artist's surface. If a viewer would caption the result with the artist's name, find the step
  that carried the signature and abstract it once more.
- *Distinctness test.* If the procedure has shrunk to "generous space and one accent", it is too
  abstract: restore the constraint that separates it from the neighbouring artist. Two artists'
  procedures run on one brief must give structurally different layouts.
- *Failure test.* Name the content or format on which the procedure stops working. A procedure
  with no failure case has not been understood.

**7. Keep and discard.**
- Keep: roles, area shares, ratios, value steps, ranks ("most saturated is smallest"), order of
  decisions, constraints, failure cases. Numbers that are ratios describe perception and travel.
- Discard from the procedure: hexes, hue names, materials, motifs, subject matter, font names,
  format quirks, CSS. List the 2–3 traits that make the artist recognisable under "Signature" and
  never carry them together.

### Stage 1: Brief
Write these before any form. They are held constant through everything that follows.
1. **Case.** Who uses the product, how often, in what posture and place. Brand givens (colours, type, tone, existing assets) or "none"; givens are binding. Platform conventions that must hold. Accessibility needs.
2. **Inventory.** Every screen or flow that exists or is planned, and every component they need (navigation, lists, forms, alerts, empty, loading, error, charts). If only one screen was asked for, list the two or three screens most likely to follow. The kit will be tested against the inventory, not against one screen.
3. **Content truth.** One sentence on the shape the product's content has of its own accord ("money moving through a month", "twelve equal things", "one long text"). The kit's structure will come from this sentence.
4. **Problems.** The **4–7 design problems that recur across the product**, each phrased as a tension, not a topic: not "hierarchy" but "one figure must win the glance without shouting, in a money app". Use the vocabulary of §P. Note which screens each appears on. Rank them and mark the **crux**. A problem that lives on one screen only is not a kit problem; it will be solved later with the kit's means.

Show the problem list to the user if they are present. It is the cheapest point to steer.

### Stage 2: Mood board
One board for the whole product: **5–9 plates.**

1. **Scout by problem.** For each problem pull 2–4 candidate processes from at least two movements using §P (`references/principles.md`), read the one-line index at the top of `references/library.md`, then only the candidates' entries (search for the artist's bold name), and open a reference file only for a candidate you may put on the board (full path: at most ~15 files; light path: 8). For each candidate write one line per rung: device → principle → why it worked in that work → what differs here. Drop candidates whose principle depends on something the case lacks (Hara's emptiness needs little content; Carson's noise needs no task).
2. **Prefer** *convergence* (a principle held by artists from unrelated movements is robust and unsigned), *economy* (one principle that answers two problems), and *reach* (a principle that can show up on most of the inventory, not on one screen).
3. **Compose the board.** Each plate is one specific work, or one measured aspect of it:

   ```
   PLATE n: <Artist, Work, year>
   Answers: <problem from Stage 1>
   Principle: <one sentence, no style words>
   Take: <what enters the kit, incl. the measured figure used as calibration>
   Leave: <the surface that stays behind>
   Why this case: <users, content, brand, platform>
   Layer: structure | colour | type | motion | interaction
   ```

   Add 1–3 **case plates** that are not art: the brand's givens, a sample of the real content at its worst (longest name, largest number, emptiest state), the context of use. They sit on the board as equals and win any conflict.
4. **Make the board cohere before leaving it.**
   - **One thesis.** One sentence that the whole board supports, naming no artist and no style. It must contain the content truth. If it would fit a different product unchanged, it is a template: go back.
   - **One owner per layer.** Structure, colour, type, motion and interaction each get one governing principle. Other plates on that layer must fit inside it or leave the board. A second logic on a layer is allowed only for a different role: colour for surfaces vs state signals, motion for the user's actions vs the system's news.
   - **Bundle limit.** No artist owns more than two layers, and never both structure and colour. The crux has at least two sources.
   - **One tension, by role.** Keep at most one pair of opposed principles (§P.3) and give each pole a territory defined by the role of an element (the system's news vs the user's actions; the one key figure vs everything else). Never a territory defined by screen or section.
   - **Cut.** A plate that answers no problem, or that only one screen could use, goes, however beautiful.
5. **Single-artist studies (optional).** When the user asks "what would artist X do here", build 3–5 quick strict single-artist studies. When they ask for an *exploration* or *options*, use **Exploration mode** (below) instead of one representative screen, chosen from the scouted candidates plus one foil from the opposite corner of §3. Commit fully, label them *studies*, then harvest 2–3 findings and one failure from each, stated as principles with evidence on this content. Findings become plates or sharpen them. Studies are never parts of the product and their pieces are never spliced into it. If the user falls for a study, ask what it does for them and carry that; ship a manner itself only as a deliberate homage, for the whole product.
6. **Show the board.** If you can fetch images (the Sources in each reference file list them), show the works; otherwise show the plate cards and mark any figure you did not see yourself as *text-derived*. Get the user's steer: add, drop, reweight. When several directions are wanted, offer **2–3 boards that differ in thesis or in the tension kept**, not in costume, and let the user pick one.

### Exploration mode: ten fused triads (inside Stage 2)

Use it when the person asks for a design exploration, for options, or nobody has a view yet and there is no kit. It replaces Stage 2's single-artist studies for that run and runs before step 6. Stage 1 comes first and is never skipped: the ranked problems, the crux and the content truth are the only yardstick for every decision below. Before drawing, also fix the **specimen constants**: the crux screen, its real content (worst cases included), the viewport, and the *case hues* (the brand's, or case-derived and marked *unconfirmed*). Fix nothing else: type, the ground's lightness and temperature, value distribution, line and density belong to each board, because a board that cannot choose them can only differ in layout. State the content truth as what the content does, not as a shape ("money comes in, goes out, and some of it is already promised", not "the month is a line"), so it does not pre-decide the structure for all ten. Ladder exception (b) does not apply here: a triad board carries processes, never a member's surface.

**1. Draw.** Run `python3 scripts/triads.py` (it prints its seed; `--seed N` reproduces a draw). Log the seed and the level. `--level artists` (default) gives the sharpest fusions. `--level movements` when the person said "schools": per slot, take the artist of that school whose index line answers the highest-ranked problem that no other member answers, and log the choice. `--level mixed` gives both. `--exclude` only an artist whose *Fails when* matches the content truth in every role; log it. Never hand-pick a member, never swap one you find awkward, never run several seeds and keep the nicest draw. A new round is a new seed.
**Re-draw one member** only when its *Fails when* matches the case in **all three roles** of 2c. A failure in one role is a casting constraint, not a reason. At most once per triad. Do it mechanically: `python3 scripts/triads.py --seed <seed> --redraw "Tnn:<member>"` (it keeps the rest of the draw and the caps, and prints the replacement). Log it: `T04: X → Y, because <Fails-when clause> = <case fact>`.

**2. Fuse.** Work from the three library entries only (no reference files yet), in this order.
a. **Profile.** Fill one row per member from its entry: *Unit* (what repeats and how the field is divided) · *Exception* (where the one difference or the intensity goes, and how much) · *Change* (what moves or responds, what holds still) · *Mechanism* (from "Why it works") · *Fails here* (its failure cases checked against this case). Write every cell in the case's nouns (row, balance, warning), not the artist's (bay, slab, mast). A step that cannot be rewritten that way is surface: drop it.
b. **Bridge.** Read the 3×3 down its columns and across the failures. Look, in this order, for: a **lock and key** (one member's *Fails here* is another member's step; the strongest bridge, because each needs the other); a **shared mechanism** (two or three members rely on the same perceptual mechanism; it becomes the spine, and those members must then act on different layers, or they are one member twice); a **tension** (two members give opposite answers in one column). Keep at most one tension and split it by the *role* of an element (anchored or free, settled or open, the key figure or the rest, the system's news or the user's acts), never by screen, section or component. Write the bridge as one sentence.
c. **Cast.** Three roles, one member each. **Skeleton** owns structure: the division of the field. **Charge** owns colour: where the one difference goes and its budget. **Behaviour** owns motion and interaction: what happens when the data or the hand changes something. Score each member in each role: 2 = its strongest step lives here and fits the content truth; 1 = it has a usable step here; 0 = its *Fails here* applies in this role, or it is silent. Of the six assignments take the highest total that contains no 0; break a tie by the one that solves the crux with two members. Note the runner-up. Type and line go to the member whose type requirement the content meets, or to the case. No member holds more than two layers, and none holds both structure and colour.
d. **Run** each cast process on the content, in dependency order: the Skeleton's own process first, deciding how the field is divided (the content-shape mapping of Stage 3 is a constraint the result must satisfy, not the structure itself: a time sequence can be told by an axis, a stack of states, cells, a vessel, a promenade or a single opening), then the Charge on the crux, then the Behaviour on the state changes in the inventory (arrives, runs out, empty, error, press). Keep the entry's ratios and ranks as calibration. Take hues, type family and shapes from the case.
e. **Resolve collisions.** List every step of a member that lies outside its own layers. If it fits inside the owner's range, it becomes a **parameter** of the owner's rule (the owner's one split is placed where the other member's ratio says). If it contradicts the owner, it is **dropped, with a one-line note**. If it is the bridge's tension, it gets its role territory. A non-owner's colour step survives only for a different role (surface values, not signals). Two members do not outvote an owner. Guardrails and case plates beat all three.
f. **Count what is left.** Every member must keep at least one step that only it has. If one is left with none, take the runner-up casting. If no casting works, the triad does not fuse plainly: use ONE device, and name it on the card. **Scale split:** format, unit and mark get one member each, on every screen. **Time split:** one member rules the resting state, another only what happens on change. **Constraint:** the member survives as one prohibition taken from its counterfactuals. If a member still carries nothing, show the board anyway, labelled `DUO + idle: <member>`, last on the page. Do not replace the triad: an awkward draw is where the non-median idea usually sits, and a substitute you choose brings your own defaults back. The label keeps the page honest.
g. **Thesis and name.** One sentence that contains the content truth and no artist or style word. Name the idea, not the sources.

**3. Test.** Hinge, thesis and case-fit on paper before the specimen; name and patch on the specimen; difference across the ten.
- **Hinge.** Delete each member in turn and write what the design loses, in one clause. "A flourish" or "nothing" means a duo with decoration: recast (2c) or flag (2f).
- **Thesis.** One sentence, no names, and it would not fit another product unchanged.
- **Case-fit.** Mark every Stage 1 problem *solved*, *untouched* or *worsened*, with the members responsible. The crux is solved and has two sources. A *worsened* is printed on the card, never hidden.
- **Name.** Not captionable as any one member, or as one movement, within five seconds. No member carries two of its Signature traits.
- **Patch.** Any 200px crop of the specimen shows at least two members' rules at work. A region that answers to one member is patchwork.
- **Difference.** Line up the ten theses with their (structure idea · signal logic · tension). Two boards alike in two of the three differ only in costume: recast the later one with its runner-up casting, or with the same casting and a different structure taken from its Skeleton member's process. No structural idea (e.g. "a time axis with a today line") may carry more than two of the ten.
- **Median.** Check each specimen against §0 (rounded cards, pill buttons, shadows, one brand-blue accent): none may appear unless the board's rules adopt it with a reason.

**4. The early design.** Per triad: one TRIAD BOARD card (§5) and one specimen of the crux screen. The specimen is one static HTML file at the fixed viewport, at most 150 lines, with no script, images or icons, type chosen by the board from its own type requirement (system stacks such as `ui-serif`, `ui-monospace`, `ui-rounded`, condensed or wide system faces, or one web font if the session can load it), its own ground and value logic (neutrals of any lightness and temperature, chroma ≤ 6) plus the case hues, and at most 12 custom properties. It must show the division of the field, the key figure, at least five repeated units (with fewer, rhythm cannot be judged), the crux in its hard state, the primary action, and one caption line for what moves. It must still read at 240px wide: squint, and structure and signal placement survive. If nothing can be rendered, the smallest acceptable form is a zone list in px with value steps and the one hue. Run the Stage 5 guardrails on it. Polish nothing else.
**In parallel.** Draw and re-draw yourself. Then brief one subagent per triad with: the Stage 1 brief verbatim; the specimen constants; its three library entries pasted in; this section and the card template; the Stage 5 guardrails; the output paths `explore/Tnn/card.md` and `explore/Tnn/specimen.html`; and a return of at most 100 words (name, thesis, cast, flags). A subagent sees no other triad, re-draws nothing and opens no reference file. Run *Difference* yourself afterwards and send back only the boards that must be recast. **Without subagents:** write all ten cards as far as 2g and run *Difference* on paper. Then build the specimens from one shared content skeleton, each from its own card, without looking at the previous one.

**5. Compare and pick.** Build one page, `explore/index.html`. At the top: the problems with the crux, the seed, the level and the re-draw log. Then ten equal tiles in draw order, flagged boards last: number, name, triad, thesis, the three castings, the tension, the case-fit row, flags, and the specimen at one scale. Each tile offers three handles: `.S` structure, `.C` signal logic, `.B` behaviour. Do not rank the boards for the person; say which ones pass every test.
The person answers with a board (`T03`), a mix by layer (`T03.S + T07.C`), or a feeling ("the calm of T05"). For a feeling, ask what it does for them and carry that as a principle. A pick by region ("T03's header and T07's list") is translated into layers before anything is built.
A mix becomes ONE board. The board that gives `.S` is the host, and every layer not named comes from it. Run 2e to 2g and all of step 3 on the mix as if its donors were one triad: one owner per layer, the bundle limit, one tension, a new thesis. If the thesis needs "and" to hold two ideas, go back to the person with the conflict. Render one new specimen of the same crux screen and get it approved. Only then open the reference files of the surviving members, write them as PLATEs with the case plates, scout more plates only for problems still *untouched*, pass step 4 above, and go to Stage 3.
The unpicked boards go into `explore/log.md` (seed, triads, theses, the reason if one was given) and are closed. They are never applied to a screen, a section or a component later; an idea from them that comes back follows L5. With nobody present, take the board with the best case-fit and the crux solved, mark it *assumed, unconfirmed*, and continue.

Worked fusions (one plain, one hard): `references/EXPLORATION-EXAMPLE.md`.

### Stage 3: Kit (brand book and UI kit)
Distil the board into a system that names no artist. Build it as real files in one folder the user can find (default: `design/kit/` in the project, or the session's artifact if there is no project): `kit.css` (tokens and component classes), `brand-book.html` (rules with IDs, specimens, provenance) and one HTML file per screen. Every rule gets an ID so screens can cite it.

1. **Thesis and 3–5 principles**, in the product's own words.
2. **Structure.** The grid or axis logic, the module, the screen archetypes (overview, list, form or flow, detail, confirmation, empty, error) each as a fixed arrangement of zones.
   - **From content shape to structure.** Derive the structural idea from the content truth, then let a board process shape it: a *sequence in time* (money through a month, a habit streak) → one axis or rail with past and future on either side; *peers* (twelve equal things) → a field of equal units, no hero; a *hierarchy* → nesting or terraces; a *flow* → a promenade of rooms; a *quantity against a limit* → a fixed vessel with a level; *live change* → fixed slots or anchors with everything else relaxing. Write the mapping in one line and keep it in the brand book.
   - **Re-solve for narrow formats.** Many processes are stated for a wide field (periphery, frame edges, side-by-side panels). On a phone keep the process's invariant (the rank, the ratio, the counterweight, the sequence) and change the division: periphery becomes the top and bottom edges, side-by-side becomes a vertical sequence read by scrolling, a frame-edge counterweight goes to the edge nearest the thumb. Test the specimen at 390 px wide; if an entry's *Fails when* names narrow formats, say how the kit re-solves it.
3. **Colour.** Tokens by *role*, each with an **area budget** per screen. Defaults from §P.2, change them only with a reason: quiet grounds ≥ 60% (≥ 75% for calm, frequent-use products); structure/ink ≤ 20%; a point signal ≤ 1%, a main accent ≤ 8%, all saturated colour ≤ 13%; at most one saturated element per screen unless a rule says otherwise. Adjacent surfaces 3–5 L apart. A signal set of **2–3 states** (e.g. attention and fault), each with a non-colour partner (shape, position, label); other states are told apart by form or position, not by more hues. **Hues come from the brand or the case, never from the plates.** With no brand, derive two candidates from the case (the domain's conventions, the context of use, what must stay calm vs. what must be noticed), state why, pick one, and mark it *case-derived, unconfirmed*.
4. **Type.** One logic: a hard jump (two sizes, ≥1:6 on desktop, ≥1:4 on a phone; recalibrated from the poster scale of the sources) *or* hierarchy by isolation and position, never both. Write the type *requirement* first (e.g. tabular figures, a width axis, a wide weight range, one family) and then choose a family that meets it; the library-median families of §0 need a stated reason. Every size and weight is a token.
5. **Line, shape, texture.** Line weights (two, far apart), corner rule, any texture, with reasons.
6. **Motion grammar.** One material (mechanism, light, weight), duration and easing tokens, what may move and what never does.
7. **Interaction grammar.** What press, focus, select, drag and disabled look like, once, for every component.
8. **Components.** Every item in the inventory, each defined by kit tokens only, with its states.
9. **Voice.** How the product speaks: tense, length, how numbers and dates are written, what it never says.
10. **The exception.** The one rule-break the system allows, defined as a class of element and limited to one per screen. And the one unfamiliar interaction in the whole product, if any; everything else follows platform convention.
11. **Do / Don't.** Six to ten pairs, the Don'ts drawn from §0, from the library median and from the sources' own surfaces ("no primaries with black rules").
12. **Provenance appendix.** A table, kept at the back: `Kit rule | Problem | Principle | Plate(s) | Left behind`. This is the only place artists are named.

**Prove it before freezing.** Render a specimen sheet: three contrasting screens from the inventory (the densest, the emptiest, one form or flow) built from the kit alone. If any of them needs a value or component the kit lacks, the kit is not finished. Then run the kit checks:
- **Name test.** Could a design-literate viewer name one source artist or movement from the specimen within five seconds? If yes, find the bundled surface traits that cause it and abstract one further.
- **Caption test.** Delete the provenance appendix. Every rule must still have a reason in terms of the user and the content.
- **Swap test.** Swap the hues for another brand's and the typeface for another family. If the system survives, it is made of principles. If it collapses, it was a look.
- **Elsewhere test.** Would this kit suit an unrelated product with the labels changed? If yes, the structure is not from the content truth.
- **Three medians.** Mechanically: grep the kit for §0 patterns (`border-radius` 12–16px, `box-shadow`, `#FFF`/`#FFFFFF`, a single `300ms ease`, a 1.2–1.25 type scale) and for the library-median fonts and cream papers. Then by eye against each plate. It should sit near none.
- **Reach test.** Every principle appears on at least two of the three specimen screens.

Show the brand book and specimen. On approval the kit is **frozen as v1.0**. If nobody is there to approve (an autonomous run), freeze it as **v1.0 (assumed)**, list the assumptions at the top of the brand book, and continue.

### Stage 4: Screens, from the kit only
For each screen or component:
1. Write its skeleton: goal, content, actions, states. Real copy, real numbers.
2. Pick its archetype from the kit. Compose it from kit components. Import `kit.css`; write no raw hex, size, duration or easing in the screen.
3. Solve the screen's local problems with the kit's means. Do not open the library or the reference files. Do not consult the mood board for a new idea.
4. Write a short rationale that cites kit rule IDs. No artist names appear at screen level.
5. Run the coherence checks, then the guardrails.

**Lock rules.**
- **L1. Frozen.** After approval the kit changes only through "Changing the kit" below.
- **L2. No artists downstream.** The library, references and §P are closed in Stage 4. A screen is traced to kit rules, and through them to the kit's own plates, never to any other source.
- **L3. No one-offs.** A value that is not a token is a bug. A component variant that exists on one screen must be a kit component that other screens could use, or it does not exist.
- **L4. Same thing, same form.** One meaning has one form across the product (a forecast always looks like a forecast). One form has one meaning.
- **L5. Resonance is parked.** If a new artist or idea seems perfect for one screen, write it in a parking list with the screen that prompted it. Do not apply it. It is reviewed at the next kit version, for the whole product.
- **L6. The user can override, the model cannot.** If the user asks for a local deviation, say what it breaks, offer the kit-level alternative, and if they still want it record it in the kit as a named exception.

**Changing the kit.** When a screen cannot be built from the kit:
1. Try again with existing tokens and components. Most gaps are compositions nobody wrote down.
2. If something is truly missing, write a change request: what is missing, which screens in the inventory will use it, the proposed rule in kit terms.
3. Derive the answer from the **existing board** first. Add a new plate only if the board cannot answer, and only if the plate passes Stage 2's coherence rules against the plates already there.
4. Bump the version. *Minor* (v1.1): additions that contradict nothing. *Major* (v2.0): anything that changes the thesis, a layer's owner or a token's meaning; this needs the user's approval.
5. Apply the change to **every** screen already built, list the screens touched, and re-run the checks. A change that is right for one screen and wrong for the others is rejected.

**Coherence checks (every screen).**
- **Token lint.** Every colour, size, space, radius, duration and easing in the screen resolves to a kit token. Check it mechanically: grep the screen for raw hex and px outside `kit.css`.
- **Budget check.** Screenshot the screen (e.g. Playwright, 390×844) and run `python3 scripts/measure_palette.py SCREENSHOT -k 6` from this skill's folder, then assign each cluster to its kit role (ground, ink, signal…) and compare: ground, ink and signal shares and counts against the kit's budgets (signal ≤ y%, one exception, one key figure).
- **Component check.** Every element is a kit component in a documented state.
- **Citation check.** Every decision in the rationale cites a kit rule ID. No artist name appears. No decision traces to a source outside the kit's provenance appendix.
- **Sibling test.** Put the screen beside any other screen of the product: same hand, same structure logic, same signal meaning?
- **Crop test.** A 200px crop from anywhere on the screen should be recognisable as this product.
- **Fit.** The screen's own problems are solved, with the longest real name, the largest real number, zero items and an error.

### Stage 5: Guardrails pass (always; on the kit specimen and on every screen)
- Body text contrast ≥ WCAG AA 4.5:1; meaningful graphics and control boundaries ≥ 3:1. Low-contrast sources (Ando, Agnes Martin, Turrell, Sejima) still have to pass.
- Navigation, forms, data, errors and checkout must stay plainly legible and semantic (Carson's own boundary). Expressive distortion goes only on decorative layers, with real text underneath.
- Respect `prefers-reduced-motion`: every idle or ambient motion (sway, drift, shimmer, growth) has a static state. No flashing more than 3 times a second (WCAG 2.3.1) and no flicker sequences: light comes on with one monotone fade. Ambient change is ≥ 30s per cycle; idle motion runs only where the kit names it.
- Vibrating fields (fine stripes, moiré, high-contrast bands near 3 cycles/degree, 50% duty cycle) are decorative only: no text and no control may sit on them; content sits on flat panels.
- Tap targets ≥ 44px, even where a design compresses the visible row. Rotate only decorative layers, never controls or text you need to read. Any text ≥ 12px. A hidden gesture (press-and-hold, drag) always has a visible or keyboard/assistive-technology equivalent.
- Colour must never be the only signal: pair it with shape, position or a label. A selected state is never only a value step.
- Map tokens, not hexes, to dark mode (keep the value steps, the single signal and the area budgets), and mirror structural axes for right-to-left scripts.
- Conventions with safety weight keep their meaning: red stays for errors and destructive acts where the platform or domain expects it; money, health and legal figures are never animated, cropped or stylised into ambiguity.

### Stage 6: What to show the user, and when to stop
With the user present, stop and ask at three points only: after the problem list (Stage 1), after the board (Stage 2; in Exploration mode, after the comparison page, for the pick), and before freezing the kit (Stage 3). Without a user, record each choice as *assumed, unconfirmed* and continue; never stall waiting.
- **After Stage 1:** the problem list with the crux.
- **After Stage 2:** the board (plates with Answers / Take / Leave / Why), the thesis, the tension kept. Handles: "drop plate 4", "more weight on plate 2", "swap the tension".
- **After Stage 3:** the brand book, the specimen sheet, the provenance appendix. Handles phrased as rules: "tighten the signal budget", "allow a second key figure".
- **After Stage 4:** each screen with its kit citations, the kit version it was built from, and the parking list if it has grown.


**Worked example.** `references/WORKED-EXAMPLE-rail.md` runs all stages on a mobile bank (board → kit → Home → a second screen from the same kit). Its built files are in `references/worked-example/` (`kit.css`, `brand-book.html`, `home.html`, `send.html`).

---

## 2. Cross-cutting principles (where the artists converge)

1. **Scarcity of accent.** Many of the library's artists restrict the saturated color to *one element per screen*, the primary action or the current state. That single constraint does more against genericness than anything else.
2. **Depth without shadows.** Get depth from overlapping flat planes (Rietveld, Popova), value steps (Albers, Sejima, Turrell), translucent multiply (Moholy-Nagy, Kandinsky), scale tiers, emitted glow (Flavin), parallax interference (Soto, Cruz-Diez) or pattern density (Klimt).
3. **Grounds are a chosen tone, never default white.** Pick the ground's lightness, temperature and chroma from the case; adjacent surfaces 3–5 L apart read as separate without borders (§P.2). White is an active plane, not "nothing".
4. **Show the structure.** Make the grid visible as graph paper (Crouwel), tie-hole dots (Ando), scored joints (Wright), struts (Popova) or bronze mullions (Mies). Structure can be the ornament.
5. **Unequal is alive.** Use irregular tracks (`3.2fr 1fr .45fr 1.6fr`), asymmetric margins and off-center masses. Symmetry is allowed only as a deliberate exception (Klimt's Stoclet bookends, Tanaka's near-symmetry with one offset).
6. **Violent or zero hierarchy.** Either jump scale hard (1:6, 8–12× numerals, 60vh glyphs) or remove size hierarchy entirely and rely on space and position. The mushy middle is the median.
7. **Sequence and threshold.** A screen is a place you arrive at: compression then release (Wright), a dim narrow entry then wide light (Barragán), a void band to cross (Ando), a ramp or promenade (Le Corbusier, Wright's Guggenheim).
8. **System over composition.** Design the rule that generates layouts: Gerstner's morphological box, LeWitt's exhaustive permutations, Vasarely's plastic units, Stepanova's single tile, Le Parc's 14-hue ring. Show the rule to the user.
9. **Motion has a material.** Mechanisms step (`steps()`), light fades slowly (600–1400ms), gravity settles, cuts are hard. Motion either follows content (scroll- or pointer-bound) or makes a point. It never runs as idle decoration on a timer, except in deliberate kinetic idle states.
10. **Interaction changes the medium.** On hover or focus, change value, light, width axis, track size, ring position or transparency instead of lifting and scaling.

---

---

## 3. Axes map: choose a foil

Use it in Stage 2 to pick a contrasting exploration and to check that the mood board does not sit in one corner.

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
| Growth & Form | rule-generated order | packed field or one pierced mass | relief, hollow and see-through | grows once, then settles | natural-computational |

---

---

## P. Principle index (in `references/principles.md`)

§P lives in `references/principles.md`: **P.1** the UI problems mapped to the artist processes that solve them (scout here in Stage 2), **P.2** calibration ranges pooled from the measured works (set Stage 3 budgets from it), **P.3** tensions worth keeping (pick at most one per board, split by role). Open it in Stages 1–3. A session that starts at Stage 4 from an existing kit does not need it.

---

## 4. The Library (opened in Stages 2 and 3 only)

The 55 artist entries live in `references/library.md`, outside this file, so that Stage 4 can really be built without them. Each entry is a **process** (ordered steps with parameters that run with any palette, content or medium), the reasons it works, colour stated as relations, a type requirement, when it fails, and its **signature** (the surface traits never to carry together). The full study for each artist is `references/<movement>/<artist>.md`: key works examined (and which were visually checked), process and relations observed in the works, composition, colour, form and type, motion, UI translations for studies, what the artist would reject, and sources. A reference file's colour table is a *reference sample for strict studies and homage only*.

Movement folders: `01-bauhaus`, `02-de-stijl`, `03-constructivism`, `04-swiss`, `05-modernist-arch`, `06-japanese-ma`, `07-art-nouveau-secession`, `08-minimalism`, `09-op-kinetic`, `10-postmodern-newwave`, `11-growth-form`. File stems are the common short surname, lowercase, hyphenated, without diacritics (`mies`, `barragan`, `gaudi`, `huszar`, `muller-brockmann`, `van-der-leck`, `agnes-martin`, `le-corbusier`, `le-parc`, `cruz-diez`, `frei-otto`, `nervous-system`).

---

## 5. Templates (board, kit, screen, study)

```
BOARD: <name describing the idea, no artist names>          for: <product>
Content truth: <one sentence>
Thesis: <one sentence, no artist, no style>
Tension kept: <pole A for role X ↔ pole B for role Y>
Plates: 1 … 2 … (PLATE format from Stage 2) + case plates
Layer owners: structure <plate> · colour <plate> · type <plate> · motion <plate> · interaction <plate>

KIT <name> v<major.minor>
Principles: K1 … K5
Structure S1… · Colour C1… (role, token, budget) · Type T1… · Line/shape F1… · Motion M1… · Interaction I1…
Components: <name: tokens, states>
Voice V1… · Exception X1 · Do/Don't
Provenance: rule | problem | principle | plate(s) | left behind
Checks: name · caption · swap · elsewhere · three medians · reach

SCREEN <name>   built from KIT v<…>
Archetype: <…>   Components: <…>
Decisions: <decision → kit rule IDs>
Coherence: token lint · budgets · components · citations · sibling · crop · fit
Guardrails: <contrast, motion, targets>

TRIAD BOARD Tnn: <name of the idea, no artist>          seed <N> · level <…> · for: <product>
Triad: <A> × <B> × <C>        Re-draw: none | <X → Y, Fails-when clause = case fact>
Profile (case nouns)    Unit | Exception | Change | Mechanism | Fails here
  A: … | … | … | … | …
  B: … | … | … | … | …
  C: … | … | … | … | …
Bridge: <lock and key | shared mechanism | tension>: <one sentence>
Tension kept: <pole for role X ↔ pole for role Y> | none
Cast: Skeleton <member: steps kept> · Charge <member: steps kept> · Behaviour <member: steps kept>
      scores <a+b+c> · runner-up <casting, total>
Layer owners: structure · colour (surfaces / signals) · type · line · motion · interaction   (a member, or "case")
Collisions: <step> → parameter of <owner's rule> | dropped: <why> | role territory        (one line each)
Device (only if forced): scale split | time split | constraint | DUO + idle: <member>
Thesis: <one sentence, the content truth inside, no artist, no style word>
Specimen: <file> · <viewport> · zones with numbers · budgets (ground %, ink %, signal %)
Tests: hinge A / B / C <what is lost> · thesis · case-fit P1…Pn (solved | untouched | worsened, members)
       · name · patch · difference vs <nearest board>
Handles: .S <one line> · .C <one line> · .B <one line>
Left behind: <the steps and signature traits not carried>

STUDY (Stage 2 single-artist study only): <Artist>, strict
Findings: 1 <principle + evidence on this content> 2 … 3 …   Failure: <what the manner cost here>
```

## 6. Provenance note

**How the entries were made.** Each study was first written from museum, foundation and scholarly texts (`references/BRIEF.md` is the research brief). In November 2026 the key works were then obtained and looked at: measured where a proportion was claimed, and their colour roles and area shares sampled (k-means in CIELAB on the painted or built area, frames and walls cropped out). Rules the images contradicted were corrected and missed moves added (`CHANGELOG.md`). Finally every entry was converted **from observation to process** (§1): what transfers is the procedure and the reasons it works, not the artist's colours or forms. Growth & Form (movement 11) was written from texts and images together.

**Sources used.** Art Institute of Chicago, Cleveland Museum of Art, V&A, Met (object API), Tate, Stedelijk, Cooper Hewitt open data, Centre Pompidou, Kröller-Müller, Kunstmuseum Den Haag, Centraal Museum, RKD, Neue Galerie, Belvedere, MAK, Guggenheim, LACMA, Russian Museum, Pushkin Museum, Europeana, the Internet Archive and Wellcome scans of public-domain books, Arts Council Collection, Buffalo AKG, and official foundation, estate, practice and publisher sites. In the second retry pass, secondary reproductions found by web search were also allowed and are labelled as such (39 of the counted works). Wikimedia Commons refused this machine almost throughout and supplied only a few images. No image is stored in this skill.

**Works visually checked** (282 named key works; substitutes checked in place of unobtainable works are noted in the reference files and not counted):
- **Bauhaus.** Albers (4): Homage to the Square: Light Passage, 1956 (AIC) · Homage to the Square: Yellow Signal, 1962 (AIC) · Homage to the Square: Promise, 1967 (AIC) · Homage to the Square: New Light, 1967 (AIC). Bayer (5): universal alphabet, 1925 · Thuringian emergency banknotes, 1 and 2 million mark, 1923 (V&A) · Breuer Metallmöbel catalogue, 1927 (V&A) · 50 Jahre Bauhaus poster, 1968 (AIC) · World Geo-Graphic Atlas, 1953. Kandinsky (4): Composition VII, 1913 · Composition VIII, 1923 · Yellow-Red-Blue, 1925 · Several Circles, 1926. Klee (9): Twittering Machine, 1922 (MoMA) · Static-Dynamic Gradation, 1923 (Met) · Castle and Sun, 1928 · Ad Parnassum, 1932 (Kunstmuseum Bern) · Sunset, 1930 (AIC) · Mosaic-Like, 1932 (AIC) · Tightrope Walker, 1923 (CMA) · Architecture, 1921 (AIC) · Carnival in the Snow, 1923 (CMA). Moholy-Nagy (3): Light Play: Black White Gray, 1930 · Composition A.XX, 1924 · The Mavericks II (Die Eigenbrötler II), 1927 (AIC).
- **De Stijl.** Huszár (4): De Stijl masthead/cover, 1917 · Bruynzeel boys' bedroom, Voorburg, 1918–c.1920 · Mechanical Dancing Figure, 1920 · Miss Blanche Virginia cigarettes, 1926–28. Mondrian (5): Tableau I, 1921 · Composition C (No. III) with Red, Yellow and Blue, 1935 · Composition with Yellow, Blue and Red, 1937–42 · Broadway Boogie Woogie, 1942–43 · Victory Boogie Woogie, 1942–44. Rietveld (4): Red Blue Chair, 1918 · Rietveld Schröder House, Utrecht, 1924 · Schröder House façade · Zig-Zag Chair, 1934. van der Leck (5): Batavier Line poster, 1915–16 · Composition 1917 No. 4 (Leaving the Factory) · The "Leaving the Factory" series, 1916–17 · Metz & Co. identity, from 1930 · H.C. Andersen, Het Vlas, 1941. van Doesburg (7): De Stijl magazine · Counter-Composition V, 1924 · Contra-compositie VII, 1924 · Counter-Composition VI, 1925 · Café Aubette ciné-dancing, Strasbourg, 1926–28 · Simultaneous Counter-Composition, 1929–30 · Colour scheme for apartments in Drachten, 1921.
- **Constructivism & Suprematism.** Lissitzky (5): Beat the Whites with the Red Wedge, 1919 · Prouns, 1919–1923 · About Two Squares, 1922 · Proun Room, Great Berlin Art Exhibition, 1923 · For the Voice (Dlia golosa), 1923. Malevich (4): Suprematist Composition: Airplane Flying, 1915 · Dynamic Suprematism (Supremus No. 57), 1915–16 · Red Square, 1915 · Suprematist Composition: White on White, 1918. Popova (4): Spatial-Force Construction, 1921 · The Magnanimous Cuckold, 1922 · Textile designs for the First State Textile Printing Works (formerly Zindel), 1923–24 · Muzykal'naia nov' (Musical New Land) no. 10 cover, 1924. Rodchenko (3): Lengiz "Books in All Branches of Knowledge" poster, 1924 · Workers' Club, Paris 1925 · Lef no. 4 cover, 1924. Stepanova (4): Set for The Death of Tarelkin (Meyerhold), 1922 · Chevron flannel, Tsindel factory, 1924 (V&A) · SA (Sovremennaia arkhitektura) no. 2 cover, 1926 · Oktiabr' book catalog cover, 1927.
- **Swiss.** Crouwel (4): Vormgevers poster, Stedelijk Museum, 1968 · New Alphabet, 1967 · Stedelijk catalogue series, 1964–84 · Stedelijk identity and posters, 1963–85. Gerstner (3): Designing Programmes · Morphological box of the typogram (in Designing Programmes) · Holzäpfel Büromöbel poster. Hofmann (6): Graphic Design Manual: Principles and Practice, 1965 · Giselle, Basler Freilichtspiele, 1959 · Stadt Theater Basel 1965, the "feets" poster · Added: Robert Jacobsen / Serge Poliakoff, Kunsthalle Basel, 1958; Stadttheater Basel 1962 and 1963/64; Schweiz kleines Land grosse Landschaft, c. 1965 · Wilhelm Tell, 1963 · Dot/line studies. Müller-Brockmann (5): Beethoven, Tonhalle Zürich · musica viva series · der Film, Kunstgewerbemuseum Zürich · Schützt das Kind! · Grid Systems in Graphic Design. Ruder (5): Typographie · "The Typography of Order", Graphis 85 · TM covers · Added: posters reproduced by Lars Müller Publishers · Added: Typographische Monatsblätter covers and inserts, bound volume.
- **Modernist architecture.** Aalto (6): Viipuri Library, 1927–35 · Paimio Sanatorium, 1929–33 · Paimio armchair, 1931–32 · Stool 60, L-leg patented 1933 · Savoy Vase, 1936 · Villa Mairea, 1938–39. Barragán (5): Casa Luis Barragán, Mexico City · Capuchin Convent Chapel, Tlalpan · Cuadra San Cristóbal, with Andrés Casillas · Casa Gilardi · Torres de Satélite, with Mathias Goeritz. Le Corbusier (5): Villa Savoye, Poissy · Le Modulor · Notre-Dame du Haut, Ronchamp · Pilgrims' house, Ronchamp · Polychromie Architecturale. Mies (5): Barcelona Pavilion, 1929 · Golden onyx wall, Barcelona Pavilion · Farnsworth House, 1951 · Seagram Building and plaza, 1958 · Seagram bronze I-beams. Wright (5): Darwin D. Martin House "Tree of Life" window, 1904 · Robie House, Chicago, 1908–10 · Fallingwater, 1935–37 · Guggenheim Museum, 1943–59 · Coonley Playhouse triptych window, 1912.
- **Japanese Ma.** Ando (5): Row House in Sumiyoshi (Azuma House), 1976 · Row House in Sumiyoshi: the building · Church of the Light, Ibaraki, 1989 · Chichu Art Museum, Naoshima, 2004 · Modern Art Museum of Fort Worth, 2002. Hara (8): MUJI "Horizon," 2003 · MUJI "Tea House," 2005 · RE-DESIGN, 2000 · HAPTIC, Takeo Paper Show 2004 · Designing Design, 2007 · White, 2009/2010 (Lars Müller) · Ex-formation (Lars Müller) · Nagano 1998 Olympic ceremony programmes. Hokusai (7): Under the Wave off Kanagawa (The Great Wave), c. 1830–32 · Thirty-six Views of Mount Fuji, c. 1830–32 · Fine Wind, Clear Morning ("Red Fuji") · Thunderstorm Beneath the Summit (Shower Below the Summit) · Fujimigahara in Owari Province · Hokusai Manga, 1814 onward (15 vols.) · Ryakuga hayaoshie, 1812–14. Sejima/SANAA (5): 21st Century Museum of Contemporary Art, Kanazawa · Glass Pavilion, Toledo Museum of Art · Serpentine Pavilion, London · Rolex Learning Center, EPFL Lausanne · New Museum, New York. Tanaka (6): Nihon Buyo poster · The 8th Sankei Kanze Noh · MUJI identity · Seibu target pattern · Kimono, Textilmuseum Max Berk · Hanae Mori poster.
- **Art Nouveau & Secession.** Gaudí (4): Park Güell · Casa Batlló facade · Sagrada Família nave columns · Sagrada Família stained glass (with Joan Vila-Grau). Hoffmann (8): Hohe Warte houses, 1899–1902 · Lattice vases and baskets, c. 1906 · Purkersdorf Sanatorium, 1904–05 · Sitzmaschine armchair, 1905 · Palais Stoclet, Brussels, 1905–11 · Cabaret Fledermaus, 1907 · Rundes Modell cutlery, c. 1906 · Tall-case clock, c. 1906, added. Klimt (6): Adele Bloch-Bauer I, 1903–07 (Neue Galerie, 140 × 140 cm) · The Kiss, 1908–09 (Belvedere, 180 × 180 cm) · Beethoven Frieze, 1902 (Secession, about 2.15 × 34.14 m) · Stoclet Frieze, 1905–11 (Palais Stoclet, with the Wiener Werkstätte) · Judith I, 1901 (Belvedere), added · Square landscapes from 1899 on (e.g. Schloss Kammer on the Attersee). Mackintosh (5): Argyle Street Tea Rooms high-back chair, 1897 · Glasgow School of Art, 1897–99 / 1907–09 · Willow Tea Rooms, Salon de Luxe, 1903 · Hill House, 1902–04 · White-painted table, 1902, added. Mucha (6): Gismonda (Sarah Bernhardt), 1894–95 · Job (cigarette papers), 1896 · The Seasons, 1896 · Rêverie, 1897–98 · The Arts / The Precious Stones · Documents Décoratifs, 1902.
- **Minimalism / Light & Space.** Agnes Martin (7): Friendship, 1963 · Untitled #4 / Untitled #12, 1977 · With My Back to the World, 1997 · Morning, 1965 · Untitled, 1961 · Untitled #8, 1990 · Untitled #5, 1994; Faraway Love, 1999; Happy Holiday, 1999. Flavin (4): "monument" 1 for V. Tatlin, 1964 · untitled (Marfa project), 1996–2000 · untitled, 1969 (AIC) · untitled, Santa Maria Annunciata in Chiesa Rossa, Milan, 1996–97. Judd (8): Untitled (stack), 1968 (AIC) · Untitled (stack), 1980 (Tate) · Untitled (progression), 1967 (Indianapolis) · Untitled, 1973 (Tate) · 100 untitled works in mill aluminum, 1982–86 (Chinati, Marfa) · Untitled, 1972 (Tate) · Untitled, 1968 (AIC) · Untitled, 1976 (AIC). LeWitt (4): Wall Drawing #63, 1971 (AIC) · Incomplete Open Cubes, 1974 · Wall Drawing #574, 1988 (AIC) · Six Geometric Figures (+ Two), 1980–1 (Tate). Turrell (5): Rayna, 1979 (AIC, installation photo, B&W) · Skyspaces, e.g. The Color Inside · Breathing Light, a Ganzfeld · Aten Reign · Roden Crater.
- **Op & Kinetic.** Cruz-Diez (5): Physichromie 113, 1963/1976 · Physichromie No. 123, 1964 · Induction Chromatique n° 54. Bleu + Noir = Jaune, 1973 · Chromosaturation, 1965/1968 · Ambientación de Color Aditivo, Maiquetía airport, 1974–78. Le Parc (6): Continuel-Lumière Mobile, 1960 onward · Une journée dans la rue (GRAV), 19 April 1966 · Miroir en vibration and 3 jeux avec balles de ping-pong, 1965 · La Longue Marche, 1974 · Séquences progressives, 1959; Instabilité, 1959; Instabilité visuelle, 1959–70; Double progression, 1959–91 · Untitled, 1969. Riley (6): Movement in Squares, 1961 · Fall, 1963 · Hesitate, 1964 · Cataract 3, 1967 · Late Morning, 1967–68 / Rise I, 1968 · Deny II, 1967. Soto (6): Light Trap, 1965 (Tate) · Volume suspendu, 1968 (Pompidou) · Horizontal Movement, 1963 · Cardinal, 1965 · Colour volumes, Centre Pompidou (added in the retry pass, substitutes for the colour Penetrables) · Twelve Blacks and Four Silvers, 1966. Vasarely (4): Zebra · Unités plastiques · Supernovae, 1959–61 · Capella, 1964.
- **Postmodern & New Wave.** Carson (3): Beach Culture · Ray Gun · nucollage.001. Greiman (6): CalArts poster (with Jayme Odgers), 1978 · Douglas W. Schmidt poster, 1980 · Your Turn, My Turn, 1983 · Design Quarterly #133, "Does It Make Sense?", 1986 · AIGA Communication Graphics poster, 1993 · Hand Holding a Bowl of Rice, Wilshire/Vermont, 2007. Scher (5): The Public Theater identity, 1994– · "Bring in 'da Noise, Bring in 'da Funk" poster, 1995 · Public Theater redraw, 2008 · Painted maps, 1998–2010s · Lucent Technologies Center for Arts Education (NJPAC), c. 2000. Sottsass (3): Valentine portable typewriter · Carlton room divider · Casablanca sideboard. Weingart (5): Typografische Monatsblätter covers, 1972–73 · Nine Collages series, 1974–75 · Kunsthalle Basel Kunstkredit 76/77, 1977 · Kunstkredit color posters, 1980–83 · Typographic Process posters NR.4 and NR.5, 1974 (added).
- **Growth & Form.** Blossfeldt (5): Urformen der Kunst, Plate 1: Equisetum hiemale, young shoot ×25 · Plate 6: Equisetum hiemale ×8, and E. arvense fruiting cone ×12 · Plate 30: Saxifraga aizoon leaf rosette ×8 · Plate 54: Adiantum pedatum, young rolled fronds ×8 and ×12 · Plate 113: Asclepias speciosa umbel ×3. Frei Otto (6): German Pavilion, Expo 67, Montreal · Roofs of the Olympic Park, Munich · Multihalle, Mannheim · Institute for Lightweight Structures (IL), Stuttgart-Vaihingen · Soap-film form-finding models · IL 18, minimal surfaces between three rigid rings. Haeckel (5): Kunstformen der Natur, Tafel 1, Phaeodaria (Circogonia), 1899 · Tafel 4, Diatomea (Triceratium), 1899 · Tafel 8, Discomedusae (Desmonema), 1899 · Tafel 18, Discomedusae (Linantha), 1899 · Tafel 71, Stephoidea (Tympanidium), 1899–1904. Hepworth (5): Pelagos, 1946 · Oval Sculpture (No. 2), 1943, cast 1958 · Sphere with Inner Form, 1963 · Single Form (September), 1961 · Single Form (Eikon), 1937–8, cast 1963. Nervous System (5): Hyphae lamps · Floraform · Floraform, uniform-growth control · Kinematics · Generative jigsaw puzzles.

**Not checked.** 98 named works could not be obtained after two retry passes (mostly museum sites that refuse scripted access, works with no reliably captioned reproduction, or Commons-only images). The reference files mark the rules that depended on them *unverified*, and no process step rests on an unverified claim. Thinnest coverage: Moholy-Nagy (3), Rodchenko (3), Gerstner (3), Carson (3), Sottsass (3).

**Limits.** Colours of buildings and objects come from photographs and carry lighting casts; some works were seen only as book, publisher or secondary reproductions, whose colours are approximate; aged paper and faded inks were sampled as they are now. Conclusions rest on 2–9 named works per artist, not on whole careers; steps resting on a single work are listed in the rollout notes and flagged in the reference files where it matters.

**How to use the measurements.** Measured figures are calibration for perception (§P.2) and become kit budgets. Reference-file hex tables are for strict studies and homage only; a kit takes processes, roles and area shares, never an artist's hexes.
