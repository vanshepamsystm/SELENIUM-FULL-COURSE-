import pytest

@pytest.fixture()
def setup():
    print("this statement is coming from setup method")
    yield
    print("this statement is coming after yield statement")
def test_fixture(setup):
    print("this statement is coming from fixture method")