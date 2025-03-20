import unittest
from api_requests.simple_books_requests import SimpleBooksRequests


class TestAPIStatus(unittest.TestCase):

    def test_api_status(self):
        response = SimpleBooksRequests.get_api_status()
        actual_status_code = response.status_code
        self.assertEqual(200, actual_status_code, "Unexpected status code")
        response_json = response.json()
        assert response_json["status"] == "OK", "Unexpected status response"

