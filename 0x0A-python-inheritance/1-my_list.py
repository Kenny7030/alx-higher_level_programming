#!/usr/bin/python3
"""Module containing the MyList class definition."""


class MyList(list):
    """Custom list class with additional functionality."""

    def print_sorted(self):
        """Prints the elements of the list in sorted order."""
        print(sorted(self))

