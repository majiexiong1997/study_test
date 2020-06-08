from pytest_demo.cal_demo import Calculator
import pytest
import yaml
cal = Calculator()

cfg = yaml.safe_load(open("cal_test.yml"))



#{'add': [1, 1, 2]}

class TestCal():
    '''加法用例'''

    @pytest.mark.parametrize(('a'), cfg['add'])
    def test_add(self,a,start_message):


        assert a[2] == cal.add(a[0],a[1])
    '''除法'''
    @pytest.mark.parametrize(('a'), cfg['div'])
    def test_div(self,a,start_message):

        assert a[2] == cal.div(a[0],a[1])
    '''乘法'''
    @pytest.mark.parametrize(('a'), cfg['ride'])
    def test_ride(self,a,start_message):

        assert a[2] == cal.ride(a[0],a[1])
    '''减法'''
    @pytest.mark.parametrize(('a'),cfg['cut'])
    def test_cut(self,a,start_message):

        assert a[2] == cal.cut(a[0],a[1])
