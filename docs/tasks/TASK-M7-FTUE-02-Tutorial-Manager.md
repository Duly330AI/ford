- [ ] ID: TASK-M7-FTUE-02-Tutorial-Manager
  Title: Tutorial Manager (Phase FSM, Event Integration)
  Status: Proposed
  Priority: P1
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `game/tutorial/tutorial_manager.py`, `data/tutorial/phases.json`, `tests/tutorial/test_tutorial_manager.py`
  DependsOn: TASK-M4-QUEST-01, TASK-M4-QUEST-03, TASK-M5-01
  Notes:
  Implementiere TutorialManager: FTUE-Phases FSM, State-Transitions, Completion-Flags. Event-Bus Integration: Player-Actions (Movement, Inventory, Combat) → Prompts/Quests. Tutorial-Progress persistent via Save-Schema, Skip-Status. APIs: Scripted-Events, UI-Overlay-Triggers, Telemetry-Logging. Debug-Commands für QA. Phases als Declarative-Data (JSON) für Content-Iteration. Feature-Flag für Tutorial-Disable.
  Acceptance:
  - [ ] Phases progredient per TUTORIAL_FTUE.md Timeline, Emits Prompts, Gates Features.
  - [ ] Manager respektiert Skip-Flag, Tutorial can disabled/enabled via Settings.
  - [ ] State persistiert über Save/Load, no Duplication/Regression.
  - [ ] Tests: Events triggered Once, Re-entry nach Failure works.
  - [ ] Doku: Integration-Points, Configuration.
  Tests:
  - [ ] **Phase-Progression-Test**: Phases transition korrekt.
  - [ ] **Event-Trigger-Test**: Player-Actions triggern Prompts.
  - [ ] **Skip-Test**: Skip-Flag bypasses Tutorial.
  - [ ] **Save-Load-Test**: Tutorial-Progress persists.
  References:
  - docs/TUTORIAL_FTUE.md
  - docs/QUEST_SYSTEM.md
  - docs/ARCHITECTURE.md
