- [ ] ID: TASK-M4-14
  Title: World-Adapter fuer Nodes (Spawn/Despawn, Hitbox, Label)
  Status: Proposed
  Priority: P2
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/util/nodes_adapter.py`, `game/scenes/dungeon.py`, `tests/smoke/test_nodes_adapter_import.py`
  DependsOn: TASK-M4-05
  Notes:
  Szene rendert Nodes (Sprite/Icon pro Typ/Tier), einfache Hitbox fuer Interaktion ("E"). Logik bleibt getrennt.
  Acceptance:
  - [ ] Spawn/Despawn synct mit Logik-States; kein GL in Tests.
  Tests:
  - [ ] TBD
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
  - docs/DUNGEON_GENERATOR.md
