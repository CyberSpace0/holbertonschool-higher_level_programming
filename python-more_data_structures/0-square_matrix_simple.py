#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    r = 0
    for i in matrix:
        new.append([])
        for x in i:
            new[r].append(x*x)
        r = r + 1
    return new
