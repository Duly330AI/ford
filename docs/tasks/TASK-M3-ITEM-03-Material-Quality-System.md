- [ ] ID: TASK-M3-ITEM-03-Material-Quality-System
  Title: Material & Quality System (Modifier Pipeline)
  Status: Proposed
  Priority: P0
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `data/materials.json`, `data/quality.json`, `data/schemas/materials.schema.json`, `data/schemas/quality.schema.json`, `game/systems/material_quality.py`, `tests/systems/test_materials.py`
  DependsOn: TASK-M3-02, TASK-M4-02, TASK-M3-ITEM-01
  Notes:
  Implementiere Material-Tiers (Iron, Bronze, Verite, Valorite) & Quality-States (Worn, Fine, Masterwork) als Data-driven Modifiers. Extend Item-Model: Material/Quality-IDs referenzieren, Stat-Adjustments runtime applizieren. Data: `data/materials.json`, `data/quality.json` mit Schemas. Composable Modifier-Pipeline (no Duplication). Integrate: Crafting-Outputs, Loot-Generation, Economy-Pricing. Clamping-Rules respektiert. Save/Load persistent. Backward-Compat mit bestehenden Items.
  Acceptance:
  - [ ] Items reflect correct Base-Stats adjustiert von Material + Quality Data, keine Hardcodes.
  - [ ] Crafting & Loot-Pipelines können Specific Materials/Qualities request, Deterministic Results.
  - [ ] Economy-Pricing consumiert Quality-Modifiers from Data, Auto-Adjust Sell/Buy Values.
  - [ ] Tests: Modifier-Stacking, Crafting-Transitions (Repair/Upgrade), Data-Validation, Clamping.
  - [ ] Doku: Material/Quality Format, Integration-Points.
  Tests:
  - [ ] **Modifier-Pipeline-Test**: Material + Quality Modifiers stacked korrekt.
  - [ ] **Crafting-Transition-Test**: Repair/Upgrade appliziert Modifiers korrekt.
  - [ ] **Save-Load-Test**: Material & Quality Attrs persistent.
  - [ ] **Determinismus-Test**: gleicher Seed → identische Modified Stats.
  References:
  - docs/ITEMIZATION_DESIGN.md
  - docs/ECONOMY_AND_VENDORS.md
  - docs/CONVENTIONS.md
