#!/usr/bin/python3
"""Module that defines is_same_class function"""


def is_same_class(obj, a_class):
    """Check if object is exactly an instance of a class.

    This function returns True if and only if the object
    is exactly an instance of the specified class. It will
    return False if the object is an instance of a subclass.

    Args:
        obj: The object to check
        a_class: The class to check against

    Returns:
        bool: True if obj is exactly an instance of a_class,
              False otherwise
    """
    # Use type() to get the exact class of the object
    # Then compare it directly with the specified class
    return type(obj) is a_class
