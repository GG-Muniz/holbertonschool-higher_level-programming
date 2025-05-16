#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements (use 0 for missing ones)
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Return a new tuple with the sum of first and second elements
    return (a[0] + b[0], a[1] + b[1])
