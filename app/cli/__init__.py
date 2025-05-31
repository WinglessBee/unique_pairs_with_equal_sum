"""CLI.

Initializes the root command group.
"""

import click


EPILOG = "Make sure uv venv is active or use `uv run python -m app.cli ...` instead."

cli_root = click.Group(epilog=EPILOG)
