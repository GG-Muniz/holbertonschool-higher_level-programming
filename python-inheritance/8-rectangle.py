#!/usr/bin/python3
"""Module defining a Rectangle class that inherits from BaseGeometry.

This module demonstrates concrete inheritance where a subclass inherits
and uses functionality from its parent class. The Rectangle class shows
how inheritance eliminates code duplication and creates a robust,
well-validated geometric shape.
"""


class BaseGeometry:
    """Base class for geometry shapes with area calculation and validation.

    This is included here for the Rectangle to inherit from.
    In a real project, this would typically be imported from another module.
    """

    def area(self):
        """Calculate the area of the geometry shape.

        Raises:
            Exception: This method must be implemented by subclasses
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer.

        Args:
            name (str): Name of the parameter being validated
            value: Value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry.

    This class demonstrates the practical application of inheritance.
    By inheriting from BaseGeometry, Rectangle automatically gains:
    1. The integer_validator method for input validation
    2. The area method interface (which it must implement)
    3. All the underlying object functionality

    The Rectangle class focuses on what makes it unique: storing width
    and height dimensions and ensuring they're properly validated.

    Notice how inheritance eliminates code duplication:
    - We don't rewrite validation logic (inherited from BaseGeometry)
    - We don't redefine the area method interface (inherited)
    - We only implement what's specific to rectangles

    This follows the DRY principle: Don't Repeat Yourself.
    """

    def __init__(self, width, height):
        """Initialize a rectangle with width and height.

        This constructor demonstrates several important inheritance concepts:

        1. Using inherited methods: We call self.integer_validator() which
           is inherited from BaseGeometry. This ensures our dimensions are
           valid without rewriting validation logic.

        2. Private attributes: We use name mangling (__width, __height) to
           make these attributes private. Python transforms these names to
           _Rectangle__width and _Rectangle__height internally.

        3. Validation before storage: We validate first, then store. This
           ensures the object is never in an invalid state.

        The constructor follows this pattern:
        1. Validate inputs (using inherited validator)
        2. Store validated data in private attributes
        3. The object is now ready for use

        Args:
            width (int): Width of the rectangle (must be positive integer)
            height (int): Height of the rectangle (must be positive integer)

        Raises:
            TypeError: If width or height is not an integer
            ValueError: If width or height is less than or equal to 0
        """
        # Validate width using inherited method from BaseGeometry
        # This demonstrates code reuse - we don't reimplement validation
        self.integer_validator("width", width)

        # Validate height using the same inherited method
        self.integer_validator("height", height)

        # Store dimensions as private attributes using name mangling
        # The double underscore prefix makes Python transform these names
        # to _Rectangle__width and _Rectangle__height internally
        self.__width = width
        self.__height = height

        # Note: We don't provide getter/setter methods as per requirements
        # The dimensions are truly private and can only be accessed by
        # methods within this class
