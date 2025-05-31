#!/usr/bin/python3
"""Module for checking inheritance without exact class membership.

This module provides functionality to determine if an object inherits from
a class without being exactly that class. This is useful when you want to
identify objects that have been extended or specialized from a base class.
"""


def inherits_from(obj, a_class):
    """Check if an object inherits from a class but is not exactly that class.

    This function combines the concepts from the previous two functions to
    answer a very specific question: "Is this object a specialized version
    of this class?" It returns True only when the object inherits from the
    class but is not exactly that class.

    This is particularly useful in inheritance hierarchies where you want to
    identify objects that have been extended or modified from a base class.
    For example, if you have a base Animal class and Dog/Cat subclasses,
    this function would return True for Dog instances when checking against
    Animal, but False for Animal instances.

    The logic combines two checks:
    1. isinstance(obj, a_class) - Can this object act like a_class?
    2. type(obj) is not a_class - But it's not exactly a_class?

    Args:
        obj: The object to check
        a_class: The class to check inheritance from

    Returns:
        bool: True if obj inherits from a_class but is not exactly a_class

    Examples:
        >>> class Animal: pass
        >>> class Dog(Animal): pass
        >>> dog = Dog()
        >>> animal = Animal()
        >>> inherits_from(dog, Animal)
        True
        >>> inherits_from(animal, Animal)  # Exact match, so False
        False
        >>> inherits_from(True, int)  # bool inherits from int
        True
        >>> inherits_from(5, int)  # 5 is exactly int, not inherited
        False
    """
    # Two conditions must be met:
    # 1. Object must be compatible with the class (isinstance check)
    # 2. Object must NOT be exactly that class (type check)
    return isinstance(obj, a_class) and type(obj) is not a_class
