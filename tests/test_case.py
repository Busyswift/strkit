import pytest

from strkit import to_camel_case, to_kebab_case, to_snake_case, to_title_case


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello World", "hello_world"),
        ("helloWorld", "hello_world"),
        ("hello-world", "hello_world"),
        ("  padded  text  ", "padded_text"),
        ("", ""),
    ],
)
def test_to_snake_case(text, expected):
    assert to_snake_case(text) == expected


def test_to_kebab_case():
    assert to_kebab_case("Hello big_World") == "hello-big-world"


@pytest.mark.parametrize(
    ("text", "expected"),
    [("hello world", "helloWorld"), ("Hello-Big-World", "helloBigWorld"), ("", "")],
)
def test_to_camel_case(text, expected):
    assert to_camel_case(text) == expected


def test_to_title_case():
    assert to_title_case("hello   big_world") == "Hello Big World"
