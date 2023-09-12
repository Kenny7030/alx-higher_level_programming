#!/usr/bin/python3
""" Module for task 13 """


def append_after(filename="", search_string="", new_string=""):
    """
    Appends a new string after the first occurrence of a search string in a file.

    Args:
        filename (str): The name of the file to operate on.
        search_string (str): The string to search for in each line of the file.
        new_string (str): The string to append after the search string.

    """
    lines = []
    with open(filename, "r") as f:
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w') as f:
        f.writelines(lines)

