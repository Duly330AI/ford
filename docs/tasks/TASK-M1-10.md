- [ ] ID: TASK-M1-10
  Title: Input-System & Keybinds (WASD/Arrows, R, F3, L)
  Status: Proposed
  Priority: P2
  Owner: Copilot Agent
  Artifacts: `game/util/input.py`, `game/scenes/dungeon.py`, `tests/util/test_input.py`
  DependsOn: TASK-M1-03
  Notes:
  Einheitliche Keymap + Rebind-Hooks für spätere Settings.
  Acceptance:
  - [ ] Keymap als Daten (dict), leicht testbar.
  Tests:
  - [ ] Mapping-Tests (idempotent, keine Doppelbelegung).
