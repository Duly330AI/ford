- [ ] ID: TASK-M1-GEN-02-Room-Tagging-System
  Title: Room Tagging System
  Status: Proposed
  Priority: P0
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `game/systems/room_tagger.py`, `data/dungeon_tags.json`, `tests/systems/test_room_tagger.py`
  DependsOn: TASK-M1-01, TASK-M1-GEN-01
  Notes:
  Implementiere heuristic-driven Tagging-Algorithm: Jeder Raum erhält semantic Tags (altar, crypt, market, boss_antechamber, shrine_of_*) basierend auf Size, Connectivity, Depth, Biom-Config. Post-Processing nach BSP, vor Spawn-Pass. Multi-Tags möglich mit Exclusivity-Rules. Tags in Dungeon-Metadaten persistent. Config data-driven, Designer können anpassen ohne Code.
  Acceptance:
  - [ ] Jeder Raum hat deterministen Tag-Set pro Seed & Config.
  - [ ] Tag-Assignments stabil über Runs mit identischem Seed.
  - [ ] Systems (Spawner, Loot, Tutorial) können Tags abfragen ohne Generator-Coupling.
  - [ ] Tests: Multiple Seeds, Edge-Cases (Min-Room-Size, Branching, Boss-Depth).
  - [ ] Debug-Overlay zeigt getaggte Räume (togglebar).
  Tests:
  - [ ] **Tagging-Determinismus-Test**: gleicher Seed → identische Tags.
  - [ ] **Tag-Config-Test**: Config-Änderungen reflektieren korrekt.
  - [ ] **Edge-Case-Test**: Min-Room-Size, Boss-Depth-Requirements beachtet.
  - [ ] **Multi-Tag-Test**: Räume mit mehreren Tags, Exclusivity enforced.
  References:
  - docs/DUNGEON_GENERATOR.md
  - docs/WORLD_BIBLE.md
  - docs/ARCHITECTURE.md
