"""  dsdads """

import requests

def get_price(product_id):
    """
    Fetch the price of a product by calling a web service.

    Args:
        product_id (str): The ID of the product.

    Returns:
        float: The price of the product.
    """
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{product_id}")
    if response.status_code == 200:
        # printing json response
        print(response.json())
        return response.json()
    else:
        print("Error ", response.raise_for_status())
        response.raise_for_status()
