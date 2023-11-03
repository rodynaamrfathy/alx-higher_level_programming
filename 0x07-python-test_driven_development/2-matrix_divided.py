#!/usr/bin/python3
"""Module for matrix_divided method."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number.

    Args:
        matrix (list): A list of lists representing the matrix.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix with the elements divided by div.

    Raises:
        TypeError: If matrix is not a matrix of integers or floats,
            or if div is not a number.
        TypeError: if sublists are not all same size
        ZeroDivisionError: If div is equal to 0.

    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
