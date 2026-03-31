import json

import pytest

from OfficialPageObjects.login import LoginPage
from OfficialPageObjects.ShopPage import ShopPage
from OfficialPageObjects.checkout_Confirmation import checkout_Confirmation


def test_framework(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    #loginPage
    loginpage = LoginPage(driver)
    loginpage.login("rahulshetttyacademy","learning")

    #shopPage
    shop_page = ShopPage(driver)
    shop_page.add_to_cart("Blackberry")
    shop_page.go_to_cart()

    # checkout page
    c = checkout_Confirmation(driver)
    c.checkout_page()
    c.address_page()
    c.validate_mssg()