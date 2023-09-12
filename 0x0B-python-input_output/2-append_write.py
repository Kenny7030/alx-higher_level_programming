#!/usr/bin/python3
""" Module for task 2 """


def append_write(filename="", text=""):
    """
    Append the given text to a file.

    Args:
        filename (str): The name of the file to which text will be appended.
        text (str): The text to be appended to the file.

    Returns:
        int: The number of characters appended to the file.
    """
    try:
        with open(filename, "a", encoding="utf-8") as file:
            count = file.write(text)
        return count
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1
