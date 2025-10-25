# Phase 3 — Skills & Progression Analysis

## Executive Summary
Progression rules define 0.1 increments, sweet-spot center 0.5, a single `slowdown_mode`, and anti-macro parameters. Docs reference 0.1 increments and sweet-spot; curves mapping is implied in some specs but not present in JSON.

## Findings
- 0.1 Increment System: present in `progression_rules.json.skill.increment = 0.1`; docs mention 0.1 increments.
- Sweet Spot Mechanic: `sweet_spot_center = 0.5` present.
- Slowdown Formulas: `slowdown_mode = "quadratic"` present; no `curves` profile map found.
- Anti-Macro: present (`repeat_window`, `penalty`).
- Stat Affinities: expected in `skills.json` (per-skill); ensure docs include affinity weighting and daily caps (present in JSON: stats.daily caps; `gain_on_skill_gain`).
- Skill Caps: present (per_skill=100, total_skills=700).

## Gaps & Inconsistencies
- Curves map absent: specs elsewhere reference multiple curve profiles; JSON currently declares a single `slowdown_mode` string.
- Ensure anti-macro description in docs matches JSON keys (`repeat_window`, `penalty`).

## Recommendations
- Either (a) add `curves` mapping to JSON or (b) align docs to the single `slowdown_mode` model; include acceptance examples.
- Document daily stat gain caps and `gain_on_skill_gain` explicitly in gameplay docs.

## Statistics
- slowdown_mode: quadratic
- anti_macro: enabled (window=30s, penalty=0.2)
- caps: per_skill 100, total 700, per_stat 100
