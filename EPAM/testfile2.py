import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.epam.com/")
driver.find_element(By.CSS_SELECTOR,"#onetrust-accept-btn-handler").click()
driver.find_element(By.CSS_SELECTOR,".search-icon.dark-icon.header-search__search-icon").click()
driver.find_element(By.ID,"new_form_search").send_keys("Blockchain cloud automation")
driver.find_element(By.CSS_SELECTOR,".bth-text-layer").click()
time.sleep(2)

links = driver.find_element(By.CSS_SELECTOR,".search-results__items").text

assert 'Blockchain' in links
assert 'Cloud' in links
assert 'automation' in links