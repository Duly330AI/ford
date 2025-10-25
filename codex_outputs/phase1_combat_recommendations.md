# Phase 1 — Combat Recommendations

## Executive Summary
Concrete actions to close gaps and harden the combat documentation and data.

## Critical Recommendations
- Define and implement `dodge` in `combat_rules.json` and document with formula, parameters, and examples.
- Remove literal dice tokens from prose; rephrase the "d20" mention in GAMEPLAY.md to avoid violating the dice-notation rule.

## High Priority
- Expand `ranged` documentation (reload turn logic, accuracy adjustments, movement penalties, weapon class specifics) and ensure alignment with JSON.
- Document `crit` behavior (chance and multiplier) and parameter mapping.

## Medium Priority
- Add CI checks that compare `combat_rules.json` keys against COMBAT_RULES.md sections.
- Add unit tests that compute example outcomes directly from JSON parameters and compare to documented examples.

## Low Priority
- Clarify wording around "Roll" to emphasize seeded random integers rather than tabletop dice.
