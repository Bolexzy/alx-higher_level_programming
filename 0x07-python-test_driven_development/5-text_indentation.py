#!/usr/bin/python3

"""
    Defines a function that prints a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """Print text with two new lines after ".?:" characters.
    Args:
        text: input string.

    Raises:
        TypeError: if text is not a string.

    Returns:
        No return.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    length = len(text)
    s = 0
    while s < len(text) and text[s] == ' ':
        s += 1

    while s < length:
        print(text[s], end="")
        if text[s] == "\n" or text[s] in ".?:":
            if text[s] in ".?:":
                print("\n")
            s += 1
            while s < length and text[s] == ' ':
                s += 1
            continue
        s += 1
