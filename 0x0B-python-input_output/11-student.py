#!/usr/bin/python3
"""This module defines a class Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student object."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student object.
        
        If attrs is a list of strings, include only those attributes
        specified in the list.
        """
        if attrs is not None and isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json_data):
        """Replace all attributes of the Student object with the provided JSON data."""
        for key, value in json_data.items():
            setattr(self, key, value)

