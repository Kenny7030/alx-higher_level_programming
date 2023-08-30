#!/usr/bin/python3
"""
Class that defines a square based on 2-square.py
"""


class Square:
    """
    Private instance attribute: size
    """

    def __init__(self, size=0):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = 0
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size value to set.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

