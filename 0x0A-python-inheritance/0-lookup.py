#!/usr/bin/python3
"""Module containing the ``lookup`` function definition.
"""


def lookup(obj):
    """Return a list of available attributes and methods of an object.
    
    Args:
        obj (object): The object to inspect.

    Returns:
        list: A list of strings containing attribute and method names.
    """
    return dir(obj)

