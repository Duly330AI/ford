Hier ist eine vollständige, pragmatische **`TOOLING.md`** für FORD. Kopier sie 1:1 ins Repo.

````markdown
# FORD • TOOLING.md

Ziel: Reproduzierbare Dev-Umgebung (Windows/macOS/Linux), **eine** Kommandooberfläche (Poetry/Make), sauberes Linting/Formatting, zuverlässige Tests + CI, Datenvalidierung und Headless-Strategien für Arcade.

---

## 1) Systemvoraussetzungen

- **Python**: 3.13.5+
- **Poetry**: >= 1.8 (`pipx install poetry`)
- **Git**: >= 2.40
- **Tiled** (Map-Editor, optional): https://www.mapeditor.org/
- **VS Code** (empfohlen) + empfohlene Extensions (siehe unten)

**GPU/GL**: Arcade nutzt OpenGL über Pyglet. Unit-Tests der Logik sind **headless**; GL/Scene-Teile werden „gesmoke-testet“ oder per Marker **geskippt**.

---

## 2) Projekt aufsetzen

```bash
# Klonen
git clone <repo-url> ford
cd ford

# Abhängigkeiten
poetry install --no-root

# Pre-commit (optional aber empfohlen)
pipx install pre-commit
pre-commit install
````

**Starten (lokal)**

```bash
poetry run python -m game.main
# oder via Make:
make run
```

**Tests**

```bash
poetry run pytest -q                         # schnell
poetry run pytest -q -m "slow"               # Monte-Carlo/Perf
```

---

## 3) Ordner & wichtige Dateien

```
.vscode/                # Editor-Empfehlungen (extensions, settings, launch, tasks)
.github/workflows/      # CI (ci.yml, nightly.yml)
data/                   # JSON-Daten + schemas/
game/                   # Code (scenes/, systems/, util/, entities/)
tests/                  # Unit/Integration/Perf/Smoke
saves/                  # Save-Slots (wird zur Laufzeit angelegt)
```

---

## 4) VS Code Einrichtung

**Empfohlene Extensions**

* Python (ms-python.python), Pylance, Ruff (astral-sh.ruff), Black Formatter
* GitHub Copilot + Copilot Chat
* GitLens, Error Lens, Even Better TOML, YAML, Jupyter
* Path Intellisense, Todo Tree, Shader languages support

`/.vscode/extensions.json`

```json
{
  "recommendations": [
    "ms-python.python",
    "ms-python.vscode-pylance",
    "astral-sh.ruff",
    "ms-python.black-formatter",
    "tamasfe.even-better-toml",
    "GitHub.copilot",
    "GitHub.copilot-chat",
    "eamodio.gitlens",
    "usernamehw.errorlens",
    "redhat.vscode-yaml",
    "ms-toolsai.jupyter",
    "christian-kohler.path-intellisense",
    "Gruntfuggly.todo-tree",
    "slevesque.shader"
  ]
}
```

`/.vscode/settings.json` (Ausschnitt)

```json
{
  "python.analysis.typeCheckingMode": "basic",
  "editor.formatOnSave": true,
  "[python]": { "editor.defaultFormatter": "ms-python.black-formatter" },
  "editor.codeActionsOnSave": {
    "source.organizeImports.ruff": true,
    "source.fixAll.ruff": true
  },
  "ruff.lint.enable": true,
  "ruff.organizeImports": true,
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": ["tests"],
  "editor.rulers": [100]
}
```

`/.vscode/launch.json`

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Run FORD",
      "type": "python",
      "request": "launch",
      "module": "game.main",
      "justMyCode": true,
      "console": "integratedTerminal",
      "env": { "PYTHONHASHSEED": "0" }
    }
  ]
}
```

`/.vscode/tasks.json`

```json
{
  "version": "2.0.0",
  "tasks": [
    { "label": "poetry: install", "type": "shell", "command": "poetry install" },
    { "label": "run", "type": "shell", "command": "poetry run python -m game.main" },
    { "label": "tests", "type": "shell", "command": "poetry run pytest -q" }
  ]
}
```

---

## 5) Makefile (einheitliche Befehle)

`Makefile`

```makefile
.PHONY: run test test-slow lint fmt validate bench clean

run:
\tpoetry run python -m game.main

test:
\tpoetry run pytest -q -m "not slow"

test-slow:
\tpoetry run pytest -q -m "slow"

lint:
\tpoetry run ruff check .
\tpoetry run ruff format --check .

fmt:
\tpoetry run ruff format .
\tpoetry run ruff check . --fix

validate:
\tpoetry run python -m game.tools.validate_data

bench:
\tpoetry run pytest -q tests/perf -m "slow"

clean:
\trm -rf .pytest_cache .ruff_cache **/__pycache__
```

---

## 6) Linting & Formatting

* **Ruff** für Lint/Imports, **Black** für Format.
* Konfiguration im `pyproject.toml`:

```toml
[tool.black]
line-length = 100
target-version = ["py313"]

[tool.ruff]
line-length = 100
target-version = "py313"
lint.select = ["E","F","I","N","UP","ARG","B"]
lint.ignore = ["E203"] # Black-Kompatibilität
```

Schnelllauf:

```bash
poetry run ruff check . && poetry run ruff format .
```

---

## 7) Tests & Coverage

* **Pytest** mit Markern:

  * `@pytest.mark.slow` – Monte-Carlo/Perf
  * `@pytest.mark.integration` – Integrations-/Flow-Tests
* **Headless-Regel**: Keine Arcade/GL-Abhängigkeit in `systems/*`.
  GL-nahe Module nur als **Import-Smoketests**.
* **Determinismus**: RNG in Tests **immer seeden** (`random.seed(1337)`); `PYTHONHASHSEED=0`.

Optionale Dateien:

`pytest.ini`

```ini
[pytest]
testpaths = tests
addopts = -q
markers =
    slow: Long-running or Monte-Carlo tests
    integration: Integration/flow tests
```

`.coveragerc` (optional)

```ini
[run]
branch = True
source = game
omit =
    game/scenes/*
    game/assets/*
[report]
fail_under = 85
show_missing = True
```

---

## 8) Pre-commit Hooks

`.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: check-json
      - id: check-toml
      - id: check-yaml
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.5
    hooks:
      - id: ruff
      - id: ruff-format
```

Aktivieren:

```bash
pipx install pre-commit
pre-commit install
```

---

## 9) Datenvalidierung (Schemas)

* Alle `data/*.json` werden gegen `data/schemas/*.schema.json` geprüft.
* CLI-Tool (empfohlen): `game/tools/validate_data.py`

Beispiel-Aufruf:

```bash
poetry run python -m game.tools.validate_data
```

**CI bricht ab**, wenn:

* IDs doppelt/fehlen,
* Referenzen (item_id/table_id/recipe_id/skill_id) ungültig sind,
* Zyklen in Loot-Tabellen bestehen,
* Werte außerhalb der erlaubten Bereiche liegen.

---

## 10) Continuous Integration (GitHub Actions)

`/.github/workflows/ci.yml`

```yaml
name: ci
on:
  push:
  pull_request:
jobs:
  test:
    runs-on: ubuntu-latest
    env:
      PYTHONHASHSEED: "0"
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.13"
          cache: "poetry"
      - name: Install Poetry
        run: pipx install poetry
      - name: Install deps
        run: poetry install --no-interaction --no-ansi
      - name: Lint
        run: |
          poetry run ruff check .
          poetry run ruff format --check .
      - name: Validate data
        run: poetry run python -m game.tools.validate_data
      - name: Tests (fast)
        run: poetry run pytest -q -m "not slow"
```

`/.github/workflows/nightly.yml` (Slow/Perf)

```yaml
name: nightly
on:
  schedule:
    - cron: "0 2 * * *"
jobs:
  slow:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.13"
          cache: "poetry"
      - name: Install Poetry
        run: pipx install poetry
      - name: Deps
        run: poetry install --no-interaction --no-ansi
      - name: Slow/Perf tests
        run: poetry run pytest -q -m "slow"
```

---

## 11) Git-Workflow & Commits

* **Kurzlebige Feature-Branches**: `feat/<kurz>`, `fix/<kurz>`, `chore/<kurz>`
* **Conventional Commits**:

  * `feat: add initiative order`
  * `fix: correct loot roll`
  * `test: add crafting failure cases`
  * `refactor: split combat`
* **PR-Richtlinie**: klein halten (< ~400 LOC), Tests & Lint grün, Daten validiert.

---

## 12) Umgebungsvariablen

* `FORD_SEED`: Integer-Seed (überschreibt Config)
* `FORD_SIZE`: Mapgröße (z. B. `128x128`)
* `ARCADE_HEADLESS`: `1` → GL-abhängige Tests **skippen**
* `PYTHONHASHSEED`: `0` (Determinismus)

Beispiel:

```bash
FORD_SEED=1337 poetry run python -m game.main
```

---

## 13) Headless/GL-Strategie

* **Kernlogik** in `systems/*` und `util/*` **ohne Arcade** halten.
* Tests, die Arcade/GL bräuchten → **skip**, z. B.:

```python
import os, pytest
pytestmark = pytest.mark.skipif(os.environ.get("ARCADE_HEADLESS") != "1",
                                reason="Requires headless GL; skipped in CI")
```

* Scene/UI nur **Import-Smoketests**, kein Rendern in CI.

---

## 14) Performance & Profiling

* Mikro-Profiler (`game/util/prof.py`) für zeitkritische Pfade (BSP, Culling, Collision, Combat).
* Benchmarks unter `tests/perf/` (als `@pytest.mark.slow`).
* Zielwerte:

  * BSP 128×128 < 50 ms Ø (CI, M1)
  * 1 Runde (1P+3E) Logik < 2 ms Ø (CI, M2)
  * 100k Loot-Rolls < 250 ms (CI, M3)
  * 2.000 Node-Ticks < 1 ms Logik (CI, M4)
  * Save+Write < 50 ms (M5)

---

## 15) Assets & Pixel-Policy

* **Nur CC0/CC-BY** Platzhalter. Quellen in `ATTRIBUTIONS.md`.
* **Tiles**: 16×16, **on-screen** 64 px (Scale=4). **Keine** Subpixel-Bewegung (Integer-Kamera).
* **Atlas** optional: `assets/atlas/` (kann später gebacken werden).
* **SFX**: Platzhalter in `assets/sfx/`, per Adapter (`util/audio_adapter.py`) angebunden.

---

## 16) Optional: Typprüfung (mypy)

Aktivieren (optional):

```toml
[tool.mypy]
python_version = "3.13"
warn_unused_ignores = true
warn_redundant_casts = true
disallow_untyped_defs = true
strict_optional = true
```

Lauf:

```bash
poetry run mypy game
```

---

## 17) Datenpflege & Migrationsregeln

* Änderungen an `data/*.json` nur **additiv**, keine ID-Reuse.
* Breaking Schema → `schemas/*` bump + Migration (siehe M5).
* `validate_data` **muss grün** sein, bevor PR landet.

---

## 18) Troubleshooting

* **ImportError: arcade/pyglet** → Poetry-Env prüfen, `poetry run python -c "import arcade"`
* **GL-Fehler in CI** → GL-Tests sind zu entfernen/skippen; Logik darf nicht von Arcade abhängen.
* **Windows Pfade** → vermeide `\` in Datenpfaden; nutze `pathlib`.
* **Unicode/UTF-8** → Editor auf `LF` und UTF-8 (VS Code `files.eol: "\n"`).

---

## 19) Release & Versionierung

* **SemVer**: `0.x` in Entwicklung; Tags `v0.1.0`, `v0.2.0` …
* **CHANGELOG.md** pflegen (Unreleased/Added/Changed/Fixed).
* **Save-Schema-Version** wird in Save-Datei gesichert (M5), Migrationen testen.

---

## 20) Schnelle Befehle (Cheatsheet)

```bash
poetry install                         # Setup
make run                               # Spiel starten
make test                              # schnelle Tests
make test-slow                         # langsame/Perf-Tests
make lint && make fmt                  # prüfen/formatieren
make validate                          # Datenvalidierung
```

```

**Hinweis:** Wenn du möchtest, liefere ich dir zusätzlich `game/tools/validate_data.py` (CLI), ein fertiges `Makefile`, `pyproject.toml` (Poetry-Gruppen inkl. dev) und die beiden CI-Workflows als Dateien – passend zu dieser Doku.
```
