# TASK-M4-ECON-02: Vendor Data Schema & Loader

**Milestone:** M4 - Nodes, Berufe & Crafting
**Priority:** P0 (High)
**Estimated Effort:** 3d
**Dependencies:** TASK-M3-01, TASK-M4-ECON-01-Core-Economy-System

## Objectives

- Define vendor configuration structure under `data/vendors/*.json` including inventory ranges, restock cadence, modifiers, biome affinities.
- Add schema `data/schemas/vendor.schema.json` enforcing item references, numeric bounds, and optional requirements (reputation, milestones).
- Implement loader module providing lookup APIs (per biome, per vendor) and validation at startup.
- Integrate with economy system to deliver vendor metadata for pricing, restocking, and UI display.
- Create tests verifying schema rejection of invalid vendors (unknown items, overlapping ranges, bad modifiers).

## Acceptance Criteria

- Vendor definitions validate successfully with descriptive errors for missing or incorrect fields.
- Loader caches vendor records for efficient queries and surfaces convenience methods (e.g. `list_vendors_for_biome`).
- Economy system reads vendor modifiers, inventory definitions, and restock timers exclusively through loader API.
- Tests include fixtures for multi-biome vendors, specialty shops, and vendor-specific price modifiers.
- Documentation or sample vendor JSON added to guide designers.

## Implementation Notes

- Support localization keys for display names rather than inline strings per CONVENTIONS.
- Provide optional sections for gold sinks (repair/travel) to be consumed by other systems.
- Consider deriving default spreads/stock from economy rules file to reduce duplication.
- Align vendor IDs with WORLD_BIBLE factions/locations for future quest integration.

## Related Documents

- docs/ECONOMY_AND_VENDORS.md
- docs/CONVENTIONS.md
- docs/TODO/ECONOMY_AND_VENDORS_TD.md
- docs/WORLD_BIBLE.md
