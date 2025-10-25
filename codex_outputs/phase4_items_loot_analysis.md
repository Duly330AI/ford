# Phase 4 — Items, Crafting & Loot Analysis

## Executive Summary
Cross-references between items, recipes, loot tables, and monsters are largely consistent. One recipe references a non-existent reagent ID.

## Critical Issues (must fix)
- Orphaned Item Reference in Recipe
  - Recipe `brew_cure_potion` input references `reagent_spider_silk` (singular), but items define `reagent_spiders_silk` (plural). This will fail at runtime.

## High Priority Issues
- None detected in loot tables → items references (sampled).

## Medium Priority Issues
- Consider adding schema validation for recipes to ensure `inputs[*].item_id` and `outputs[*].item_id` exist in `items.json`.

## Low Priority Issues
- Add optional lints for duplicate or unused items and for loot table weight sanity checks.

## Recommendations
- Fix the `brew_cure_potion` reagent ID to match `reagent_spiders_silk` or update the item ID consistently across data files.
- Add validation tests in CI to catch recipe/loot/monster cross-ref errors early.

## Statistics
- Missing recipe inputs: 1 (brew_cure_potion → reagent_spider_silk)
- Missing recipe outputs: 0
- Loot → missing item references: 0 (sampled)
- Monsters → missing loot_table: 0 (sampled)
