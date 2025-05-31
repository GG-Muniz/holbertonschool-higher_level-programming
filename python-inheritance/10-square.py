#!/usr/bin/python3
"""Module defining a Square class that inherits from Rectangle.

This module demonstrates multi-level inheritance where Square inherits
from Rectangle, which inherits from BaseGeometry. This creates a three-level
hierarchy that shows how inheritance can be layered to create increasingly
specialized classes while maintaining the benefits of code reuse.
"""


class BaseGeometry:
    """Base class for geometry shapes with area calculation and validation."""

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
    """Rectangle class with area calculation and string representation."""

    def __init__(self, width, height):
        """Initialize a rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Square class that inherits from Rectangle.

    This class demonstrates multi-level inheritance and the concept of
    specialization. In mathematical terms, a square IS a rectangle where
    width equals height. This "is-a" relationship makes inheritance perfect
    for modeling this concept in code.

    Think about what Square inherits through this hierarchy:

    From BaseGeometry (grandparent):
    - integer_validator() method for validation
    - area() method interface (implemented by Rectangle)

    From Rectangle (parent):
    - __init__() constructor logic (we'll override this)
    - area() method implementation (width × height works for squares too!)
    - __str__() method (we'll inherit this, so it says [Rectangle])

    This demonstrates the principle of inheritance chain: Square gets
    functionality from both its parent and grandparent classes. Each
    level adds its own value while building on the foundation below.

    Notice something elegant here: we don't need to reimplement area()!
    A square's area is still width × height, it just happens that
    width and height are equal. The Rectangle's area() method works
    perfectly for squares without any modification.

    This is a perfect example of the Liskov Substitution Principle:
    anywhere you can use a Rectangle, you can use a Square instead,
    because a Square IS a Rectangle with additional constraints.
    """

    def __init__(self, size):
        """Initialize a square with equal width and height.

        This constructor shows how to properly specialize an inherited class.
        Rather than duplicating the Rectangle's initialization logic, we:

        1. Validate our input using inherited validation
        2. Call the parent constructor with appropriate parameters
        3. Store our specific data for later use

        The key insight: a square is just a rectangle where width equals
        height, so we can reuse Rectangle's constructor by passing the
        same value for both width and height.

        The super() call is crucial here. It ensures that all the parent's
        initialization logic runs properly. This includes:
        - Rectangle's validation calls
        - Setting up private __width and __height attributes
        - Any future enhancements to Rectangle's constructor

        Args:
            size (int): Size of the square (must be positive integer)
                       This becomes both width and height

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than or equal to 0
        """
        # First, validate our input using inherited method
        # This ensures we catch bad inputs early with clear error messages
        self.integer_validator("size", size)

        # Call the parent constructor with size for both width and height
        # super() ensures we properly initialize the Rectangle portion
        # of our Square object
        super().__init__(size, size)

        # Store the size for potential future use
        # This gives us easy access to the square's dimension
        self.__size = size

        # Note: We now have several ways to access our square's dimension:
        # - self.__size (our specific attribute)
        # - self._Rectangle__width (inherited private attribute)
        # - self._Rectangle__height (inherited private attribute)
        # The last two are equal for squares, but __size is clearer
