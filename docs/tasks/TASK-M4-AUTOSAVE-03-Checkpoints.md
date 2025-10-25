- [ ] ID: TASK-M4-03
  Title: Stationen-Registry & Scene-Adapter (Forge, Alchemy)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/util/stations.py`, `game/scenes/ui_crafting.py`, `tests/smoke/test_stations_import.py`
  DependsOn: TASK-M4-02
  Notes:
  Registry `get_station(id)` gibt reine Logik-Instanz zurueck. Szene implementiert UI (Liste Rezepte, Queue, Fortschritt) ueber Adapter-API. **Keine Arcade-Abhaengigkeit** in der Logik.
  Acceptance:
  - [ ] Mindestens **Forge** und **Alchemy** konfiguriert.
  - [ ] UI-Adapter funktionsfaehig (Smoke-Test importierbar).
  Tests:
  - [ ] TBD
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
