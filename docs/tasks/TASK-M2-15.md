- [ ] ID: TASK-M2-15
  Title: Kampf-Log & Replay (Debug)
  Status: Proposed
  Priority: P2
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/util/combat_log.py`, `tests/util/test_combat_log.py`
  DependsOn: TASK-M2-04
  Notes:
  Strukturierte Events (JSON-serialisierbar) fuer jede Aktion (Rolls, Modifikatoren, Outcomes). Minimaler Replay: gleiche Intents + Seed -> identisches Ergebnis.
  Acceptance:
  - [ ] Logeintraege enthalten Wurf, Mods, Ziel, Schaden, Effekte.
  Tests:
  - [ ] Roundtrip: Log reproduziert Ergebnis bei festem Seed.
