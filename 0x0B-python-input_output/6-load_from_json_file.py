#!/usr/bin/python3
'''
Module that works with JSON files
'''

import json


def load_from_json_file(filename):
    '''
    Read a JSON file and create a Python object from its content.

    Args:
        filename (str): The name of the JSON file to be read.

    Returns:
        object: The Python object created from the JSON file.
    '''
    try:
        with open(filename, 'r') as file:
            obj = json.load(file)
        return obj
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
