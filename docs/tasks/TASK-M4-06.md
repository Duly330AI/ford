- [ ] ID: TASK-M4-06
  Title: Gather-Interaktion (Tool-Checks, Dauer, Stamina, Yield)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/gather.py`, `tests/systems/test_gather.py`
  DependsOn: TASK-M4-04, TASK-M3-03, TASK-M3-06, TASK-M3-07
  Notes:
  `begin_gather(node_id)` -> prueft Reichweite (Tile-Nachbarschaft), Tool (z. B. `pickaxe`, `axe`), Stamina-Kosten (optional), **Dauer abhaengig von Tier/Skill**. Abschluss triggert `nodes.gather(...)`, Loot -> Inventory.
  Acceptance:
  - [ ] Ohne Tool kein Start; falsches Tool -> sauberer Fehler.
  - [ ] Skill reduziert Dauer / erhoeht Yield (datengetrieben).
  Tests:
  - [ ] Tool-/Skill-Pfade; Abbruch/Retry; Kapazitaetsfehler Inventar.
