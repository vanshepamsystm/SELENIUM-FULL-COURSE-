import time

from selenium import webdriver
from selenium.webdriver import ActionChains    #imp
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(7)

driver.get("https://rahulshettyacademy.com/AutomationPractice/#top")

actions = ActionChains(driver)

#this will hover over that button which will show 2 options reload and top
actions.move_to_element(driver.find_element(By.CSS_SELECTOR,"#mousehover")).perform()

# this is a left  click method of actionn class swhere it is clicking on reload
actions.click(driver.find_element(By.XPATH,"//a[text()='Reload']")).perform()
time.sleep(2)   #just used ro check ui automation
actions.move_to_element(driver.find_element(By.CSS_SELECTOR,"#mousehover")).perform()
actions.context_click(driver.find_element(By.XPATH,"//a[text()='Top']")).perform()
time.sleep(2)
elements = driver.find_elements(By.XPATH,"//div[@class='right-align']//label//input")
for el in elements:
    actions.double_click(el)
actions.perform()
