#!/usr/bin/python3
"""Module defining a geometry base class with validation capabilities.

This module demonstrates how base classes provide shared functionality
that all subclasses can use. The validation logic here will be inherited
by all geometry shapes, eliminating code duplication and ensuring
consistent validation across the entire hierarchy.
"""


class BaseGeometry:
    """Base class for geometry shapes with area calculation and validation.

    This version of BaseGeometry adds crucial validation functionality that
    will be shared by all geometry shapes. Think about it: every shape needs
    positive integer dimensions, so rather than implementing this validation
    in each subclass, we put it in the base class where it can be inherited.

    This demonstrates one of inheritance's greatest strengths: code reuse.
    Write the validation logic once, use it everywhere. This approach:
    1. Reduces code duplication
    2. Ensures consistent validation across all shapes
    3. Makes maintenance easier (change validation logic in one place)
    4. Reduces the chance of bugs (implement complex logic once, correctly)

    The integer_validator method showcases careful error handling with
    specific exception types and clear error messages. This makes debugging
    much easier for developers using your geometry classes.
    """

    def area(self):
        """Calculate the area of the geometry shape.

        This abstract method must be implemented by all subclasses.
        Each geometry shape has its own area calculation formula.

        Raises:
            Exception: Always raised to indicate this method must be overridden
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer.

        This method provides shared validation logic for all geometry shapes.
        All shapes need positive integer dimensions, so this validation
        prevents invalid shapes from being created and provides clear
        error messages when validation fails.

        The method checks two conditions:
        1. Is the value actually an integer? (not float, string, etc.)
        2. Is the value positive? (greater than 0)

        Notice the careful type checking: we use 'type(value) is not int'
        rather than 'not isinstance(value, int)' because in Python,
        bool is a subclass of int. We want to reject boolean values
        even though they're technically integers.

        Args:
            name (str): The name of the parameter being validated
                       (used in error messages for clarity)
            value: The value to validate (should be a positive integer)

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0

        Examples:
            >>> bg = BaseGeometry()
            >>> bg.integer_validator("width", 5)  # Valid - no exception
            >>> bg.integer_validator("width", "5")  # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
            TypeError: width must be an integer
        """
        # First check: Is it actually an integer?
        # We use 'type(value) is not int' instead of 'not isinstance(value, int)'
        # because bool inherits from int, but we want to reject True/False
        if type(value) is not int:
            # Use f-string for clear, readable error message
            raise TypeError(f"{name} must be an integer")

        # Second check: Is it positive?
        # We require > 0, not >= 0, because dimensions can't be zero
        if value <= 0:
            # Again, clear error message explaining the requirement
            raise ValueError(f"{name} must be greater than 0")
