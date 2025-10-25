# Phase 0 Gap Master Plan

## Gap Overview

| Gap ID | Description | Priority | Target Milestone(s) | Key Dependencies |
|--------|-------------|----------|----------------------|-------------------|
| G1 | Magic system backend (casting, fizzle, resist, spells data) | Critical | M2 Combat Core, M3 Skills | TASK-M2-04, TASK-M3-06, MAGIC_SYSTEM.md |
| G2 | Dungeon biome + themed generation layers | Critical | M1 Dungeon Generator, M3 Encounter Tuning | TASK-M1-01, TASK-M2-07, DUNGEON_GENERATOR.md |
| G3 | Economy & vendor pricing/restock systems | High | M4 Crafting & Nodes, future M6 UI | TASK-M3-13, TASK-M6-UI-11 |
| G4 | Procedural itemization (affixes, materials, uniques) | High | M3 Loot systems | TASK-M3-02, TASK-M3-08 |
| G5 | Quest system engine & data | High | Proposed M4 Questline | TASK-M2-04, TASK-M3-03 |
| G6 | Advanced input & rebinding with gamepad | Medium | M1 Input foundation, M6 UI | TASK-M1-10 |
| G7 | Audio mixer & context-aware playback | Medium | M4 Audio hooks | TASK-M4-15 |
| G8 | Tutorial & FTUE systems | Medium | Proposed M7 FTUE | TASK-M5-01, QUEST_SYSTEM tasks |
| G9 | Localization service + tooling + CI | Low | Proposed M8 Localization | CONVENTIONS.md |
| G10 | Art style guide & graphics production standards | Low | Documentation | GRAPHIC_DOC_MISSING_COMPLETLY.md |
| G11 | Biome content alignment with world bible | Low | M1/M3 Biome Content | WORLD_BIBLE.md, DUNGEON_GENERATOR.md |

## Prioritization Summary

- **Critical**: G1, G2 – required to unlock combat/magic depth and themed level generation.
- **High**: G3, G4, G5 – economy, loot, quests form core progression loops once combat + biomes exist.
- **Medium**: G6, G7, G8 – improve usability, audiovisual feedback, onboarding; depend on earlier systems.
- **Low**: G9, G10, G11 – supporting systems/documentation to polish and internationalize content.

## Milestone Mapping & Sequencing

1. **Milestone M2 Extensions** (Magic Core)
   - Implement core casting engine, formulas, and integration before UI hooks (drives TASK-M6-UI-09 readiness).
2. **Milestone M1/M3 Enhancements** (Biomes & Threat Spawning)
   - Layer biome data + threat-based spawns atop BSP generator; prerequisite for faction-themed encounters.
3. **Milestone M4 Economy/Quest Foundations**
   - Economy backend before Merchant UI; quest engine before save/UI extensions.
4. **Milestone M3 Loot Evolution**
   - Procedural itemization leverages existing loot tables; sequence after threat-based spawns for tuned rewards.
5. **Milestone M1 Input Revamp**
   - Context-aware input, controls schema, and gamepad support extend TASK-M1-10 groundwork.
6. **Milestone M4 Audio Mixer**
   - Build mixer + selection logic off existing hooks; ensures data-driven audio.
7. **Milestone M7 FTUE (New)**
   - Tutorial systems rely on quest engine and save schema extensions; define tasks under new milestone.
8. **Milestone M8 Localization (New)**
   - Localization manager and tooling integrate with CONVENTIONS Phase 3 roadmap.
9. **Documentation Deliverables**
   - Art style guide + biome content briefs finalize visual + lore alignment for upcoming assets.

## Dependency Highlights

- Magic backend (G1) must precede UI (TASK-M6-UI-09) and any spell-dependent quests (G5).
- Biome system (G2) feeds encounter tables needed by threat spawner and world bible alignment (G11).
- Economy (G3) requires procedural loot (G4) for meaningful pricing ranges; restock uses Timekeeper (TASK-M4-16).
- Quest engine (G5) depends on event bus work aligned with combat/inventory systems, and informs FTUE content (G8).
- Input overhaul (G6) is prerequisite for rebinding UI (M6) and controller accessibility tests.
- Audio mixer (G7) must exist before UI/audio tasks wire real assets; uses data-driven rule sets from CONVENTIONS.
- Tutorial module (G8) integrates quest engine, save schema updates, and localization keys.
- Localization (G9) underpins UI, quest journal, tutorial prompts; CI tooling ensures parity across languages.
- Art guide (G10) informs asset production for biomes, UI, and tutorial scenes.
- World bible alignment (G11) references biome + encounter tasks to ensure factional consistency in data.
