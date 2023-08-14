#!/usr/bin/python3
# 9-max_integer.py

"""
Module - max_integer
Contains a function that finds the biggest integer in a list
"""

def max_integer(my_list=[]):
    """
    Find the biggest integer in a list.
    Args:
        my_list (list): The list of integers.
    Returns:
        The maximum integer in the list, or None if the list is empty.
    """
    if len(my_list) == 0:
        return None

    big = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > big:
            big = my_list[i]

    return big

