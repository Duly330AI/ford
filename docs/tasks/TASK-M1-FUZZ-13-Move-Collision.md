- [ ] ID: TASK-M1-13
  Title: Movement-/Collision-Fuzz-Tests (stabilitätsfokus)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Artifacts: `tests/fuzz/test_move_collision_fuzz.py`
  DependsOn: TASK-M1-04, TASK-M1-05
  Notes:
  Randomisierte Sequenzen aus Input-Vektoren gegen enge Geometrien (Korridore 1–2 Tiles, Ecken).
  Acceptance:
  - [ ] Keine Exceptions/NaNs; keine Penetration nach 10k Schritten.
  Tests:
  - [ ] Fuzz-Suite (seeded).
  References:
  - docs/CONVENTIONS.md
  - docs/ARCHITECTURE.md
