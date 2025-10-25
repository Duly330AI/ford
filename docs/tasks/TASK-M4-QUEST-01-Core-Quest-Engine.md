- [ ] ID: TASK-M4-QUEST-01
  Title: Core Quest Engine (FSM, Objectives, Progress Tracking)
  Status: Proposed
  Priority: P0
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `game/systems/quest_engine.py`, `tests/systems/test_quest_engine.py`
  DependsOn: TASK-M2-04, TASK-M3-03, TASK-M4-15
  Notes:
  Implementiere QuestEngine FSM: Offered → Active → Succeeded/Failed/Cancelled. Objective-Progress via Events (Kill, Collect, UseItem, Location, Time) deterministic. APIs: Accept, Update, Complete, Abandon Quests, Emit Outcome-Events für UI/Save. Multi-Step Objectives mit Dependencies & Timers. Deterministic per Seed. No Arcade-Deps. Headless Testable. Event-Hooks via Adapter-Interface. Instrumentation/Logging für Debug.
  Acceptance:
  - [ ] Quest-Engine processes Event-Payloads, Updates Objectives per QUEST_SYSTEM.md.
  - [ ] State-Transitions enforce Requirements (Level, Skills), Trigger Journal-Entries (Localization-Keys).
  - [ ] Query-APIs für UI: Active-Quests, Objective-Status.
  - [ ] Save/Load-Integration Plan (TASK-M5-01), Serialization-Hooks implemented.
  - [ ] Tests: Progression-Paths, Branching-Objectives, Failure-Conditions, Restart, Seeded-RNG.
  Tests:
  - [ ] **FSM-Test**: State-Transitions korrekt (Offered → Active → Succeeded).
  - [ ] **Objective-Update-Test**: Events triggern Objective-Progress.
  - [ ] **Query-API-Test**: Active-Quests, Status abfragbar.
  - [ ] **Determinismus-Test**: gleicher Seed → identische Quest-Progression.
  References:
  - docs/QUEST_SYSTEM.md
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
