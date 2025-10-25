- [ ] ID: TASK-M6-UI-11
  Title: Merchant/Trade UI (Buy/Sell Tables, Dynamic Prices, Quick-Sell)
  Status: Proposed
  Priority: P2
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/ui/merchant.py`, `tests/ui/test_merchant.py`
  DependsOn: TASK-M6-UI-01, TASK-M3-04
  Notes:
  Design the merchant interface from UI_SPEC_UO_STYLE.md Section 8 with buy and sell tables and search filters.
  Prepare hooks for dynamic pricing and faction modifiers while shipping a static prototype.
  Implement Ctrl+Click quick-sell with confirmation for rare items and support favorites or wishlist markers.
  Acceptance:
  - [ ] Buy and sell tables load merchant inventory and player offers.
  - [ ] Ctrl+Click quick-sell works with confirmation for protected items.
  - [ ] Favorites or wishlist markers display for tracked items.
  - [ ] Dynamic pricing hook points exist for future economy data.
  Tests:
  - [ ] tests/ui/test_merchant.py::test_buy_sell_tables
  - [ ] tests/ui/test_merchant.py::test_quick_sell_flow
  - [ ] tests/ui/test_merchant.py::test_favorite_markers
