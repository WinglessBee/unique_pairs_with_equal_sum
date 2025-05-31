"""Formatting tools."""

import collections.abc
import typing


def comma_joined_values(values: collections.abc.Iterable[typing.Any]) -> str:
    """Return values joined by commas as a string."""
    return ", ".join(str(v) for v in values)


def space_joined_value_iterables(
    iterables: collections.abc.Iterable[collections.abc.Iterable[typing.Any]],
) -> str:
    """Return iterables as space-separated strings of comma-joined values."""
    return " ".join(f"( {comma_joined_values(i)})" for i in iterables)
