#!/usr/bin/python3
"""BaseGeometry class module"""

class BaseGeometry:
    """Class for base geometry"""

    def area(self):
        """Raises an exception for area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value as an integer greater than 0"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
