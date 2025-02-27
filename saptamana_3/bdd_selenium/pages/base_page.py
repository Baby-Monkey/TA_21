from browser import Browser


class BasePage(Browser):

    def find(self, locator):
        return self.driver.find_element(*locator)

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def click_element(self, locator):
        self.find(locator).click()
