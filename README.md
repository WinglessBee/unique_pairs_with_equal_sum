# Unique Pairs with Equal Sum

This project is built around one core feature — unique pairs with equal sum.

The codebase is structured for scalability and maintainability. It includes:
* A modular CLI interface with dynamic command registration.
* Core logic separated cleanly from the interface.
* Shared formatting tools.
* A test suite with code coverage tracking.
* A consistent and extendable project layout.


## Requirements

* [Python](https://www.python.org/downloads) 3.13+
* [uv](https://docs.astral.sh/uv/getting-started/installation) — fast package and project manager


## Installation

```bash
uv sync
```


## Usage

```bash
uv run python -m app.cli --help
uv run python -m app.cli eq-sum-prs 1 2 3 4 5
```

If you activate uv venv as follows, you can omit `uv run`:

```bash
source .venv/bin/activate  # or .venv/Scripts/activate on Windows
```


## Project Structure

```text
app/
├── cli/        # CLI entrypoint and commands
├── core/       # Core logic and algorithms
├── tools/      # Non-feature utilities
tests/
```


## Development

Install development dependencies:

```bash
uv sync --extra dev
```


### Testing with Coverage

```bash
uv run pytest -v --cov=app tests
```


### Code Quality Tools

```bash
uv run ruff format .
uv run ruff check .
uv run mypy .
```
