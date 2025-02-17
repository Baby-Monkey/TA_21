import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.get("https://magento.softwaretestingboard.com/")
driver.maximize_window()
time.sleep(1)
driver.delete_all_cookies()

#Cautam dupa cuvantul backpack si verificam lungimea listei produselor returnate
search_bar = driver.find_element(By.XPATH, "//input[@id='search']")
search_bar.send_keys("backpack")
# search_button = driver.find_element((By.XPATH, "//button[@title='Search']")).click()
search_bar.send_keys(Keys.ENTER)
time.sleep(1)

lista_produse = driver.find_elements(By.XPATH, "//div[@class='product-item-info']")
assert len(lista_produse) >= 5, "S-au gasit mai putin de 5 elemnete"


# Printam pretul produsului cel mai ieftin
lista_elemente_pret = driver.find_elements(By.XPATH,"//span[@class='price']")
lista_valori_pret = []

for pret in lista_elemente_pret:
    lista_valori_pret.append(float(pret.text.strip("$")))

lista_valori_pret.sort()
print(lista_valori_pret[0])

# Sortam produsele dupa pret crescator si validam ca s-a sortat corect in pagina



driver.quit()
