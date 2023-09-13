#!/usr/bin/python3
"""Module contains definition of ``Rectangle`` class.
A subclass of the ``BaseGeometry`` class.
"""

from .base_geometry import BaseGeometry  # Use relative import

class Rectangle(BaseGeometry):
    """``Rectangle`` class definition.
    """
    def __init__(self, width, height):
        """Initializes the attributes of class ``Rectangle``
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

