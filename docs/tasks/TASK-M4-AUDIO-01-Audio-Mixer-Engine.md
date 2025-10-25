# TASK-M4-AUDIO-01: Audio Mixer Engine

**Milestone:** M4 - Nodes, Berufe & Crafting
**Priority:** P1 (Medium)
**Estimated Effort:** 4-5d
**Dependencies:** TASK-M4-15, TASK-M4-06

## Objectives

- Implement audio mixer module managing buses (MUSIC, SFX, UI) with per-bus volume, mute, and routing controls.
- Provide asset loading, caching, and playback APIs abstracted from scenes to maintain testability.
- Support crossfade, ducking (side-chain) behavior per SOUND_DESIGN roadmap.
- Ensure mixer configurable via `audio/audio_config.json` (volumes, bus settings) with validation.
- Add tests (headless) verifying bus volume math, ducking application, and resource lifecycle.

## Acceptance Criteria

- Gameplay systems trigger mixer events through existing hooks without direct dependency on pyglet.
- Volume adjustments and ducking behave per configuration; UI can query/update volumes at runtime.
- Mixer gracefully handles missing assets with descriptive errors and fallback behavior.
- Tests run headless using stubbed audio backend ensuring deterministic results.
- Documentation updated describing mixer architecture and configuration file format.

## Implementation Notes

- Keep mixer within adapter layer but avoid tight coupling to scenes so other modules (tutorial) can request audio.
- Provide interface abstraction to allow swapping audio backend in future.
- Instrument bus levels for debug overlay and analytics.
- Coordinate with localization to ensure audio cues align with context (future text prompts).

## Related Documents

- docs/SOUND_DESIGN.md
- docs/TODO/SOUND_DESIGN_TD.md
- docs/CONVENTIONS.md
- docs/ARCHITECTURE.md
