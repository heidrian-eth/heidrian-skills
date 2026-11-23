# Research brief: artist → UX/UI design principles

Goal: we're building a skill that makes an AI designer stop producing generic "Material / Apple median" interfaces. Each artist's work gets distilled into concrete, *operational* design moves that can be applied to web/app UI (layout, color, typography, rhythm, motion, interaction, texture). Ignore biography except where it explains a method.

## Method
1. Use WebSearch (mode "standard") and WebFetch to look at the artist's key works: paintings, buildings, posters, typefaces, installations, writings or manifestos, and teaching materials. Museum pages (MoMA, Tate, Met, Guggenheim, the artist's foundation) and serious design/architecture sources are best. Aim for 4–8 lookups. Also draw on your own knowledge, but ground specific claims (dates, dimensions, palettes, grid systems, quotes) in what you retrieve.
2. Analyze **how** the work is built, not just what it looks like: proportion systems, grids, color relationships, figure/ground, how the eye is led, tension and balance, repetition and variation, scale jumps, edges, materials, light, time and motion.
3. Translate each into UI moves a front-end designer could implement tomorrow (CSS/layout/type/motion terms are welcome).

## Output
Write ONE markdown file to the exact path you were given, 700–1100 words, with these sections:

```
# <Artist> — <Movement>
## Essence (2–3 sentences: the core idea that makes this artist's work unmistakable)
## Key works examined (5–8 bullets: title, year, one line on what it teaches)
## Space & composition (principles, with specifics: ratios, grids, asymmetry, density, void)
## Color (relationships and logic; give an approximate 4–7 swatch palette as hex with roles)
## Form, line & typography (letterforms if relevant; else how shape/line language would map to type; suggest 1–3 real, freely available fonts, e.g. Google Fonts, that fit)
## Rhythm, motion & time (how it would move/animate/respond to interaction)
## UI translations (8–12 concrete, imperative moves, e.g. "Let one element break the grid by 1.5× its column width"; include at least one layout, one color, one type, one motion, one interaction pattern)
## What this artist would reject (4–6 anti-patterns: things common in generic UI they'd refuse)
## Signature prompt seed (one dense paragraph, 60–100 words, you'd give a designer to work "in the manner of" this artist on an app screen)
## Sources (URLs actually consulted)
```

Rules: be specific and surprising rather than generic ("use whitespace" is useless; "let 60% of the viewport be a single flat field with content huddled in the lower-left third" is useful). Don't reproduce long quotes (under 15 words, max one per source). Don't save image files. When finished, reply with just the file path and one line summarizing the most distinctive idea.
