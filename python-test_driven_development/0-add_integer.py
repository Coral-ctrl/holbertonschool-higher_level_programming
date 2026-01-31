#!/usr/bin/python3
"""
Module that defines an integer addition function.

The function adds two numbers after validating their types.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Floats are cast to integers before addition

    Returns:
        The addition of a and b as an integer

    Raises:
        TypeError: If a or b is not an integer or float
        OverflowError: If a or b is infinity
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Check for NaN (must check before infinity)
    if isinstance(a, float) and a != a:
        raise ValueError("cannot convert float NaN to integer")
    if isinstance(b, float) and b != b:
        raise ValueError("cannot convert float NaN to integer")

    # Check for infinity
    if isinstance(a, float):
        if a == float('inf') or a == float('-inf'):
            raise OverflowError("cannot convert float infinity to integer")
    if isinstance(b, float):
        if b == float('inf') or b == float('-inf'):
            raise OverflowError("cannot convert float infinity to integer")

    return int(a) + int(b)
