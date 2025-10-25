- [ ] ID: TASK-M3-EXT
  Title: Usables & Containers System (Locks, Traps, Ownership, Interactions)
  Status: Proposed
  Priority: P0
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `docs/USABLES_AND_CONTAINERS_OVERVIEW.md`
  DependsOn: TASK-M3-02, TASK-M3-06, TASK-M3-08
  Notes:
  Summarize the container and usable object pipeline defined in USABLES_AND_CONTAINERS.md, including container archetypes (chest, barrel, cabinet, etc.), interactions (open, lockpick, disarm, search, inspect, bash, read), and supporting systems (locks, traps, ownership, respawn).
  Cross-reference data sources such as `data/loot_tables.json`, prospective `data/usables/*.json`, and progression systems that influence skill checks (lockpicking, tinkering, detect hidden).
  Break down the milestone into TASK-M3-EXT-01..06 covering container core, locks, traps, detect hidden, bash, and ownership mechanics, and align dependencies with AI faction reactions where applicable.
  Document sequencing expectations with related milestones (e.g., TASK-M2-AI-04 for faction responses, TASK-M3-08 for loot generation) and capture outstanding design questions for later phases.
  Acceptance:
  - [ ] TASK-M3-EXT-01..06 reach Status: Done and are referenced from this milestone.
  - [ ] Overview document synthesizes USABLES_AND_CONTAINERS.md requirements and inter-task dependencies.
  - [ ] Integration plan covers locks->disarm->loot workflow including skill and faction touchpoints.
  Tests:
  - [ ] `tests/integration/test_usables_workflow.py::test_lock_to_loot_flow` (seeded).
  - [ ] `tests/integration/test_usables_workflow.py::test_trap_detect_disarm_flow` (seeded).
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
  - docs/DUNGEON_GENERATOR.md
  - docs/ITEMIZATION_DESIGN.md
  - docs/QUEST_SYSTEM.md
