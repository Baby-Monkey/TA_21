from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.XPATH, "//input[@name = 'Password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@class='button-1 login-button']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.message-error ul li")

    def open(self):
        self.driver.get("https://demo.nopcommerce.com/login")

    def set_email(self, email):
        self.type(self.EMAIL_INPUT, email)

    def set_password(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)

    def verify_error_message(self, text_message):
        assert self.find(self.ERROR_MESSAGE).text == text_message