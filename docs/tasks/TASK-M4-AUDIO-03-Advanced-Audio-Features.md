- [ ] ID: TASK-M4-AUDIO-03-Advanced-Audio-Features
  Title: Advanced Audio Features (3D Positioning, Snapshots, Streaming)
  Status: Proposed
  Priority: P1
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `game/audio/spatial_audio.py`, `data/snapshots.json`, `data/schemas/snapshots.schema.json`, `tests/audio/test_spatial.py`
  DependsOn: TASK-M4-AUDIO-01, TASK-M4-AUDIO-02
  Notes:
  Implementiere 3D-Audio: Distance-Attenuation, Panning, Optional Height-Simulation. Snapshot/State-System für Reverb, Ambience, Combat-Transitions. Streaming/Looping für Ambient-Tracks, Crossfades. APIs für Tutorial/Quest-Scripts. Abstrakt Engine-spezifische Handles (Mocking für Tests). Snapshot-Defs in `audio/snapshots.json`. Debug-Tools: Active-Snapshot, Listener/Source-Positions. Graceful Degradation wenn 3D-Data unavailable.
  Acceptance:
  - [ ] Spatial-Audio Kalkulationen Deterministic, Reproducible Tests.
  - [ ] State-Changes (z.B. Enter-Cavern) apply Appropriate Reverb/LPF per Data-Config.
  - [ ] Mixer transitions ohne Audio-Glitches, keine Resource-Leaks (Stress-Tests).
  - [ ] APIs documented mit Usage-Examples.
  - [ ] Tests: Fallback-Behavior wenn 3D-Data unavailable.
  Tests:
  - [ ] **Attenuation-Test**: Distance-Attenuation Curve korrekt.
  - [ ] **Panning-Test**: Panning-Calcs deterministisch.
  - [ ] **Snapshot-Test**: State-Changes applizieren Reverb/LPF.
  - [ ] **Streaming-Test**: Looping & Crossfades ohne Glitches.
  References:
  - docs/SOUND_DESIGN.md
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
