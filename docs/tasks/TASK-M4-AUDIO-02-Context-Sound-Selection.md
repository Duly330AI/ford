# TASK-M4-AUDIO-02: Context Sound Selection

**Milestone:** M4 - Nodes, Berufe & Crafting
**Priority:** P1 (Medium)
**Estimated Effort:** 3-4d
**Dependencies:** TASK-M4-AUDIO-01-Audio-Mixer-Engine, TASK-M1-GEN-01-Biome-System, TASK-M3-GEN-01-Threat-Budget-Spawner

## Objectives

- Implement rule system mapping gameplay context (floor tags, biome, faction, weather) to sound events per SOUND_DESIGN.md.
- Support variant pools and randomization with seeded RNG for deterministic playback sequences.
- Integrate with biome/room tags to choose footsteps, ambient loops, and encounter cues dynamically.
- Provide data-driven configuration (`audio/sounds.json`) with schema enforcing categories, variants, and weightings.
- Add tests verifying rule resolution for multiple scenarios and deterministic variant selection.

## Acceptance Criteria

- Sound selection picks appropriate variants based on room tags and biome metadata with consistent results for given seeds.
- Data validation catches missing assets, invalid categories, or conflicting rules at startup.
- Systems publish sound intents to mixer without referencing raw file paths directly.
- Tests simulate multi-context transitions (overworld -> combat -> UI) ensuring correct rule application.
- Documentation describes configuration format and how to extend sound pools.

## Implementation Notes

- Design rule evaluation to short-circuit efficiently and support priority overrides.
- Provide fallbacks when specific combo not defined (e.g., default footsteps) while logging for designers.
- Keep rule engine decoupled from scenes; deliver results as mixer events plus metadata.
- Coordinate with debug tools to visualize active audio rules when diagnosing mixes.

## Related Documents

- docs/SOUND_DESIGN.md
- docs/DUNGEON_GENERATOR.md
- docs/CONVENTIONS.md
- docs/TODO/SOUND_DESIGN_TD.md
