#!/usr/bin/python3
'''
Module to Write to file
'''


def write_file(filename="", text=""):
    '''
    Write the given text to a file.

    Args:
        filename (str): The name of the file to which text will be written.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.
    '''
    try:
        with open(filename, 'w') as open_file:
            open_file.write(text)
            count = open_file.tell()
        return count
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1
