from pytest_demo.cal_demo import Calculator
import pytest
import yaml
cal = Calculator()

cfg = yaml.safe_load(open("cal_test.yml"))



#{'add': [1, 1, 2]}

class TestCal():
    '''加法用例'''

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize(('a'), cfg['add'])
    @pytest.mark.dependency()
    def test_add(self,a,start_message):


        assert a[2] == cal.add(a[0],a[1])
    '''除法'''

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize(('a'), cfg['div'])
    @pytest.mark.dependency(depends=["test_ride"])
    def test_div(self,a,start_message):

        assert a[2] == cal.div(a[0],a[1])
    '''乘法'''

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize(('a'), cfg['ride'])
    @pytest.mark.dependency()

    def test_ride(self,a,start_message):

        assert a[2] == cal.ride(a[0],a[1])
    '''减法'''

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize(('a'),cfg['cut'])
    @pytest.mark.dependency(depends=["test_add"])

    def test_cut(self,a,start_message):

        assert a[2] == cal.cut(a[0],a[1])
