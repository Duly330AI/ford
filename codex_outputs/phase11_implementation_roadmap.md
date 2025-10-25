# Phase 11 – Implementation Roadmap

## Suggested Waves

1. **Foundational Data & Validation**
   - TASK-M3-MAGIC-01, TASK-M1-GEN-01, TASK-M1-GEN-02, TASK-M4-ECON-02, TASK-M3-ITEM-02, TASK-M4-QUEST-02, TASK-M1-INPUT-02, TASK-M8-I18N-02
   - Rationale: establish schemas/loaders before system logic to ensure data integrity.

2. **Core Systems**
   - TASK-M2-MAGIC-01, TASK-M2-MAGIC-02, TASK-M2-MAGIC-03
   - TASK-M3-GEN-01, TASK-M1-GEN-03, TASK-M1-GEN-04
   - TASK-M4-ECON-01, TASK-M4-ECON-03
   - TASK-M3-ITEM-01, TASK-M3-ITEM-03, TASK-M3-ITEM-04
   - TASK-M4-QUEST-01, TASK-M4-QUEST-03
   - TASK-M1-INPUT-01, TASK-M1-INPUT-03, TASK-M4-AUDIO-01
   - Outcome: gameplay-critical logic ready for content/UI integration.

3. **Integration & Adapters**
   - Update dependent tasks: TASK-M6-UI-09, TASK-M6-UI-11, TASK-M3-08, TASK-M5-01, TASK-M6-UI-02, TASK-M4-15.
   - Implement context-aware sound rules (TASK-M4-AUDIO-02) and advanced audio features (TASK-M4-AUDIO-03).
   - Introduce localization service (TASK-M8-I18N-01) and connect to UI base (TASK-M6-UI-01).

4. **Tutorial & UX Enhancements**
   - Character creation (TASK-M7-FTUE-01), tutorial manager (TASK-M7-FTUE-02), overlay (TASK-M7-FTUE-03), scripted events (TASK-M7-FTUE-04), tutorial content data (TASK-M7-FTUE-05).
   - Rebinding UI (TASK-M6-UI-INPUT-01) leveraging completed input foundation.
   - Localization CI integration (TASK-M8-I18N-03).

5. **Polish & Documentation**
   - Execute art production guided by docs/ART_STYLE_GUIDE.md.
   - Conduct biome/world alignment pass via TASK-M1-GEN-04 outputs.
   - Finalize debug tooling (TASK-M1-GEN-03) and audio rule QA (TASK-M4-AUDIO-02/03).

## Milestone Sequencing

- **M1 Focus:** Input manager, controls schema, biomes, debug tools.
- **M2 Focus:** Magic backend (core, formulas, cast rounds).
- **M3 Focus:** Itemization systems and threat-based spawning integration.
- **M4 Focus:** Economy, quests, audio mixer.
- **M6 Focus:** UI adaptations (spellbook, merchant, rebinding, HUD quest display).
- **M7 Focus:** Tutorial/FTUE modules once quest engine stable.
- **M8 Focus:** Localization service & CI gating for multi-language readiness.

## Risk Considerations

- Ensure event bus scalability before adding tutorial/quest listeners to prevent bottlenecks.
- Align affix generator balancing with economy pricing to avoid runaway item values.
- Localization key discipline required ahead of implementing tutorial overlay copy.

## Recommended Cadence

- Establish bi-weekly integration checkpoints verifying data schemas, system tests, and UI wiring.
- Lock art palette before large-scale asset production to avoid rework.
- Introduce localization CI step only after base language strings stabilized to prevent churn.
