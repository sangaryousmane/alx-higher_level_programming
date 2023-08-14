#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    """ Print a matrix of index integers """

    if matrix:
        for row in matrix:
            for col in row:
                if col == row[-1]:
                    print("{}".format(col), end="")
                else:
                    print("{}".format(col), end=" ")
            print()
