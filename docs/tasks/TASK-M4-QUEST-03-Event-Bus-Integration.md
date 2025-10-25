- [ ] ID: TASK-M4-QUEST-03
  Title: Event Bus Integration (Gameplay Events, Pub/Sub)
  Status: Proposed
  Priority: P0
  Owner: Codex Agent
  Created: 2025-10-26
  Artifacts: `game/systems/event_bus.py`, `tests/systems/test_event_bus.py`
  DependsOn: TASK-M2-04, TASK-M3-03, TASK-M4-QUEST-01
  Notes:
  Implementiere Global Event-Bus: Propagate Gameplay-Events (Kill, Collect, UseItem, Location, Time). Wire Combat, Inventory, Interaction, Timekeeper als Publishers. Quest-Engine als Subscriber. Deterministic Processing-Order, Thread-Safe. Subscription-APIs für Tutorial-Manager, Analytics, Future-Systems. Typed Events (Dataclasses, kein Dicts). Replay/Logging optional. Batch/Queue für Turn-Based Determinismus. Event-Naming aligned mit Localization/Quest-Data.
  Acceptance:
  - [ ] Event-Bus handles Concurrent Streams, kein Event-Loss, keine Race-Conditions.
  - [ ] Quest-Engine receives Relevant Events, Ignoriert Unrelated via Filter-Predicates.
  - [ ] System supports Replay/Logging optional, Performance-Budgets maintained.
  - [ ] Tests: Multiple Publishers/Subscribers, Event-Ordering-Guarantees, Unsubscribe.
  - [ ] Doku: Event-Payload-Structure, Subscription-Usage.
  Tests:
  - [ ] **Event-Propagation-Test**: Events reach Subscribers.
  - [ ] **Filtering-Test**: Filter-Predicates work, Unrelated Events ignored.
  - [ ] **Ordering-Test**: Event-Ordering deterministic.
  - [ ] **Concurrency-Test**: Multiple Publishers concurrent, no Races.
  References:
  - docs/QUEST_SYSTEM.md
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
