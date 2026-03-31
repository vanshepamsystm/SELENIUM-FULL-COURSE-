import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.youtube.com/")
time.sleep(2)

driver.find_element(By.NAME,"search_query").send_keys("love me like you do")


driver.switch_to.new_window('tab')

time.sleep(2)