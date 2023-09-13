#!/usr/bin/python3
"""Module contains the function ``inherits_from`` definition.
"""

def inherits_from(obj, a_class):
    """Determines if ``obj`` is an instance of a class which is a
    subclass of ``a_class``.
    
    Args:
        obj (object): Object to be evaluated.
        a_class (class): Class to be evaluated against.
        
    Returns:
        bool: True if ``obj`` is an instance of a subclass of ``a_class``, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class

