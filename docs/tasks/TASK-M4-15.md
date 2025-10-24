- [ ] ID: TASK-M4-15
  Title: Audio-Hooks (Gather-Start/Success/Fail, Craft-Complete)
  Status: Proposed
  Priority: P2
  Owner: Copilot Agent
  Created: 2025-10-24
  Artifacts: `game/util/audio_adapter.py`, `tests/smoke/test_audio_adapter_import.py`
  DependsOn: TASK-M4-02, TASK-M4-06
  Notes:
  Duenne API: `play_sfx("gather_start")`, `"gather_success"`, `"craft_complete"`. Scene verdrahtet Arcade-Audio.
  Acceptance:
  - [ ] No-ops in Tests; saubere Aufrufe aus Systems.
  Tests:
  - [ ] TBD
