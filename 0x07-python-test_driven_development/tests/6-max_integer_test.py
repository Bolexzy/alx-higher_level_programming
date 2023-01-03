#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_two_element_list(self):
        self.assertEqual(max_integer([5, 10]), 10)
        self.assertEqual(max_integer([10, 5]), 10)

    def test_ordered_list(self):
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        unordered = [1, 3, 10, 9]
        self.assertEqual(max_integer(unordered), 10)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_repeated_ints(self):
        repeated = [1, 4, 8, 8, 8, 8]
        self.assertEqual(max_integer(repeated), 8)

    def test_max_at_begginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_floats(self):
        floats = [1.5, 3.4, 0.8, 10.8]
        self.assertEqual(max_integer(floats), 10.8)

    def test_ints_and_floats(self):
        mixed = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(mixed), 15.5)
        
    def test_negative_ints(self):
        neg = [-10, -5, -2, -1]
        self.assertEqual(max_integer(neg), -1)

    def test_string(self):
        string = "Boluwatife"
        self.assertEqual(max_integer(string), 'w')

    def test_list_of_strings(self):
        strings = ["Bolwuatife", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        self.assertEqual(max_integer(""), None)

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'key1': 1, 'key2': 2})

    def test_integer_type(self):
        with self.assertRaises(TypeError):
            max_integer(1)
    
    def test_string_and_ints_list(self):
        with self.assertRaises(TypeError):
            max_integer([0, '1'])

if __name__ == '__main__':
  unittest.main()
