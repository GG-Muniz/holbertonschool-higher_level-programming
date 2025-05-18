#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class for max_integer function"""

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test with a list containing a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        """Test with a list of positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        """Test with a list of negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with a list of mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_duplicate_numbers(self):
        """Test with a list containing duplicate numbers"""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_max_at_beginning(self):
        """Test with the maximum value at the beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test with the maximum value in the middle"""
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_max_at_end(self):
        """Test with the maximum value at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_floats(self):
        """Test with a list of floats"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)

    def test_mixed_types(self):
        """Test with a list of mixed integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)

    def test_string(self):
        """Test with a string (list of characters)"""
        self.assertEqual(max_integer("abcdefg"), "g")

    def test_list_of_strings(self):
        """Test with a list of strings"""
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_empty_string(self):
        """Test with an empty string"""
        self.assertIsNone(max_integer(""))

if __name__ == '__main__':
    unittest.main()
