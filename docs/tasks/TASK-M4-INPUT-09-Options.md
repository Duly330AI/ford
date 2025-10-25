- [ ] ID: TASK-M4-09
  Title: Blueprint-/Rezept-Entdeckung (Drops/Scrolls)
  Status: Proposed
  Priority: P2
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/recipes_discovery.py`, `tests/systems/test_recipes_discovery.py`
  DependsOn: TASK-M3-09, TASK-M4-01
  Notes:
  Rezepte sind **nicht alle** von Start an bekannt. Items `recipe_scroll:<id>` schalten Rezepte frei (persistenter Flag).
  Acceptance:
  - [ ] Doppelte Entdeckung idempotent; Save-Hooks vorbereitet (M5).
  Tests:
  - [ ] Unlock-Flows, Dopplungs- und Fehlerfaelle.
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
