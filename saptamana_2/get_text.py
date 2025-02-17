import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://formy-project.herokuapp.com/form")
driver.maximize_window()
time.sleep(2)

#NOTA: Selenium lucrează doar cu elemente HTML, nu cu noduri de text, deci find_element nu poate localiza nodul de text de mai jos
# element = driver.find_element(By.XPATH, "//input[@id='checkbox-1']//following-sibling::text()[normalize-space()='Male']")
element= driver.find_element(By.XPATH, "//input[@id='checkbox-1']/..")
text = element.text.strip()
print(text)

print(driver.find_element(By.XPATH, "//label[@for='job-title']").text)
print(driver.find_element(By.XPATH, "//input[@id='job-title']").get_attribute("placeholder"))

job_title = driver.find_element(By.XPATH, "//input[@id='job-title']")
job_title.send_keys("test")
time.sleep(1)
print("Valoarea introdusa este: ", job_title.get_attribute("value"))

driver.quit()
