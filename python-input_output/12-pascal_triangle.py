#!/usr/bin/python3
"""Module containing pascal_triangle function."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle."""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]

        previous = triangle[i - 1]

        for j in range(1, i):
            row.append(previous[j - 1] + previous[j])

        row.append(1)
        triangle.append(row)

    return triangle
