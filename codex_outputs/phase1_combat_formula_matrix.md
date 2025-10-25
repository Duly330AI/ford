# Phase 1 — Combat Formula Matrix

## Executive Summary
Matrix of combat parameters in `data/combat_rules.json` and their documentation presence.

## Parameter Coverage
- initiative: present in JSON; documented (formula present; uses random(1-100)).
- hit_chance: present in JSON; documented (formula + parameters + example).
- damage: present in JSON; documented (formula + parameters + example).
- parry: present in JSON; documented (formula + parameters + example).
- dodge: missing in JSON; not documented (gap).
- movement: present in JSON; documented (formula + example).
- recovery: present in JSON; documented (formula + parameters + example).
- ranged: present in JSON; minimally documented (low coverage; expand section).
- crit: present in JSON; mentioned sparsely; expand details.

## Notes
- Coverage counts in docs (occurrence-only heuristic):
  - hit_chance: 12, parry: 19, damage: 37, movement: 11, recovery: 19, ranged: 2, initiative: 9, crit: 3

## Recommendations
- Add `dodge` to JSON and COMBAT_RULES.md.
- Flesh out `ranged` and `crit` sections to match implementation detail.
