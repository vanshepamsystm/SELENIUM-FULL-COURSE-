from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///C:/Users/VanshAhuja/Desktop/practice.html")

driver.find_element(By.ID,"name").send_keys("Vansh")

#custom xpath  //input [@type ='text']
#custom css   input[type = 'text'] ... no need of // and @ thats it , #id for css
driver.find_element(By.CSS_SELECTOR,"input[id='phone']").send_keys("9588199226")

driver.find_element(By.ID,"male").click()


driver.find_element(By.XPATH,"//button[@type='submit']").click()

message = driver.find_element(By.ID,"successMsg").text

print(message)
assert "Successful" in message
time.sleep(7)



# short cut to make class a css selector = .classname
