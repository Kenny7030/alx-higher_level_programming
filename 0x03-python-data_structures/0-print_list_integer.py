#!/usr/bin/python3

"""
Module - print_list_integer
Contains a function that prints integers from a list
"""

def print_list_integer(my_list=[]):
    """
    Prints integers from a list
    Args:
        my_list (list): The list containing integers
    """
    for i in my_list:
        print('{:d}'.format(i))

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_list_integer(my_list)

