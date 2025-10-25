# TASK-M7-FTUE-04: Scripted Events System

**Milestone:** M7 - First Time User Experience
**Priority:** P1 (Medium)
**Estimated Effort:** 4-5d
**Dependencies:** TASK-M7-FTUE-02-Tutorial-Manager, TASK-M4-QUEST-03, TASK-M2-04

## Objectives

- Implement lightweight scripted event runner capable of sequencing actions (spawn NPC, play audio, move camera, trigger dialogue).
- Integrate with event bus and tutorial manager to drive FTUE scenes (intro narration, first combat encounter).
- Provide data-driven script definitions (`data/tutorial/scripts/*.json`) including conditional branches and delays.
- Ensure system operates deterministically under seeded RNG and remains testable without Arcade dependencies.
- Add tests executing sample scripts verifying sequencing, branching, and failure handling.

## Acceptance Criteria

- Script runner executes tutorial scenario as outlined (wake-up, NPC interactions, first combat) in order.
- Scripts pause/resume based on tutorial manager state and player input (e.g., wait for acknowledgement).
- Errors (missing actors, invalid commands) surface descriptive logs and safely abort script execution.
- Tests validate deterministic ordering and confirm cleanup occurs after script completion.
- Documentation provides script authoring guide and explains available commands.

## Implementation Notes

- Model commands as declarative steps referencing existing systems (quest engine, dialogue, audio).
- Support reusable macros for common patterns (show prompt, wait for objective, reward player).
- Ensure integration with save system to persist script progress when tutorial mid-flow.
- Provide debug tooling to replay scripts or skip ahead for QA.

## Related Documents

- docs/TUTORIAL_FTUE.md
- docs/QUEST_SYSTEM.md
- docs/SOUND_DESIGN.md
- docs/CONVENTIONS.md
