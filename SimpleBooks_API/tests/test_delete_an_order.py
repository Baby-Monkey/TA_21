import unittest
from api_requests.simple_books_requests import SimpleBooksRequests


class TestDeleteAnOrder(unittest.TestCase):

    def test_delete_an_order(self):
        book_id = 5
        customer_name = "AutomationTester"
        response_submit_order = SimpleBooksRequests.submit_an_order(book_id, customer_name)
        order_id = response_submit_order.json()["orderId"]
        response = SimpleBooksRequests.delete_an_order(order_id)
        assert response.status_code == 204, "Unexpected status code"
        response_get_order = SimpleBooksRequests.get_an_order(order_id)
        assert response_get_order.status_code == 404, "Unexpected status code"
        expected_error_message = f"No order with id {order_id}."
        assert expected_error_message == response_get_order.json()["error"], "Unexpected error message"
