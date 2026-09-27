# strkit

[![CI](https://github.com/sheepdogs/strkit/actions/workflows/ci.yml/badge.svg)](https://github.com/sheepdogs/strkit/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](pyproject.toml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Small, dependency-free string utilities for Python, with a command-line interface.

```python
>>> from strkit import slugify, to_snake_case, truncate
>>> slugify("Crème brûlée")
'creme-brulee'
>>> to_snake_case("Hello World")
'hello_world'
>>> truncate("The quick brown fox", 10)
'The quick…'
```

## Install

```bash
pip install git+https://github.com/sheepdogs/strkit
```

## Functions

| Function | What it does |
|---|---|
| `slugify(text, separator="-")` | Lowercase, ASCII-only, URL-safe slug |
| `to_snake_case(text)` | `hello_world` |
| `to_kebab_case(text)` | `hello-world` |
| `to_camel_case(text)` | `helloWorld` |
| `to_title_case(text)` | `Hello World` |
| `truncate(text, width, ellipsis="…")` | Shorten to at most `width` characters |
| `word_count(text)` | Number of words |

## Command line

```bash
$ strkit slug "Hello World"
hello-world
$ strkit camel "hello big world"
helloBigWorld
$ strkit truncate "The quick brown fox" --width 10
The quick…
```

Run `strkit --help` for every command.

## Contributing

Small, well-scoped issues are the point of this project. Pick anything labeled
[`good first issue`](https://github.com/sheepdogs/strkit/labels/good%20first%20issue),
then read [CONTRIBUTING.md](CONTRIBUTING.md). Every pull request runs the `lint`
and `test` checks and gets an automated review from
[PR-Agent](https://github.com/qodo-ai/pr-agent).

### Paid tasks on PRSwarm

strkit is the public proving ground for [PRSwarm](https://prswarm.com), a
marketplace where funded, well-specified software tasks are completed by
autonomous agents. Issues labeled `prswarm` may be posted there as funded jobs,
with the `lint` and `test` checks as their acceptance criteria. Claim those jobs
through PRSwarm; don't open a PR for them directly.

## License

[MIT](LICENSE)
