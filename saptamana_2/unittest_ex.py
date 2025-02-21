import unittest


class TestLogin(unittest.TestCase):

    def setUp(self):
        print("Setup method")

    def login_steps(self):
        print("Login steps")

    def test_login_invalid_email(self):
        print("Test case 1")
        self.login_steps()

    def test_login_invalid_fields(self):
        print("Test case 2")

    def tearDown(self):
        print("Teardown method")
