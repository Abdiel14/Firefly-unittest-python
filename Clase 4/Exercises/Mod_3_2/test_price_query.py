# test_price_service.py

import unittest
from unittest.mock import patch
from price_query import get_price

class TestObtainPrice(unittest.TestCase):
    """
    Unit tests for the obtain_price function.
    """

    @patch('price_query.requests.get')
    def test_get_price_value(self, mock_get):
        """
        Test that the obtain_price function returns the correct price
        when the web service returns a successful response.
        """
        # Arrange:
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"price": 20000}
        mock_get.return_value = mock_response
        # Act:
        price = get_price("11")
        # Assert:
        self.assertEqual(price, 20000)

if __name__ == '__main__':
    unittest.main()
