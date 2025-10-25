- [ ] ID: TASK-M1-INPUT-01-Context-Input-Manager
  Title: Context Input Manager (Context Stack, Priority Routing)
  Status: Proposed
  Priority: P1
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `game/input/context_manager.py`, `tests/input/test_context_manager.py`
  DependsOn: TASK-M1-10, TASK-M6-UI-01
  Notes:
  Implementiere Context-Stack-Manager: UI > Combat > Overworld > Rebind Prioritäten. Input-Events normalisiert von Arcade, context-aware Action-Dispatch ohne Scene-Coupling. APIs: Push/Pop Contexts, Query Active Context, Register Callbacks mit Conflict-Resolution. Backward-Compat für MVP. Diagnostic Logging für Debug.
  Acceptance:
  - [ ] Input-Events routed zu höchst-priorität Context, Lower-Contexts blockiert wenn Higher aktiv.
  - [ ] Context-Manager exponiert deterministische Stack-Operations, Safe Reentrancy.
  - [ ] Bestehende Movement/Combat-Input Flows operational via Compat-Shim.
  - [ ] Tests: Context-Transitions, Priority-Enforcement, Edge-Cases (Nested UI, Rebind).
  - [ ] Doku updated: APIs & Migration-Path für Scene-Input-Handler.
  Tests:
  - [ ] **Context-Priority-Test**: Higher Context blockiert Lower Events.
  - [ ] **Stack-Operations-Test**: Push/Pop/Query funktionieren deterministisch.
  - [ ] **Compat-Shim-Test**: Alte Input-Flows noch operational.
  - [ ] **Nested-UI-Test**: Mehrere Contexts gleichzeitig, korrektes Blocking.
  References:
  - docs/INPUT_AND_REBIND.md
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
