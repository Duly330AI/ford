# TASK-M2-MAGIC-01: Core Magic System

**Milestone:** M2 - Gegner & Kampfgrundlagen
**Priority:** P0 (Critical)
**Estimated Effort:** 5-7d
**Dependencies:** TASK-M2-04, TASK-M3-02, TASK-M3-06

## Objectives

- Implement `game/systems/magic_system.py` with deterministic casting pipeline (request -> validation -> outcome events).
- Expose APIs to resolve cast intents from `systems/combat` without introducing Arcade dependencies.
- Consume mana and reagents via inventory/resource services; fail casts when costs not met.
- Emit structured outcomes for success, fizzle, resist, and side-effects (damage, buffs, summons) for scene adapters.
- Provide hooks for skill progression (Magery, Meditation, Resist Spells) consistent with usage-based gains.
- Ensure all numeric parameters come from data (`data/combat_rules.json`, `data/spells.json`, `data/progression_rules.json`).

## Acceptance Criteria

- Casting intents routed through combat core call the magic system and receive deterministic outcomes based on seed.
- Mana, reagent consumption, and cooldown/cast_round bookkeeping persist correctly across turns and saves.
- Fizzle and resist results emit discrete outcome events with structured payloads for UI/log adapters.
- Unit tests cover successful cast, fizzle path, resist path, and resource exhaustion using seeded RNG.
- System raises validation errors for missing spell IDs or malformed data, failing fast during load.

## Implementation Notes

- Keep system stateless per invocation; inject required services (inventory, skills, rng) explicitly for testability.
- Leverage existing intent/outcome dataclasses in `systems/combat` to avoid duplication.
- Register the magic system with combat via composition to preserve single-responsibility and facilitate mocking.
- Provide utility helpers for repeated checks (cost payment, skill lookup) under `game/systems/_shared` if reuse is needed.

## Related Documents

- docs/MAGIC_SYSTEM.md
- docs/CONVENTIONS.md
- docs/COMBAT_RULES.md
- docs/ARCHITECTURE.md
