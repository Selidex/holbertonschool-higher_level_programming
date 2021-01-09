#!/usr/bin/python3
""" This module is a matrix divide function meant to help
develope simple test case files"""


def matrix_divided(matrix, div):
    """This function divides a matrix by div

    Args:
        matrix(object): the matrix being divided by
        div(int): what the matrix is being dived by
    """
    tl = "Each row of the matrix must have the same size"
    te = "matrix must be a matrix (list of lists) of integers/floats"
    mlen = 0

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list:
        raise TypeError(te)
    mlen = len(matrix[0])
    for x in matrix:
        if type(x) != list:
            raise TypeError(te)
        if len(x) != mlen:
            raise TypeError(tl)
        for y in matrix[x]:
            if type(y) != int:
                raise TypeError(te)

    new_matrix = list(map(list, matrix))
    for i in range(0, len(new_matrix)):
        for j in range(0, len(new_matrix[i])):
            new_matrix[i][j] = (matrix[i][j] * div)
    return new_matrix
