- [ ] ID: TASK-M2-LOS-11-Sight-Range
  Title: Sichtlinie (LOS) & Reichweitenpruefung
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/util/los.py`, `tests/util/test_los.py`
  DependsOn: -
  Notes:
  Grid-basierter Bresenham-Ray; beruecksichtigt `walls`/`light-blockers`.
  Acceptance:
  - [ ] True/False fuer Paare von Zellen, Kantenfaelle (Diagonalen).
  Tests:
  - [ ] Wand-Block, Ecke, offener Raum, langer Korridor.
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
