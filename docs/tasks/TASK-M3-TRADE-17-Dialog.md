- [ ] ID: TASK-M3-17
  Title: Performance: Loot-Monte-Carlo & Inventory-Mikros
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `tests/perf/test_loot_perf.py`, `tests/perf/test_inventory_perf.py`
  DependsOn: TASK-M3-03, TASK-M3-08
  Notes:
  100k Loot-Rolls (versch. Tabellen) messen; Inventory-Add/Remove/Stack-Operationen in tight loop.
  Acceptance:
  - [ ] Loot 100k < 250 ms (CI grob); Inventory-ops je < 1 s median (CI-grobe Schaetzung, plattformabhaengig).
  Tests:
  - [ ] TBD
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
