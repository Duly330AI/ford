- [ ] ID: TASK-M3-EXT-02
  Title: Locks & Lockpicking System (Skill Checks, Keys, Failure)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/systems/locks.py`, `tests/systems/test_locks.py`
  DependsOn: TASK-M3-EXT-01, TASK-M3-06
  Notes:
  Extend container interactions to support lock metadata (`locked`, `difficulty`, `key_id`, optional anti-tamper triggers) per USABLES_AND_CONTAINERS.md Section 3-4.
  Implement the lockpicking formula `P = clamp(0.02, 0.5 + (lockpicking - difficulty)/200, 0.98)` and allow keys to bypass the roll when `key_id` matches.
  Emit skill gain rolls on every attempt (success or failure) and trigger optional anti-tamper responses such as traps or guard alerts when configured.
  Ensure lockpicking is treated as a Main Action in combat contexts and that failure states bubble up to the container core for follow-up actions.
  Acceptance:
  - [ ] Lockpick checks use skill vs difficulty.
  - [ ] Keys bypass lockpick check.
  - [ ] Skill gains on attempts (success/fail).
  - [ ] Anti-tamper triggers (optional, configurable).
  Tests:
  - [ ] Lockpick success/fail tests (seeded).
  - [ ] Key bypass tests.
  - [ ] Skill gain tests.
  - [ ] Anti-tamper tests.
