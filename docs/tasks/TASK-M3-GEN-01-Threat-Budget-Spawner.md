- [ ] ID: TASK-M3-GEN-01-Threat-Budget-Spawner
  Title: Threat Budget Spawner (Encounter Loading, Mob Allocation)
  Status: Proposed
  Priority: P0
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `game/systems/spawner.py`, `data/encounters/*.json`, `data/schemas/encounters.schema.json`, `tests/systems/test_spawner.py`
  DependsOn: TASK-M1-GEN-01, TASK-M1-GEN-02, TASK-M2-04
  Notes:
  Implementiere Threat-Budget-Spawner: Encounter-Loader für `data/encounters/*.json` mit Schema-Validierung & Fraktions/Threat-Metadaten. Deterministic Threat-Budget-Algorithm: Mobs pro Room basierend auf Depth, Biom, Tag-Rules. Spawn-Respekt: Fraktions-Weights, Elite/Boss-Probabilities, Environmental-Constraints (LOS, Pathing). Hooks für Scripted-Encounters. Data-Parsing separiert von Allocation-Logik. Biom/Tag-Weights optional (data-driven). Instrumentation für Designer-Tuning.
  Acceptance:
  - [ ] Threat-Budget-Distribution matcht DUNGEON_GENERATOR.md Formulas, Configurable Tolerances, Elite-Probabilities.
  - [ ] Encounter-Tables validiert (Mob-IDs, Required-Skills cross-refs).
  - [ ] Spawn-Placements avoid Unreachable-Tiles, Respekt Room-Tags (Boss-Rooms, Resources).
  - [ ] Seeds produce Consistent Layouts, Integration-Tests capture Golden-Outputs (Regression).
  - [ ] API exposes Spawn-Summaries für Debug-Overlays (F5) & Analytics.
  Tests:
  - [ ] **Budget-Adherence-Test**: Threat-Budget per Room korrekt.
  - [ ] **Depth-Scaling-Test**: Difficulty scales mit Tiefe.
  - [ ] **Biom-Override-Test**: Biom-Specific Rules applied.
  - [ ] **Determinismus-Test**: gleicher Seed → identische Spawn-Layouts.
  References:
  - docs/DUNGEON_GENERATOR.md
  - docs/WORLD_BIBLE.md
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
