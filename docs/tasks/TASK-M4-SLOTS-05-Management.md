- [ ] ID: TASK-M4-SLOTS-05-Management
  Title: Node-Spawner (Platzierung, Seeds, Distanzen, Biome)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/util/node_spawn.py`, `tests/util/test_node_spawn.py`
  DependsOn: TASK-M1-01, TASK-M1-02, TASK-M1-03, TASK-M4-04
  Notes:
  Prozedurale Platzierung auf `FLOOR`-Tiles:
        - Regeln: Mindestabstand zw. Nodes gleicher Art, Verbot an Korridorengstellen, optional Biome/Tags (Rooms vs. Corridors).
        - RNG-seeded, reproduzierbar.
  Acceptance:
  - [ ] Dichte/Zaehlung innerhalb konfigurierter Grenzen; keine Blockierung kritischer Durchgaenge.
  Tests:
  - [ ] Distanz-/Dichte-Checks; Wiederholbarkeit mit Seed.
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
  - docs/DUNGEON_GENERATOR.md
