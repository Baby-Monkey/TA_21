from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegisterPage(BasePage):
    REGISTER_MESSAGE = (By.XPATH, '//div[@class="result"]')
    INPUT_FIRST_NAME = (By.ID, 'FirstName')
    INPUT_LAST_NAME = (By.ID, 'LastName')
    INPUT_EMAIL = (By.ID, 'Email')
    INPUT_PASSWORD = (By.ID, 'Password')
    INPUT_CONFIRM_PASSWORD = (By.ID, 'ConfirmPassword')
    BUTTON_REGISTER = (By.ID, 'register-button')

    def open(self):
        self.driver.get('https://demo.nopcommerce.com/register')

    def type_first_name(self, text):
        self.type(self.INPUT_FIRST_NAME, text)

    def type_last_name(self, text):
        self.type(self.INPUT_LAST_NAME, text)

    def type_email(self, text):
        self.type(self.INPUT_EMAIL, text)

    def type_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def type_confirm_password(self, text):
        self.type(self.INPUT_CONFIRM_PASSWORD, text)

    def click_register_button(self):
        self.click_element(self.BUTTON_REGISTER)

    def verify_register_message(self, text_message):
        message = self.wait_for_element(self.REGISTER_MESSAGE)
        assert message.is_displayed(), "Button not displayed"
        assert message.text == text_message, "Text not as expected"