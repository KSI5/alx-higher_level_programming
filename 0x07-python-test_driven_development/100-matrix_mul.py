#!/usr/bin/python3
# 100-matrix_mul.py
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        ValueError: If m_a or m_b is an empty list.
        TypeError: If m_a and m_b have different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("Both m_a and m_b must be lists")

    if len(m_a) == 0 or len(m_a[0]) == 0 or len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("Both m_a and m_b cannot be empty")

    if any(not isinstance(row, list) for row in m_a) or any(not isinstance(row, list) for row in m_b):
        raise TypeError("Both m_a and m_b must be lists of lists")

    if any(not all(isinstance(ele, int) or isinstance(ele, float) for ele in row) for row in m_a) or \
            any(not all(isinstance(ele, int) or isinstance(ele, float) for ele in row) for row in m_b):
        raise TypeError("Both m_a and m_b should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a) or any(len(row) != len(m_b[0]) for row in m_b):
        raise ValueError("Rows of m_a and m_b must have the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b cannot be multiplied")

    # Transpose matrix m_b to simplify multiplication
    transposed_b = [[m_b[j][i] for j in range(len(m_b))] for i in range(len(m_b[0]))]

    new_matrix = []
    for row_a in m_a:
        new_row = []
        for row_b in transposed_b:
            prod = sum(a * b for a, b in zip(row_a, row_b))
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
