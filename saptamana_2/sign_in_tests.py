import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SignIn (unittest.TestCase):

    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.XPATH, "//input[ @ title = 'Password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@class='action login primary']")
    # UNEXISTING_ERROR_MESSAGE = (By.XPATH, '//div[@data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
    UNEXISTING_ERROR_MESSAGE = (By.CLASS_NAME, "message-error")
    INVALID_ERROR_MESSAGE = (By.ID, 'email-error')
    EMPTY_EMAIL_ERROR_MESSAGE = (By.ID, 'email-error')
    EMPTY_PAS_ERROR_MESSAGE = (By.ID, 'pass-error')


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get('https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/')
        self.driver.maximize_window()


    def insert_login_data(self, email, password):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def evaluate_error_message(self, expected_error_message, error_selector):
        actual_error_message = self.driver.find_element(*error_selector).text
        self.assertEqual(expected_error_message, actual_error_message, "Error message is different")


    def test_login_with_unexisting_credentials(self):
        # self.driver.find_element(By.ID, "email").send_keys("unexisting_email@gamil.com")
        # self.driver.find_element(By.XPATH, "// input[ @ title = 'Password']").send_keys("unexisting_pass")
        # self.driver.find_element(By.XPATH, "//button[@class='action login primary']").click()
        self.insert_login_data("unexisting_email@gamil.com", "unexisting_pass")
        # time.sleep(3)
        expected_error_message = "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."
        # WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.UNEXISTING_ERROR_MESSAGE))
        # actual_error_message = self.driver.find_element(By.XPATH, '//div[@data-bind="html: $parent.prepareMessageForHtml(message.text)"]').text
        # self.assertEqual(expected_error_message, actual_error_message, "Error message is different")
        self.evaluate_error_message(expected_error_message, self.UNEXISTING_ERROR_MESSAGE)


    def test_login_with_invalid_credentials(self):
        # self.driver.find_element(By.ID, "email").send_keys("unexisting_email")
        # self.driver.find_element(By.XPATH, "// input[ @ title = 'Password']").send_keys("pas")
        # self.driver.find_element(By.XPATH, "//button[@class='action login primary']").click()
        self.insert_login_data("unexisting_email", "pas")
        time.sleep(1)
        expected_error_message = "Please enter a valid email address (Ex: johndoe@domain.com)."
        # actual_error_message = self.driver.find_element(By.ID, 'email-error').text

        # self.assertEqual(expected_error_message, actual_error_message, "Error message is different")
        self.evaluate_error_message(expected_error_message, self.INVALID_ERROR_MESSAGE.text)


    def test_login_with_empty_credentials(self):
        # self.driver.find_element(By.XPATH, "//button[@class='action login primary']").click()
        self.insert_login_data("", "")
        time.sleep(1)
        expected_error_message = "This is a required field."
        # actual_email_error_message = self.driver.find_element(By.ID, 'email-error').text
        # actual_pass_error_message = self.driver.find_element(By.ID, 'pass-error').text
        # self.assertEqual(expected_error_message, actual_email_error_message, "Email error message is different")
        # self.assertEqual(expected_error_message, actual_pass_error_message, "Pass error message is different")
        self.evaluate_error_message(expected_error_message, self.EMPTY_EMAIL_ERROR_MESSAGE)
        self.evaluate_error_message(expected_error_message, self.EMPTY_PAS_ERROR_MESSAGE)



    def tearDown(self):
        self.driver.quit()