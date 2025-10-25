# TASK-M4-QUEST-02: Quest Data Schema & Loader

**Milestone:** M4 - Nodes, Berufe & Crafting
**Priority:** P0 (High)
**Estimated Effort:** 3-4d
**Dependencies:** TASK-M3-01, TASK-M4-QUEST-01-Core-Quest-Engine

## Objectives

- Define quest data structure under `data/quests/*.json` capturing requirements, objectives, rewards, hooks, and localization keys.
- Create schema `data/schemas/quest.schema.json` ensuring field validation, objective types, references (items, mobs, locations).
- Implement loader module to validate, normalize, and supply quest definitions to quest engine.
- Provide tooling/tests detecting duplicate IDs, invalid hook combinations, and missing localization keys.
- Document workflow for adding new quests including recommended directory structure and naming.

## Acceptance Criteria

- Quest files validate during startup; schema errors pinpoint offending fields/paths.
- Loader exposes iteration and retrieval APIs (by ID, by giver NPC, by biome) supporting gameplay queries.
- Objective references verified against existing data (items, mobs, tiles), preventing runtime mismatches.
- Tests include positive fixtures and multiple negative cases (bad reward type, invalid objective count, missing hook target).
- Documentation updated to include sample quest JSON aligned with localization conventions.

## Implementation Notes

- Support modular quest packages (tutorial, factions) by allowing subdirectories under `data/quests/` with shared schema.
- Provide optional metadata fields for prerequisites (reputation, quest chains) to support future expansions.
- Integrate schema validation with existing tooling to run in CI/pre-commit.
- Expose helper to map quest localization keys for use in UI/tut overlay tasks.

## Related Documents

- docs/QUEST_SYSTEM.md
- docs/LOCALIZATION.md
- docs/CONVENTIONS.md
- docs/TODO/QUEST_SYSTEM_TD.md
