#!/usr/bin/python3
"""
    Defines a matrix divide function
"""


def matrix_divided(matrix, div):
    """ Divides all element in a matrix by div
    Args:
        matrix: A list of lists of int/floats
        div: integer/float divisor

    Returns:
        A new matrix with the result of each division.

    Raises:
        TypeErrror: If the elements of matrix is not list.
                    If the elements of the matrix lists isn't int/floats.
                    If div is not an integer or float.
                    If each row of matrix is not of same size.

        ZeroDivisionError: If div is zero(0)

    """

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(item, int) or isinstance(item, float))
                    for item in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
