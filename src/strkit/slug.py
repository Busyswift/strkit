"""URL slugs."""

import re
import unicodedata


def slugify(text: str, separator: str = "-") -> str:
    """Return a lowercase, ASCII-only, URL-safe slug for ``text``.

    >>> slugify("Hello World")
    'hello-world'
    >>> slugify("Crème brûlée")
    'creme-brulee'
    """
    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", separator, ascii_text.lower())
    return slug.strip(separator)
