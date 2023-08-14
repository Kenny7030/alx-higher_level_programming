#!/usr/bin/python3
# 5-no_c.py

"""
Module - no_c
Contains a function that removes all occurrences of 'c' and 'C' from a string
"""

def no_c(my_string):
    """
    Remove all occurrences of 'c' and 'C' from a string.
    Args:
        my_string (str): The input string from which to remove characters.
    Returns:
        A new string with 'c' and 'C' removed.
    """
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return "".join(copy)

