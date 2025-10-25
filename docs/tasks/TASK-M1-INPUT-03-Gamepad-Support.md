- [ ] ID: TASK-M1-INPUT-03
  Title: Gamepad Support (Deadzones, Sensitivity, Mapping)
  Status: Proposed
  Priority: P1
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `game/input/gamepad_handler.py`, `tests/input/test_gamepad.py`
  DependsOn: TASK-M1-INPUT-01, TASK-M1-INPUT-02
  Notes:
  Implementiere Gamepad-Input: Axis-Deadzones, Button-Mapping, Sensitivity-Curves, Rumble-Hooks. Gamepad-Events normalisiert durch Input-Manager, context-aware Action-Dispatch identisch zu Keyboard-Flow. Gamepad-spezifische Controls-JSON Felder. Platform-Diffs (Xbox/PlayStation) via Mapping-Tables. Deterministische Mapping-Names für Localization & Analytics. Optional Rumble-Callbacks.
  Acceptance:
  - [ ] Gamepad-Inputs mappt zu Actions über Contexts, keine Interference mit Keyboard/Mouse.
  - [ ] Deadzone & Sensitivity configurable via Controls-JSON, Runtime-Applied.
  - [ ] Rebinding-UI erkennt Gamepad-Inputs, updated Config.
  - [ ] Tests: Analog-Stick-Thresholds, Button-Chords, Keyboard-Kombinationen.
  - [ ] Accessibility/Support-Docs mit Controller-Guidelines.
  Tests:
  - [ ] **Deadzone-Test**: Analog-Inputs innerhalb Deadzone → kein Action.
  - [ ] **Button-Mapping-Test**: Gamepad-Buttons mappt korrekt zu Actions.
  - [ ] **Sensitivity-Test**: Sensitivity-Curves appliziert auf Analog-Werte.
  - [ ] **Context-Test**: Gamepad-Input respektiert Context-Blocking.
  References:
  - docs/INPUT_AND_REBIND.md
  - docs/CONVENTIONS.md
  - docs/ARCHITECTURE.md
