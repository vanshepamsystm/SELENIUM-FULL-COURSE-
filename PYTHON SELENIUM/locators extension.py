from selenium.webdriver.common.by import By
from selenium import  webdriver
driver = webdriver.Chrome()
import time

driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
# driver.find_element(By.CSS_SELECTOR,"input[type='email']").send_keys("vanshahuja266@gmail.com")
# below is the way of parent child traversal using xpath
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("vanshahuja266@gmail.com")
#below is way of parent child traversal using css selector
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("45677654")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("45677654")
driver.find_element(By.XPATH,"//button[text()= 'Save New Password']").click()

#
# basics diff of css selector and xpath is in traversal is of slash , we give slash in xpath
# and in css instead of slash give space and also css we use nth child thing

time.sleep(5)
