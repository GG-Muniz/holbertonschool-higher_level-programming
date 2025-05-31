#!/usr/bin/python3
"""Module for checking class membership including inheritance.

This module demonstrates the difference between exact type checking and
inheritance-aware type checking. Understanding this distinction is fundamental
to working effectively with object-oriented programming in Python.
"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class or inherits from it.

    This function uses isinstance() which is inheritance-aware, meaning it
    considers the entire inheritance hierarchy. This is usually what you want
    when checking if an object can be used in a particular context.

    Think of this as asking "Can this object behave like this class?"
    If a Square inherits from Rectangle, then a Square can behave like a
    Rectangle, so isinstance(square, Rectangle) returns True.

    This follows the Liskov Substitution Principle: objects of a superclass
    should be replaceable with objects of a subclass without breaking
    the application.

    Args:
        obj: The object to check
        a_class: The class to check against

    Returns:
        bool: True if obj is an instance of a_class or inherits from it

    Examples:
        >>> is_kind_of_class(1, int)
        True
        >>> is_kind_of_class(1, object)  # Everything inherits from object
        True
        >>> is_kind_of_class(True, bool)
        True
        >>> is_kind_of_class(True, int)  # bool inherits from int
        True
        >>> is_kind_of_class("hello", str)
        True
        >>> is_kind_of_class("hello", object)  # str inherits from object
        True
    """
    # isinstance() traverses the inheritance hierarchy
    # It checks if obj's class is a_class OR
    # if obj's class inherits from a_class
    return isinstance(obj, a_class)
