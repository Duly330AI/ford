# TASK-M3-ITEM-03: Material & Quality System

**Milestone:** M3 - Skills, Loot & Inventory/Hotbar
**Priority:** P0 (High)
**Estimated Effort:** 4-5d
**Dependencies:** TASK-M3-02, TASK-M4-02, TASK-M3-ITEM-01-Affix-Generator

## Objectives

- Implement material tiers (iron, bronze, verite, valorite, etc.) and quality states (worn, fine, masterwork) as data-driven modifiers.
- Extend item model to reference material/quality IDs and apply corresponding stat adjustments at runtime.
- Add data definitions (`data/materials.json`, `data/quality.json`) with schemas validating modifier ranges and compatibility.
- Integrate materials/quality into crafting outputs, loot generation, and economy pricing hooks.
- Provide tests covering modifier stacking, crafting transitions (repair/upgrade), and data validation.

## Acceptance Criteria

- Items reflect correct base stats adjusted by material + quality data without hardcoded constants.
- Crafting and loot pipelines can request specific materials/qualities and receive deterministic results.
- Economy pricing consumes quality modifiers from data files to adjust sell/buy values automatically.
- Tests validate that applying multiple modifiers respects clamping rules and remains deterministic under seeded RNG.
- Documentation added detailing material/quality data format and integration points.

## Implementation Notes

- Use composable modifier pipeline to avoid duplicating stat adjustment logic across systems.
- Ensure save/load persists material and quality attributes, maintaining backward compatibility with existing items.
- Provide developer tooling (e.g. debug print) to inspect final stats for generated items.
- Coordinate with crafting tasks to surface new requirements or UI updates.

## Related Documents

- docs/ITEMIZATION_DESIGN.md
- docs/ECONOMY_AND_VENDORS.md
- docs/CONVENTIONS.md
- data/combat_rules.json
