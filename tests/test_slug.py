from strkit import slugify


def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"


def test_slugify_strips_accents():
    assert slugify("Crème brûlée") == "creme-brulee"


def test_slugify_custom_separator():
    assert slugify("Hello World", separator="_") == "hello_world"


def test_slugify_trims_edges():
    assert slugify("  Hello  ") == "hello"
