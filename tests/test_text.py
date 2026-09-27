from strkit import truncate, word_count


def test_truncate_keeps_short_text():
    assert truncate("short", 10) == "short"


def test_truncate_adds_ellipsis():
    assert truncate("The quick brown fox", 10) == "The quick…"
    assert len(truncate("The quick brown fox", 10)) == 10


def test_truncate_custom_ellipsis():
    assert truncate("The quick brown fox", 10, ellipsis="...") == "The qui..."


def test_word_count():
    assert word_count("one two three") == 3
