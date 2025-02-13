import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(1)

LINK = "https://formy-project.herokuapp.com"
# deschid URL
driver.get(LINK)
time.sleep(2)


# driver.find_element(By.LINK_TEXT, "Complete Web Form").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Web Form").click()
time.sleep(2)

driver.quit()