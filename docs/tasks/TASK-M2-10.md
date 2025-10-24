- [ ] ID: TASK-M2-10
  Title: Projektile (Logik, LOS-Treffer, Block an Waenden)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/projectile_logic.py`, `game/entities/projectiles.py`, `tests/systems/test_projectile_logic.py`
  DependsOn: TASK-M2-11, TASK-M2-04
  Notes:
  Logisch "raycast" (Bresenham) ueber Grid; erster Blocker (Wand/Entity) beendet Flug. Scene rendert Animation asynchron **nach** bestaetigtem Outcome.
  Acceptance:
  - [ ] Waende blocken; Treffzelle korrekt; kein Friendly-Fire (vorerst).
  Tests:
  - [ ] Raycast ueber verschiedene Winkel/Korridore; deterministisch.
