# TASK-M3-ITEM-01: Affix Generator

**Milestone:** M3 - Skills, Loot & Inventory/Hotbar
**Priority:** P0 (High)
**Estimated Effort:** 5-6d
**Dependencies:** TASK-M3-02, TASK-M3-08, TASK-M2-07

## Objectives

- Implement `game/systems/affix_generator.py` generating item modifiers using budget-based algorithm defined in ITEMIZATION_DESIGN.md.
- Support rarity roll, affix slot allocation, budget enforcement, and deterministic RNG via injected seed stream.
- Provide APIs for generating loot drops, crafting upgrades, and vendor inventory enhancements.
- Emit metadata (rolled affixes, budget spent) for logging and debugging.
- Add seeded tests covering each rarity tier, budget compliance, conflict handling, and determinism.

## Acceptance Criteria

- Generated items respect defined budget per rarity, never exceeding total cost or slot limits.
- Affix conflicts (e.g. quick vs weighted) resolved per data rules; duplicates avoided unless permitted.
- RNG seeding yields repeatable items for identical seeds across runs/tests.
- Generator exposes functions for preview vs commit flows (e.g. UI preview before purchase).
- Tests validate integration with base item stats ensuring modifiers apply correctly.

## Implementation Notes

- Structure generator into composable steps (roll rarity, allocate budget, pick affixes, finalize) for easier testing.
- Provide hooks to bias affix pools based on biome, faction, or item tags (data-driven weights).
- Ensure generator outputs data structure compatible with inventory/save serialization.
- Align error handling with systems conventions (raise `DataValidationError` for missing affixes, etc.).

## Related Documents

- docs/ITEMIZATION_DESIGN.md
- docs/TODO/ITEMIZATION_DESIGN_TD.md
- docs/CONVENTIONS.md
- docs/ARCHITECTURE.md
