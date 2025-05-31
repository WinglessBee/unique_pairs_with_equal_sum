"""Unique pairs with equal sum."""

UniquePairsWithEqualSum = dict[int, list[tuple[int, int]]]


def find_all_unique_pairs_with_equal_sum(array: list[int]) -> UniquePairsWithEqualSum:
    """Find all unique pairs with equal sum in an unsorted array."""
    previous_numbers: list[int] = []
    unique_pairs_with_equal_sum: UniquePairsWithEqualSum = {}
    unique_pairs_with_equal_sum_without_orphans: UniquePairsWithEqualSum = {}

    for current_number in array:
        if current_number in previous_numbers:
            continue

        for previous_number in previous_numbers:
            new_pair: tuple[int, int] = (previous_number, current_number)
            new_sum: int = previous_number + current_number

            if new_sum in unique_pairs_with_equal_sum:
                unique_pairs_with_equal_sum[new_sum].append(new_pair)
                unique_pairs_with_equal_sum_without_orphans[new_sum] = sorted(
                    unique_pairs_with_equal_sum[new_sum]
                )
            else:
                unique_pairs_with_equal_sum[new_sum] = [new_pair]

        previous_numbers.append(current_number)

    return unique_pairs_with_equal_sum_without_orphans
