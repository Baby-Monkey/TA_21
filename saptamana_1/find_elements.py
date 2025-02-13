import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
time.sleep(1)
LINK = "https://formy-project.herokuapp.com/form"
driver.get(LINK)
driver.maximize_window()
time.sleep(2)


driver.find_element(By.CSS_SELECTOR, "#checkbox-4").click()

lista_checkbox = driver.find_elements(By.CSS_SELECTOR, '[type="checkbox"]')
print(len(lista_checkbox))

for element in lista_checkbox:
    element.click()
    print(element.is_selected())
    print(element.get_attribute("value"))
    print(element.is_enabled())
    print("\n")


