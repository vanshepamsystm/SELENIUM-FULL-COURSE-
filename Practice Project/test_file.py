import json

from Sign import LoginPage
from inventory import InventoryPage
from cart_page import CartPage
import pytest

path = 'C:\\Users\\VanshAhuja\\PycharmProjects\\PythonTesting\\Practice Project\\file.json'

with open(path) as f:
    test_data = json.load(f)
    test_list = test_data['data']

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_credentials", test_list)
def test_add_product_to_cart(browserInstance,test_list_credentials):
    driver = browserInstance

    login_page = LoginPage(driver)
    login_page.login(test_list_credentials['userEmail'], test_list_credentials['userPassword'])

    inventory_page = InventoryPage(driver)
    assert "Products" in inventory_page.get_page_title()

    inventory_page.add_product_to_cart()
    inventory_page.open_cart()

    cart_page = CartPage(driver)
    assert "T-Shirt (Red)" in cart_page.get_cart_item_name()


    '''
    here we have connected json indexes mentioned in file.json to python object mentioned in this file above using load and from python object to pytest parametrization mentioned above and
    using that in function in line 15
    '''