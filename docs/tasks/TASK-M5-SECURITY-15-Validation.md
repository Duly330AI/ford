- [ ] ID: TASK-M5-SECURITY-15-Validation
  Title: E2E Save/Load Flow (Kampf -> Loot -> Craft -> Load)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `tests/integration/test_full_save_load_flow.py`
  DependsOn: TASK-M5-02, TASK-M5-03, TASK-M5-04, TASK-M5-05, TASK-M5-06, TASK-M5-07, TASK-M5-08, TASK-M5-10, TASK-M5-12
  Notes:
  Simuliere Gameplay (Combat -> Loot -> Craft -> Equip), speichere, lade frisches Game-Objekt, vergleiche State (Stats, Inventory, Nodes, RNG).
  Acceptance:
  - [ ] State nach Load entspricht exakt dem gespeicherten Zustand (inkl. RNG-Streams).
  - [ ] Flow deckt Save-Policy & Autosave Hooks ab.
  Tests:
  - [ ] Integrationstest mit deterministischem Seed.
  - [ ] Vergleich von RNG-States vor/nach Load.
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
