#!/usr/bin/python3
"""Module defining a geometry base class with abstract area method.

This module demonstrates the concept of abstract methods in inheritance.
An abstract method defines what subclasses must implement while not
providing the implementation itself. This creates a contract that all
subclasses must follow.
"""


class BaseGeometry:
    """Base class for geometry shapes with area calculation interface.

    This version of BaseGeometry introduces the concept of an abstract method.
    The area() method defines what every geometry shape should be able to do
    (calculate its area) but doesn't provide the implementation because each
    shape calculates area differently.

    This design pattern is called the Template Method pattern. The base class
    defines the interface (what methods should exist) but leaves the specific
    implementation to the subclasses. This ensures consistency across all
    geometry shapes while allowing for shape-specific calculations.

    Key concepts demonstrated:
    1. Abstract methods: Methods that must be overridden by subclasses
    2. Interface definition: Establishing what all subclasses must provide
    3. Fail-fast design: Raising an exception immediately if the method
       isn't properly implemented in a subclass

    The Exception with a descriptive message serves two purposes:
    - It prevents silent failures if someone forgets to implement area()
    - It provides clear guidance about what needs to be implemented
    """

    def area(self):
        """Calculate the area of the geometry shape.

        This is an abstract method that must be implemented by all subclasses.
        Each geometry shape (rectangle, circle, triangle) has its own formula
        for calculating area, so this base class cannot provide a generic
        implementation.

        The method raises an Exception to ensure that subclasses override it.
        This is a common pattern in object-oriented programming called
        "abstract method" - it defines the interface without implementation.

        Raises:
            Exception: Always raised with message "area() is not implemented"
                      to indicate this method must be overridden

        Note:
            In more advanced Python, you might
            use the abc (Abstract Base Class)
            module for this, but this simpler approach demonstrates the concept
            clearly and is sufficient for many use cases.
        """
        # This exception ensures subclasses
        # must provide their own implementation
        # The message clearly explains what needs to be done
        raise Exception("area() is not implemented")
