#!/usr/bin/python3
# 10-divisible_by_2.py

"""
Module - divisible_by_2
Contains a function that finds all multiples of 2 in a list
"""

def divisible_by_2(my_list=[]):
    """
    Find all multiples of 2 in a list.
    Args:
        my_list (list): The list of integers.
    Returns:
        A list of boolean values indicating if each element is divisible by 2.
    """
    multiples = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return multiples

