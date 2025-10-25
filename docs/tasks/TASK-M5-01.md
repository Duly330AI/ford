- [ ] ID: TASK-M5-01
  Title: Save-Schema-Definition & Validatoren (v1)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `data/schemas/save_v1.schema.json`, `game/systems/save_schema.py`, `tests/systems/test_save_schema.py`
  DependsOn: TASK-M4-QUEST-01, TASK-M4-QUEST-03
  Notes:
  Definiere Schema fuer Welt/Player/Inventory/Skills/Nodes/Stations/RNG/Timekeeper/Quests/Tutorial-Flags. Stelle sicher, dass alle Referenzen IDs aus data/* validieren.
  Modelliert Quest- und Objective-States (FSM) sowie Event-Bus-Persistenz laut TASK-M4-QUEST-01/03 und FTUE-Progress Haken.
  Acceptance:
  - [ ] Schema deckt alle Kernbereiche ab (Player, Inventory, Equipment, Skills, Loot, Nodes, Stations, RNG, Timekeeper).
  - [ ] Beispiel-Save (fixtures/save_v1.json) validiert erfolgreich; Negativfaelle erzeugen praezise Fehlermeldungen.
  Tests:
  - [ ] Positiv/Negativ-Tests fuer Schema-Validation.
  - [ ] Referenz-Test prueft unbekannte Item-/Node-IDs.
