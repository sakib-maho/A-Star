"""Backward-compatible entrypoint for the package CLI."""

from astar.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
