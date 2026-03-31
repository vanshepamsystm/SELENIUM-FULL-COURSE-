import pytest

# @pytest.mark.smoke
# @pytest.mark.skip
@pytest.mark.xfail(reason="creditcard not working")
def test_creditcard():
    mssg = "Hello World"
    assert mssg == "Hello","test failed because conditions do not match"

def test_upi():
    a = 4
    b = 4
    assert a == b, "test failed because conditions do not match"