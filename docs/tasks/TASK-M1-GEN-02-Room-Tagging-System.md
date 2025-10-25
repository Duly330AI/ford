# TASK-M1-GEN-02: Room Tagging System

**Milestone:** M1 - Prozeduraler Dungeon, Spielerbewegung & Licht
**Priority:** P0 (Critical)
**Estimated Effort:** 4d
**Dependencies:** TASK-M1-01, TASK-M1-GEN-01-Biome-System

## Objectives

- Design heuristic-driven tagging algorithm assigning semantic tags (altar, crypt, market, boss_antechamber, shrine_of_{element}) to generated rooms.
- Provide configuration file (`data/dungeon_tags.json` or within biome definitions) to tune tag weights, minimum room sizes, and distance thresholds.
- Emit tag metadata into dungeon output for consumption by encounter placement, loot distribution, and scripted events.
- Add analytics hooks/tests ensuring tag distribution meets expected ratios over seeded runs.
- Expose CLI or debug utility to visualize tags for designers.

## Acceptance Criteria

- Each generated room carries deterministic tag set based on size, connectivity, depth, and biome configuration.
- Tag assignments remain stable across runs with identical seeds and configuration.
- Systems using tags (spawner, loot, tutorial scripts) can query metadata without direct generator coupling.
- Tests simulate multiple seeds verifying edge cases (minimum room size, branching rooms, boss depth requirements).
- Debug overlay or log output highlights tagged rooms for inspection (toggleable).

## Implementation Notes

- Implement tagging as post-processing step after BSP layout but before spawn pass to keep responsibilities clear.
- Allow multiple tags per room while respecting exclusivity rules defined in config.
- Persist tags in dungeon metadata dump (CTRL+S debug task) for offline analysis.
- Document configuration format to enable content designers to adjust without code changes.

## Related Documents

- docs/DUNGEON_GENERATOR.md
- docs/TODO/DUNGEON_GENERATOR_TD.md
- docs/WORLD_BIBLE.md
- docs/ARCHITECTURE.md
