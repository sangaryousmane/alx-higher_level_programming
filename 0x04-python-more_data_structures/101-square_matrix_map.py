#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map((lambda value: list(map((lambda y: y * y), value))), matrix))
