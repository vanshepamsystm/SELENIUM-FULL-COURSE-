import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By



@pytest.fixture()
def browser():
    driver = webdriver.Edge()
    driver.implicitly_wait(5)
    yield driver
    driver.close()


def test_lastmessage(browser):
    driver=browser
    driver.get("https://www.saucedemo.com/")
    usernames = driver.find_element(By.XPATH, "//div[@id='login_credentials']").text
    login_usernames = [username for username in usernames.split()]
    driver.find_element(By.ID, "user-name").send_keys(login_usernames[3])

    password = driver.find_element(By.CLASS_NAME, "login_password").text
    login_password = [pw for pw in password.split()]
    driver.find_element(By.ID, "password").send_keys(login_password[4])

    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").click()

    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Vansh")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Ahuja")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("131001")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()
    driver.find_element(By.CSS_SELECTOR, "#finish").click()

    mssg = "Thank you for your!"
    assert mssg == driver.find_element(By.CSS_SELECTOR,".complete-header").text
