import time
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignIn(unittest.TestCase):

    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.XPATH, '//input[@title="Password"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@class="action login primary"]')
    NON_EXISTENT_ERROR_MESSAGE = (By.XPATH, '//div[@data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
    INVALID_ERROR_MESSAGE = (By.XPATH, '//div[@id="email-error"]')
    EMPTY_EMAIL_ERROR_MESSAGE = (By.ID, 'email-error')
    EMPTY_PASSWORD_ERROR_MESSAGE = (By.ID, 'pass-error')
    EMPTY_ERROR_MESSAGE = (By.XPATH, '//div[@data-bind="html: $parent.prepareMessageForHtml(message.text)"]')

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get('https://magento.softwaretestingboard.com/customer/account/login')
        self.driver.maximize_window()
        # Dezactiveaza validarea nativa a browserului HTML5
        self.driver.execute_script("document.getElementById('login-form').setAttribute('novalidate', 'novalidate')")

    def insert_login_data(self, email, password):
        # sleep(1)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.wait_for_elem(self.SUBMIT_BUTTON)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()


    def evaluate_error_message(self, expected_error_message, error_selector):
        self.wait_for_elem(error_selector)
        actual_error_message = self.driver.find_element(*error_selector).text
        self.assertEqual(expected_error_message, actual_error_message, 'Error message is different')

    def wait_for_elem(self, xpath_selector):
        # Aceasta conditie este indeplinita atunci cand elementul exista in DOM, dar nu garanteaza ca este și vizibil pe ecran
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(xpath_selector))
        # Aceasta conditie este indeplinita atunci cand elementul este prezent in DOM si vizibil pe ecran
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(xpath_selector))

    def test_login_with_non_existing_credentials(self):
        self.insert_login_data('name@email.net', 'non_existing_password123')
        expected_error_message = 'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'
        self.evaluate_error_message(expected_error_message, self.NON_EXISTENT_ERROR_MESSAGE)

    def test_login_with_invalid_credentials(self):
        # If there is no sleep on insert login data error message appears on email field "Please insert @ sign ..."
        self.insert_login_data('namedfasdfasdfasdfa', 'password123')
        expected_error_message = 'Please enter a valid email address (Ex: johndoe@domain.com).'
        message = "Please include an in the email address. 'namedfasdfasdfasdfa' is missing an"
        # element_with_tooltip = self.driver.find_element(By.CSS_SELECTOR, '.tooltip')
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element_with_tooltip).perform()
        self.evaluate_error_message(expected_error_message, self.INVALID_ERROR_MESSAGE)

    def test_login_no_credentials(self):
        self.driver.find_element(By.XPATH, '//button[@class="action login primary"]').click()
        expected_error_message = 'A login and a password are required.'
        # sleep(3)
        self.evaluate_error_message(expected_error_message, self.EMPTY_ERROR_MESSAGE)

    def test_login_no_credentials_fields(self):
        self.insert_login_data("", "")
        expected_error_message = 'This is a required field.'
        # sleep(3)
        self.evaluate_error_message(expected_error_message, self.EMPTY_EMAIL_ERROR_MESSAGE)
        self.evaluate_error_message(expected_error_message, self.EMPTY_PASSWORD_ERROR_MESSAGE)

    def tearDown(self):
        self.driver.quit()
        print('End of test')
