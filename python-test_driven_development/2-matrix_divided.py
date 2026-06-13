#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.

The function matrix_divided takes a matrix (list of lists of integers/floats)
and divides each element by a given number (div).
It returns a new matrix with results rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div and returns a new matrix.

    The matrix must be a list of lists of integers or floats.
    All rows must be of the same size.

    div must be a number (int or float) and cannot be zero.

    Args:
        matrix: list of lists of integers/floats
        div: integer or float used as divisor

    Returns:
        list: new matrix with divided values rounded to 2 decimal places

    Raises:
        TypeError: if matrix or div has invalid type
        ZeroDivisionError: if div is zero
    """

    if not isinstance(matrix, list) or matrix == [] or \
       not all(isinstance(row, list) for row in matrix) or \
       not all(isinstance(elem, (int, float))
               for row in matrix for elem in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [
        [round(elem / div, 2) for elem in row]
        for row in matrix
    ]

    return new_matrix