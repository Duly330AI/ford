# FORD — Single-player 2D Dungeon Crawler (prototype)

Short: Prototype in Python + arcade. This repo is a scaffold and uses Poetry for package management.

Quick start (Windows PowerShell)

```powershell
# 1) (optional) create & activate venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2) install poetry or use pip + dependencies; preferred: poetry
# poetry install

# 3) run (via poetry) or directly (if venv active)
# poetry run python -m game.main
python -m game.main
```

Pre-commit (recommended)

Install and enable locally:

```powershell
# Install via pipx (recommended)
pipx install pre-commit
# Install hook into local repo
pre-commit install
# Run checks locally
pre-commit run --all-files
```

Notes
- The project expects assets and data under `data/` and game code under `game/` (see `docs/start.md`).
- There is a sample `pyproject.toml` and pre-commit config. Update dependency versions as needed.