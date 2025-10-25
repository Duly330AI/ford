# Phase 2 — Magic Recommendations

## Executive Summary
Actions to align Magic documentation with data-driven spells and fill missing mechanics.

## Critical Recommendations
- Remove dice-notation examples from MAGIC_SYSTEM.md and replace with base/variance/scaling formulations consistent with `spells.json`.
- Add a documented `fizzle` formula and factors (skill vs. circle, armor, movement); ensure `spells.json` `fizzle` field is clearly specified.

## High Priority
- Document `cost.mana` computation and any modifiers (stats, passives, meditative states).
- Specify `resist_check` mechanics and interactions with target resistances.

## Medium Priority
- Add a short circle (1–8) overview (requirements, typical cast_rounds, scaling expectations) and link to spells list.

## Low Priority
- Include a reagent glossary table in MAGIC_SYSTEM.md sourced from `items.json` to aid consistency.
