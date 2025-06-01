#!/usr/bin/env python3
"""
Module for Shapes, Interfaces, and Duck Typing
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """Abstract method to calculate area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate perimeter"""
        pass


class Circle(Shape):
    """Circle class that inherits from Shape"""

    def __init__(self, radius):
        """Initialize Circle with radius"""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape"""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Function that prints area and perimeter of a shape
    Uses duck typing - doesn't check the type explicitly
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
