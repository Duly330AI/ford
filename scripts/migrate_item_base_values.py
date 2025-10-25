#!/usr/bin/env python3
"""
Add base_value to all items in items.json based on rarity and type.
Usage: python scripts/migrate_item_base_values.py
"""
import json
from pathlib import Path

# Base values by rarity
RARITY_BASE_VALUES = {
    "common": 5,
    "uncommon": 25,
    "rare": 100,
    "epic": 500,
    "legendary": 2000,
}

# Type multipliers (some types are worth more/less)
TYPE_MULTIPLIERS = {
    "weapon": 3.0,       # Weapons more valuable
    "armor": 2.5,        # Armor valuable
    "shield": 2.0,       # Shields decent
    "reagent": 1.0,      # Base price
    "consumable": 1.5,   # Potions/food
    "material": 0.5,     # Raw materials cheaper
    "tool": 1.2,         # Tools moderate
    "ammo": 0.3,         # Ammo cheap (stackable)
    "currency": 1.0,     # Gold is gold
    "misc": 1.0,         # Default
}


def calculate_base_value(item: dict) -> int:
    """Calculate base_value for an item based on rarity and type."""
    rarity = item.get("rarity", "common")
    item_type = item.get("type", "misc")

    base = RARITY_BASE_VALUES.get(rarity, 5)
    multiplier = TYPE_MULTIPLIERS.get(item_type, 1.0)

    return max(1, int(base * multiplier))


def migrate_items(items_path: Path) -> tuple[int, int]:
    """
    Add base_value to all items in items.json.

    Returns:
        (items_modified, total_items)
    """
    with open(items_path, 'r', encoding='utf-8') as f:
        items = json.load(f)

    items_modified = 0

    for item in items:
        item_id = item.get('id', '???')

        if 'base_value' not in item:
            base_value = calculate_base_value(item)
            item['base_value'] = base_value
            items_modified += 1
            print(f"  {item_id}: base_value = {base_value} (rarity={item.get('rarity')}, type={item.get('type')})")
        else:
            print(f"  {item_id}: already has base_value = {item['base_value']}")

    # Write back
    with open(items_path, 'w', encoding='utf-8') as f:
        json.dump(items, f, indent=2, ensure_ascii=False)

    return items_modified, len(items)


def main():
    project_root = Path(__file__).parent.parent
    items_path = project_root / 'data' / 'items.json'

    if not items_path.exists():
        print(f"ERROR: {items_path} not found")
        return 1

    print(f"🔄 Adding base_value to items in {items_path}...")
    items_modified, total_items = migrate_items(items_path)

    print(f"\n✅ Migration complete!")
    print(f"   Items modified: {items_modified}")
    print(f"   Total items: {total_items}")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
