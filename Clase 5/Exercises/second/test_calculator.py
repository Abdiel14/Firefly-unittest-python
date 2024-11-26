""" Unittest to check division method with multiple value cases """

import pytest
from calculator import division

def test_positive_division():
    """ Testing with positive numbers """
    assert division(10, 2) == 5

def test_division_negativos():
    """ Testing with negative numbers """
    assert division(10, -2) == -5

def test_division_positivo_negativo():
    """ Testing with positive and negative numbers """
    assert division(-10, 2) == -5

def test_division_negativo_positivo():
    """ Testing with negative and positive numbers """
    assert division(10, -2) == -5

def test_division_cero_dividendo():
    """ Testing with zero number values """
    assert division(0, 1) == 0

def test_division_cero_divisor():
    """ Testing with zero number divisor value """
    with pytest.raises(ValueError, match="Divisor cannot be zero"):
        division(10, 0)
