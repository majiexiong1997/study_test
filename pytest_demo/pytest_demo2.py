import pytest
import yaml



class TestData:
    #string,list,tuple
    @pytest.mark.parametrize('a,b',yaml.safe_load(open("./data.yml")) )
    def test_param(self,a,b):
        print(a + b)

class TestDemo:
    #如果是字典，只读取key
    @pytest.mark.parametrize('env',yaml.safe_load(open("./env")))
    def test_demo(self,env):
        if "test" in env:
            print('这是测试环境')
            print(env["test"])
        if 'dev' in env:
            print('这是开发环境')
