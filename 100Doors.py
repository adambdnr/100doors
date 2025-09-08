#!/usr/bin/env python3
"""Solve the classic 100 doors puzzle using modern Python."""

from __future__ import annotations

from math import isqrt


def open_doors(num_doors: int = 100) -> list[int]:
    """Return the door numbers that remain open after all passes.

    Doors are toggled on each pass. A door ends up open only if it is toggled
    an odd number of times, which happens when its number is a perfect square.
    """

    return [door for door in range(1, num_doors + 1) if isqrt(door) ** 2 == door]


def main() -> None:
    """Print the list of doors left open after the last pass."""

    print("The following doors are open:")
    print(open_doors())


if __name__ == "__main__":
    main()

