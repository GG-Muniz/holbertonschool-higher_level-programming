#!/usr/bin/python3
class Student:
    """Define a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a
        Student instance.

        If attrs is a list of strings, only attributes
        in this list are retrieved.
        Otherwise, all attributes are retrieved.
        """
        if isinstance(attrs, list) and all(isinstance(item, str)
                                           for item in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance.

        Assumes json will always be a dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
