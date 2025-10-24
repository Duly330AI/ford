# FORD • CONTRIBUTING.md

Willkommen! Dieses Dokument erklärt, **wie** du an FORD mitarbeitest – vom lokalen Setup über Code-Style & Tests bis zum PR-Prozess. Ziel: **kleine, getestete, deterministische** Beiträge ohne Reibung.

---

## 1) Voraussetzungen & Setup

**Benötigt**
- Python **3.13.5+**
- Poetry **≥ 1.8** (`pipx install poetry`)
- Git **≥ 2.40**
- (optional) Tiled Map Editor

**Projekt klonen & installieren**
```bash
git clone <repo-url> ford
cd ford
poetry install --no-root
pipx install pre-commit
pre-commit install
