- [ ] ID: TASK-M7-FTUE-05-Tutorial-Content-Data
  Title: Tutorial Content Data (Quests, NPCs, Dialogue, Loot)
  Status: Proposed
  Priority: P1
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `data/tutorial_quests.json`, `data/abbey_npcs.json`, `data/tutorial_dialogue/*.json`, `data/schemas/tutorial_*.schema.json`
  DependsOn: TASK-M7-FTUE-02, TASK-M4-QUEST-02, TASK-M3-02
  Notes:
  Erstelle Tutorial-Data-Files: `data/tutorial_quests.json`, `data/abbey_npcs.json`, Dialogue-Scripts aligned mit Quest & Localization-Schemas. Tutorial-spezifische Loot-Tables, Encounters, Item-Presets. Canonical-ID-Refs (Skills, Items, Locations), Event-Scripts Integration. Schema-Validation. Localized Strings via i18n-Keys (Phase 9 Ready) mit Fallback-Copy. WORLD_BIBLE Faction-Alignment. Gating-Flags: Tutorial-Content disabled nach Completion/Skip.
  Acceptance:
  - [ ] Tutorial-Quests load via Quest-Loader, Drive Tutorial-Manager-Objectives.
  - [ ] Abbey-NPCs haben Dialogue-Keys via i18n mit Fallback-Copy.
  - [ ] Content-Data passes Validation, Integriert mit Scripted-Events.
  - [ ] Tests: Tutorial-Data leaks nicht in Main-Game außer Tutorial-Active.
  - [ ] Doku: Tutorial-Data-Files-List, Update-Instructions.
  Tests:
  - [ ] **Load-Test**: Tutorial-Quests & NPCs laden korrekt.
  - [ ] **Reference-Test**: Item/Location-Refs exist in Data.
  - [ ] **Gating-Test**: Tutorial-Content disabled nach Completion.
  - [ ] **Localization-Ready-Test**: Localization-Keys accessible.
  References:
  - docs/TUTORIAL_FTUE.md
  - docs/QUEST_SYSTEM.md
  - docs/WORLD_BIBLE.md
  - docs/LOCALIZATION.md
