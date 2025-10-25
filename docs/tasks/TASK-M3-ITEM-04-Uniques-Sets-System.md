# TASK-M3-ITEM-04: Uniques & Sets System

**Milestone:** M3 - Skills, Loot & Inventory/Hotbar
**Priority:** P0 (High)
**Estimated Effort:** 4d
**Dependencies:** TASK-M3-ITEM-01-Affix-Generator, TASK-M3-ITEM-02-Affixes-Data-Schema, TASK-M3-ITEM-03-Material-Quality-System

## Objectives

- Define `data/uniques.json` capturing unique item templates, fixed mods, lore keys, and drop sources.
- Add support for item sets (2-4 pieces) including data representation of bonuses per piece count.
- Extend loot pipeline to spawn uniques/sets deterministically with seed tracking and drop restrictions.
- Implement systems logic applying set bonuses when equipped counts reached and removing when unequipped.
- Provide tests covering unique generation, set bonus activation/deactivation, and save/load persistence.

## Acceptance Criteria

- Unique items spawn with fixed stats plus optional random rolls per design while remaining deterministic per seed.
- Set bonus calculations trigger correctly across combat stats, resistances, and effects defined in data.
- Loot tables integrate unique/set entries without breaking existing drop rates; duplicates controlled via data flags.
- Tests confirm serialization retains unique IDs, set membership, and bonus states.
- Documentation includes examples for designers and describes integration with affix/material systems.

## Implementation Notes

- Support gating uniques by biome/faction/quest progress through data fields consumed by spawner/economy systems.
- Provide debug hooks to inspect set bonus status per actor for balancing.
- Align localization keys with i18n conventions (no inline display text in data files).
- Ensure generator gracefully handles exhaustion of unique pools (e.g. reroll fallback or skip).

## Related Documents

- docs/ITEMIZATION_DESIGN.md
- docs/WORLD_BIBLE.md
- docs/CONVENTIONS.md
- docs/TODO/ITEMIZATION_DESIGN_TD.md
