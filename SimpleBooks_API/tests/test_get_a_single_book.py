import unittest

from api_requests.simple_books_requests import SimpleBooksRequests


class TestGetASingleBook(unittest.TestCase):

    def test_get_a_single_book_with_valid_id(self):
        response = SimpleBooksRequests.get_a_single_book(3)
        assert response.status_code == 200, "Unexpected status code"
        assert response.json()["id"] == 3, "Wrong book"