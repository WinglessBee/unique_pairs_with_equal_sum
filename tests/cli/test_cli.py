"""Tests for CLI."""

import click.testing

from app.cli import cli_root
import app.cli.__main__  # ensures commands are loaded  # noqa: F401


def test_cli_entrypoint() -> None:
    runner = click.testing.CliRunner()
    result = runner.invoke(cli_root, [])
    assert result.exit_code == 2  # incorrect usage
    assert "Usage" in result.output
    assert "Commands" in result.output
