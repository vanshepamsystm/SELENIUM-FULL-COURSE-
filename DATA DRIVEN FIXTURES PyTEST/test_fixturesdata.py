import pytest
@pytest.mark.usefixtures("dataload")
class Testexample2:
    def test_editprofile(self,dataload):
        print(dataload)
        '''
        to print each data individually
        '''
        print(dataload[0])
        print(dataload[1])
        print(dataload[2])