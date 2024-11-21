"""
This module contains Discount price calculator method from discount_calculator.py file, 
checking correct behavior for discount_calculator method
"""
import unittest
from discount_calculator import calculate_discounted_price

class TestCalculateDiscountedPrice(unittest.TestCase):
    """
    Class which contains unit tests for calculate_discounted_price function
    """

    def test_discount_10_percent(self):
        """ Verifying 10 percent item value """
        # Arrange:
        base_price = 100.0
        discount_percentage = 10.0
        expected_price = 90.0
        # Act:
        final_price = calculate_discounted_price(base_price, discount_percentage)
        # Assert:
        self.assertEqual(final_price, expected_price)

    def test_discount_50_percent(self):
        """ Verifying 50 percent item value """
        # Arrange:
        base_price = 100.0
        discount_percentage = 50.0
        expected_price = 50.0
        # Act:
        final_price = calculate_discounted_price(base_price, discount_percentage)
        # Assert:
        self.assertEqual(final_price, expected_price)

    def test_discount_0_percent(self):
        """ Verifying 0 percent item value """
        # Arrange:
        base_price = 100.0
        discount_percentage = 0.0
        expected_price = 100.0
        # Act:
        final_price = calculate_discounted_price(base_price, discount_percentage)
        # Assert:
        self.assertEqual(final_price, expected_price)

if __name__ == '__main__':
    unittest.main()
