# test_calculadora.py

import pytest
from calculator import sum_value, subtract, multiply, division, exponent

def test_sum():
    """
    Test the suma function to ensure it returns the correct sum.
    """
    assert sum_value(1, 2) == 3

def test_subtract():
    """
    Test the resta function to ensure it returns the correct difference.
    """
    assert subtract(5, 3) == 2

def test_multiply():
    """
    Test the multiplicacion function to ensure it returns the correct product.
    """
    assert multiply(2, 3) == 6

def test_division():
    """
    Test the division function to ensure it returns the correct quotient and handles division by zero.
    """
    assert division(10, 2) == 5
    with pytest.raises(ValueError, match="Divisor cannot be zero"):
        division(10, 0)

def test_exponent():
    """
    Test the exponente function to ensure it returns the correct power result.
    """
    assert exponent(2, 3) == 8
    assert exponent(5, 0) == 1
    assert exponent(1, 5) == 1
    assert exponent(0, 5) == 0
    assert exponent(2, -1) == 0.5
