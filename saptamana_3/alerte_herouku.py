import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


# class TestAlert(unittest.TestCase):
from saptamana_3.base_herouku import BaseTest


class TestAlert(BaseTest):
    BUTON_JS_ALERTA_SIMPLU = (By.XPATH, '//button[@onclick="jsAlert()"]')
    BUTON_JS_CONFIRM = (By.CSS_SELECTOR, 'button[onclick = "jsConfirm()"]')
    BUTON_JS_PROMPT = (By.XPATH, '//button[text()="Click for JS Prompt"]')
    MESAJ_RASPUNS = (By.ID, "result")


    def setUp(self):
        super().setUp()
        self.full_url("/javascript_alerts")
        # self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")


    # def evaluate_error_message(self, expected_message, locator, asertion_fail_message):
    #     actual_result = self.driver.find_element(*locator).text
    #     self.assertEqual(expected_message, actual_result, asertion_fail_message)


    # @unittest.skip
    def test_accept_simple_alert(self):
        self.driver.find_element(*self.BUTON_JS_ALERTA_SIMPLU).click()
        js_alert_ok = self.driver.switch_to.alert
        js_alert_ok.accept()

        expected_result = "You successfully clicked an alert"
        # actual_result = self.driver.find_element(*self.MESAJ_RASPUNS).text
        # self.assertEqual(expected_result, actual_result, "Text are not equal")
        self.evaluate_error_message(expected_result, self.MESAJ_RASPUNS, "Text are not equal")


    @unittest.skip
    def test_cancel_alert(self):
        self.driver.find_element(*self.BUTON_JS_CONFIRM).click()
        alerta = self.driver.switch_to.alert
        alerta.dismiss()
        expected_result = "You clicked: Cancel"
        actual_result = self.driver.find_element(*self.MESAJ_RASPUNS).text
        self.assertEqual(expected_result, actual_result, "Text are not equal")


    def test_cancel_alert(self):
        self.driver.find_element(*self.BUTON_JS_PROMPT).click()
        alerta = self.driver.switch_to.alert
        alerta.send_keys("test alerta")
        alerta.accept()

        expected_result = "You entered: test alerta"
        actual_result = self.driver.find_element(*self.MESAJ_RASPUNS).text
        self.assertEqual(expected_result, actual_result, "Text are not equal")
