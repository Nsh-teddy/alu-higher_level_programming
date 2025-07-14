#!/usr/bin/python3
"""
Module that defines a Student class with optional attribute filtering
for JSON serialization.
"""


class Student:
    """
    Defines a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, returns only those attributes
        that exist in the instance.

        Args:
            attrs (list, optional): List of attribute names to include.

        Returns:
            dict: Dictionary of attributes.
        """
        if (isinstance(attrs, list) and
                all(type(attr) is str for attr in attrs)):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__
