#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    ew_matrix = list(map(list, matrix))
    for i in range(0, len(ew_matrix)):
        for j in range(0, len(ew_matrix[i])):
            ew_matrix[i][j] = (matrix[i][j] * matrix[i][j])
    return ew_matrix
