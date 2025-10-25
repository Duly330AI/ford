- [ ] ID: TASK-M7-FTUE-04-Scripted-Events-System
  Title: Scripted Events System (Sequencing, Conditionals, Commands)
  Status: Proposed
  Priority: P1
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `game/tutorial/script_runner.py`, `data/tutorial/scripts/*.json`, `tests/tutorial/test_script_runner.py`
  DependsOn: TASK-M7-FTUE-02, TASK-M4-QUEST-03, TASK-M2-04
  Notes:
  Implementiere Scripted-Event-Runner: Sequencing Actions (Spawn-NPC, Play-Audio, Move-Camera, Trigger-Dialogue). Event-Bus Integration für FTUE-Scenes (Intro-Narration, First-Combat). Data-driven Scripts: `data/tutorial/scripts/*.json` mit Conditionals & Delays. Deterministic unter Seeded-RNG. Commands als Declarative-Steps zu bestehende Systems. Reusable-Macros. Save-Integration für Mid-Flow-Progress. Debug-Tools für Replay/Skip.
  Acceptance:
  - [ ] Script-Runner executes Tutorial-Szenarios in Order (Wake-Up, NPCs, First-Combat).
  - [ ] Scripts pause/resume basierend auf Tutorial-Manager State & Player-Input.
  - [ ] Errors (Missing-Actors, Invalid-Commands) → Descriptive Logs & Safe-Abort.
  - [ ] Tests: Deterministic Ordering, Cleanup nach Completion.
  - [ ] Doku: Script-Authoring-Guide, Available-Commands.
  Tests:
  - [ ] **Sequencing-Test**: Commands execute in Order.
  - [ ] **Conditional-Test**: Branches resolve korrekt.
  - [ ] **Error-Handling-Test**: Invalid Commands → Logs & Abort.
  - [ ] **Determinismus-Test**: gleicher Seed → identische Sequencing.
  References:
  - docs/TUTORIAL_FTUE.md
  - docs/QUEST_SYSTEM.md
  - docs/SOUND_DESIGN.md
  - docs/CONVENTIONS.md
