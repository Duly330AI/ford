- [ ] ID: TASK-TOOLING-1
  Title: Developer tooling (formatters, tests, CI)
  Status: Proposed
  Notes: Minimal recommended tools: `black`, `ruff`, `pytest`, `pre-commit`, GitHub Actions workflow.
  Subtasks:
  - [ ] Add `requirements-dev.txt` or `[tool.poetry.dev-dependencies]` entries
  - [ ] Add pre-commit config + sample hooks (black, ruff)
  - [ ] Add GitHub Actions workflow: `ci.yml` that runs tests and lint
