#!/usr/bin/python3

"""
    Defines a sqaure print function using #
"""


def print_square(size):
    """Prints a square using the character '#'
    Args:
        size: size(int) of the square (height/width).
    Raises:
        TypeError: If size is not an integer or
                    if size is a float and is less than 0.
        ValueError: If size is < 0

    Returns:
        Prints the square, no return.
    """

    if not isinstance(size, int) or (isinstance(size, float) and (size < 0)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print()
