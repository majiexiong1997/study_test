import pytest




class TestDemo():
    @pytest.mark.dependency()
    def test_demo1(self):
        print('1')

    @pytest.mark.dependency(depends=["test_demo1"])
    def test_demo2(self):
        print('2')