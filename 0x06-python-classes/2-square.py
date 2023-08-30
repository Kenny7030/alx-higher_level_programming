#!/usr/bin/python3
"""
    This module defines Square class with a private instance
    attribute, including a default argument and validation on
    the data for the attribute.
"""


class Square:
    """ A class definition for a square. """
    def __init__(self, size=0):
        """
        Initialization of instance attributes.

        Args:
            size (int): The unit length of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = 0
        self.size = size

    @property
    def size(self):
        """ Get the size attribute. """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size attribute.
        Args:
            value (int): The value to set the size to.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

