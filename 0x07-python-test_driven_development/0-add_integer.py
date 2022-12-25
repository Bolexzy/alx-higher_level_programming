#!/usr/bin/python3

"""
    Defines an integer addition function.
"""


def add_integer(a, b=98):
    """Adds two integers a and b

    Args:
        integers a and b

    Returns:
        Addition of a and b

    Raises:
        TypeError: If a or b is a non-integer and non-float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
