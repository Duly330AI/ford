# Phase 2 — Magic Inconsistencies

## Executive Summary
Spells data is formula-based (base/variance/scaling) and references reagents correctly. The Magic System doc has a dice-notation example and lacks documentation for the `fizzle` mechanic despite its presence in `spells.json`.

## Critical Issues (must fix)
- Dice notation present in MAGIC_SYSTEM.md
  - `docs/MAGIC_SYSTEM.md:52` example: `2d6 + INT*0.2` — violates “no dice notation” rule.
  - Replace with: `base + variance_pct * base ± scaling(INT)` consistent with spells data.
- Fizzle mechanic undocumented
  - `spells.json` includes a `fizzle` field; there is no formula/section in MAGIC_SYSTEM.md describing fizzle probability and modifiers.

## High Priority Issues
- Mana cost formula not defined in docs
  - Spells define `cost.mana` per spell; document base cost, modifiers (INT/Meditation?), and edge cases.
- Resist check behavior
  - `spells.json` uses `resist_check`; document formula and interactions with target stats/resists.

## Medium Priority Issues
- Circle (1–8) usage is present in data; ensure section summarizing circle gating, cast_rounds defaults, and scaling expectations.

## Low Priority Issues
- Ensure naming/prefix guidance for reagents is explicitly documented (all current spell reagents valid).

## Informational Notes
- Spells reagent cross-check: 8 distinct reagents referenced by spells; all exist in `items.json` (`reagent_*`).
- No dice notation found in `spells.json` (good).
- `cast_rounds` is referenced in MAGIC_SYSTEM.md and GAMEPLAY.md.

## Recommendations
- Update MAGIC_SYSTEM.md examples to remove dice, align with data-driven fields (`effects[].base`, `effects[].variance_pct`, `effects[].scaling`).
- Add `fizzle` formula (e.g., based on skill vs. circle, movement, armor interference) and acceptance examples.
- Document `cost.mana` formula and modifiers; add guidance on reagent consumption per cast.
