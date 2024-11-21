"""
This module contains a TestFindMax class testing and a find_max method 
from max_finder.py file, checking correct behavior for find_max method
"""

import unittest
from max_finder import find_max

class TestFindMax(unittest.TestCase):
    """
    Unit tests for the find_max function.
    """

    def test_find_max(self):
        """
        Verify that the function correctly identifies the largest number
        in a list of positive integers.
        """
        # Arrange:
        numbers = [1, 2, 3, 4, 5, 6, 7]
        expected = 7
        # Act:
        result = find_max(numbers)
        # Assert:
        self.assertEqual(result, expected)

    def test_find_max_empty_list(self):
        """
        Verify that the function raises a ValueError when the list is empty.
        """
        # Arrange:
        numbers = []
        # Act & Assert:
        with self.assertRaises(ValueError):
            find_max(numbers)

    def test_find_max_not_equal(self):
        """
        Verify that the function does not return a wrong maximum value.
        """
        # Arrange:
        numbers = [1, 2, 3, 4, 5, 6, 7]
        wrong_value = 4
        # Act:
        result = find_max(numbers)
        # Assert:
        self.assertNotEqual(result, wrong_value)

if __name__ == '__main__':
    unittest.main()
