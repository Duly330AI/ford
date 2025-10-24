- [ ] ID: TASK-M3-10
  Title: World-Drops & Pickup-Adapter (Scene-Stubs)
  Status: Proposed
  Priority: P2
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/util/drops_adapter.py`, `game/scenes/dungeon.py`, `tests/smoke/test_drops_adapter_import.py`
  DependsOn: TASK-M3-09
  Notes:
  Duenner Adapter: `spawn_drop(logical_drop, pos)` und `pickup_drop(player, drop_id)`. **In Tests No-op**; Scene implementiert Visuals spaeter.
  Acceptance:
  - [ ] Pickup ruft Inventory-`add` auf; Fehlerpfade sauber.
  Tests:
  - [ ] Import/No-op-Tests; Integrations-Test ohne GL.
