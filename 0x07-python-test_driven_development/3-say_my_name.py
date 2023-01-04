#!/usr/bin/python3

"""
    Defines a name printing function
"""


def say_my_name(first_name, last_name=""):
    """ Prints name in the format `My name is <first name> <last name>`
    Args:
        firstname: firstname string input
        last_name: last name string input

    Returns:
        The string "y name is <first name> <last name>"
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    name = "My name is {} {}".format(first_name, last_name)
    print(name)
