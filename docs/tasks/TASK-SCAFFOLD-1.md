- [ ] ID: TASK-SCAFFOLD-1
  Title: Project scaffolding & run/test commands
  Status: Proposed
  Notes: Provide developer convenience files and commands so `poetry run python -m game.main` works per docs.
  Subtasks:
  - [ ] Add `pyproject.toml` with project metadata and dependencies (Python 3.12+, arcade>=3.x)
  - [ ] Add `README.md` with run instructions: `poetry install` and `poetry run python -m game.main` or `make run`
  - [ ] Add `Makefile` or `.venv`-aware run scripts if desired
  - [ ] Add `tests/` skeleton and a smoke test that imports `game.main`
