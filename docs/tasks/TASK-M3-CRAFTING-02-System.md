- [ ] ID: TASK-M3-02
  Title: Items-Datenmodell & Typen (weapon/armor/consumable/material/currency)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/items.py`, `data/items.json`, `tests/systems/test_items_model.py`
  DependsOn: TASK-M3-01
  Notes:
  Item-Felder (Beispiel):
        - `id`, `name`, `type`, `rarity` (`common/rare/epic`), `stackable`, `max_stack`, `weight`, `value`, `mods` (z. B. `+ATK`, `resist.fire`), optional: `dmg` (dice string), `damage_type`, `defense`, `use_effect` (fuer consumables).
  Acceptance:
  - [ ] Items laden & instanziieren; Standardwerte/Validierung korrekt.
  - [ ] Stack-Regeln (stackable/max_stack) im Modell abgebildet.
  Tests:
  - [ ] Parsing, Edge-Cases (max_stack=1 vs. 99), Mods-Merging.
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
