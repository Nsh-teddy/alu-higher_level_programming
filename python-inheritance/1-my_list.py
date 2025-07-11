#!/usr/bin/python3
"""This module defines a class MyList that inherits from list"""


class MyList(list):
    """Inherits from the built-in list class"""

    def print_sorted(self):
        """Prints the list, but sorted in ascending order"""
        print(sorted(self))
