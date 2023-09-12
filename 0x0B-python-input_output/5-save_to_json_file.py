#!/usr/bin/python3
"""
Function that writes an object to a text file using JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Write a Python object to a text file using JSON representation.

    Args:
        my_obj: The Python object to be saved to the file.
        filename (str): The name of the file to which the object will be saved.

    Returns:
        None
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(my_obj, file)
    except Exception as e:
        print(f"An error occurred: {e}")
