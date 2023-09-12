#!/usr/bin/python3
'''
Module to work with JSON.
'''

import json


def to_json_string(my_obj):
    '''
    Convert a Python object into its JSON representation as a string.

    Args:
        my_obj: The Python object to be converted.

    Returns:
        str: The JSON representation of the object as a string.
    '''
    try:
        json_str = json.dumps(my_obj)
        return json_str
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
