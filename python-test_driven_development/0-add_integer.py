#!/usr/bin/python3
"""
Module that defines an integer addition function.

The function adds two numbers after validating their types.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Floats are cast to integers before addition
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Reject NaN and infinity
    if isinstance(a, float) and (math.isinf(a) or math.isnan(a)):
        raise OverflowError("cannot convert float infinity to integer")
    if isinstance(b, float) and (math.isinf(b) or math.isnan(b)):
        raise OverflowError("cannot convert float infinity to integer")
    
    return int(a) + int(b)
