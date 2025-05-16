#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:  # Check if list exists and is not empty
        for i in reversed(my_list):
            print("{:d}".format(i))
