"""
This module contains a pytest parametrized to check 
the right discounted price from calculate_discounted_price method
"""


import pytest
from discount import calculate_discounted_price

@pytest.mark.parametrize("price, discount, expected", [
    (100, 0.10, 90),
    (100, 0.50, 50),
    (100, 0.00, 100)
])
def test_calculate_discounted_price(price, discount, expected):
    """
    Parametrized test for calculate_discounted_price function.
    Verifies that the function correctly calculates the final price
    for various prices and discount percentages.
    """
    assert calculate_discounted_price(price, discount) == expected
