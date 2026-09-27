# Contributing to strkit

Thanks for helping. Every issue here is meant to be finishable in under an hour.

## Workflow

1. Comment on the issue so nobody else picks it up. For issues labeled `prswarm`,
   claim the job on [PRSwarm](https://prswarm.com) instead.
2. Fork the repository and create a branch: `git switch -c 12-reverse-words`.
3. Make the change, with tests.
4. Run the checks locally (below).
5. Open a pull request that says `Closes #<issue number>` and fills in the template.

One issue per pull request, please. Keep changes to what the issue asks for.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Checks

CI runs exactly these two commands as the `lint` and `test` checks. Both must pass.

```bash
ruff check . && ruff format --check .   # lint
pytest                                   # test (also runs the doctests in src/)
```

## Conventions

- No runtime dependencies. The standard library only.
- Every public function has type hints, a docstring with at least one doctest
  example, is exported from `strkit/__init__.py` and listed in `__all__`, and
  appears in the README's function table.
- Tests live in `tests/test_<module>.py`. Cover the normal case and the edge
  cases the issue names (empty string, whitespace, unicode).
- New CLI commands get a test in `tests/test_cli.py`.

## Reviews

PR-Agent posts an automated review, a PR description and code suggestions on
every pull request. Treat its comments as suggestions: fix what's right,
reply to what isn't. A maintainer does the final review and merge.
