#!/usr/bin/python3
# 1-element_at.py

"""
Module - element_at
Contains a function that retrieves an element from a list
"""

def element_at(my_list, idx):
    """
    Retrieve an element from a list.
    Args:
        my_list (list): The list to retrieve elements from.
        idx (int): The index of the element to retrieve.
    Returns:
        The element at the specified index, or None if index is out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]

