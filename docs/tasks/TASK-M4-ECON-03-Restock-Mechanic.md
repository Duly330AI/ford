# TASK-M4-ECON-03: Vendor Restock Mechanic

**Milestone:** M4 - Nodes, Berufe & Crafting
**Priority:** P0 (High)
**Estimated Effort:** 3-4d
**Dependencies:** TASK-M4-16, TASK-M4-ECON-01-Core-Economy-System, TASK-M4-ECON-02-Vendor-Data-Schema

## Objectives

- Implement restock scheduler consuming Timekeeper ticks to decrement vendor restock timers and replenish inventory.
- Support vendor-specific restock_turns and variance (optional) as defined in vendor data files.
- Persist vendor stock state (quantities, restock timers) in save system; expose serialization integration plan.
- Provide API/events notifying UI when stock changes to refresh merchant screens in real time.
- Add tests simulating time progression, partial restocks, and persistence round-trip.

## Acceptance Criteria

- Vendors replenish items according to configured min/max ranges and restock cadence without duplicating unique items.
- Restock process respects deterministic RNG seeded per vendor for reproducible inventories when needed.
- Save/load retains restock timers and current stock, preventing duplication exploits.
- System exposes hooks for gold sinks (repair/travel) to consume restock updates where relevant.
- Tests verify restock skip in combat time (Timekeeper integration) and concurrency safety when multiple vendors update.

## Implementation Notes

- Store vendor state separately from static definitions (e.g. `VendorState` dataclass) for clarity.
- Allow manual restock triggers for debugging/testing via command or dev tools.
- Coordinate with economy UI task to ensure notifications align with session-level caches.
- Consider telemetry stubs to track stockouts and restock frequency for balancing.

## Related Documents

- docs/ECONOMY_AND_VENDORS.md
- docs/TODO/ECONOMY_AND_VENDORS_TD.md
- docs/ARCHITECTURE.md
- docs/CONVENTIONS.md
