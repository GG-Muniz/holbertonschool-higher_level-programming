#!/usr/bin/python3
"""Module defining a complete Rectangle class with area calculation.

This module shows how inheritance evolves from basic structure to full
functionality. The Rectangle class now provides complete implementation
of the area method and proper string representation, demonstrating how
subclasses fulfill the contracts established by their parent classes.
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
    """Complete Rectangle class with area calculation
    and string representation.

    This version of Rectangle demonstrates the full power of inheritance by:
    1. Inheriting validation logic from BaseGeometry
    2. Implementing the abstract area() method with rectangle-specific logic
    3. Providing meaningful string representation
    4. Creating a complete, usable geometric shape class

    This class shows how inheritance creates a progression from abstract
    concepts (BaseGeometry) to concrete,
    functional implementations (Rectangle).
    Each class in the hierarchy adds its own unique value while building
    on the foundation provided by its parents.

    Key concepts demonstrated:
    - Method implementation: Providing concrete implementation
    for abstract methods
    - String representation: Making objects human-readable
    - Encapsulation: Private attributes with controlled access
    - Code reuse: Leveraging inherited validation logic
    """

    def __init__(self, width, height):
        """Initialize a rectangle with validated width and height.

        This constructor builds on the validation foundation from BaseGeometry
        to ensure we never create an invalid rectangle. The process follows
        a clear pattern that you'll see repeated in many well-designed classes:

        1. Validate inputs thoroughly
        2. Store validated data securely
        3. Leave the object in a ready-to-use state

        Args:
            width (int): Width of the rectangle (must be positive integer)
            height (int): Height of the rectangle (must be positive integer)

        Raises:
            TypeError: If width or height is not an integer
            ValueError: If width or height is less than or equal to 0
        """
        # Use inherited validation - this is the power of inheritance!
        # We get robust, tested validation logic without writing it ourselves
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Store as private attributes using name mangling
        # This prevents accidental modification from outside the class
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle.

        This method fulfills the contract established by BaseGeometry's
        abstract area() method. Each geometric shape has its own area
        formula, and this implements the rectangle-specific calculation.

        This demonstrates polymorphism: different classes can have methods
        with the same name but different implementations. A Rectangle's
        area() method works differently from a Circle's area() method,
        but they both satisfy the same interface.

        Returns:
            int: The area of the rectangle (width × height)

        Example:
            >>> rect = Rectangle(3, 4)
            >>> rect.area()
            12
        """
        # Rectangle area formula: width × height
        # We access our private attributes directly
        # since we're inside the class
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle.

        This method makes Rectangle objects human-readable and debuggable.
        When you print a Rectangle or convert it to a string, Python calls
        this method to determine what to display.

        The format [Rectangle] width/height provides clear, consistent
        information about the object's type and dimensions. This follows
        a common pattern in object-oriented programming where string
        representations include the class name and key attributes.

        This method demonstrates encapsulation: even though width and height
        are private, the class can still provide controlled access to their
        values through carefully designed methods.

        Returns:
            str: String representation in format "[Rectangle] width/height"

        Example:
            >>> rect = Rectangle(5, 3)
            >>> str(rect)
            '[Rectangle] 5/3'
            >>> print(rect)
            [Rectangle] 5/3
        """
        # Access private attributes from within the class
        # The f-string provides clean, readable formatting
        return f"[Rectangle] {self.__width}/{self.__height}"
