def find_max(numbers):
    """
    It returns the max number from list
    Args: 
        numbers (list): A list of numbers (It may contains integer or float values).
    Returns:
        float: The max number from list. If is the list empty, it returns None value.
    """
    if not numbers:
        return None
    return max(numbers)