# TASK-M3-GEN-01: Threat Budget Spawner

**Milestone:** M3 - Skills, Loot & Inventory/Hotbar
**Priority:** P0 (Critical)
**Estimated Effort:** 5-6d
**Dependencies:** TASK-M1-GEN-01-Biome-System, TASK-M1-GEN-02-Room-Tagging-System, TASK-M2-07

## Objectives

- Implement encounter loader for `data/encounters/*.json` including schema validation and faction/threat metadata.
- Design deterministic threat budget algorithm allocating mobs per room based on depth, biome, and tag rules.
- Integrate with spawn pass to respect faction weights, elite/boss probabilities, and environmental constraints (LOS, pathing).
- Provide hooks for future scripted encounters and ensure compatibility with AI faction diplomacy.
- Build tests covering budget adherence, depth scaling, biome-specific overrides, and deterministic seeded outcomes.

## Acceptance Criteria

- Threat budget distribution matches formulas in DUNGEON_GENERATOR.md with configurable tolerances and elite probabilities.
- Encounter tables validated for cross-references (mob IDs, required skills) before generation begins.
- Spawn placements avoid unreachable tiles and respect room tags (e.g. boss rooms, resource nodes).
- Seeds produce consistent spawn layouts across runs; integration tests capture golden outputs for regression.
- API exposes spawn summaries for debug overlays (F5) and analytics.

## Implementation Notes

- Separate data parsing from allocation logic to simplify testing and allow offline balancing tools.
- Support optional weights per biome/tag combination to bias encounters without code changes.
- Provide instrumentation (e.g. threat budget remaining, picks) to assist designers in tuning tables.
- Coordinate with loot system to align encounter IDs with loot table selections.

## Related Documents

- docs/DUNGEON_GENERATOR.md
- docs/TODO/DUNGEON_GENERATOR_TD.md
- docs/WORLD_BIBLE.md
- docs/ARCHITECTURE.md
