import pytest

from strkit import __version__
from strkit.cli import main


@pytest.mark.parametrize(
    ("argv", "expected"),
    [
        (["slug", "Hello World"], "hello-world"),
        (["snake", "Hello World"], "hello_world"),
        (["kebab", "Hello World"], "hello-world"),
        (["camel", "hello world"], "helloWorld"),
        (["title", "hello world"], "Hello World"),
        (["truncate", "The quick brown fox", "--width", "10"], "The quick…"),
    ],
)
def test_commands(capsys, argv, expected):
    assert main(argv) == 0
    assert capsys.readouterr().out == expected + "\n"


def test_version_prints_package_version_and_exits_zero(capsys):
    with pytest.raises(SystemExit) as exit_info:
        main(["--version"])
    assert exit_info.value.code == 0
    assert capsys.readouterr().out == f"strkit {__version__}\n"


def test_unknown_command_exits_with_usage(capsys):
    with pytest.raises(SystemExit) as exit_info:
        main(["shout", "hi"])
    assert exit_info.value.code == 2
    assert "usage: strkit" in capsys.readouterr().err
