- [ ] ID: TASK-M1
  Title: M1 — Prozeduraler Dungeon, Spielerbewegung & Licht
  Status: Proposed
  Milestone: M1
  Created: 2025-10-24
  Notes: Implement BSP-based dungeon generation, collision for walls, player movement with dt and camera + light layer.
  Artifacts:
  - `game/main.py` (bootstrap)
  - `game/scenes/dungeon.py`
  - `game/util/tilemap.py`
  - `game/util/lighting.py`
  Acceptance:
  - [ ] BSP generator produces rooms+corridors saved to `data/maps/*.tmx` or an in-memory TileMap
  - [ ] Player moves 8-way using dt; collisions with walls (AABB) block movement
  - [ ] Camera follows player and light (torch) renders via Arcade lights
  - [ ] 60 FPS sustained at 1280×720 for a mid-size test map

  Subtasks:
  - [ ] Implement BSP dungeon generator (unit test: map connectivity)
  - [ ] Implement TileMap <-> Arcade TileLayer adapter
  - [ ] Player movement system (dt-based) + wall collisions
  - [ ] Light layer around player (torch) using Arcade lights
