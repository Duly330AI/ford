- [ ] ID: TASK-M1-CONFIG-11-Seeds-ENV
  Title: Konfiguration & Seeds (INI/JSON + ENV)
  Status: Proposed
  Priority: P2
  Owner: Copilot Agent
  Created: 2025-10-26
  Artifacts: `game/util/config.py`, `data/config.default.json`, `tests/util/test_config.py`
  DependsOn: TASK-M1-01
  Notes:
  Lese Reihenfolge: ENV → lokale `config.json` → `config.default.json`. Parameter: Dungeon-Größe, Raumgrenzen, Korridorbreite, Seed.
  Acceptance:
  - [ ] ENV überschreibt Datei.
  - [ ] Fehlende Werte → Defaults.
  Tests:
  - [ ] Merge/Override-Tests, Typ-Validierung.
  References:
  - docs/CONVENTIONS.md
  - docs/ARCHITECTURE.md
