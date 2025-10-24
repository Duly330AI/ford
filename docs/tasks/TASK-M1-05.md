- [ ] ID: TASK-M1-05
  Title: Player-Controller (dt-Bewegung, 8-Wege, Diagonalen clampen)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Artifacts: `game/entities/player.py`, `game/systems/movement.py`, `tests/systems/test_movement.py`
  DependsOn: TASK-M1-04
  Notes:
  Input-Vektor (WASD/Arrows) normalisieren, Diagonal-Geschwindigkeit **clampen** (keine 1.414x). `dt`-basiert mit `min(dt, 1/30)` Clamp. Geschwindigkeit/Accel parametrisierbar.
  Acceptance:
  - [ ] Gleichmäßige Geschwindigkeit in allen Richtungen.
  - [ ] Kein **tunneling** durch dünne Wände (zus. Kollisionsauflösung).
  Tests:
  - [ ] Bewegungs-Invarianten (|v| konstant), Diagonal-Clamp.
  - [ ] Integrations-Test mit Kollision (ohne Arcade).
