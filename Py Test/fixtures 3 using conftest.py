import pytest
# def test_conf(browser,login):
#     print("work done by user!")


# below is example of multiple stest cases wrapped inside classes
@pytest.mark.usefixtures("browser","login")
class Testexample:
    def test_conf(self):
        print("work done by user1!")
    def test_conf1(self):
        print("work done by user2!")
    def test_conf2(self):
        print("work done by user3!")
    def test_conf3(self):
        print("work done by user4!")
    def test_conf4(self):
        print("work done by user5!")