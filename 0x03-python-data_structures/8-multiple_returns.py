#!/usr/bin/python3
# 8-multiple_returns.py

"""
Module - multiple_returns
Contains a function that returns the length of a string and its first character
"""

def multiple_returns(sentence):
    """
    Returns the length of a string and its first character.
    Args:
        sentence (str): The input string.
    Returns:
        A tuple containing the length of the string and its first character.
    """
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])

