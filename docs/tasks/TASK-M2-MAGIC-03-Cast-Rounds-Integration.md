# TASK-M2-MAGIC-03: Cast Rounds Integration

**Milestone:** M2 - Gegner & Kampfgrundlagen
**Priority:** P0 (Critical)
**Estimated Effort:** 3-4d
**Dependencies:** TASK-M2-04, TASK-M2-MAGIC-01-Core-Magic-System, TASK-M2-MAGIC-02-Fizzle-Resist-Formulas

## Objectives

- Extend turn manager to support multi-round casting with explicit `cast_rounds_remaining` state per caster.
- Apply meditation modifiers and external effects to casting duration using data-driven parameters.
- Handle interruption rules (damage taken, movement, stun) by emitting cancel outcomes and refund policies per design.
- Update initiative/turn sequencing to surface casting progress in outcomes for UI display.
- Add tests covering uninterrupted casts, interrupted casts, and simultaneous multi-caster scenarios.

## Acceptance Criteria

- Combat core tracks casting progress deterministically and resumes after partial turns when conditions allow.
- Interruption events trigger correct state cleanup (mana consumption, reagent usage per design) and inform skill progression.
- Cast states serialize into combat save data to survive mid-fight save/load cycles.
- System allows 0-round instant casts and >1 round spells without breaking existing melee/ranged intents.
- Tests verify interactions with wait/defend actions and ensure RNG seeding consistency.

## Implementation Notes

- Store casting state within combat actor context to avoid global mutable singletons.
- Provide explicit API for scenes to query progress (e.g. `get_cast_queue(actor_id)`) for UI overlays.
- Update combat log/outcome schema to include cast start, progress tick, completion, and interruption events.
- Coordinate with TASK-M6-UI-09 to ensure necessary data (cast rounds remaining, reagents) available for display.

## Related Documents

- docs/MAGIC_SYSTEM.md
- docs/COMBAT_RULES.md
- docs/ARCHITECTURE.md
- docs/TODO/MAGIC_SYSTEM_TD.md
