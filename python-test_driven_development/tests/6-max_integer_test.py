#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        """Test with a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with max integer at the beginning"""
        self.assertEqual(max_integer([5, 3, 2, 1]), 5)

    def test_max_in_middle(self):
        """Test with max integer in the middle"""
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)

    def test_one_element(self):
        """Test with a list of one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-10, 5, -3, 8, 2]), 8)

    def test_all_same_numbers(self):
        """Test with all identical numbers"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_zero_in_list(self):
        """Test with zero in the list"""
        self.assertEqual(max_integer([0, -1, -5, -3]), 0)

    def test_only_zero(self):
        """Test with only zero"""
        self.assertEqual(max_integer([0]), 0)

    def test_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)

    def test_two_elements(self):
        """Test with two elements"""
        self.assertEqual(max_integer([1, 2]), 2)

    def test_two_elements_reversed(self):
        """Test with two elements in reverse order"""
        self.assertEqual(max_integer([2, 1]), 2)

    def test_floats(self):
        """Test with float numbers"""
        self.assertEqual(max_integer([1.5, 2.7, 3.2, 1.1]), 3.2)

    def test_mixed_int_float(self):
        """Test with mixed integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 1.5]), 3)

    def test_default_parameter(self):
        """Test with no argument (default empty list)"""
        self.assertIsNone(max_integer())

    def test_negative_and_zero(self):
        """Test with negative numbers and zero"""
        self.assertEqual(max_integer([-5, 0, -10, -1]), 0)

    def test_long_list(self):
        """Test with a longer list"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)

    def test_duplicate_max(self):
        """Test with duplicate maximum values"""
        self.assertEqual(max_integer([5, 3, 5, 1, 5]), 5)


if __name__ == '__main__':
    unittest.main()
