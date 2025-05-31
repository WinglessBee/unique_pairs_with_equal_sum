"""Tests for command eq-sum-prs (unique pairs with equal sum)."""

import click.testing
import pytest

from app.cli import cli_root
import app.cli.__main__  # ensures commands are loaded  # noqa: F401


@pytest.mark.parametrize(
    "args, expected",
    [
        (
            ["eq-sum-prs", "1", "2", "3", "4", "5"],
            (
                "Input: A[] = { 1, 2, 3, 4, 5}\n"
                "Output:\n"
                "Pairs : ( 1, 4) ( 2, 3) have sum : 5\n"
                "Pairs : ( 1, 5) ( 2, 4) have sum : 6\n"
                "Pairs : ( 2, 5) ( 3, 4) have sum : 7\n"
            ),
        ),
        (
            ["eq-sum-prs", "6", "4", "12", "10", "22", "54", "32", "42", "21", "11"],
            (
                "Input: A[] = { 6, 4, 12, 10, 22, 54, 32, 42, 21, 11}\n"
                "Output:\n"
                "Pairs : ( 4, 12) ( 6, 10) have sum : 16\n"
                "Pairs : ( 10, 22) ( 21, 11) have sum : 32\n"
                "Pairs : ( 12, 21) ( 22, 11) have sum : 33\n"
                "Pairs : ( 22, 21) ( 32, 11) have sum : 43\n"
                "Pairs : ( 32, 21) ( 42, 11) have sum : 53\n"
                "Pairs : ( 12, 42) ( 22, 32) have sum : 54\n"
                "Pairs : ( 10, 54) ( 22, 42) have sum : 64\n"
            ),
        ),
        (
            ["eq-sum-prs", "4", "23", "65", "67", "24", "12", "86"],
            (
                "Input: A[] = { 4, 23, 65, 67, 24, 12, 86}\n"
                "Output:\n"
                "Pairs : ( 4, 86) ( 23, 67) have sum : 90\n"
            ),
        ),
        (
            ["eq-sum-prs", "3", "20", "19"],
            "Input: A[] = { 3, 20, 19}\nOutput:\nNo unique pairs with equal sum found.\n",
        ),
    ],
    ids=[
        "example-usage-values",
        "given-example-with-long-output",
        "given-example-with-short-output",
        "no-pairs-with-equal-sum",
    ],
)
def test_unique_pairs_with_equal_sum(args: list[str], expected: str) -> None:
    runner = click.testing.CliRunner()
    result = runner.invoke(cli_root, args)

    assert result.exit_code == 0
    assert result.output == expected
