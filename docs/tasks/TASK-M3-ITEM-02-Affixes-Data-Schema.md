- [ ] ID: TASK-M3-ITEM-02-Affixes-Data-Schema
  Title: Affixes Data Schema & Loader
  Status: Proposed
  Priority: P0
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `data/affixes.json`, `data/schemas/affixes.schema.json`, `game/data_loader/affixes.py`, `tests/data/test_affixes.py`
  DependsOn: TASK-M3-01, TASK-M3-ITEM-01
  Notes:
  Definiere `data/affixes.json`: Prefix/Suffix-Defs, Slot-Restrictions, Budget-Costs, Stat-Ranges, Conflicts. Schema `data/schemas/affixes.schema.json` validiert Struktur, Slot-Enums, Numeric-Ranges, Conflict-Refs. Loader: Efficient Lookup (by Slot, Rarity, Biom), Caching. Content-Validation: Refs zu Stats/Modifiers align mit Combat/Economy-Rules. Localization-Keys für Display. Support Weighting-Fields für Biom/Fraktions-Adjustments.
  Acceptance:
  - [ ] Affix-Defs validieren bei Startup, Invalid entries → descriptive Errors.
  - [ ] Loader exponiert API für Generator: Fetch Eligible Affixes by Slot/Rarity mit Deterministic Ordering.
  - [ ] Data-Struktur supports Localization-Keys, kein User-Text in JSON.
  - [ ] Tests: Positive Fixture + Invalid Scenarios (Schema & Logical Validation).
  - [ ] Doku: Example-Affixes, Designer-Guidance.
  Tests:
  - [ ] **Schema-Validation-Test**: Invalid Affixes → Errors.
  - [ ] **Stat-Reference-Test**: Stat-Names canonical in combat_rules.json.
  - [ ] **Conflict-Reference-Test**: Conflict-IDs exist.
  - [ ] **Loader-Efficiency-Test**: Caching works, Lookup deterministic.
  References:
  - docs/ITEMIZATION_DESIGN.md
  - docs/CONVENTIONS.md
  - docs/ARCHITECTURE.md
