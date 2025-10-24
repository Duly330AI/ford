- [ ] ID: TASK-M2-17
  Title: Mikrobenchmarks Kampf (CI)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `tests/perf/test_combat_bench.py`, `.github/workflows/ci.yml` (Ergaenzung)`
  DependsOn: TASK-M2-04, TASK-M2-09
  Notes:
  1000 Zug-Resolutionen (ohne GL) zeitlich messen.
  Acceptance:
  - [ ] Median < 2 ms pro kompletter Runde (1P+3E) in CI (approx).
  Tests:
  - [ ] TBD
