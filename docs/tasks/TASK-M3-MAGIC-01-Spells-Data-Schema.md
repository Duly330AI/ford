- [ ] ID: TASK-M3-MAGIC-01-Spells-Data-Schema
  Title: Spells Data Schema & Loader
  Status: Proposed
  Priority: P0
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `data/spells.json`, `data/schemas/spells.schema.json`, `game/data_loader/spells.py`, `tests/data/test_spells.py`
  DependsOn: TASK-M3-01, TASK-M2-MAGIC-01
  Notes:
  Definiere `data/spells.json` Struktur: Cost, Circles, Effects, Fizzle, Resist, AI-Tags per MAGIC_SYSTEM.md. JSON-Schema `data/schemas/spells.schema.json` für ID, Numeric-Bounds, Nested-Objects. Loader `game/data_loader/spells.py` validiert bei Startup, exposes typed Records. Schema-driven Tests. Link zu `combat_rules.json` Parametern (Fizzle-Clamp, Resist-Scales) dokumentiert.
  Acceptance:
  - [ ] `data/spells.json` validiert gegen Schema bei Preflight, Fehler bricht Game-Start ab.
  - [ ] Loader bietet deterministische Ordering, cached Spell-Definitions für Combat/Magic.
  - [ ] Schema enforced Reagent-IDs aus `data/items.json`, Skill-Refs aus `data/skills.json`.
  - [ ] Tests: Positive Fixture, Negative Fixtures (fehlende Costs, invalid Circle, Duplicate ID).
  - [ ] Doku: Wie neue Spells via JSON ohne Code-Changes hinzufügen.
  Tests:
  - [ ] **Schema-Validation-Test**: Ungültige Defs → descriptive Errors.
  - [ ] **Reagent-Reference-Test**: Reagent-IDs existieren in items.json.
  - [ ] **Skill-Reference-Test**: Skill-IDs existieren in skills.json.
  - [ ] **Circle-Bounds-Test**: Circle 1-8, numeric Bounds korrekt.
  References:
  - docs/MAGIC_SYSTEM.md
  - docs/CONVENTIONS.md
  - docs/ARCHITECTURE.md
