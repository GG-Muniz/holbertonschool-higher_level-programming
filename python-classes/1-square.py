#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """A class that defines a square with a private size attribute."""

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size: The size of the square.
        """
        self.__size = size
