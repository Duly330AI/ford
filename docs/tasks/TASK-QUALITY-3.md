- [ ] ID: TASK-QUALITY-3
  Title: Commit Message Linting (Conventional Commits Enforcement)
  Status: Proposed
  Priority: P2
  Owner: Copilot Agent
  Created: 2025-10-25
  Artifacts: $_, $_, $_
  DependsOn: -
  Notes:
  Configure a commit message linter (commitlint or gitlint) enforcing `type(scope): subject` with allowed types feat, fix, test, refactor, chore, docs, style, perf, ci, build.
  Provide examples in docs/CONTRIBUTING.md showing valid patterns and common failures, aligning with repository workflow.
  Optionally add a pre-commit hook that warns (non-blocking) on invalid messages while CI blocks merges with bad commits.
  Validate PR titles and commits in CI using the new workflow.
  Acceptance:
  - [ ] Commit linting config rejects non-conforming messages.
  - [ ] Pre-commit hook warns developers about invalid messages (skippable).
  - [ ] CI workflow fails when commit messages or PR title violate the convention.
  - [ ] CONTRIBUTING.md documents the allowed types and examples.
  Tests:
  - [ ] tests/ci/test_commitlint_config.py::test_valid_examples
  - [ ] tests/ci/test_commitlint_config.py::test_invalid_examples
  - [ ] tests/ci/test_commitlint_ci_integration.py::test_workflow_runs
