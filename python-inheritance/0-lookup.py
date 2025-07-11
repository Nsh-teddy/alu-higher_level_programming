#!/usr/bin/python3
"""
Defines a function that returns available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing attribute and method names.
    """
    return dir(obj)
