import unittest

from api_requests.simple_books_requests import SimpleBooksRequests


class TestGetAnOrder(unittest.TestCase):

    def test_get_an_order_with_valid_id(self):
        book_id = 3
        customer_name = "AutomationTester"
        response_submit_order = SimpleBooksRequests.submit_an_order(book_id, customer_name)
        order_id = response_submit_order.json()["orderId"]
        response = SimpleBooksRequests.get_an_order(order_id)
        assert response.status_code == 200, "Unexpected status code"
        assert response.json()["id"] == order_id, "Unexpected ID"
        assert response.json()["bookId"] == book_id, "Wrong book id"
        assert response.json()["customerName"] == customer_name, "Wrong customer name"
        assert response.json()["quantity"] == 1, "Too many books"
