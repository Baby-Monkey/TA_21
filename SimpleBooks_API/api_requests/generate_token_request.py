import requests
from faker import Faker


def generate_token():
    faker_obj = Faker()
    endpoint = "https://simple-books-api.glitch.me/api-clients/"
    email = faker_obj.email()
    request_body = {
       "clientName": "AutomationTester",
       "clientEmail": email
    }
    response = requests.post(endpoint, json=request_body)
    return response.json()["accessToken"]