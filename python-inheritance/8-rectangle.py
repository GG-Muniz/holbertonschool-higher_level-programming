#!/usr/bin/python3
"""Module that defines Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry.

    This class represents a rectangle with width and height
    attributes that are validated to be positive integers.
    """

    def __init__(self, width, height):
        """Initialize a Rectangle with width and height.

        Both width and height are validated using the
        integer_validator method from BaseGeometry to ensure
        they are positive integers.

        Args:
            width: The width of the rectangle
            height: The height of the rectangle

        Raises:
            TypeError: If width or height is not an integer
            ValueError: If width or height is <= 0
        """
        # Validate width using inherited method
        # This happens before assignment to ensure invalid
        # values never get stored
        self.integer_validator("width", width)

        # Validate height using inherited method
        self.integer_validator("height", height)

        # Store as private attributes using name mangling
        # The double underscore prefix triggers Python's
        # name mangling mechanism
        self.__width = width
        self.__height = height
