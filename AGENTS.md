# strkit: notes for AI agents and automated reviewers

- Python 3.10+, standard library only. No runtime dependencies may be added.
- Source is in `src/strkit/`; tests are in `tests/`. `pytest` also runs doctests in `src/`.
- Required checks: `lint` (`ruff check .` and `ruff format --check .`) and `test` (`pytest`).
- Public functions need type hints, a docstring with a doctest, an export in
  `__init__.py` / `__all__`, and a row in the README function table.
- One issue per pull request. Reference it with `Closes #N`. Don't change unrelated code.
- Reviewers: check the acceptance criteria in the linked issue first, then correctness and
  edge cases (empty string, whitespace, unicode), then style. The formatter handles formatting.
