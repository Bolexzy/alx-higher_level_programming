#!/usr/bin/python3

"""Defines a matrix multiplication function """


def matrix_mul(m_a, m_b):
    """
    Args:
        m_a -> First element(list of lists of ints/floats)
        m_b -> Second element(list of lists of ints/floats)

    Raises:
        ValueError: If m_a or m_b is empty.
                    If m_a and m_b cant be multiplied(A column != B rows)
        TypeError: If m_a or m_b is not a type `list`.
                   If m_a or m_b is not a list of lists of ints/floats.
                   If m_a and m_b doesnt have same sized rows.

    Returns:
        new_matrix containing result of multiplication.
    """
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # create an empty result matrix
    new_matrix = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    # Multiply the matrices
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                new_matrix[i][j] += m_a[i][k] * m_b[k][j]

    return new_matrix
