import unittest
import pytest
from api_requests.simple_books_requests import SimpleBooksRequests


class TestGetListOfBooks(unittest.TestCase):

    def test_get_list_of_books_with_no_params(self):
        response = SimpleBooksRequests.get_list_of_books()
        response_json = response.json()
        actual_status_code = response.status_code
        self.assertEqual(200, actual_status_code, "Unexpected status code")
        assert len(response_json) == 6, "Unexpected number of books"

    @pytest.mark.smoke
    def test_get_list_of_books_with_limit(self):
        response = SimpleBooksRequests.get_list_of_books(limit=4)
        self.assertEqual(200, response.status_code, "Unexpected status code")
        assert len(response.json()) == 4, "Unexpected number of books"

    def test_get_list_of_books_with_invalid_limit_less_than_one(self):
        response = SimpleBooksRequests.get_list_of_books(limit=0)
        expected_error_message = "Invalid value for query parameter 'limit'. Must be greater than 1."
        self.assertEqual(400,response.status_code, "Unexpected status code")
        assert expected_error_message == response.json()["error"], "Different response body"

