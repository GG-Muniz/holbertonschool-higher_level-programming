#!/usr/bin/python3
"""Module that defines BaseGeometry class"""


class BaseGeometry:
    """Base class for geometric shapes.

    This class provides basic functionality for geometric
    calculations including area computation and value
    validation for geometric properties.
    """

    def area(self):
        """Calculate the area of the geometric shape.

        This method is not implemented in the base class
        and must be overridden by subclasses.

        Raises:
            Exception: Always, as this method is not
                      implemented in the base class
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer.

        This method ensures that values used for geometric
        properties (like width, height, radius) are valid
        positive integers.

        Args:
            name (str): The name of the parameter being
                       validated (assumed to always be string)
            value: The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        # Check if value is exactly an integer
        # We use type() instead of isinstance() to handle
        # the bool case - bool is a subclass of int in Python
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        # Check if value is positive
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
