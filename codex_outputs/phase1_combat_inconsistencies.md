# Phase 1 — Combat Inconsistencies

## Executive Summary
- Combat rules are largely formula-based and mapped to `data/combat_rules.json`. However, Dodge is undocumented and absent from `combat_rules.json`, while Parry is documented and present. One document uses the literal token "d20" (as a contrast example), which can be misread as using dice. Initiative uses `random(1-100)` (acceptable).

## Critical Issues (must fix)
- Missing Dodge configuration and documentation
  - `combat_rules.json` top-level keys: hit_chance, parry, damage, movement, recovery, ranged, initiative, crit. No `dodge` section present.
  - Docs contain Parry formula but no Dodge formula/parameters. ASCII flow mentions "Parry/Dodge" but Dodge is not specified.
- Dice token present in gameplay doc
  - `docs/GAMEPLAY.md:130` contains the literal "d20" (even if stating to avoid dice). This violates the “no dice-notation” rule at face value.

## High Priority Issues
- Ranged coverage is minimal in docs relative to other sections (2 matches vs. 11–37 for others). Ensure full parity with `ranged` parameters in `combat_rules.json`.
- Ensure `crit` parameters and usage are fully specified (present in JSON; limited doc mentions).

## Medium Priority Issues
- Consistency of constants between examples and `combat_rules.json` (e.g., factor names, bounds) should be auto-validated in CI to prevent drift.

## Low Priority Issues
- Clarify that `random(1-100)` is a seeded integer roll (no dice tables); reduce ambiguity around wording like "Roll" where possible.

## Informational Notes
- Coverage counts in docs for combat keys (occurrence search):
  - hit_chance: 12, parry: 19, damage: 37, movement: 11, recovery: 19, ranged: 2, initiative: 9, crit: 3

## Recommendations
- Add a `dodge` section in `combat_rules.json` with documented parameters and acceptance tests; add a matching doc section in COMBAT_RULES.md.
- Reword the "d20" reference in GAMEPLAY.md to "tabletop dice" to avoid literal dice notation.
- Expand Ranged documentation (reload, accuracy modifiers, penalties) to match `ranged` keys in JSON.
- Add a CI compliance test verifying each top-level key in `combat_rules.json` appears in COMBAT_RULES.md to guard documentation drift.

## Statistics
- combat_rules.json keys found: hit_chance, parry, damage, movement, recovery, ranged, initiative, crit
- Missing from JSON: dodge
- Dice tokens found in docs: GAMEPLAY.md: "d20"
