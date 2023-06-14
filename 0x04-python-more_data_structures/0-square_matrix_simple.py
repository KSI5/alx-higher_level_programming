#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Compute the square value of all integers in a matrix.

    Args:
        matrix (list): 2-dimensional list representing the matrix.

    Returns:
        list: A new matrix with the same size as the input matrix.
        """
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(num ** 2)
        new_matrix.append(new_row)
    return new_matrix
