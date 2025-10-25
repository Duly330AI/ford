- [ ] ID: TASK-M6-UI-11-Performance
  Title: Merchant/Trade UI (Buy/Sell Tables, Dynamic Prices, Quick-Sell)
  Status: Proposed
  Priority: P2
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/ui/merchant.py`, `tests/ui/test_merchant.py`
  DependsOn: TASK-M6-UI-01, TASK-M3-04, TASK-M4-ECON-01, TASK-M4-ECON-02, TASK-M4-ECON-03
  Notes:
  Design the merchant interface from UI_SPEC_UO_STYLE.md Section 8 with buy and sell tables and search filters.
  Bind price/stock data via `systems/economy` and vendor loader APIs; surface faction modifiers from data.
  Implement Ctrl+Click quick-sell with confirmation for rare items and support favorites or wishlist markers.
  Alle Texte und Tooltips nutzen Localization-Service (TASK-M8-I18N-01) inklusive dynamischer Parameter (Preis, Menge).
  Acceptance:
  - [ ] Buy and sell tables load merchant inventory and player offers.
  - [ ] Ctrl+Click quick-sell works with confirmation for protected items.
  - [ ] Favorites or wishlist markers display for tracked items.
  - [ ] Dynamic pricing hook points exist for future economy data.
  Tests:
  - [ ] tests/ui/test_merchant.py::test_buy_sell_tables
  - [ ] tests/ui/test_merchant.py::test_quick_sell_flow
  - [ ] tests/ui/test_merchant.py::test_favorite_markers
  References:
  - docs/ARCHITECTURE.md
  - docs/CONVENTIONS.md
  - docs/ITEMIZATION_DESIGN.md
  - docs/LOCALIZATION.md
