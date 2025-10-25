- [ ] ID: TASK-M1-GEN-01
  Title: Biome System Foundation
  Status: Proposed
  Priority: P0
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `game/systems/biome_manager.py`, `data/schemas/biome.schema.json`, `data/biomes/*.json`, `tests/systems/test_biome_manager.py`
  DependsOn: TASK-M1-01, TASK-M1-11, TASK-M2-07
  Notes:
  Implementiere `BiomeManager` zur Verwaltung datengestützter Biom-Konfigurationen. Jedes Biom definiert: Tileset-ID, Fraktions-Gewichte, Loot-Tabellen, Reagenzien-Vorkommen, Ambiente (Musik, Beleuchtung). Biome werden bei Dungeon-Generierung ausgewählt (seed-deterministisch) und beeinflussen BSP-Output, Gegner-Spawning und Umwelteigenschaften. JSON-Schema validiert Struktur und Cross-File-Referenzen. Manager bleibt testbar (keine Arcade-Deps).
  Acceptance:
  - [ ] `BiomeManager.load()` parsed `data/biomes/*.json`, validiert gegen Schema, gibt strukturierte Daten zurück.
  - [ ] Biom-Auswahl und Tileset-Anwendung sind deterministisch pro Seed.
  - [ ] Schema-Fehler (fehlende Felder, ungültige Refs) werden früh geworfen mit aussagekräftigen Meldungen.
  - [ ] API verfügbar: `get_biome()`, `get_tileset()`, `get_faction_weights()`, `get_ambient_tags()`.
  - [ ] Dungeon-Metadaten (Biom-ID) persistieren über Save/Load.
  Tests:
  - [ ] **Load-Test**: Sample-Biom-Defs laden, validieren, abfragen.
  - [ ] **Schema-Validation**: Ungültige Configs → Fehler mit Zeile/Feld.
  - [ ] **Integration-Test**: Biom + BSP-Generator erzeugen konsistente Dungeons pro Seed.
  - [ ] **Determinismus-Test**: gleicher Seed + Biom → identische Tileset-Anwendung.
  References:
  - docs/DUNGEON_GENERATOR.md
  - docs/WORLD_BIBLE.md
  - docs/CONVENTIONS.md
