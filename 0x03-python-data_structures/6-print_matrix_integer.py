#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    transposed = [[row[i] for row in matrix] for i in range(len(matrix))]
    
    for row in transposed:
        for item in row:
            print("{:d}".format(item), end=' ')
            print()
