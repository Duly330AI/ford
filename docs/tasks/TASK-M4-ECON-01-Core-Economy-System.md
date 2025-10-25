- [ ] ID: TASK-M4-ECON-01
  Title: Core Economy System (Price Calculations, Transactions)
  Status: Proposed
  Priority: P0
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `game/systems/economy.py`, `tests/systems/test_economy.py`
  DependsOn: TASK-M3-13, TASK-M3-02, TASK-M4-16
  Notes:
  Implementiere `EconomySystem`: Price-Kalkulationen, Transaction-Handling, Spread-Logik per ECONOMY_AND_VENDORS.md. Formula parameterisiert via `data/economy_rules.json`. APIs: Buy/Sell-Preview, Affordability-Checks, Gold-Sinks (Repairs, Travel). Events für Analytics. Inventory-Adjustments atomar. Tests mit Determinismus über Rarity/Quality/Vendor-Modifiers.
  Acceptance:
  - [ ] Prices matchen Design-Beispiele, Overrides via Data.
  - [ ] Transactions adjustten Player/Vendor-Inventories & Gold-Balances atomar, Rollback on Failure.
  - [ ] Hooks für Vendor-Modifiers & Faction-Reputation (Future-Ready).
  - [ ] Tests: Deterministic Behavior, Seeded RNG.
  - [ ] Doku: Economy-Rules-File, Tuning-Workflow.
  Tests:
  - [ ] **Price-Calculation-Test**: Base *Rarity-Factor* Quality-Mod * Vendor-Modifier korrekt.
  - [ ] **Transaction-Atomicity-Test**: Inventory & Gold zusammen adjustten, oder Rollback.
  - [ ] **Determinismus-Test**: gleicher Seed → identische Prices.
  References:
  - docs/ECONOMY_AND_VENDORS.md
  - docs/CONVENTIONS.md
