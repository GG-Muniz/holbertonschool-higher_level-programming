#!/usr/bin/env python3
"""
Module for Abstract Animal Class and its Subclasses
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals"""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses"""
        pass


class Dog(Animal):
    """Dog class that inherits from Animal"""

    def sound(self):
        """Implementation of sound method for Dog"""
        return "Bark"


class Cat(Animal):
    """Cat class that inherits from Animal"""

    def sound(self):
        """Implementation of sound method for Cat"""
        return "Meow"
