
from PageObjectModel.checkout import CheckoutPage
from PageObjectModel.country import FinalPage
from PageObjectModel.login import LoginPage
from PageObjectModel.shop import ShopPage


def test_method(browser):
    driver = browser
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    loginPage= LoginPage(driver)
    loginPage.login()

    shoppage = ShopPage(driver)
    shoppage.shop()

    checkoutpage = CheckoutPage(driver)
    checkoutpage.Checkout()

    finalpage = FinalPage(driver)
    finalpage.Lastpage()