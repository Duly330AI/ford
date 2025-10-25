# Master Inconsistency Report — Combat & Magic Focus

## Executive Summary
The project’s combat documentation and data are in strong shape for Hit Chance, Parry, Damage, Movement, Recovery, and Initiative. The most significant gap is Dodge: it is referenced at a high level but not specified in JSON or documentation. For Magic, data is formula-based and consistent, but the documentation contains a dice-based example and omits the `fizzle` mechanic specification. A single recipe input has an orphaned reagent ID.

## Critical Issues (must fix)
- Missing Dodge system (docs + data)
  - No `dodge` section in `combat_rules.json`; no formula or parameters in COMBAT_RULES.md.
- Dice notation in MAGIC_SYSTEM.md
  - Replace `2d6` example with base/variance/scaling to align with `spells.json`.
- Orphaned recipe input
  - `brew_cure_potion` uses `reagent_spider_silk`; items define `reagent_spiders_silk`.

## High Priority Issues
- Ranged and Crit sections are under-documented relative to JSON presence.
- Magic: `fizzle` is present in `spells.json` but undocumented (formula and modifiers missing).
- Magic: Document mana cost formula and `resist_check` behavior.

## Medium Priority Issues
- Progression: Docs reference curve profiles in places; JSON has a single `slowdown_mode`. Align model or add a `curves` map.
- Add CI validations (schema and cross-ref) for combat docs vs JSON and for recipe/loot integrity.

## Low Priority Issues
- Reword "d20" occurrence in GAMEPLAY.md to avoid literal dice notation, even when used as a contrast example.
- Clarify wording around “roll” to emphasize seeded integer randomness (not dice tables).

## Informational Notes
- `combat_rules.json` keys: hit_chance, parry, damage, movement, recovery, ranged, initiative, crit.
- Dice tokens found: GAMEPLAY.md contains "d20"; MAGIC_SYSTEM.md contains "2d6".
- Spells use `cost.mana` and `cost.reagents{}` with valid reagent IDs (8 used, 11 available).

## Recommendations
- Add Dodge to JSON and COMBAT_RULES.md; include tests.
- Remove dice from MAGIC_SYSTEM.md; add Fizzle and Mana formula sections; document Resist Check.
- Fix recipe reagent ID; add CI lints for data cross-references.
- Add doc coverage tests for all combat parameters.

## Statistics
- Docs scanned: 7 key files (combat, gameplay, magic, etc.)
- Data scanned: combat_rules.json, spells.json, items.json, recipes.json, loot_tables.json, monsters.json, progression_rules.json, skills.json
