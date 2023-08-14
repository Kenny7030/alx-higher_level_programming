#!/usr/bin/python3

"""
Module - print_matrix_integer
Contains a function that prints a matrix of integers
"""

def print_matrix_integer(matrix=[[]]):
    """
    Print a matrix of integers.
    Args:
        matrix (list): The matrix to be printed.
    """
    for row in matrix:
        for col_idx, col in enumerate(row):
            print("{:d}".format(col), end=" " if col_idx != len(row) - 1 else "")
        print()

