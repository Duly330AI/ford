- [ ] ID: TASK-M3-18
  Title: Integrationsszenario "Kampf -> Drop -> Pickup -> Equip/Use"
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `tests/integration/test_combat_drop_pickup_flow.py`
  DependsOn: TASK-M2-04, TASK-M3-03, TASK-M3-08, TASK-M3-10, TASK-M3-11
  Notes:
  End-to-End: Gegner stirbt -> Loot generiert -> World-Drop -> Pickup -> Inventory -> Equip **oder** Use.
  Acceptance:
  - [ ] Vollstaendige Sequenz deterministisch mit Seed; Endzustaende (Stats/Stacks) korrekt.
  Tests:
  - [ ] TBD
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
