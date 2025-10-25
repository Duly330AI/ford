- [ ] ID: TASK-M4-AUDIO-01-Audio-Mixer-Engine
  Title: Audio Mixer Engine (Buses, Volume, Routing)
  Status: Proposed
  Priority: P1
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `game/audio/mixer.py`, `tests/audio/test_mixer.py`
  DependsOn: TASK-M4-15, TASK-M4-06
  Notes:
  Implementiere Audio-Mixer: Buses (MUSIC, SFX, UI) mit Per-Bus Volume/Mute/Routing. Asset-Loading, Caching, Playback-APIs. Crossfade, Ducking-Behavior. Config via `audio/audio_config.json`. Testable Headless (Stubbed Backend). Interface-Abstraction für Audio-Backend-Swapping. Debug-Overlay Bus-Levels. Graceful Missing-Asset-Handling mit Fallback.
  Acceptance:
  - [ ] Gameplay-Systems trigger Mixer-Events via Existing-Hooks.
  - [ ] Volume-Adjustments & Ducking per Config, UI can Query/Update Runtime.
  - [ ] Mixer handles Missing-Assets mit Descriptive-Errors & Fallback.
  - [ ] Tests Headless, Deterministic Bus-Volume-Math & Ducking.
  - [ ] Doku: Mixer-Architektur, Config-Format.
  Tests:
  - [ ] **Bus-Volume-Test**: Volume-Math korrekt.
  - [ ] **Ducking-Test**: Ducking applies per Config.
  - [ ] **Asset-Lifecycle-Test**: Loading, Caching, Cleanup korrekt.
  - [ ] **Headless-Test**: Mixer works ohne Audio-Hardware.
  References:
  - docs/SOUND_DESIGN.md
  - docs/CONVENTIONS.md
  - docs/ARCHITECTURE.md
