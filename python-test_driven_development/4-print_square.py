#!/usr/bin/python3
"""
Module for printing squares.
This module provides a function to print a square using the # character.
"""
def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size: The size length of the square (must be a non-negative integer)

    Raises:
        TypeError: If size is not an integer or is a negative float
        ValueError: If size is a negative integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
