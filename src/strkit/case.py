"""Convert identifiers and phrases between naming conventions."""

import re

_BOUNDARY = re.compile(r"(?<=[a-z0-9])(?=[A-Z])|[\s_\-]+")


def _words(text: str) -> list[str]:
    """Split ``text`` into lowercase words on spaces, underscores, hyphens
    and lowercase-to-uppercase boundaries."""
    return [word.lower() for word in _BOUNDARY.split(text.strip()) if word]


def to_snake_case(text: str) -> str:
    """Return ``text`` as ``snake_case``.

    >>> to_snake_case("Hello World")
    'hello_world'
    >>> to_snake_case("parseHTTPResponse")
    'parse_httpresponse'
    """
    return "_".join(_words(text))


def to_kebab_case(text: str) -> str:
    """Return ``text`` as ``kebab-case``.

    >>> to_kebab_case("Hello World")
    'hello-world'
    """
    return "-".join(_words(text))


def to_camel_case(text: str) -> str:
    """Return ``text`` as ``camelCase``.

    >>> to_camel_case("hello world")
    'helloWorld'
    """
    words = _words(text)
    if not words:
        return ""
    return words[0] + "".join(word.capitalize() for word in words[1:])


def to_title_case(text: str) -> str:
    """Return ``text`` with each word capitalized and single-spaced.

    >>> to_title_case("hello   big_world")
    'Hello Big World'
    """
    return " ".join(word.capitalize() for word in _words(text))
