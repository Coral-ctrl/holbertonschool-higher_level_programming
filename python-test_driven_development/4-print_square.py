#!/usr/bin/python3
"""Module for print_square function."""


def print_square(size):
    """Print a square with the character #.

    Args:
        size: The size length of the square (must be an integer)

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """

    if isinstance(size, float):
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
