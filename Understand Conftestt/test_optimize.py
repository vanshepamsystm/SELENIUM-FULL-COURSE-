import pytest

@pytest.mark.usefixtures("browser")
class Testexample:
    def test_authentication(self):
        print("Testing Authentication")

    def test_profile(self):
        print("Testing Profile")

    def test_secret(self):
        print("Testing Secret")

@pytest.mark.usefixtures("browser")
class Testclasstwo:
    def test_login(self):
        print("Testing Login")

    def test_logout(self):
        print("Testing Logout")
