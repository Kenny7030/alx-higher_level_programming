#!/usr/bin/python3
""" Module for task 0 """

def read_file(filename=""):
    """
    Read the contents of a file and print them to the standard output.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = file.read()
            print(data, end="")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
