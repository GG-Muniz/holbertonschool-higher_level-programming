#!/usr/bin/python3
"""MyList module.

This module defines a MyList class that inherits from list.
"""


class MyList(list):
    """MyList class that inherits from list.

    This class inherits all the functionality of the built-in list class
    and adds a method to print the list in sorted order.
    """

    def print_sorted(self):
        """Print the list but sorted (ascending sort).

        This method prints the list in ascending order without modifying
        the original list.
        """
        print(sorted(self))
