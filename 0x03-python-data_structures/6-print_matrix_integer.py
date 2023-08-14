#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    """ Print a matrix of index integers """

    if matrix:
        for row in matrix:
            for col in row:
                if col == row[-1]:
                    print("{:d}".format(col), end="")
                else:
                    print("{:d}".format(col), end=" ")
            print()
