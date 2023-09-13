#!/usr/bin/python3
"""
This script defines a function called lookup that returns a list of available
attributes and methods of an object.
"""

def lookup(obj):
    """
    Returns a list of available attributes and methods of the provided object.

    :param obj: The object to inspect.
    :return: A list of strings containing attribute and method names.
    """
    return dir(obj)

