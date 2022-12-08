#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix.copy()
    for l in range(len(matrix)):
        new[l] = list(map(lambda x: x ** 2, new[l]))
    return new
