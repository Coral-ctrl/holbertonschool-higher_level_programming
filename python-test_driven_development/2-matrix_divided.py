#!/usr/bin/python3
"""
Module that defines a matrix_divided function.

The function divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix: List of lists of integers or floats
        div: Number to divide by (int or float)
    
    Returns:
        New matrix with all elements divided by div, rounded to 2 decimals
    
    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
        TypeError: If rows have different sizes
        TypeError: If div is not a number
        ZeroDivisionError: If div is 0
    """

    # Check if matrix is a list
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if matrix is a list of lists with valid elements
    row_length = None
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        # Check if all elements are integers or floats
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        # Check if all rows have the same size
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create new matrix with divided values
    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2] for element in row]
        new_matrix.append(new_row)

    return new_matrix
