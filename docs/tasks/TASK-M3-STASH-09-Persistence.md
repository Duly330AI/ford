- [ ] ID: TASK-M3-09
  Title: Drop-Hooks bei Gegner-Death (Integration mit M2)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/combat.py` (Death->Drop)`, `tests/integration/test_death_drops.py`
  DependsOn: TASK-M2-04, TASK-M3-08
  Notes:
  Bei `Death` eines Gegners: resolve Loot-Tabelle aus `data/monsters.json` (`drop_table_id`) -> erzeuge **logical drops** (noch kein Arcade-Spawning).
  Acceptance:
  - [ ] Drops sind deterministisch mit Seed; mehrere Eintraege moeglich.
  Tests:
  - [ ] Simulierter Kampf -> erwartete Drops/Anzahl pro Tabelle.
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
