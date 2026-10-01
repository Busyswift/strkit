from strkit import slugify


def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"


def test_slugify_strips_accents():
    assert slugify("Crème brûlée") == "creme-brulee"


def test_slugify_custom_separator():
    assert slugify("Hello World", separator="_") == "hello_world"


def test_slugify_trims_edges():
    assert slugify("  Hello  ") == "hello"


def test_slugify_collapses_punctuation_runs():
    # Issue #3: runs of non-alphanumerics become ONE separator
    assert slugify("Hello, World!") == "hello-world"


def test_slugify_collapses_repeated_separators():
    assert slugify("a -- b") == "a-b"


def test_slugify_custom_separator_collapses_runs():
    assert slugify("Hello, World!", separator="_") == "hello_world"


def test_slugify_still_trims_edges_after_collapse():
    assert slugify("-- a -- b --") == "a-b"


def test_slugify_mixed_runs():
    assert slugify("a -!- b??c") == "a-b-c"
