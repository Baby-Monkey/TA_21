import unittest
from api_requests.simple_books_requests import SimpleBooksRequests


class TestSumbitOrder(unittest.TestCase):

    def test_sumbit_valid_order(self):
        response = SimpleBooksRequests.submit_an_order(4, "AutomationTester")
        assert response.status_code == 201, "Unexpected status code"
        assert response.json()["created"] == True, "Order not created"

