#!/usr/bin/python3
# 11-delete_at.py

"""
Module - delete_at
Contains a function that deletes an item at a specific position in a list
"""

def delete_at(my_list=[], idx=0):
    """
    Delete an item at a specific position in a list.
    Args:
        my_list (list): The list from which to delete an item.
        idx (int): The index of the item to delete.
    Returns:
        The modified list after the deletion, or the original list if the index is out of range.
    """
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list

