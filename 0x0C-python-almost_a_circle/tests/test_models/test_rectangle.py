"""
test cases for the rectangle module
 run with python3 -m unittest discover tests
run with python3 -m unittest tests/test_models/test_rectangle.py
"""

# import
import unittest
import sys
from io import StringIO
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

    # Test display() Method
    def test_display(self):
        r = Rectangle(2, 2)
        expected_output = "##\n##\n"
        captured_output = StringIO()
        sys.stdout = captured_output

        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

        r = Rectangle(2, 3, 2, 4)
        expected_output = "\n\n\n\n  ##\n  ##\n  ##\n"
        captured_output = StringIO()
        sys.stdout = captured_output

        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    # Test __str__() Method
    def test_str(self):
        rec = Rectangle(3, 5, 0, 0, 3)
        expected_output = "[Rectangle] (3) 0/0 - 3/5"
        self.assertEqual(expected_output, str(rec))

        rec2 = Rectangle(2, 4, 6, 8, 10)
        expected_output = "[Rectangle] (10) 6/8 - 2/4"
        self.assertEqual(expected_output, str(rec2))

    # Test update() Method
    def test_update(self):
        rec = Rectangle(3, 5, 0, 0, 3)
        rec.update(2, 3, 4, 5, 6)
        self.assertEqual(str(rec), '[Rectangle] (2) 5/6 - 3/4')
        self.assertEqual(rec.id, 2)
        self.assertEqual(rec.width, 3)
        self.assertEqual(rec.height, 4)
        self.assertEqual(rec.x, 5)
        self.assertEqual(rec.y, 6)

    # test with invalid arguments
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec = Rectangle(3, 5, "string", 0, 3)

         # test with **kwargs
        rec = Rectangle(3, 5, 0, 0, 3)
        rec.update(id=1, width=2, height=3, x=4, y=5)
        self.assertEqual(rec.id, 1)
        self.assertEqual(rec.width, 2)
        self.assertEqual(rec.height, 3)
        self.assertEqual(rec.x, 4)
        self.assertEqual(rec.y, 5)


if __name__ == "__main__":
    unittest.main()
# run with "python3 -m unittest discover tests"
