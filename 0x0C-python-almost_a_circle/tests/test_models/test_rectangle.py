"""
test cases for the rectangle module
 run with python3 -m unittest discover tests
run with python3 -m unittest tests/test_models/test_rectangle.py
"""

# import
import unittest
from models import rectangle
Rectangle = rectangle.Rectangle


class TestRectangle(unittest.TestCase):
    def test_valid_attributes(self):
        """
        test all attributes
        """
        r1 = Rectangle(2, 4, 6, 8, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 6)
        self.assertEqual(r1.y, 8)
        self.assertEqual(r1.id, 1)

    def test_default_attributes(self):
        r2 = Rectangle(2, 4)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertTrue(r2.id is not None)

    def test_class(self):
        r3 = Rectangle(2, 8)
        self.assertEqual(type(r3), Rectangle)

    def test_valid_height_width(self):
        r4 = Rectangle(3, 6)
        r4.width = 5
        r4.height = 9
        self.assertEqual(r4.width, 5)
        self.assertEqual(r4.height, 9)

    def test_negative_value(self):
        r5 = Rectangle(6, 4)
        with self.assertRaises(ValueError):
            r5.width = -1
        with self.assertRaises(ValueError):
            r5.height = -8

    def test_with_invalid_types(self):
        # strings
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("string", 3)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(7, "string")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(4, 3, "one", 1, 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(4, 3, 7, "two", 5)
        # floats
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(4.5, 3)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, 3.2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(4, 3, 4.9, 1, 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(4, 3, 7, 5.7, 5)

    # Test area() Method
    def test_area(self):
        rect = Rectangle(2, 2)
        self.assertEqual(rect.area(), 4)
        rect = Rectangle(5, 8)
        self.assertEqual(rect.area(), 40)
        self.assertEqual(Rectangle(1, 2, 0, 0, 5).area(), 2)
