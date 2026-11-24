# heidrian-skills

**Skills that make AI agents do the work like a studio, not like an average.**

Out of the box, a model designs, writes and plans toward the middle of its training data. Each skill here replaces that default with a real method: a sequence of stages, hard rules, named failure modes and checks the agent must pass before it shows you anything. Drop a folder into your agent and the output changes character.

## Skills

### [art-movements-ux](art-movements-ux/)

> **70 artists. 14 movements. One design system that looks like none of them.**

Ask for a UI and you get rounded cards, soft shadows and one brand blue. This skill sends the agent to Leonardo, Albers, Barragán, the Eameses, Riley, Hara and more than sixty others, not to copy their look, but to borrow *how they solved problems* your product actually has. It builds a mood board, distils it into a locked brand book and UI kit, and generates every screen from that kit alone.

- **Processes, not pastiche.** Every artist is an ordered, parameterised process with the reason it works and when it fails.
- **Checked against the real works.** Key works were colour-sampled, and music measured from recordings and scores, with the entries corrected to match.
- **Exploration mode.** Ten random triads of artists, fused into ten boards, rendered side by side. Pick one or mix by layer.
- **Built-in guardrails.** WCAG contrast, reduced motion, tap targets, and a detector for the generic look.

[Read the skill →](art-movements-ux/)

## Install

These follow the [Agent Skills](https://docs.claude.com/en/docs/claude-code/skills) format: a folder with a `SKILL.md` and its references.

```bash
git clone https://github.com/heidrian-eth/heidrian-skills.git
cp -r heidrian-skills/art-movements-ux ~/.claude/skills/
```

For one project only, copy into that project's `.claude/skills/` instead. The agent picks the skill up when your request matches its description, or when you name it.

## Image credits

Artwork thumbnails in `art-movements-ux/assets/works/` belong to their rights holders and are credited individually next to each image. They illustrate the commentary on each artist's method.
