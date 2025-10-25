#!/usr/bin/env python3
import json, sys, os

def flatten(d, prefix=""):
    for k, v in d.items():
        key = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            yield from flatten(v, key)
        else:
            yield key

def main():
    # Get project root (go up 2 levels from scripts/i18n/)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(os.path.dirname(script_dir))
    en_path = os.path.join(root, "i18n", "en.json")
    langs = ["de.json"]
    base = json.load(open(en_path, "r", encoding="utf-8"))
    base_keys = set(flatten(base))

    failed = 0
    for lang in langs:
        lp = os.path.join(root, "i18n", lang)
        data = json.load(open(lp, "r", encoding="utf-8"))
        keys = set(flatten(data))
        missing = base_keys - keys
        extra = keys - base_keys
        if missing:
            print(f"[FAIL] {lang}: missing keys:", sorted(missing))
            failed += 1
        if extra:
            print(f"[WARN] {lang}: extra keys:", sorted(extra))
    if failed:
        sys.exit(1)
    print("[OK] i18n keys match base.")
if __name__ == "__main__":
    main()
