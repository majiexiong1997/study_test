#pytest 测试框架
import pytest

def inc(x):
    return x + 1

#参数化用例
@pytest.mark.parametrize('a,b',[(1,2),(10,20)])
def test_answer(a,b):
    assert inc(a) == b

def test_answer1():
    assert inc(4) == 5

#传入参数
@pytest.fixture()
def login():
    username = 'jerry'
    return username

class TestDemo:
    def test_a(self,login):
        print(f'ausername = {login}')
    def test_b(self):
        print('b')
    def test_c(self,login):
        print('c')




if __name__ == '__main__':
    pytest.main(['pytest_demo1.py'])
