#!/usr/bin/python3
"""
Module that returns a Python object from a JSON string.
"""

import json


def from_json_string(my_str):
    """
    Returns the Python object represented by a JSON string.

    Args:
        my_str (str): JSON string representation of an object.

    Returns:
        object: The Python data structure represented by my_str.
    """
    return json.loads(my_str)
