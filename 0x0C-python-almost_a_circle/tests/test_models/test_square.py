"""
test cases for the square module
 run with python3 -m unittest discover tests
run with python3 -m unittest tests/test_models/test_square.py
"""

# import
import unittest
import sys
from io import StringIO
from models import square
Square = square.Square


class Test_Square(unittest.TestCase):
    def test_valid_args(self):
        sq = Square(5, 2, 3, 2)
        self.assertEqual(sq.size, 5)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 3)
        self.assertEqual(sq.id, 2)

    def test_default_args(self):
        sq = Square(5)
        self.assertEqual(sq.size, 5)
        self.assertEqual(sq.x, 0)
        self.assertEqual(sq.y, 0)
        self.assertTrue(sq.id is not None)

    def test_invalid_args(self):
        with self.assertRaises(TypeError):
            sq = Square("five")

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            sq = Square(1, 2, 3, 4, 5, 5, 7, 8, 9)
