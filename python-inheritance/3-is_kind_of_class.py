#!/usr/bin/python3
"""Function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance or subclass instance of a_class"""
    return isinstance(obj, a_class)
