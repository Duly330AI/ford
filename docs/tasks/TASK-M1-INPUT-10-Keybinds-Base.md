- [ ] ID: TASK-M1-10
  Title: Input-System & Keybinds (WASD/Arrows, R, F3, L)
  Status: Proposed
  Priority: P2
  Owner: Copilot Agent
  Artifacts: `game/util/input.py`, `game/scenes/dungeon.py`, `tests/util/test_input.py`
  DependsOn: TASK-M1-03
  Notes:
  Einheitliche Keymap + Rebind-Hooks für spätere Settings.
  Bereite Umstellung auf Context Input Manager (TASK-M1-INPUT-01) und Controls-Schema (TASK-M1-INPUT-02) mit klaren Adapter-Punkten vor.
  Acceptance:
  - [ ] Keymap als Daten (dict), leicht testbar.
  Tests:
  - [ ] Mapping-Tests (idempotent, keine Doppelbelegung).
  References:
  - docs/INPUT_AND_REBIND.md
  - docs/CONVENTIONS.md
  - docs/ARCHITECTURE.md
