# what if we have multiple test nmethods or cases here like

def test_authentication(browser):
    print("Testing Authentication")

def test_profile(browser):
    print("Testing Profile")

def test_secret(browser):
    print("Testing Secret")

def test_login(browser):
    print("Testing Login")

def test_logout(browser):
    print("Testing Logout")


#so above we have multiple tets cases currently there are 5 , at some point it can be 50 here so in every test case we are passing our fixture name
# so question is cant we optmize this ? we can like i have mentioned in optimize file in folder understand conftestt refer