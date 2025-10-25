- [ ] ID: TASK-M1-CAMERA-06-Pixel-Perfect
  Title: Kamera-Follow (Pixel-Perfect, Integer-Offsets)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-26
  Artifacts: `game/util/camera.py`, `game/scenes/dungeon.py`, `tests/util/test_camera.py`
  DependsOn: TASK-M1-05
  Notes:
  Kamera folgt Player; **Integer-Rounding** der Kamera-Offsets, um Sub-Pixel-Blur zu vermeiden. Clamping an Level-Bounds.
  Acceptance:
  - [ ] Kein sichtbarer Blur bei Scrollen (Pixel-Perfect).
  - [ ] Kamera verlässt die Map-Bounds nicht.
  Tests:
  - [ ] Rounding-Test (Offsets sind int), Bounds-Clamping.
  References:
  - docs/CONVENTIONS.md
  - docs/ARCHITECTURE.md
