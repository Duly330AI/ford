- [ ] ID: TASK-M1-03
  Title: Level-Bootstrap & Scene-Wiring (DungeonScene)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Artifacts: `game/main.py`, `game/scenes/dungeon.py`, `tests/smoke/test_boot.py`
  DependsOn: TASK-M1-02
  Notes:
  `main.py` startet Arcade-App, lädt `DungeonScene`, erzeugt per Seed den Dungeon, baut TileMap, und setzt Kamera/Viewport. Provide CLI-Args/ENV (`FORD_SEED`, `FORD_SIZE`), default Seed.
  Acceptance:
  - [ ] `poetry run python -m game.main` startet ohne Fehler.
  - [ ] Seed in Log ausgegeben; Taste `R` regeneriert mit neuem Seed.
  Tests:
  - [ ] Smoke-Test importiert `game.main` (kein GL nötig).
  - [ ] Scene-Init in Headless-CI **skipped** (Marker).
  References:
  - docs/DUNGEON_GENERATOR.md
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
