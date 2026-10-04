"""Command-line interface: ``strkit <command> TEXT``."""

import argparse
import sys
from collections.abc import Callable, Sequence

from strkit import __version__, case, slug, text

COMMANDS: dict[str, Callable[[str], str]] = {
    "slug": slug.slugify,
    "snake": case.to_snake_case,
    "kebab": case.to_kebab_case,
    "camel": case.to_camel_case,
    "title": case.to_title_case,
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="strkit", description="Small, dependency-free string utilities."
    )
    # Shared by the top-level parser and every subcommand so `--version` works in both places.
    # The text is fixed (not %(prog)s) so subcommands also print "strkit <version>".
    version = argparse.ArgumentParser(add_help=False)
    version.add_argument("--version", action="version", version=f"strkit {__version__}")
    parser.add_argument(
        "--version", action="version", version=f"strkit {__version__}", help="show the version"
    )
    sub = parser.add_subparsers(dest="command", required=True)
    for name, func in COMMANDS.items():
        summary = (func.__doc__ or "").strip().splitlines()[0]
        command = sub.add_parser(name, help=summary, description=summary, parents=[version])
        command.add_argument("text", help="the text to convert")
    truncate = sub.add_parser(
        "truncate", help="Shorten text to a maximum width.", parents=[version]
    )
    truncate.add_argument("text", help="the text to shorten")
    truncate.add_argument("--width", type=int, default=80, help="maximum length (default: 80)")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "truncate":
        result = text.truncate(args.text, args.width)
    else:
        result = COMMANDS[args.command](args.text)
    sys.stdout.write(result + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
