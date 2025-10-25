- [ ] ID: TASK-M1-14
  Title: Frame-Timer & Micro-Profiler (ohne GL)
  Status: Proposed
  Priority: P2
  Owner: Copilot Agent
  Artifacts: `game/util/prof.py`, `tests/util/test_prof.py`
  DependsOn: TASK-M1-03
  Notes:
  Kontextmanager/Decorator für Timing (BSP, Culling, Collision). Export als rollierende Mittelwerte fürs Debug-Overlay.
  Acceptance:
  - [ ] Messungen in ms; Overhead < 5 µs/Call.
  Tests:
  - [ ] Zeit-Messung mit Fake-Clock (monotonic Mock).
  References:
  - docs/CONVENTIONS.md
  - docs/ARCHITECTURE.md
