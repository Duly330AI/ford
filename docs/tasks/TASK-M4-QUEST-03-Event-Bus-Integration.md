# TASK-M4-QUEST-03: Event Bus Integration

**Milestone:** M4 - Nodes, Berufe & Crafting
**Priority:** P0 (High)
**Estimated Effort:** 3-4d
**Dependencies:** TASK-M2-04, TASK-M3-03, TASK-M4-QUEST-01-Core-Quest-Engine

## Objectives

- Implement global event bus (or extend existing dispatcher) to propagate gameplay events (kill, collect, use_item, location, time) to subscribed systems.
- Wire combat, inventory, interaction, and timekeeper systems to publish normalized event payloads.
- Connect quest engine as subscriber, ensuring deterministic processing order and thread-safety.
- Provide subscription APIs for tutorial manager, analytics, and future systems without tight coupling.
- Add tests verifying event propagation, filtering, and quest engine reactions using seeded simulations.

## Acceptance Criteria

- Event bus handles concurrent event streams without losing events or introducing race conditions.
- Quest engine receives relevant events and ignores unrelated ones via filter predicates.
- System supports replay/logging for debugging (optional) while maintaining performance budgets.
- Tests cover multiple publishers/subscribers, event ordering guarantees, and unsubscribe behavior.
- Documentation updated explaining event payload structure and subscription usage.

## Implementation Notes

- Keep bus implementation in systems/util layer to preserve testability; scenes should subscribe via adapters when needed.
- Use dataclasses or typed events to avoid reliance on loosely structured dicts.
- Consider batching or queueing strategies for turn-based context to maintain determinism.
- Align event naming and payload schema with localization/quest data expectations for minimal translation logic.

## Related Documents

- docs/QUEST_SYSTEM.md
- docs/ARCHITECTURE.md
- docs/TODO/QUEST_SYSTEM_TD.md
- docs/CONVENTIONS.md
