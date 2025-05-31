#!/usr/bin/python3
"""Module defining a custom list class that extends built-in
list functionality.

This module demonstrates basic inheritance by creating a class that inherits
from Python's built-in list class and adds additional functionality.
"""


class MyList(list):
    """A custom list class that inherits from the built-in list class.

    This class demonstrates inheritance by extending the built-in list
    with additional functionality while preserving all existing list
    behavior. It's a perfect example of the "is-a" relationship in
    object-oriented programming - a MyList IS a list, but with extra features.

    Inherits all methods from list: append, extend, remove, pop, etc.
    """

    def print_sorted(self):
        """Print the list in ascending sorted order without
        modifying the original.

        This method demonstrates how to add new functionality to an inherited
        class. It uses the built-in sorted() function which returns a new
        sorted list, leaving the original list unchanged.

        The method doesn't return anything -
        it simply prints the sorted version.
        This follows the single responsibility principle: the method does one
        thing and does it well.

        Example:
            >>> my_list = MyList([3, 1, 4, 1, 5])
            >>> my_list.print_sorted()
            [1, 1, 3, 4, 5]
            >>> print(my_list)  # Original unchanged
            [3, 1, 4, 1, 5]
        """
        # sorted() returns a new list, preserving the original
        # This is safer than using self.sort() which would modify the original
        print(sorted(self))
