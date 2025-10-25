# TASK-M1-GEN-01: Biome System Foundation

**Milestone:** M1 - Prozeduraler Dungeon, Spielerbewegung & Licht
**Priority:** P0 (Critical)
**Estimated Effort:** 5-6d
**Dependencies:** TASK-M1-01, TASK-M1-11, TASK-M2-07

## Objectives

- Define data-driven biome configs under `data/biomes/*.json` capturing tileset, factions, loot tables, reagents, ambient settings.
- Create JSON schema `data/schemas/biome.schema.json` validating required fields, cross-file references, and optional overrides.
- Implement `game/systems/biome_manager.py` to load, validate, and provide biome context to dungeon generator and encounter systems.
- Integrate biome selection into BSP generator initialization, including seed persistence and metadata export.
- Provide API for querying biome attributes (tileset, faction weights, ambience) for use in scenes/UI/debug tools.

## Acceptance Criteria

- Dungeon generation accepts biome ID and applies biome-specific tileset + ambient metadata deterministically per seed.
- Schema validation fails fast on missing fields, invalid references (loot tables, factions), or naming violations.
- Biome manager exposes data for spawning (faction weights) and audio/lighting (ambient tags) without coupling to scenes.
- Tests cover loading sample biome definitions, invalid configs, and integration with generator seeding.
- Generated dungeon metadata persists biome ID for save/load and analytics.

## Implementation Notes

- Ensure biome manager remains pure systems-layer logic; provide bridging adapters for scene-specific usage as needed.
- Support inheritance or composition for shared defaults (e.g. base crypt biome) via schema patterns or loader logic.
- Coordinate with encounter/threat spawner task to align faction lists and loot biases.
- Update generator CLI/tooling (if any) to accept biome parameter and emit helpful errors.

## Related Documents

- docs/DUNGEON_GENERATOR.md
- docs/WORLD_BIBLE.md
- docs/CONVENTIONS.md
- docs/TODO/DUNGEON_GENERATOR_TD.md
