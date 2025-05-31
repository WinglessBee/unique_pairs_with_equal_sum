"""Tests for unique pairs with equal sum."""

import pytest

from app.core.unique_pairs_with_equal_sum import (
    find_all_unique_pairs_with_equal_sum,
    UniquePairsWithEqualSum,
)


@pytest.mark.parametrize(
    "array, expected",
    [
        (
            [1, 2, 3, 4, 5],
            {
                5: [(1, 4), (2, 3)],
                6: [(1, 5), (2, 4)],
                7: [(2, 5), (3, 4)],
            },
        ),
        (
            [6, 4, 12, 10, 22, 54, 32, 42, 21, 11],
            {
                16: [(4, 12), (6, 10)],
                32: [(10, 22), (21, 11)],
                33: [(12, 21), (22, 11)],
                43: [(22, 21), (32, 11)],
                53: [(32, 21), (42, 11)],
                54: [(12, 42), (22, 32)],
                64: [(10, 54), (22, 42)],
            },
        ),
        (
            [4, 23, 65, 67, 24, 12, 86],
            {90: [(4, 86), (23, 67)]},
        ),
        (
            [],
            {},
        ),
        (
            [42],
            {},
        ),
        (
            [3, 20, 19],
            {},
        ),
        (
            [40, 60, 40, 30, 70],
            {100: [(30, 70), (40, 60)]},
        ),
        (
            [40, 80, 60, 30, 70, 20],
            {
                100: [(30, 70), (40, 60), (80, 20)],
                110: [(40, 70), (80, 30)],
                90: [(60, 30), (70, 20)],
            },
        ),
        (
            [40, 20, 60, 30, -10],
            {50: [(20, 30), (60, -10)]},
        ),
        (
            [0, 20, 50, 30],
            {50: [(0, 50), (20, 30)]},
        ),
    ],
    ids=[
        "example-usage-values",
        "given-example-with-long-output",
        "given-example-with-short-output",
        "empty-input",
        "one-number-input",
        "no-pairs-with-equal-sum",
        "duplicate-input-number",
        "more-than-two-pairs",
        "negative-input-number",
        "zero-input-number",
    ],
)
def test_find_all_unique_pairs_with_equal_sum(
    array: list[int],
    expected: UniquePairsWithEqualSum,
) -> None:
    assert find_all_unique_pairs_with_equal_sum(array) == expected
