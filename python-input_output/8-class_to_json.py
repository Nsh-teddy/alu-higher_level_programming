#!/usr/bin/python3
"""
Module that returns the dictionary description of an object
for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description for JSON serialization of an object.

    Args:
        obj (any): An instance of a class with serializable attributes.

    Returns:
        dict: The dictionary containing serializable attributes of the object.
    """
    return obj.__dict__
