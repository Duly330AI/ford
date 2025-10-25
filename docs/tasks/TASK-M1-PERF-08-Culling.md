- [ ] ID: TASK-M1-08
  Title: Performance-Budget & Culling (SpriteList)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Artifacts: `game/util/perf.py`, `tests/perf/test_spawn_2000_entities.py`
  DependsOn: TASK-M1-03
  Notes:
  Naives Culling: render-nahe Sprites anhand Kamera-Viewport + Margin. SpriteLists pro Layer.
  Acceptance:
  - [ ] Test-Map mit 2000 Deko-Entities bleibt ≥ **60 FPS Feel** bei 1280×720 auf Referenz-Maschine (lokal; CI misst nur Ticks/Loops).
  - [ ] CPU-Zeit pro Frame für Culling < 2 ms (Mittel über 500 Frames, ohne GL).
  Tests:
  - [ ] Mikro-Benchmark (ohne GL) für Culling-Filter (Zeitbudget).
  References:
  - docs/CONVENTIONS.md
  - docs/ARCHITECTURE.md
