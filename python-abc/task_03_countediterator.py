#!/usr/bin/env python3
"""
Module for CountedIterator - Keeping Track of Iteration
"""


class CountedIterator:
    """An iterator that keeps track of the number of items iterated"""

    def __init__(self, iterable):
        """Initialize with an iterable and set counter to 0"""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Get the next item and increment the counter"""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise

    def __iter__(self):
        """Return self as an iterator"""
        return self

    def get_count(self):
        """Return the current count of items iterated"""
        return self.count
