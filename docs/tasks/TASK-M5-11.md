- [ ] ID: TASK-M5-11
  Title: Migration Framework (v1 -> v2)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/save_migrate.py`, `tests/systems/test_save_migrate.py`
  DependsOn: TASK-M5-01
  Notes:
  Registriere migrations: migrate(data, from_version, to_version). Beispiel: v1 -> v2 fuegt neues Feld hinzu.
  Acceptance:
  - [ ] Migrationen idempotent; wiederholter Lauf veraendert Daten nicht.
  - [ ] Ungueltige Versionsspruenge erzeugen klare Fehlermeldung.
  Tests:
  - [ ] Fixtures fuer v1 Save -> Migration -> Validation.
  - [ ] Mehrfachmigration (v1->v2->v3) bleibt konsistent.
