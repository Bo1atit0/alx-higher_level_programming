#!/usr/bin/python3


"""
Testing the 6-max_integer module

This text file contains unittests for the max_integer
function in the 6-max_integer module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class MyTests(unittest.TestCase):
    """
    unittest class for the max_integer function
    """

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        self.assertEqual(max_integer([2]), 2)

    def test_positive_elements(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_elements(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_elements(self):
        self.assertEqual(max_integer([1, 2, -3, 4]), 4)

    def test_float_elements(self):
        self.assertEqual(max_integer([1.0, 2.0, 3.0, 4.0]), 4)

    def test_string_elements(self):
        self.assertEqual(max_integer(['1', '2', '3', '4']), '4')

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer(['a', 1, 2, 3])


if __name__ == '__main__':
    unittest.main()
