- [ ] ID: TASK-M2-08
  Title: Pfadfindung (A*, Kostenfelder, "keep distance")
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/util/pathfinding.py`, `tests/util/test_pathfinding.py`
  DependsOn: TASK-M2-06
  Notes:
  Gitter-A* (4/8-neighbor konfigurierbar), Kostenfelder (z. B. Vermeide Licht/Engstellen optional), "kitedistance" Heuristik.
  Acceptance:
  - [ ] Pfad existiert, wenn Zellen verbunden; Kosten respektiert.
  Tests:
  - [ ] Korridor-/Eckenfaelle; Distanzhaltung fuer Ranged-KI.
