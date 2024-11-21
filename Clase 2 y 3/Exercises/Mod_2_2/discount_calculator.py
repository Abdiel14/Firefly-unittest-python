""" 
This module contains a calculate discounted price method 
to verify the right discounted price value. 
"""

def calculate_discounted_price(base_price, discount_percentage):
    """
    Calculate the price of an item after applying the discount.

    Args:
        base_price (float): The original price of the item.
        discount_percentage (float): The discount percentage to be applied.

    Returns:
        float: The final price after applying the discount.
    """
    discount_amount = base_price * (discount_percentage / 100)
    return base_price - discount_amount
