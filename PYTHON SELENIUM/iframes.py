from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://vinothqaacademy.com/iframe/")
driver.switch_to.frame("registeruser")
driver.find_element(By.CSS_SELECTOR,"#vfb-5").send_keys("Vansh")

