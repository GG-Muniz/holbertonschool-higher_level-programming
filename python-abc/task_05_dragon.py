#!/usr/bin/env python3
"""
Module for Dragon - Mastering Mixins
"""


class SwimMixin:
    """Mixin class that provides swimming ability"""

    def swim(self):
        """Method for swimming"""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that provides flying ability"""

    def fly(self):
        """Method for flying"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that inherits from both SwimMixin and FlyMixin"""

    def roar(self):
        """Method for roaring"""
        print("The dragon roars!")
