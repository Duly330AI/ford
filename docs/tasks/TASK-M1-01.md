- [ ] ID: TASK-M1-01
  Title: BSP-Dungeon-Generator (Räume, Korridore, Seed)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/util/bsp.py`, `game/util/grid.py`, `tests/util/test_bsp.py`
  DependsOn: —
  Notes:
  Implementiere rekursives BSP mit konfigurierbaren Parametern (Dungeon-Breite/Höhe in Tiles, min/max Raumgröße, Korridorbreite). Output ist ein **reines Grid-Modell** (Enum/Int für `WALL`, `FLOOR`). RNG via injizierbarem `random.Random(seed)`.
  Acceptance:
  - [ ] Für N=100 Seeds ist der erzeugte Dungeon **zusammenhängend** (mind. ein Pfad zwischen allen Räumen).
  - [ ] Räume erfüllen min/max Grenzen; Korridore verbinden Raumzentren ohne Diagonallücken.
  - [ ] Laufzeit für 128×128 Tiles < 50 ms (Durchschnitt über 100 Läufe auf CI).
  Tests:
  - [ ] **Connectivity-Test**: Graph aus begehbaren Zellen ist 1-komponentig.
  - [ ] **Property-Tests** (optional Hypothesis): Raumgrößen, Korridorbreiten in Bounds.
  - [ ] **Determinismus-Test**: gleicher Seed → identisches Grid.
