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

    @pytest.mark.xfail(reason="known_issue")
    def test_get_list_of_books_with_invalid_limit_less_than_one(self):
        response = SimpleBooksRequests.get_list_of_books(limit=0)
        expected_error_message = "Invalid value for query parameter 'limit'. Must be greater than 1."
        self.assertEqual(400,response.status_code, "Unexpected status code")
        assert expected_error_message == response.json()["error"], "Different response body"

    @pytest.mark.xfail(reason="known_issue")
    def test_get_list_of_books_with_invalid_limit_minus_one(self):
        response = SimpleBooksRequests.get_list_of_books(limit=-1)
        expected_error_message = "Invalid value for query parameter 'limit'. Must be greater than 1."
        self.assertEqual(400, response.status_code, "Unexpected status code")
        assert expected_error_message == response.json()["error"], "Different response body"

    @pytest.mark.debug
    def test_get_list_of_books_filter_by_limit_and_type(self):
        response = SimpleBooksRequests.get_list_of_books("non-fiction", 3)
        list_of_books = response.json()
        assert response.status_code == 200, "Unexpected response code"
        for book in list_of_books:
            assert book["type"] == "non-fiction", "Wrong type"
        assert len(list_of_books) <= 3, "Too many books"
        print("\nEnd of test\n")

    def test_get_list_of_books_filter_by_type_fiction(self):
        response = SimpleBooksRequests.get_list_of_books(type="fiction")
        list_of_books = response.json()
        assert response.status_code == 200, "Unexpected status code"
        for book in list_of_books:
            assert book["type"] == "fiction", "Wrong type"

