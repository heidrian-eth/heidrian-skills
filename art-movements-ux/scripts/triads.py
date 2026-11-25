#!/usr/bin/env python3
"""Draw random triads of artists (or movements) for Exploration mode (SKILL.md, Stage 2).

Usage:
  python3 scripts/triads.py                      # 10 triads of artists, random seed (printed)
  python3 scripts/triads.py --n 10 --seed 4242   # reproducible
  python3 scripts/triads.py --level movements    # triads of schools; pick the artist inside each school later
  python3 scripts/triads.py --level mixed        # each slot is an artist or a whole school
  python3 scripts/triads.py --exclude "Klimt,Le Parc"   # drop artists the brief rules out
  python3 scripts/triads.py --json
  python3 scripts/triads.py --seed 7 --redraw "T02:Frei Otto"   # re-draw one member (SKILL.md rule: only when it fails in all three roles)

Constraints (so random stays useful):
  * each triad spans at least 2 movements (3 whenever possible) and at least 2 different
    corners of the axes map (order/expression, void/density, still/kinetic);
  * no artist appears in more than 2 triads (schools: at most 4 when drawing schools); no two triads share two members;
  * every movement appears at least once when the draw has a slot for each (3 * n >= movements).
Time-based companions (references/time/) are never in the draw; they are chosen by fit, for dynamic content only.
The script prints each member's one-line process from references/library.md, so fusion can start.
Do not hand-pick replacements: re-draw a member only when its "Fails when" matches the case (see SKILL.md).
"""
import argparse, json, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(HERE, "..", "references", "library.md")

# coarse axes per movement: (order 0 / expression 1, void 0 / density 1, still 0 / kinetic 1)
AXES = {
    "BAUHAUS": (0, 0.5, 0.5), "DE STIJL": (0, 0, 0.3), "CONSTRUCTIVISM & SUPREMATISM": (0.5, 0.3, 0.6),
    "SWISS / INTERNATIONAL TYPOGRAPHIC STYLE": (0, 0.5, 0.2), "MODERNIST ARCHITECTURE": (0.2, 0.2, 0.3),
    "JAPANESE MA & WABI-SABI": (0.1, 0, 0.1), "ART NOUVEAU & VIENNA SECESSION": (0.4, 1, 0.3),
    "MINIMALISM / LIGHT & SPACE": (0, 0.2, 0.1), "OP & KINETIC ART": (0.3, 1, 1),
    "POSTMODERN & NEW WAVE": (1, 1, 0.8), "GROWTH & FORM": (0.4, 0.7, 0.6),
    "FUTURISM": (0.7, 0.7, 1.0),
    "IMPRESSIONISM": (0.8, 0.7, 0.5),
    "ISLAMIC GEOMETRY": (0.0, 0.8, 0.1),
    "CUBISM": (0.4, 0.8, 0.2),
    "RENAISSANCE": (0.0, 0.5, 0.1),
    "CRANBROOK & ORGANIC MODERNISM": (0.2, 0.4, 0.3),
}


def load():
    t = open(LIB).read()
    idx = t[t.index("## Index"):t.index("### 4.1 ")]
    artists, mv = [], None
    for line in idx.split("\n"):
        m = re.match(r"\*\*(.+)\*\*\s*$", line.strip())
        if m:
            mv = m.group(1).upper(); continue
        m = re.match(r"- \*\*(.+?)\*\*: (.*)", line.strip())
        if m and mv:
            artists.append({"artist": m.group(1), "movement": mv, "process": m.group(2)})
    unknown = {a["movement"] for a in artists} - set(AXES)
    if unknown:
        sys.exit(f"movement(s) missing from AXES: {unknown}")
    return artists


def corner(mv):
    o, d, k = AXES.get(mv, (0.5, 0.5, 0.5))
    return (o >= 0.5, d >= 0.5, k >= 0.5)


def valid(tri, level):
    mvs = {m["movement"] for m in tri}
    if level != "movements" and len(mvs) < 2:
        return False
    return len({corner(m["movement"]) for m in tri}) >= 2


def draw(pool, n, level, rng, tries=20000):
    need = {m["movement"] for m in pool}
    cover = 3 * n >= len(need)
    cap = 2 if len(pool) >= 3 * n / 2 else -(-3 * n // len(pool)) + 1  # max uses per member
    for _ in range(200):
        out, use = [], {}
        for _ in range(tries):
            if len(out) == n:
                break
            tri = rng.sample(pool, 3)
            names = [m["artist"] for m in tri]
            if not valid(tri, level):
                continue
            if any(use.get(x, 0) >= cap for x in names):
                continue
            if any(len(set(names) & set(m["artist"] for m in t)) >= 2 for t in out):
                continue
            if level != "movements" and len({m["movement"] for m in tri}) < 3 and rng.random() < 0.7:
                continue  # prefer three movements
            left = need - {m["movement"] for t in out + [tri] for m in t}
            if cover and len(left) > 3 * (n - len(out) - 1):
                continue
            out.append(tri)
            for x in names:
                use[x] = use.get(x, 0) + 1
        if len(out) == n:
            return out
    sys.exit("could not satisfy constraints; lower --n or loosen --exclude")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--n", type=int, default=10)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--level", choices=["artists", "movements", "mixed"], default="artists")
    ap.add_argument("--exclude", default="")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--redraw", action="append", default=[], metavar='"Tnn:Member name"')
    a = ap.parse_args()
    seed = a.seed if a.seed is not None else random.SystemRandom().randrange(10**6)
    rng = random.Random(seed)
    artists = [x for x in load() if x["artist"] not in {e.strip() for e in a.exclude.split(",") if e.strip()}]
    if a.level == "movements":
        pool = [{"artist": mv.title(), "movement": mv, "process": "(choose the artist in this school whose process best fits the case)"} for mv in AXES]
    elif a.level == "mixed":
        pool = artists + [{"artist": "Any of " + mv.title(), "movement": mv, "process": "(choose the artist in this school whose process best fits the case)"} for mv in AXES]
    else:
        pool = artists
    tris = draw(pool, a.n, a.level, rng)
    log = []
    for spec in a.redraw:
        tag, _, who = spec.partition(":")
        k = int(tag.strip().lstrip("Tt")) - 1
        tri = tris[k]
        idx = next(i for i, m in enumerate(tri) if m["artist"] == who.strip())
        used = {}
        for t in tris:
            for m in t:
                used[m["artist"]] = used.get(m["artist"], 0) + 1
        r2 = random.Random(seed * 100 + k + 1)
        cands = [m for m in pool if m["artist"] not in {x["artist"] for x in tri} and used.get(m["artist"], 0) < 2]
        r2.shuffle(cands)
        for c in cands:
            new = tri[:idx] + [c] + tri[idx + 1:]
            if valid(new, a.level):
                tris[k] = new
                log.append(f"T{k + 1:02d}: {who.strip()} -> {c['artist']} (seed {seed * 100 + k + 1})")
                break
        else:
            sys.exit(f"no valid replacement for {spec}")
    if a.json:
        print(json.dumps({"seed": seed, "level": a.level, "redraws": log, "triads": tris}, ensure_ascii=False, indent=1)); return
    print(f"seed {seed} · level {a.level} · {a.n} triads" + ("\nre-draws: " + "; ".join(log) if log else "") + "\n")
    for i, t in enumerate(tris, 1):
        print(f"T{i:02d}  " + "  ×  ".join(m["artist"] for m in t))
        for m in t:
            print(f"      - {m['artist']} ({m['movement'].title()}): {m['process']}")
        print()


if __name__ == "__main__":
    main()
