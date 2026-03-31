import pytest

@pytest.fixture()
def method_one():
    print("Open Browser")
    yield
    print("browser closed")
def test_method(method_one):
    print("close browser")



#
# HOW WE WILL USE THIS THING IN SELENIUM IS
#
# setup → open browser
# test  → perform actions
# teardown → close browser
