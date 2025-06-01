#!/usr/bin/env python3
"""
Module for FlyingFish - Exploring Multiple Inheritance
"""


class Fish:
    """Fish class with swimming abilities"""

    def swim(self):
        """Method for swimming"""
        print("The fish is swimming")

    def habitat(self):
        """Method for habitat"""
        print("The fish lives in water")


class Bird:
    """Bird class with flying abilities"""

    def fly(self):
        """Method for flying"""
        print("The bird is flying")

    def habitat(self):
        """Method for habitat"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class that inherits from both Fish and Bird"""

    def fly(self):
        """Override fly method for FlyingFish"""
        print("The flying fish is soaring!")

    def swim(self):
        """Override swim method for FlyingFish"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override habitat method for FlyingFish"""
        print("The flying fish lives both in water and the sky!")
