- [ ] ID: TASK-M3-COMBAT-12-Integration
  Title: Tooltips & Rarity-UI (Adapter)
  Status: Proposed
  Priority: P2
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/util/tooltip.py`, `game/scenes/ui_hotbar.py`, `tests/smoke/test_tooltip_import.py`
  DependsOn: TASK-M3-02, TASK-M3-11
  Notes:
  Tooltip-Formatter (reine Strings): Name, Typ, Rarity, Mods, dmg/def, Stack/Weight, Value. Scene rendert Stil (Farben je Rarity).
  Acceptance:
  - [ ] Formatter ohne Arcade; Strings sauber formatiert.
  Tests:
  - [ ] Beispiel-Items -> erwartete Tooltip-Zeilen.
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
