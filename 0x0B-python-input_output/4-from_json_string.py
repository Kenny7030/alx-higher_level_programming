#!/usr/bin/python3
'''
Module that works with JSON
'''

import json


def from_json_string(my_str):
    '''
    Convert a JSON string into a Python object.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The Python object created from the JSON string.
    '''
    try:
        obj = json.loads(my_str)
        return obj
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
