#!/usr/bin/python3
# 4-new_in_list.py

"""
Module - new_in_list
Contains a function that replaces an element in a copied list at a specific position
"""

def new_in_list(my_list, idx, element):
    """
    Replace an element in a copied list at a specific position.
    Args:
        my_list (list): The list from which to create a copy and replace an element.
        idx (int): The index at which to replace the element.
        element: The element to replace with.
    Returns:
        A new list with the replacement, or the original list if the index is out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    
    copy = my_list.copy()
    copy[idx] = element
    return copy

