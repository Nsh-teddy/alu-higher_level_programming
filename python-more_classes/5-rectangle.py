#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns the rectangle with the character '#'."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Returns a string that can recreate the instance using eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message when a Rectangle instance is deleted."""
        print("Bye rectangle...")
