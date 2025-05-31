#!/usr/bin/python3
"""Module defining a Square class with custom string representation.

This module completes our geometry hierarchy by demonstrating method
overriding. The Square class inherits from Rectangle but provides its
own implementation of the __str__() method to display "[Square]" instead
of "[Rectangle]". This shows how subclasses can customize inherited
behavior while maintaining the benefits of inheritance.
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
    """Square class with custom string representation.

    This final version of Square demonstrates method overriding, one of the
    fundamental concepts in object-oriented programming. While Square inherits
    most behavior from Rectangle unchanged, it provides its own implementation
    of the __str__() method to display more accurate information.

    Method overriding allows subclasses to:
    1. Customize inherited behavior while keeping the same interface
    2. Provide specialized implementations that are more appropriate
    3. Maintain polymorphism (different classes, same method names)

    This Square class showcases the complete inheritance hierarchy:

    BaseGeometry (abstract base)
    ├── Provides: integer_validator(), area() interface
    │
    └── Rectangle (concrete implementation)
        ├── Provides: area() implementation, __str__() method
        ├── Uses: integer_validator() from BaseGeometry
        │
        └── Square (specialized rectangle)
            ├── Inherits: area(), integer_validator()
            ├── Customizes: __init__(), __str__()
            └── Adds: Square-specific behavior

    Notice how each level adds value while building on the foundation below.
    This creates a robust, maintainable hierarchy where changes at higher
    levels automatically benefit all subclasses.
    """

    def __init__(self, size):
        """Initialize a square with equal width and height.

        This constructor maintains the same logic as the previous version,
        demonstrating that method overriding is selective - we override only
        what needs to be different, while keeping everything else the same.

        Args:
            size (int): Size of the square (must be positive integer)

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than or equal to 0
        """
        # Validate using inherited method from BaseGeometry
        self.integer_validator("size", size)

        # Initialize as a Rectangle with equal width and height
        super().__init__(size, size)

        # Store the size for our custom string representation
        self.__size = size

    def __str__(self):
        """Return a string representation specific to squares.

        This method demonstrates method overriding in action. By defining
        our own __str__() method, we replace the one inherited from Rectangle.
        When Python needs to convert a Square to a string, it will call this
        method instead of Rectangle's version.

        This is powerful because:
        1. The interface remains the same (str(square) still works)
        2. The behavior is customized for the specific class
        3. Polymorphism is maintained (str() works on any geometry object)

        Method overriding follows a simple rule: Python looks for methods
        starting from the most specific class and works up the inheritance
        chain until it finds the method. This means:

        - Square objects use Square.__str__()
        - Rectangle objects use Rectangle.__str__()
        - Any geometry object can be converted to string

        Notice how we access self.__size instead of the inherited private
        attributes. This is cleaner and more semantic - we're dealing with
        a square, so "size" is more meaningful than "width" and "height".

        Returns:
            str: String representation in format "[Square] size/size"

        Example:
            >>> square = Square(5)
            >>> str(square)
            '[Square] 5/5'
            >>> print(square)
            [Square] 5/5
        """
        # Use our stored size attribute for clear, semantic code
        # The format shows that it's a square with equal dimensions
        return f"[Square] {self.__size}/{self.__size}"

        # Alternative implementation using inherited attributes:
        # return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
        # This would work but is less clean and harder to understand
