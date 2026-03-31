import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.youtube.com/")

driver.find_element(By.CLASS_NAME,"ytSearchboxComponentInput").click()
driver.find_element(By.NAME,"search_query").send_keys("Tennis")
driver.find_element(By.CSS_SELECTOR,".ytSearchboxComponentSearchButton").click()
time.sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT,"Dubai 2026").click()
time.sleep(3)