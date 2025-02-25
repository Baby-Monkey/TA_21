import unittest

from selenium import webdriver


class BaseTest(unittest.TestCase):

    BASE_URL = "https://the-internet.herokuapp.com"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def evaluate_error_message(self, expected_message, locator, asertion_fail_message):
        actual_result = self.driver.find_element(*locator).text
        self.assertEqual(expected_message, actual_result, asertion_fail_message)

    def full_url(self, path):
        url = f'{self.BASE_URL}{path}'
        self.driver.get(url)
