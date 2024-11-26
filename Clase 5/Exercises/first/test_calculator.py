""" Unittest to check sum method with multiple value cases """

import pytest
from calculator import sum_value

def test_suma_positivos():
    """ Testing positive numbers """
    assert sum_value(1, 2) == 3

def test_suma_negativos():
    """ Testing negative numbers """
    assert sum_value(-1, -2) == -3

def test_suma_positivo_negativo():
    """ Testing negative and positive numbers """
    assert sum_value(-1, 2) == 1

def test_suma_flotantes():
    """ Testing float numbers """
    assert sum_value(1.5, 2.5) == 4.0

def test_suma_cero():
    """ Testing zero number values """
    assert sum_value(0, 0) == 0
    assert sum_value(0, 5) == 5
    assert sum_value(-3, 0) == -3
