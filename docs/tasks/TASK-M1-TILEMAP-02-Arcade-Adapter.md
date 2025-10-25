- [ ] ID: TASK-M1-TILEMAP-02-Arcade-Adapter
  Title: TileMap-Adapter (Grid → Arcade TileMap/Layers)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-26
  Artifacts: `game/util/tilemap.py`, `tests/util/test_tilemap_adapter.py`
  DependsOn: TASK-M1-01
  Notes:
  Adapter baut aus dem Grid drei Layer: `ground`, `walls (collidable)`, `decals`. Ermöglicht späteren Austausch durch `.tmx`. **Keine** Arcade-Im-Kern; liefere reine Datenstrukturen + **schlanke Adapter-Fassade**, die die `arcade.TileMap` baut (nur im Scene-Code instanziert).
  Acceptance:
  - [ ] Wände landen in einem **collidable** Layer; ground separiert.
  - [ ] Layer-IDs/Names gem. Projektstandard: `ground`, `walls`, `decals`.
  - [ ] Adapter unterstützt Tile-Size 16 und Scaling-Faktor (z. B. 4× → 64px).
  Tests:
  - [ ] Mapping-Test: WALL/FLOOR richtig aufLayer verteilt.
  - [ ] Kein Arcade-Import in `game/util/tilemap.py`.
  References:
  - docs/DUNGEON_GENERATOR.md
  - docs/CONVENTIONS.md
  - docs/ARCHITECTURE.md
