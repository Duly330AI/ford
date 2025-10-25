- [ ] ID: TASK-M2-24
  Title: Monster AI Field Mapping Extension (Extend M2-07 with ai/faction Fields)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: $_, $_, $_
  DependsOn: TASK-M2-07, TASK-M2-AI-03, TASK-M2-AI-04
  Notes:
  Augment monsters.json with AI metadata (ai archetype, faction id, optional ai_tags, ai_overworld, ai_combat) per AI_DESIGN.md Section 7.
  Populate existing monster entries with ai and faction fields and map archetypes to behaviors.json entries.
  Extend enemies.py to load new fields and expose them to tactics/faction systems.
  Cross-reference CROSS_REFERENCE_ANALYSIS.md Section 18 to ensure schema alignment and integration pathways.
  Acceptance:
  - [ ] `monsters.json` entries include ai and faction fields with validated values.
  - [ ] Schema or validation ensures ai_tags, ai_overworld, ai_combat follow expected shapes.
  - [ ] Enemies loader attaches AI metadata for use by tactics and faction systems.
  - [ ] Integration tests confirm AI archetype informs behavior selection.
  Tests:
  - [ ] tests/systems/test_enemies.py::test_monster_ai_fields_loaded
  - [ ] tests/systems/test_enemies.py::test_monster_ai_schema_validation
  - [ ] tests/systems/test_enemies.py::test_behavior_mapping_integration
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
  - docs/DUNGEON_GENERATOR.md
