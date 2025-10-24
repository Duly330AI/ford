- [ ] ID: TASK-M5-13
  Title: Korruptions-Recovery & Fallback
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `tests/integration/test_corruption_recovery.py`
  DependsOn: TASK-M5-04, TASK-M5-05, TASK-M5-06
  Notes:
  Szenarien: truncierte Datei, falscher Hash, ungueltiges MsgPack. Greife auf letzte gueltige Auto/Manual-Save zurueck und logge Vorfall.
  Acceptance:
  - [ ] Detektion korrupten Saves fuehrt zu Recovery aus Manifest.
  - [ ] Letzter gueltiger Save bleibt intakt (keine Ueberschreibung).
  Tests:
  - [ ] Integrationstest mit Fake-Dateien (korrupt).
  - [ ] Pruefe Log-Eintrag / Fehlercode.
