import pytest

@pytest.fixture
def method_one():
    print("Open Browser")
def test_method(method_one):
    print("close browser")


# Simple fixture method without yield
