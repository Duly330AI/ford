- [ ] ID: TASK-M7-FTUE-03-Tutorial-UI-Overlay
  Title: Tutorial UI Overlay (Highlights, Arrows, Prompts)
  Status: Proposed
  Priority: P1
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `game/views/tutorial_overlay.py`, `tests/views/test_tutorial_overlay.py`
  DependsOn: TASK-M6-UI-01, TASK-M6-UI-02, TASK-M7-FTUE-02
  Notes:
  Implementiere Overlay-System: Highlight-Boxes, Animated-Arrows, Contextual-Instructions per TUTORIAL_FTUE.md. Focus-Locking UI/World-Entities mit Smooth-Transitions. Localization-Ready Text-Slots & Iconography. API für Tutorial-Manager: Trigger Overlays, Queue Prompts, Auto-Dismiss on Completion. Overlay-Highlights dynam zu UI-Layout-Changes. Controller-Navigation-Support. Fallback für Headless-Tests.
  Acceptance:
  - [ ] Overlay-Highlights respond zu Tutorial-Events, Follow UI-Changes dynamisch.
  - [ ] Prompts zeigen Localized-Text & Control-Indicators (Keyboard/Gamepad).
  - [ ] System handles Overlapping-Prompts, Nur 1 Active Highlight per Context.
  - [ ] Tests: Overlay-Coords update bei UI-Reposition/Resize.
  - [ ] Doku: Overlay-Authoring, Asset-Naming, Performance.
  Tests:
  - [ ] **Highlight-Test**: Highlights render & follow UI-Elements.
  - [ ] **Prompt-Test**: Prompts display Localized-Text.
  - [ ] **Controller-Nav-Test**: Controller-Navigation works.
  - [ ] **Layout-Change-Test**: Coords update bei UI-Changes.
  References:
  - docs/TUTORIAL_FTUE.md
  - docs/INPUT_AND_REBIND.md
  - docs/CONVENTIONS.md
