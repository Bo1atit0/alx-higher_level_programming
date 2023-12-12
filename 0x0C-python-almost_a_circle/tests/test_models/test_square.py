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

    # Test update() Method
    def test_sq_update(self):
        sq = Square(3, 5, 0, 0)
        sq.update(2, 3, 4, 5)
        self.assertEqual(str(sq), '[Square] (2) 4/5 - 3')
        self.assertEqual(sq.id, 2)
        self.assertEqual(sq.size, 3)
        self.assertEqual(sq.x, 4)
        self.assertEqual(sq.y, 5)

    # test with invalid arguments
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq = Square(3, 5, "one", 1)

        # test with **kwargs
        sq = Square(3, 5, 0, 0)
        sq.update(id=1, size=2, x=4, y=5)
        self.assertEqual(sq.id, 1)
        self.assertEqual(sq.size, 2)
        self.assertEqual(sq.x, 4)
        self.assertEqual(sq.y, 5)

    def test_to_dict(self):
        sq = Square(10, 2, 9, 5)
        # r1.update(10, 2, 1, 9, 5)
        sq_dictionary = sq.to_dictionary()
        output = {'id': 5, 'size': 10, 'x': 2, 'y': 9}
        self.assertEqual(output, sq_dictionary)

        # test type
        self.assertIsInstance(sq_dictionary, dict)
