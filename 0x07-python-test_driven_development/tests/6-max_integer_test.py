#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        """ Empty list"""
        self.assertIsNone(max_integer([]), None)
        
    def test_single_element(self):
        """ single element"""
        self.assertEqual(max_integer([3]), 3)

    def test_multiple_element(self):
        """ multiple element"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 1, 2]), 4)


if __name__ == '__main__':
    unittest.main()
