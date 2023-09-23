#!/usr/bin/python3

def matrix_divided(matrix, div):
    """ performs matrix multiplication with division"""
    if (not isinstance(matrix, list) or matrix == [] or
            not all(type(row) == list for row in matrix) or
            not all((type(ele) == int or type(ele) == float)
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(r) == len(matrix[0]) for r in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda num: round(num / div, 2), r)) for r in matrix]
