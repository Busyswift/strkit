"""strkit: small, dependency-free string utilities."""

from strkit.case import to_camel_case, to_kebab_case, to_snake_case, to_title_case
from strkit.slug import slugify
from strkit.text import truncate, word_count

__all__ = [
    "slugify",
    "to_camel_case",
    "to_kebab_case",
    "to_snake_case",
    "to_title_case",
    "truncate",
    "word_count",
]

__version__ = "0.1.0"
