#!/usr/bin/python3
"""Module that defines Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle.

    A square is a special rectangle where all sides are equal.
    This class represents a square using a single size parameter
    for all sides.
    """

    def __init__(self, size):
        """Initialize a Square with a given size.

        The square is implemented as a rectangle where width
        and height are both equal to size. The size is validated
        to ensure it's a positive integer.

        Args:
            size: The length of all sides of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is <= 0
        """
        # First, validate the size using inherited method
        # We validate before calling super() to ensure
        # we never create an invalid square
        self.integer_validator("size", size)

        # Store size as a private attribute
        # This follows the same pattern as Rectangle
        self.__size = size

        # Initialize the parent Rectangle with equal width and height
        # This is the key insight: a square is just a rectangle
        # where width equals height
        super().__init__(size, size)

    def area(self):
        """Calculate and return the area of the square.

        Since a square's area is size squared, we could calculate
        it as self.__size ** 2. However, to demonstrate inheritance
        and code reuse, we'll use Rectangle's area method.

        Returns:
            int: The area of the square
        """
        # We inherit area calculation from Rectangle
        # Rectangle's area() returns width * height
        # For a square, width = height = size, so this gives size²
        return super().area()
