from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_PAGE_URL = "https://www.saucedemo.com/"
    INPUT_USERNAME = (By.ID, "user-name")
    INPUT_PASSWORD = (By.ID, "password")
    BUTTON_LOGIN = (By.ID, "login-button")


    def open(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def set_username(self, text):
        self.type(self.INPUT_USERNAME, text)

    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def click_login_button(self):
        self.click_element(self.BUTTON_LOGIN)

    def login(self, username, password):
        self.open()
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()
