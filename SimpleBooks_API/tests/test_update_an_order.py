import unittest
from pprint import pprint

from api_requests.simple_books_requests import SimpleBooksRequests


class TestUpdateAnOrder(unittest.TestCase):

    def test_update_order_with_valid_order_id(self):
        book_id = 4
        customer_name = "AutomationTester"
        response_submit_order = SimpleBooksRequests.submit_an_order(book_id, customer_name)
        pprint(response_submit_order.json())
        order_id = response_submit_order.json()["orderId"]
        new_customer_name = "PythonAutomationTester"
        response = SimpleBooksRequests.update_an_order(order_id, new_customer_name)
        assert response.status_code == 204, "Unexpected status code"
        response_get_order = SimpleBooksRequests.get_an_order(order_id)
        assert response_get_order.json()["customerName"] == new_customer_name, "Unchanged customer name"

