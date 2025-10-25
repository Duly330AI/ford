# TASK-M3-MAGIC-01: Spells Data Schema & Loader

**Milestone:** M3 - Skills, Loot & Inventory/Hotbar
**Priority:** P0 (Critical)
**Estimated Effort:** 3-4d
**Dependencies:** TASK-M3-01, TASK-M2-MAGIC-01-Core-Magic-System

## Objectives

- Define `data/spells.json` structure covering cost, circles, effects, fizzle, resist, and AI tags per MAGIC_SYSTEM.md.
- Author JSON Schema at `data/schemas/spells.schema.json` enforcing IDs, numeric bounds, and nested object rules.
- Implement loader/validator module (e.g. `game/data_loader/spells.py`) that validates at startup and exposes typed records.
- Add schema-driven tests ensuring invalid definitions (bad IDs, missing costs, circle mismatch) raise descriptive errors.
- Document data-driven parameters that link to `combat_rules.json` (e.g. fizzle clamp, resist scales).

## Acceptance Criteria

- `data/spells.json` validated against `spells.schema.json` during preflight; failure aborts game start.
- Loader provides deterministic ordering and caches parsed spell definitions for combat/magic systems.
- Schema enforces reagent IDs that exist in `data/items/*.json` and skill references from `data/skills.json`.
- Test suite includes positive fixture and multiple negative fixtures (missing mana cost, invalid circle, duplicate ID).
- Documentation updated (README or data docs) to show how to extend spells via JSON without code changes.

## Implementation Notes

- Structure schema to allow extensibility (future scrolls, channel times) via `additionalProperties: false` on known objects.
- Reuse existing validation utilities from TASK-M3-01 for schema registration and CLI tooling.
- Provide helper that returns spells grouped by circle for UI/skill progression usage.
- Coordinate with combat rules by exposing references for formula parameters (fizzle base, magery factor).

## Related Documents

- docs/MAGIC_SYSTEM.md
- docs/CONVENTIONS.md
- docs/ARCHITECTURE.md
- docs/TODO/MAGIC_SYSTEM_TD.md
