import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.XPATH,"//a[text()='Click Here']").click()
time.sleep(5)
#method to get windows name
windows = driver.window_handles    #imp
#specified 1 here because parent window is at 0 and child is at 1
driver.switch_to.window(windows[1])    #switching to window
print(driver.find_element(By.XPATH,"//h3").text)

#getting back to parent window which is at index 0
driver.switch_to.window(windows[0])
print(driver.find_element(By.XPATH,"//h3").text)



# we have specified index 0,1 in a order like parent window is opening is first so it is at index 0  and child is at 1
