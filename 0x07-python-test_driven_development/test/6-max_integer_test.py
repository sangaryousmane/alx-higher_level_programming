#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Test class for our max_integer function"""

    def test_empty_list(self):
        """ Checks for emptiness """
        self.assertIsNone(max_integer([]), None)

    def test_single_element(self):
        """" test for single element"""
        self.assertEqual(max_integer([3]), 3)

    def test_multiple_element(self):
        """ test multiple element"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 1, 2]), 4)


if __name__ == '__main__':
    unittest.main()
