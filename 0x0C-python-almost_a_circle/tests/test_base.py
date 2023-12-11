"""
test case for Base module
"""
import unittest
# import module
from models import base
Base = base.Base


class TestBase(unittest.TestCase):
    def test_base_with_id(self):
        base1 = Base(20)
        self.assertEqual(base1.id, 20)

    def test_without_id(self):
        base2 = Base()
        base3 = Base()
        base4 = Base()
        self.assertEqual(base2.id, 1)
        self.assertEqual(base3.id, 2)
        # test increment
        self.assertEqual(Base._Base__nb_objects, 3)

    def test_change_id(self):
        base5 = Base(22)
        base5.id = 44
        self.assertEqual(base5.id, 44)

    def test_id_with_string(self):
        base6 = Base("string")
        self.assertEqual(base6.id, "string")

    def test_negative_number(self):
        base7 = Base(-2)
        self.assertEqual(base7.id, -2)

    def test_type(self):
        self.assertEqual(type(Base), type)

    def test_multiple_args(self):
        with self.assertRaises(TypeError):
            base8 = Base(2, 5)


if __name__ == "__main__":
    unittest.main()
# run with "python3 -m unittest discover test"
