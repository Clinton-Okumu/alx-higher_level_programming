#!/usr/bin/python3
def square_matrix_simple(matrix):
    result_matrix = []
    for row in matrix:
        row_result = []
        for element in row:
            squared_value = element ** 2
            row_result.append(squared_value)
        result_matrix.append(row_result)
    return result_matrix
