#!/usr/bin/python3

"""Defines a function that returns the list of
    available attributes and methods of an object.
"""


def lookup(obj):
    """Returns list of available attributes and methods of an object.
    Args:
        obj: The instance of the class.

    Returns:
         List of attributes and methods of the instance.
    """

    return (dir(obj))
