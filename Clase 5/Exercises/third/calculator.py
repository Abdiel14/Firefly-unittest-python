""" Multiple math methods file """


def sum_value(a, b):
    """
    Return the sum of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    return a + b

def subtract(a, b):
    """
    Return the difference between two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The difference between the two numbers.
    """
    return a - b

def multiply(a, b):
    """
    Return the product of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of the two numbers.
    """
    return a * b

def division(a, b):
    """
    Return the division of two numbers.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The result of the division.

    Raises:
        ValueError: If the divisor is zero.
    """
    if b == 0:
        raise ValueError("Divisor cannot be zero")
    return a / b

def exponent(a, b):
    """
    Return the exponentiation of a number.

    Args:
        a (float): The base number.
        b (float): The exponent.

    Returns:
        float: The result of raising the base to the power of the exponent.
    """
    return a ** b
