# Kenya Hara — Japanese Ma / contemporary design

## Essence
Hara designs empty containers. Emptiness (*kū*) is not minimalism but a vessel awaiting the viewer's meaning: one question, many answers. White is a way of perceiving, not a color, and the senses (touch above all) complete the work.

## Key works examined
- **MUJI "Horizon," 2003.** Bolivia's Salar de Uyuni (photo: Tamotsu Fujii) and Mongolia. Earth, sky, a tiny figure, a small logo, and no product or slogan. Teaches that presence can replace message.
- **RE-DESIGN, 2000.** Shigeru Ban's square toilet roll (it resists free spinning, so it saves paper) and Kaoru Mende's twig matches. Teaches you to redesign the familiar instead of inventing.
- **HAPTIC, Takeo Paper Show 2004.** 22 creators designed for touch with no sketching first: logos in animal hair and cultured mold, Fukasawa's fruit-skin juice packs. Teaches that texture carries information.
- **SENSEWARE / Tokyo Fiber (Holon 2010).** New synthetic fibers given to architects, fashion designers and an automaker. Teaches that the material is the interface.
- ***Designing Design*, 2007.** Exformation (making the known unknown), MUJI as "nothing, yet everything."
- ***White*, 2009/2010 (Lars Müller).** 白 is a radical inside the character for emptiness, and the red circle holds many meanings because it holds nothing.
- **MUJI naming.** An "oak table," not a "coffee table". The function is left open.

## Space & composition
- **The horizon split.** Horizon posters are two flat fields, sky and ground, with the line placed roughly at the halfway point or slightly below. A human-scale mark sits at about 1–2% of frame height. Scale contrast between a vast field and a tiny figure does the emotional work.
- **One question per surface.** Each composition has a single focal proposition. Everything else is field.
- **Peripheral anchoring.** The logo or sign-off sits small in a corner or bottom margin, never centered. It behaves like a signature, not a headline.
- **Density through absence.** In print layouts 70–85% of the page is often unprinted paper. Text sits in narrow columns with large, generous margins (the head margin is often larger than the column itself).

## Color
White is a family of whites distinguished by paper and light. MUJI's palette is unbleached and earthy, and red appears only as a small seal (*hinomaru* logic: one red dot holds infinite meaning).

| Role | Hex | Note |
|---|---|---|
| Field / paper | `#F5F2EB` | Warm unbleached white, never pure `#FFF` |
| Secondary field | `#E9E4D8` | Kraft-adjacent, for the "ground" band |
| Sky / cool white | `#EEF1F2` | The salt-flat upper field |
| Ink | `#3A3733` | Warm charcoal, softer than black |
| Quiet text | `#8C877E` | Captions, metadata |
| Seal accent | `#7F0019` | MUJI burgundy, max one instance per screen |

The logic is near-monochrome warmth, temperature shifts instead of hue shifts, and one red point as punctuation.

## Form, line & typography
Hara's type is small, light and straight. Sans and Mincho appear in modest sizes and one weight, and hairline rules divide fields like a horizon. Hierarchy comes from position and space, not weight. Forms are rectangles and the circle (vessel, seal).
- **Fonts:** *Noto Serif JP* (Mincho flavor for display), *Zen Kaku Gothic New* or *Noto Sans JP* for UI text, and optionally *Shippori Mincho* for editorial headings.
- Set body at 13–15px with 0.04–0.08em tracking and generous line-height (1.8–2.0). Headlines rarely exceed 1.5× body size.

## Rhythm, motion & time
Motion should feel like a breath or a slow change of light. Use long fades (600–1200ms, ease-out), with no bounce. Following Haptic, responses should read as texture: a 1px pressure inset, or a soft shadow that appears only on contact. Treat waiting time as *ma*. Leave a beat of empty screen before content arrives, rather than showing a spinner.

## UI translations
1. **Horizon layout:** split the hero into two flat fields (`#EEF1F2` over `#E9E4D8`) at 55/45. Place one small element (≤24px) on the line, and nothing else above the fold.
2. **Corner signature:** put the brand mark at 11–12px in the bottom-left corner, never in a centered header bar.
3. **Name nouns, not purposes:** label containers by what they are ("Notes," "Folder," "Board"), not prescribed uses ("Meeting Notes Template"). Let users assign the meaning.
4. **Empty states as invitations:** a blank canvas with one hairline and a single quiet prompt. No illustrations, no mascots, no onboarding checklist.
5. **One red point:** allow exactly one `#7F0019` element per screen (an active state, a save dot). If a second appears, demote one.
6. **Type hierarchy by placement:** use one weight (400) throughout. Differentiate headings through isolation (48px+ space around them) and position, not boldness or size jumps above 1.5×.
7. **Warm whites only:** ban `#FFFFFF`. Layer 2–3 whites a few percent apart to separate regions instead of borders and cards.
8. **Haptic surfaces:** add a 2–3% opacity paper-grain noise texture to fields. On press, inset by 1px with an inner shadow, so the click reads as touch.
9. **Slow reveals:** content fades in over 800ms after a 200ms empty pause. Hover states shift tone only, never scale.
10. **Exformation pass:** redesign one everyday control (a checkbox, a pager) the way Ban redesigned the toilet roll, slightly unfamiliar so users notice it.
11. **Margins larger than content:** cap text columns at 32–38ch and give the page top margin ≥ 20vh.

## What this artist would reject
- Hero sections that shout a value proposition with a CTA button. Hara sells presence, not persuasion.
- Over-prescriptive UI: wizards, tooltips on everything, labels that dictate use.
- Pure white backgrounds and pure black text, plus gradient blobs and saturated brand color everywhere.
- Decorative illustration in empty states that fills the void instead of offering it.
- Bold, heavy type stacks and hierarchy by size inflation.
- Springy, attention-seeking motion and confetti.

## Signature prompt seed
Design this screen as an empty vessel in the manner of Kenya Hara. Use two flat fields of warm white, cool salt-sky over pale kraft ground, divided by a hairline horizon at 55%. Place one small element on the line. Set all type in a single light weight (Zen Kaku Gothic New, Noto Serif JP for one heading), tracked wide, with hierarchy made by space alone. Use one burgundy point per screen, a faint paper grain, and fades that take a breath. Name things by what they are, not what to do. Leave the meaning for the user to bring.

## Sources
- https://qz.com/quartzy/1140182/mujis-design-philosophy-is-emptiness-not-minimalism-says-kenya-hara
- https://www.muji.com/my/flagship/huaihai755/archive/hara.html
- https://www.designboom.com/design/kenya-hara-designing-design/
- https://lars-mueller-publishers.com/white
- https://www.ndc.co.jp/hara/en/works/2014/08/redesign.html
- https://a-g-i.org/design/haptic
- https://www.core77.com/posts/16765/kenya-haras-senseware-exhibit-on-applications-for-artificial-fibers-16765
- https://blakecrosley.com/blog/design-philosophy-kenya-hara
- https://www.packworld.com/home/news/13345020/in-japan-fruit-juice-comes-in-fruitlike-packaging
