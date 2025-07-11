#!/usr/bin/python3
"""Defines inherits_from function."""


def inherits_from(obj, a_class):
    """
    Checks if object is an instance of a subclass of a_class.

    Args:
        obj: the object to check
        a_class: the class to compare against

    Returns:
        True if obj is an instance of a subclass of a_class,
        otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
