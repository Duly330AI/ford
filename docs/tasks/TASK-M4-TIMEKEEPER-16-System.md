- [ ] ID: TASK-M4-TIMEKEEPER-16-System
  Title: Zeit- & Takt-Adapter (Overworld vs. Combat)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/util/timekeeper.py`, `tests/util/test_timekeeper.py`
  DependsOn: TASK-M2-04
  Notes:
  `Timekeeper` liefert `dt_overworld` & pausiert bei Combat (oder skaliert). Crafting tickt nur mit `overworld_active=True`.
  Acceptance:
  - [ ] Pause/Resume ohne Drift (Test mit Fake-Clock).
  Tests:
  - [ ] TBD
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
