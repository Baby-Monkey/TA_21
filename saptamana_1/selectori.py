import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
time.sleep(1)

# LINK = "https://formy-project.herokuapp.com"
# # driver.find_element(By.LINK_TEXT, "Complete Web Form").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Web Form").click()
# time.sleep(2)


LINK = "https://formy-project.herokuapp.com/form"
# deschid URL
driver.get(LINK)
driver.maximize_window()
time.sleep(2)

assert driver.title == "Formy", "Titlul plaginii este diferit de cel asteptat"
header = driver.find_element(By.CSS_SELECTOR, "div.container>h1")
assert header.text == "Complete Web Form", "Headerul este diferit de cel asteptat"


driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Ana")
# time.sleep(1)
# driver.find_element(By.ID, "first-name").clear()
# time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter last name']").send_keys('Ionescu')
time.sleep(1)
driver.find_element(By.ID, "job-title").send_keys("tester")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "input[value='radio-button-3']").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#checkbox-2").click()
time.sleep(1)


# driver.find_element(By.CSS_SELECTOR, "#select-menu").click()
# driver.find_element(By.CSS_SELECTOR, "select#select-menu>option:nth-of-type(2)").click()
# time.sleep(1)

dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#select-menu"))
dropdown.select_by_value("4")
# dropdown.select_by_visible_text("2-4")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '[data-provide="datepicker"]').click()
driver.find_element(By.CSS_SELECTOR, '.today.day').click()
time.sleep(1)

driver.find_element(By.CLASS_NAME, "btn-primary").click()
time.sleep(1)

submit_header = driver.find_element(By.CSS_SELECTOR, "div.container>h1")
message = driver.find_element(By.CSS_SELECTOR, '.alert-success')
assert submit_header.text == "Thanks for submitting your form"
assert message.text == "The form was successfully submitted!"
time.sleep(1)

driver.quit()