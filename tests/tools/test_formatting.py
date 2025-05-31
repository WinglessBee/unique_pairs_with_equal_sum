"""Tests for formatting tools."""

import collections
import typing

import pytest

from app.tools.formatting import comma_joined_values, space_joined_value_iterables


@pytest.mark.parametrize(
    "values, expected",
    [
        ((1, 2, 3), "1, 2, 3"),
        (["a", "b", "c", "d", "e"], "a, b, c, d, e"),
        ([0], "0"),
        ([], ""),
    ],
    ids=[
        "integer-tuple-input",
        "string-list-input",
        "one-value-list-input",
        "empty-list-input",
    ],
)
def test_comma_joined_values(
    values: collections.abc.Iterable[typing.Any],
    expected: str,
) -> None:
    assert comma_joined_values(values) == expected


@pytest.mark.parametrize(
    "iterables, expected",
    [
        ([(1, 2), (3, 4)], "( 1, 2) ( 3, 4)"),
        ([["42"]], "( 42)"),
        ((), ""),
    ],
    ids=[
        "integer-pairs-input",
        "one-value-list-input",
        "empty-tuple-input",
    ],
)
def test_space_joined_value_iterables(
    iterables: collections.abc.Iterable[collections.abc.Iterable[typing.Any]],
    expected: str,
) -> None:
    assert space_joined_value_iterables(iterables) == expected
