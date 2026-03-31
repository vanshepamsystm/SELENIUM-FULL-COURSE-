from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
driver.maximize_window()
time.sleep(5)
driver.get("https://www.youtube.com/")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,".ytSearchboxComponentInputBox").click()
time.sleep(5)
driver.find_element(By.NAME,"search_query").send_keys("Love me Like You Do")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"button[title='Search']").click()
time.sleep(10)
driver.find_element(By.CLASS_NAME,"ytd-video-renderer").click()
time.sleep(10)
