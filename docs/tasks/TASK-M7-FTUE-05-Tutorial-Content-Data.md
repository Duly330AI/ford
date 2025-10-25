# TASK-M7-FTUE-05: Tutorial Content Data

**Milestone:** M7 - First Time User Experience
**Priority:** P1 (Medium)
**Estimated Effort:** 3-4d
**Dependencies:** TASK-M7-FTUE-02-Tutorial-Manager, TASK-M4-QUEST-02, TASK-M3-02

## Objectives

- Create tutorial-specific data files (`data/tutorial_quests.json`, `data/abbey_npcs.json`, dialogue scripts) aligned with quest and localization schemas.
- Define dedicated loot tables, encounters, and item presets required for FTUE scenarios.
- Ensure data references canonical IDs (skills, items, locations) and integrate with event scripts.
- Provide schema validation or extend existing ones to cover tutorial datasets.
- Add tests/linters verifying data completeness and cross-reference integrity.

## Acceptance Criteria

- Tutorial quests load via quest loader and drive tutorial manager objectives as designed.
- Abbey NPCs have dialogue keys localized via i18n system (Phase 9 readiness) with fallback copy for development.
- Content data passes validation and integrates with scripted events for deterministic experience.
- Tests confirm tutorial data does not leak into main game progression unless tutorial active.
- Documentation lists tutorial data files and instructions for updating content.

## Implementation Notes

- Store localized strings using keys anticipating localization rollout; include temporary EN placeholders if necessary.
- Align NPC definitions with WORLD_BIBLE factions and art direction for future asset production.
- Provide gating flags in data so tutorial content disabled after completion or when skip selected.
- Coordinate with save schema to record tutorial completion status.

## Related Documents

- docs/TUTORIAL_FTUE.md
- docs/QUEST_SYSTEM.md
- docs/WORLD_BIBLE.md
- docs/TODO/TUTORIAL_FTUE_TD.md
