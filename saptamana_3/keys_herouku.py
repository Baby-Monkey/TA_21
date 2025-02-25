import random
import time
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestKeys(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/key_presses")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_key(self):
        input_box = self.driver.find_element(By.ID, "target")
        expected_message = self.driver.find_element(By.ID, "result")

        input_box.send_keys(Keys.DELETE)
        time.sleep(1)
        self.assertEqual("You entered: DELET", expected_message.text, "Message are different")

        input_box.send_keys("Test")
        time.sleep(1)
        input_box.send_keys(Keys.CONTROL, "a")
        input_box.send_keys(Keys.BACKSPACE)
        self.assertEqual("You entered: BACK_SPACE", expected_message.text, "Message are different")

        random_nr = str(random.randint(0, 99999999))
        input_box.send_keys("Test" + random_nr)
        self.assertEqual("You entered: " + random_nr[-1], expected_message.text, "Message are different")