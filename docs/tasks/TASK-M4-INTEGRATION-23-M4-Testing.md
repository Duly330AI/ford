- [ ] ID: TASK-M4-23
  Title: Reading & Lore System (Books, Scrolls, Notes, Lore Flags)
  Status: Proposed
  Priority: P2
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/systems/lore.py`, `tests/systems/test_lore.py`
  DependsOn: TASK-M3-EXT-01
  Notes:
  Support readable objects defined in USABLES_AND_CONTAINERS.md Section 6.3 via fields such as `readable.pages` and `readable.lore_id`, enabling multi-page content with navigation.
  Implement reading as a Main Action during combat (instant in overworld) that sets lore flags for quest progression or journal entries.
  Persist lore flags through save/load and expose them to quest/tracking systems.
  Acceptance:
  - [ ] Reading action works (main action in combat).
  - [ ] Lore flags set on read.
  - [ ] Multi-page support (UI shows pages).
  - [ ] Lore IDs persist in save/load.
  Tests:
  - [ ] Reading tests (lore flag set).
  - [ ] Multi-page tests (navigation).
  - [ ] Persistence tests.
  References:
  - docs/ARCHITECTURE.md
  - docs/COMBAT_RULES.md
  - docs/CONVENTIONS.md
  - docs/QUEST_SYSTEM.md
