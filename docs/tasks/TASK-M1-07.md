- [ ] ID: TASK-M1-07
  Title: Light-Layer (Fackel um Spieler, Blocker-Layer)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Artifacts: `game/util/lighting.py`, `game/scenes/dungeon.py`, `tests/smoke/test_lighting_import.py`
  DependsOn: TASK-M1-06
  Notes:
  Arcade-Light-System mit einer dynamischen Punktlichtquelle (Fackel). Unterstützung für `light-blockers`-Layer (Wände/Objekte). Intensität/Radius konfigurierbar (z. B. Options-Menü später).
  Acceptance:
  - [ ] Spieler erzeugt Lichtschein, Wände blocken Licht plausibel.
  - [ ] Toggle per Taste `L` (debug) ohne Ruckler.
  Tests:
  - [ ] Modul importierbar ohne GL (keine GL-Seitenwirkungen).
  - [ ] Scene-bezogene Tests `skip` in Headless.
