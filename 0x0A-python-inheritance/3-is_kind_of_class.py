#!/usr/bin/python3
"""Module containing the ``is_kind_of_class`` function definition.
"""

def is_kind_of_class(obj, a_class):
    """Determines if ``obj`` is an instance of ``a_class`` or any of
    its subclasses.
    
    Args:
        obj (object): Object to be evaluated.
        a_class (type): Class to check ``obj`` against.
        
    Returns:
        bool: True if ``obj`` is an instance of ``a_class`` or its subclass, False otherwise.
    """
    return isinstance(obj, a_class)
