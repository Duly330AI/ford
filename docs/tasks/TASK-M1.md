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
  Summary: High-level M1 overview. Detailed M1 subtasks were split into `TASK-M1-01.md` .. `TASK-M1-16.md` for clarity and per-task tracking.

  See the detailed subtasks:
  - TASK-M1-01 — BSP-Dungeon-Generator (Räume, Korridore, Seed) (./TASK-M1-01.md)
  - TASK-M1-02 — TileMap-Adapter (Grid → Arcade TileMap/Layers) (./TASK-M1-02.md)
  - TASK-M1-03 — Level-Bootstrap & Scene-Wiring (DungeonScene) (./TASK-M1-03.md)
  - TASK-M1-04 — AABB-Kollisionen (Wand-Blocking, Slide) (./TASK-M1-04.md)
  - TASK-M1-05 — Player-Controller (dt-Bewegung, 8-Wege, Diagonalen clampen) (./TASK-M1-05.md)
  - TASK-M1-06 — Kamera-Follow (Pixel-Perfect, Integer-Offsets) (./TASK-M1-06.md)
  - TASK-M1-07 — Light-Layer (Fackel um Spieler, Blocker-Layer) (./TASK-M1-07.md)
  - TASK-M1-08 — Performance-Budget & Culling (SpriteList) (./TASK-M1-08.md)
  - TASK-M1-09 — Debug-Overlay (F3): FPS, Seed, Room-Count, Coords (./TASK-M1-09.md)
  - TASK-M1-10 — Input-System & Keybinds (WASD/Arrows, R, F3, L) (./TASK-M1-10.md)
  - TASK-M1-11 — Konfiguration & Seeds (INI/JSON + ENV) (./TASK-M1-11.md)
  - TASK-M1-12 — Minimal-Assets & Pixel-Skalierung (16→64 px) (./TASK-M1-12.md)
  - TASK-M1-13 — Movement-/Collision-Fuzz-Tests (stabilitätsfokus) (./TASK-M1-13.md)
  - TASK-M1-14 — Frame-Timer & Micro-Profiler (ohne GL) (./TASK-M1-14.md)
  - TASK-M1-15 — Dokumentation „Wie M1 prüfen“ (README Abschnitt) (./TASK-M1-15.md)
  - TASK-M1-16 — M1-Abnahme: Kriterien & Benchmarks (CI + Lokal) (./TASK-M1-16.md)
