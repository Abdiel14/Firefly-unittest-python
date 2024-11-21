""" 
This module contains a find_max value method 
to check the higher value from list item values 
"""

def find_max(numbers):
    """
    Return the largest number in a list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The largest number in the list.

    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("The list is empty")
    return max(numbers)
