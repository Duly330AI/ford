# TASK-M7-FTUE-02: Tutorial Manager

**Milestone:** M7 - First Time User Experience
**Priority:** P1 (Medium)
**Estimated Effort:** 5-6d
**Dependencies:** TASK-M4-QUEST-01, TASK-M4-QUEST-03, TASK-M5-01

## Objectives

- Implement `game/tutorial/tutorial_manager.py` orchestrating FTUE phases, state transitions, and completion flags.
- Integrate with event bus to react to player actions (movement, inventory use, combat) and trigger prompts/quests.
- Manage persistence of tutorial progress, skip status, and unlocked systems via save schema.
- Provide APIs for scripted events, UI overlay triggers, and telemetry logging.
- Add tests simulating full tutorial flow, skip path, and failure/retry scenarios with deterministic outcomes.

## Acceptance Criteria

- Tutorial phases progress according to TUTORIAL_FTUE.md timeline, emitting prompts and gating features appropriately.
- Manager respects skip flag and allows tutorial to be disabled/enabled via settings.
- State persists across save/load without duplication or regression when tutorial partially complete.
- Tests verify events triggered only once and ensure re-entry after failure works as designed.
- Documentation updated describing integration points and configuration.

## Implementation Notes

- Structure phases as declarative data (JSON or YAML) to allow content iteration without code changes.
- Provide debug commands to jump to specific tutorial stages for QA.
- Coordinate with quest engine to reuse objective tracking where possible (tutorial quests as data).
- Ensure tutorial module isolated; core gameplay should function with tutorial disabled (feature flag).

## Related Documents

- docs/TUTORIAL_FTUE.md
- docs/QUEST_SYSTEM.md
- docs/TODO/TUTORIAL_FTUE_TD.md
- docs/ARCHITECTURE.md
