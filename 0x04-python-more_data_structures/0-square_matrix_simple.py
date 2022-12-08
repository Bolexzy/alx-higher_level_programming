#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    if len(matrix) == 0:
        return new
    new = [list(map(lambda x: x * x,  row)) for row in matrix]
    return new
