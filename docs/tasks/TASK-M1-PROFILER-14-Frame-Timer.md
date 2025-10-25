- [ ] ID: TASK-M1-PROFILER-14-Frame-Timer
  Title: Frame-Timer & Micro-Profiler (ohne GL)
  Status: Proposed
  Priority: P2
  Owner: Copilot Agent
  Created: 2025-10-26
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
