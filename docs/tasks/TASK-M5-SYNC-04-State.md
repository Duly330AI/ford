- [ ] ID: TASK-M5-SYNC-04-State
  Title: Atomic File Writer (tmp -> rename -> fsync)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/util/atomic_fs.py`, `tests/util/test_atomic_fs.py`
  DependsOn: -
  Notes:
  Schreibe Saves als tmp-Datei, fsync Datei & Verzeichnis, benenne atomar um. Unterstuetze Windows & POSIX Pfade.
  Acceptance:
  - [ ] Crash-Simulation laesst keine halb geschriebenen Saves zurueck.
  - [ ] Fsync-Calls optional konfigurierbar (fuer Tests mockbar).
  Tests:
  - [ ] Unit-Tests mit Temp-Verzeichnis (pytest tmp_path).
  - [ ] Fehlerpfade (keine Rechte, voller Datentraeger) erzeugen Exceptions mit Code.
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
