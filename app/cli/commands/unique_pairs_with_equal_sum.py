"""CLI for unique pairs with equal sum."""

import click

from app.cli import cli_root, EPILOG
from app.core.unique_pairs_with_equal_sum import find_all_unique_pairs_with_equal_sum
from app.tools.formatting import comma_joined_values, space_joined_value_iterables


@cli_root.command(name="eq-sum-prs", epilog=EPILOG)
@click.argument("array", type=int, nargs=-1, required=True)
def unique_pairs_with_equal_sum(array: tuple[int]) -> None:
    """Find and print all unique pairs of integers from the input ARRAY that have the same sum.

    ARRAY: List of integers.

    Example: eq-sum-prs 1 2 3 4 5
    """
    click.echo(f"Input: A[] = {{ {comma_joined_values(array)}}}")

    all_unique_pairs_with_equal_sum = find_all_unique_pairs_with_equal_sum(list(array))

    click.echo("Output:")
    if all_unique_pairs_with_equal_sum:
        for equal_sum, unique_pairs in sorted(all_unique_pairs_with_equal_sum.items()):
            click.echo(
                f"Pairs : {space_joined_value_iterables(unique_pairs)} have sum : {equal_sum}"
            )
    else:
        click.echo("No unique pairs with equal sum found.")
