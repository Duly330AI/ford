- [ ] ID: TASK-M1-COLLISION-04-AABB-System
  Title: AABB-Kollisionen (Wand-Blocking, Slide)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-26
  Artifacts: `game/systems/collision.py`, `tests/systems/test_collision.py`
  DependsOn: TASK-M1-02
  Notes:
  Implementiere effiziente Kollision zwischen Player-AABB und `walls` via Grid-Abtastung (nur umgebende Zellen). Bevorzuge **separate Axis Resolution** (X dann Y) für sauberes „Slide“ an Wänden.
  Acceptance:
  - [ ] Keine Penetration; Slide entlang Wand bei diagonaler Bewegung.
  - [ ] O(T) in betroffenen Nachbar-Tiles, **kein** Full-Map-Scan.
  Tests:
  - [ ] Penetration-Regression (versch. Geschwindigkeiten/Angles).
  - [ ] Kantenfälle: enge Korridore (1 Tile), Ecken (inner/outer).
  References:
  - docs/DUNGEON_GENERATOR.md
  - docs/CONVENTIONS.md
  - docs/ARCHITECTURE.md
