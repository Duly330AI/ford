- [ ] ID: TASK-M4-13
  Title: Performance: 2 000 Nodes Tick/Respawn + Gather-Load
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `tests/perf/test_nodes_perf.py`
  DependsOn: TASK-M4-04, TASK-M4-05, TASK-M4-06
  Notes:
  Messen: `tick_all_nodes(dt)` + sporadische `gather` Aufrufe.
  Acceptance:
  - [ ] 2 000 Nodes Verwaltung < 1 ms reine Logik (CI-Richtwert).
  Tests:
  - [ ] TBD
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
