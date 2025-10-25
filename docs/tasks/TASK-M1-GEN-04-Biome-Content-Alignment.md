# TASK-M1-GEN-04: Biome Content Alignment

**Milestone:** M1 - Prozeduraler Dungeon, Spielerbewegung & Licht
**Priority:** P2 (Low)
**Estimated Effort:** 3d
**Dependencies:** TASK-M1-GEN-01-Biome-System, TASK-M3-GEN-01-Threat-Budget-Spawner, TASK-M3-08

## Objectives

- Curate biome reference documents linking WORLD_BIBLE factions to biome definitions (tiles, encounters, loot tables).
- Audit existing loot/encounter tables, ensuring faction signatures (resources, reagents) match lore expectations.
- Provide checklist and data templates for adding biome-specific props, audio cues, and ambient lighting hooks.
- Document workflow for designers to extend biome content without breaking data schemas.
- Produce sample alignment sheet (one per biome) to guide content production and QA.

## Acceptance Criteria

- Each biome definition cross-references faction IDs, loot tables, and encounter sets aligned with WORLD_BIBLE.md.
- Alignment checklist stored under `docs/biome_guides/` covers assets, loot, audio, and quest seeds.
- Review identifies mismatches (if any) and creates follow-up issues/tasks for remediation.
- Designers can add new biome content by following provided template without additional engineering guidance.
- Documentation updated to reflect interplay between biome system and world bible lore.

## Implementation Notes

- Reuse data from tasks TASK-M1-GEN-01/02 and TASK-M3-GEN-01 to populate alignment tables.
- Consider simple validation script to ensure loot tables assigned to biome factions contain signature items.
- Work closely with narrative design to capture unique biome storytelling hooks for future quests.
- Feed outputs into art style guide reference for visual motif alignment.

## Related Documents

- docs/WORLD_BIBLE.md
- docs/DUNGEON_GENERATOR.md
- docs/TODO/WORLD_BIBLE_TD.md
- docs/ART_STYLE_GUIDE.md
