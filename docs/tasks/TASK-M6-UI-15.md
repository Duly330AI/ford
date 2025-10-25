- [ ] ID: TASK-M6-UI-15
  Title: Accessibility (Font Scaling, Colorblind Modes, Contrast, Labeled Icons)
  Status: Proposed
  Priority: P1
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: `game/ui/accessibility.py`, `tests/ui/test_accessibility.py`
  DependsOn: TASK-M6-UI-01
  Notes:
  Implement accessibility options from UI_SPEC_UO_STYLE.md Section 12: font sizes, colorblind palettes, contrast boost, and icon labels.
  Add delayed tooltip timing, keyboard remapping shortcuts, and controller radial menus for context actions.
  Persist settings per profile and expose quick toggles for testing.
  Acceptance:
  - [ ] Font scaling presets (S, M, L, XL) adjust text across UI panes.
  - [ ] Colorblind profiles adjust palettes and legends.
  - [ ] Contrast boost increases readability without clipping styles.
  - [ ] Icon labels or legend mode can be toggled on demand.
  Tests:
  - [ ] tests/ui/test_accessibility.py::test_font_scaling
  - [ ] tests/ui/test_accessibility.py::test_colorblind_profiles
  - [ ] tests/ui/test_accessibility.py::test_contrast_boost
