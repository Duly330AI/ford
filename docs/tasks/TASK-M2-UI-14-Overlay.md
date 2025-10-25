- [ ] ID: TASK-M2-UI-14-Overlay
  Title: Combat-UI Overlay (Turn Order, Action Bar, Tooltips)
  Status: Proposed
  Priority: P2
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/scenes/ui_combat.py`, `tests/smoke/test_ui_combat_import.py`
  DependsOn: TASK-M2-03, TASK-M2-04
  Notes:
  Overlay zeigt Initiative-Leiste, aktuelle Aktion, Reichweiten-Highlight bei `Move/Attack/Shoot/Cast`. Bestaetigung via Tastatur (z. B. 1-5) oder Maus.
  Acceptance:
  - [ ] Overlay toggelbar; keine Koppelung an Combat-Logik.
  Tests:
  - [ ] Smoke (Import/Init), kein GL in Unit-Tests.
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
