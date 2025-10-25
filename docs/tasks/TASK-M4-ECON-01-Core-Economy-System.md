# TASK-M4-ECON-01: Core Economy System

**Milestone:** M4 - Nodes, Berufe & Crafting
**Priority:** P0 (High)
**Estimated Effort:** 4-5d
**Dependencies:** TASK-M3-13, TASK-M3-02, TASK-M4-16

## Objectives

- Implement `game/systems/economy.py` providing price calculations, transaction handling, and spread logic per ECONOMY_AND_VENDORS.md.
- Parameterize pricing formula using `data/economy_rules.json` (or extend `combat_rules.json`) for rarity factors, quality modifiers, vendor spreads.
- Provide APIs for buy/sell preview, affordability checks, and gold sink integrations (repairs, travel hooks).
- Ensure system emits events for analytics/logging and integrates with inventory adjustments atomically.
- Supply deterministic tests covering price calculations across rarity/quality tiers and vendor modifiers.

## Acceptance Criteria

- Price outputs match reference examples from design document within tolerance; overrides controlled by data.
- Transactions adjust player/vendor inventories and gold balances consistently, including rollback on failure.
- System exposes hooks for vendor-specific modifiers and potential faction reputation adjustments (future-ready).
- Tests validate deterministic behavior with seeded RNG for restock randomness (if applicable).
- Documentation added for economy rules file explaining fields and tuning workflow.

## Implementation Notes

- Keep economy logic systems-layer only; UI interactions should consume via adapters.
- Structure price formula components for reuse (e.g. `calculate_base_price`, `apply_vendor_modifier`).
- Support batched transactions to reduce repeated validation when buying multiple items.
- Coordinate with restock mechanic task to share vendor state structures.

## Related Documents

- docs/ECONOMY_AND_VENDORS.md
- docs/CONVENTIONS.md
- docs/TODO/ECONOMY_AND_VENDORS_TD.md
- data/combat_rules.json (or new data/economy_rules.json)
