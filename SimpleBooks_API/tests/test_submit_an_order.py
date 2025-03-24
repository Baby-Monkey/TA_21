import unittest
from api_requests.simple_books_requests import SimpleBooksRequests


class TestSubmitOrder(unittest.TestCase):

    def test_submit_valid_order(self):
        response = SimpleBooksRequests.submit_an_order(4, "AutomationTester")
        assert response.status_code == 201, "Unexpected status code"
        assert response.json()["created"] == True, "Order not created"

    def test_submit_invalid_book_id(self):
        response = SimpleBooksRequests.submit_an_order(8, "AutomationTester")
        expected_error_message = "Invalid or missing bookId."
        assert response.status_code == 400, "Unexpected status code"
        assert response.json()["error"] == expected_error_message, "Unexpected error message"
