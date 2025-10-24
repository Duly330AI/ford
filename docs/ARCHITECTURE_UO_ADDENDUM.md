# ARCHITECTURE – UO Addendum

## Datenfluss (Skills)
1. **Event**: `onSkillUse(skillId, context)` ermittelt `p_success` (z. B. HitChance).
2. **Lookup**: `skills.json[skillId].xp_curve` → `progression_rules.json.curves[curveName]`.
3. **Formel**: `progression_rules.json.skill` + Kurvenprofil bestimmen `P(gain)` (Chance auf **+0.1**).
4. **Stat-Gains**: bei Skill-Gain Roll auf STR/DEX/INT/STAM gemäß `skills.json[skillId].stats` und `progression_rules.json.stats`.
5. **Caps**: `progression_rules.json.caps` (per Skill, total, per Stat).

## Datenfluss (Kampf)
- **combat_rules.json** versorgt das Kampfsystem: `hit_chance`, `parry`, `damage`, `movement`, `recovery`, `initiative`, `dodge`.
- Optional kann jede Waffe einen `base_delay` tragen; sonst greift die Map in `combat_rules.recovery.weapon_base_delay`.

## Engagement & Zeit
- **Encounter-Bubble** (R=12 Tiles), alle Gegner mit LOS joinen; neue Gegner treten am Rundenbeginn bei.
- **Rundenzeit**: 1 Runde = 3 s. Crafting läuft auf Rundenzeit weiter (Outputs markiert), Node-Respawn pausiert (Default).
- **Escape**: LOS-frei + Distanz ≥ *leash_break* (10 Tiles) über 1 volle Runde → Overworld.
