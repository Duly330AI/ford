- [ ] ID: TASK-M5-08
  Title: Autosave Scheduler & Rate Limiter
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/util/autosave.py`, `tests/util/test_autosave.py`
  DependsOn: TASK-M5-07
  Notes:
  Trigger: Raumwechsel, Craft-Job Abschluss, Boss/Elite Kill, seltenes Item. Rate-Limit (>=30 s) und Debounce. Integration in Game-Loop.
  Acceptance:
  - [ ] Autosave feuert nur bei erlaubten Events und Respektiert Rate-Limit.
  - [ ] Scheduler pausiert im Combat oder waehrend Save-Lock.
  Tests:
  - [ ] Fake-Clock Tests (advance time) fuer Rate-Limit.
  - [ ] Event-Reihenfolge (mehrere Trigger) erzeugt max 1 Autosave.
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
  - docs/QUEST_SYSTEM.md
