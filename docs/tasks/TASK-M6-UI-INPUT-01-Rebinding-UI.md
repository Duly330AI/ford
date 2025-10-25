- [ ] ID: TASK-M6-UI-INPUT-01
  Title: Rebinding UI (Conflict Detection, Profile Management)
  Status: Proposed
  Priority: P1
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `game/views/rebinding_ui.py`, `tests/views/test_rebinding_ui.py`
  DependsOn: TASK-M6-UI-01, TASK-M1-INPUT-01, TASK-M1-INPUT-02
  Notes:
  Implementiere Rebinding-Screen: Keyboard & Gamepad-Mappings mit Search/Filter. Listening-Mode: Next-Input-Capture, Conflict-Validation, Swap/Replace/Cancel Options. Chord-Handling & Reserved-Keys Messaging. Export/Import/Reset Control-Profiles. Context-Stack für Exclusive-Rebind-Mode. Virtualization für Long-Action-Lists. Localization-Ready Copy (Phase 9 Anticipation). Accessibility: Narration/Visual-Cues. Telemetry-Hooks optional.
  Acceptance:
  - [ ] Rebinding-UI updates Controls-Config, Propagates Zu Active-Input-Manager ohne Restart.
  - [ ] Conflicting-Bindings: Dialog mit Optionen (Swap, Replace, Cancel), Deterministic.
  - [ ] Gamepad & Keyboard Simultaneous, Chords/Holds visuell indicated.
  - [ ] Tests: Binding-Updates, Data Saved & Reloaded.
  - [ ] Accessibility: Narration, Visual-Cues per Conventions.
  Tests:
  - [ ] **Binding-Flow-Test**: Capture & Update Works.
  - [ ] **Conflict-Detection-Test**: Conflicts detected, Dialog Triggered.
  - [ ] **Persistence-Test**: Bindings Saved & Reloaded.
  - [ ] **Gamepad-Support-Test**: Gamepad-Mappings funktionieren.
  References:
  - docs/INPUT_AND_REBIND.md
  - docs/CONVENTIONS.md
  - docs/ARCHITECTURE.md
