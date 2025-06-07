#!/usr/bin/python3
"""Module that contains a function to convert class instance to JSON."""


def class_to_json(obj):
    """Return the dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: The dictionary representation of the object.
    """
    return obj.__dict__
