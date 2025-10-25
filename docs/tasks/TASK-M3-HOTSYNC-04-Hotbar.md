- [ ] ID: TASK-M3-HOTSYNC-04-Hotbar
  Title: Equipment-Slots & Stat-Aggregation (weapon/offhand/armor/accessory)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/equipment.py`, `tests/systems/test_equipment.py`
  DependsOn: TASK-M3-03
  Notes:
  Ausruestungs-Slots: `weapon`, `offhand`, `armor`, `accessory`. Regeln: Typkompatibilitaet, z. B. Bogen belegt `weapon` und verbraucht **Arrows** (Item-Typ). Stat-Aggregation (Basis + Mods aus Items + Skill-Boni).
  Acceptance:
  - [ ] Equip/Unequip verschiebt Items zu/von Inventar transaktional.
  - [ ] Aggregierte Stats reproduzierbar und testbar.
  Tests:
  - [ ] Mehrere Mods-Quellen; Konflikte/inkompatible Typen.
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
