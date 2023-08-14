#!/usr/bin/python3
# 2-replace_in_list.py

"""
Module - replace_in_list
Contains a function that replaces an element in a list at a specific position
"""

def replace_in_list(my_list, idx, element):
    """
    Replace an element in a list at a specific position.
    Args:
        my_list (list): The list in which to replace an element.
        idx (int): The index at which to replace the element.
        element: The element to replace with.
    Returns:
        The modified list after the replacement, or the original list if the index is out of range.
    """
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list

