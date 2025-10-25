- [ ] ID: TASK-M4-ECON-03
  Title: Vendor Restock Mechanic (Timekeeper Integration)
  Status: Proposed
  Priority: P0
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `game/systems/restock_scheduler.py`, `tests/systems/test_restock.py`
  DependsOn: TASK-M4-16, TASK-M4-ECON-01, TASK-M4-ECON-02
  Notes:
  Implementiere Restock-Scheduler: Timekeeper-Ticks → Vendor-Restock-Timers decrement, Inventory replenish. Vendor-spezifische Restock_Turns & Variance aus Vendor-Data. Vendor-State (Quantities, Timers) persistent in Save. Events notifizieren UI bei Stock-Changes. Deterministic RNG per Vendor für Reproducibility. VendorState Dataclass separiert von statischen Defs. Manual-Restock via Debug-Tools.
  Acceptance:
  - [ ] Vendors replenish Items per Config-Ranges & Cadence, keine Unique-Item-Duplikate.
  - [ ] Restock respektiert Deterministic RNG, Reproducible Inventories.
  - [ ] Save/Load retainiert Restock-Timers & Current-Stock, no Duplication-Exploits.
  - [ ] Hooks für Gold-Sinks (Repair, Travel) wenn relevant.
  - [ ] Tests: Restock-Skip in Combat-Time, Concurrency-Safety.
  Tests:
  - [ ] **Restock-Time-Test**: Timers decrement korrekt pro Tick.
  - [ ] **Inventory-Replenish-Test**: Items replenished zwischen Min/Max-Ranges.
  - [ ] **Save-Load-Test**: Restock-State persistiert & restored.
  - [ ] **Determinismus-Test**: gleicher Seed → identische Inventory nach Restock.
  References:
  - docs/ECONOMY_AND_VENDORS.md
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
