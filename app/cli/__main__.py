"""CLI Entrypoint.

Registers all commands and invokes CLI.
"""

import importlib
import pkgutil

from app.cli import cli_root
import app.cli.commands


for module_info in pkgutil.iter_modules(app.cli.commands.__path__):
    importlib.import_module(f"{app.cli.commands.__name__}.{module_info.name}")


if __name__ == "__main__":
    cli_root()
