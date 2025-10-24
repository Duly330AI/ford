- [ ] ID: TASK-M3-14
  Title: Pfeilverbrauch & Munition-Handling (Archery)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/ammo.py`, `tests/systems/test_ammo.py`
  DependsOn: TASK-M2-10, TASK-M3-03
  Notes:
  Ranged-Angriffe benoetigen Munition (`arrows`). Bei Mangel -> entweder Fail oder automatische Umschaltung auf Melee (konfigurierbar in `data/combat_rules.json`).
  Acceptance:
  - [ ] Verbrauch pro Schuss; UI-Fehlerfall; Hotbar-Update der Menge.
  Tests:
  - [ ] Schiessen bis leer, Verhalten wie konfiguriert.
