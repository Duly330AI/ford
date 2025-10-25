- [ ] ID: TASK-M3-INVENTORY-05-System
  Title: Consumables & Use-Effects (Heiltrank, Buff, Cleanse)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/item_use.py`, `data/items.json` (Erweiterung `use_effect`)`, `tests/systems/test_item_use.py`
  DependsOn: TASK-M3-02
  Notes:
  Modell fuer `use_effect`: typisiert & datengetrieben (`heal.hp=50`, `apply_effect="Haste", duration=2`, `cleanse=["poison"]`). **Keine Arcade-Calls.**
  Acceptance:
  - [ ] Use reduziert Stack; Effekte landen im `effects`-System (M2).
  - [ ] Ungueltige Nutzung (cooldown, out-of-combat-only etc.) wird abgewiesen (fuer jetzt minimal).
  Tests:
  - [ ] Heil-/Buff-/Cleanse-Faelle, Stack-Verbrauch, Fehlerfaelle.
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
