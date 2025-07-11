#!/usr/bin/python3
"""BaseGeometry module with area and integer_validator methods."""


class BaseGeometry:
    """BaseGeometry class with validation and area method."""

    def area(self):
        """Raises an Exception indicating area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer greater than 0.

        Args:
            name (str): Name of the variable.
            value (int): Va            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
