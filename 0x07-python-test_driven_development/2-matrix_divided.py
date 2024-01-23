#!/usr/bin/python3
"""
Module for methods:
    - matrix_divided
"""


def matrix_divided(matrix, div):
    """Divides the elements in a matrix by the value of `div`.

    Args:
        matrix (2d array): the 2d array.
        div (int): the number to divide by.

    Return:
        The new matrix with it's values divided by 3
    """

    mat_size = 0
    out_mat = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    for idx in range(len(matrix)):
        submat = matrix[idx]

        if not isinstance(submat, list):
            raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
        elif mat_size == 0:
            mat_size = len(submat)
        elif not len(submat) == mat_size:
            raise TypeError("Each row of the matrix must have the same size")

        out_mat.append([])

        for item in submat:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
            out_mat[idx].append(round(item / div, 2))

    return out_mat


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
