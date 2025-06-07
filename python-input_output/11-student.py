#!/usr/bin/python3
"""Module that defines a Student class with filtered JSON
representation."""


class Student:
    """Define a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a
        Student instance.

        Args:
            attrs (list): List of attribute names to retrieve.
                         If None, all attributes are retrieved.

        Returns:
            dict: The dictionary representation of the instance.
        """
        if isinstance(attrs, list) and all(isinstance(item, str)
                                           for item in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
