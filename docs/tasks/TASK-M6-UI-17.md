- [ ] ID: TASK-M6-UI-17
  Title: Error/State Messages (Toast Notifications, Status Feedback)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/ui/messages.py`, `tests/ui/test_messages.py`
  DependsOn: TASK-M6-UI-01
  Notes:
  Build the toast and status messaging system from UI_SPEC_UO_STYLE.md Section 14 with 3 second non-blocking notifications.
  Cover inventory full, no ammo, recovery active, skill locked, and theft warning states with iconography.
  Allow queueing and rate limiting so repeated events do not spam the interface.
  Acceptance:
  - [ ] Toast notifications display with correct text and auto-dismiss timing.
  - [ ] Status feedback appears for inventory full, no ammo, recovery, skill locked, and theft warnings.
  - [ ] Message queue prevents spam by coalescing repeats.
  - [ ] Ownership warnings trigger before trespass interactions.
  Tests:
  - [ ] tests/ui/test_messages.py::test_toast_display
  - [ ] tests/ui/test_messages.py::test_status_messages
  - [ ] tests/ui/test_messages.py::test_message_queue_coalesce
