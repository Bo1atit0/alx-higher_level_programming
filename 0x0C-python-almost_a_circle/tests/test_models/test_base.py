"""
test case for Base module
run with python3 -m unittest discover tests
run with python3 -m unittest tests/test_models/test_base.py
"""
import unittest
import json
# import module
from models import base, square, rectangle
Base = base.Base
Rectangle = rectangle.Rectangle
Square = square.Square


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

    def test_to_json_string(self):
        # empty list
        dict_list = []
        expected_output = '[]'
        result = Base.to_json_string(dict_list)
        self.assertEqual(expected_output, result)

        # valid list
        r1 = [{"id": 1, "name": "May"}, {"id": 2, "name": "Mark"}]
        output = '[{"id": 1, "name": "May"}, {"id": 2, "name": "Mark"}]'
        json_dictionary = Base.to_json_string(r1)
        self.assertEqual(json_dictionary, output)

        # None
        dict_list = None
        expected_output = '[]'
        result = Base.to_json_string(dict_list)
        self.assertEqual(expected_output, result)

    def test_save_to_file(self):
        """Test save to file with instance that inherited from Base.
        """
        r = Rectangle(10, 7, 2, 8, 99)
        r2 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([r, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                json.dumps([r.to_dictionary(), r2.to_dictionary()]),
                file.read())

    def test_save_to_file_empty_list(self):
        """Test if empty list is given to be saved.
        """
        # Create an empty list
        list_of_objs = []
        # Save the empty list to a file
        filename = 'Rectangle.json'
        Rectangle.save_to_file(list_of_objs)
        # Read the saved file
        with open(filename, 'r') as my_file:
            saved_data = my_file.read()
        expected_data = '[]'  # Verify the saved data
        self.assertEqual(saved_data, expected_data)

    def test_save_to_file_none(self):
        # Save None to a file
        filename = 'Rectangle.json'
        Rectangle.save_to_file(None)
        # Read the saved file
        with open(filename, 'r') as my_file:
            saved_data = my_file.read()
        # Verify the saved data
        expected_data = '[]'
        self.assertEqual(saved_data, expected_data)










if __name__ == "__main__":
    unittest.main()
# run with "python3 -m unittest discover test"
