- [ ] ID: TASK-M3-ITEM-01
  Title: Affix Generator (Budget-Based ARPG Generation)
  Status: Proposed
  Priority: P0
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `game/systems/affix_generator.py`, `tests/systems/test_affix_generator.py`
  DependsOn: TASK-M3-02, TASK-M3-08, TASK-M2-07
  Notes:
  Implementiere Budget-based Affix-Generator per ITEMIZATION_DESIGN.md: Rarity-Roll, Affix-Slot-Allocation, Budget-Enforcement, Deterministic RNG. Composable Steps: Roll-Rarity → Allocate-Budget → Pick-Affixes → Finalize. Biom/Fraktions/Item-Tag Bias via Data-Weights. Hooks für Preview vs Commit Flows. Conflict-Resolution (Quick vs Weighted) per Data. Seeded RNG für Reproducibility.
  Acceptance:
  - [ ] Generated Items respektieren Budget per Rarity, nie Überschreitung von Cost/Slot-Limits.
  - [ ] Affix-Conflicts resolved per Data, Duplicates avoided wenn nicht permitted.
  - [ ] RNG-Seeding yields Repeatable Items pro Seed.
  - [ ] APIs für Preview vs Commit (e.g. UI Preview vor Purchase).
  - [ ] Tests: Rarity-Tiers, Budget-Compliance, Conflict-Handling, Determinismus.
  Tests:
  - [ ] **Budget-Enforcement-Test**: Affixes never exceed Budget per Rarity.
  - [ ] **Conflict-Resolution-Test**: Quick vs Weighted korrekt resolved.
  - [ ] **Determinismus-Test**: gleicher Seed → identische Affixes.
  - [ ] **Bias-Pool-Test**: Biom-Weights beeinflussen Affix-Selection.
  References:
  - docs/ITEMIZATION_DESIGN.md
  - docs/CONVENTIONS.md
  - docs/ARCHITECTURE.md
