# TASK-M4-QUEST-01: Core Quest Engine

**Milestone:** M4 - Nodes, Berufe & Crafting
**Priority:** P0 (High)
**Estimated Effort:** 5-6d
**Dependencies:** TASK-M2-04, TASK-M3-03, TASK-M4-15

## Objectives

- Implement `game/systems/quest_engine.py` managing quest lifecycle FSM (offered, active, succeeded, failed, cancelled).
- Handle objective progress updates via events (kill, collect, use_item, location, time) with deterministic tracking.
- Provide APIs for accepting, updating, completing, and abandoning quests; emit outcome events for UI/save systems.
- Maintain per-actor quest state and support multi-step objectives with dependencies and timers.
- Add comprehensive tests covering progression paths, branching objectives, failure conditions, and restart scenarios.

## Acceptance Criteria

- Quest engine processes event payloads and updates objectives per QUEST_SYSTEM.md examples.
- State transitions enforce requirements (level, skills) and trigger journal entries via localization keys.
- Engine exposes query interfaces (active quests, objective status) for UI and tutorial systems.
- Save/load integration plan established (see TASK-M5-01 extension) with serialization hooks implemented.
- Tests run deterministically with seeded RNG where applicable (e.g. random objective counts).

## Implementation Notes

- Represent quests and objectives using dataclasses/typed models loaded from JSON definitions.
- Ensure engine operates headless with no Arcade dependencies; event hooks should rely on adapter interface.
- Provide instrumentation/logging toggles for debugging quest progression.
- Coordinate with tutorial manager task to reuse quest engine events for FTUE scripting.

## Related Documents

- docs/QUEST_SYSTEM.md
- docs/TODO/QUEST_SYSTEM_TD.md
- docs/ARCHITECTURE.md
- docs/CONVENTIONS.md
