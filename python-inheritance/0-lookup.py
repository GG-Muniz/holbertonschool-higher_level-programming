#!/usr/bin/python3
"""Module that provides object introspection functionality.

This module contains a function to examine the attributes and methods
available on any Python object, which is fundamental for understanding
inheritance and object composition.
"""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    This function uses Python's built-in dir() function to provide
    introspection capabilities. It's particularly useful when working
    with inheritance to see what methods and attributes are available
    on an object, including those inherited from parent classes.

    Args:
        obj: Any Python object to inspect

    Returns:
        list: A list of strings representing all available attributes
              and methods for the given object

    Example:
        >>> lookup(int)  # doctest: +ELLIPSIS
        ['__abs__', '__add__', ..., 'bit_length', ...]
    """
    return dir(obj)
