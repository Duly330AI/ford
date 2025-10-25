# TASK-M1-GEN-03: Debug Tools Extended

**Milestone:** M1 - Prozeduraler Dungeon, Spielerbewegung & Licht
**Priority:** P1 (Critical Support)
**Estimated Effort:** 2-3d
**Dependencies:** TASK-M1-GEN-01-Biome-System, TASK-M3-GEN-01-Threat-Budget-Spawner

## Objectives

- Extend existing debug overlay to add F4 reachability heatmap using current dungeon graph data.
- Implement F5 spawn overlay highlighting mob placements, threat budget totals, and faction distribution.
- Add Ctrl+S map metadata dump exporting dungeon layout, tags, biomes, and spawn records for offline review.
- Ensure tools operate in headless mode (log outputs) for CI diagnostics.
- Update developer documentation describing new shortcuts and expected outputs.

## Acceptance Criteria

- F4 heatmap visualizes reachable tiles with gradient scale; headless mode logs coverage statistics.
- F5 overlay differentiates factions/encounter tiers and displays threat totals per room.
- Ctrl+S dumps deterministic JSON under `saves/runs/{seed}/map.json` including biome/tag/spawn metadata.
- Tools respect performance budgets (<16ms toggling) and can be disabled via config for release builds.
- Tests or smoke checks verify command handlers register and metadata dump structure matches schema.

## Implementation Notes

- Keep debug tooling under scenes/adapters layer, consuming data via biome/spawn manager APIs (no cross-layer leaks).
- Introduce schema for map dump to allow validation and future tooling.
- Include CLI flags or config options to auto-export debug data during automated generation runs.
- Coordinate color palettes with forthcoming art style guide to preserve readability.

## Related Documents

- docs/DUNGEON_GENERATOR.md
- docs/TODO/DUNGEON_GENERATOR_TD.md
- docs/DEVELOPMENT.md
- docs/CONVENTIONS.md
