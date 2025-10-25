# TASK-M2-MAGIC-02: Fizzle & Resist Formulas

**Milestone:** M2 - Gegner & Kampfgrundlagen
**Priority:** P0 (Critical)
**Estimated Effort:** 3d
**Dependencies:** TASK-M2-02, TASK-M2-MAGIC-01-Core-Magic-System, TASK-M3-MAGIC-01-Spells-Data-Schema

## Objectives

- Implement fizzle probability calculations per MAGIC_SYSTEM.md using magery skill and spell-provided parameters.
- Implement spell resist checks comparing caster magery vs defender resist_spells, respecting clamp ranges from data.
- Add new configurable parameters to `data/combat_rules.json` (clamps, default scales) and wire them into formulas.
- Ensure partial vs full resist logic is data-driven for future expansion (enable/disable via config).
- Create deterministic tests covering min/max clamp, skill differentials, and parameter overrides.

## Acceptance Criteria

- Fizzle and resist calculations return values consistent with reference examples in MAGIC_SYSTEM.md.
- `combat_rules.json` extended with namespaced magic entries (e.g. `magic.fizzle.min_pct`) and schema updates.
- Magic system consumes parameters exclusively via data loaders (no hardcoded constants in logic).
- Tests seeded with `PYTHONHASHSEED=0` validate probability outputs across representative skill ranges.
- Documentation (combat rules or changelog) updated to highlight new parameters and usage.

## Implementation Notes

- Keep formula helpers pure functions within `game/systems/magic_math.py` (or similar) for unit isolation.
- Add schema validation for new combat rules fields to prevent invalid configuration slipping into runtime.
- Coordinate with skill progression to log resist/fizzle events for analytics hooks (optional but expose event payload).
- Ensure default values preserve existing combat behavior when magic is disabled.

## Related Documents

- docs/MAGIC_SYSTEM.md
- docs/COMBAT_RULES.md
- docs/CONVENTIONS.md
- data/combat_rules.json
