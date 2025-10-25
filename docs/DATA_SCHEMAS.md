# FORD Data Schemas - Reference Guide

**Status:** Living Document • **Last Updated:** 2025-10-25

This document provides an overview of all JSON schemas used in FORD, including examples, validation rules, and cross-reference requirements.

---

## 📋 **Schema Overview**

FORD uses [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12/schema) for data validation.

| Schema | File | Purpose | Example Count |
|--------|------|---------|---------------|
| **Item** | `item.schema.json` | Items, weapons, armor, reagents | 121 items |
| **Skill** | `skill.schema.json` | Player skills and caps | 36 skills |
| **Spell** | `spell.schema.json` | Magic spells and effects | 36 spells |
| **Quest** | `quest.schema.json` | Quests and objectives | (Future) |
| **Vendor** | `vendor.schema.json` | NPC merchants | (Future) |
| **Biome** | `biome.schema.json` | Dungeon biomes | (Future) |
| **Encounter** | `encounter.schema.json` | Combat encounters | (Future) |

**Schema Location:** `data/schemas/*.schema.json`

---

## 🔧 **Validation Workflow**

```
┌────────────────────────────────────────────────────────────┐
│ 1. LOAD SCHEMA                                              │
│    └─> Read *.schema.json from data/schemas/               │
│                                                             │
│ 2. LOAD DATA                                                │
│    └─> Read *.json from data/ directory                    │
│                                                             │
│ 3. VALIDATE STRUCTURE                                       │
│    ├─> Required fields present?                            │
│    ├─> Data types correct?                                 │
│    ├─> Enum values valid?                                  │
│    └─> Additional properties allowed (flexibility)         │
│                                                             │
│ 4. CROSS-REFERENCE VALIDATION                              │
│    ├─> Spell reagents exist in items?                      │
│    ├─> Quest requirements reference valid items/skills?    │
│    ├─> Vendor inventories reference valid items?           │
│    └─> Biome reagent_bias references valid items?          │
│                                                             │
│ 5. REPORT RESULTS                                           │
│    ├─> [OK] if all validations pass                        │
│    ├─> [WARN] if soft violations (missing cross-refs)      │
│    └─> [FAIL] if hard violations (schema mismatch)         │
└────────────────────────────────────────────────────────────┘
```

**Validation Tool:** `scripts/validate_content.py`

```bash
# Validate all data files
python scripts/validate_content.py --root .

# Strict mode (warnings = errors)
python scripts/validate_content.py --root . --strict
```

---

## 📦 **Schema 1: Item**

**File:** `data/schemas/item.schema.json`
**Data:** `data/items.json`

### **Schema Definition:**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": true,
  "required": ["id", "type", "base_value"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9_]+$",
      "description": "Unique item identifier (snake_case)"
    },
    "name": {
      "type": "string",
      "description": "Display name (will move to i18n)"
    },
    "type": {
      "enum": ["weapon", "armor", "shield", "ammo", "reagent",
               "consumable", "material", "tool", "currency", "misc"],
      "description": "Item category"
    },
    "base_value": {
      "type": "number",
      "minimum": 0,
      "description": "Base gold value for economy"
    },
    "rarity": {
      "enum": ["common", "uncommon", "rare", "epic", "legendary"],
      "description": "Item rarity tier"
    },
    "weight": {
      "type": "number",
      "minimum": 0,
      "description": "Item weight in stones (optional)"
    }
  }
}
```

### **Example: Reagent**

```json
{
  "id": "reagent_bloodmoss",
  "name": "Blood Moss",
  "type": "reagent",
  "base_value": 5,
  "rarity": "common",
  "stack": 99,
  "weight": 0.1
}
```

### **Example: Weapon**

```json
{
  "id": "broadsword",
  "name": "Broadsword",
  "type": "weapon",
  "base_value": 75,
  "rarity": "uncommon",
  "stack": 1,
  "dmg": 10,
  "handed": 1,
  "dmg_type": "slash",
  "weight": 6.0
}
```

### **Validation Rules:**

- ✅ `id` must be unique across all items
- ✅ `id` must match `^[a-z0-9_]+$` (snake_case)
- ✅ `type` must be one of the enum values
- ✅ `base_value` ≥ 0
- ⚠️ `rarity` recommended but optional
- ⚠️ Extra fields allowed for flexibility (e.g., `dmg`, `armor`, `stack`)

---

## 🎓 **Schema 2: Skill**

**File:** `data/schemas/skill.schema.json`
**Data:** `data/skills.json`

### **Schema Definition:**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": true,
  "required": ["id", "display_name"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9_]+$",
      "description": "Unique skill identifier"
    },
    "display_name": {
      "type": "string",
      "description": "Skill display name (will move to i18n)"
    },
    "cap": {
      "type": "integer",
      "minimum": 0,
      "maximum": 100,
      "description": "Maximum skill value (default 100)"
    },
    "xp_curve": {
      "enum": ["linear", "exponential", "logarithmic"],
      "description": "XP gain curve type"
    }
  }
}
```

### **Example:**

```json
{
  "id": "magery",
  "display_name": "Magery",
  "cap": 100,
  "xp_curve": "linear"
}
```

### **Validation Rules:**

- ✅ `id` must be unique across all skills
- ✅ `id` must match `^[a-z0-9_]+$`
- ✅ `display_name` required (temporary, will move to i18n)
- ✅ `cap` must be 0-100
- ⚠️ Extra fields allowed (e.g., `stat_bonuses`, `synergies`)

---

## ✨ **Schema 3: Spell**

**File:** `data/schemas/spell.schema.json`
**Data:** `data/spells.json`

### **Schema Definition:**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": true,
  "required": ["id", "name", "school", "circle", "cost"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9_]+$"
    },
    "name": {
      "type": "string",
      "description": "Spell display name"
    },
    "school": {
      "type": "string",
      "enum": ["fire", "cold", "toxic", "energy", "earth", "arcanum"]
    },
    "circle": {
      "type": "integer",
      "minimum": 1,
      "maximum": 8
    },
    "cost": {
      "type": "object",
      "required": ["mana"],
      "properties": {
        "mana": {
          "type": "integer",
          "minimum": 0
        },
        "reagents": {
          "type": "object",
          "additionalProperties": {
            "type": "integer",
            "minimum": 1
          },
          "description": "Map of reagent_id -> quantity"
        }
      }
    },
    "cast_rounds": {
      "type": "integer",
      "minimum": 0
    },
    "range_tiles": {
      "type": "integer",
      "minimum": 0
    },
    "effects": {
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "fizzle": {
      "type": "object",
      "properties": {
        "base": {
          "type": "number",
          "minimum": 0,
          "maximum": 1
        },
        "magery_factor": {
          "type": "number"
        }
      }
    }
  }
}
```

### **Example:**

```json
{
  "id": "fireball",
  "name": "Fireball",
  "school": "fire",
  "circle": 3,
  "cost": {
    "mana": 12,
    "reagents": {
      "reagent_black_pearl": 1,
      "reagent_sulfurous_ash": 2
    }
  },
  "cast_rounds": 0,
  "range_tiles": 8,
  "effects": [
    {
      "type": "damage",
      "element": "fire",
      "base": 18,
      "variance_pct": 0.2,
      "scaling": {
        "INT": 0.15
      }
    }
  ],
  "fizzle": {
    "base": 0.12,
    "magery_factor": -0.002
  },
  "resist_check": {
    "type": "resist_spells",
    "scale": 200
  }
}
```

### **Validation Rules:**

- ✅ `id` must be unique across all spells
- ✅ `school` must be valid enum
- ✅ `circle` must be 1-8
- ✅ `cost.reagents` keys must reference valid item IDs (cross-ref)
- ⚠️ `effects` structure is flexible (additionalProperties: true)

---

## 📜 **Schema 4: Quest**

**File:** `data/schemas/quest.schema.json`
**Data:** `data/quests/*.json` (Future)

### **Schema Definition:**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": true,
  "required": ["id", "display_name"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9_]+$"
    },
    "display_name": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "objectives": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["type", "target"],
        "properties": {
          "type": {
            "enum": ["kill", "collect", "escort", "explore", "interact"]
          },
          "target": {
            "type": "string",
            "description": "Monster ID, Item ID, or Location ID"
          },
          "count": {
            "type": "integer",
            "minimum": 1
          }
        }
      }
    },
    "rewards": {
      "type": "object",
      "properties": {
        "gold": {
          "type": "integer"
        },
        "items": {
          "type": "array",
          "items": {
            "type": "string",
            "description": "Item ID"
          }
        },
        "xp": {
          "type": "integer"
        }
      }
    }
  }
}
```

### **Example:**

```json
{
  "id": "clear_the_crypt",
  "display_name": "Clear the Crypt",
  "description": "Defeat the skeletal guardians in the old crypt.",
  "objectives": [
    {
      "type": "kill",
      "target": "skeleton",
      "count": 10
    },
    {
      "type": "kill",
      "target": "skeleton_captain",
      "count": 1
    }
  ],
  "rewards": {
    "gold": 500,
    "items": ["iron_ingot", "iron_ingot", "iron_ingot"],
    "xp": 1000
  }
}
```

### **Validation Rules:**

- ✅ `objectives[].target` must reference valid monster/item/location ID (cross-ref)
- ✅ `rewards.items[]` must reference valid item IDs (cross-ref)
- ⚠️ Quest chains via `prerequisites` field (future)

---

## 🛒 **Schema 5: Vendor**

**File:** `data/schemas/vendor.schema.json`
**Data:** `data/vendors/*.json` (Future)

### **Schema Definition:**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": true,
  "required": ["id", "display_name"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9_]+$"
    },
    "display_name": {
      "type": "string"
    },
    "inventory": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["item_id"],
        "properties": {
          "item_id": {
            "type": "string"
          },
          "stock": {
            "type": "integer",
            "description": "-1 for infinite"
          },
          "restock_hours": {
            "type": "number"
          },
          "price_mult": {
            "type": "number",
            "description": "Multiplier on base_value"
          }
        }
      }
    }
  }
}
```

### **Example:**

```json
{
  "id": "abbey_herbalist",
  "display_name": "Abbey Herbalist",
  "location": "abbey_courtyard",
  "inventory": [
    {
      "item_id": "reagent_ginseng",
      "stock": 20,
      "restock_hours": 24,
      "price_mult": 1.0
    },
    {
      "item_id": "reagent_garlic",
      "stock": 30,
      "restock_hours": 24,
      "price_mult": 1.0
    },
    {
      "item_id": "heal_potion",
      "stock": 10,
      "restock_hours": 12,
      "price_mult": 1.5
    }
  ]
}
```

### **Validation Rules:**

- ✅ `inventory[].item_id` must reference valid item ID (cross-ref)
- ⚠️ `price_mult` defaults to 1.0 if omitted
- ⚠️ `stock: -1` means infinite supply

---

## 🌍 **Schema 6: Biome**

**File:** `data/schemas/biome.schema.json`
**Data:** `data/biomes/*.json` (Future)

### **Schema Definition:**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": true,
  "required": ["id", "display_name"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9_]+$"
    },
    "display_name": {
      "type": "string"
    },
    "tileset": {
      "type": "string"
    },
    "reagents_bias": {
      "type": "array",
      "items": {
        "type": "string",
        "description": "Item ID of reagent"
      }
    },
    "encounter_tables": {
      "type": "array",
      "items": {
        "type": "string",
        "description": "Encounter table ID"
      }
    }
  }
}
```

### **Example:**

```json
{
  "id": "crypt_undead",
  "display_name": "Ancient Crypt",
  "tileset": "crypt_stone",
  "ambient_light": 0.2,
  "reagents_bias": [
    "reagent_grave_dust",
    "reagent_nightshade",
    "reagent_bat_wing"
  ],
  "encounter_tables": [
    "crypt_weak",
    "crypt_medium",
    "crypt_boss"
  ]
}
```

### **Validation Rules:**

- ✅ `reagents_bias[]` items must reference valid item IDs (cross-ref)
- ✅ `encounter_tables[]` must reference valid encounter table IDs (cross-ref)

---

## ⚔️ **Schema 7: Encounter**

**File:** `data/schemas/encounter.schema.json`
**Data:** `data/encounters/*.json` (Future)

### **Schema Definition:**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": true,
  "required": ["id", "enemies"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9_]+$"
    },
    "enemies": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["monster_id", "count"],
        "properties": {
          "monster_id": {
            "type": "string"
          },
          "count": {
            "type": "object",
            "properties": {
              "min": {
                "type": "integer",
                "minimum": 1
              },
              "max": {
                "type": "integer",
                "minimum": 1
              }
            }
          }
        }
      }
    },
    "threat_budget": {
      "type": "number",
      "description": "Total encounter difficulty"
    }
  }
}
```

### **Example:**

```json
{
  "id": "crypt_weak",
  "enemies": [
    {
      "monster_id": "skeleton",
      "count": {
        "min": 2,
        "max": 4
      }
    }
  ],
  "threat_budget": 100,
  "loot_table": "crypt_common"
}
```

### **Validation Rules:**

- ✅ `enemies[].monster_id` must reference valid monster ID (cross-ref)
- ✅ `loot_table` must reference valid loot table ID (cross-ref)

---

## 🔗 **Cross-Reference Rules**

### **Spell → Item (Reagents):**

```python
# Validation
for spell in spells:
    for reagent_id in spell['cost']['reagents'].keys():
        assert reagent_id in item_ids, f"Spell {spell['id']} references unknown reagent {reagent_id}"
```

**Example:**

```json
// spell fireball references reagents
"reagents": {
  "reagent_black_pearl": 1,  // ✅ Must exist in items.json
  "reagent_sulfurous_ash": 2 // ✅ Must exist in items.json
}
```

### **Quest → Item (Rewards):**

```python
for quest in quests:
    for item_id in quest['rewards']['items']:
        assert item_id in item_ids, f"Quest {quest['id']} rewards unknown item {item_id}"
```

### **Vendor → Item (Inventory):**

```python
for vendor in vendors:
    for inv_entry in vendor['inventory']:
        assert inv_entry['item_id'] in item_ids, f"Vendor {vendor['id']} sells unknown item"
```

### **Biome → Item (Reagent Bias):**

```python
for biome in biomes:
    for reagent_id in biome['reagents_bias']:
        assert reagent_id in item_ids, f"Biome {biome['id']} references unknown reagent"
```

---

## ✅ **Validation Best Practices**

### **DO:**

- ✅ Always validate data files before committing
- ✅ Use `--strict` mode in CI/CD pipeline
- ✅ Add new fields to schemas as needed (additionalProperties: true)
- ✅ Document schema changes in this file
- ✅ Test cross-references with realistic data
- ✅ Use semantic versioning for schema changes

### **DON'T:**

- ❌ Hardcode validation logic (use schemas)
- ❌ Remove required fields without migration
- ❌ Use display names in cross-references (use IDs)
- ❌ Skip validation "just this once"
- ❌ Make schemas too rigid (allow extra fields)

---

## 🧪 **Testing Validation**

### **Run Validation:**

```bash
# Validate all data
python scripts/validate_content.py --root .

# Expected output:
# [OK]   data/items.json: 121 items
# [OK]   data/skills.json: 36 skills
# [OK]   data/spells.json: 36 spells
# [DONE] Validation complete with 0 warning(s).
```

### **Test Failure Scenarios:**

```bash
# Missing required field
{
  "id": "test_item"
  // ❌ Missing "type" and "base_value"
}
# Error: 'type' is a required property

# Invalid enum value
{
  "id": "test_item",
  "type": "invalid_type",  // ❌ Not in enum
  "base_value": 10
}
# Error: 'invalid_type' is not one of ['weapon', 'armor', ...]

# Cross-reference failure
{
  "id": "test_spell",
  "cost": {
    "reagents": {
      "unknown_reagent": 1  // ❌ Not in items.json
    }
  }
}
# Warning: spell test_spell: reagent 'unknown_reagent' not found
```

---

## 📊 **Schema Versioning**

### **Version History:**

| Version | Date | Changes |
|---------|------|---------|
| **1.0** | 2025-10-25 | Initial schemas for items, skills, spells |
| **1.1** | (Future) | Add quest, vendor, biome, encounter schemas |
| **2.0** | (Future) | Move display_name to i18n, enforce stricter validation |

### **Breaking Changes:**

When making breaking changes to schemas:

1. **Increment major version** (1.0 → 2.0)
2. **Provide migration script** (`scripts/migrate_v1_to_v2.py`)
3. **Update this document** with migration guide
4. **Test with all existing data**
5. **Announce in CHANGELOG.md**

---

## 📁 **Related Files**

- **Schemas:** `data/schemas/*.schema.json`
- **Data:** `data/*.json` and `data/*/*.json`
- **Validator:** `scripts/validate_content.py`
- **Conventions:** `docs/CONVENTIONS.md`
- **Docs:** `docs/ITEMIZATION_DESIGN.md` (item-specific design)
- **Docs:** `docs/MAGIC_SYSTEM.md` (spell-specific design)

---

## 🔧 **Schema Tools**

### **Generate Sample Data:**

```python
# scripts/generate_sample_from_schema.py
import json
from jsonschema import Draft202012Validator

schema = json.load(open('data/schemas/item.schema.json'))
# Use faker or hypothesis to generate valid samples
```

### **Validate Single File:**

```python
import json
from jsonschema import Draft202012Validator

schema = json.load(open('data/schemas/item.schema.json'))
data = json.load(open('data/items.json'))
validator = Draft202012Validator(schema)

for item in data:
    errors = list(validator.iter_errors(item))
    if errors:
        print(f"Item {item['id']} has errors:")
        for err in errors:
            print(f"  - {err.message}")
```

---

**Questions?** Check `docs/CONVENTIONS.md` for naming rules and `scripts/README_VALIDATE.md` for validation workflow.
