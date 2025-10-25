- [ ] ID: TASK-M3-11
  Title: Hotbar (10 Slots) & Keybinds (1-0) + Quick-Use
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/hotbar.py`, `game/scenes/ui_hotbar.py`, `tests/systems/test_hotbar.py`, `tests/smoke/test_ui_hotbar_import.py`
  DependsOn: TASK-M3-03, TASK-M3-05
  Notes:
  Hotbar referenziert Inventar-Stacks per (inventory_slot_id, qty view). Aktionen: `assign`, `unassign`, `activate(index)` -> leitet an `item_use` oder `equipment` weiter.
  Acceptance:
  - [ ] Aktivierung konsumiert/equipt korrekt; fehlende Stacks handled.
  Tests:
  - [ ] Zuweisen/Entfernen/Verbrauch; Edge-Cases (leerer Slot).
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
