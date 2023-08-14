#!/usr/bin/python3
# 7-add_tuple.py

"""
Module - add_tuple
Contains a function that adds two tuples
"""

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Add two tuples.
    Args:
        tuple_a (tuple): The first tuple.
        tuple_b (tuple): The second tuple.
    Returns:
        A new tuple representing the sum of the two input tuples.
    """
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = (0, 0)
        else:
            tuple_a = (tuple_a[0], 0)
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = (0, 0)
        else:
            tuple_b = (tuple_b[0], 0)

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

