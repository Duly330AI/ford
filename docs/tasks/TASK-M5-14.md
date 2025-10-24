- [ ] ID: TASK-M5-14
  Title: Performance Benchmark (Dump + Write < 50 ms)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `tests/perf/test_save_perf.py`
  DependsOn: TASK-M5-02, TASK-M5-04
  Notes:
  Messtypischer Save (Inventar <=200 Stacks, 2 000 Nodes, Crafting Queues). Budget: Dump + Atomic Write < 50 ms; Groesse JSON-gzip < 200 KB.
  Acceptance:
  - [ ] Benchmark unter Budget auf CI Hardware.
  - [ ] Profil-Ausgabe dokumentiert (stdout/Log).
  Tests:
  - [ ] pytest mark perf fuer Save-Benchmark.
  - [ ] Optionaler slow mark fuer Stress-Run.
