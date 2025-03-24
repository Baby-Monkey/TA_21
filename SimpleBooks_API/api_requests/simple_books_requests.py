from http.client import responses

import requests
from api_requests.generate_token_request import generate_token


class SimpleBooksRequests:
    BASE_URL = "https://simple-books-api.glitch.me"
    API_STATUS_ENDPOINT = "/status"
    BOOKS_ENDPOINT = "/books"
    ORDER_ENDPOINT = "/orders"
    token = generate_token()


    @staticmethod
    def get_api_status():
        endpoint = SimpleBooksRequests.BASE_URL + SimpleBooksRequests.API_STATUS_ENDPOINT
        response = requests.get(endpoint)
        return response

    @staticmethod
    def get_list_of_books(type="", limit=""):
        endpoint = SimpleBooksRequests.BASE_URL + SimpleBooksRequests.BOOKS_ENDPOINT + f"?type={type}&limit={limit}"
        print()
        print("endpoint: ", endpoint)
        response = requests.get(endpoint)
        return response

    @staticmethod
    def submit_an_order(book_id=0, customer_name=""):
        endpoint = SimpleBooksRequests.BASE_URL + SimpleBooksRequests.ORDER_ENDPOINT
        request_headers = {
            "Authorization": f"Bearer {SimpleBooksRequests.token}"
        }
        request_body = {
            "bookId": book_id,
            "customerName": customer_name
        }
        response = requests.post(endpoint, headers=request_headers, json=request_body)
        return response

    @staticmethod
    def get_a_single_book(book_id):
        endpoint = SimpleBooksRequests.BASE_URL + SimpleBooksRequests.BOOKS_ENDPOINT + "/" + str(book_id)
        response = requests.get(endpoint)
        return response

    @staticmethod
    def get_an_order(order_id):
        endpoint = SimpleBooksRequests.BASE_URL + SimpleBooksRequests.ORDER_ENDPOINT + "/" + str(order_id)
        print("endpoint = ", endpoint)
        request_headers = {
            "Authorization": f"Bearer {SimpleBooksRequests.token}"
        }
        response = requests.get(endpoint, headers=request_headers)
        return response

    @staticmethod
    def update_an_order(order_id, customer_name):
        endpoint = SimpleBooksRequests.BASE_URL + SimpleBooksRequests.ORDER_ENDPOINT + "/" + str(order_id)
        request_headers = {
            "Authorization": f"Bearer {SimpleBooksRequests.token}"
        }
        request_body = {
            "customerName": customer_name
        }
        response = requests.patch(endpoint, headers=request_headers, json=request_body)
        return response

    @staticmethod
    def delete_an_order(order_id):
        endpoint = SimpleBooksRequests.BASE_URL + SimpleBooksRequests.ORDER_ENDPOINT + "/" + str(order_id)
        request_headers = {
            "Authorization": f"Bearer {SimpleBooksRequests.token}"
        }
        response = requests.delete(endpoint, headers=request_headers)
        return response
