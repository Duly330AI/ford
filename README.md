# FORD — Single-player 2D Ultima Online Roguelike Dungeon Crawler mit Systemen (prototype)

Short: Prototype in Python + arcade. This repo is a scaffold and uses Poetry for package management.

## Quick Start

### Prerequisites

- **Windows 10+** or **macOS/Linux**
- **Git** (with Git Bash for Windows)
- **Conda** (Miniconda/Anaconda) or **Python 3.12+**
- **Poetry** (for dependency management)

### 1. Clone & Setup Environment (Git Bash / macOS / Linux)

```bash
# Clone repository
git clone https://github.com/Duly330AI/ford.git
cd ford

# Create conda environment (or use existing)
conda create -n ford python=3.12
conda activate ford

# Install Poetry
conda install poetry
# or: pip install poetry

# Install dependencies
poetry install --no-root
```

### 2. Running the Game

```bash
# Via Poetry (recommended)
poetry run python -m game.main

# Or if conda environment active:
python -m game.main
```

### 3. Development Setup (Optional)

```bash
# Install pre-commit hooks
pre-commit install

# Run linters and tests
poetry run pytest -v
poetry run ruff check .
poetry run black .
```

### Alternative: PowerShell (Windows)

If you prefer PowerShell instead of Git Bash:

```powershell
# Same steps, but use PowerShell syntax
conda activate ford
poetry install --no-root
poetry run python -m game.main
```

### Using Helper Script (Optional)

For faster development with predefined commands:

```bash
# Git Bash / macOS / Linux
source dev.sh
dev-help          # Show all available commands
install-deps      # Install dependencies
install-hooks     # Setup pre-commit
run-game          # Start FORD
lint-all          # Run all linters
```

## Code Quality

### Pre-commit Hooks (Recommended)

Automatically run linters and formatters before each commit:

```bash
# Install via Poetry (already included)
pre-commit install

# Run checks on all files
pre-commit run --all-files

# Run checks on staged files only
pre-commit run
```

### Manual Quality Checks

```bash
# Type checking
poetry run pylance check game/

# Linting
poetry run ruff check .
poetry run ruff check . --fix

# Formatting
poetry run black .

# Tests
poetry run pytest -v
poetry run pytest -m "not slow" -q
```

## Notes

- The project expects assets and data under `data/` and game code under `game/` (see `docs/DEVELOPMENT.md`).
- There is a sample `pyproject.toml` and pre-commit config. Update dependency versions as needed.
- **Audio assets** (436 WAV files) are included in `audio/sfx/`. See `docs/AUDIO_SYSTEM.md`.
- **LLM Agents:** VS Code is configured with Git Bash as default terminal. See `docs/LLM_AGENT_GUIDELINES.md`.

## Documentation

- **Getting Started:** `docs/DEVELOPMENT.md` (setup, commands, troubleshooting)
- **Architecture:** `docs/ARCHITECTURE_UO_ADDENDUM.md`
- **Combat System:** `docs/COMBAT_RULES.md`
- **Magic System:** `docs/AUDIO_SYSTEM.md`
- **Audio System:** `docs/AUDIO_SYSTEM.md`
- **Project Tasks:** `docs/task.md`
- **Contributing:** `CONTRIBUTING.md`
- **For LLM Agents:** `docs/LLM_AGENT_GUIDELINES.md`

## License

CC0 Public Domain (see `ATTRIBUTIONS.md` for asset sources)
