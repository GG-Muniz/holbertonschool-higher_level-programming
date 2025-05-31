#!/usr/bin/python3
"""Module that defines MyList class"""


class MyList(list):
    """MyList class that inherits from list

    This class extends the built-in list class with
    additional functionality to print a sorted version
    of the list without modifying the original.
    """

    def print_sorted(self):
        """Print the list in ascending order

        This method creates a sorted copy of the list
        and prints it. The original list remains unchanged.
        """
        # Create a copy of the list and sort it
        # We use sorted() which returns a new sorted list
        # This ensures the original list is not modified
        sorted_list = sorted(self)

        # Print the sorted list
        print(sorted_list)
