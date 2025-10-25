- [ ] ID: TASK-M4-ECON-02-Vendor-Data-Schema
  Title: Vendor Data Schema & Loader
  Status: Proposed
  Priority: P0
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `data/vendors/*.json`, `data/schemas/vendor.schema.json`, `game/data_loader/vendors.py`, `tests/data/test_vendors.py`
  DependsOn: TASK-M3-01, TASK-M4-ECON-01
  Notes:
  Definiere `data/vendors/*.json`: Inventory-Ranges, Restock-Cadence, Modifiers, Biom-Affinitäten. Schema `data/schemas/vendor.schema.json` enforced Item-Refs, Numeric-Bounds, Optional-Requirements (Reputation, Milestones). Loader API: Lookup pro Biom/Vendor, Validation bei Startup. Localization-Keys für Display-Names (CONVENTIONS). Vendor-IDs aligned mit WORLD_BIBLE für Quest-Integration.
  Acceptance:
  - [ ] Vendor-Defs validieren, Fehler descriptive für Missing/Incorrect Fields.
  - [ ] Loader cached Records, convenient Methods (list_vendors_for_biome, etc).
  - [ ] Economy-System liest Vendor-Modifiers, Inventory-Defs, Restock-Timers via Loader-API.
  - [ ] Tests: Multi-Biom-Vendors, Specialty-Shops, Vendor-Modifiers.
  - [ ] Doku/Sample-JSON für Designer.
  Tests:
  - [ ] **Schema-Validation-Test**: Invalid Vendors → Errors.
  - [ ] **Item-Reference-Test**: Item-IDs existieren in items.json.
  - [ ] **Biom-Affinity-Test**: Vendor-Biom-Refs valid.
  References:
  - docs/ECONOMY_AND_VENDORS.md
  - docs/CONVENTIONS.md
  - docs/WORLD_BIBLE.md
