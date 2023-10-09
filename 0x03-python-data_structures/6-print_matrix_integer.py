#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for row in matrix:
        for item in matrix:
            print("{:d}".format(item), end=' ')
        print()
