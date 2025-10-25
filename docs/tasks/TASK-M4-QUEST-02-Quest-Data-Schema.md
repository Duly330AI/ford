- [ ] ID: TASK-M4-QUEST-02
  Title: Quest Data Schema & Loader
  Status: Proposed
  Priority: P0
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `data/quests/*.json`, `data/schemas/quest.schema.json`, `game/data_loader/quests.py`, `tests/data/test_quests.py`
  DependsOn: TASK-M3-01, TASK-M4-QUEST-01
  Notes:
  Definiere `data/quests/*.json`: Requirements, Objectives, Rewards, Hooks, Localization-Keys. Schema `data/schemas/quest.schema.json` validiert Felder, Objective-Types, Refs (Items, Mobs, Locations). Loader validiert, normalizediert, supplies Quest-Defs. Modular Quest-Packages (Tutorial, Factions) via Subdirs. Duplicate-ID-Detection, Invalid-Hook-Validation, Missing-Localization-Key-Detection. Metadata für Prerequisites (Reputation, Quest-Chains) Future-Ready.
  Acceptance:
  - [ ] Quest-Files validieren bei Startup, Schema-Errors pinpoint Offending-Fields.
  - [ ] Loader exponiert Iteration & Retrieval-APIs (by ID, by NPC, by Biom).
  - [ ] Objective-Refs verified gegen Items/Mobs/Tiles, no Runtime-Mismatches.
  - [ ] Tests: Positive Fixtures + Negatives (Bad Reward, Invalid Objective-Count, Missing Hook).
  - [ ] Doku: Sample-Quest-JSON, Localization-Conventions.
  Tests:
  - [ ] **Schema-Validation-Test**: Invalid Quests → Errors.
  - [ ] **Objective-Reference-Test**: Objective-Refs exist in Data.
  - [ ] **Reward-Type-Test**: Reward-Types valid.
  - [ ] **Loader-API-Test**: By-ID, By-NPC, By-Biom Retrieval works.
  References:
  - docs/QUEST_SYSTEM.md
  - docs/LOCALIZATION.md
  - docs/CONVENTIONS.md
