#!/usr/bin/python3
"""Module that defines a Student class."""


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

    def to_json(self):
        """Retrieve a dictionary representation of a
        Student instance.

        Returns:
            dict: The dictionary representation of the instance.
        """
        return self.__dict__
