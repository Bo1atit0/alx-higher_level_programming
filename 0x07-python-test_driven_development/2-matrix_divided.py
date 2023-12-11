#!/usr/bin/python3

"""
matrix_divided.py: divides elements in a matrix
by a divisor
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix by div

    Parameters:
    - matrix: List of lists representing the matrix.
    - div: Divisor

    Returns:
    A new matrix containing divided matrix.
    """
    errmesg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix:
        raise TypeError(errmesg)
    elif type(matrix) is not list:
        raise TypeError(errmesg)
    elif len(matrix) == 0:
        raise TypeError(errmesg)
    elif len(matrix[0]) == 0:
        raise TypeError(errmesg)

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    elif type(div) is bool:
        raise TypeError("div must be a number")
    elif type(div) is str:
        raise TypeError("div must be a number")

    row_size = len(matrix[0])
    new_matrix = []
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        row_list = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(errmesg)
            row_list.append(round(element / div, 2))
        new_matrix.append(row_list)

    return new_matrix
