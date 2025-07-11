#!/usr/bin/python3
"""Function inherits_from"""

def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class that inherits from a_class"""
    # type(obj) is the class of obj
    # Check if a_class is a parent class of type(obj) but not the same class
    return issubclass(type(obj), a_class) and type(obj) != a_class
