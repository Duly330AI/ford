- [ ] ID: TASK-M4-AUDIO-02-Context-Sound-Selection
  Title: Context Sound Selection (Rule Engine, Variants)
  Status: Proposed
  Priority: P1
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `game/audio/sound_rules.py`, `data/sounds.json`, `data/schemas/sounds.schema.json`, `tests/audio/test_sound_rules.py`
  DependsOn: TASK-M4-AUDIO-01, TASK-M1-GEN-01, TASK-M3-GEN-01
  Notes:
  Implementiere Rule-System: Gameplay-Context (Floor-Tags, Biom, Fraktions, Weather) → Sound-Events. Variant-Pools mit Seeded-RNG für Deterministic Playback. Biom/Room-Tags → Footsteps, Ambient-Loops, Encounter-Cues dynamisch. Data-Config `audio/sounds.json` mit Schema. Rule-Evaluation efficient mit Priority-Overrides. Fallbacks bei Missing Combos. Keep Rule-Engine decoupled von Scenes.
  Acceptance:
  - [ ] Sound-Selection picks Appropriate Variants basierend auf Room-Tags/Biom, Consistent per Seed.
  - [ ] Data-Validation catches Missing-Assets, Invalid-Categories, Conflicting-Rules bei Startup.
  - [ ] Systems publish Sound-Intents zu Mixer, no Raw-File-Path-Refs.
  - [ ] Tests: Multi-Context Transitions (Overworld → Combat → UI), Correct Rule-Application.
  - [ ] Doku: Config-Format, Extend Sound-Pools.
  Tests:
  - [ ] **Rule-Resolution-Test**: Rules resolve für Multiple Scenarios.
  - [ ] **Variant-Selection-Test**: Variants deterministisch per Seed.
  - [ ] **Context-Transition-Test**: Rule-Switching bei Context-Changes.
  - [ ] **Fallback-Test**: Missing Combos fallback graceful.
  References:
  - docs/SOUND_DESIGN.md
  - docs/DUNGEON_GENERATOR.md
  - docs/CONVENTIONS.md
