#!/usr/bin/python3
# 3-print_reversed_list_integer.py

"""
Module - print_reversed_list_integer
Contains a function that prints all integers of a list in reverse order
"""

def print_reversed_list_integer(my_list=[]):
    """
    Print all integers of a list in reverse order.
    Args:
        my_list (list): The list of integers to print in reverse.
    """
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))

