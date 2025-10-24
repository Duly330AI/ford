- [ ] ID: TASK-M5-05
  Title: Save-Metadaten & Manifest (Slots, Versions, History)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/systems/save_manifest.py`, `tests/systems/test_save_manifest.py`
  DependsOn: TASK-M5-04
  Notes:
  Verwalte manifest.json pro Slot: version, timestamp, duration, seed, player_level, checksum, autosave_history.
  Acceptance:
  - [ ] Manifest aktualisiert nach jedem Save; behalt konfigurierbare Historie (z. B. 5 Autosaves).
  - [ ] Inkonsistente Manifest-Eintraege werden aufgeraeumt (fehlende Dateien).
  Tests:
  - [ ] Manifest-Rotation fuer Autosaves.
  - [ ] Recovery bei fehlenden Dateien aktualisiert Manifest.
