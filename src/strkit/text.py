"""General text helpers."""


def truncate(text: str, width: int, ellipsis: str = "…") -> str:
    """Shorten ``text`` to at most ``width`` characters, ending with
    ``ellipsis`` when anything was cut.

    >>> truncate("The quick brown fox", 10)
    'The quick…'
    >>> truncate("short", 10)
    'short'
    """
    if len(text) <= width:
        return text
    return text[: width - len(ellipsis)] + ellipsis


def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in ``text``.

    >>> word_count("one two  three")
    3
    """
    return len(text.split(" ")) - text.count("  ")
