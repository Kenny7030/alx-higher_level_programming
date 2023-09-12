#!/usr/bin/python3
'''
Module for JSON serialization
'''


def class_to_json(obj):
    '''
    Serialize a Python object by converting its attributes to a dictionary.

    Args:
        obj: The Python object to be serialized.

    Returns:
        dict: A dictionary representing the object's attributes.
    '''
    try:
        if hasattr(obj, '__dict__'):
            return obj.__dict__
        else:
            raise AttributeError("Object has no '__dict__' attribute.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
