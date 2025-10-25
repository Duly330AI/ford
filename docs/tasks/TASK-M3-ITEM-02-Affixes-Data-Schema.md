# TASK-M3-ITEM-02: Affixes Data Schema & Loader

**Milestone:** M3 - Skills, Loot & Inventory/Hotbar
**Priority:** P0 (High)
**Estimated Effort:** 3-4d
**Dependencies:** TASK-M3-01, TASK-M3-ITEM-01-Affix-Generator

## Objectives

- Create `data/affixes.json` capturing prefix/suffix definitions, slot restrictions, budget costs, stat ranges, and conflicts.
- Author schema `data/schemas/affixes.schema.json` validating structure, slot enums, numeric ranges, and conflict references.
- Implement loader module providing efficient lookup (by slot, rarity, biome) and caching for generator usage.
- Introduce content validation ensuring referenced stats/modifiers align with combat/economy rule sets.
- Add tests verifying schema catches invalid ranges, missing conflicts, unknown target stats, and duplicate IDs.

## Acceptance Criteria

- Affix definitions validate successfully at startup; invalid entries surface descriptive errors.
- Loader exposes API for generator to fetch eligible affixes by slot/rarity/filters with deterministic ordering.
- Data structure supports localization keys for display without embedding user-facing text in JSON.
- Tests include positive fixture plus multiple invalid scenarios covering schema and logical validation.
- Documentation includes example affix entries and guidance for designers.

## Implementation Notes

- Consider splitting affixes by slot groups in JSON while keeping schema consistent (prefix/suffix dictionaries).
- Provide optional weighting fields enabling biome/faction adjustments used by generator.
- Align stat names with canonical IDs in `data/combat_rules.json` or progression rules to avoid mismatch.
- Support versioning metadata for future balancing updates (e.g., `revision` field).

## Related Documents

- docs/ITEMIZATION_DESIGN.md
- docs/CONVENTIONS.md
- docs/TODO/ITEMIZATION_DESIGN_TD.md
- docs/ARCHITECTURE.md
