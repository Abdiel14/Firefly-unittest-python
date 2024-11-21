""" 
This module contains a calculate_discounted_price method 
to check the right discounted price value 
"""

def calculate_discounted_price(price, discount):
    """
    Calculate the final price of a product after applying a discount.

    Args:
        price (float): The original price of the product.
        discount (float): The discount percentage to be applied (0-1).

    Returns:
        float: The final price after applying the discount.
    """
    if not 0 <= discount <= 1:
        raise ValueError("Discount must be between 0 and 1")
    return price * (1 - discount)
