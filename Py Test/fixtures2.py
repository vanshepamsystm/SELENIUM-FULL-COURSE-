import pytest

@pytest.fixture
def Vansh():
    print("9588199226")
    yield
    print("yield vansh")
@pytest.fixture
def Kriti():
    print("9050600207")
    yield
    print("yield Kriti")
def test_normal():
    print("Hello from normal method")
def test_fixture(Vansh,Kriti):
    print("Hello from test method ")

