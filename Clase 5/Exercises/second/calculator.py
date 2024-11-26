""" Division method file """

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
