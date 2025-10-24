- [ ] ID: TASK-M3-08
  Title: Loot-Tabellen (Gewichte, Mengen, Nested Tables)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/loot.py`, `data/loot_tables.json`, `tests/systems/test_loot_tables.py`
  DependsOn: TASK-M3-01, TASK-M3-02
  Notes:
  Tabellen mit Eintraegen: `item_id|table_id`, `weight`, `qty_min/max`. Unterstuetze **nested tables** (z. B. "rare_gems"). Optional `unique_once` Flag pro Roll.
  Acceptance:
  - [ ] Gewichtsbasierte Auswahl; Mengen im Bereich; nested aufgeloest.
  - [ ] Schutz vor Zyklen & zu tiefer Rekursion.
  Tests:
  - [ ] Monte-Carlo-Verteilung (100k Rolls) ~ erwarteten Proportionen.
  - [ ] Zirkularitaets-Erkennung, Fehlerfaelle.
